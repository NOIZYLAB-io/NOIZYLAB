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

// Check if ticket can close (runbook lock: needs PREVENTION_PLAN_CREATED + scheduled followups)
async function canTicketClose(env: Env, ticketId: number): Promise<{ ok: boolean; reason?: string }> {
  const hasPlan = await env.DB.prepare(
    "SELECT 1 FROM events WHERE ticket_id=? AND type='PREVENTION_PLAN_CREATED' LIMIT 1"
  ).bind(ticketId).first<any>();
  if (!hasPlan) return { ok: false, reason: "Missing PREVENTION_PLAN_CREATED event. Run prevention:plan first." };

  const hasFollowups = await env.DB.prepare(
    "SELECT 1 AS ok FROM followups WHERE ticket_id=? AND status='scheduled' LIMIT 1"
  ).bind(ticketId).first<any>();
  if (!hasFollowups?.ok) return { ok: false, reason: "Missing scheduled followups. Schedule followups first." };

  return { ok: true };
}

// Throws if close not allowed (strict version for routes)
async function assertCloseAllowed(env: Env, ticketId: number) {
  const hasPlan = await env.DB.prepare(
    "SELECT 1 AS ok FROM events WHERE ticket_id=? AND type='PREVENTION_PLAN_CREATED' LIMIT 1"
  ).bind(ticketId).first<any>();

  const hasFollowups = await env.DB.prepare(
    "SELECT 1 AS ok FROM followups WHERE ticket_id=? AND status='scheduled' LIMIT 1"
  ).bind(ticketId).first<any>();

  if (!hasPlan?.ok || !hasFollowups?.ok) {
    throw new Error("Close blocked: prevention plan + followups required");
  }
}

// =====================
// HOT ROD HELPERS
// =====================

// Track SLA for new ticket
async function initSlaTracking(env: Env, ticketId: number, slaTargetId: number = 1) {
  await env.DB.prepare(
    "INSERT OR IGNORE INTO sla_tracking (ticket_id, sla_target_id, created_at) VALUES (?,?,?)"
  ).bind(ticketId, slaTargetId, nowISO()).run();
}

// Record first response and check breach
async function recordFirstResponse(env: Env, ticketId: number) {
  const tracking = await env.DB.prepare(
    "SELECT sla_target_id, first_response_at, created_at FROM sla_tracking WHERE ticket_id=?"
  ).bind(ticketId).first<any>();
  if (!tracking || tracking.first_response_at) return null; // already recorded

  const target = await env.DB.prepare(
    "SELECT first_response_mins FROM sla_targets WHERE id=?"
  ).bind(tracking.sla_target_id).first<any>();
  
  const now = nowISO();
  const createdMs = new Date(tracking.created_at).getTime();
  const nowMs = new Date(now).getTime();
  const elapsedMins = (nowMs - createdMs) / 60_000;
  const breached = target && elapsedMins > target.first_response_mins ? 1 : 0;

  await env.DB.prepare(
    "UPDATE sla_tracking SET first_response_at=?, first_response_breached=? WHERE ticket_id=?"
  ).bind(now, breached, ticketId).run();

  return { elapsedMins: Math.round(elapsedMins), breached: !!breached };
}

// Record resolution and check breach
async function recordResolution(env: Env, ticketId: number) {
  const tracking = await env.DB.prepare(
    "SELECT sla_target_id, resolution_at, created_at FROM sla_tracking WHERE ticket_id=?"
  ).bind(ticketId).first<any>();
  if (!tracking || tracking.resolution_at) return null;

  const target = await env.DB.prepare(
    "SELECT resolution_mins FROM sla_targets WHERE id=?"
  ).bind(tracking.sla_target_id).first<any>();

  const now = nowISO();
  const createdMs = new Date(tracking.created_at).getTime();
  const nowMs = new Date(now).getTime();
  const elapsedMins = (nowMs - createdMs) / 60_000;
  const breached = target && elapsedMins > target.resolution_mins ? 1 : 0;

  await env.DB.prepare(
    "UPDATE sla_tracking SET resolution_at=?, resolution_breached=? WHERE ticket_id=?"
  ).bind(now, breached, ticketId).run();

  return { elapsedMins: Math.round(elapsedMins), breached: !!breached };
}

// Update client health score
async function updateClientHealth(env: Env, clientId: number) {
  // Count tickets
  const tickets = await env.DB.prepare(
    "SELECT COUNT(*) AS total, SUM(CASE WHEN status != 'CLOSED' THEN 1 ELSE 0 END) AS open_count, MAX(created_at) AS last_ticket FROM tickets WHERE client_id=?"
  ).bind(clientId).first<any>();

  // Average sentiment
  const sentiment = await env.DB.prepare(
    "SELECT AVG(score) AS avg_score FROM client_sentiment WHERE client_id=?"
  ).bind(clientId).first<any>();

  const total = tickets?.total ?? 0;
  const openCount = tickets?.open_count ?? 0;
  const avgSentiment = sentiment?.avg_score ?? 0;

  // Calculate health: start at 100, deduct for issues
  let health = 100;
  health -= Math.min(30, openCount * 10);           // -10 per open ticket, max -30
  health -= Math.min(20, total > 10 ? 20 : total * 2); // -2 per ticket, max -20
  health += Math.round(avgSentiment * 10);          // sentiment boost/penalty
  health = Math.max(0, Math.min(100, health));

  const riskLevel = health >= 80 ? 'low' : health >= 50 ? 'medium' : health >= 25 ? 'high' : 'critical';

  await env.DB.prepare(
    "INSERT INTO client_health (client_id, health_score, risk_level, total_tickets, open_tickets, avg_sentiment, last_ticket_at, updated_at) " +
    "VALUES (?,?,?,?,?,?,?,?) ON CONFLICT(client_id) DO UPDATE SET health_score=excluded.health_score, risk_level=excluded.risk_level, " +
    "total_tickets=excluded.total_tickets, open_tickets=excluded.open_tickets, avg_sentiment=excluded.avg_sentiment, last_ticket_at=excluded.last_ticket_at, updated_at=excluded.updated_at"
  ).bind(clientId, health, riskLevel, total, openCount, avgSentiment, tickets?.last_ticket ?? null, nowISO()).run();

  return { health, riskLevel, total, openCount, avgSentiment };
}

// Check for duplicate tickets (same client + similar subject in last 7 days)
async function findDuplicates(env: Env, clientId: number, subject: string): Promise<any[]> {
  const sevenDaysAgo = new Date(Date.now() - 7 * 86400_000).toISOString();
  const existing = await env.DB.prepare(
    "SELECT id, public_id, subject, status, created_at FROM tickets WHERE client_id=? AND created_at > ? AND status != 'CLOSED' ORDER BY created_at DESC LIMIT 10"
  ).bind(clientId, sevenDaysAgo).all<any>();

  // Simple keyword matching
  const subjectWords = new Set(subject.toLowerCase().split(/\s+/).filter(w => w.length > 3));
  const matches: any[] = [];

  for (const t of (existing.results ?? [])) {
    const tWords = new Set((t.subject || "").toLowerCase().split(/\s+/).filter((w: string) => w.length > 3));
    const overlap = [...subjectWords].filter(w => tWords.has(w)).length;
    if (overlap >= 2 || (subjectWords.size <= 3 && overlap >= 1)) {
      matches.push(t);
    }
  }
  return matches;
}

// Update activity heatmap
async function updateHeatmap(env: Env) {
  const now = new Date();
  const dayOfWeek = now.getUTCDay();
  const hourOfDay = now.getUTCHours();

  await env.DB.prepare(
    "INSERT INTO activity_heatmap (day_of_week, hour_of_day, ticket_count, updated_at) VALUES (?,?,1,?) " +
    "ON CONFLICT(day_of_week, hour_of_day) DO UPDATE SET ticket_count = ticket_count + 1, updated_at = excluded.updated_at"
  ).bind(dayOfWeek, hourOfDay, nowISO()).run();
}

// Run escalation check
async function runEscalations(env: Env, limit: number) {
  const rules = await env.DB.prepare(
    "SELECT * FROM escalation_rules WHERE active=1 ORDER BY stale_hours ASC"
  ).all<any>();

  let escalated = 0;

  for (const rule of (rules.results ?? [])) {
    const cutoff = new Date(Date.now() - rule.stale_hours * 3600_000).toISOString();
    
    // Find stale tickets not yet escalated by this rule
    const stale = await env.DB.prepare(
      "SELECT t.id FROM tickets t WHERE t.status NOT IN ('CLOSED', 'RESOLVED') AND t.updated_at < ? " +
      "AND NOT EXISTS (SELECT 1 FROM escalations e WHERE e.ticket_id = t.id AND e.rule_id = ?) LIMIT ?"
    ).bind(cutoff, rule.id, limit).all<any>();

    for (const t of (stale.results ?? [])) {
      await env.DB.prepare(
        "INSERT INTO escalations (ticket_id, rule_id, escalated_to, created_at) VALUES (?,?,?,?)"
      ).bind(t.id, rule.id, rule.escalate_to, nowISO()).run();

      await writeEvent(env, t.id, "ESCALATED", "system", "system", {
        rule: rule.name,
        escalatedTo: rule.escalate_to,
        staleHours: rule.stale_hours
      });

      escalated++;
    }
  }

  return { escalated };
}

// Deliver webhooks for event
async function deliverWebhooks(env: Env, eventType: string, ticketId: number, payload: any) {
  const hooks = await env.DB.prepare(
    "SELECT * FROM webhooks WHERE active=1"
  ).all<any>();

  let delivered = 0;

  for (const hook of (hooks.results ?? [])) {
    const events = JSON.parse(hook.events || "[]");
    if (!events.includes(eventType) && !events.includes("*")) continue;

    const body = JSON.stringify({
      event: eventType,
      ticketId,
      payload,
      timestamp: nowISO()
    });

    const headers: Record<string, string> = { "Content-Type": "application/json" };
    
    // HMAC signature if secret configured
    if (hook.secret) {
      const sig = await sha256Hex(hook.secret + body);
      headers["X-NoizyLab-Signature"] = sig;
    }

    let responseCode = 0;
    let responseBody = "";

    try {
      const resp = await fetch(hook.url, { method: "POST", headers, body });
      responseCode = resp.status;
      responseBody = await resp.text().catch(() => "");
    } catch (e: any) {
      responseBody = e.message ?? "fetch error";
    }

    await env.DB.prepare(
      "INSERT INTO webhook_deliveries (webhook_id, event_type, payload_json, response_code, response_body, delivered_at, created_at) VALUES (?,?,?,?,?,?,?)"
    ).bind(hook.id, eventType, body, responseCode, responseBody.slice(0, 1000), nowISO(), nowISO()).run();

    if (responseCode >= 200 && responseCode < 300) delivered++;
  }

  return { delivered, total: hooks.results?.length ?? 0 };
}

// Bulk tag tickets
async function bulkTag(env: Env, ticketIds: number[], tags: string[], actorId: string) {
  const { valid } = validateTags(tags);
  let affected = 0;

  for (const id of ticketIds) {
    const ticket = await env.DB.prepare("SELECT tags_json FROM tickets WHERE id=?").bind(id).first<any>();
    const existing = JSON.parse(ticket?.tags_json || "[]");
    const merged = [...new Set([...existing, ...valid])];
    
    await env.DB.prepare("UPDATE tickets SET tags_json=?, updated_at=? WHERE id=?")
      .bind(JSON.stringify(merged), nowISO(), id).run();
    
    await writeEvent(env, id, "BULK_TAGGED", "staff", actorId, { addedTags: valid });
    affected++;
  }

  await env.DB.prepare(
    "INSERT INTO bulk_ops (operation, ticket_ids, params_json, affected_count, actor_id, created_at) VALUES (?,?,?,?,?,?)"
  ).bind("tag", JSON.stringify(ticketIds), JSON.stringify({ tags: valid }), affected, actorId, nowISO()).run();

  return { affected, tags: valid };
}

// Bulk close tickets
async function bulkClose(env: Env, ticketIds: number[], actorId: string) {
  let affected = 0;
  const skipped: number[] = [];

  for (const id of ticketIds) {
    try {
      await assertCloseAllowed(env, id);
      await env.DB.prepare("UPDATE tickets SET status='CLOSED', updated_at=? WHERE id=?")
        .bind(nowISO(), id).run();
      await writeEvent(env, id, "BULK_CLOSED", "staff", actorId, {});
      await recordResolution(env, id);
      affected++;
    } catch {
      skipped.push(id);
    }
  }

  await env.DB.prepare(
    "INSERT INTO bulk_ops (operation, ticket_ids, params_json, affected_count, actor_id, created_at) VALUES (?,?,?,?,?,?)"
  ).bind("close", JSON.stringify(ticketIds), JSON.stringify({ skipped }), affected, actorId, nowISO()).run();

  return { affected, skipped };
}

// Create ticket from template
async function createFromTemplate(env: Env, templateCode: string, clientId: number | null) {
  const template = await env.DB.prepare(
    "SELECT * FROM ticket_templates WHERE code=?"
  ).bind(templateCode).first<any>();
  if (!template) return null;

  const publicId = crypto.randomUUID().slice(0, 8);
  const now = nowISO();

  const result = await env.DB.prepare(
    "INSERT INTO tickets (public_id, status, channel, subject, client_id, tags_json, created_at, updated_at) VALUES (?,?,?,?,?,?,?,?)"
  ).bind(publicId, "NEW", "template", template.subject, clientId, template.default_tags || "[]", now, now).run();

  const ticketId = result.meta.last_row_id as number;

  // Init SLA tracking
  if (template.sla_target_id) {
    await initSlaTracking(env, ticketId, template.sla_target_id);
  }

  // Auto-apply playbooks
  const playbooks = JSON.parse(template.playbook_codes || "[]");
  for (const code of playbooks) {
    // Queue playbook application (simplified - just log event)
    await writeEvent(env, ticketId, "TEMPLATE_PLAYBOOK_QUEUED", "system", "system", { playbookCode: code });
  }

  await writeEvent(env, ticketId, "CREATED_FROM_TEMPLATE", "system", "system", { templateCode });
  await updateHeatmap(env);

  return { ticketId, publicId, template: templateCode };
}

// Get SLA dashboard stats
async function getSlaStats(env: Env) {
  const stats = await env.DB.prepare(`
    SELECT 
      COUNT(*) AS total,
      SUM(CASE WHEN first_response_breached = 1 THEN 1 ELSE 0 END) AS response_breaches,
      SUM(CASE WHEN resolution_breached = 1 THEN 1 ELSE 0 END) AS resolution_breaches,
      SUM(CASE WHEN first_response_at IS NULL THEN 1 ELSE 0 END) AS awaiting_response
    FROM sla_tracking
  `).first<any>();

  return stats;
}

// Get activity heatmap
async function getHeatmap(env: Env) {
  const data = await env.DB.prepare(
    "SELECT day_of_week, hour_of_day, ticket_count FROM activity_heatmap ORDER BY day_of_week, hour_of_day"
  ).all<any>();

  // Format as 7x24 grid
  const grid: number[][] = Array.from({ length: 7 }, () => Array(24).fill(0));
  for (const row of (data.results ?? [])) {
    grid[row.day_of_week][row.hour_of_day] = row.ticket_count;
  }

  return grid;
}

// =====================================================
// LEGENDARY HELPERS
// =====================================================

// AI-powered triage suggestion
async function aiTriageSuggestion(env: Env, ticketId: number, subject: string, description?: string) {
  const text = `${subject} ${description || ""}`.trim();
  
  // Use existing AI helper or Workers AI
  const prompt = `Analyze this support ticket and suggest:
1. Priority (low/medium/high/urgent)
2. Category tags (from: SLOW_BOOT, CRASH, VIRUS, NO_WIFI, NO_AUDIO, NO_VIDEO, STORAGE_FULL, PASSWORD_CHAOS, UPDATE_AVOIDER, BACKUP_NONE, MAC, WIN, IPHONE, ANDROID, PRINTER, EMAIL, BROWSER, OFFICE, ZOOM, RECURRING)
3. Suggested playbook codes
4. Sentiment (positive/neutral/negative)
5. Brief summary

Ticket: ${text}

Respond in JSON format: {"priority":"medium","tags":["TAG1"],"playbooks":["code1"],"sentiment":"neutral","summary":"..."}`;

  try {
    const result = await aiTriage(env, prompt);
    if (result) {
      const suggestion = typeof result === "string" ? JSON.parse(result) : result;
      
      // Store suggestion
      await env.DB.prepare(
        "INSERT INTO ai_suggestions (ticket_id, type, suggestion_json, confidence, created_at) VALUES (?,?,?,?,?)"
      ).bind(ticketId, "triage", JSON.stringify(suggestion), 0.8, nowISO()).run();
      
      return suggestion;
    }
  } catch (e) {
    // AI failed, return null
  }
  return null;
}

// Knowledge base search
async function searchKnowledgeBase(env: Env, query: string, limit: number = 5) {
  // Simple keyword search (could be enhanced with vector search)
  const words = query.toLowerCase().split(/\s+/).filter(w => w.length > 2);
  if (words.length === 0) return [];
  
  const likeConditions = words.map(() => "(title LIKE ? OR content LIKE ? OR tags_json LIKE ?)").join(" OR ");
  const params = words.flatMap(w => [`%${w}%`, `%${w}%`, `%${w}%`]);
  
  const articles = await env.DB.prepare(
    `SELECT id, slug, title, category, views, helpful_yes, helpful_no FROM kb_articles WHERE status='published' AND (${likeConditions}) ORDER BY views DESC LIMIT ?`
  ).bind(...params, limit).all<any>();
  
  return articles.results ?? [];
}

// Suggest KB articles for ticket
async function suggestArticlesForTicket(env: Env, ticketId: number, subject: string) {
  const articles = await searchKnowledgeBase(env, subject, 3);
  const suggestions: any[] = [];
  
  for (const article of articles) {
    await env.DB.prepare(
      "INSERT OR IGNORE INTO kb_ticket_links (ticket_id, article_id, suggested_by, created_at) VALUES (?,?,?,?)"
    ).bind(ticketId, article.id, "ai", nowISO()).run();
    suggestions.push(article);
  }
  
  return suggestions;
}

// Schedule appointment
async function scheduleAppointment(env: Env, data: {
  ticketId?: number;
  clientId?: number;
  staffId: string;
  title: string;
  description?: string;
  startAt: string;
  endAt: string;
  location?: string;
}) {
  const now = nowISO();
  
  // Check staff availability
  const startDate = new Date(data.startAt);
  const dayOfWeek = startDate.getUTCDay();
  const startTime = startDate.toISOString().slice(11, 16); // HH:MM
  
  const availability = await env.DB.prepare(
    "SELECT * FROM staff_availability WHERE staff_id=? AND day_of_week=? AND is_available=1"
  ).bind(data.staffId, dayOfWeek).first<any>();
  
  if (!availability || startTime < availability.start_time || startTime > availability.end_time) {
    return { ok: false, error: "Staff not available at this time" };
  }
  
  // Check for conflicts
  const conflicts = await env.DB.prepare(
    "SELECT id FROM appointments WHERE staff_id=? AND status IN ('scheduled','confirmed') AND ((start_at <= ? AND end_at > ?) OR (start_at < ? AND end_at >= ?))"
  ).bind(data.staffId, data.startAt, data.startAt, data.endAt, data.endAt).first<any>();
  
  if (conflicts) {
    return { ok: false, error: "Time slot conflict" };
  }
  
  // Check blocked time
  const blocked = await env.DB.prepare(
    "SELECT id FROM staff_blocked_time WHERE staff_id=? AND start_at <= ? AND end_at >= ?"
  ).bind(data.staffId, data.startAt, data.startAt).first<any>();
  
  if (blocked) {
    return { ok: false, error: "Staff has blocked this time" };
  }
  
  const result = await env.DB.prepare(
    "INSERT INTO appointments (ticket_id, client_id, staff_id, title, description, start_at, end_at, location, status, created_at, updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
  ).bind(data.ticketId || null, data.clientId || null, data.staffId, data.title, data.description || null, data.startAt, data.endAt, data.location || "remote", "scheduled", now, now).run();
  
  const appointmentId = result.meta.last_row_id as number;
  
  // Queue reminder notification
  const reminderAt = new Date(new Date(data.startAt).getTime() - 60 * 60_000).toISOString(); // 1 hour before
  if (data.clientId) {
    await env.DB.prepare(
      "INSERT INTO notifications (user_type, user_id, channel, type, title, body, scheduled_at, created_at) VALUES (?,?,?,?,?,?,?,?)"
    ).bind("client", String(data.clientId), "email", "appointment_reminder", "Appointment Reminder", `Your appointment "${data.title}" is in 1 hour`, reminderAt, now).run();
  }
  
  if (data.ticketId) {
    await writeEvent(env, data.ticketId, "APPOINTMENT_SCHEDULED", "staff", data.staffId, {
      appointmentId,
      startAt: data.startAt,
      endAt: data.endAt
    });
  }
  
  return { ok: true, appointmentId };
}

// Get staff available slots
async function getAvailableSlots(env: Env, staffId: string, date: string, durationMins: number = 60) {
  const targetDate = new Date(date);
  const dayOfWeek = targetDate.getUTCDay();
  
  // Get availability for this day
  const availability = await env.DB.prepare(
    "SELECT start_time, end_time FROM staff_availability WHERE staff_id=? AND day_of_week=? AND is_available=1"
  ).bind(staffId, dayOfWeek).first<any>();
  
  if (!availability) return [];
  
  // Get existing appointments
  const dayStart = date + "T00:00:00Z";
  const dayEnd = date + "T23:59:59Z";
  
  const appointments = await env.DB.prepare(
    "SELECT start_at, end_at FROM appointments WHERE staff_id=? AND status IN ('scheduled','confirmed') AND start_at >= ? AND start_at <= ? ORDER BY start_at"
  ).bind(staffId, dayStart, dayEnd).all<any>();
  
  const blocked = await env.DB.prepare(
    "SELECT start_at, end_at FROM staff_blocked_time WHERE staff_id=? AND start_at <= ? AND end_at >= ?"
  ).bind(staffId, dayEnd, dayStart).all<any>();
  
  // Generate available slots
  const slots: { start: string; end: string }[] = [];
  const [startHour, startMin] = availability.start_time.split(":").map(Number);
  const [endHour, endMin] = availability.end_time.split(":").map(Number);
  
  let current = new Date(date + `T${availability.start_time}:00Z`);
  const dayEndTime = new Date(date + `T${availability.end_time}:00Z`);
  
  while (current.getTime() + durationMins * 60_000 <= dayEndTime.getTime()) {
    const slotStart = current.toISOString();
    const slotEnd = new Date(current.getTime() + durationMins * 60_000).toISOString();
    
    // Check conflicts
    let hasConflict = false;
    for (const apt of (appointments.results ?? [])) {
      if (slotStart < apt.end_at && slotEnd > apt.start_at) {
        hasConflict = true;
        break;
      }
    }
    for (const blk of (blocked.results ?? [])) {
      if (slotStart < blk.end_at && slotEnd > blk.start_at) {
        hasConflict = true;
        break;
      }
    }
    
    if (!hasConflict) {
      slots.push({ start: slotStart, end: slotEnd });
    }
    
    current = new Date(current.getTime() + 30 * 60_000); // 30 min increments
  }
  
  return slots;
}

// Send email notification
async function sendEmail(env: Env, to: string, templateCode: string, variables: Record<string, string>) {
  const template = await env.DB.prepare(
    "SELECT * FROM email_templates WHERE code=?"
  ).bind(templateCode).first<any>();
  
  if (!template) return { ok: false, error: "Template not found" };
  
  let subject = template.subject;
  let body = template.body_text;
  
  // Replace variables
  for (const [key, value] of Object.entries(variables)) {
    subject = subject.replace(new RegExp(`{{${key}}}`, "g"), value);
    body = body.replace(new RegExp(`{{${key}}}`, "g"), value);
  }
  
  // Queue notification (actual sending would be via external service)
  await env.DB.prepare(
    "INSERT INTO notifications (user_type, user_id, channel, type, title, body, status, created_at) VALUES (?,?,?,?,?,?,?,?)"
  ).bind("client", to, "email", templateCode, subject, body, "pending", nowISO()).run();
  
  return { ok: true, subject, to };
}

// Process notification queue
async function processNotifications(env: Env, limit: number = 50) {
  const pending = await env.DB.prepare(
    "SELECT * FROM notifications WHERE status='pending' AND (scheduled_at IS NULL OR scheduled_at <= ?) ORDER BY created_at ASC LIMIT ?"
  ).bind(nowISO(), limit).all<any>();
  
  let sent = 0;
  let failed = 0;
  
  for (const notif of (pending.results ?? [])) {
    try {
      // Here you would integrate with actual email/push services
      // For now, just mark as sent
      await env.DB.prepare(
        "UPDATE notifications SET status='sent', sent_at=? WHERE id=?"
      ).bind(nowISO(), notif.id).run();
      sent++;
    } catch {
      await env.DB.prepare(
        "UPDATE notifications SET status='failed' WHERE id=?"
      ).bind(notif.id).run();
      failed++;
    }
  }
  
  return { sent, failed };
}

// Audit log helper
async function auditLog(env: Env, data: {
  actorType: string;
  actorId?: string;
  action: string;
  resourceType: string;
  resourceId?: string;
  changes?: any;
  ip?: string;
  userAgent?: string;
}) {
  await env.DB.prepare(
    "INSERT INTO audit_log (actor_type, actor_id, action, resource_type, resource_id, changes_json, ip_address, user_agent, created_at) VALUES (?,?,?,?,?,?,?,?,?)"
  ).bind(
    data.actorType,
    data.actorId || null,
    data.action,
    data.resourceType,
    data.resourceId || null,
    data.changes ? JSON.stringify(data.changes) : null,
    data.ip || null,
    data.userAgent || null,
    nowISO()
  ).run();
}

// GDPR: Export user data
async function exportUserData(env: Env, clientId: number) {
  const client = await env.DB.prepare("SELECT * FROM clients WHERE id=?").bind(clientId).first<any>();
  const profile = await env.DB.prepare("SELECT * FROM client_profiles WHERE client_id=?").bind(clientId).first<any>();
  const tickets = await env.DB.prepare("SELECT * FROM tickets WHERE client_id=?").bind(clientId).all<any>();
  const devices = await env.DB.prepare("SELECT * FROM devices WHERE client_id=?").bind(clientId).all<any>();
  const appointments = await env.DB.prepare("SELECT * FROM appointments WHERE client_id=?").bind(clientId).all<any>();
  const sentiment = await env.DB.prepare("SELECT * FROM client_sentiment WHERE client_id=?").bind(clientId).all<any>();
  const surveys = await env.DB.prepare(
    "SELECT s.* FROM surveys s JOIN tickets t ON t.id = s.ticket_id WHERE t.client_id=?"
  ).bind(clientId).all<any>();
  
  // Get all events for client's tickets
  const ticketIds = (tickets.results ?? []).map((t: any) => t.id);
  let events: any[] = [];
  for (const tid of ticketIds) {
    const e = await env.DB.prepare("SELECT * FROM events WHERE ticket_id=?").bind(tid).all<any>();
    events = events.concat(e.results ?? []);
  }
  
  return {
    exportedAt: nowISO(),
    client,
    profile,
    tickets: tickets.results ?? [],
    devices: devices.results ?? [],
    appointments: appointments.results ?? [],
    sentiment: sentiment.results ?? [],
    surveys: surveys.results ?? [],
    events
  };
}

// GDPR: Delete user data (right to erasure)
async function deleteUserData(env: Env, clientId: number) {
  const now = nowISO();
  let deleted = { tickets: 0, devices: 0, events: 0, uploads: 0, appointments: 0 };
  
  // Get all ticket IDs
  const tickets = await env.DB.prepare("SELECT id FROM tickets WHERE client_id=?").bind(clientId).all<any>();
  const ticketIds = (tickets.results ?? []).map((t: any) => t.id);
  
  // Delete uploads from R2
  for (const tid of ticketIds) {
    const uploads = await env.DB.prepare("SELECT r2_key FROM uploads WHERE ticket_id=?").bind(tid).all<any>();
    for (const u of (uploads.results ?? [])) {
      if (u.r2_key && env.UPLOADS) {
        await env.UPLOADS.delete(u.r2_key);
        deleted.uploads++;
      }
    }
  }
  
  // Cascade delete from DB
  for (const tid of ticketIds) {
    await env.DB.prepare("DELETE FROM events WHERE ticket_id=?").bind(tid).run();
    await env.DB.prepare("DELETE FROM uploads WHERE ticket_id=?").bind(tid).run();
    await env.DB.prepare("DELETE FROM followups WHERE ticket_id=?").bind(tid).run();
    await env.DB.prepare("DELETE FROM surveys WHERE ticket_id=?").bind(tid).run();
    deleted.events++;
  }
  
  deleted.tickets = ticketIds.length;
  await env.DB.prepare("DELETE FROM tickets WHERE client_id=?").bind(clientId).run();
  
  // Delete appointments
  const appts = await env.DB.prepare("DELETE FROM appointments WHERE client_id=?").bind(clientId).run();
  deleted.appointments = appts.meta.changes ?? 0;
  
  // Delete devices
  const devs = await env.DB.prepare("DELETE FROM devices WHERE client_id=?").bind(clientId).run();
  deleted.devices = devs.meta.changes ?? 0;
  
  // Delete profile and sentiment
  await env.DB.prepare("DELETE FROM client_profiles WHERE client_id=?").bind(clientId).run();
  await env.DB.prepare("DELETE FROM client_sentiment WHERE client_id=?").bind(clientId).run();
  await env.DB.prepare("DELETE FROM client_health WHERE client_id=?").bind(clientId).run();
  
  // Anonymize client record (keep for referential integrity)
  await env.DB.prepare(
    "UPDATE clients SET name='[DELETED]', email='deleted_' || id || '@redacted.local', phone=NULL, updated_at=? WHERE id=?"
  ).bind(now, clientId).run();
  
  return { deleted, anonymizedClientId: clientId };
}

// Generate API key
async function generateApiKey(env: Env, name: string, scopes: string[], createdBy: string, expiresAt?: string) {
  const key = `nlk_${crypto.randomUUID().replace(/-/g, "")}`;
  const prefix = key.slice(0, 12);
  const keyHash = await sha256Hex(key);
  
  await env.DB.prepare(
    "INSERT INTO api_keys (name, key_hash, prefix, scopes_json, expires_at, created_by, created_at) VALUES (?,?,?,?,?,?,?)"
  ).bind(name, keyHash, prefix, JSON.stringify(scopes), expiresAt || null, createdBy, nowISO()).run();
  
  return { key, prefix }; // Return full key only once!
}

// Validate API key
async function validateApiKey(env: Env, key: string, requiredScope?: string) {
  const keyHash = await sha256Hex(key);
  
  const apiKey = await env.DB.prepare(
    "SELECT * FROM api_keys WHERE key_hash=?"
  ).bind(keyHash).first<any>();
  
  if (!apiKey) return { valid: false, error: "Invalid API key" };
  if (apiKey.expires_at && new Date(apiKey.expires_at) < new Date()) {
    return { valid: false, error: "API key expired" };
  }
  
  const scopes = JSON.parse(apiKey.scopes_json || "[]");
  if (requiredScope && !scopes.includes("*") && !scopes.includes(requiredScope)) {
    return { valid: false, error: "Insufficient scope" };
  }
  
  // Update last used
  await env.DB.prepare("UPDATE api_keys SET last_used_at=? WHERE id=?").bind(nowISO(), apiKey.id).run();
  
  return { valid: true, name: apiKey.name, scopes };
}

// Time tracking - start timer
async function startTimer(env: Env, ticketId: number, staffId: string, description?: string) {
  // Check for running timer
  const running = await env.DB.prepare(
    "SELECT id FROM ticket_timers WHERE ticket_id=? AND staff_id=? AND stopped_at IS NULL"
  ).bind(ticketId, staffId).first<any>();
  
  if (running) return { ok: false, error: "Timer already running", timerId: running.id };
  
  const result = await env.DB.prepare(
    "INSERT INTO ticket_timers (ticket_id, staff_id, started_at, description) VALUES (?,?,?,?)"
  ).bind(ticketId, staffId, nowISO(), description || null).run();
  
  return { ok: true, timerId: result.meta.last_row_id };
}

// Time tracking - stop timer
async function stopTimer(env: Env, timerId: number) {
  const timer = await env.DB.prepare(
    "SELECT * FROM ticket_timers WHERE id=?"
  ).bind(timerId).first<any>();
  
  if (!timer) return { ok: false, error: "Timer not found" };
  if (timer.stopped_at) return { ok: false, error: "Timer already stopped" };
  
  const now = nowISO();
  const startMs = new Date(timer.started_at).getTime();
  const endMs = new Date(now).getTime();
  const durationMins = Math.round((endMs - startMs) / 60_000);
  
  await env.DB.prepare(
    "UPDATE ticket_timers SET stopped_at=?, duration_mins=? WHERE id=?"
  ).bind(now, durationMins, timerId).run();
  
  await writeEvent(env, timer.ticket_id, "TIME_LOGGED", "staff", timer.staff_id, {
    timerId,
    durationMins,
    description: timer.description
  });
  
  return { ok: true, durationMins };
}

// Get ticket time summary
async function getTicketTime(env: Env, ticketId: number) {
  const timers = await env.DB.prepare(
    "SELECT SUM(duration_mins) AS total_mins, SUM(CASE WHEN billable=1 THEN duration_mins ELSE 0 END) AS billable_mins FROM ticket_timers WHERE ticket_id=? AND stopped_at IS NOT NULL"
  ).bind(ticketId).first<any>();
  
  return {
    totalMins: timers?.total_mins ?? 0,
    billableMins: timers?.billable_mins ?? 0
  };
}

// Send satisfaction survey
async function sendSurvey(env: Env, ticketId: number) {
  const ticket = await env.DB.prepare(
    "SELECT t.*, c.email, c.name FROM tickets t LEFT JOIN clients c ON c.id = t.client_id WHERE t.id=?"
  ).bind(ticketId).first<any>();
  
  if (!ticket || !ticket.email) return { ok: false, error: "No client email" };
  
  const token = crypto.randomUUID().replace(/-/g, "");
  
  await env.DB.prepare(
    "INSERT OR REPLACE INTO surveys (ticket_id, token, created_at) VALUES (?,?,?)"
  ).bind(ticketId, token, nowISO()).run();
  
  // Send email with survey link
  await sendEmail(env, ticket.email, "ticket_resolved", {
    ticket_id: ticket.public_id,
    client_name: ticket.name || "there",
    resolution: "Your issue has been resolved. Please take a moment to rate your experience."
  });
  
  return { ok: true, token };
}

// Post to Slack/Discord
async function postToChatIntegration(env: Env, platform: string, eventType: string, message: string, data?: any) {
  const integrations = await env.DB.prepare(
    "SELECT * FROM chat_integrations WHERE platform=? AND active=1"
  ).bind(platform).all<any>();
  
  let posted = 0;
  
  for (const integration of (integrations.results ?? [])) {
    const events = JSON.parse(integration.events_json || "[]");
    if (!events.includes("*") && !events.includes(eventType)) continue;
    
    if (integration.webhook_url) {
      try {
        const payload = platform === "slack" 
          ? { text: message, blocks: data?.blocks }
          : { content: message, embeds: data?.embeds };
        
        await fetch(integration.webhook_url, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });
        posted++;
      } catch { /* ignore */ }
    }
  }
  
  return { posted };
}

// Get canned response
async function getCannedResponse(env: Env, code: string) {
  const response = await env.DB.prepare(
    "SELECT * FROM canned_responses WHERE code=?"
  ).bind(code).first<any>();
  
  if (response) {
    // Increment use count
    await env.DB.prepare("UPDATE canned_responses SET use_count = use_count + 1 WHERE id=?").bind(response.id).run();
  }
  
  return response;
}

// Generate report
async function generateReport(env: Env, type: string, params: any) {
  const now = nowISO();
  const startDate = params.startDate || new Date(Date.now() - 30 * 86400_000).toISOString().slice(0, 10);
  const endDate = params.endDate || new Date().toISOString().slice(0, 10);
  
  let result: any = {};
  
  switch (type) {
    case "ticket_volume":
      const volume = await env.DB.prepare(`
        SELECT 
          date(created_at) AS date,
          COUNT(*) AS count,
          channel
        FROM tickets 
        WHERE created_at >= ? AND created_at <= ?
        GROUP BY date(created_at), channel
        ORDER BY date
      `).bind(startDate, endDate + "T23:59:59Z").all<any>();
      result = { type, dates: volume.results ?? [] };
      break;
      
    case "sla_compliance":
      const sla = await env.DB.prepare(`
        SELECT 
          COUNT(*) AS total,
          SUM(CASE WHEN first_response_breached = 0 THEN 1 ELSE 0 END) AS response_met,
          SUM(CASE WHEN resolution_breached = 0 AND resolution_at IS NOT NULL THEN 1 ELSE 0 END) AS resolution_met
        FROM sla_tracking st
        JOIN tickets t ON t.id = st.ticket_id
        WHERE t.created_at >= ? AND t.created_at <= ?
      `).bind(startDate, endDate + "T23:59:59Z").first<any>();
      result = {
        type,
        total: sla?.total ?? 0,
        responseCompliance: sla?.total ? Math.round((sla.response_met / sla.total) * 100) : 100,
        resolutionCompliance: sla?.total ? Math.round((sla.resolution_met / sla.total) * 100) : 100
      };
      break;
      
    case "staff_performance":
      const staff = await env.DB.prepare(`
        SELECT 
          actor_id AS staff_id,
          COUNT(DISTINCT ticket_id) AS tickets_touched,
          COUNT(*) AS actions
        FROM events 
        WHERE actor_type = 'staff' AND created_at >= ? AND created_at <= ?
        GROUP BY actor_id
        ORDER BY actions DESC
      `).bind(startDate, endDate + "T23:59:59Z").all<any>();
      result = { type, staff: staff.results ?? [] };
      break;
      
    case "client_satisfaction":
      const satisfaction = await env.DB.prepare(`
        SELECT 
          AVG(rating) AS avg_rating,
          COUNT(*) AS total_surveys,
          SUM(CASE WHEN rating >= 4 THEN 1 ELSE 0 END) AS satisfied
        FROM surveys
        WHERE submitted_at IS NOT NULL AND submitted_at >= ? AND submitted_at <= ?
      `).bind(startDate, endDate + "T23:59:59Z").first<any>();
      result = {
        type,
        avgRating: satisfaction?.avg_rating ?? 0,
        totalSurveys: satisfaction?.total_surveys ?? 0,
        satisfactionRate: satisfaction?.total_surveys ? Math.round((satisfaction.satisfied / satisfaction.total_surveys) * 100) : 0
      };
      break;
  }
  
  return result;
}

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

// Redact PII from case bundle
function redactCaseBundle(bundle: any) {
  if (!bundle) return bundle;

  // events: strip IP and any obvious headers you store
  if (Array.isArray(bundle.events)) {
    bundle.events = bundle.events.map((e: any) => ({
      ...e,
      ip: null
    }));
  }

  // If you ever add UA later: strip it here.
  // bundle.events = bundle.events.map(e => ({...e, ua: null}))

  // client: keep only minimal operational identity (optional)
  if (bundle.client) {
    bundle.client = {
      id: bundle.client.id,
      name: bundle.client.name ?? null
      // email/phone intentionally removed
    };
  }

  return bundle;
}

// Build full case bundle for export
async function buildCaseBundle(env: Env, ticketId: number, redacted: boolean) {
  const ticket = await env.DB.prepare("SELECT * FROM tickets WHERE id=?").bind(ticketId).first<any>();
  if (!ticket) return null;

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
    "SELECT id, type, actor_type, actor_id, payload_json, created_at FROM events WHERE ticket_id=? ORDER BY id ASC"
  ).bind(ticketId).all<any>();

  const uploads = await env.DB.prepare(
    "SELECT id, r2_key, filename, content_type, bytes, created_at FROM uploads WHERE ticket_id=? ORDER BY id ASC"
  ).bind(ticketId).all<any>();

  const followups = await env.DB.prepare(
    "SELECT * FROM followups WHERE ticket_id=? ORDER BY due_at ASC"
  ).bind(ticketId).all<any>();

  const playbookRuns = await env.DB.prepare(
    "SELECT pr.id AS run_id, pr.status, pr.created_at, pr.updated_at, p.code, p.name " +
    "FROM playbook_runs pr JOIN playbooks p ON p.id=pr.playbook_id WHERE pr.ticket_id=? ORDER BY pr.id ASC"
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

  const fixReceipts = await env.DB.prepare(
    "SELECT * FROM fix_receipts WHERE ticket_id=? ORDER BY id ASC"
  ).bind(ticketId).all<any>();

  // Evidence pack: what user approved + timestamps
  const approvals = (events.results ?? []).filter((e: any) => 
    ["ESTIMATE_APPROVED", "CONSENT_GRANTED", "PAYMENT_CONFIRMED"].includes(e.type)
  );

  const bundle: any = {
    exportedAt: nowISO(),
    ticket,
    client,
    device,
    clientProfile: profile,
    events: events.results ?? [],
    uploads: uploads.results ?? [],
    followups: followups.results ?? [],
    playbooks: { runs: playbookRuns.results ?? [] },
    billing: {
      estimates: estimates.results ?? [],
      payments: payments.results ?? [],
      invoices: invoices.results ?? [],
      invoiceItems: invoiceItems.results ?? []
    },
    fixReceipts: fixReceipts.results ?? [],
    approvals
  };

  return redacted ? redactCaseBundle(bundle) : bundle;
}

// Run auto-close (warn + close)
async function runAutoClose(env: Env, limit: number) {
  const now = nowISO();
  let warned = 0;
  let closed = 0;

  // 1) Send warnings for tickets approaching close
  const toWarn = await env.DB.prepare(
    "SELECT id, ticket_id FROM auto_close_queue WHERE warned=0 AND warn_at <= ? LIMIT ?"
  ).bind(now, limit).all<any>();

  for (const row of (toWarn.results ?? [])) {
    await env.DB.prepare("UPDATE auto_close_queue SET warned=1 WHERE id=?").bind(row.id).run();
    await writeEvent(env, row.ticket_id, "AUTO_CLOSE_WARNING", "system", "system", {
      message: "This ticket will be auto-closed soon if no response."
    });
    warned++;
  }

  // 2) Close tickets past close_at
  const toClose = await env.DB.prepare(
    "SELECT id, ticket_id FROM auto_close_queue WHERE close_at <= ? LIMIT ?"
  ).bind(now, limit).all<any>();

  for (const row of (toClose.results ?? [])) {
    // Check runbook lock
    const check = await canTicketClose(env, row.ticket_id);
    if (!check.ok) {
      // Can't close - extend by 7 days
      const newClose = new Date(Date.now() + 7 * 86400_000).toISOString();
      await env.DB.prepare("UPDATE auto_close_queue SET close_at=?, warned=0 WHERE id=?")
        .bind(newClose, row.id).run();
      await writeEvent(env, row.ticket_id, "AUTO_CLOSE_DEFERRED", "system", "system", {
        reason: check.reason,
        newCloseAt: newClose
      });
      continue;
    }

    // Close the ticket
    await env.DB.prepare("UPDATE tickets SET status='CLOSED', updated_at=? WHERE id=?")
      .bind(now, row.ticket_id).run();
    await env.DB.prepare("DELETE FROM auto_close_queue WHERE id=?").bind(row.id).run();
    await writeEvent(env, row.ticket_id, "AUTO_CLOSED", "system", "system", {});
    closed++;
  }

  return { warned, closed };
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

      // Parallel: access + event writes + SLA init + heatmap
      await Promise.all([
        env.DB.prepare("INSERT INTO ticket_access (ticket_id, secret_hash) VALUES (?,?)").bind(ticketId, secretHash).run(),
        writeEvent(env, ticketId, "CREATED", "public", ip ?? null, { channel, subject }),
        initSlaTracking(env, ticketId, 1), // default SLA
        updateHeatmap(env),
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
      const newStatus = String(body?.status ?? "");
      if (!id || !newStatus) return bad(400, "Missing id/status");

      // Runbook lock: can't close without PREVENTION_PLAN_CREATED + followups
      if (newStatus === "CLOSED") {
        await assertCloseAllowed(env, id);
        // Record resolution for SLA
        await recordResolution(env, id);
      }

      await env.DB.prepare("UPDATE tickets SET status=?, updated_at=? WHERE id=?")
        .bind(newStatus, nowISO(), id).run();

      await writeEvent(env, id, "STATUS_CHANGED", "staff", "staff", { status: newStatus });

      return json({ ok: true });
    }

    // --------------------
    // STAFF: Add note to ticket (tracks first response for SLA)
    // --------------------
    if (path.match(/^\/staff\/tickets\/\d+\/note$/) && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const ticketId = Number(path.split("/")[3]);
      const body = await readJson(req);
      const note = String(body?.note ?? "").trim();
      const isPublic = !!body?.isPublic; // visible to client?

      if (!note) return bad(400, "Missing note");

      // Record first response for SLA
      const slaResult = await recordFirstResponse(env, ticketId);

      await env.DB.prepare("UPDATE tickets SET updated_at=? WHERE id=?")
        .bind(nowISO(), ticketId).run();

      await writeEvent(env, ticketId, isPublic ? "PUBLIC_NOTE" : "STAFF_NOTE", "staff", "staff", { note });

      // Update client if linked
      const ticket = await env.DB.prepare("SELECT client_id FROM tickets WHERE id=?").bind(ticketId).first<any>();
      if (ticket?.client_id) {
        await updateClientHealth(env, ticket.client_id);
      }

      // Deliver webhooks
      await deliverWebhooks(env, isPublic ? "PUBLIC_NOTE" : "STAFF_NOTE", ticketId, { note });

      return json({ ok: true, sla: slaResult });
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
        });

        // Auto-generate fix receipt
        const invoice = await env.DB.prepare(
          "SELECT id FROM invoices WHERE ticket_id=? ORDER BY id DESC LIMIT 1"
        ).bind(ticketId).first<any>();
        if (invoice) {
          const receipt = await generateFixReceipt(env, ticketId, invoice.id);
          await env.DB.prepare(
            "INSERT INTO fix_receipts (ticket_id, invoice_id, receipt_json, created_at) VALUES (?,?,?,?)"
          ).bind(ticketId, invoice.id, JSON.stringify(receipt), nowIso).run();
          await writeEvent(env, ticketId, "FIX_RECEIPT_GENERATED", "system", "system", { invoiceId: invoice.id });
        }

        return json({ ok: true, received: true });
      }

      // Ack other events (Stripe expects 200)
      return json({ ok: true, received: true, eventType });
    }

    // --------------------
    // STAFF: Control Lane - Grant (with 30m auto-revoke guardrail)
    // --------------------
    if (path === "/staff/control/grant" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const ticketId = Number(body?.ticketId);
      const minutes = Number(body?.minutes ?? 30);
      if (!ticketId) return bad(400, "Missing ticketId");

      const now = nowISO();
      const expiresAt = new Date(Date.now() + minutes * 60_000).toISOString();

      const ins = await env.DB.prepare(
        "INSERT INTO control_lanes (ticket_id, status, granted_at, expires_at, created_at) VALUES (?,?,?,?,?)"
      ).bind(ticketId, "active", now, expiresAt, now).run();

      await writeEvent(env, ticketId, "CONTROL_GRANTED", "staff", "staff", { 
        controlLaneId: ins.meta.last_row_id, 
        expiresAt,
        minutesGranted: minutes 
      });

      return json({ ok: true, controlLaneId: ins.meta.last_row_id, expiresAt });
    }

    // --------------------
    // STAFF: Control Lane - Revoke
    // --------------------
    if (path === "/staff/control/revoke" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const ticketId = Number(body?.ticketId);
      if (!ticketId) return bad(400, "Missing ticketId");

      const now = nowISO();
      await env.DB.prepare(
        "UPDATE control_lanes SET status='revoked', revoked_at=? WHERE ticket_id=? AND status='active'"
      ).bind(now, ticketId).run();

      await writeEvent(env, ticketId, "CONTROL_REVOKED", "staff", "staff", {});

      return json({ ok: true });
    }

    // --------------------
    // STAFF: Expire stale control lanes (run from cron or manually)
    // --------------------
    if (path === "/staff/control/expire" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const now = nowISO();
      const stale = await env.DB.prepare(
        "SELECT id, ticket_id FROM control_lanes WHERE status='active' AND expires_at <= ?"
      ).bind(now).all<any>();

      for (const lane of (stale.results ?? [])) {
        await env.DB.prepare("UPDATE control_lanes SET status='expired' WHERE id=?").bind(lane.id).run();
        await writeEvent(env, lane.ticket_id, "CONTROL_EXPIRED", "system", "system", { controlLaneId: lane.id });
      }

      return json({ ok: true, expired: stale.results?.length ?? 0 });
    }

    // --------------------
    // STAFF: Validate tags against controlled enum
    // --------------------
    if (path === "/staff/tags/validate" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const tags = Array.isArray(body?.tags) ? body.tags : [];
      const { valid, invalid } = validateTags(tags);

      return json({ ok: invalid.length === 0, valid, invalid, allowedTags: [...ALLOWED_TAGS] });
    }

    // --------------------
    // STAFF: Get allowed tag enum
    // --------------------
    if (path === "/staff/tags/enum" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const rows = await env.DB.prepare(
        "SELECT tag, category, description FROM tag_enum ORDER BY category, tag"
      ).all<any>();

      return json({ ok: true, tags: rows.results ?? [] });
    }

    // --------------------
    // STAFF: Playbook compiler (generates client + tech versions)
    // --------------------
    if (path === "/staff/playbooks/compile" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const code = String(body?.code ?? "").toUpperCase();
      const os = String(body?.os ?? "both");
      if (!code) return bad(400, "Missing playbook code");

      const pb = await env.DB.prepare(
        "SELECT id, code, name, persona FROM playbooks WHERE code=?"
      ).bind(code).first<any>();
      if (!pb) return bad(404, "Playbook not found");

      const steps = await env.DB.prepare(
        "SELECT step_order, title, detail FROM playbook_steps WHERE playbook_id=? AND (os=? OR os='both') ORDER BY step_order ASC"
      ).bind(pb.id, os).all<any>();

      // Client version: simplified, no jargon
      const clientVersion = {
        title: pb.name,
        steps: (steps.results ?? []).map((s: any, i: number) => ({
          step: i + 1,
          what: s.title
        }))
      };

      // Tech version: full detail
      const techVersion = {
        code: pb.code,
        name: pb.name,
        persona: pb.persona,
        os,
        steps: steps.results ?? []
      };

      return json({ ok: true, clientVersion, techVersion });
    }

    // --------------------
    // STAFF: Schedule D3 micro-check-in (anti-repeat nudge)
    // --------------------
    if (path === "/staff/followups/d3" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const ticketId = Number(body?.ticketId);
      if (!ticketId) return bad(400, "Missing ticketId");

      const now = new Date();
      const d3 = new Date(now.getTime() + 3 * 86400_000).toISOString();
      const nowIso = nowISO();

      // Check if D3 already scheduled
      const existing = await env.DB.prepare(
        "SELECT id FROM followups WHERE ticket_id=? AND type='D3' AND status='scheduled'"
      ).bind(ticketId).first<any>();

      if (existing) return json({ ok: true, alreadyScheduled: true, followupId: existing.id });

      const ins = await env.DB.prepare(
        "INSERT INTO followups (ticket_id, type, due_at, status, created_at) VALUES (?,?,?,?,?)"
      ).bind(ticketId, "D3", d3, "scheduled", nowIso).run();

      await writeEvent(env, ticketId, "D3_SCHEDULED", "staff", "staff", { dueAt: d3 });

      return json({ ok: true, followupId: ins.meta.last_row_id, dueAt: d3 });
    }

    // --------------------
    // STAFF: Triage autopilot (if tags match PB, auto-apply in draft)
    // --------------------
    if (path === "/staff/ai/autopilot" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const ticketId = Number(body?.ticketId);
      if (!ticketId) return bad(400, "Missing ticketId");

      // Get ticket's tags
      const ptRow = await env.DB.prepare(
        "SELECT tags_json FROM persona_tags WHERE ticket_id=?"
      ).bind(ticketId).first<any>();

      const ticketTags = ptRow?.tags_json ? JSON.parse(ptRow.tags_json) : [];
      if (ticketTags.length === 0) return json({ ok: true, matched: false, reason: "No tags on ticket" });

      // Find playbooks with matching tags
      const playbooks = await env.DB.prepare(
        "SELECT id, code, name, tags_json FROM playbooks"
      ).all<any>();

      let bestMatch: { code: string; name: string; score: number } | null = null;

      for (const pb of (playbooks.results ?? [])) {
        const pbTags = pb.tags_json ? JSON.parse(pb.tags_json) : [];
        const overlap = ticketTags.filter((t: string) => pbTags.includes(t)).length;
        if (overlap > 0 && (!bestMatch || overlap > bestMatch.score)) {
          bestMatch = { code: pb.code, name: pb.name, score: overlap };
        }
      }

      if (!bestMatch) return json({ ok: true, matched: false, reason: "No playbook matches tags" });

      // Auto-apply in draft mode (don't run steps)
      await writeEvent(env, ticketId, "PLAYBOOK_AUTO_SUGGESTED", "ai", "ai", {
        playbookCode: bestMatch.code,
        playbookName: bestMatch.name,
        matchScore: bestMatch.score,
        mode: "draft"
      });

      return json({ ok: true, matched: true, playbook: bestMatch });
    }

    // --------------------
    // STAFF: Get fix receipt
    // --------------------
    if (path === "/staff/receipt/get" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const ticketId = Number(url.searchParams.get("ticketId"));
      if (!ticketId) return bad(400, "Missing ticketId");

      const receipt = await env.DB.prepare(
        "SELECT * FROM fix_receipts WHERE ticket_id=? ORDER BY id DESC LIMIT 1"
      ).bind(ticketId).first<any>();

      if (!receipt) return bad(404, "No fix receipt found");

      return json({ ok: true, receipt: { ...receipt, receipt: JSON.parse(receipt.receipt_json) } });
    }

    // --------------------
    // STAFF: Generate fix receipt manually
    // --------------------
    if (path === "/staff/receipt/generate" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const ticketId = Number(body?.ticketId);
      const invoiceId = Number(body?.invoiceId);
      if (!ticketId || !invoiceId) return bad(400, "Missing ticketId/invoiceId");

      const receipt = await generateFixReceipt(env, ticketId, invoiceId);
      const now = nowISO();

      await env.DB.prepare(
        "INSERT INTO fix_receipts (ticket_id, invoice_id, receipt_json, created_at) VALUES (?,?,?,?)"
      ).bind(ticketId, invoiceId, JSON.stringify(receipt), now).run();

      await writeEvent(env, ticketId, "FIX_RECEIPT_GENERATED", "staff", "staff", { invoiceId });

      return json({ ok: true, receipt });
    }

    // --------------------
    // PUBLIC: Resumable upload - init
    // --------------------
    if (path === "/public/upload/init" && method === "POST") {
      const turnstileToken = req.headers.get("X-Turnstile-Token") ?? "";
      const publicId = req.headers.get("X-Ticket-PublicId") ?? "";
      const secret = req.headers.get("X-Ticket-Secret") ?? "";
      if (!turnstileToken || !publicId || !secret) return bad(400, "Missing headers");

      const ip = getIP(req);
      const [v, t] = await Promise.all([
        verifyTurnstile(env.TURNSTILE_SECRET, turnstileToken, ip),
        getTicketByPublic(env, publicId),
      ]);

      if (!v.success) return bad(403, "Turnstile failed");
      if (!t) return bad(404, "Ticket not found");

      const [access, secretHash] = await Promise.all([
        env.DB.prepare("SELECT secret_hash FROM ticket_access WHERE ticket_id=?").bind(t.id).first<any>(),
        sha256Hex(secret),
      ]);
      if (!access || access.secret_hash !== secretHash) return bad(403, "Bad secret");

      const body = await readJson(req);
      const totalBytes = Number(body?.totalBytes ?? 0);
      const filename = String(body?.filename ?? "file");
      const contentType = String(body?.contentType ?? "application/octet-stream");

      if (totalBytes > 100 * 1024 * 1024) return bad(413, "Max 100MB for resumable uploads");

      const uploadId = crypto.randomUUID();

      return json({ ok: true, uploadId, ticketId: t.id, totalBytes, filename, contentType });
    }

    // --------------------
    // PUBLIC: Resumable upload - chunk
    // --------------------
    if (path === "/public/upload/chunk" && method === "POST") {
      const publicId = req.headers.get("X-Ticket-PublicId") ?? "";
      const secret = req.headers.get("X-Ticket-Secret") ?? "";
      const uploadId = req.headers.get("X-Upload-Id") ?? "";
      const chunkIndex = Number(req.headers.get("X-Chunk-Index") ?? "-1");
      const expectedChecksum = req.headers.get("X-Checksum") ?? "";

      if (!publicId || !secret || !uploadId || chunkIndex < 0) return bad(400, "Missing headers");

      const t = await getTicketByPublic(env, publicId);
      if (!t) return bad(404, "Ticket not found");

      const [access, secretHash] = await Promise.all([
        env.DB.prepare("SELECT secret_hash FROM ticket_access WHERE ticket_id=?").bind(t.id).first<any>(),
        sha256Hex(secret),
      ]);
      if (!access || access.secret_hash !== secretHash) return bad(403, "Bad secret");

      const blob = await req.arrayBuffer();
      if (blob.byteLength > 5 * 1024 * 1024) return bad(413, "Chunk max 5MB");

      // Verify checksum
      const actualChecksum = await sha256Hex(new TextDecoder().decode(blob));
      if (expectedChecksum && actualChecksum !== expectedChecksum) {
        return bad(400, "Checksum mismatch");
      }

      const key = `chunks/${uploadId}/${chunkIndex}`;
      await env.UPLOADS.put(key, blob);

      const now = nowISO();
      await env.DB.prepare(
        "INSERT INTO upload_chunks (upload_id, ticket_id, chunk_index, r2_key, checksum, bytes, created_at) VALUES (?,?,?,?,?,?,?)"
      ).bind(uploadId, t.id, chunkIndex, key, actualChecksum, blob.byteLength, now).run();

      return json({ ok: true, chunkIndex, bytes: blob.byteLength, checksum: actualChecksum });
    }

    // --------------------
    // PUBLIC: Resumable upload - complete
    // --------------------
    if (path === "/public/upload/complete" && method === "POST") {
      const publicId = req.headers.get("X-Ticket-PublicId") ?? "";
      const secret = req.headers.get("X-Ticket-Secret") ?? "";
      const uploadId = req.headers.get("X-Upload-Id") ?? "";

      if (!publicId || !secret || !uploadId) return bad(400, "Missing headers");

      const t = await getTicketByPublic(env, publicId);
      if (!t) return bad(404, "Ticket not found");

      const [access, secretHash] = await Promise.all([
        env.DB.prepare("SELECT secret_hash FROM ticket_access WHERE ticket_id=?").bind(t.id).first<any>(),
        sha256Hex(secret),
      ]);
      if (!access || access.secret_hash !== secretHash) return bad(403, "Bad secret");

      const body = await readJson(req);
      const filename = String(body?.filename ?? "file");
      const contentType = String(body?.contentType ?? "application/octet-stream");

      // Get all chunks
      const chunks = await env.DB.prepare(
        "SELECT r2_key, chunk_index, bytes FROM upload_chunks WHERE upload_id=? ORDER BY chunk_index ASC"
      ).bind(uploadId).all<any>();

      if (!chunks.results || chunks.results.length === 0) {
        return bad(400, "No chunks found for this upload");
      }

      // Concatenate chunks (for small files - production would use multipart)
      const parts: ArrayBuffer[] = [];
      let totalBytes = 0;
      for (const c of chunks.results) {
        const obj = await env.UPLOADS.get(c.r2_key);
        if (!obj) return bad(500, `Missing chunk ${c.chunk_index}`);
        const buf = await obj.arrayBuffer();
        parts.push(buf);
        totalBytes += buf.byteLength;
      }

      // Merge and store final file
      const merged = new Uint8Array(totalBytes);
      let offset = 0;
      for (const p of parts) {
        merged.set(new Uint8Array(p), offset);
        offset += p.byteLength;
      }

      const finalKey = `${publicId}/${Date.now()}-${filename}`;
      await env.UPLOADS.put(finalKey, merged, { httpMetadata: { contentType } });

      // Record in uploads table
      const now = nowISO();
      await env.DB.prepare(
        "INSERT INTO uploads (ticket_id, r2_key, filename, content_type, bytes, created_at) VALUES (?,?,?,?,?,?)"
      ).bind(t.id, finalKey, filename, contentType, totalBytes, now).run();

      await writeEvent(env, t.id, "UPLOAD_COMPLETED", "public", getIP(req) ?? null, {
        key: finalKey,
        filename,
        contentType,
        bytes: totalBytes,
        chunks: chunks.results.length
      });

      // Cleanup chunks
      for (const c of chunks.results) {
        await env.UPLOADS.delete(c.r2_key);
      }
      await env.DB.prepare("DELETE FROM upload_chunks WHERE upload_id=?").bind(uploadId).run();

      return json({ ok: true, key: finalKey, bytes: totalBytes });
    }

    // --------------------
    // STAFF: Get case bundle inline (optional redact via query param)
    // --------------------
    if (path.match(/^\/staff\/tickets\/\d+\/bundle$/) && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");

      const ticketId = Number(path.split("/")[3]);
      const redacted = url.searchParams.get("redact") === "1";

      const bundle = await buildCaseBundle(env, ticketId, redacted);
      if (!bundle) return bad(404, "Ticket not found");

      return json({ ok: true, bundle });
    }

    // --------------------
    // STAFF: Create R2 snapshot export + mint signed URL
    // --------------------
    if (path === "/staff/export/snapshot" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const ticketId = Number(body?.ticketId);
      const redacted = !!body?.redacted;
      const expiresMinutes = Number(body?.expiresMinutes ?? 60); // default 60 min
      if (!ticketId) return bad(400, "Missing ticketId");

      const bundle = await buildCaseBundle(env, ticketId, redacted);
      if (!bundle) return bad(404, "Ticket not found");

      const token = crypto.randomUUID().replace(/-/g, "");
      const createdAt = nowISO();
      const expiresAt = new Date(Date.now() + expiresMinutes * 60_000).toISOString();

      const key = `exports/tickets/${ticketId}/${createdAt.replace(/[:.]/g, "-")}${redacted ? "_redacted" : ""}.json`;
      const bodyText = JSON.stringify(bundle);

      // Store in R2
      await env.UPLOADS.put(key, bodyText, {
        httpMetadata: { contentType: "application/json" }
      });

      // Record token
      await env.DB.prepare(
        "INSERT INTO exports (token, ticket_id, r2_key, redacted, expires_at, created_at) VALUES (?,?,?,?,?,?)"
      ).bind(token, ticketId, key, redacted ? 1 : 0, expiresAt, createdAt).run();

      await writeEvent(env, ticketId, "CASE_SNAPSHOT_STORED", "staff", "staff", {
        r2_key: key,
        redacted,
        expiresAt,
        bytes: bodyText.length
      });

      const origin = new URL(req.url).origin;
      const downloadUrl = `${origin}/public/export/${token}`;

      return json({ ok: true, ticketId, redacted, r2_key: key, expiresAt, downloadUrl });
    }

    // --------------------
    // PUBLIC: Download export via signed token (streams from R2)
    // --------------------
    if (path.startsWith("/public/export/") && method === "GET") {
      const token = path.split("/").pop()!;
      if (!token) return bad(400, "Missing token");

      const row = await env.DB.prepare(
        "SELECT token, ticket_id, r2_key, redacted, expires_at, downloaded_at FROM exports WHERE token=?"
      ).bind(token).first<any>();

      if (!row) return bad(404, "Invalid token");
      if (new Date(row.expires_at).getTime() < Date.now()) return bad(410, "Token expired");

      const obj = await env.UPLOADS.get(row.r2_key);
      if (!obj) return bad(404, "Missing object");

      const now = nowISO();
      if (!row.downloaded_at) {
        await env.DB.prepare("UPDATE exports SET downloaded_at=? WHERE token=?").bind(now, token).run();
        await writeEvent(env, row.ticket_id, "CASE_SNAPSHOT_DOWNLOADED", "public", getIP(req) ?? null, {
          redacted: !!row.redacted
        });
      }

      const headers = new Headers();
      obj.writeHttpMetadata(headers);
      headers.set("Content-Type", "application/json");
      headers.set(
        "Content-Disposition",
        `attachment; filename="noizylab_case_ticket_${row.ticket_id}${row.redacted ? "_redacted" : ""}.json"`
      );

      return new Response(obj.body, { headers });
    }

    // --------------------
    // STAFF: Schedule auto-close for ticket
    // --------------------
    if (path === "/staff/autoclose/schedule" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const ticketId = Number(body?.ticketId);
      const warnDays = Number(body?.warnDays ?? 5);
      const closeDays = Number(body?.closeDays ?? 7);
      if (!ticketId) return bad(400, "Missing ticketId");

      const now = new Date();
      const warnAt = new Date(now.getTime() + warnDays * 86400_000).toISOString();
      const closeAt = new Date(now.getTime() + closeDays * 86400_000).toISOString();
      const nowIso = nowISO();

      // Upsert into auto_close_queue
      await env.DB.prepare(
        "INSERT INTO auto_close_queue (ticket_id, warn_at, close_at, created_at) VALUES (?,?,?,?) " +
        "ON CONFLICT(ticket_id) DO UPDATE SET warn_at=excluded.warn_at, close_at=excluded.close_at, warned=0"
      ).bind(ticketId, warnAt, closeAt, nowIso).run();

      await writeEvent(env, ticketId, "AUTO_CLOSE_SCHEDULED", "staff", "staff", {
        warnAt,
        closeAt
      });

      return json({ ok: true, warnAt, closeAt });
    }

    // --------------------
    // STAFF: Cancel auto-close for ticket
    // --------------------
    if (path === "/staff/autoclose/cancel" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const ticketId = Number(body?.ticketId);
      if (!ticketId) return bad(400, "Missing ticketId");

      await env.DB.prepare("DELETE FROM auto_close_queue WHERE ticket_id=?").bind(ticketId).run();
      await writeEvent(env, ticketId, "AUTO_CLOSE_CANCELED", "staff", "staff", {});

      return json({ ok: true });
    }

    // --------------------
    // STAFF: Run auto-close manually
    // --------------------
    if (path === "/staff/autoclose/run" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const limit = Number(body?.limit ?? 50);
      const result = await runAutoClose(env, limit);

      return json({ ok: true, ...result });
    }

    // --------------------
    // STAFF: ops:run (unified ops runner - by type)
    // --------------------
    if (path === "/staff/ops/run" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);

      const type = String(body?.type ?? "");
      const limit = Number(body?.limit ?? 200);

      if (!type) return bad(400, "Missing type");

      if (type === "retention_purge") return json({ ok: true, result: await runRetention(env, limit) });
      if (type === "followups_run") return json({ ok: true, result: await runFollowups(env, limit) });
      if (type === "metrics_rollup") return json({ ok: true, result: await rollupMetrics(env) });

      return bad(400, "Unknown type");
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

    // ====================
    // HOT ROD ROUTES
    // ====================

    // --------------------
    // STAFF: SLA Dashboard stats
    // --------------------
    if (path === "/staff/sla/stats" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const stats = await getSlaStats(env);
      return json({ ok: true, stats });
    }

    // --------------------
    // STAFF: SLA targets list
    // --------------------
    if (path === "/staff/sla/targets" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const targets = await env.DB.prepare("SELECT * FROM sla_targets ORDER BY id").all<any>();
      return json({ ok: true, targets: targets.results ?? [] });
    }

    // --------------------
    // STAFF: Set ticket SLA target
    // --------------------
    if (path === "/staff/sla/set" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const ticketId = Number(body?.ticketId);
      const slaTargetId = Number(body?.slaTargetId ?? 1);
      if (!ticketId) return bad(400, "Missing ticketId");

      await initSlaTracking(env, ticketId, slaTargetId);
      await writeEvent(env, ticketId, "SLA_SET", "staff", "staff", { slaTargetId });
      return json({ ok: true });
    }

    // --------------------
    // STAFF: Client health score
    // --------------------
    if (path.match(/^\/staff\/clients\/\d+\/health$/) && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const clientId = Number(path.split("/")[3]);
      const health = await updateClientHealth(env, clientId);
      return json({ ok: true, ...health });
    }

    // --------------------
    // STAFF: Record sentiment
    // --------------------
    if (path === "/staff/sentiment/record" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const clientId = Number(body?.clientId);
      const ticketId = body?.ticketId ? Number(body.ticketId) : null;
      const score = Number(body?.score ?? 0);
      const source = String(body?.source ?? "manual");
      const notes = body?.notes ?? null;

      if (!clientId) return bad(400, "Missing clientId");
      if (score < -2 || score > 2) return bad(400, "Score must be -2 to +2");

      await env.DB.prepare(
        "INSERT INTO client_sentiment (client_id, ticket_id, score, source, notes, created_at) VALUES (?,?,?,?,?,?)"
      ).bind(clientId, ticketId, score, source, notes, nowISO()).run();

      // Update health score
      await updateClientHealth(env, clientId);

      return json({ ok: true });
    }

    // --------------------
    // STAFF: Activity heatmap
    // --------------------
    if (path === "/staff/heatmap" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const grid = await getHeatmap(env);
      return json({ ok: true, grid });
    }

    // --------------------
    // STAFF: Run escalations
    // --------------------
    if (path === "/staff/escalations/run" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const limit = Number(body?.limit ?? 50);
      const result = await runEscalations(env, limit);
      return json({ ok: true, ...result });
    }

    // --------------------
    // STAFF: List escalations for ticket
    // --------------------
    if (path.match(/^\/staff\/tickets\/\d+\/escalations$/) && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const ticketId = Number(path.split("/")[3]);
      const escalations = await env.DB.prepare(
        "SELECT e.*, r.name AS rule_name FROM escalations e JOIN escalation_rules r ON r.id = e.rule_id WHERE e.ticket_id=? ORDER BY e.created_at DESC"
      ).bind(ticketId).all<any>();
      return json({ ok: true, escalations: escalations.results ?? [] });
    }

    // --------------------
    // STAFF: Bulk tag tickets
    // --------------------
    if (path === "/staff/bulk/tag" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const ticketIds = body?.ticketIds ?? [];
      const tags = body?.tags ?? [];
      if (!Array.isArray(ticketIds) || ticketIds.length === 0) return bad(400, "Missing ticketIds");
      if (!Array.isArray(tags) || tags.length === 0) return bad(400, "Missing tags");

      const result = await bulkTag(env, ticketIds.map(Number), tags, "staff");
      return json({ ok: true, ...result });
    }

    // --------------------
    // STAFF: Bulk close tickets
    // --------------------
    if (path === "/staff/bulk/close" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const ticketIds = body?.ticketIds ?? [];
      if (!Array.isArray(ticketIds) || ticketIds.length === 0) return bad(400, "Missing ticketIds");

      const result = await bulkClose(env, ticketIds.map(Number), "staff");
      return json({ ok: true, ...result });
    }

    // --------------------
    // STAFF: List ticket templates
    // --------------------
    if (path === "/staff/templates" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const templates = await env.DB.prepare("SELECT * FROM ticket_templates ORDER BY name").all<any>();
      return json({ ok: true, templates: templates.results ?? [] });
    }

    // --------------------
    // STAFF: Create ticket from template
    // --------------------
    if (path === "/staff/templates/create-ticket" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const templateCode = String(body?.templateCode ?? "");
      const clientId = body?.clientId ? Number(body.clientId) : null;

      if (!templateCode) return bad(400, "Missing templateCode");

      const result = await createFromTemplate(env, templateCode, clientId);
      if (!result) return bad(404, "Template not found");

      return json({ ok: true, ...result });
    }

    // --------------------
    // STAFF: Create ticket template
    // --------------------
    if (path === "/staff/templates/create" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const code = String(body?.code ?? "").toLowerCase().replace(/[^a-z0-9_]/g, "_");
      const name = String(body?.name ?? "");
      const subject = String(body?.subject ?? "");
      const defaultTags = JSON.stringify(body?.defaultTags ?? []);
      const playbookCodes = JSON.stringify(body?.playbookCodes ?? []);
      const slaTargetId = body?.slaTargetId ? Number(body.slaTargetId) : null;

      if (!code || !name || !subject) return bad(400, "Missing code/name/subject");

      await env.DB.prepare(
        "INSERT INTO ticket_templates (code, name, subject, default_tags, playbook_codes, sla_target_id, created_at) VALUES (?,?,?,?,?,?,?)"
      ).bind(code, name, subject, defaultTags, playbookCodes, slaTargetId, nowISO()).run();

      return json({ ok: true, code });
    }

    // --------------------
    // STAFF: Find duplicate tickets
    // --------------------
    if (path === "/staff/tickets/duplicates" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const clientId = Number(body?.clientId);
      const subject = String(body?.subject ?? "");

      if (!clientId || !subject) return bad(400, "Missing clientId/subject");

      const duplicates = await findDuplicates(env, clientId, subject);
      return json({ ok: true, duplicates });
    }

    // --------------------
    // STAFF: Link tickets (duplicate/related)
    // --------------------
    if (path === "/staff/tickets/link" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const ticketId = Number(body?.ticketId);
      const linkedTicketId = Number(body?.linkedTicketId);
      const linkType = String(body?.linkType ?? "related");

      if (!ticketId || !linkedTicketId) return bad(400, "Missing ticketId/linkedTicketId");
      if (!["duplicate", "related", "parent", "child"].includes(linkType)) return bad(400, "Invalid linkType");

      await env.DB.prepare(
        "INSERT OR IGNORE INTO ticket_links (ticket_id, linked_ticket_id, link_type, created_by, created_at) VALUES (?,?,?,?,?)"
      ).bind(ticketId, linkedTicketId, linkType, "staff", nowISO()).run();

      await writeEvent(env, ticketId, "TICKET_LINKED", "staff", "staff", { linkedTicketId, linkType });

      return json({ ok: true });
    }

    // --------------------
    // STAFF: List webhooks
    // --------------------
    if (path === "/staff/webhooks" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const hooks = await env.DB.prepare("SELECT id, name, url, events, active, created_at FROM webhooks ORDER BY id").all<any>();
      return json({ ok: true, webhooks: hooks.results ?? [] });
    }

    // --------------------
    // STAFF: Create webhook
    // --------------------
    if (path === "/staff/webhooks/create" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const name = String(body?.name ?? "");
      const hookUrl = String(body?.url ?? "");
      const secret = body?.secret ?? null;
      const events = JSON.stringify(body?.events ?? ["*"]);

      if (!name || !hookUrl) return bad(400, "Missing name/url");

      const result = await env.DB.prepare(
        "INSERT INTO webhooks (name, url, secret, events, active, created_at) VALUES (?,?,?,?,1,?)"
      ).bind(name, hookUrl, secret, events, nowISO()).run();

      return json({ ok: true, id: result.meta.last_row_id });
    }

    // --------------------
    // STAFF: Toggle webhook active
    // --------------------
    if (path.match(/^\/staff\/webhooks\/\d+\/toggle$/) && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const webhookId = Number(path.split("/")[3]);
      await env.DB.prepare("UPDATE webhooks SET active = 1 - active WHERE id=?").bind(webhookId).run();
      return json({ ok: true });
    }

    // --------------------
    // STAFF: Test webhook
    // --------------------
    if (path.match(/^\/staff\/webhooks\/\d+\/test$/) && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const webhookId = Number(path.split("/")[3]);
      
      const hook = await env.DB.prepare("SELECT * FROM webhooks WHERE id=?").bind(webhookId).first<any>();
      if (!hook) return bad(404, "Webhook not found");

      const testPayload = { test: true, timestamp: nowISO() };
      const body = JSON.stringify({ event: "TEST", ticketId: 0, payload: testPayload, timestamp: nowISO() });
      const headers: Record<string, string> = { "Content-Type": "application/json" };
      
      if (hook.secret) {
        const sig = await sha256Hex(hook.secret + body);
        headers["X-NoizyLab-Signature"] = sig;
      }

      let responseCode = 0;
      let responseBody = "";
      try {
        const resp = await fetch(hook.url, { method: "POST", headers, body });
        responseCode = resp.status;
        responseBody = await resp.text().catch(() => "");
      } catch (e: any) {
        responseBody = e.message ?? "fetch error";
      }

      return json({ ok: responseCode >= 200 && responseCode < 300, responseCode, responseBody: responseBody.slice(0, 500) });
    }

    // --------------------
    // STAFF: Bulk operations history
    // --------------------
    if (path === "/staff/bulk/history" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const limit = Number(url.searchParams.get("limit") ?? 50);
      const ops = await env.DB.prepare(
        "SELECT * FROM bulk_ops ORDER BY created_at DESC LIMIT ?"
      ).bind(limit).all<any>();
      return json({ ok: true, operations: ops.results ?? [] });
    }

    // --------------------
    // STAFF: Saved searches
    // --------------------
    if (path === "/staff/searches" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const searches = await env.DB.prepare("SELECT * FROM saved_searches ORDER BY name").all<any>();
      return json({ ok: true, searches: searches.results ?? [] });
    }

    // --------------------
    // STAFF: Save search
    // --------------------
    if (path === "/staff/searches/save" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const name = String(body?.name ?? "");
      const queryJson = JSON.stringify(body?.query ?? {});
      const staffId = body?.staffId ?? null;

      if (!name) return bad(400, "Missing name");

      const result = await env.DB.prepare(
        "INSERT INTO saved_searches (name, query_json, staff_id, created_at) VALUES (?,?,?,?)"
      ).bind(name, queryJson, staffId, nowISO()).run();

      return json({ ok: true, id: result.meta.last_row_id });
    }

    // --------------------
    // STAFF: At-risk clients (low health score)
    // --------------------
    if (path === "/staff/clients/at-risk" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const threshold = Number(url.searchParams.get("threshold") ?? 50);
      const clients = await env.DB.prepare(
        "SELECT ch.*, c.name, c.email FROM client_health ch JOIN clients c ON c.id = ch.client_id WHERE ch.health_score < ? ORDER BY ch.health_score ASC LIMIT 50"
      ).bind(threshold).all<any>();
      return json({ ok: true, clients: clients.results ?? [] });
    }

    // =====================================================
    // LEGENDARY ROUTES
    // =====================================================

    // --------------------
    // STAFF: AI Triage ticket
    // --------------------
    if (path.match(/^\/staff\/tickets\/\d+\/ai-triage$/) && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const ticketId = Number(path.split("/")[3]);
      
      const ticket = await env.DB.prepare("SELECT subject FROM tickets WHERE id=?").bind(ticketId).first<any>();
      if (!ticket) return bad(404, "Ticket not found");
      
      const body = await readJson(req);
      const suggestion = await aiTriageSuggestion(env, ticketId, ticket.subject, body?.description);
      
      // Also suggest KB articles
      const articles = await suggestArticlesForTicket(env, ticketId, ticket.subject);
      
      await auditLog(env, { actorType: "staff", action: "ai_triage", resourceType: "ticket", resourceId: String(ticketId) });
      
      return json({ ok: true, suggestion, suggestedArticles: articles });
    }

    // --------------------
    // STAFF: Accept/reject AI suggestion
    // --------------------
    if (path.match(/^\/staff\/ai-suggestions\/\d+\/(accept|reject)$/) && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const parts = path.split("/");
      const suggestionId = Number(parts[3]);
      const action = parts[4];
      
      await env.DB.prepare(
        "UPDATE ai_suggestions SET accepted=?, accepted_by=? WHERE id=?"
      ).bind(action === "accept" ? 1 : 0, "staff", suggestionId).run();
      
      return json({ ok: true });
    }

    // --------------------
    // KNOWLEDGE BASE: List articles
    // --------------------
    if (path === "/staff/kb/articles" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const status = url.searchParams.get("status") ?? "published";
      const articles = await env.DB.prepare(
        "SELECT id, slug, title, category, views, helpful_yes, helpful_no, status, created_at FROM kb_articles WHERE status=? OR ?='all' ORDER BY views DESC"
      ).bind(status, status).all<any>();
      return json({ ok: true, articles: articles.results ?? [] });
    }

    // --------------------
    // KNOWLEDGE BASE: Get article
    // --------------------
    if (path.match(/^\/staff\/kb\/articles\/[a-z0-9-]+$/) && method === "GET") {
      const slug = path.split("/").pop()!;
      const article = await env.DB.prepare("SELECT * FROM kb_articles WHERE slug=?").bind(slug).first<any>();
      if (!article) return bad(404, "Article not found");
      
      // Increment views
      await env.DB.prepare("UPDATE kb_articles SET views = views + 1 WHERE id=?").bind(article.id).run();
      
      return json({ ok: true, article });
    }

    // --------------------
    // KNOWLEDGE BASE: Create/update article
    // --------------------
    if (path === "/staff/kb/articles" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const slug = String(body?.slug ?? "").toLowerCase().replace(/[^a-z0-9-]/g, "-");
      const title = String(body?.title ?? "");
      const content = String(body?.content ?? "");
      const category = body?.category ?? null;
      const tagsJson = JSON.stringify(body?.tags ?? []);
      const status = body?.status ?? "draft";
      
      if (!slug || !title || !content) return bad(400, "Missing slug/title/content");
      
      const now = nowISO();
      await env.DB.prepare(
        "INSERT INTO kb_articles (slug, title, content, category, tags_json, status, created_by, created_at, updated_at) VALUES (?,?,?,?,?,?,?,?,?) " +
        "ON CONFLICT(slug) DO UPDATE SET title=excluded.title, content=excluded.content, category=excluded.category, tags_json=excluded.tags_json, status=excluded.status, updated_at=excluded.updated_at"
      ).bind(slug, title, content, category, tagsJson, status, "staff", now, now).run();
      
      await auditLog(env, { actorType: "staff", action: "create", resourceType: "kb_article", resourceId: slug });
      
      return json({ ok: true, slug });
    }

    // --------------------
    // KNOWLEDGE BASE: Search
    // --------------------
    if (path === "/staff/kb/search" && method === "GET") {
      const query = url.searchParams.get("q") ?? "";
      const articles = await searchKnowledgeBase(env, query, 10);
      return json({ ok: true, articles });
    }

    // --------------------
    // KNOWLEDGE BASE: Rate article
    // --------------------
    if (path.match(/^\/staff\/kb\/articles\/\d+\/rate$/) && method === "POST") {
      const articleId = Number(path.split("/")[4]);
      const body = await readJson(req);
      const helpful = !!body?.helpful;
      
      if (helpful) {
        await env.DB.prepare("UPDATE kb_articles SET helpful_yes = helpful_yes + 1 WHERE id=?").bind(articleId).run();
      } else {
        await env.DB.prepare("UPDATE kb_articles SET helpful_no = helpful_no + 1 WHERE id=?").bind(articleId).run();
      }
      
      return json({ ok: true });
    }

    // --------------------
    // APPOINTMENTS: List for staff
    // --------------------
    if (path === "/staff/appointments" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const staffId = url.searchParams.get("staffId") ?? "staff";
      const from = url.searchParams.get("from") ?? nowISO().slice(0, 10);
      const to = url.searchParams.get("to") ?? new Date(Date.now() + 30 * 86400_000).toISOString().slice(0, 10);
      
      const appointments = await env.DB.prepare(
        "SELECT a.*, c.name AS client_name, c.email AS client_email FROM appointments a LEFT JOIN clients c ON c.id = a.client_id WHERE a.staff_id=? AND a.start_at >= ? AND a.start_at <= ? ORDER BY a.start_at"
      ).bind(staffId, from + "T00:00:00Z", to + "T23:59:59Z").all<any>();
      
      return json({ ok: true, appointments: appointments.results ?? [] });
    }

    // --------------------
    // APPOINTMENTS: Schedule
    // --------------------
    if (path === "/staff/appointments/schedule" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      
      const result = await scheduleAppointment(env, {
        ticketId: body?.ticketId ? Number(body.ticketId) : undefined,
        clientId: body?.clientId ? Number(body.clientId) : undefined,
        staffId: body?.staffId ?? "staff",
        title: body?.title ?? "Appointment",
        description: body?.description,
        startAt: body?.startAt,
        endAt: body?.endAt,
        location: body?.location
      });
      
      if (!result.ok) return bad(400, result.error!);
      return json(result);
    }

    // --------------------
    // APPOINTMENTS: Get available slots
    // --------------------
    if (path === "/staff/appointments/slots" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const staffId = url.searchParams.get("staffId") ?? "staff";
      const date = url.searchParams.get("date") ?? new Date().toISOString().slice(0, 10);
      const duration = Number(url.searchParams.get("duration") ?? 60);
      
      const slots = await getAvailableSlots(env, staffId, date, duration);
      return json({ ok: true, slots });
    }

    // --------------------
    // APPOINTMENTS: Update status
    // --------------------
    if (path.match(/^\/staff\/appointments\/\d+\/status$/) && method === "PATCH") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const appointmentId = Number(path.split("/")[3]);
      const body = await readJson(req);
      const status = body?.status;
      
      if (!["scheduled", "confirmed", "completed", "cancelled", "no_show"].includes(status)) {
        return bad(400, "Invalid status");
      }
      
      await env.DB.prepare("UPDATE appointments SET status=?, updated_at=? WHERE id=?")
        .bind(status, nowISO(), appointmentId).run();
      
      return json({ ok: true });
    }

    // --------------------
    // STAFF AVAILABILITY: Set
    // --------------------
    if (path === "/staff/availability" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const staffId = body?.staffId ?? "staff";
      const availability = body?.availability ?? []; // [{dayOfWeek, startTime, endTime, isAvailable}]
      
      for (const slot of availability) {
        await env.DB.prepare(
          "INSERT INTO staff_availability (staff_id, day_of_week, start_time, end_time, is_available) VALUES (?,?,?,?,?) " +
          "ON CONFLICT(staff_id, day_of_week) DO UPDATE SET start_time=excluded.start_time, end_time=excluded.end_time, is_available=excluded.is_available"
        ).bind(staffId, slot.dayOfWeek, slot.startTime, slot.endTime, slot.isAvailable ? 1 : 0).run();
      }
      
      return json({ ok: true });
    }

    // --------------------
    // STAFF AVAILABILITY: Get
    // --------------------
    if (path === "/staff/availability" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const staffId = url.searchParams.get("staffId") ?? "staff";
      
      const availability = await env.DB.prepare(
        "SELECT * FROM staff_availability WHERE staff_id=? ORDER BY day_of_week"
      ).bind(staffId).all<any>();
      
      return json({ ok: true, availability: availability.results ?? [] });
    }

    // --------------------
    // TIME TRACKING: Start timer
    // --------------------
    if (path.match(/^\/staff\/tickets\/\d+\/timer\/start$/) && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const ticketId = Number(path.split("/")[3]);
      const body = await readJson(req);
      
      const result = await startTimer(env, ticketId, body?.staffId ?? "staff", body?.description);
      if (!result.ok) return bad(400, result.error!);
      return json(result);
    }

    // --------------------
    // TIME TRACKING: Stop timer
    // --------------------
    if (path.match(/^\/staff\/timers\/\d+\/stop$/) && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const timerId = Number(path.split("/")[3]);
      
      const result = await stopTimer(env, timerId);
      if (!result.ok) return bad(400, result.error!);
      return json(result);
    }

    // --------------------
    // TIME TRACKING: Get ticket time
    // --------------------
    if (path.match(/^\/staff\/tickets\/\d+\/time$/) && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const ticketId = Number(path.split("/")[3]);
      
      const time = await getTicketTime(env, ticketId);
      return json({ ok: true, ...time });
    }

    // --------------------
    // CANNED RESPONSES: List
    // --------------------
    if (path === "/staff/canned" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const responses = await env.DB.prepare(
        "SELECT * FROM canned_responses ORDER BY use_count DESC"
      ).all<any>();
      return json({ ok: true, responses: responses.results ?? [] });
    }

    // --------------------
    // CANNED RESPONSES: Get by code
    // --------------------
    if (path.match(/^\/staff\/canned\/[a-z0-9_]+$/) && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const code = path.split("/").pop()!;
      const response = await getCannedResponse(env, code);
      if (!response) return bad(404, "Not found");
      return json({ ok: true, response });
    }

    // --------------------
    // CANNED RESPONSES: Create
    // --------------------
    if (path === "/staff/canned" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const code = String(body?.code ?? "").toLowerCase().replace(/[^a-z0-9_]/g, "_");
      const name = String(body?.name ?? "");
      const content = String(body?.content ?? "");
      const category = body?.category ?? null;
      
      if (!code || !name || !content) return bad(400, "Missing code/name/content");
      
      await env.DB.prepare(
        "INSERT INTO canned_responses (code, name, content, category, created_by, created_at) VALUES (?,?,?,?,?,?)"
      ).bind(code, name, content, category, "staff", nowISO()).run();
      
      return json({ ok: true, code });
    }

    // --------------------
    // REPORTS: Generate
    // --------------------
    if (path === "/staff/reports/generate" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const type = String(body?.type ?? "");
      const params = body?.params ?? {};
      
      if (!["ticket_volume", "sla_compliance", "staff_performance", "client_satisfaction"].includes(type)) {
        return bad(400, "Invalid report type");
      }
      
      const report = await generateReport(env, type, params);
      return json({ ok: true, report });
    }

    // --------------------
    // API KEYS: List
    // --------------------
    if (path === "/staff/api-keys" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const keys = await env.DB.prepare(
        "SELECT id, name, prefix, scopes_json, last_used_at, expires_at, created_at FROM api_keys ORDER BY created_at DESC"
      ).all<any>();
      return json({ ok: true, keys: keys.results ?? [] });
    }

    // --------------------
    // API KEYS: Create
    // --------------------
    if (path === "/staff/api-keys" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const name = String(body?.name ?? "");
      const scopes = body?.scopes ?? ["*"];
      const expiresAt = body?.expiresAt ?? null;
      
      if (!name) return bad(400, "Missing name");
      
      const result = await generateApiKey(env, name, scopes, "staff", expiresAt);
      
      await auditLog(env, { actorType: "staff", action: "create", resourceType: "api_key", resourceId: result.prefix });
      
      return json({ ok: true, key: result.key, prefix: result.prefix, warning: "Save this key now - it won't be shown again!" });
    }

    // --------------------
    // API KEYS: Delete
    // --------------------
    if (path.match(/^\/staff\/api-keys\/\d+$/) && method === "DELETE") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const keyId = Number(path.split("/").pop());
      await env.DB.prepare("DELETE FROM api_keys WHERE id=?").bind(keyId).run();
      return json({ ok: true });
    }

    // --------------------
    // AUDIT LOG: Query
    // --------------------
    if (path === "/staff/audit" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const resourceType = url.searchParams.get("resourceType");
      const resourceId = url.searchParams.get("resourceId");
      const actorId = url.searchParams.get("actorId");
      const limit = Number(url.searchParams.get("limit") ?? 100);
      
      let query = "SELECT * FROM audit_log WHERE 1=1";
      const params: any[] = [];
      
      if (resourceType) { query += " AND resource_type=?"; params.push(resourceType); }
      if (resourceId) { query += " AND resource_id=?"; params.push(resourceId); }
      if (actorId) { query += " AND actor_id=?"; params.push(actorId); }
      
      query += " ORDER BY created_at DESC LIMIT ?";
      params.push(limit);
      
      const logs = await env.DB.prepare(query).bind(...params).all<any>();
      return json({ ok: true, logs: logs.results ?? [] });
    }

    // --------------------
    // SURVEYS: Send satisfaction survey
    // --------------------
    if (path.match(/^\/staff\/tickets\/\d+\/survey$/) && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const ticketId = Number(path.split("/")[3]);
      
      const result = await sendSurvey(env, ticketId);
      if (!result.ok) return bad(400, result.error!);
      return json(result);
    }

    // --------------------
    // PUBLIC: Submit survey response
    // --------------------
    if (path.match(/^\/public\/survey\/[a-f0-9]+$/) && method === "POST") {
      const token = path.split("/").pop()!;
      const body = await readJson(req);
      const rating = Number(body?.rating);
      const feedback = body?.feedback ?? null;
      
      if (rating < 1 || rating > 5) return bad(400, "Rating must be 1-5");
      
      const survey = await env.DB.prepare("SELECT * FROM surveys WHERE token=?").bind(token).first<any>();
      if (!survey) return bad(404, "Survey not found");
      if (survey.submitted_at) return bad(400, "Survey already submitted");
      
      await env.DB.prepare(
        "UPDATE surveys SET rating=?, feedback=?, submitted_at=? WHERE token=?"
      ).bind(rating, feedback, nowISO(), token).run();
      
      // Update client sentiment
      const ticket = await env.DB.prepare("SELECT client_id FROM tickets WHERE id=?").bind(survey.ticket_id).first<any>();
      if (ticket?.client_id) {
        const score = rating >= 4 ? 2 : rating === 3 ? 0 : rating === 2 ? -1 : -2;
        await env.DB.prepare(
          "INSERT INTO client_sentiment (client_id, ticket_id, score, source, notes, created_at) VALUES (?,?,?,?,?,?)"
        ).bind(ticket.client_id, survey.ticket_id, score, "survey", feedback, nowISO()).run();
        await updateClientHealth(env, ticket.client_id);
      }
      
      return json({ ok: true, message: "Thank you for your feedback!" });
    }

    // --------------------
    // CHAT INTEGRATIONS: List
    // --------------------
    if (path === "/staff/integrations/chat" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const integrations = await env.DB.prepare(
        "SELECT id, platform, workspace_id, channel_id, channel_name, events_json, active, created_at FROM chat_integrations ORDER BY created_at DESC"
      ).all<any>();
      return json({ ok: true, integrations: integrations.results ?? [] });
    }

    // --------------------
    // CHAT INTEGRATIONS: Create
    // --------------------
    if (path === "/staff/integrations/chat" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      
      await env.DB.prepare(
        "INSERT INTO chat_integrations (platform, workspace_id, channel_id, channel_name, webhook_url, bot_token, events_json, created_at) VALUES (?,?,?,?,?,?,?,?)"
      ).bind(
        body?.platform ?? "slack",
        body?.workspaceId ?? "",
        body?.channelId ?? "",
        body?.channelName ?? null,
        body?.webhookUrl ?? null,
        body?.botToken ?? null,
        JSON.stringify(body?.events ?? ["*"]),
        nowISO()
      ).run();
      
      return json({ ok: true });
    }

    // --------------------
    // NOTIFICATIONS: Process queue (manual trigger)
    // --------------------
    if (path === "/staff/notifications/process" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const limit = Number(body?.limit ?? 50);
      
      const result = await processNotifications(env, limit);
      return json({ ok: true, ...result });
    }

    // --------------------
    // EMAIL TEMPLATES: List
    // --------------------
    if (path === "/staff/email-templates" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const templates = await env.DB.prepare("SELECT * FROM email_templates ORDER BY name").all<any>();
      return json({ ok: true, templates: templates.results ?? [] });
    }

    // --------------------
    // EMAIL TEMPLATES: Create/Update
    // --------------------
    if (path === "/staff/email-templates" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const code = String(body?.code ?? "");
      const name = String(body?.name ?? "");
      const subject = String(body?.subject ?? "");
      const bodyText = String(body?.bodyText ?? "");
      const bodyHtml = body?.bodyHtml ?? null;
      const variables = JSON.stringify(body?.variables ?? []);
      
      if (!code || !name || !subject || !bodyText) return bad(400, "Missing required fields");
      
      const now = nowISO();
      await env.DB.prepare(
        "INSERT INTO email_templates (code, name, subject, body_text, body_html, variables_json, created_at, updated_at) VALUES (?,?,?,?,?,?,?,?) " +
        "ON CONFLICT(code) DO UPDATE SET name=excluded.name, subject=excluded.subject, body_text=excluded.body_text, body_html=excluded.body_html, variables_json=excluded.variables_json, updated_at=excluded.updated_at"
      ).bind(code, name, subject, bodyText, bodyHtml, variables, now, now).run();
      
      return json({ ok: true, code });
    }

    // --------------------
    // GDPR: Request data export/deletion
    // --------------------
    if (path === "/staff/gdpr/request" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const clientId = Number(body?.clientId);
      const requestType = body?.type ?? "export"; // export, delete, restrict
      
      if (!clientId) return bad(400, "Missing clientId");
      if (!["export", "delete", "restrict"].includes(requestType)) return bad(400, "Invalid type");
      
      await env.DB.prepare(
        "INSERT INTO gdpr_requests (client_id, request_type, status, requested_at) VALUES (?,?,?,?)"
      ).bind(clientId, requestType, "pending", nowISO()).run();
      
      await auditLog(env, { actorType: "staff", action: "gdpr_request", resourceType: "client", resourceId: String(clientId), changes: { type: requestType } });
      
      return json({ ok: true });
    }

    // --------------------
    // GDPR: List requests
    // --------------------
    if (path === "/staff/gdpr/requests" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const requests = await env.DB.prepare(
        "SELECT g.*, c.name, c.email FROM gdpr_requests g JOIN clients c ON c.id = g.client_id ORDER BY g.requested_at DESC"
      ).all<any>();
      return json({ ok: true, requests: requests.results ?? [] });
    }

    // --------------------
    // TIME TRACKING: Start timer
    // --------------------
    if (path === "/staff/timer/start" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const ticketId = Number(body?.ticketId);
      const staffId = String(body?.staffId ?? "");
      const description = body?.description;
      
      if (!ticketId || !staffId) return bad(400, "Missing ticketId or staffId");
      
      const result = await startTimer(env, ticketId, staffId, description);
      return json(result);
    }

    // --------------------
    // TIME TRACKING: Stop timer
    // --------------------
    if (path === "/staff/timer/stop" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const timerId = Number(body?.timerId);
      
      if (!timerId) return bad(400, "Missing timerId");
      
      const result = await stopTimer(env, timerId);
      return json(result);
    }

    // --------------------
    // TIME TRACKING: Get ticket time summary
    // --------------------
    if (path.match(/^\/staff\/tickets\/\d+\/time$/) && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const ticketId = Number(path.split("/")[3]);
      
      const summary = await getTicketTime(env, ticketId);
      const timers = await env.DB.prepare(
        "SELECT * FROM ticket_timers WHERE ticket_id=? ORDER BY started_at DESC"
      ).bind(ticketId).all<any>();
      
      return json({ ok: true, ...summary, timers: timers.results ?? [] });
    }

    // --------------------
    // CANNED RESPONSES: List
    // --------------------
    if (path === "/staff/canned" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const category = url.searchParams.get("category");
      
      let query = "SELECT * FROM canned_responses";
      const params: any[] = [];
      
      if (category) {
        query += " WHERE category=?";
        params.push(category);
      }
      
      query += " ORDER BY use_count DESC, title ASC";
      
      const responses = await env.DB.prepare(query).bind(...params).all<any>();
      return json({ ok: true, responses: responses.results ?? [] });
    }

    // --------------------
    // CANNED RESPONSES: Create
    // --------------------
    if (path === "/staff/canned/create" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const code = String(body?.code ?? "").toUpperCase();
      const title = String(body?.title ?? "");
      const responseBody = String(body?.body ?? "");
      const category = body?.category ?? null;
      const variablesJson = JSON.stringify(body?.variables ?? []);
      
      if (!code || !title || !responseBody) return bad(400, "Missing required fields");
      
      await env.DB.prepare(
        "INSERT INTO canned_responses (code, title, body, category, variables_json, created_at) VALUES (?,?,?,?,?,?)"
      ).bind(code, title, responseBody, category, variablesJson, nowISO()).run();
      
      return json({ ok: true, code });
    }

    // --------------------
    // CANNED RESPONSES: Get by code
    // --------------------
    if (path.match(/^\/staff\/canned\/[A-Z0-9_]+$/) && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const code = path.split("/").pop()!.toUpperCase();
      
      const response = await getCannedResponse(env, code);
      if (!response) return bad(404, "Canned response not found");
      
      return json({ ok: true, response });
    }

    // --------------------
    // SURVEY: Send satisfaction survey
    // --------------------
    if (path === "/staff/survey/send" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const ticketId = Number(body?.ticketId);
      
      if (!ticketId) return bad(400, "Missing ticketId");
      
      const result = await sendSurvey(env, ticketId);
      if (!result.ok) return bad(400, result.error!);
      
      return json(result);
    }

    // --------------------
    // SURVEY: Get statistics
    // --------------------
    if (path === "/staff/survey/stats" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      
      const stats = await env.DB.prepare(`
        SELECT 
          COUNT(*) AS total,
          COUNT(submitted_at) AS submitted,
          AVG(rating) AS avg_rating,
          SUM(CASE WHEN rating >= 4 THEN 1 ELSE 0 END) AS satisfied,
          SUM(CASE WHEN rating <= 2 THEN 1 ELSE 0 END) AS unsatisfied
        FROM surveys
        WHERE created_at >= date('now', '-30 days')
      `).first<any>();
      
      return json({
        ok: true,
        total: stats?.total ?? 0,
        submitted: stats?.submitted ?? 0,
        responseRate: stats?.total ? Math.round((stats.submitted / stats.total) * 100) : 0,
        avgRating: stats?.avg_rating ? Number(stats.avg_rating.toFixed(2)) : 0,
        satisfactionRate: stats?.submitted ? Math.round((stats.satisfied / stats.submitted) * 100) : 0
      });
    }

    // --------------------
    // AUDIT LOG: Query with action filter
    // --------------------
    if (path === "/staff/audit/log" && method === "GET") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const resourceType = url.searchParams.get("resourceType");
      const resourceId = url.searchParams.get("resourceId");
      const actorId = url.searchParams.get("actorId");
      const action = url.searchParams.get("action");
      const limit = Number(url.searchParams.get("limit") ?? 100);
      
      let query = "SELECT * FROM audit_log WHERE 1=1";
      const params: any[] = [];
      
      if (resourceType) { query += " AND resource_type=?"; params.push(resourceType); }
      if (resourceId) { query += " AND resource_id=?"; params.push(resourceId); }
      if (actorId) { query += " AND actor_id=?"; params.push(actorId); }
      if (action) { query += " AND action LIKE ?"; params.push(`%${action}%`); }
      
      query += " ORDER BY created_at DESC LIMIT ?";
      params.push(limit);
      
      const logs = await env.DB.prepare(query).bind(...params).all<any>();
      return json({ ok: true, logs: logs.results ?? [] });
    }

    // --------------------
    // GDPR: Export user data
    // --------------------
    if (path === "/staff/gdpr/export" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const email = String(body?.email ?? "");
      
      if (!email) return bad(400, "Missing email");
      
      // Find client
      const client = await env.DB.prepare("SELECT * FROM clients WHERE email=?").bind(email).first<any>();
      if (!client) return bad(404, "Client not found");
      
      const data = await exportUserData(env, client.id);
      
      // Log export
      await auditLog(env, {
        actorType: "staff",
        action: "gdpr_export",
        resourceType: "client",
        resourceId: String(client.id)
      });
      
      return json({ ok: true, data });
    }

    // --------------------
    // GDPR: Delete user data
    // --------------------
    if (path === "/staff/gdpr/delete" && method === "POST") {
      if (!(await staffAuthPlaceholder(req))) return bad(403, "Forbidden");
      const body = await readJson(req);
      const email = String(body?.email ?? "");
      
      if (!email) return bad(400, "Missing email");
      
      // Find client
      const client = await env.DB.prepare("SELECT * FROM clients WHERE email=?").bind(email).first<any>();
      if (!client) return bad(404, "Client not found");
      
      const result = await deleteUserData(env, client.id);
      
      // Log deletion
      await auditLog(env, {
        actorType: "staff",
        action: "gdpr_delete",
        resourceType: "client",
        resourceId: String(client.id)
      });
      
      return json({ ok: true, ...result });
    }

    return bad(404, "No route");
  },

  async scheduled(event: ScheduledController, env: Env, ctx: ExecutionContext) {
    // enqueue jobs every run
    await (env as any).OPS_QUEUE.send({ type: "retention_purge", limit: 200 });
    await (env as any).OPS_QUEUE.send({ type: "followups_run", limit: 200 });
    await (env as any).OPS_QUEUE.send({ type: "metrics_rollup" });
    await (env as any).OPS_QUEUE.send({ type: "auto_close", limit: 50 });
    await (env as any).OPS_QUEUE.send({ type: "control_expire" });
    await (env as any).OPS_QUEUE.send({ type: "escalations", limit: 50 });
    await (env as any).OPS_QUEUE.send({ type: "notifications", limit: 100 });
    await (env as any).OPS_QUEUE.send({ type: "appointment_reminders" });
  },

  async queue(batch: MessageBatch<any>, env: Env, ctx: ExecutionContext) {
    for (const msg of batch.messages) {
      try {
        const j = msg.body;
        if (j.type === "retention_purge") await runRetention(env, j.limit ?? 200);
        if (j.type === "followups_run") await runFollowups(env, j.limit ?? 200);
        if (j.type === "metrics_rollup") await rollupMetrics(env);
        if (j.type === "auto_close") await runAutoClose(env, j.limit ?? 50);
        if (j.type === "escalations") await runEscalations(env, j.limit ?? 50);
        if (j.type === "notifications") await processNotifications(env, j.limit ?? 100);
        if (j.type === "appointment_reminders") {
          // Send reminders for appointments in next hour
          const soon = new Date(Date.now() + 60 * 60_000).toISOString();
          const appointments = await env.DB.prepare(
            "SELECT a.*, c.email, c.name FROM appointments a LEFT JOIN clients c ON c.id = a.client_id WHERE a.status IN ('scheduled','confirmed') AND a.reminder_sent=0 AND a.start_at <= ?"
          ).bind(soon).all<any>();
          for (const apt of (appointments.results ?? [])) {
            if (apt.email) {
              await sendEmail(env, apt.email, "appointment_reminder", {
                client_name: apt.name || "there",
                date: apt.start_at.slice(0, 10),
                time: apt.start_at.slice(11, 16),
                location: apt.location || "Remote"
              });
            }
            await env.DB.prepare("UPDATE appointments SET reminder_sent=1 WHERE id=?").bind(apt.id).run();
          }
        }
        if (j.type === "control_expire") {
          const now = nowISO();
          const stale = await env.DB.prepare(
            "SELECT id, ticket_id FROM control_lanes WHERE status='active' AND expires_at <= ?"
          ).bind(now).all<any>();
          for (const lane of (stale.results ?? [])) {
            await env.DB.prepare("UPDATE control_lanes SET status='expired' WHERE id=?").bind(lane.id).run();
            await writeEvent(env, lane.ticket_id, "CONTROL_EXPIRED", "system", "system", { controlLaneId: lane.id });
          }
        }

        msg.ack();
      } catch (e) {
        // retry until max_retries then DLQ
        msg.retry();
      }
    }
  }
};
