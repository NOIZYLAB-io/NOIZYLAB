-- ═══════════════════════════════════════════════════════════════════════════
-- NOIZYLAB OS v1 - D1 Schema
-- GO RUN FREE, AI-managed, fully logged
-- ═══════════════════════════════════════════════════════════════════════════

-- ───────────────────────────────────────────────────────────────────────────
-- TICKETS - Core ticket records
-- ───────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS tickets (
  id TEXT PRIMARY KEY,                    -- Internal UUID
  public_id TEXT UNIQUE NOT NULL,         -- 6-char public ID (e.g., "NL-A1B2C3")
  
  -- Status (single label)
  status TEXT NOT NULL DEFAULT 'TRIAGE'   -- TRIAGE|WAITING_CLIENT|WAITING_PARTS|SCHEDULED|IN_PROGRESS|DONE|BILLING
    CHECK (status IN ('TRIAGE','WAITING_CLIENT','WAITING_PARTS','SCHEDULED','IN_PROGRESS','DONE','BILLING')),
  
  -- Channel origin
  channel TEXT NOT NULL DEFAULT 'web'     -- web|email|phone|live
    CHECK (channel IN ('web','email','phone','live')),
  
  -- Client info
  client_name TEXT NOT NULL,
  client_email TEXT NOT NULL,
  client_phone TEXT,
  
  -- Content
  subject TEXT NOT NULL,
  description TEXT NOT NULL,
  
  -- Timestamps
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  resolved_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_tickets_status ON tickets(status);
CREATE INDEX IF NOT EXISTS idx_tickets_public_id ON tickets(public_id);
CREATE INDEX IF NOT EXISTS idx_tickets_created ON tickets(created_at DESC);

-- ───────────────────────────────────────────────────────────────────────────
-- TICKET_ACCESS - Secret-based access for clients
-- ───────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS ticket_access (
  ticket_id TEXT PRIMARY KEY REFERENCES tickets(id) ON DELETE CASCADE,
  secret_hash TEXT NOT NULL,              -- SHA-256 hash of the secret
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- ───────────────────────────────────────────────────────────────────────────
-- EVENTS - Append-only timeline (EVERYTHING = EVENT)
-- ───────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS events (
  id TEXT PRIMARY KEY,
  ticket_id TEXT NOT NULL REFERENCES tickets(id) ON DELETE CASCADE,
  
  -- Event classification
  type TEXT NOT NULL,                     -- CREATED|STATUS_CHANGED|MESSAGE|UPLOAD|AI_TRIAGE|etc
  
  -- Actor
  actor_type TEXT NOT NULL                -- PUBLIC|STAFF|SYSTEM
    CHECK (actor_type IN ('PUBLIC','STAFF','SYSTEM')),
  actor_id TEXT,                          -- Who did it (email, staff ID, or NULL for system)
  
  -- Payload
  payload_json TEXT NOT NULL DEFAULT '{}',
  
  -- Timestamp
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_events_ticket ON events(ticket_id, created_at);
CREATE INDEX IF NOT EXISTS idx_events_type ON events(type);

-- ───────────────────────────────────────────────────────────────────────────
-- UPLOADS - R2 file references
-- ───────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS uploads (
  id TEXT PRIMARY KEY,
  ticket_id TEXT NOT NULL REFERENCES tickets(id) ON DELETE CASCADE,
  
  r2_key TEXT NOT NULL,                   -- R2 object key
  filename TEXT NOT NULL,                 -- Original filename
  size INTEGER NOT NULL,                  -- Bytes
  mime_type TEXT NOT NULL,
  
  uploaded_by TEXT NOT NULL,              -- PUBLIC or staff ID
  uploaded_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_uploads_ticket ON uploads(ticket_id);

-- ───────────────────────────────────────────────────────────────────────────
-- LIVE_ROOMS - Short-lived join codes for live sessions
-- ───────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS live_rooms (
  id TEXT PRIMARY KEY,                    -- Room UUID
  ticket_id TEXT NOT NULL REFERENCES tickets(id) ON DELETE CASCADE,
  
  code TEXT UNIQUE NOT NULL,              -- 6-digit join code
  mode TEXT NOT NULL DEFAULT 'video'      -- video|audio|chat
    CHECK (mode IN ('video','audio','chat')),
  
  created_by TEXT NOT NULL,               -- Staff ID who created
  expires_at TEXT NOT NULL,               -- 10 min from creation
  ended_at TEXT,
  
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_live_rooms_code ON live_rooms(code);
CREATE INDEX IF NOT EXISTS idx_live_rooms_ticket ON live_rooms(ticket_id);

-- ───────────────────────────────────────────────────────────────────────────
-- FOLLOWUPS - Scheduled follow-up tasks
-- ───────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS followups (
  id TEXT PRIMARY KEY,
  ticket_id TEXT NOT NULL REFERENCES tickets(id) ON DELETE CASCADE,
  
  type TEXT NOT NULL                      -- check_in|feedback|upsell|warranty
    CHECK (type IN ('check_in','feedback','upsell','warranty')),
  
  due_at TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'pending'  -- pending|sent|completed|cancelled
    CHECK (status IN ('pending','sent','completed','cancelled')),
  
  message TEXT,                           -- Prepared message
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_followups_due ON followups(due_at, status);

-- ───────────────────────────────────────────────────────────────────────────
-- PERSONA_TAGS - AI-assigned persona and tags
-- ───────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS persona_tags (
  ticket_id TEXT PRIMARY KEY REFERENCES tickets(id) ON DELETE CASCADE,
  
  persona TEXT NOT NULL,                  -- P1-P12
  tags_json TEXT NOT NULL DEFAULT '[]',   -- Array of ≤3 tags
  suggested_playbook TEXT,                -- PB1-PB12
  confidence REAL NOT NULL DEFAULT 0.0,   -- 0.0-1.0
  
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- ───────────────────────────────────────────────────────────────────────────
-- EVENT TYPES REFERENCE (for documentation)
-- ───────────────────────────────────────────────────────────────────────────
-- CREATED              - Ticket created
-- STATUS_CHANGED       - Status transition
-- MESSAGE_OUT          - Staff message to client
-- MESSAGE_IN           - Client reply
-- UPLOAD               - File uploaded
-- AI_TRIAGE            - AI assigned persona/tags/playbook
-- AI_SUMMARIZE         - AI generated summary
-- PLAYBOOK_STARTED     - Playbook execution began
-- PLAYBOOK_COMPLETED   - Playbook finished
-- LIVE_CREATED         - Live room created
-- LIVE_JOINED          - Client joined live
-- LIVE_MODE_CHANGED    - Fallback: video→audio→chat
-- LIVE_ENDED           - Live session ended
-- FOLLOWUP_SCHEDULED   - Follow-up created
-- FOLLOWUP_SENT        - Follow-up message sent
-- RESOLVED             - Ticket marked done
-- BILLING_ADDED        - Billing info attached
