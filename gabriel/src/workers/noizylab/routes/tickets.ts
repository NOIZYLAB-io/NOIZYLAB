// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Ticket Routes
// CRUD operations for support tickets
// ═══════════════════════════════════════════════════════════════════════════

import { Hono } from 'hono';
import { z } from 'zod';
import { zValidator } from '@hono/zod-validator';
import type { Env } from '../index';
import { verifyTurnstile } from '../lib/turnstile';
import { logEvent } from '../lib/events';
import { generateTicketId, generateUUID } from '../lib/utils';

const app = new Hono<{ Bindings: Env }>();

// ═══════════════════════════════════════════════════════════════════════════
// Validation Schemas
// ═══════════════════════════════════════════════════════════════════════════

const createTicketSchema = z.object({
  clientName: z.string().min(1).max(100),
  clientEmail: z.string().email(),
  clientPhone: z.string().optional(),
  deviceType: z.string().min(1).max(50),
  deviceModel: z.string().optional(),
  deviceOs: z.string().optional(),
  issueSummary: z.string().min(1).max(50),  // 3-word max guidance
  issueDescription: z.string().optional(),
  turnstileToken: z.string(),
});

const updateTicketSchema = z.object({
  status: z.enum([
    '0-TRIAGE', '1-WAITING-CLIENT', '2-WAITING-PARTS',
    '3-SCHEDULED', '4-IN-PROGRESS', '5-DONE', '9-BILLING'
  ]).optional(),
  persona: z.string().optional(),
  tags: z.array(z.string()).max(3).optional(),
  suggestedPlaybook: z.string().optional(),
  nextUpdateBy: z.string().optional(),
  scheduledAt: z.string().optional(),
});

// ═══════════════════════════════════════════════════════════════════════════
// Create Ticket
// ═══════════════════════════════════════════════════════════════════════════

app.post('/', zValidator('json', createTicketSchema), async (c) => {
  const body = c.req.valid('json');
  
  // Verify Turnstile
  const turnstileValid = await verifyTurnstile(body.turnstileToken, c.env.TURNSTILE_SECRET);
  if (!turnstileValid) {
    return c.json({ error: 'Bot verification failed' }, 403);
  }
  
  // Generate ticket ID (NL-0042 format)
  const ticketId = await generateTicketId(c.env.DB);
  const eventId = generateUUID();
  
  // Calculate next update time (default: 2 hours from now)
  const nextUpdateBy = new Date(Date.now() + 2 * 60 * 60 * 1000).toISOString();
  
  try {
    // Insert ticket
    await c.env.DB.prepare(`
      INSERT INTO tickets (
        id, client_name, client_email, client_phone,
        device_type, device_model, device_os,
        issue_summary, issue_description,
        status, next_update_by, source_channel
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `).bind(
      ticketId,
      body.clientName,
      body.clientEmail,
      body.clientPhone || null,
      body.deviceType,
      body.deviceModel || null,
      body.deviceOs || null,
      body.issueSummary,
      body.issueDescription || null,
      '0-TRIAGE',
      nextUpdateBy,
      'portal'
    ).run();
    
    // Log CREATED event
    await logEvent(c.env.DB, {
      id: eventId,
      ticketId,
      eventType: 'CREATED',
      actorType: 'client',
      actorId: body.clientEmail,
      data: {
        clientName: body.clientName,
        deviceType: body.deviceType,
        issueSummary: body.issueSummary,
      },
    });
    
    // Trigger AI triage (async, don't wait)
    c.executionCtx.waitUntil(triggerAITriage(c.env, ticketId, body));
    
    return c.json({
      success: true,
      ticketId,
      message: `Ticket ${ticketId} created. Next update by ${nextUpdateBy}`,
      status: '0-TRIAGE',
      nextUpdateBy,
    }, 201);
    
  } catch (error) {
    console.error('Error creating ticket:', error);
    return c.json({ error: 'Failed to create ticket' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Get Ticket by ID
// ═══════════════════════════════════════════════════════════════════════════

app.get('/:id', async (c) => {
  const ticketId = c.req.param('id');
  
  try {
    const ticket = await c.env.DB.prepare(`
      SELECT * FROM tickets WHERE id = ?
    `).bind(ticketId).first();
    
    if (!ticket) {
      return c.json({ error: 'Ticket not found' }, 404);
    }
    
    // Get events timeline
    const events = await c.env.DB.prepare(`
      SELECT * FROM events 
      WHERE ticket_id = ? 
      ORDER BY created_at DESC
      LIMIT 50
    `).bind(ticketId).all();
    
    // Get uploads
    const uploads = await c.env.DB.prepare(`
      SELECT * FROM uploads 
      WHERE ticket_id = ?
      ORDER BY uploaded_at DESC
    `).bind(ticketId).all();
    
    return c.json({
      ticket,
      events: events.results,
      uploads: uploads.results,
    });
    
  } catch (error) {
    console.error('Error fetching ticket:', error);
    return c.json({ error: 'Failed to fetch ticket' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Get Ticket Status (Public - minimal info)
// ═══════════════════════════════════════════════════════════════════════════

app.get('/:id/status', async (c) => {
  const ticketId = c.req.param('id');
  
  try {
    const ticket = await c.env.DB.prepare(`
      SELECT id, status, next_update_by, updated_at
      FROM tickets WHERE id = ?
    `).bind(ticketId).first();
    
    if (!ticket) {
      return c.json({ error: 'Ticket not found' }, 404);
    }
    
    // Get latest status event for NOW/NEXT
    const latestEvent = await c.env.DB.prepare(`
      SELECT data FROM events 
      WHERE ticket_id = ? AND event_type IN ('STATUS_CHANGED', 'AI_NEXT_STEPS')
      ORDER BY created_at DESC
      LIMIT 1
    `).bind(ticketId).first();
    
    let now = 'Processing your request';
    let next = 'We\'ll update you soon';
    
    if (latestEvent?.data) {
      try {
        const eventData = JSON.parse(latestEvent.data as string);
        now = eventData.now || now;
        next = eventData.next || next;
      } catch (e) {}
    }
    
    return c.json({
      ticketId: ticket.id,
      status: ticket.status,
      now,
      next,
      nextUpdateBy: ticket.next_update_by,
      lastUpdated: ticket.updated_at,
    });
    
  } catch (error) {
    console.error('Error fetching ticket status:', error);
    return c.json({ error: 'Failed to fetch status' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Update Ticket (Staff only)
// ═══════════════════════════════════════════════════════════════════════════

app.put('/:id', zValidator('json', updateTicketSchema), async (c) => {
  const ticketId = c.req.param('id');
  const body = c.req.valid('json');
  const staffId = c.req.header('X-Staff-Id') || 'system';
  
  try {
    // Build update query dynamically
    const updates: string[] = ['updated_at = datetime(\'now\')'];
    const values: any[] = [];
    
    if (body.status) {
      updates.push('status = ?');
      values.push(body.status);
    }
    if (body.persona) {
      updates.push('persona = ?');
      values.push(body.persona);
    }
    if (body.tags) {
      updates.push('tags = ?');
      values.push(JSON.stringify(body.tags));
    }
    if (body.suggestedPlaybook) {
      updates.push('suggested_playbook = ?');
      values.push(body.suggestedPlaybook);
    }
    if (body.nextUpdateBy) {
      updates.push('next_update_by = ?');
      values.push(body.nextUpdateBy);
    }
    if (body.scheduledAt) {
      updates.push('scheduled_at = ?');
      values.push(body.scheduledAt);
    }
    
    values.push(ticketId);
    
    await c.env.DB.prepare(`
      UPDATE tickets SET ${updates.join(', ')} WHERE id = ?
    `).bind(...values).run();
    
    // Log STATUS_CHANGED event if status changed
    if (body.status) {
      await logEvent(c.env.DB, {
        id: generateUUID(),
        ticketId,
        eventType: 'STATUS_CHANGED',
        actorType: 'staff',
        actorId: staffId,
        data: { newStatus: body.status, ...body },
      });
    }
    
    return c.json({ success: true, ticketId });
    
  } catch (error) {
    console.error('Error updating ticket:', error);
    return c.json({ error: 'Failed to update ticket' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// List Tickets (Staff only)
// ═══════════════════════════════════════════════════════════════════════════

app.get('/', async (c) => {
  const status = c.req.query('status');
  const limit = parseInt(c.req.query('limit') || '50');
  const offset = parseInt(c.req.query('offset') || '0');
  
  try {
    let query = 'SELECT * FROM tickets';
    const params: any[] = [];
    
    if (status) {
      query += ' WHERE status = ?';
      params.push(status);
    }
    
    query += ' ORDER BY created_at DESC LIMIT ? OFFSET ?';
    params.push(limit, offset);
    
    const tickets = await c.env.DB.prepare(query).bind(...params).all();
    
    // Get counts by status
    const counts = await c.env.DB.prepare(`
      SELECT status, COUNT(*) as count 
      FROM tickets 
      WHERE status != '5-DONE'
      GROUP BY status
    `).all();
    
    return c.json({
      tickets: tickets.results,
      counts: counts.results,
      pagination: { limit, offset },
    });
    
  } catch (error) {
    console.error('Error listing tickets:', error);
    return c.json({ error: 'Failed to list tickets' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// AI Triage Helper (called async)
// ═══════════════════════════════════════════════════════════════════════════

async function triggerAITriage(env: Env, ticketId: string, ticketData: any) {
  try {
    // Import AI triage function
    const { triageTicket } = await import('../lib/ai-jobs');
    await triageTicket(env, ticketId, ticketData);
  } catch (error) {
    console.error('AI triage error:', error);
  }
}

export { app as ticketRoutes };
