// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS v1 - Public Routes
// 3-button UX: Create Ticket / Check Status / Start Live Help
// ═══════════════════════════════════════════════════════════════════════════

import { Hono } from 'hono';
import { Env, CreateTicketRequest, CreateTicketResponse, StatusResponse, JoinLiveRequest, JoinLiveResponse, Ticket, TicketAccess, LiveRoom } from '../types';
import { generateId, generatePublicId, generateSecret, hashSecret, verifySecret, verifyTurnstile, isExpired, now, json, error, notFound, sanitize, validateEmail } from '../lib/utils';
import { logEvent, getTimeline, formatPublicTimeline } from '../lib/events';

const app = new Hono<{ Bindings: Env }>();

// ═══════════════════════════════════════════════════════════════════════════
// POST /public/tickets - Create a new ticket (Turnstile protected)
// ═══════════════════════════════════════════════════════════════════════════
app.post('/tickets', async (c) => {
  const body = await c.req.json<CreateTicketRequest>();
  
  // Validate Turnstile
  const ip = c.req.header('CF-Connecting-IP');
  const turnstileValid = await verifyTurnstile(body.turnstile_token, c.env.TURNSTILE_SECRET, ip);
  if (!turnstileValid) {
    return error('Bot check failed. Please try again.', 403);
  }
  
  // Validate required fields
  if (!body.name || !body.email || !body.subject || !body.description) {
    return error('Missing required fields: name, email, subject, description');
  }
  
  if (!validateEmail(body.email)) {
    return error('Invalid email address');
  }
  
  // Generate IDs and secret
  const ticketId = generateId();
  const publicId = generatePublicId();
  const secret = generateSecret();
  const secretHash = await hashSecret(secret);
  
  // Create ticket
  await c.env.DB.prepare(`
    INSERT INTO tickets (id, public_id, client_name, client_email, client_phone, subject, description, channel)
    VALUES (?, ?, ?, ?, ?, ?, ?, 'web')
  `).bind(
    ticketId,
    publicId,
    sanitize(body.name, 100),
    sanitize(body.email, 200),
    body.phone ? sanitize(body.phone, 20) : null,
    sanitize(body.subject, 200),
    sanitize(body.description, 5000)
  ).run();
  
  // Create access record
  await c.env.DB.prepare(`
    INSERT INTO ticket_access (ticket_id, secret_hash) VALUES (?, ?)
  `).bind(ticketId, secretHash).run();
  
  // Log CREATED event
  await logEvent(c.env.DB, ticketId, 'CREATED', 'PUBLIC', body.email, {
    channel: 'web',
    subject: body.subject,
  });
  
  const response: CreateTicketResponse = {
    ticketPublicId: publicId,
    secret,
  };
  
  return json(response, 201);
});

// ═══════════════════════════════════════════════════════════════════════════
// GET /public/status/:publicId - Check ticket status (secret required)
// ═══════════════════════════════════════════════════════════════════════════
app.get('/status/:publicId', async (c) => {
  const publicId = c.req.param('publicId');
  const secret = c.req.query('secret');
  
  if (!secret) {
    return error('Secret required', 401);
  }
  
  // Get ticket
  const ticket = await c.env.DB.prepare(`
    SELECT * FROM tickets WHERE public_id = ?
  `).bind(publicId).first<Ticket>();
  
  if (!ticket) {
    return notFound('Ticket not found');
  }
  
  // Verify secret
  const access = await c.env.DB.prepare(`
    SELECT * FROM ticket_access WHERE ticket_id = ?
  `).bind(ticket.id).first<TicketAccess>();
  
  if (!access || !(await verifySecret(secret, access.secret_hash))) {
    return error('Invalid secret', 401);
  }
  
  // Get timeline (public-safe events only)
  const events = await getTimeline(c.env.DB, ticket.id, { publicOnly: true });
  const timeline = formatPublicTimeline(events);
  
  const response: StatusResponse = {
    ticket: {
      public_id: ticket.public_id,
      status: ticket.status,
      subject: ticket.subject,
      created_at: ticket.created_at,
      updated_at: ticket.updated_at,
    },
    timeline,
  };
  
  return json(response);
});

// ═══════════════════════════════════════════════════════════════════════════
// POST /public/upload - Upload file (Turnstile + secret)
// ═══════════════════════════════════════════════════════════════════════════
app.post('/upload', async (c) => {
  const formData = await c.req.formData();
  
  const publicId = formData.get('publicId') as string;
  const secret = formData.get('secret') as string;
  const turnstileToken = formData.get('turnstile_token') as string;
  const file = formData.get('file') as File;
  
  if (!publicId || !secret || !turnstileToken || !file) {
    return error('Missing required fields');
  }
  
  // Verify Turnstile
  const ip = c.req.header('CF-Connecting-IP');
  const turnstileValid = await verifyTurnstile(turnstileToken, c.env.TURNSTILE_SECRET, ip);
  if (!turnstileValid) {
    return error('Bot check failed', 403);
  }
  
  // Get and verify ticket
  const ticket = await c.env.DB.prepare(`
    SELECT * FROM tickets WHERE public_id = ?
  `).bind(publicId).first<Ticket>();
  
  if (!ticket) {
    return notFound('Ticket not found');
  }
  
  const access = await c.env.DB.prepare(`
    SELECT * FROM ticket_access WHERE ticket_id = ?
  `).bind(ticket.id).first<TicketAccess>();
  
  if (!access || !(await verifySecret(secret, access.secret_hash))) {
    return error('Invalid secret', 401);
  }
  
  // Validate file
  const maxSize = 10 * 1024 * 1024; // 10MB
  if (file.size > maxSize) {
    return error('File too large (max 10MB)');
  }
  
  const allowedTypes = [
    'image/jpeg', 'image/png', 'image/gif', 'image/webp',
    'application/pdf', 'text/plain',
    'video/mp4', 'video/quicktime',
  ];
  if (!allowedTypes.includes(file.type)) {
    return error('File type not allowed');
  }
  
  // Upload to R2
  const uploadId = generateId();
  const r2Key = `tickets/${ticket.id}/${uploadId}/${file.name}`;
  
  await c.env.UPLOADS.put(r2Key, file.stream(), {
    httpMetadata: { contentType: file.type },
    customMetadata: { ticketId: ticket.id, originalName: file.name },
  });
  
  // Record in DB
  await c.env.DB.prepare(`
    INSERT INTO uploads (id, ticket_id, r2_key, filename, size, mime_type, uploaded_by)
    VALUES (?, ?, ?, ?, ?, ?, 'PUBLIC')
  `).bind(uploadId, ticket.id, r2Key, file.name, file.size, file.type).run();
  
  // Log event
  await logEvent(c.env.DB, ticket.id, 'UPLOAD', 'PUBLIC', ticket.client_email, {
    filename: file.name,
    size: file.size,
    mime_type: file.type,
  });
  
  return json({ success: true, upload_id: uploadId });
});

// ═══════════════════════════════════════════════════════════════════════════
// POST /public/live/join - Join live help session with code (Turnstile)
// ═══════════════════════════════════════════════════════════════════════════
app.post('/live/join', async (c) => {
  const body = await c.req.json<JoinLiveRequest>();
  
  // Verify Turnstile
  const ip = c.req.header('CF-Connecting-IP');
  const turnstileValid = await verifyTurnstile(body.turnstile_token, c.env.TURNSTILE_SECRET, ip);
  if (!turnstileValid) {
    return error('Bot check failed', 403);
  }
  
  if (!body.code || body.code.length !== 6) {
    return error('Invalid join code');
  }
  
  // Find room by code
  const room = await c.env.DB.prepare(`
    SELECT * FROM live_rooms WHERE code = ? AND ended_at IS NULL
  `).bind(body.code).first<LiveRoom>();
  
  if (!room) {
    return error('Room not found or expired', 404);
  }
  
  // Check expiration
  if (isExpired(room.expires_at)) {
    return error('Join code has expired. Please request a new one.', 410);
  }
  
  // Generate client token
  const token = generateId(); // Simple token for this client session
  
  // Log join event
  await logEvent(c.env.DB, room.ticket_id, 'LIVE_JOINED', 'PUBLIC', null, {
    room_id: room.id,
    mode: room.mode,
  });
  
  const response: JoinLiveResponse = {
    room_id: room.id,
    token,
    ws_url: `/ws/room/${room.id}?token=${token}&role=client`,
    mode: room.mode,
  };
  
  return json(response);
});

export default app;
