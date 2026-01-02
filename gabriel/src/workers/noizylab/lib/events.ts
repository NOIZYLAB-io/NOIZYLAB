// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Event Logging
// Everything is logged - the timeline is the system truth
// ═══════════════════════════════════════════════════════════════════════════

import { generateUUID } from './utils';

// ═══════════════════════════════════════════════════════════════════════════
// Types
// ═══════════════════════════════════════════════════════════════════════════

export type EventType =
  | 'CREATED'
  | 'STATUS_CHANGED'
  | 'INFO_REQUESTED'
  | 'UPLOAD_ADDED'
  | 'LIVE_SESSION_STARTED'
  | 'LIVE_SESSION_MODE_CHANGED'
  | 'LIVE_SESSION_ENDED'
  | 'AUTO_PERSONA'
  | 'AUTO_TAGS'
  | 'PLAYBOOK_SUGGESTED'
  | 'PLAYBOOK_APPLIED'
  | 'AI_SUMMARY'
  | 'AI_NEXT_STEPS'
  | 'FOLLOWUP_SCHEDULED'
  | 'FOLLOWUP_RESULT'
  | 'BILLING_CREATED'
  | 'BILLING_PAID';

export type ActorType = 'client' | 'staff' | 'ai' | 'system';

export interface EventData {
  id: string;
  ticketId: string;
  eventType: EventType;
  actorType: ActorType;
  actorId: string;
  r2Objects?: string[];
  sessionId?: string;
  aiModel?: string;
  aiVersion?: string;
  aiConfidence?: number;
  aiReason?: string;
  data: Record<string, any>;
}

// ═══════════════════════════════════════════════════════════════════════════
// Main Event Logger
// ═══════════════════════════════════════════════════════════════════════════

export async function logEvent(db: D1Database, event: EventData): Promise<void> {
  try {
    await db.prepare(`
      INSERT INTO events (
        id, ticket_id, event_type, actor_type, actor_id,
        r2_objects, session_id,
        ai_model, ai_version, ai_confidence, ai_reason,
        data
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `).bind(
      event.id || generateUUID(),
      event.ticketId,
      event.eventType,
      event.actorType,
      event.actorId,
      event.r2Objects ? JSON.stringify(event.r2Objects) : null,
      event.sessionId || null,
      event.aiModel || null,
      event.aiVersion || null,
      event.aiConfidence || null,
      event.aiReason || null,
      JSON.stringify(event.data)
    ).run();
    
    console.log(`[EVENT] ${event.eventType} for ticket ${event.ticketId}`);
    
  } catch (error) {
    console.error('Failed to log event:', error);
    // Don't throw - event logging should not break the main flow
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// Convenience Loggers
// ═══════════════════════════════════════════════════════════════════════════

export async function logStatusChange(
  db: D1Database,
  ticketId: string,
  actorId: string,
  actorType: ActorType,
  oldStatus: string,
  newStatus: string,
  note?: string
): Promise<void> {
  await logEvent(db, {
    id: generateUUID(),
    ticketId,
    eventType: 'STATUS_CHANGED',
    actorType,
    actorId,
    data: { oldStatus, newStatus, note },
  });
}

export async function logUpload(
  db: D1Database,
  ticketId: string,
  actorId: string,
  actorType: ActorType,
  r2Key: string,
  filename: string,
  uploadType: string
): Promise<void> {
  await logEvent(db, {
    id: generateUUID(),
    ticketId,
    eventType: 'UPLOAD_ADDED',
    actorType,
    actorId,
    r2Objects: [r2Key],
    data: { filename, uploadType },
  });
}

export async function logLiveSessionStart(
  db: D1Database,
  ticketId: string,
  sessionId: string,
  staffId: string,
  mode: string
): Promise<void> {
  await logEvent(db, {
    id: generateUUID(),
    ticketId,
    eventType: 'LIVE_SESSION_STARTED',
    actorType: 'staff',
    actorId: staffId,
    sessionId,
    data: { mode },
  });
}

export async function logLiveSessionModeChange(
  db: D1Database,
  ticketId: string,
  sessionId: string,
  oldMode: string,
  newMode: string,
  reason: string
): Promise<void> {
  await logEvent(db, {
    id: generateUUID(),
    ticketId,
    eventType: 'LIVE_SESSION_MODE_CHANGED',
    actorType: 'system',
    actorId: 'fallback-system',
    sessionId,
    data: { oldMode, newMode, reason },
  });
}

export async function logLiveSessionEnd(
  db: D1Database,
  ticketId: string,
  sessionId: string,
  durationSeconds: number,
  finalMode: string
): Promise<void> {
  await logEvent(db, {
    id: generateUUID(),
    ticketId,
    eventType: 'LIVE_SESSION_ENDED',
    actorType: 'system',
    actorId: 'session-manager',
    sessionId,
    data: { durationSeconds, finalMode },
  });
}

export async function logPlaybookApplied(
  db: D1Database,
  ticketId: string,
  staffId: string,
  playbookId: string,
  playbookName: string
): Promise<void> {
  await logEvent(db, {
    id: generateUUID(),
    ticketId,
    eventType: 'PLAYBOOK_APPLIED',
    actorType: 'staff',
    actorId: staffId,
    data: { playbookId, playbookName },
  });
}

export async function logBillingCreated(
  db: D1Database,
  ticketId: string,
  staffId: string,
  amount: number,
  details: string
): Promise<void> {
  await logEvent(db, {
    id: generateUUID(),
    ticketId,
    eventType: 'BILLING_CREATED',
    actorType: 'staff',
    actorId: staffId,
    data: { amount, details },
  });
}

export async function logBillingPaid(
  db: D1Database,
  ticketId: string,
  amount: number,
  method: string
): Promise<void> {
  await logEvent(db, {
    id: generateUUID(),
    ticketId,
    eventType: 'BILLING_PAID',
    actorType: 'system',
    actorId: 'payment-system',
    data: { amount, method },
  });
}

// ═══════════════════════════════════════════════════════════════════════════
// Event Retrieval
// ═══════════════════════════════════════════════════════════════════════════

export async function getTicketTimeline(
  db: D1Database,
  ticketId: string,
  limit = 100
): Promise<any[]> {
  const result = await db.prepare(`
    SELECT * FROM events 
    WHERE ticket_id = ?
    ORDER BY created_at DESC
    LIMIT ?
  `).bind(ticketId, limit).all();
  
  return result.results.map(event => ({
    ...event,
    data: event.data ? JSON.parse(event.data as string) : {},
    r2Objects: event.r2_objects ? JSON.parse(event.r2_objects as string) : [],
  }));
}

export async function getRecentEvents(
  db: D1Database,
  eventTypes?: EventType[],
  limit = 50
): Promise<any[]> {
  let query = 'SELECT * FROM events';
  const params: any[] = [];
  
  if (eventTypes && eventTypes.length > 0) {
    const placeholders = eventTypes.map(() => '?').join(', ');
    query += ` WHERE event_type IN (${placeholders})`;
    params.push(...eventTypes);
  }
  
  query += ' ORDER BY created_at DESC LIMIT ?';
  params.push(limit);
  
  const result = await db.prepare(query).bind(...params).all();
  
  return result.results.map(event => ({
    ...event,
    data: event.data ? JSON.parse(event.data as string) : {},
  }));
}

// ═══════════════════════════════════════════════════════════════════════════
// Event Statistics
// ═══════════════════════════════════════════════════════════════════════════

export async function getEventStats(
  db: D1Database,
  ticketId?: string
): Promise<Record<string, number>> {
  let query = 'SELECT event_type, COUNT(*) as count FROM events';
  const params: any[] = [];
  
  if (ticketId) {
    query += ' WHERE ticket_id = ?';
    params.push(ticketId);
  }
  
  query += ' GROUP BY event_type';
  
  const result = await db.prepare(query).bind(...params).all();
  
  const stats: Record<string, number> = {};
  for (const row of result.results) {
    stats[row.event_type as string] = row.count as number;
  }
  
  return stats;
}
