// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Environment Types
// Type definitions for Cloudflare Worker bindings
// ═══════════════════════════════════════════════════════════════════════════

export interface Env {
  // ─────────────────────────────────────────────────────────────────────────
  // D1 Database
  // ─────────────────────────────────────────────────────────────────────────
  DB: D1Database;
  
  // ─────────────────────────────────────────────────────────────────────────
  // R2 Storage
  // ─────────────────────────────────────────────────────────────────────────
  UPLOADS: R2Bucket;
  
  // ─────────────────────────────────────────────────────────────────────────
  // Durable Objects
  // ─────────────────────────────────────────────────────────────────────────
  CHAT_ROOM: DurableObjectNamespace;
  PRESENCE: DurableObjectNamespace;
  
  // ─────────────────────────────────────────────────────────────────────────
  // AI Gateway
  // ─────────────────────────────────────────────────────────────────────────
  AI: Ai;
  
  // ─────────────────────────────────────────────────────────────────────────
  // Environment Variables
  // ─────────────────────────────────────────────────────────────────────────
  ENVIRONMENT: string;
  APP_NAME: string;
  VERSION: string;
  
  // ─────────────────────────────────────────────────────────────────────────
  // Secrets
  // ─────────────────────────────────────────────────────────────────────────
  TURNSTILE_SECRET_KEY: string;
  STRIPE_WEBHOOK_SECRET: string;
  EMAIL_API_KEY: string;
  STAFF_API_KEY: string;
}

// ═══════════════════════════════════════════════════════════════════════════
// Ticket Types
// ═══════════════════════════════════════════════════════════════════════════

export type TicketStatus = 
  | 'new'
  | 'triage'
  | 'waiting_info'
  | 'in_progress'
  | 'waiting_parts'
  | 'scheduled'
  | 'resolved'
  | 'closed';

export type TicketPriority = 'low' | 'medium' | 'high' | 'urgent';

export type LiveHelpMode = 'text' | 'screen' | 'remote';

export interface Ticket {
  id: string;
  short_code: string;
  client_id: string;
  client_email: string;
  client_name: string;
  subject: string;
  description: string;
  status: TicketStatus;
  priority: TicketPriority;
  assigned_to: string | null;
  persona_id: string | null;
  tags: string;
  playbook_id: string | null;
  source: string;
  created_at: string;
  updated_at: string;
  resolved_at: string | null;
  is_live: number;
  session_id: string | null;
}

// ═══════════════════════════════════════════════════════════════════════════
// Event Types
// ═══════════════════════════════════════════════════════════════════════════

export type EventType = 
  | 'CREATED'
  | 'STATUS_CHANGED'
  | 'ASSIGNED'
  | 'AI_TRIAGE'
  | 'AI_SUMMARY'
  | 'AI_DRAFT'
  | 'MESSAGE_SENT'
  | 'MESSAGE_RECEIVED'
  | 'FILE_UPLOADED'
  | 'LIVE_STARTED'
  | 'LIVE_ENDED'
  | 'PLAYBOOK_STARTED'
  | 'PLAYBOOK_COMPLETED'
  | 'NOTE_ADDED'
  | 'MERGED';

export interface TicketEvent {
  id: string;
  ticket_id: string;
  event_type: EventType;
  actor: string;
  actor_type: 'system' | 'staff' | 'client' | 'ai';
  data: string;
  created_at: string;
}

// ═══════════════════════════════════════════════════════════════════════════
// Session Types
// ═══════════════════════════════════════════════════════════════════════════

export interface LiveSession {
  id: string;
  ticket_id: string;
  mode: LiveHelpMode;
  staff_id: string;
  started_at: string;
  ended_at: string | null;
  summary: string | null;
  recording_url: string | null;
}

// ═══════════════════════════════════════════════════════════════════════════
// Upload Types
// ═══════════════════════════════════════════════════════════════════════════

export interface Upload {
  id: string;
  ticket_id: string;
  filename: string;
  size: number;
  mime_type: string;
  r2_key: string;
  uploaded_by: string;
  uploaded_at: string;
}

// ═══════════════════════════════════════════════════════════════════════════
// Client Types
// ═══════════════════════════════════════════════════════════════════════════

export interface Client {
  id: string;
  email: string;
  name: string;
  phone: string | null;
  primary_persona_id: string | null;
  tags: string;
  notes: string | null;
  created_at: string;
  last_contact_at: string | null;
}

// ═══════════════════════════════════════════════════════════════════════════
// Playbook Types
// ═══════════════════════════════════════════════════════════════════════════

export interface PlaybookRun {
  id: string;
  ticket_id: string;
  playbook_id: string;
  started_at: string;
  completed_at: string | null;
  status: 'running' | 'completed' | 'aborted';
  steps_completed: string;
  notes: string | null;
}

// ═══════════════════════════════════════════════════════════════════════════
// AI Types
// ═══════════════════════════════════════════════════════════════════════════

export interface TriageResult {
  priority: TicketPriority;
  persona_id: string | null;
  tags: string[];
  suggested_playbook: string | null;
  summary: string;
  confidence: number;
}

export interface DraftResult {
  subject: string;
  body: string;
  template_used: string;
  tone: string;
}

export interface FollowupSuggestion {
  type: 'followup' | 'upsell' | 'check_in';
  trigger_at: string;
  message: string;
  reason: string;
}

// ═══════════════════════════════════════════════════════════════════════════
// API Types
// ═══════════════════════════════════════════════════════════════════════════

export interface ApiResponse<T = unknown> {
  success: boolean;
  data?: T;
  error?: string;
  meta?: {
    page?: number;
    limit?: number;
    total?: number;
  };
}

export interface CreateTicketRequest {
  client_email: string;
  client_name: string;
  subject: string;
  description: string;
  source?: string;
  turnstile_token?: string;
}

export interface UpdateTicketRequest {
  status?: TicketStatus;
  priority?: TicketPriority;
  assigned_to?: string;
  persona_id?: string;
  tags?: string[];
  playbook_id?: string;
}

export interface CreateSessionRequest {
  ticket_id: string;
  mode: LiveHelpMode;
  staff_id: string;
}

export interface PresignRequest {
  ticket_id: string;
  filename: string;
  mime_type: string;
  size: number;
}

// ═══════════════════════════════════════════════════════════════════════════
// Persona & Playbook Config Types
// ═══════════════════════════════════════════════════════════════════════════

export interface Persona {
  id: string;
  name: string;
  emoji: string;
  description: string;
  indicators: string[];
  common_tags: string[];
  playbooks: string[];
  tone: string;
}

export interface Playbook {
  id: string;
  name: string;
  emoji: string;
  description: string;
  steps: string[];
  triggers: string[];
  output: string;
  estimated_time: string;
}

export interface Tag {
  id: string;
  category: string;
  name: string;
  emoji: string;
  color: string;
}
