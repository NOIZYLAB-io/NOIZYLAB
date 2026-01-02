// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Status Routes
// Public status page endpoints
// ═══════════════════════════════════════════════════════════════════════════

import { Hono } from 'hono';
import type { Env } from '../index';

const app = new Hono<{ Bindings: Env }>();

// ═══════════════════════════════════════════════════════════════════════════
// Get Status by Ticket ID (Public)
// ═══════════════════════════════════════════════════════════════════════════

app.get('/:id', async (c) => {
  const ticketId = c.req.param('id').toUpperCase();
  
  try {
    const ticket = await c.env.DB.prepare(`
      SELECT id, status, next_update_by, updated_at
      FROM tickets WHERE id = ?
    `).bind(ticketId).first();
    
    if (!ticket) {
      return c.json({ error: 'Ticket not found' }, 404);
    }
    
    // Get latest status message
    const latestEvent = await c.env.DB.prepare(`
      SELECT data FROM events 
      WHERE ticket_id = ? 
      AND event_type IN ('STATUS_CHANGED', 'AI_NEXT_STEPS', 'INFO_REQUESTED')
      ORDER BY created_at DESC
      LIMIT 1
    `).bind(ticketId).first();
    
    let statusMessage = {
      now: getDefaultNow(ticket.status as string),
      next: getDefaultNext(ticket.status as string),
    };
    
    if (latestEvent?.data) {
      try {
        const eventData = JSON.parse(latestEvent.data as string);
        if (eventData.now) statusMessage.now = eventData.now;
        if (eventData.next) statusMessage.next = eventData.next;
      } catch (e) {}
    }
    
    return c.json({
      ticketId: ticket.id,
      status: ticket.status,
      statusLabel: getStatusLabel(ticket.status as string),
      now: statusMessage.now,
      next: statusMessage.next,
      nextUpdateBy: ticket.next_update_by,
      lastUpdated: ticket.updated_at,
    });
    
  } catch (error) {
    console.error('Error fetching status:', error);
    return c.json({ error: 'Failed to fetch status' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Get Uploads for Ticket (Public - limited)
// ═══════════════════════════════════════════════════════════════════════════

app.get('/:id/uploads', async (c) => {
  const ticketId = c.req.param('id').toUpperCase();
  
  try {
    const uploads = await c.env.DB.prepare(`
      SELECT id, filename, upload_type, uploaded_at
      FROM uploads 
      WHERE ticket_id = ?
      ORDER BY uploaded_at DESC
      LIMIT 10
    `).bind(ticketId).all();
    
    return c.json({
      ticketId,
      uploads: uploads.results,
    });
    
  } catch (error) {
    console.error('Error fetching uploads:', error);
    return c.json({ error: 'Failed to fetch uploads' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════
// Helper Functions
// ═══════════════════════════════════════════════════════════════════════════

function getStatusLabel(status: string): string {
  const labels: Record<string, string> = {
    '0-TRIAGE': 'Reviewing',
    '1-WAITING-CLIENT': 'Waiting for your response',
    '2-WAITING-PARTS': 'Parts on order',
    '3-SCHEDULED': 'Appointment scheduled',
    '4-IN-PROGRESS': 'In progress',
    '5-DONE': 'Complete',
    '9-BILLING': 'Invoice sent',
  };
  return labels[status] || 'Processing';
}

function getDefaultNow(status: string): string {
  const defaults: Record<string, string> = {
    '0-TRIAGE': 'Reviewing your request',
    '1-WAITING-CLIENT': 'Waiting for information from you',
    '2-WAITING-PARTS': 'Parts have been ordered',
    '3-SCHEDULED': 'Your appointment is confirmed',
    '4-IN-PROGRESS': 'Currently working on your device',
    '5-DONE': 'Work completed',
    '9-BILLING': 'Invoice has been sent',
  };
  return defaults[status] || 'Processing your request';
}

function getDefaultNext(status: string): string {
  const defaults: Record<string, string> = {
    '0-TRIAGE': 'A technician will review and respond',
    '1-WAITING-CLIENT': 'Please reply with the requested information',
    '2-WAITING-PARTS': 'We\'ll notify you when parts arrive',
    '3-SCHEDULED': 'See you at your appointment',
    '4-IN-PROGRESS': 'Updates as work progresses',
    '5-DONE': 'Thank you for choosing NoizyLab',
    '9-BILLING': 'Please submit payment',
  };
  return defaults[status] || 'We\'ll update you soon';
}

export { app as statusRoutes };
