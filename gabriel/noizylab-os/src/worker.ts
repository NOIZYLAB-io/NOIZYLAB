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

  AI_BASE_URL: string;
  AI_API_KEY: string;

  CF_ACCOUNT_ID: string;
  RTK_APP_ID: string;
  CF_API_TOKEN: string;
  RTK_PRESET_STAFF: string;
  RTK_PRESET_CLIENT: string;
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
  const data = await r.json<any>();
  if (!data?.success) {
    throw new Error(`RTK API error: ${JSON.stringify(data?.errors ?? data)}`);
  }
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

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const { url, path, method } = route(req);

    // Static homepage (optional). In production, serve from Pages.
    if (path === "/" && method === "GET") {
      return new Response(
        `NoizyLab OS API online. Use /public/* endpoints.`,
        { headers: { "Content-Type": "text/plain" } }
      );
    }

    // WebSocket room
    if (path.startsWith("/ws/room/") && method === "GET") {
      const roomId = path.split("/").pop()!;
      const id = env.ROOMS.idFromName(roomId);
      const stub = env.ROOMS.get(id);
      return stub.fetch(req);
    }

    // --------------------
    // PUBLIC: Create Ticket
    // --------------------
    if (path === "/public/tickets" && method === "POST") {
      const body = await readJson(req);
      if (!body) return bad(400, "Bad JSON");

      const ip = getIP(req);
      const ts = body.turnstileToken as string | undefined;
      if (!ts) return bad(400, "Missing turnstileToken");

      const v = await verifyTurnstile(env.TURNSTILE_SECRET, ts, ip);
      if (!v.success) return bad(403, "Turnstile failed");

      const publicId = crypto.randomUUID().slice(0, 8).toUpperCase();
      const secret = crypto.randomUUID();
      const secretHash = await sha256Hex(secret);

      const created = nowISO();
      const status = "TRIAGE";
      const channel = (body.channel ?? "portal") as string;
      const subject = (body.subject ?? "").slice(0, 200);

      const ins = await env.DB.prepare(
        "INSERT INTO tickets (public_id, status, channel, subject, created_at, updated_at) VALUES (?,?,?,?,?,?)"
      ).bind(publicId, status, channel, subject, created, created).run();

      const ticketId = ins.meta.last_row_id as number;

      await env.DB.prepare(
        "INSERT INTO ticket_access (ticket_id, secret_hash) VALUES (?,?)"
      ).bind(ticketId, secretHash).run();

      await writeEvent(env, ticketId, "CREATED", "public", ip ?? null, { channel, subject });

      return json({ ok: true, ticketPublicId: publicId, secret });
    }

    // --------------------
    // PUBLIC: Status page data
    // --------------------
    if (path.startsWith("/public/status/") && method === "GET") {
      const publicId = path.split("/").pop()!;
      const secret = url.searchParams.get("secret");
      if (!secret) return bad(401, "Missing secret");

      const t = await getTicketByPublic(env, publicId);
      if (!t) return bad(404, "Not found");

      const access = await env.DB.prepare("SELECT secret_hash FROM ticket_access WHERE ticket_id=?")
        .bind(t.id).first<any>();

      const secretHash = await sha256Hex(secret);
      if (!access || access.secret_hash !== secretHash) return bad(403, "Bad secret");

      const ev = await env.DB.prepare(
        "SELECT type, actor_type, actor_id, payload_json, created_at FROM events WHERE ticket_id=? ORDER BY id ASC"
      ).bind(t.id).all<any>();

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
    // PUBLIC: Upload (Worker-proxy to R2) + logs event
    // --------------------
    if (path === "/public/upload" && method === "POST") {
      const ip = getIP(req);
      const turnstileToken = req.headers.get("X-Turnstile-Token") ?? "";
      const publicId = req.headers.get("X-Ticket-PublicId") ?? "";
      const secret = req.headers.get("X-Ticket-Secret") ?? "";

      if (!turnstileToken || !publicId || !secret) return bad(400, "Missing headers");
      const v = await verifyTurnstile(env.TURNSTILE_SECRET, turnstileToken, ip);
      if (!v.success) return bad(403, "Turnstile failed");

      const t = await getTicketByPublic(env, publicId);
      if (!t) return bad(404, "Ticket not found");

      const access = await env.DB.prepare("SELECT secret_hash FROM ticket_access WHERE ticket_id=?")
        .bind(t.id).first<any>();
      const secretHash = await sha256Hex(secret);
      if (!access || access.secret_hash !== secretHash) return bad(403, "Bad secret");

      const contentType = req.headers.get("Content-Type") ?? "application/octet-stream";
      const blob = await req.arrayBuffer();

      // Guardrail: keep uploads small for free-first
      if (blob.byteLength > 15 * 1024 * 1024) return bad(413, "Max 15MB");

      const key = `${publicId}/${Date.now()}-${crypto.randomUUID()}`;
      await env.UPLOADS.put(key, blob, { httpMetadata: { contentType } });

      await env.DB.prepare(
        "INSERT INTO uploads (ticket_id, r2_key, mime, size, created_at) VALUES (?,?,?,?,?)"
      ).bind(t.id, key, contentType, blob.byteLength, nowISO()).run();

      await writeEvent(env, t.id, "UPLOAD_ADDED", "public", ip ?? null, {
        key, mime: contentType, size: blob.byteLength
      });

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
    // STAFF: set status
    // --------------------
    if (path.startsWith("/staff/tickets/") && path.endsWith("/status") && method === "PATCH") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const parts = path.split("/");
      const id = Number(parts[3]);
      const body = await readJson(req);
      const status = String(body?.status ?? "");
      if (!id || !status) return bad(400, "Missing id/status");

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

    return bad(404, "No route");
  },
};
