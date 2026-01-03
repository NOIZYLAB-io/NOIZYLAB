// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS v1 - Type Definitions
// GO RUN FREE, AI-managed, fully logged
// ═══════════════════════════════════════════════════════════════════════════

// ───────────────────────────────────────────────────────────────────────────
// Environment Bindings
// ───────────────────────────────────────────────────────────────────────────
export interface Env {
  DB: D1Database;
  UPLOADS: R2Bucket;
  LIVE_ROOM: DurableObjectNamespace;
  AI: Ai;
  
  // Secrets
  TURNSTILE_SECRET: string;
  ACCESS_AUD: string;  // Cloudflare Access audience tag
  RESEND_API_KEY: string;  // Email service
}

// ───────────────────────────────────────────────────────────────────────────
// Status & Enums
// ───────────────────────────────────────────────────────────────────────────
export type TicketStatus = 
  | 'TRIAGE' 
  | 'WAITING_CLIENT' 
  | 'WAITING_PARTS' 
  | 'SCHEDULED' 
  | 'IN_PROGRESS' 
  | 'DONE' 
  | 'BILLING';

export type Channel = 'web' | 'email' | 'phone' | 'live';
export type ActorType = 'PUBLIC' | 'STAFF' | 'SYSTEM';
export type LiveMode = 'video' | 'audio' | 'chat';
export type FollowupType = 'check_in' | 'feedback' | 'upsell' | 'warranty';
export type FollowupStatus = 'pending' | 'sent' | 'completed' | 'cancelled';

// ───────────────────────────────────────────────────────────────────────────
// Event Types (append-only)
// ───────────────────────────────────────────────────────────────────────────
export type EventType =
  | 'CREATED'
  | 'STATUS_CHANGED'
  | 'MESSAGE_OUT'
  | 'MESSAGE_IN'
  | 'UPLOAD'
  | 'AI_TRIAGE'
  | 'AI_SUMMARIZE'
  | 'PLAYBOOK_STARTED'
  | 'PLAYBOOK_COMPLETED'
  | 'LIVE_CREATED'
  | 'LIVE_JOINED'
  | 'LIVE_MODE_CHANGED'
  | 'LIVE_ENDED'
  | 'FOLLOWUP_SCHEDULED'
  | 'FOLLOWUP_SENT'
  | 'RESOLVED'
  | 'BILLING_ADDED'
  | 'EMAIL_SENT';

// ───────────────────────────────────────────────────────────────────────────
// Personas (P1-P12)
// ───────────────────────────────────────────────────────────────────────────
export type Persona = 
  | 'P1'   // Tab Tornado
  | 'P2'   // Storage Closet
  | 'P3'   // Click-Yes Optimizer
  | 'P4'   // Update Avoider
  | 'P5'   // Password Spiral
  | 'P6'   // Wi-Fi Whiplash
  | 'P7'   // Peripheral Collector
  | 'P8'   // Cloud Sync Tangle
  | 'P9'   // Thermal Throttler
  | 'P10'  // Creative Chaos
  | 'P11'  // Fine Yesterday
  | 'P12'; // Hardware Failing Quietly

export const PERSONA_NAMES: Record<Persona, string> = {
  P1: 'Tab Tornado',
  P2: 'Storage Closet',
  P3: 'Click-Yes Optimizer',
  P4: 'Update Avoider',
  P5: 'Password Spiral',
  P6: 'Wi-Fi Whiplash',
  P7: 'Peripheral Collector',
  P8: 'Cloud Sync Tangle',
  P9: 'Thermal Throttler',
  P10: 'Creative Chaos',
  P11: 'Fine Yesterday',
  P12: 'Hardware Failing Quietly',
};

// ───────────────────────────────────────────────────────────────────────────
// Tags (≤3 per ticket)
// ───────────────────────────────────────────────────────────────────────────
export type Tag =
  // Performance
  | 'PERF-TABS' | 'PERF-STARTUP' | 'PERF-BACKGROUND' | 'PERF-THERMAL' | 'PERF-LOWRAM'
  // Storage/files
  | 'STOR-LOWDISK' | 'STOR-DISKERRORS' | 'STOR-EXTERNALDRIVE' | 'FILE-PERMISSIONS' | 'FILE-CORRUPTION'
  // Security
  | 'SEC-PUP' | 'SEC-BROWSERHIJACK' | 'SEC-PHISH-ACCOUNT' | 'SEC-AV-CONFLICT'
  // Accounts
  | 'AUTH-APPLEID' | 'AUTH-MICROSOFT' | 'AUTH-GOOGLE' | 'AUTH-MFA' | 'AUTH-PASSWORDRESET'
  // Network
  | 'NET-WIFIDROP' | 'NET-DNS' | 'NET-ROUTER' | 'NET-VPN'
  // Updates/drivers
  | 'UPD-OS' | 'UPD-APP' | 'DRV-PRINTER' | 'DRV-USB' | 'DRV-GPU' | 'DRV-AUDIO'
  // Cloud/sync
  | 'SYNC-ICLOUD' | 'SYNC-ONEDRIVE' | 'SYNC-GDRIVE' | 'SYNC-DUPES'
  // Hardware
  | 'HW-SSD' | 'HW-RAM' | 'HW-BATTERY' | 'HW-DUSTFAN' | 'HW-LIQUID'
  // Behavior
  | 'USR-CLICKYES' | 'USR-NOBACKUP' | 'USR-UPDATEAVOID' | 'USR-DOWNLOADSCHAOS' | 'USR-PASSWORDCHAOS';

// ───────────────────────────────────────────────────────────────────────────
// Playbooks (PB1-PB12)
// ───────────────────────────────────────────────────────────────────────────
export type Playbook =
  | 'PB1'   // Browser Diet
  | 'PB2'   // Space Guard
  | 'PB3'   // No Snake Oil
  | 'PB4'   // Update Safe-Window
  | 'PB5'   // Password Cleanroom
  | 'PB6'   // Wi-Fi Stabilizer
  | 'PB7'   // Peripheral Detox
  | 'PB8'   // Cloud Sync Sanity
  | 'PB9'   // Thermal Rescue
  | 'PB10'  // Creative Workstation Tune
  | 'PB11'  // Hardware Truth Test
  | 'PB12'; // Backup Bulletproof

export const PLAYBOOK_NAMES: Record<Playbook, string> = {
  PB1: 'Browser Diet',
  PB2: 'Space Guard',
  PB3: 'No Snake Oil',
  PB4: 'Update Safe-Window',
  PB5: 'Password Cleanroom',
  PB6: 'Wi-Fi Stabilizer',
  PB7: 'Peripheral Detox',
  PB8: 'Cloud Sync Sanity',
  PB9: 'Thermal Rescue',
  PB10: 'Creative Workstation Tune',
  PB11: 'Hardware Truth Test',
  PB12: 'Backup Bulletproof',
};

// ───────────────────────────────────────────────────────────────────────────
// Database Records
// ───────────────────────────────────────────────────────────────────────────
export interface Ticket {
  id: string;
  public_id: string;
  status: TicketStatus;
  channel: Channel;
  client_name: string;
  client_email: string;
  client_phone: string | null;
  subject: string;
  description: string;
  created_at: string;
  updated_at: string;
  resolved_at: string | null;
}

export interface TicketAccess {
  ticket_id: string;
  secret_hash: string;
  created_at: string;
}

export interface Event {
  id: string;
  ticket_id: string;
  type: EventType;
  actor_type: ActorType;
  actor_id: string | null;
  payload_json: string;
  created_at: string;
}

export interface Upload {
  id: string;
  ticket_id: string;
  r2_key: string;
  filename: string;
  size: number;
  mime_type: string;
  uploaded_by: string;
  uploaded_at: string;
}

export interface LiveRoom {
  id: string;
  ticket_id: string;
  code: string;
  mode: LiveMode;
  created_by: string;
  expires_at: string;
  ended_at: string | null;
  created_at: string;
}

export interface Followup {
  id: string;
  ticket_id: string;
  type: FollowupType;
  due_at: string;
  status: FollowupStatus;
  message: string | null;
  created_at: string;
}

export interface PersonaTags {
  ticket_id: string;
  persona: Persona;
  tags_json: string;
  suggested_playbook: Playbook | null;
  confidence: number;
  created_at: string;
  updated_at: string;
}

// ───────────────────────────────────────────────────────────────────────────
// AI Output (Strict Format)
// ───────────────────────────────────────────────────────────────────────────
export interface AITriageResult {
  persona: Persona;                    // Exactly 1
  tags: Tag[];                         // ≤3
  next_question: string | null;        // ≤1 (or null)
  playbook: Playbook;                  // Exactly 1
  calm_message: string;                // 3 lines max
  confidence: number;                  // 0.0-1.0
}

export interface AISummaryResult {
  summary: string;                     // 3 sentences max
  key_points: string[];                // ≤3
  next_steps: string[];                // ≤3
  sentiment: 'positive' | 'neutral' | 'frustrated';
}

// ───────────────────────────────────────────────────────────────────────────
// API Request/Response Types
// ───────────────────────────────────────────────────────────────────────────
export interface CreateTicketRequest {
  name: string;
  email: string;
  phone?: string;
  subject: string;
  description: string;
  turnstile_token: string;
}

export interface CreateTicketResponse {
  ticketPublicId: string;
  secret: string;
}

export interface StatusResponse {
  ticket: {
    public_id: string;
    status: TicketStatus;
    subject: string;
    created_at: string;
    updated_at: string;
  };
  timeline: Array<{
    type: EventType;
    created_at: string;
    summary: string;
    payload?: unknown;
    // Public view: summary is the primary display field
  }>;
}

export interface JoinLiveRequest {
  code: string;
  turnstile_token: string;
}

export interface JoinLiveResponse {
  room_id: string;
  token: string;
  ws_url: string;
  mode: LiveMode;
}

// ───────────────────────────────────────────────────────────────────────────
// WebSocket Messages
// ───────────────────────────────────────────────────────────────────────────
export type WSClientMessage =
  | { type: 'chat'; text: string }
  | { type: 'mode_request'; mode: LiveMode }
  | { type: 'signal'; sdp?: string; ice?: string }
  | { type: 'ping' };

export type WSServerMessage =
  | { type: 'chat'; from: string; text: string; ts: string }
  | { type: 'mode_changed'; mode: LiveMode; reason: string }
  | { type: 'signal'; sdp?: string; ice?: string }
  | { type: 'user_joined'; role: 'client' | 'staff' }
  | { type: 'user_left'; role: 'client' | 'staff' }
  | { type: 'room_closed'; reason: string }
  | { type: 'pong' }
  | { type: 'error'; message: string };
