-- ═══════════════════════════════════════════════════════════════════════════
-- NOIZYLAB OS - D1 Database Schema
-- "GO RUN FREE" Hot-Rod Edition
-- ═══════════════════════════════════════════════════════════════════════════

-- ═══════════════════════════════════════════════════════════════════════════
-- TICKETS - Core ticket management
-- ═══════════════════════════════════════════════════════════════════════════

CREATE TABLE IF NOT EXISTS tickets (
    id TEXT PRIMARY KEY,                          -- NL-0042 format
    
    -- Client Info
    client_name TEXT NOT NULL,
    client_email TEXT NOT NULL,
    client_phone TEXT,
    
    -- Device Info
    device_type TEXT NOT NULL,                    -- MacBook, Desktop, Surface, etc.
    device_model TEXT,
    device_os TEXT,
    
    -- Issue
    issue_summary TEXT NOT NULL,                  -- 3-word max
    issue_description TEXT,
    
    -- Status Flow
    status TEXT NOT NULL DEFAULT '0-TRIAGE',      -- 0-TRIAGE, 1-WAITING-CLIENT, 2-WAITING-PARTS, 3-SCHEDULED, 4-IN-PROGRESS, 5-DONE, 9-BILLING
    
    -- AI Analysis
    persona TEXT,                                 -- P1-P12
    tags TEXT,                                    -- JSON array, max 3
    suggested_playbook TEXT,                      -- PB1-PB12
    ai_confidence TEXT,                           -- green, yellow, red
    
    -- Scheduling
    next_update_by TEXT,                          -- ISO timestamp
    scheduled_at TEXT,
    
    -- Billing
    estimate_amount REAL,
    estimate_approved INTEGER DEFAULT 0,
    billing_status TEXT,                          -- pending, invoiced, paid
    
    -- Timestamps
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    closed_at TEXT,
    
    -- Source tracking
    source_channel TEXT DEFAULT 'portal',         -- portal, email-help, email-hello, email-rsp, phone
    gmail_thread_id TEXT
);

CREATE INDEX idx_tickets_status ON tickets(status);
CREATE INDEX idx_tickets_client_email ON tickets(client_email);
CREATE INDEX idx_tickets_persona ON tickets(persona);
CREATE INDEX idx_tickets_created_at ON tickets(created_at);

-- ═══════════════════════════════════════════════════════════════════════════
-- EVENTS - Everything is logged (the system truth)
-- ═══════════════════════════════════════════════════════════════════════════

CREATE TABLE IF NOT EXISTS events (
    id TEXT PRIMARY KEY,
    ticket_id TEXT NOT NULL,
    
    -- Event Type
    event_type TEXT NOT NULL,                     -- CREATED, STATUS_CHANGED, UPLOAD_ADDED, etc.
    
    -- Actor (Who)
    actor_type TEXT NOT NULL,                     -- client, staff, ai, system
    actor_id TEXT NOT NULL,
    
    -- Timestamp (When)
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    
    -- Links
    r2_objects TEXT,                              -- JSON array of R2 keys
    session_id TEXT,
    
    -- AI Audit Trail
    ai_model TEXT,
    ai_version TEXT,
    ai_confidence REAL,
    ai_reason TEXT,
    
    -- Payload (What)
    data TEXT NOT NULL,                           -- JSON object
    
    FOREIGN KEY (ticket_id) REFERENCES tickets(id)
);

CREATE INDEX idx_events_ticket_id ON events(ticket_id);
CREATE INDEX idx_events_event_type ON events(event_type);
CREATE INDEX idx_events_created_at ON events(created_at);
CREATE INDEX idx_events_actor_type ON events(actor_type);

-- ═══════════════════════════════════════════════════════════════════════════
-- LIVE SESSIONS - Video/Audio/Chat sessions
-- ═══════════════════════════════════════════════════════════════════════════

CREATE TABLE IF NOT EXISTS live_sessions (
    id TEXT PRIMARY KEY,
    ticket_id TEXT NOT NULL,
    
    -- Session Info
    join_code TEXT NOT NULL UNIQUE,               -- 6-char code
    qr_code_url TEXT,
    
    -- Mode tracking
    current_mode TEXT NOT NULL DEFAULT 'video',   -- video, audio, chat, status
    mode_history TEXT,                            -- JSON array of mode changes
    
    -- Participants
    client_joined INTEGER DEFAULT 0,
    staff_id TEXT,
    
    -- Timing
    started_at TEXT NOT NULL DEFAULT (datetime('now')),
    ended_at TEXT,
    duration_seconds INTEGER,
    
    -- Quality metrics
    video_quality TEXT,                           -- 720p, 480p, audio-only
    connection_drops INTEGER DEFAULT 0,
    
    -- Summary (AI-generated after session)
    ai_summary TEXT,                              -- JSON: 5 bullets
    ai_risks TEXT,
    ai_followups TEXT,                            -- JSON array
    
    FOREIGN KEY (ticket_id) REFERENCES tickets(id)
);

CREATE INDEX idx_sessions_ticket_id ON live_sessions(ticket_id);
CREATE INDEX idx_sessions_join_code ON live_sessions(join_code);
CREATE INDEX idx_sessions_started_at ON live_sessions(started_at);

-- ═══════════════════════════════════════════════════════════════════════════
-- UPLOADS - R2 object tracking
-- ═══════════════════════════════════════════════════════════════════════════

CREATE TABLE IF NOT EXISTS uploads (
    id TEXT PRIMARY KEY,
    ticket_id TEXT NOT NULL,
    
    -- R2 Info
    r2_key TEXT NOT NULL,
    r2_bucket TEXT NOT NULL DEFAULT 'noizylab-uploads',
    
    -- File Info
    filename TEXT NOT NULL,
    content_type TEXT NOT NULL,
    size_bytes INTEGER NOT NULL,
    
    -- Metadata
    upload_type TEXT NOT NULL,                    -- photo, log, screenshot, receipt, document
    description TEXT,
    
    -- Upload source
    uploaded_by TEXT NOT NULL,                    -- client, staff
    uploaded_at TEXT NOT NULL DEFAULT (datetime('now')),
    
    -- Security
    presigned_url_expires TEXT,
    
    FOREIGN KEY (ticket_id) REFERENCES tickets(id)
);

CREATE INDEX idx_uploads_ticket_id ON uploads(ticket_id);
CREATE INDEX idx_uploads_r2_key ON uploads(r2_key);

-- ═══════════════════════════════════════════════════════════════════════════
-- FOLLOWUPS - Scheduled check-ins
-- ═══════════════════════════════════════════════════════════════════════════

CREATE TABLE IF NOT EXISTS followups (
    id TEXT PRIMARY KEY,
    ticket_id TEXT NOT NULL,
    
    -- Schedule
    scheduled_for TEXT NOT NULL,                  -- ISO timestamp
    followup_type TEXT NOT NULL,                  -- 7d, 30d, custom
    
    -- Check details
    check_description TEXT NOT NULL,              -- What to verify
    playbook_id TEXT,                             -- Related playbook
    
    -- Status
    status TEXT NOT NULL DEFAULT 'pending',       -- pending, completed, skipped
    completed_at TEXT,
    result TEXT,                                  -- JSON: outcome details
    
    -- AI generated?
    ai_suggested INTEGER DEFAULT 0,
    
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    
    FOREIGN KEY (ticket_id) REFERENCES tickets(id)
);

CREATE INDEX idx_followups_scheduled_for ON followups(scheduled_for);
CREATE INDEX idx_followups_status ON followups(status);
CREATE INDEX idx_followups_ticket_id ON followups(ticket_id);

-- ═══════════════════════════════════════════════════════════════════════════
-- STAFF - Staff members with Access integration
-- ═══════════════════════════════════════════════════════════════════════════

CREATE TABLE IF NOT EXISTS staff (
    id TEXT PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    
    -- Access integration
    access_user_id TEXT,
    
    -- Role
    role TEXT NOT NULL DEFAULT 'tech',            -- admin, tech, support
    
    -- Stats
    tickets_handled INTEGER DEFAULT 0,
    avg_resolution_hours REAL,
    
    -- Status
    is_active INTEGER DEFAULT 1,
    last_login TEXT,
    
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- ═══════════════════════════════════════════════════════════════════════════
-- PLAYBOOK APPLICATIONS - Track which playbooks were applied
-- ═══════════════════════════════════════════════════════════════════════════

CREATE TABLE IF NOT EXISTS playbook_applications (
    id TEXT PRIMARY KEY,
    ticket_id TEXT NOT NULL,
    playbook_id TEXT NOT NULL,                    -- PB1-PB12
    
    -- Application details
    applied_by TEXT NOT NULL,                     -- staff_id
    applied_at TEXT NOT NULL DEFAULT (datetime('now')),
    
    -- Steps tracking
    steps_completed TEXT,                         -- JSON array of completed step IDs
    all_steps_done INTEGER DEFAULT 0,
    
    -- Outcome
    fix_successful INTEGER,
    prevent_measures_applied INTEGER DEFAULT 0,
    followup_scheduled INTEGER DEFAULT 0,
    
    -- Notes
    notes TEXT,
    
    FOREIGN KEY (ticket_id) REFERENCES tickets(id)
);

CREATE INDEX idx_playbook_apps_ticket_id ON playbook_applications(ticket_id);
CREATE INDEX idx_playbook_apps_playbook_id ON playbook_applications(playbook_id);

-- ═══════════════════════════════════════════════════════════════════════════
-- BILLING - Invoice and payment tracking
-- ═══════════════════════════════════════════════════════════════════════════

CREATE TABLE IF NOT EXISTS billing (
    id TEXT PRIMARY KEY,
    ticket_id TEXT NOT NULL,
    
    -- Amounts
    labor_amount REAL DEFAULT 0,
    parts_amount REAL DEFAULT 0,
    total_amount REAL NOT NULL,
    tax_amount REAL DEFAULT 0,
    
    -- Status
    status TEXT NOT NULL DEFAULT 'draft',         -- draft, sent, approved, paid
    
    -- Payment
    payment_method TEXT,                          -- cash, etransfer, card
    paid_at TEXT,
    
    -- Timestamps
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    sent_at TEXT,
    
    FOREIGN KEY (ticket_id) REFERENCES tickets(id)
);

CREATE INDEX idx_billing_ticket_id ON billing(ticket_id);
CREATE INDEX idx_billing_status ON billing(status);

-- ═══════════════════════════════════════════════════════════════════════════
-- AI ANALYSIS LOG - Full AI audit trail
-- ═══════════════════════════════════════════════════════════════════════════

CREATE TABLE IF NOT EXISTS ai_analysis (
    id TEXT PRIMARY KEY,
    ticket_id TEXT NOT NULL,
    
    -- Analysis type
    analysis_type TEXT NOT NULL,                  -- intake, session_summary, followup_check
    
    -- AI Details
    model TEXT NOT NULL,                          -- claude-3-5-sonnet, etc.
    model_version TEXT,
    
    -- Input/Output
    input_text TEXT NOT NULL,
    output_json TEXT NOT NULL,
    
    -- Quality
    confidence TEXT NOT NULL,                     -- green, yellow, red
    confidence_score REAL,
    reasoning TEXT,
    
    -- Human review
    staff_reviewed INTEGER DEFAULT 0,
    staff_approved INTEGER,
    staff_corrections TEXT,
    
    -- Timing
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    processing_ms INTEGER,
    
    FOREIGN KEY (ticket_id) REFERENCES tickets(id)
);

CREATE INDEX idx_ai_analysis_ticket_id ON ai_analysis(ticket_id);
CREATE INDEX idx_ai_analysis_type ON ai_analysis(analysis_type);
CREATE INDEX idx_ai_analysis_confidence ON ai_analysis(confidence);

-- ═══════════════════════════════════════════════════════════════════════════
-- EMAIL THREADS - Gmail integration tracking
-- ═══════════════════════════════════════════════════════════════════════════

CREATE TABLE IF NOT EXISTS email_threads (
    id TEXT PRIMARY KEY,                          -- Gmail thread ID
    ticket_id TEXT,
    
    -- Thread info
    subject TEXT NOT NULL,
    from_email TEXT NOT NULL,
    to_alias TEXT NOT NULL,                       -- help, hello, rsp
    
    -- Gmail labels
    current_labels TEXT,                          -- JSON array
    
    -- Status
    last_message_at TEXT,
    message_count INTEGER DEFAULT 1,
    
    -- Linking
    linked_at TEXT,
    
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    
    FOREIGN KEY (ticket_id) REFERENCES tickets(id)
);

CREATE INDEX idx_email_threads_ticket_id ON email_threads(ticket_id);
CREATE INDEX idx_email_threads_from_email ON email_threads(from_email);

-- ═══════════════════════════════════════════════════════════════════════════
-- PATTERN METRICS - For repeat risk scoring
-- ═══════════════════════════════════════════════════════════════════════════

CREATE TABLE IF NOT EXISTS pattern_metrics (
    id TEXT PRIMARY KEY,
    client_email TEXT NOT NULL,
    
    -- Counts
    total_tickets INTEGER DEFAULT 0,
    tickets_last_90_days INTEGER DEFAULT 0,
    
    -- Patterns
    most_common_persona TEXT,
    most_common_tags TEXT,                        -- JSON array
    repeat_issues TEXT,                           -- JSON array
    
    -- Risk
    repeat_risk_score REAL DEFAULT 0,             -- 0-100
    last_calculated TEXT,
    
    -- Prevention
    preventions_applied TEXT,                     -- JSON array
    prevention_success_rate REAL,
    
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX idx_patterns_client_email ON pattern_metrics(client_email);
CREATE INDEX idx_patterns_risk_score ON pattern_metrics(repeat_risk_score);

-- ═══════════════════════════════════════════════════════════════════════════
-- VIEWS - Useful aggregations
-- ═══════════════════════════════════════════════════════════════════════════

-- Active tickets by status
CREATE VIEW IF NOT EXISTS v_ticket_board AS
SELECT 
    status,
    COUNT(*) as count,
    GROUP_CONCAT(id) as ticket_ids
FROM tickets
WHERE status != '5-DONE'
GROUP BY status
ORDER BY status;

-- Today's followups
CREATE VIEW IF NOT EXISTS v_todays_followups AS
SELECT 
    f.*,
    t.client_name,
    t.device_type,
    t.issue_summary
FROM followups f
JOIN tickets t ON f.ticket_id = t.id
WHERE f.status = 'pending'
AND date(f.scheduled_for) <= date('now')
ORDER BY f.scheduled_for;

-- High risk clients
CREATE VIEW IF NOT EXISTS v_high_risk_clients AS
SELECT *
FROM pattern_metrics
WHERE repeat_risk_score > 50
ORDER BY repeat_risk_score DESC;

-- ═══════════════════════════════════════════════════════════════════════════
-- SEED DATA - Initial personas and tags
-- ═══════════════════════════════════════════════════════════════════════════

-- This would typically be in a separate seed file, but included for completeness
-- Personas and tags are stored in JSON config files, not in DB
