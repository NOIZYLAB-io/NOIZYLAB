// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS v1 - Staff Routes (Access-gated)
// Full control: status, messages, live, playbooks, AI
// ═══════════════════════════════════════════════════════════════════════════

import { Hono } from 'hono';
import { Env, Ticket, TicketStatus, Playbook, LiveRoom, PLAYBOOK_NAMES, PERSONA_NAMES } from '../types';
import { verifyAccess, generateId, generateJoinCode, addMinutes, now, json, error, notFound, unauthorized, sanitize } from '../lib/utils';
import { logEvent, getTimeline } from '../lib/events';
import { triageTicket, summarizeSession } from '../lib/ai';

const app = new Hono<{ Bindings: Env }>();

// ───────────────────────────────────────────────────────────────────────────
// Middleware: Verify Cloudflare Access
// ───────────────────────────────────────────────────────────────────────────
app.use('*', async (c, next) => {
  const { valid, email } = await verifyAccess(c.req.raw, c.env.ACCESS_AUD);
  if (!valid) {
    return unauthorized('Access denied. Staff login required.');
  }
  c.set('staffEmail', email);
  await next();
});

// ═══════════════════════════════════════════════════════════════════════════
// GET /staff/tickets - List tickets with filters
// ═══════════════════════════════════════════════════════════════════════════
app.get('/tickets', async (c) => {
  const status = c.req.query('status') as TicketStatus | undefined;
  const limit = parseInt(c.req.query('limit') || '50');
  const offset = parseInt(c.req.query('offset') || '0');
  
  let query = 'SELECT * FROM tickets';
  const params: (string | number)[] = [];
  
  if (status) {
    query += ' WHERE status = ?';
    params.push(status);
  }
  
  query += ' ORDER BY created_at DESC LIMIT ? OFFSET ?';
  params.push(limit, offset);
  
  const stmt = c.env.DB.prepare(query);
  const result = await stmt.bind(...params).all<Ticket>();
  
  // Enrich with persona/tags
  const tickets = await Promise.all(result.results.map(async (ticket) => {
    const pt = await c.env.DB.prepare(`
      SELECT persona, tags_json, suggested_playbook, confidence 
      FROM persona_tags WHERE ticket_id = ?
    `).bind(ticket.id).first();
    
    return {
      ...ticket,
      persona: pt ? { id: pt.persona, name: PERSONA_NAMES[pt.persona as keyof typeof PERSONA_NAMES] } : null,
      tags: pt ? JSON.parse(pt.tags_json as string) : [],
      suggested_playbook: pt?.suggested_playbook,
      ai_confidence: pt?.confidence,
    };
  }));
  
  return json({ tickets, total: result.results.length });
});

// ═══════════════════════════════════════════════════════════════════════════
// GET /staff/tickets/:id - Get single ticket with full timeline
// ═══════════════════════════════════════════════════════════════════════════
app.get('/tickets/:id', async (c) => {
  const id = c.req.param('id');
  
  const ticket = await c.env.DB.prepare(`
    SELECT * FROM tickets WHERE id = ? OR public_id = ?
  `).bind(id, id).first<Ticket>();
  
  if (!ticket) {
    return notFound('Ticket not found');
  }
  
  const events = await getTimeline(c.env.DB, ticket.id);
  
  const pt = await c.env.DB.prepare(`
    SELECT * FROM persona_tags WHERE ticket_id = ?
  `).bind(ticket.id).first();
  
  const uploads = await c.env.DB.prepare(`
    SELECT * FROM uploads WHERE ticket_id = ?
  `).bind(ticket.id).all();
  
  return json({
    ticket,
    persona: pt ? { id: pt.persona, name: PERSONA_NAMES[pt.persona as keyof typeof PERSONA_NAMES] } : null,
    tags: pt ? JSON.parse(pt.tags_json as string) : [],
    suggested_playbook: pt?.suggested_playbook ? { 
      id: pt.suggested_playbook, 
      name: PLAYBOOK_NAMES[pt.suggested_playbook as keyof typeof PLAYBOOK_NAMES] 
    } : null,
    ai_confidence: pt?.confidence,
    timeline: events,
    uploads: uploads.results,
  });
});

// ═══════════════════════════════════════════════════════════════════════════
// PATCH /staff/tickets/:id/status - Change ticket status
// ═══════════════════════════════════════════════════════════════════════════
app.patch('/tickets/:id/status', async (c) => {
  const id = c.req.param('id');
  const staffEmail = c.get('staffEmail');
  const { status } = await c.req.json<{ status: TicketStatus }>();
  
  const validStatuses: TicketStatus[] = ['TRIAGE', 'WAITING_CLIENT', 'WAITING_PARTS', 'SCHEDULED', 'IN_PROGRESS', 'DONE', 'BILLING'];
  if (!validStatuses.includes(status)) {
    return error('Invalid status');
  }
  
  const ticket = await c.env.DB.prepare(`
    SELECT * FROM tickets WHERE id = ?
  `).bind(id).first<Ticket>();
  
  if (!ticket) {
    return notFound('Ticket not found');
  }
  
  const oldStatus = ticket.status;
  
  await c.env.DB.prepare(`
    UPDATE tickets SET status = ?, updated_at = ? WHERE id = ?
  `).bind(status, now(), id).run();
  
  // Log status change
  await logEvent(c.env.DB, id, 'STATUS_CHANGED', 'STAFF', staffEmail, {
    from: oldStatus,
    to: status,
  });
  
  // If resolved, set resolved_at
  if (status === 'DONE') {
    await c.env.DB.prepare(`
      UPDATE tickets SET resolved_at = ? WHERE id = ?
    `).bind(now(), id).run();
    
    await logEvent(c.env.DB, id, 'RESOLVED', 'STAFF', staffEmail, {});
  }
  
  return json({ success: true, old_status: oldStatus, new_status: status });
});

// ═══════════════════════════════════════════════════════════════════════════
// POST /staff/tickets/:id/message - Send message to client
// ═══════════════════════════════════════════════════════════════════════════
app.post('/tickets/:id/message', async (c) => {
  const id = c.req.param('id');
  const staffEmail = c.get('staffEmail');
  const { message, send_email } = await c.req.json<{ message: string; send_email?: boolean }>();
  
  if (!message) {
    return error('Message required');
  }
  
  const ticket = await c.env.DB.prepare(`
    SELECT * FROM tickets WHERE id = ?
  `).bind(id).first<Ticket>();
  
  if (!ticket) {
    return notFound('Ticket not found');
  }
  
  // Log message event
  await logEvent(c.env.DB, id, 'MESSAGE_OUT', 'STAFF', staffEmail, {
    message: sanitize(message, 5000),
    send_email: send_email || false,
  });
  
  // Update status to WAITING_CLIENT if in TRIAGE
  if (ticket.status === 'TRIAGE') {
    await c.env.DB.prepare(`
      UPDATE tickets SET status = 'WAITING_CLIENT', updated_at = ? WHERE id = ?
    `).bind(now(), id).run();
    
    await logEvent(c.env.DB, id, 'STATUS_CHANGED', 'SYSTEM', null, {
      from: 'TRIAGE',
      to: 'WAITING_CLIENT',
      reason: 'Message sent to client',
    });
  }
  
  // TODO: If send_email, trigger email via Cloudflare Email or external service
  
  return json({ success: true });
});

// ═══════════════════════════════════════════════════════════════════════════
// POST /staff/live/create - Create live help session
// ═══════════════════════════════════════════════════════════════════════════
app.post('/live/create', async (c) => {
  const staffEmail = c.get('staffEmail');
  const { ticket_id, mode } = await c.req.json<{ ticket_id: string; mode?: 'video' | 'audio' | 'chat' }>();
  
  if (!ticket_id) {
    return error('ticket_id required');
  }
  
  const ticket = await c.env.DB.prepare(`
    SELECT * FROM tickets WHERE id = ?
  `).bind(ticket_id).first<Ticket>();
  
  if (!ticket) {
    return notFound('Ticket not found');
  }
  
  const roomId = generateId();
  const joinCode = generateJoinCode();
  const expiresAt = addMinutes(10); // Code expires in 10 minutes
  
  await c.env.DB.prepare(`
    INSERT INTO live_rooms (id, ticket_id, code, mode, created_by, expires_at)
    VALUES (?, ?, ?, ?, ?, ?)
  `).bind(roomId, ticket_id, joinCode, mode || 'video', staffEmail, expiresAt).run();
  
  // Log event
  await logEvent(c.env.DB, ticket_id, 'LIVE_CREATED', 'STAFF', staffEmail, {
    room_id: roomId,
    mode: mode || 'video',
    join_code: joinCode,
    expires_at: expiresAt,
  });
  
  return json({
    room_id: roomId,
    join_code: joinCode,
    expires_at: expiresAt,
    ws_url: `/ws/room/${roomId}?token=${generateId()}&role=staff`,
  });
});

// ═══════════════════════════════════════════════════════════════════════════
// POST /staff/playbooks/apply - Apply a playbook to ticket
// ═══════════════════════════════════════════════════════════════════════════
app.post('/playbooks/apply', async (c) => {
  const staffEmail = c.get('staffEmail');
  const { ticket_id, playbook_id } = await c.req.json<{ ticket_id: string; playbook_id: Playbook }>();
  
  if (!ticket_id || !playbook_id) {
    return error('ticket_id and playbook_id required');
  }
  
  if (!PLAYBOOK_NAMES[playbook_id]) {
    return error('Invalid playbook_id');
  }
  
  const ticket = await c.env.DB.prepare(`
    SELECT * FROM tickets WHERE id = ?
  `).bind(ticket_id).first<Ticket>();
  
  if (!ticket) {
    return notFound('Ticket not found');
  }
  
  // Log playbook started
  await logEvent(c.env.DB, ticket_id, 'PLAYBOOK_STARTED', 'STAFF', staffEmail, {
    playbook_id,
    playbook_name: PLAYBOOK_NAMES[playbook_id],
  });
  
  // Update status to IN_PROGRESS
  if (ticket.status !== 'IN_PROGRESS') {
    await c.env.DB.prepare(`
      UPDATE tickets SET status = 'IN_PROGRESS', updated_at = ? WHERE id = ?
    `).bind(now(), ticket_id).run();
    
    await logEvent(c.env.DB, ticket_id, 'STATUS_CHANGED', 'SYSTEM', null, {
      from: ticket.status,
      to: 'IN_PROGRESS',
      reason: `Playbook ${playbook_id} started`,
    });
  }
  
  return json({ 
    success: true, 
    playbook: { id: playbook_id, name: PLAYBOOK_NAMES[playbook_id] }
  });
});

// ═══════════════════════════════════════════════════════════════════════════
// POST /staff/playbooks/complete - Mark playbook as completed
// ═══════════════════════════════════════════════════════════════════════════
app.post('/playbooks/complete', async (c) => {
  const staffEmail = c.get('staffEmail');
  const { ticket_id, playbook_id, notes } = await c.req.json<{ ticket_id: string; playbook_id: Playbook; notes?: string }>();
  
  if (!ticket_id || !playbook_id) {
    return error('ticket_id and playbook_id required');
  }
  
  await logEvent(c.env.DB, ticket_id, 'PLAYBOOK_COMPLETED', 'STAFF', staffEmail, {
    playbook_id,
    playbook_name: PLAYBOOK_NAMES[playbook_id],
    notes: notes ? sanitize(notes, 2000) : null,
  });
  
  return json({ success: true });
});

// ═══════════════════════════════════════════════════════════════════════════
// POST /staff/ai/triage - Run AI triage on ticket
// ═══════════════════════════════════════════════════════════════════════════
app.post('/ai/triage', async (c) => {
  const staffEmail = c.get('staffEmail');
  const { ticket_id } = await c.req.json<{ ticket_id: string }>();
  
  if (!ticket_id) {
    return error('ticket_id required');
  }
  
  const ticket = await c.env.DB.prepare(`
    SELECT * FROM tickets WHERE id = ?
  `).bind(ticket_id).first<Ticket>();
  
  if (!ticket) {
    return notFound('Ticket not found');
  }
  
  // Run AI triage
  const result = await triageTicket(c.env.AI, ticket.subject, ticket.description);
  
  // Upsert persona_tags
  await c.env.DB.prepare(`
    INSERT INTO persona_tags (ticket_id, persona, tags_json, suggested_playbook, confidence, updated_at)
    VALUES (?, ?, ?, ?, ?, ?)
    ON CONFLICT(ticket_id) DO UPDATE SET
      persona = excluded.persona,
      tags_json = excluded.tags_json,
      suggested_playbook = excluded.suggested_playbook,
      confidence = excluded.confidence,
      updated_at = excluded.updated_at
  `).bind(
    ticket_id,
    result.persona,
    JSON.stringify(result.tags),
    result.playbook,
    result.confidence,
    now()
  ).run();
  
  // Log AI triage event
  await logEvent(c.env.DB, ticket_id, 'AI_TRIAGE', 'STAFF', staffEmail, {
    persona: result.persona,
    persona_name: PERSONA_NAMES[result.persona],
    tags: result.tags,
    playbook: result.playbook,
    playbook_name: PLAYBOOK_NAMES[result.playbook],
    next_question: result.next_question,
    calm_message: result.calm_message,
    confidence: result.confidence,
  });
  
  return json({
    persona: { id: result.persona, name: PERSONA_NAMES[result.persona] },
    tags: result.tags,
    playbook: { id: result.playbook, name: PLAYBOOK_NAMES[result.playbook] },
    next_question: result.next_question,
    calm_message: result.calm_message,
    confidence: result.confidence,
  });
});

// ═══════════════════════════════════════════════════════════════════════════
// POST /staff/ai/summarize - Summarize ticket session
// ═══════════════════════════════════════════════════════════════════════════
app.post('/ai/summarize', async (c) => {
  const staffEmail = c.get('staffEmail');
  const { ticket_id } = await c.req.json<{ ticket_id: string }>();
  
  if (!ticket_id) {
    return error('ticket_id required');
  }
  
  const ticket = await c.env.DB.prepare(`
    SELECT * FROM tickets WHERE id = ?
  `).bind(ticket_id).first<Ticket>();
  
  if (!ticket) {
    return notFound('Ticket not found');
  }
  
  // Get all events for this ticket
  const events = await getTimeline(c.env.DB, ticket_id);
  
  // Run AI summary
  const result = await summarizeSession(c.env.AI, events);
  
  // Log AI summary event
  await logEvent(c.env.DB, ticket_id, 'AI_SUMMARIZE', 'STAFF', staffEmail, {
    summary: result.summary,
    key_points: result.key_points,
    next_steps: result.next_steps,
    sentiment: result.sentiment,
  });
  
  return json(result);
});

export default app;
