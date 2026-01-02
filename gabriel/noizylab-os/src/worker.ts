import { RoomDO } from "./room-do";
import { nowISO, randCode, sha256Hex, json, bad, readJson, verifyTurnstile, getIP } from "./utils";
import { aiTriage, aiOk } from "./ai";

export { RoomDO };

type Env = {
  DB: D1Database;
  UPLOADS: R2Bucket;
  ROOMS: DurableObjectNamespace;

  TURNSTILE_SECRET: string;
  APP_NAME: string;

  // AI: external API or Workers AI binding
  AI_BASE_URL?: string;
  AI_API_KEY?: string;
  AI?: Ai;

  // RealtimeKit
  CF_ACCOUNT_ID: string;
  RTK_APP_ID: string;
  CF_API_TOKEN: string;
  RTK_PRESET_STAFF: string;
  RTK_PRESET_CLIENT: string;

  // Stripe
  STRIPE_SECRET_KEY?: string;
  STRIPE_WEBHOOK_SECRET?: string;
};

async function rtkFetch(env: Env, path: string, init: RequestInit) {
  const url = `https://api.cloudflare.com/client/v4/accounts/${env.CF_ACCOUNT_ID}/realtime/kit/${env.RTK_APP_ID}${path}`;
  const r = await fetch(url, {
    ...init,
    headers: {
      "Authorization": `Bearer ${env.CF_API_TOKEN}`,
      "Content-Type": "application/json",
      ...(init.headers || {}),
    },
  });
  if (!r.ok) throw new Error(`RTK API ${r.status}`);
  const data = await r.json<any>();
  if (!data?.success) throw new Error(`RTK: ${JSON.stringify(data?.errors ?? data)}`);
  return data.result;
}

function pickToken(participantResult: any): string {
  // Docs mention token field; UI docs refer to authToken. Support both.
  return participantResult?.token || participantResult?.authToken || participantResult?.auth_token;
}

function route(req: Request) {
  const url = new URL(req.url);
  return { url, path: url.pathname, method: req.method };
}

async function writeEvent(env: Env, ticketId: number, type: string, actorType: string, actorId: string | null, payload: any) {
  await env.DB.prepare(
    "INSERT INTO events (ticket_id, type, actor_type, actor_id, payload_json, created_at) VALUES (?,?,?,?,?,?)"
  ).bind(ticketId, type, actorType, actorId, JSON.stringify(payload ?? null), nowISO()).run();
}

async function getTicketByPublic(env: Env, publicId: string) {
  return await env.DB.prepare("SELECT * FROM tickets WHERE public_id=?").bind(publicId).first<any>();
}

async function staffAuthPlaceholder(req: Request) {
  // Put Cloudflare Access in front of /staff routes.
  // Optionally read JWT headers here later.
  return true;
}

// ALLOWED TAGS (controlled enum - no free-text rot)
const ALLOWED_TAGS = new Set([
  "SLOW_BOOT", "CRASH", "VIRUS", "NO_WIFI", "NO_AUDIO", "NO_VIDEO", "STORAGE_FULL",
  "PASSWORD_CHAOS", "UPDATE_AVOIDER", "BACKUP_NONE",
  "MAC", "WIN", "IPHONE", "ANDROID", "PRINTER",
  "EMAIL", "BROWSER", "OFFICE", "ZOOM", "RECURRING"
]);

function validateTags(tags: string[]): { valid: string[]; invalid: string[] } {
  const valid: string[] = [];
  const invalid: string[] = [];
  for (const t of tags) {
    const upper = t.toUpperCase();
    if (ALLOWED_TAGS.has(upper)) valid.push(upper);
    else invalid.push(t);
  }
  return { valid, invalid };
}

// Check if ticket can close (runbook lock: needs PREVENTION_PLAN_CREATED)
async function canTicketClose(env: Env, ticketId: number): Promise<{ ok: boolean; reason?: string }> {
  const hasPlan = await env.DB.prepare(
    "SELECT 1 FROM events WHERE ticket_id=? AND type='PREVENTION_PLAN_CREATED' LIMIT 1"
  ).bind(ticketId).first<any>();
  if (!hasPlan) return { ok: false, reason: "Missing PREVENTION_PLAN_CREATED event. Run prevention:plan first." };
  return { ok: true };
}

// Generate fix receipt JSON
async function generateFixReceipt(env: Env, ticketId: number, invoiceId: number) {
  const ticket = await env.DB.prepare("SELECT * FROM tickets WHERE id=?").bind(ticketId).first<any>();
  const events = await env.DB.prepare(
    "SELECT type, payload_json, created_at FROM events WHERE ticket_id=? ORDER BY id ASC"
  ).bind(ticketId).all<any>();
  
  const evList = events.results ?? [];
  
  // Extract key info
  const created = evList.find((e: any) => e.type === "CREATED");
  const triaged = evList.find((e: any) => e.type === "AUTO_TAGS");
  const planCreated = evList.find((e: any) => e.type === "PREVENTION_PLAN_CREATED");
  const estimateApproved = evList.find((e: any) => e.type === "ESTIMATE_APPROVED");
  const paymentConfirmed = evList.find((e: any) => e.type === "PAYMENT_CONFIRMED");
  
  const receipt = {
    ticketId,
    publicId: ticket?.public_id,
    problem: ticket?.subject ?? "Issue resolved",
    solution: "See attached playbook steps and event log.",
    prevention: planCreated ? JSON.parse(planCreated.payload_json || "{}").plan : [],
    timestamps: {
      opened: created?.created_at,
      triaged: triaged?.created_at,
      estimateApproved: estimateApproved?.created_at,
      paid: paymentConfirmed?.created_at,
      closed: nowISO()
    },
    invoiceId
  };
  
  return receipt;
}

async function purgeTicket(env: Env, ticketId: number) {
  // Delete R2 objects for this ticket if you use prefix tickets/<ticketId>/
  // If your key scheme differs, adjust prefix here.
  const prefix = `tickets/${ticketId}/`;

  if (env.UPLOADS) {
    const listed = await env.UPLOADS.list({ prefix });
    for (const obj of listed.objects) {
      await env.UPLOADS.delete(obj.key);
    }
  }

  // Delete DB rows (uploads registry + events + runs, etc.)
  await env.DB.prepare("DELETE FROM uploads WHERE ticket_id=?").bind(ticketId).run();
  await env.DB.prepare("DELETE FROM events WHERE ticket_id=?").bind(ticketId).run();
  await env.DB.prepare("DELETE FROM followups WHERE ticket_id=?").bind(ticketId).run();

  // playbook runs
  const runs = await env.DB.prepare("SELECT id FROM playbook_runs WHERE ticket_id=?").bind(ticketId).all<any>();
  for (const r of (runs.results ?? [])) {
    await env.DB.prepare("DELETE FROM playbook_run_steps WHERE run_id=?").bind(r.id).run();
  }
  await env.DB.prepare("DELETE FROM playbook_runs WHERE ticket_id=?").bind(ticketId).run();

  // billing
  await env.DB.prepare("DELETE FROM invoice_items WHERE invoice_id IN (SELECT id FROM invoices WHERE ticket_id=?)").bind(ticketId).run();
  await env.DB.prepare("DELETE FROM invoices WHERE ticket_id=?").bind(ticketId).run();
  await env.DB.prepare("DELETE FROM payments WHERE ticket_id=?").bind(ticketId).run();
  await env.DB.prepare("DELETE FROM estimates WHERE ticket_id=?").bind(ticketId).run();

  // finally: keep ticket shell but mark it
  await env.DB.prepare("UPDATE tickets SET status='PURGED' WHERE id=?").bind(ticketId).run();
}

async function withIdempotency(env: Env, key: string, route: string, requestHash: string, fn: () => Promise<any>) {
  const hit = await env.DB.prepare(
    "SELECT response_json, request_hash FROM idempotency WHERE key=? AND route=?"
  ).bind(key, route).first<any>();

  if (hit) {
    if (hit.request_hash !== requestHash) throw new Error("Idempotency key reuse with different body");
    return JSON.parse(hit.response_json);
  }

  const res = await fn();
  await env.DB.prepare(
    "INSERT INTO idempotency (key, route, request_hash, response_json, created_at) VALUES (?,?,?,?,?)"
  ).bind(key, route, requestHash, JSON.stringify(res), nowISO()).run();

  return res;
}

// Queue job handlers
async function runRetention(env: Env, limit: number) {
  const now = nowISO();
  const exp = await env.DB.prepare(
    "SELECT ticket_id FROM retention WHERE delete_at <= ? LIMIT ?"
  ).bind(now, limit).all<any>();

  for (const r of (exp.results ?? [])) {
    await purgeTicket(env, r.ticket_id);
    await env.DB.prepare("DELETE FROM retention WHERE ticket_id=?").bind(r.ticket_id).run();
  }
  return { purged: exp.results?.length ?? 0 };
}

async function runFollowups(env: Env, limit: number) {
  const now = nowISO();
  const due = await env.DB.prepare(
    "SELECT id, ticket_id, type, due_at FROM followups WHERE status='scheduled' AND due_at <= ? ORDER BY due_at ASC LIMIT ?"
  ).bind(now, limit).all<any>();

  for (const f of (due.results ?? [])) {
    await env.DB.prepare("UPDATE followups SET status='done' WHERE id=?").bind(f.id).run();
    await writeEvent(env, f.ticket_id, "FOLLOWUP_TRIGGERED", "system", "system", { followupId: f.id, type: f.type, dueAt: f.due_at });
    await writeEvent(env, f.ticket_id, "STATUS_UPDATE", "system", "system", {
      now: "Quick check-in from NoizyLab.",
      next: "Reply with: FIXED / STILL BROKEN / NEW ISSUE.",
      when: "Next update: within 1 business day."
    });
  }
  return { processed: due.results?.length ?? 0 };
}

async function rollupMetrics(env: Env) {
  const now = nowISO();
  const day = now.slice(0, 10);
  const counts = await env.DB.prepare(
    "SELECT type, COUNT(1) AS n FROM events WHERE substr(created_at,1,10)=? GROUP BY type ORDER BY n DESC"
  ).bind(day).all<any>();

  const metrics = { day, topEvents: counts.results ?? [] };

  await env.DB.prepare(
    "INSERT INTO metrics_daily (day, json, created_at) VALUES (?,?,?) ON CONFLICT(day) DO UPDATE SET json=excluded.json"
  ).bind(day, JSON.stringify(metrics), now).run();

  return { day, events: counts.results?.length ?? 0 };
}

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const { url, path, method } = route(req);

    // CORS preflight (zero latency)
    if (method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, PATCH, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type, X-Turnstile-Token, X-Ticket-PublicId, X-Ticket-Secret",
        },
      });
    }

    // Static homepage (optional). In production, serve from Pages.
    if (path === "/" && method === "GET") {
      return new Response(
        `NoizyLab OS API online. Use /public/* endpoints.`,
        { headers: { "Content-Type": "text/plain" } }
      );
    }

    // WebSocket room (zero latency passthrough)
    if (path.startsWith("/ws/room/") && method === "GET") {
      const roomId = path.split("/").pop()!;
      const id = env.ROOMS.idFromName(roomId);
      return env.ROOMS.get(id).fetch(req);
    }

    // --------------------
    // PUBLIC: Create Ticket (optimized: parallel writes)
    // --------------------
    if (path === "/public/tickets" && method === "POST") {
      const [body, ip] = [await readJson(req), getIP(req)];
      if (!body) return bad(400, "Bad JSON");

      const ts = body.turnstileToken as string | undefined;
      if (!ts) return bad(400, "Missing turnstileToken");

      // Verify Turnstile first (blocks bots early)
      const v = await verifyTurnstile(env.TURNSTILE_SECRET, ts, ip);
      if (!v.success) return bad(403, "Turnstile failed");

      const publicId = crypto.randomUUID().slice(0, 8).toUpperCase();
      const secret = crypto.randomUUID();
      const [secretHash, created] = [await sha256Hex(secret), nowISO()];
      const channel = (body.channel ?? "portal") as string;
      const subject = String(body.subject ?? "").slice(0, 200);

      const ins = await env.DB.prepare(
        "INSERT INTO tickets (public_id, status, channel, subject, created_at, updated_at) VALUES (?,?,?,?,?,?)"
      ).bind(publicId, "TRIAGE", channel, subject, created, created).run();

      const ticketId = ins.meta.last_row_id as number;

      // Parallel: access + event writes
      await Promise.all([
        env.DB.prepare("INSERT INTO ticket_access (ticket_id, secret_hash) VALUES (?,?)").bind(ticketId, secretHash).run(),
        writeEvent(env, ticketId, "CREATED", "public", ip ?? null, { channel, subject }),
      ]);

      return json({ ok: true, ticketPublicId: publicId, secret });
    }

    // --------------------
    // PUBLIC: Status page data (optimized: parallel reads)
    // --------------------
    if (path.startsWith("/public/status/") && method === "GET") {
      const publicId = path.split("/").pop()!;
      const secret = url.searchParams.get("secret");
      if (!secret) return bad(401, "Missing secret");

      const t = await getTicketByPublic(env, publicId);
      if (!t) return bad(404, "Not found");

      // Parallel: verify access + fetch events
      const [access, ev, secretHash] = await Promise.all([
        env.DB.prepare("SELECT secret_hash FROM ticket_access WHERE ticket_id=?").bind(t.id).first<any>(),
        env.DB.prepare("SELECT type, actor_type, actor_id, payload_json, created_at FROM events WHERE ticket_id=? ORDER BY id ASC").bind(t.id).all<any>(),
        sha256Hex(secret),
      ]);

      if (!access || access.secret_hash !== secretHash) return bad(403, "Bad secret");

      return json({
        ok: true,
        ticket: {
          publicId: t.public_id,
          status: t.status,
          channel: t.channel,
          subject: t.subject,
          createdAt: t.created_at,
          updatedAt: t.updated_at,
        },
        events: (ev.results ?? []).map((e: any) => ({
          ...e,
          payload: e.payload_json ? JSON.parse(e.payload_json) : null,
        })),
      });
    }

    // --------------------
    // PUBLIC: Upload (optimized: parallel verify + early size check)
    // --------------------
    if (path === "/public/upload" && method === "POST") {
      const turnstileToken = req.headers.get("X-Turnstile-Token") ?? "";
      const publicId = req.headers.get("X-Ticket-PublicId") ?? "";
      const secret = req.headers.get("X-Ticket-Secret") ?? "";
      if (!turnstileToken || !publicId || !secret) return bad(400, "Missing headers");

      // Early size check via Content-Length header
      const contentLength = parseInt(req.headers.get("Content-Length") ?? "0", 10);
      if (contentLength > 15 * 1024 * 1024) return bad(413, "Max 15MB");

      const ip = getIP(req);

      // Parallel: verify turnstile + get ticket
      const [v, t] = await Promise.all([
        verifyTurnstile(env.TURNSTILE_SECRET, turnstileToken, ip),
        getTicketByPublic(env, publicId),
      ]);

      if (!v.success) return bad(403, "Turnstile failed");
      if (!t) return bad(404, "Ticket not found");

      // Verify secret
      const [access, secretHash] = await Promise.all([
        env.DB.prepare("SELECT secret_hash FROM ticket_access WHERE ticket_id=?").bind(t.id).first<any>(),
        sha256Hex(secret),
      ]);
      if (!access || access.secret_hash !== secretHash) return bad(403, "Bad secret");

      const contentType = req.headers.get("Content-Type") ?? "application/octet-stream";
      const blob = await req.arrayBuffer();
      if (blob.byteLength > 15 * 1024 * 1024) return bad(413, "Max 15MB");

      const key = `${publicId}/${Date.now()}-${crypto.randomUUID()}`;

      // Parallel: R2 put + DB insert + event
      await Promise.all([
        env.UPLOADS.put(key, blob, { httpMetadata: { contentType } }),
        env.DB.prepare("INSERT INTO uploads (ticket_id, r2_key, mime, size, created_at) VALUES (?,?,?,?,?)").bind(t.id, key, contentType, blob.byteLength, nowISO()).run(),
        writeEvent(env, t.id, "UPLOAD_ADDED", "public", ip ?? null, { key, mime: contentType, size: blob.byteLength }),
      ]);

      return json({ ok: true, key });
    }

    // --------------------
    // PUBLIC: Live join (code -> room token)
    // --------------------
    if (path === "/public/live/join" && method === "POST") {
      const body = await readJson(req);
      if (!body?.code) return bad(400, "Missing code");

      const row = await env.DB.prepare(
        "SELECT room_id, expires_at FROM live_rooms WHERE code=?"
      ).bind(String(body.code).toUpperCase()).first<any>();

      if (!row) return bad(404, "Bad code");
      if (new Date(row.expires_at).getTime() < Date.now()) return bad(410, "Code expired");

      // Simple token: roomId + exp + sig(hash)
      const exp = Date.now() + 10 * 60_000;
      const tokenRaw = `${row.room_id}.${exp}`;
      const tokenSig = await sha256Hex(tokenRaw + ".noizylab");
      const token = `${tokenRaw}.${tokenSig}`;

      return json({
        ok: true,
        roomId: row.room_id,
        wsUrl: `${url.origin}/ws/room/${row.room_id}?token=${token}`,
        exp,
      });
    }

    // --------------------
    // PUBLIC: join RealtimeKit meeting by code (creates participant, returns authToken)
    // --------------------
    if (path === "/public/rtk/join" && method === "POST") {
      const body = await readJson(req);
      const code = String(body?.code ?? "").toUpperCase();
      const name = String(body?.name ?? "Client").slice(0, 60);

      if (!code) return bad(400, "Missing code");

      const row = await env.DB.prepare(
        "SELECT room_id, meeting_id, ticket_id, expires_at FROM live_rooms WHERE code=?"
      ).bind(code).first<any>();

      if (!row) return bad(404, "Bad code");
      if (new Date(row.expires_at).getTime() < Date.now()) return bad(410, "Code expired");
      if (!row.meeting_id) return bad(500, "Meeting not attached");

      const meetingId = row.meeting_id;

      // Add client participant
      const participant = await rtkFetch(env, `/meetings/${meetingId}/participants`, {
        method: "POST",
        body: JSON.stringify({
          name,
          preset_name: env.RTK_PRESET_CLIENT,
          custom_participant_id: crypto.randomUUID(),
        }),
      });

      const authToken = pickToken(participant);
      if (!authToken) return bad(500, "No authToken returned");

      if (row.ticket_id) {
        await writeEvent(env, row.ticket_id, "CLIENT_JOINED", "public", getIP(req) ?? null, {
          roomId: row.room_id,
          meetingId,
          participantId: participant?.id ?? null,
        });
      }

      const exp = Date.now() + 60 * 60_000; // 60 min
      const tokenRaw = `${row.room_id}.${exp}`;
      const tokenSig = await sha256Hex(tokenRaw + ".noizylab");
      const wsToken = `${tokenRaw}.${tokenSig}`;

      const wsUrl = `${url.origin}/ws/room/${row.room_id}?token=${wsToken}`;

      return json({ ok: true, meetingId, authToken, roomId: row.room_id, wsUrl, exp });
    }

    // --------------------
    // STAFF: health check (Access-gated)
    // --------------------
    if (path === "/staff/health" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      // DB ping
      const dbPing = await env.DB.prepare("SELECT 1 AS ok").first<any>();
      const okDb = !!dbPing?.ok;

      return json({
        ok: true,
        app: env.APP_NAME ?? "NoizyLab OS",
        time: nowISO(),
        db: okDb ? "ok" : "fail",
        r2: !!env.UPLOADS ? "bound" : "missing",
        rooms: !!env.ROOMS ? "bound" : "missing"
      });
    }

    // --------------------
    // STAFF: seed playbooks (upsert, replace steps)
    // --------------------
    if (path === "/staff/playbooks/seed" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const playbooks = body?.playbooks;
      if (!Array.isArray(playbooks) || playbooks.length === 0) return bad(400, "Missing playbooks[]");

      let inserted = 0;
      let updated = 0;
      let stepsInserted = 0;

      for (const pb of playbooks) {
        const code = String(pb.code ?? "").trim();
        const name = String(pb.name ?? "").trim();
        if (!code || !name) continue;

        const persona = pb.persona ? String(pb.persona) : null;
        const tagsJson = JSON.stringify(Array.isArray(pb.tags) ? pb.tags : []);

        const existing = await env.DB.prepare("SELECT id FROM playbooks WHERE code=?").bind(code).first<any>();

        if (!existing) {
          const ins = await env.DB.prepare(
            "INSERT INTO playbooks (code, name, persona, tags_json, created_at) VALUES (?,?,?,?,?)"
          ).bind(code, name, persona, tagsJson, nowISO()).run();
          inserted++;
          const playbookId = ins.meta.last_row_id as number;

          const steps = Array.isArray(pb.steps) ? pb.steps : [];
          for (const s of steps) {
            await env.DB.prepare(
              "INSERT INTO playbook_steps (playbook_id, os, step_order, title, detail) VALUES (?,?,?,?,?)"
            ).bind(playbookId, String(s.os ?? "both"), Number(s.order ?? 1), String(s.title ?? ""), String(s.detail ?? "")).run();
            stepsInserted++;
          }
        } else {
          updated++;
          const playbookId = existing.id as number;

          await env.DB.prepare(
            "UPDATE playbooks SET name=?, persona=?, tags_json=? WHERE id=?"
          ).bind(name, persona, tagsJson, playbookId).run();

          // Replace steps
          await env.DB.prepare("DELETE FROM playbook_steps WHERE playbook_id=?").bind(playbookId).run();

          const steps = Array.isArray(pb.steps) ? pb.steps : [];
          for (const s of steps) {
            await env.DB.prepare(
              "INSERT INTO playbook_steps (playbook_id, os, step_order, title, detail) VALUES (?,?,?,?,?)"
            ).bind(playbookId, String(s.os ?? "both"), Number(s.order ?? 1), String(s.title ?? ""), String(s.detail ?? "")).run();
            stepsInserted++;
          }
        }
      }

      return json({ ok: true, inserted, updated, stepsInserted });
    }

    // --------------------
    // STAFF: list playbooks (optionally include step counts)
    // --------------------
    if (path === "/staff/playbooks/list" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const rows = await env.DB.prepare(
        "SELECT p.code, p.name, p.persona, p.tags_json, " +
        "(SELECT COUNT(1) FROM playbook_steps s WHERE s.playbook_id=p.id) AS step_count " +
        "FROM playbooks p ORDER BY p.code ASC"
      ).all<any>();

      return json({ ok: true, playbooks: rows.results ?? [] });
    }

    // --------------------
    // STAFF: get a playbook + steps by code (and OS filter)
    // --------------------
    if (path === "/staff/playbooks/get" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const code = url.searchParams.get("code");
      const os = url.searchParams.get("os") ?? "both"; // win/mac/both
      if (!code) return bad(400, "Missing code");

      const pb = await env.DB.prepare(
        "SELECT id, code, name, persona, tags_json FROM playbooks WHERE code=?"
      ).bind(code).first<any>();

      if (!pb) return bad(404, "Playbook not found");

      const steps = await env.DB.prepare(
        "SELECT os, step_order, title, detail FROM playbook_steps " +
        "WHERE playbook_id=? AND (os=? OR os='both') ORDER BY step_order ASC"
      ).bind(pb.id, os).all<any>();

      return json({ ok: true, playbook: pb, steps: steps.results ?? [] });
    }

    // --------------------
    // STAFF: mint WS url for a roomId (so staff can listen/chat)
    // --------------------
    if (path === "/staff/ws/url" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const body = await readJson(req);
      const roomId = String(body?.roomId ?? "").trim();
      if (!roomId) return bad(400, "Missing roomId");

      const exp = Date.now() + 60 * 60_000; // 60 min
      const tokenRaw = `${roomId}.${exp}`;
      const tokenSig = await sha256Hex(tokenRaw + ".noizylab");
      const wsToken = `${tokenRaw}.${tokenSig}`;
      const wsUrl = `${url.origin}/ws/room/${roomId}?token=${wsToken}`;

      return json({ ok: true, wsUrl, exp });
    }

    // --------------------
    // STAFF: list tickets
    // --------------------
    if (path === "/staff/tickets" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const status = url.searchParams.get("status") ?? "TRIAGE";
      const q = await env.DB.prepare(
        "SELECT id, public_id, status, channel, subject, created_at, updated_at FROM tickets WHERE status=? ORDER BY id DESC LIMIT 200"
      ).bind(status).all<any>();

      return json({ ok: true, tickets: q.results ?? [] });
    }

    // --------------------
    // STAFF: set status (with runbook lock for CLOSED)
    // --------------------
    if (path.startsWith("/staff/tickets/") && path.endsWith("/status") && method === "PATCH") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const parts = path.split("/");
      const id = Number(parts[3]);
      const body = await readJson(req);
      const status = String(body?.status ?? "");
      if (!id || !status) return bad(400, "Missing id/status");

      // Runbook lock: can't close without PREVENTION_PLAN_CREATED
      if (status === "CLOSED") {
        const check = await canTicketClose(env, id);
        if (!check.ok) return bad(400, check.reason ?? "Cannot close ticket");
      }

      await env.DB.prepare("UPDATE tickets SET status=?, updated_at=? WHERE id=?")
        .bind(status, nowISO(), id).run();

      await writeEvent(env, id, "STATUS_CHANGED", "staff", "staff", { status });

      return json({ ok: true });
    }

    // --------------------
    // STAFF: create live room (code)
    // --------------------
    if (path === "/staff/live/create" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const body = await readJson(req);
      const ticketId = body?.ticketId ? Number(body.ticketId) : null;

      const roomId = crypto.randomUUID();
      const code = randCode(6);
      const expiresAt = new Date(Date.now() + 10 * 60_000).toISOString();

      await env.DB.prepare(
        "INSERT INTO live_rooms (room_id, code, ticket_id, expires_at, created_at) VALUES (?,?,?,?,?)"
      ).bind(roomId, code, ticketId, expiresAt, nowISO()).run();

      if (ticketId) {
        await writeEvent(env, ticketId, "LIVE_SESSION_STARTED", "staff", "staff", { roomId, code, expiresAt });
      }

      return json({ ok: true, roomId, code, expiresAt });
    }

    // --------------------
    // STAFF: start RealtimeKit meeting + return staff authToken + join code
    // --------------------
    if (path === "/staff/rtk/start" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const body = await readJson(req);
      const ticketId = body?.ticketId ? Number(body.ticketId) : null;

      // 1) Create meeting
      const meeting = await rtkFetch(env, `/meetings`, {
        method: "POST",
        body: JSON.stringify({ title: body?.title ?? "NoizyLab Live Help" }),
      });
      const meetingId = meeting.id;

      // 2) Add staff participant (returns token/authToken)
      const staffParticipant = await rtkFetch(env, `/meetings/${meetingId}/participants`, {
        method: "POST",
        body: JSON.stringify({
          name: body?.staffName ?? "NoizyLab Staff",
          preset_name: env.RTK_PRESET_STAFF,
          custom_participant_id: body?.staffId ?? crypto.randomUUID(),
        }),
      });

      const staffAuthToken = pickToken(staffParticipant);
      const staffParticipantId = staffParticipant?.id;

      // 3) Create join code (reuse your live_rooms concept)
      const roomId = crypto.randomUUID();
      const code = randCode(6);
      const expiresAt = new Date(Date.now() + 10 * 60_000).toISOString();

      await env.DB.prepare(
        "INSERT INTO live_rooms (room_id, code, ticket_id, meeting_id, staff_participant_id, expires_at, created_at) VALUES (?,?,?,?,?,?,?)"
      ).bind(roomId, code, ticketId, meetingId, staffParticipantId, expiresAt, nowISO()).run();

      if (ticketId) {
        await writeEvent(env, ticketId, "LIVE_SESSION_STARTED", "staff", "staff", {
          roomId, code, expiresAt, meetingId,
        });
      }

      return json({
        ok: true,
        roomId,
        code,
        expiresAt,
        meetingId,
        staffAuthToken,
      });
    }

    // --------------------
    // STAFF: AI triage (persona/tags/playbook)
    // --------------------
    if (path === "/staff/ai/triage" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const body = await readJson(req);
      const ticketId = Number(body?.ticketId);
      const text = String(body?.text ?? "");
      if (!ticketId || !text) return bad(400, "Missing ticketId/text");

      const result = await aiTriage(env, text);

      await env.DB.prepare(
        "INSERT INTO persona_tags (ticket_id, persona, tags_json, confidence, updated_at) VALUES (?,?,?,?,?) " +
        "ON CONFLICT(ticket_id) DO UPDATE SET persona=excluded.persona, tags_json=excluded.tags_json, confidence=excluded.confidence, updated_at=excluded.updated_at"
      ).bind(ticketId, result.persona ?? null, JSON.stringify(result.tags ?? []), result.confidence ?? null, nowISO()).run();

      await writeEvent(env, ticketId, "AUTO_PERSONA", "ai", "ai", { persona: result.persona, confidence: result.confidence });
      await writeEvent(env, ticketId, "AUTO_TAGS", "ai", "ai", { tags: result.tags, confidence: result.confidence });
      await writeEvent(env, ticketId, "PLAYBOOK_SUGGESTED", "ai", "ai", { playbook: result.playbook, confidence: result.confidence });

      return aiOk(result);
    }

    // --------------------
    // STAFF: AI next-best question (1 question only)
    // --------------------
    if (path === "/staff/ai/next-question" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const ticketId = Number(body?.ticketId);
      const context = String(body?.context ?? "");
      if (!ticketId || !context) return bad(400, "Missing ticketId/context");

      const result = await aiTriage(env, context); // returns persona/tags/question/playbook/calmMessage
      await writeEvent(env, ticketId, "AI_NEXT_QUESTION", "ai", "ai", { question: result.question, confidence: result.confidence });

      return json({ ok: true, question: result.question ?? "", confidence: result.confidence ?? null });
    }

    // --------------------
    // STAFF: AI live notes (5 bullets max)
    // --------------------
    if (path === "/staff/ai/live-notes" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const ticketId = Number(body?.ticketId);
      const transcript = String(body?.transcript ?? "");
      if (!ticketId || !transcript) return bad(400, "Missing ticketId/transcript");

      // Reuse AI endpoint but enforce a strict "notes" output via a small override prompt.
      // If you have AI_BASE_URL configured, swap ai.ts to add a dedicated function; this is the fast path.
      const result = await aiTriage(env, `LIVE NOTES. Output 5 bullets max.\n\n${transcript}`);

      const notes = Array.isArray(result?.calmMessage)
        ? result.calmMessage.slice(0, 5)
        : ["Notes unavailable (AI not configured)."];

      await writeEvent(env, ticketId, "AI_SUMMARY", "ai", "ai", { notes });

      return json({ ok: true, notes });
    }

    // STAFF: create+send estimate (mints public approve/decline links)
    if (path === "/staff/estimate/send" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const ticketId = Number(body?.ticketId);
      const amountCents = Number(body?.amount_cents);
      const currency = String(body?.currency ?? "CAD");
      const summary = String(body?.summary ?? "").slice(0, 240);
      const terms = String(body?.terms ?? "").slice(0, 500);
      const expiresMinutes = Number(body?.expiresMinutes ?? 72 * 60); // 72h default

      if (!ticketId || !Number.isFinite(amountCents) || amountCents <= 0 || !summary) {
        return bad(400, "Missing ticketId/amount_cents/summary");
      }

      const now = nowISO();

      // Create estimate
      const ins = await env.DB.prepare(
        "INSERT INTO estimates (ticket_id, currency, amount_cents, summary, terms, status, created_at, updated_at) " +
        "VALUES (?,?,?,?,?,?,?,?)"
      ).bind(ticketId, currency, amountCents, summary, terms, "sent", now, now).run();

      const estimateId = ins.meta.last_row_id as number;

      await writeEvent(env, ticketId, "ESTIMATE_CREATED", "staff", "staff", { estimateId, amountCents, currency, summary });
      await writeEvent(env, ticketId, "ESTIMATE_SENT", "staff", "staff", { estimateId });

      // Mint tokens
      const approveToken = crypto.randomUUID().replace(/-/g, "");
      const declineToken = crypto.randomUUID().replace(/-/g, "");
      const expiresAt = new Date(Date.now() + expiresMinutes * 60_000).toISOString();

      const payload = JSON.stringify({ estimateId });

      await env.DB.prepare(
        "INSERT INTO public_actions (token, ticket_id, type, payload_json, expires_at, created_at) VALUES (?,?,?,?,?,?)"
      ).bind(approveToken, ticketId, "estimate_approve", payload, expiresAt, now).run();

      await env.DB.prepare(
        "INSERT INTO public_actions (token, ticket_id, type, payload_json, expires_at, created_at) VALUES (?,?,?,?,?,?)"
      ).bind(declineToken, ticketId, "estimate_decline", payload, expiresAt, now).run();

      const origin = new URL(req.url).origin;
      const approveUrl = `${origin}/public/action/${approveToken}`;
      const declineUrl = `${origin}/public/action/${declineToken}`;

      return json({
        ok: true,
        estimateId,
        amountCents,
        currency,
        approveUrl,
        declineUrl,
        expiresAt
      });
    }

    // PUBLIC: redeem an action token (approve/decline estimate)
    if (path.startsWith("/public/action/") && method === "GET") {
      const token = path.split("/").pop()!;
      if (!token) return bad(400, "Missing token");

      const row = await env.DB.prepare(
        "SELECT token, ticket_id, type, payload_json, expires_at, redeemed_at FROM public_actions WHERE token=?"
      ).bind(token).first<any>();

      if (!row) return bad(404, "Invalid token");
      if (row.redeemed_at) return bad(410, "Token already used");
      if (new Date(row.expires_at).getTime() < Date.now()) return bad(410, "Token expired");

      const payload = row.payload_json ? JSON.parse(row.payload_json) : {};
      const estimateId = Number(payload.estimateId);

      if (!estimateId) return bad(500, "Bad token payload");

      const now = nowISO();

      if (row.type === "estimate_approve") {
        await env.DB.prepare("UPDATE estimates SET status='approved', updated_at=? WHERE id=? AND ticket_id=?")
          .bind(now, estimateId, row.ticket_id).run();
        await writeEvent(env, row.ticket_id, "ESTIMATE_APPROVED", "public", getIP(req) ?? null, { estimateId });
      } else if (row.type === "estimate_decline") {
        await env.DB.prepare("UPDATE estimates SET status='declined', updated_at=? WHERE id=? AND ticket_id=?")
          .bind(now, estimateId, row.ticket_id).run();
        await writeEvent(env, row.ticket_id, "ESTIMATE_DECLINED", "public", getIP(req) ?? null, { estimateId });
      } else {
        return bad(400, "Unsupported action type");
      }

      await env.DB.prepare("UPDATE public_actions SET redeemed_at=? WHERE token=?").bind(now, token).run();

      return json({ ok: true, type: row.type, estimateId });
    }

    // STAFF: stream events for a ticket (SSE)
    if (path === "/staff/events/stream" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const ticketId = Number(url.searchParams.get("ticketId"));
      if (!ticketId) return bad(400, "Missing ticketId");

      let lastId = Number(url.searchParams.get("afterId") ?? 0);

      const encoder = new TextEncoder();
      const stream = new ReadableStream({
        async start(controller) {
          controller.enqueue(encoder.encode("retry: 1500\n\n"));
          while (true) {
            const rows = await env.DB.prepare(
              "SELECT id, ts, type, actor, ip, meta_json FROM events WHERE ticket_id=? AND id>? ORDER BY id ASC LIMIT 50"
            ).bind(ticketId, lastId).all<any>();

            const evs = rows.results ?? [];
            for (const e of evs) {
              lastId = e.id;
              const data = JSON.stringify(e);
              controller.enqueue(encoder.encode(`id: ${e.id}\nevent: ${e.type}\ndata: ${data}\n\n`));
            }
            // heartbeat
            controller.enqueue(encoder.encode(`event: ping\ndata: ${Date.now()}\n\n`));
            await new Promise(r => setTimeout(r, 1500));
          }
        }
      });

      return new Response(stream, {
        headers: {
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive"
        }
      });
    }

    // STAFF: send a 3-line status update (NOW/NEXT/WHEN)
    if (path === "/staff/status/send" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const ticketId = Number(body?.ticketId);
      const nowLine = String(body?.now ?? "").slice(0, 160);
      const nextLine = String(body?.next ?? "").slice(0, 160);
      const whenLine = String(body?.when ?? "").slice(0, 160);

      if (!ticketId || !nowLine || !nextLine || !whenLine) {
        return bad(400, "Need ticketId + now + next + when");
      }

      await writeEvent(env, ticketId, "STATUS_UPDATE", "staff", "staff", {
        now: nowLine,
        next: nextLine,
        when: whenLine
      });

      return json({ ok: true });
    }

    // STAFF: close invoice for ticket (creates invoice + items, logs)
    if (path === "/staff/invoice/close" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const ticketId = Number(body?.ticketId);
      const currency = String(body?.currency ?? "CAD");
      const items = Array.isArray(body?.items) ? body.items : [];
      const taxRate = Number(body?.taxRate ?? 0.13); // HST default (Ontario)
      if (!ticketId || items.length === 0) return bad(400, "Need ticketId + items[]");

      const now = nowISO();
      const invIns = await env.DB.prepare(
        "INSERT INTO invoices (ticket_id, status, currency, created_at, updated_at) VALUES (?,?,?,?,?)"
      ).bind(ticketId, "draft", currency, now, now).run();
      const invoiceId = invIns.meta.last_row_id as number;

      let subtotal = 0;
      for (const it of items) {
        const label = String(it.label ?? "").slice(0, 160);
        const qty = Number(it.qty ?? 1);
        const amount = Number(it.amount_cents ?? 0);
        if (!label || qty <= 0 || amount <= 0) continue;
        subtotal += qty * amount;
        await env.DB.prepare(
          "INSERT INTO invoice_items (invoice_id, label, qty, amount_cents, created_at) VALUES (?,?,?,?,?)"
        ).bind(invoiceId, label, qty, amount, now).run();
      }

      const tax = Math.round(subtotal * taxRate);
      const total = subtotal + tax;

      await env.DB.prepare(
        "UPDATE invoices SET subtotal_cents=?, tax_cents=?, total_cents=?, updated_at=? WHERE id=?"
      ).bind(subtotal, tax, total, now, invoiceId).run();

      await writeEvent(env, ticketId, "INVOICE_CREATED", "staff", "staff", { invoiceId, subtotal, tax, total, currency });
      return json({ ok: true, invoiceId, subtotal_cents: subtotal, tax_cents: tax, total_cents: total, currency });
    }

    // STAFF: metrics top hotspots (simple)
    if (path === "/staff/metrics/top" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const days = Number(url.searchParams.get("days") ?? 30);

      const since = new Date(Date.now() - days * 86400_000).toISOString();
      const rows = await env.DB.prepare(
        "SELECT type, COUNT(1) as n FROM events WHERE ts >= ? GROUP BY type ORDER BY n DESC LIMIT 20"
      ).bind(since).all<any>();

      return json({ ok: true, days, topEvents: rows.results ?? [] });
    }

    // STAFF: set client profile
    if (path === "/staff/client/profile/set" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const clientId = Number(body?.clientId);
      const traits = Array.isArray(body?.traits) ? body.traits.slice(0, 12) : [];
      const commsMode = String(body?.commsMode ?? "calm"); // calm|direct
      if (!clientId) return bad(400, "Missing clientId");

      const now = nowISO();
      await env.DB.prepare(
        "INSERT INTO client_profiles (client_id, traits_json, comms_mode, created_at, updated_at) VALUES (?,?,?,?,?) " +
        "ON CONFLICT(client_id) DO UPDATE SET traits_json=excluded.traits_json, comms_mode=excluded.comms_mode, updated_at=excluded.updated_at"
      ).bind(clientId, JSON.stringify(traits), commsMode, now, now).run();

      return json({ ok: true });
    }

    // STAFF: get client profile
    if (path === "/staff/client/profile/get" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const clientId = Number(url.searchParams.get("clientId"));
      if (!clientId) return bad(400, "Missing clientId");

      const row = await env.DB.prepare("SELECT client_id, traits_json, comms_mode FROM client_profiles WHERE client_id=?")
        .bind(clientId).first<any>();

      return json({ ok: true, profile: row ?? null });
    }

    // STAFF: register device fingerprint
    if (path === "/staff/device/register" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const clientId = body?.clientId ? Number(body.clientId) : null;
      const label = String(body?.label ?? "").slice(0, 100);
      const os = String(body?.os ?? "").toLowerCase();
      const fingerprintInput = String(body?.fingerprintInput ?? "");

      if (!label || !os || !fingerprintInput) return bad(400, "Need label + os + fingerprintInput");

      // Hash fingerprint
      const enc = new TextEncoder().encode(fingerprintInput);
      const hashBuf = await crypto.subtle.digest("SHA-256", enc);
      const fingerprint = [...new Uint8Array(hashBuf)].map(b => b.toString(16).padStart(2, "0")).join("");

      const now = nowISO();

      // Upsert device
      const existing = await env.DB.prepare("SELECT id, client_id FROM devices WHERE fingerprint=?").bind(fingerprint).first<any>();

      if (existing) {
        // Update existing
        await env.DB.prepare("UPDATE devices SET label=?, os=?, client_id=COALESCE(?,client_id) WHERE id=?")
          .bind(label, os, clientId, existing.id).run();
        return json({ ok: true, deviceId: existing.id, fingerprint, isNew: false });
      } else {
        // Insert new
        const ins = await env.DB.prepare(
          "INSERT INTO devices (client_id, label, os, fingerprint, created_at) VALUES (?,?,?,?,?)"
        ).bind(clientId, label, os, fingerprint, now).run();
        return json({ ok: true, deviceId: ins.meta.last_row_id, fingerprint, isNew: true });
      }
    }

    // STAFF: export full case bundle (JSON)
    if (path === "/staff/export/case" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const ticketId = Number(url.searchParams.get("ticketId"));
      if (!ticketId) return bad(400, "Missing ticketId");

      const ticket = await env.DB.prepare("SELECT * FROM tickets WHERE id=?").bind(ticketId).first<any>();
      if (!ticket) return bad(404, "Ticket not found");

      const client = ticket.client_id
        ? await env.DB.prepare("SELECT * FROM clients WHERE id=?").bind(ticket.client_id).first<any>()
        : null;

      const device = ticket.device_id
        ? await env.DB.prepare("SELECT * FROM devices WHERE id=?").bind(ticket.device_id).first<any>()
        : null;

      const profile = client?.id
        ? await env.DB.prepare("SELECT * FROM client_profiles WHERE client_id=?").bind(client.id).first<any>()
        : null;

      const events = await env.DB.prepare(
        "SELECT id, ts, type, actor, ip, meta_json FROM events WHERE ticket_id=? ORDER BY id ASC"
      ).bind(ticketId).all<any>();

      const uploads = await env.DB.prepare(
        "SELECT id, r2_key, filename, content_type, bytes, created_at FROM uploads WHERE ticket_id=? ORDER BY id ASC"
      ).bind(ticketId).all<any>();

      const playbookRuns = await env.DB.prepare(
        "SELECT pr.id AS run_id, pr.status, pr.created_at, pr.updated_at, p.code, p.name " +
        "FROM playbook_runs pr JOIN playbooks p ON p.id=pr.playbook_id WHERE pr.ticket_id=? ORDER BY pr.id ASC"
      ).bind(ticketId).all<any>();

      const runSteps = await env.DB.prepare(
        "SELECT rs.run_id, rs.done, rs.done_at, s.os, s.step_order, s.title, s.detail " +
        "FROM playbook_run_steps rs JOIN playbook_steps s ON s.id=rs.step_id " +
        "WHERE rs.run_id IN (SELECT id FROM playbook_runs WHERE ticket_id=?) " +
        "ORDER BY rs.run_id ASC, s.step_order ASC"
      ).bind(ticketId).all<any>();

      const estimates = await env.DB.prepare(
        "SELECT * FROM estimates WHERE ticket_id=? ORDER BY id ASC"
      ).bind(ticketId).all<any>();

      const payments = await env.DB.prepare(
        "SELECT * FROM payments WHERE ticket_id=? ORDER BY id ASC"
      ).bind(ticketId).all<any>();

      const invoices = await env.DB.prepare(
        "SELECT * FROM invoices WHERE ticket_id=? ORDER BY id ASC"
      ).bind(ticketId).all<any>();

      const invoiceItems = await env.DB.prepare(
        "SELECT ii.* FROM invoice_items ii WHERE ii.invoice_id IN (SELECT id FROM invoices WHERE ticket_id=?) ORDER BY ii.id ASC"
      ).bind(ticketId).all<any>();

      const followups = await env.DB.prepare(
        "SELECT * FROM followups WHERE ticket_id=? ORDER BY due_at ASC"
      ).bind(ticketId).all<any>();

      const bundle = {
        exportedAt: nowISO(),
        ticket,
        client,
        device,
        clientProfile: profile,
        events: events.results ?? [],
        uploads: uploads.results ?? [],
        playbooks: {
          runs: playbookRuns.results ?? [],
          steps: runSteps.results ?? []
        },
        billing: {
          estimates: estimates.results ?? [],
          payments: payments.results ?? [],
          invoices: invoices.results ?? [],
          invoiceItems: invoiceItems.results ?? []
        },
        followups: followups.results ?? []
      };

      await writeEvent(env, ticketId, "CASE_EXPORTED", "staff", "staff", { bytes: JSON.stringify(bundle).length });

      return json({ ok: true, bundle });
    }

    // STAFF: generate prevention plan + schedule followups (D7/D30)
    if (path === "/staff/prevention/plan" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const ticketId = Number(body?.ticketId);
      const os = String(body?.os ?? "both");
      const tags = Array.isArray(body?.tags) ? body.tags.slice(0, 6) : [];
      if (!ticketId) return bad(400, "Missing ticketId");

      const now = new Date();
      const d7 = new Date(now.getTime() + 7 * 86400_000).toISOString();
      const d30 = new Date(now.getTime() + 30 * 86400_000).toISOString();

      const nowIso = nowISO();

      // Schedule followups (idempotent-ish: don't double-add same type if exists)
      const existing = await env.DB.prepare(
        "SELECT type FROM followups WHERE ticket_id=? AND status='scheduled'"
      ).bind(ticketId).all<any>();
      const set = new Set((existing.results ?? []).map((r: any) => r.type));

      if (!set.has("D7")) {
        await env.DB.prepare(
          "INSERT INTO followups (ticket_id, type, due_at, status, created_at) VALUES (?,?,?,?,?)"
        ).bind(ticketId, "D7", d7, "scheduled", nowIso).run();
      }
      if (!set.has("D30")) {
        await env.DB.prepare(
          "INSERT INTO followups (ticket_id, type, due_at, status, created_at) VALUES (?,?,?,?,?)"
        ).bind(ticketId, "D30", d30, "scheduled", nowIso).run();
      }

      // Ultra-practical plan bullets (swap for AI later if desired)
      const plan = [
        "Weekly update window: same day/time, not random.",
        "Storage guard: keep 15% free space minimum.",
        "Browser hygiene: remove unknown extensions; stop fake update sites.",
        "Backup: daily incremental + monthly restore test.",
        "Followups: reply FIXED / STILL BROKEN / NEW ISSUE on day 7 + day 30."
      ];

      await writeEvent(env, ticketId, "PREVENTION_PLAN_CREATED", "staff", "staff", { os, tags, d7, d30, plan });

      return json({ ok: true, plan, followups: [{ type: "D7", dueAt: d7 }, { type: "D30", dueAt: d30 }] });
    }

    // STAFF: ops cron runner (call from CF cron trigger or CLI)
    if (path === "/staff/ops/cron" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const limit = Number(body?.limit ?? 100);

      const nowIso = nowISO();
      let purged = 0;
      let followupsProcessed = 0;

      // 1) Retention purges
      const exp = await env.DB.prepare(
        "SELECT ticket_id FROM retention WHERE delete_at <= ? LIMIT ?"
      ).bind(nowIso, limit).all<any>();

      for (const r of (exp.results ?? [])) {
        purged++;
        await purgeTicket(env, r.ticket_id);
        await env.DB.prepare("DELETE FROM retention WHERE ticket_id=?").bind(r.ticket_id).run();
      }

      // 2) Followups due
      const due = await env.DB.prepare(
        "SELECT id, ticket_id, type, due_at FROM followups WHERE status='scheduled' AND due_at <= ? ORDER BY due_at ASC LIMIT ?"
      ).bind(nowIso, limit).all<any>();

      for (const f of (due.results ?? [])) {
        followupsProcessed++;
        await env.DB.prepare("UPDATE followups SET status='done' WHERE id=?").bind(f.id).run();
        await writeEvent(env, f.ticket_id, "FOLLOWUP_TRIGGERED", "system", "system", { followupId: f.id, type: f.type, dueAt: f.due_at });

        // 3-line default check-in
        await writeEvent(env, f.ticket_id, "STATUS_UPDATE", "system", "system", {
          now: "Quick check-in from NoizyLab.",
          next: "Reply with: FIXED / STILL BROKEN / NEW ISSUE.",
          when: "Next update: within 1 business day."
        });
      }

      // 3) Daily metrics rollup (simple)
      const day = nowIso.slice(0, 10);
      const counts = await env.DB.prepare(
        "SELECT type, COUNT(1) AS n FROM events WHERE substr(ts,1,10)=? GROUP BY type ORDER BY n DESC"
      ).bind(day).all<any>();

      const metrics = { day, topEvents: counts.results ?? [] };

      await env.DB.prepare(
        "INSERT INTO metrics_daily (day, json, created_at) VALUES (?,?,?) ON CONFLICT(day) DO UPDATE SET json=excluded.json"
      ).bind(day, JSON.stringify(metrics), nowIso).run();

      return json({ ok: true, day, purged, followupsProcessed, metrics });
    }

    // STAFF: enqueue a single ops job to the queue
    if (path === "/staff/ops/enqueue" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const type = String(body?.type ?? "retention_purge");
      const limit = Number(body?.limit ?? 200);

      const validTypes = ["retention_purge", "followups_run", "metrics_rollup"];
      if (!validTypes.includes(type)) return bad(400, `Invalid type. Use: ${validTypes.join("|")}`);

      await (env as any).OPS_QUEUE.send({ type, limit });

      return json({ ok: true, queued: { type, limit } });
    }

    // STAFF: list DLQ quarantined jobs
    if (path === "/staff/dlq/list" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const rows = await env.DB.prepare(
        "SELECT id, job_type, payload_json, error_message, created_at FROM dlq_events ORDER BY id DESC LIMIT 100"
      ).all<any>();

      return json({ ok: true, jobs: rows.results ?? [] });
    }

    // --------------------
    // STAFF: Stripe Payment Link (server-side, never expose secrets)
    // --------------------
    if (path === "/staff/payment/stripe/link" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      if (!env.STRIPE_SECRET_KEY) return bad(500, "Stripe not configured");

      const body = await readJson(req);
      const ticketId = Number(body?.ticketId);
      const amountCents = Number(body?.amount_cents);
      const currency = String(body?.currency ?? "cad").toLowerCase();
      const description = String(body?.description ?? `Ticket #${ticketId}`).slice(0, 200);

      if (!ticketId || !Number.isFinite(amountCents) || amountCents <= 0) {
        return bad(400, "Missing ticketId/amount_cents");
      }

      // Create Stripe Checkout Session via REST API
      const stripeUrl = "https://api.stripe.com/v1/checkout/sessions";
      const formData = new URLSearchParams();
      formData.append("mode", "payment");
      formData.append("line_items[0][price_data][currency]", currency);
      formData.append("line_items[0][price_data][unit_amount]", String(amountCents));
      formData.append("line_items[0][price_data][product_data][name]", description);
      formData.append("line_items[0][quantity]", "1");
      formData.append("metadata[ticket_id]", String(ticketId));
      formData.append("success_url", `${new URL(req.url).origin}/public/payment/success?session_id={CHECKOUT_SESSION_ID}`);
      formData.append("cancel_url", `${new URL(req.url).origin}/public/payment/cancel`);

      const stripeRes = await fetch(stripeUrl, {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${env.STRIPE_SECRET_KEY}`,
          "Content-Type": "application/x-www-form-urlencoded"
        },
        body: formData.toString()
      });

      if (!stripeRes.ok) {
        const errText = await stripeRes.text();
        console.error("Stripe error:", errText);
        return bad(502, "Stripe API error");
      }

      const session = await stripeRes.json<any>();
      const sessionId = session.id;
      const paymentUrl = session.url;

      // Record payment intent in DB
      const now = nowISO();
      await env.DB.prepare(
        "INSERT INTO payments (ticket_id, provider, provider_ref, currency, amount_cents, status, created_at, updated_at) VALUES (?,?,?,?,?,?,?,?)"
      ).bind(ticketId, "stripe", sessionId, currency.toUpperCase(), amountCents, "pending", now, now).run();

      await writeEvent(env, ticketId, "PAYMENT_LINK_CREATED", "staff", "staff", {
        provider: "stripe",
        sessionId,
        amountCents,
        currency: currency.toUpperCase()
      });

      return json({ ok: true, sessionId, paymentUrl, amountCents, currency: currency.toUpperCase() });
    }

    // --------------------
    // WEBHOOK: Stripe (raw body + signature verification)
    // --------------------
    if (path === "/webhooks/stripe" && method === "POST") {
      if (!env.STRIPE_WEBHOOK_SECRET) return bad(500, "Stripe webhook not configured");

      const signature = req.headers.get("stripe-signature");
      if (!signature) return bad(400, "Missing stripe-signature header");

      const rawBody = await req.text();

      // Verify signature (Stripe uses t=<timestamp>,v1=<signature>)
      const parts = signature.split(",").reduce((acc, p) => {
        const [k, v] = p.split("=");
        acc[k] = v;
        return acc;
      }, {} as Record<string, string>);

      const timestamp = parts["t"];
      const sig = parts["v1"];
      if (!timestamp || !sig) return bad(400, "Invalid stripe-signature format");

      // Check timestamp tolerance (5 min)
      const tsNum = parseInt(timestamp, 10);
      const now = Math.floor(Date.now() / 1000);
      if (Math.abs(now - tsNum) > 300) return bad(400, "Webhook timestamp too old");

      // Compute expected signature
      const signedPayload = `${timestamp}.${rawBody}`;
      const enc = new TextEncoder();
      const keyData = enc.encode(env.STRIPE_WEBHOOK_SECRET);
      const key = await crypto.subtle.importKey("raw", keyData, { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
      const sigBuf = await crypto.subtle.sign("HMAC", key, enc.encode(signedPayload));
      const expectedSig = [...new Uint8Array(sigBuf)].map(b => b.toString(16).padStart(2, "0")).join("");

      if (sig !== expectedSig) return bad(401, "Invalid signature");

      // Parse event
      let event: any;
      try {
        event = JSON.parse(rawBody);
      } catch {
        return bad(400, "Invalid JSON");
      }

      const eventType = event?.type;
      const sessionObj = event?.data?.object;
      const sessionId = sessionObj?.id;
      const ticketIdStr = sessionObj?.metadata?.ticket_id;
      const ticketId = ticketIdStr ? Number(ticketIdStr) : null;

      // Handle checkout.session.completed
      if (eventType === "checkout.session.completed" && sessionId && ticketId) {
        const nowIso = nowISO();

        // Update payment status
        await env.DB.prepare(
          "UPDATE payments SET status='paid', updated_at=? WHERE provider_ref=?"
        ).bind(nowIso, sessionId).run();

        // Log event
        await writeEvent(env, ticketId, "PAYMENT_CONFIRMED", "webhook", "stripe", {
          sessionId,
          amountTotal: sessionObj?.amount_total,
          currency: sessionObj?.currency?.toUpperCase(),
          customerEmail: sessionObj?.customer_details?.email
      // Ack other events (Stripe expects 200)
      return json({ ok: true, received: true, eventType });
    }

    // --------------------
    // STAFF: POST /staff/followups/run
      return json({ ok: true, queued: { type, limit } });
    }

    // --------------------
    // STAFF: POST /staff/followups/run
    // Runs due followups + returns 3-line check-in drafts
    // --------------------
    if (path === "/staff/followups/run" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const now = nowISO();

      // Find due followups
      const dueQ = await env.DB.prepare(
        "SELECT f.id, f.ticket_id, f.type, f.due_at, t.public_id, t.subject " +
        "FROM followups f JOIN tickets t ON f.ticket_id=t.id " +
        "WHERE f.status='scheduled' AND f.due_at <= ? ORDER BY f.due_at ASC LIMIT 50"
      ).bind(now).all<any>();

      const due = dueQ.results ?? [];
      const processed: any[] = [];

      for (const f of due) {
        // Mark as done
        await env.DB.prepare("UPDATE followups SET status='done' WHERE id=?").bind(f.id).run();

        // Generate 3-line check-in draft
        const draft = {
          now: `Following up on your ${f.type} check-in for ticket ${f.public_id}.`,
          next: `Please reply if you need further assistance.`,
          when: `We'll close this ticket in 7 days if no response.`
        };

        await writeEvent(env, f.ticket_id, "FOLLOWUP_SENT", "system", "system", { followupId: f.id, type: f.type, draft });

        processed.push({
          followupId: f.id,
          ticketId: f.ticket_id,
          publicId: f.public_id,
          subject: f.subject,
          type: f.type,
          dueAt: f.due_at,
          draft
        });
      }

      return json({ ok: true, processed, count: processed.length });
    }

    return bad(404, "No route");
  },

  async scheduled(event: ScheduledController, env: Env, ctx: ExecutionContext) {
    // enqueue 3 jobs every run
    await (env as any).OPS_QUEUE.send({ type: "retention_purge", limit: 200 });
    await (env as any).OPS_QUEUE.send({ type: "followups_run", limit: 200 });
    await (env as any).OPS_QUEUE.send({ type: "metrics_rollup" });
  },

  async queue(batch: MessageBatch<any>, env: Env, ctx: ExecutionContext) {
    for (const msg of batch.messages) {
      try {
        const j = msg.body;
        if (j.type === "retention_purge") await runRetention(env, j.limit ?? 200);
        if (j.type === "followups_run") await runFollowups(env, j.limit ?? 200);
        if (j.type === "metrics_rollup") await rollupMetrics(env);

        msg.ack();
      } catch (e) {
        // retry until max_retries then DLQ
        msg.retry();
      }
    }
  }
};
