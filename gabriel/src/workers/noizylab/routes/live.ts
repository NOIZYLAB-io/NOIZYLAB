// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Live Help Routes
// Real-time video/audio/chat session management
// ═══════════════════════════════════════════════════════════════════════════

import { Hono } from 'hono';
import { z } from 'zod';
import { zValidator } from '@hono/zod-validator';
import type { Env } from '../index';
import { verifyTurnstile } from '../lib/turnstile';
import { 
  logLiveSessionStart, 
  logLiveSessionModeChange, 
  logLiveSessionEnd 
} from '../lib/events';
import { generateUUID, generateJoinCode, calculateDuration } from '../lib/utils';

const app = new Hono<{ Bindings: Env }>();

// ═══════════════════════════════════════════════════════════════════════════
// Validation Schemas
// ═══════════════════════════════════════════════════════════════════════════

const createSessionSchema = z.object({
  ticketId: z.string(),
  staffId: z.string(),
});

const joinSessionSchema = z.object({
  code: z.string().length(6),
  turnstileToken: z.string(),
});

// ═══════════════════════════════════════════════════════════════════════════
// Create Live Session (Staff)
// ═══════════════════════════════════════════════════════════════════════════

app.post('/create', zValidator('json', createSessionSchema), async (c) => {
  const body = c.req.valid('json');
  
  // Verify ticket exists
  const ticket = await c.env.DB.prepare(
    'SELECT id, client_name FROM tickets WHERE id = ?'
  ).bind(body.ticketId).first();
  
  if (!ticket) {
    return c.json({ error: 'Ticket not found' }, 404);
  }
  
  const sessionId = generateUUID();
  const joinCode = generateJoinCode();
  
  try {
    // Create session record
    await c.env.DB.prepare(`
      INSERT INTO live_sessions (
        id, ticket_id, join_code, current_mode, staff_id
      ) VALUES (?, ?, ?, 'video', ?)
    `).bind(sessionId, body.ticketId, joinCode, body.staffId).run();
    
    // Log event
    await logLiveSessionStart(c.env.DB, body.ticketId, sessionId, body.staffId, 'video');
    
    // Generate QR code URL (using QR code API)
    const joinUrl = `https://portal.noizylab.ca/live/${joinCode}`;
    const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${encodeURIComponent(joinUrl)}`;
    
    // Update session with QR URL
    await c.env.DB.prepare(
      'UPDATE live_sessions SET qr_code_url = ? WHERE id = ?'
    ).bind(qrUrl, sessionId).run();
    
    return c.json({
      success: true,
      sessionId,
      joinCode,
      joinUrl,
      qrCodeUrl: qrUrl,
      mode: 'video',
    });
    
  } catch (error) {
    console.error('Error creating live session:', error);
    return c.json({ error: 'Failed to create session' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Join Live Session (Client)
// ═══════════════════════════════════════════════════════════════════════════

app.post('/join', zValidator('json', joinSessionSchema), async (c) => {
  const body = c.req.valid('json');
  
  // Verify Turnstile
  const turnstileValid = await verifyTurnstile(body.turnstileToken, c.env.TURNSTILE_SECRET);
  if (!turnstileValid) {
    return c.json({ error: 'Bot verification failed' }, 403);
  }
  
  // Find session by code
  const session = await c.env.DB.prepare(`
    SELECT s.*, t.client_name 
    FROM live_sessions s
    JOIN tickets t ON s.ticket_id = t.id
    WHERE s.join_code = ? AND s.ended_at IS NULL
  `).bind(body.code.toUpperCase()).first();
  
  if (!session) {
    return c.json({ error: 'Session not found or expired' }, 404);
  }
  
  try {
    // Mark client as joined
    await c.env.DB.prepare(
      'UPDATE live_sessions SET client_joined = 1 WHERE id = ?'
    ).bind(session.id).run();
    
    // Get Durable Object for this session
    const roomId = c.env.CHAT_ROOM.idFromName(session.id as string);
    const room = c.env.CHAT_ROOM.get(roomId);
    
    // Get WebSocket URL for chat
    const wsUrl = `wss://api.noizylab.ca/api/live/ws/${session.id}`;
    
    return c.json({
      success: true,
      sessionId: session.id,
      ticketId: session.ticket_id,
      mode: session.current_mode,
      clientName: session.client_name,
      wsUrl,
      // Realtime Calls credentials would go here
      rtcConfig: {
        iceServers: [
          { urls: 'stun:stun.cloudflare.com:3478' },
        ],
      },
    });
    
  } catch (error) {
    console.error('Error joining session:', error);
    return c.json({ error: 'Failed to join session' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Change Session Mode (Fallback Ladder)
// ═══════════════════════════════════════════════════════════════════════════

app.post('/:sessionId/mode', async (c) => {
  const sessionId = c.req.param('sessionId');
  const { newMode, reason } = await c.req.json();
  
  const validModes = ['video', 'audio', 'chat', 'status'];
  if (!validModes.includes(newMode)) {
    return c.json({ error: 'Invalid mode' }, 400);
  }
  
  const session = await c.env.DB.prepare(
    'SELECT * FROM live_sessions WHERE id = ?'
  ).bind(sessionId).first();
  
  if (!session) {
    return c.json({ error: 'Session not found' }, 404);
  }
  
  const oldMode = session.current_mode as string;
  
  // Update mode history
  let modeHistory: any[] = [];
  if (session.mode_history) {
    try {
      modeHistory = JSON.parse(session.mode_history as string);
    } catch (e) {}
  }
  modeHistory.push({
    from: oldMode,
    to: newMode,
    reason,
    at: new Date().toISOString(),
  });
  
  try {
    await c.env.DB.prepare(`
      UPDATE live_sessions SET 
        current_mode = ?,
        mode_history = ?
      WHERE id = ?
    `).bind(newMode, JSON.stringify(modeHistory), sessionId).run();
    
    // Log event
    await logLiveSessionModeChange(
      c.env.DB,
      session.ticket_id as string,
      sessionId,
      oldMode,
      newMode,
      reason || 'Manual change'
    );
    
    return c.json({
      success: true,
      previousMode: oldMode,
      currentMode: newMode,
    });
    
  } catch (error) {
    console.error('Error changing mode:', error);
    return c.json({ error: 'Failed to change mode' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// End Live Session
// ═══════════════════════════════════════════════════════════════════════════

app.post('/:sessionId/end', async (c) => {
  const sessionId = c.req.param('sessionId');
  
  const session = await c.env.DB.prepare(
    'SELECT * FROM live_sessions WHERE id = ?'
  ).bind(sessionId).first();
  
  if (!session) {
    return c.json({ error: 'Session not found' }, 404);
  }
  
  if (session.ended_at) {
    return c.json({ error: 'Session already ended' }, 400);
  }
  
  const duration = calculateDuration(session.started_at as string);
  
  try {
    await c.env.DB.prepare(`
      UPDATE live_sessions SET 
        ended_at = datetime('now'),
        duration_seconds = ?
      WHERE id = ?
    `).bind(duration, sessionId).run();
    
    // Log event
    await logLiveSessionEnd(
      c.env.DB,
      session.ticket_id as string,
      sessionId,
      duration,
      session.current_mode as string
    );
    
    // Trigger AI summary (async)
    c.executionCtx.waitUntil(
      triggerSessionSummary(c.env, session.ticket_id as string, sessionId)
    );
    
    return c.json({
      success: true,
      duration,
      sessionId,
    });
    
  } catch (error) {
    console.error('Error ending session:', error);
    return c.json({ error: 'Failed to end session' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Get Session Status
// ═══════════════════════════════════════════════════════════════════════════

app.get('/:sessionId', async (c) => {
  const sessionId = c.req.param('sessionId');
  
  const session = await c.env.DB.prepare(`
    SELECT s.*, t.client_name, t.device_type, t.issue_summary
    FROM live_sessions s
    JOIN tickets t ON s.ticket_id = t.id
    WHERE s.id = ?
  `).bind(sessionId).first();
  
  if (!session) {
    return c.json({ error: 'Session not found' }, 404);
  }
  
  return c.json({
    sessionId: session.id,
    ticketId: session.ticket_id,
    mode: session.current_mode,
    clientJoined: Boolean(session.client_joined),
    startedAt: session.started_at,
    endedAt: session.ended_at,
    duration: session.duration_seconds,
    clientName: session.client_name,
    deviceType: session.device_type,
    issueSummary: session.issue_summary,
  });
});

// ═══════════════════════════════════════════════════════════════════════════
// WebSocket Handler (proxied to Durable Object)
// ═══════════════════════════════════════════════════════════════════════════

app.get('/ws/:sessionId', async (c) => {
  const sessionId = c.req.param('sessionId');
  
  // Verify session exists
  const session = await c.env.DB.prepare(
    'SELECT id FROM live_sessions WHERE id = ? AND ended_at IS NULL'
  ).bind(sessionId).first();
  
  if (!session) {
    return c.json({ error: 'Session not found' }, 404);
  }
  
  // Get Durable Object
  const roomId = c.env.CHAT_ROOM.idFromName(sessionId);
  const room = c.env.CHAT_ROOM.get(roomId);
  
  // Proxy the WebSocket request to the Durable Object
  return room.fetch(c.req.raw);
});

// ═══════════════════════════════════════════════════════════════════════════
// Helper: Trigger AI Session Summary
// ═══════════════════════════════════════════════════════════════════════════

async function triggerSessionSummary(env: Env, ticketId: string, sessionId: string) {
  try {
    // Get chat transcript from Durable Object
    const roomId = env.CHAT_ROOM.idFromName(sessionId);
    const room = env.CHAT_ROOM.get(roomId);
    
    const response = await room.fetch(new Request('http://internal/transcript'));
    const { transcript } = await response.json() as { transcript: string };
    
    if (transcript && transcript.length > 0) {
      const { summarizeSession } = await import('../lib/ai-jobs');
      await summarizeSession(env, ticketId, sessionId, transcript);
    }
  } catch (error) {
    console.error('Error triggering session summary:', error);
  }
}

export { app as liveRoutes };
