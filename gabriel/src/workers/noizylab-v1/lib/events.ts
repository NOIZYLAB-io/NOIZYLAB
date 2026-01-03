// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS v1 - Event Logger
// Everything = Event (append-only timeline)
// ═══════════════════════════════════════════════════════════════════════════

import { Env, EventType, ActorType, Event } from '../types';
import { generateId, now } from './utils';

// ───────────────────────────────────────────────────────────────────────────
// Log Event (append-only)
// ───────────────────────────────────────────────────────────────────────────
export async function logEvent(
  db: D1Database,
  ticketId: string,
  type: EventType,
  actorType: ActorType,
  actorId: string | null,
  payload: Record<string, unknown> = {}
): Promise<Event> {
  const event: Event = {
    id: generateId(),
    ticket_id: ticketId,
    type,
    actor_type: actorType,
    actor_id: actorId,
    payload_json: JSON.stringify(payload),
    created_at: now(),
  };
  
  await db.prepare(`
    INSERT INTO events (id, ticket_id, type, actor_type, actor_id, payload_json, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `).bind(
    event.id,
    event.ticket_id,
    event.type,
    event.actor_type,
    event.actor_id,
    event.payload_json,
    event.created_at
  ).run();
  
  // Also update ticket's updated_at
  await db.prepare(`
    UPDATE tickets SET updated_at = ? WHERE id = ?
  `).bind(now(), ticketId).run();
  
  return event;
}

// ───────────────────────────────────────────────────────────────────────────
// Get Timeline for a Ticket
// ───────────────────────────────────────────────────────────────────────────
export async function getTimeline(
  db: D1Database,
  ticketId: string,
  options: { limit?: number; publicOnly?: boolean } = {}
): Promise<Event[]> {
  const { limit = 100, publicOnly = false } = options;
  
  let query = `
    SELECT * FROM events
    WHERE ticket_id = ?
  `;
  
  // For public view, exclude internal events
  if (publicOnly) {
    query += ` AND type NOT IN ('AI_TRIAGE', 'AI_SUMMARIZE', 'BILLING_ADDED')`;
  }
  
  query += ` ORDER BY created_at ASC LIMIT ?`;
  
  const result = await db.prepare(query).bind(ticketId, limit).all<Event>();
  return result.results;
}

// ───────────────────────────────────────────────────────────────────────────
// Format Timeline for Public View
// ───────────────────────────────────────────────────────────────────────────
export function formatPublicTimeline(events: Event[]): Array<{
  type: EventType;
  created_at: string;
  summary: string;
  payload: unknown;
}> {
  return events.map(event => {
    const payload = JSON.parse(event.payload_json);
    let summary = '';
    
    switch (event.type) {
      case 'CREATED':
        summary = 'Ticket created';
        break;
      case 'STATUS_CHANGED':
        summary = `Status changed to ${formatStatus(payload.to)}`;
        break;
      case 'MESSAGE_OUT':
        summary = 'You received a message';
        break;
      case 'MESSAGE_IN':
        summary = 'Your message was received';
        break;
      case 'UPLOAD':
        summary = `File uploaded: ${payload.filename}`;
        break;
      case 'LIVE_CREATED':
        summary = 'Live help session available';
        break;
      case 'LIVE_JOINED':
        summary = 'You joined the live session';
        break;
      case 'LIVE_ENDED':
        summary = 'Live session ended';
        break;
      case 'PLAYBOOK_STARTED':
        summary = `Started: ${payload.playbook_name}`;
        break;
      case 'PLAYBOOK_COMPLETED':
        summary = `Completed: ${payload.playbook_name}`;
        break;
      case 'RESOLVED':
        summary = 'Issue resolved';
        break;
      default:
        summary = 'Update';
    }
    
    return {
      type: event.type,
      created_at: event.created_at,
      summary,
      payload,
    };
  });
}

// ───────────────────────────────────────────────────────────────────────────
// Status Formatter
// ───────────────────────────────────────────────────────────────────────────
function formatStatus(status: string): string {
  const labels: Record<string, string> = {
    TRIAGE: 'Under review',
    WAITING_CLIENT: 'Waiting for your response',
    WAITING_PARTS: 'Waiting for parts',
    SCHEDULED: 'Scheduled',
    IN_PROGRESS: 'In progress',
    DONE: 'Complete',
    BILLING: 'Ready for billing',
  };
  return labels[status] || status;
}
