-- NoizyLab OS - D1 Schema
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS tickets (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  public_id TEXT NOT NULL UNIQUE,
  status TEXT NOT NULL,
  channel TEXT NOT NULL, -- help/hello/rsp/portal
  subject TEXT,
  client_id INTEGER,
  device_id INTEGER,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ticket_access (
  ticket_id INTEGER NOT NULL UNIQUE,
  secret_hash TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  type TEXT NOT NULL,
  actor_type TEXT NOT NULL, -- public/staff/system/ai
  actor_id TEXT,
  payload_json TEXT,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_events_ticket ON events(ticket_id, created_at);

CREATE TABLE IF NOT EXISTS uploads (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  r2_key TEXT NOT NULL,
  filename TEXT,
  content_type TEXT,
  bytes INTEGER,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_uploads_ticket ON uploads(ticket_id);

CREATE TABLE IF NOT EXISTS live_rooms (
  room_id TEXT PRIMARY KEY,
  code TEXT NOT NULL UNIQUE,
  ticket_id INTEGER,
  expires_at TEXT NOT NULL,
  created_at TEXT NOT NULL,
  meeting_id TEXT,
  staff_participant_id TEXT,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_live_rooms_code ON live_rooms(code);
CREATE INDEX IF NOT EXISTS idx_live_rooms_expires ON live_rooms(expires_at);

CREATE TABLE IF NOT EXISTS followups (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  type TEXT NOT NULL, -- 7d/30d/etc
  due_at TEXT NOT NULL,
  status TEXT NOT NULL, -- scheduled/done
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS persona_tags (
  ticket_id INTEGER NOT NULL UNIQUE,
  persona TEXT,
  tags_json TEXT,
  confidence REAL,
  updated_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

-- PLAYBOOK TABLES
CREATE TABLE IF NOT EXISTS playbooks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  persona TEXT,
  tags_json TEXT,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS playbook_steps (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  playbook_id INTEGER NOT NULL,
  os TEXT NOT NULL,           -- "win" | "mac" | "both"
  step_order INTEGER NOT NULL,
  title TEXT NOT NULL,
  detail TEXT,
  FOREIGN KEY(playbook_id) REFERENCES playbooks(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS playbook_runs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  playbook_id INTEGER NOT NULL,
  status TEXT NOT NULL,       -- "running" | "completed"
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE,
  FOREIGN KEY(playbook_id) REFERENCES playbooks(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS playbook_run_steps (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id INTEGER NOT NULL,
  step_id INTEGER NOT NULL,
  done INTEGER NOT NULL DEFAULT 0,
  done_at TEXT,
  FOREIGN KEY(run_id) REFERENCES playbook_runs(id) ON DELETE CASCADE,
  FOREIGN KEY(step_id) REFERENCES playbook_steps(id) ON DELETE CASCADE
);

-- PUBLIC ACTION TOKENS (for approve/decline links without exposing ticket secret)
CREATE TABLE IF NOT EXISTS public_actions (
  token TEXT PRIMARY KEY,
  ticket_id INTEGER NOT NULL,
  type TEXT NOT NULL,          -- "estimate_approve" | "estimate_decline"
  payload_json TEXT,           -- { estimateId: number }
  expires_at TEXT NOT NULL,
  redeemed_at TEXT,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_public_actions_ticket ON public_actions(ticket_id);
CREATE INDEX IF NOT EXISTS idx_public_actions_expires ON public_actions(expires_at);

-- ESTIMATES
CREATE TABLE IF NOT EXISTS estimates (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  amount_cents INTEGER NOT NULL,
  currency TEXT NOT NULL,
  summary TEXT NOT NULL,
  terms TEXT,
  status TEXT NOT NULL,        -- "pending" | "approved" | "declined" | "expired"
  approved_at TEXT,
  declined_at TEXT,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

-- CLIENTS
CREATE TABLE IF NOT EXISTS clients (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT,
  phone TEXT,
  name TEXT,
  created_at TEXT NOT NULL
);

-- OPERATIONAL CLIENT PROFILE (non-creepy)
CREATE TABLE IF NOT EXISTS client_profiles (
  client_id INTEGER PRIMARY KEY,
  traits_json TEXT NOT NULL,       -- ["UPDATE_AVOIDER","PASSWORD_CHAOS",...]
  comms_mode TEXT NOT NULL,        -- "calm"|"direct"
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  FOREIGN KEY(client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- DEVICES (repeat patterns)
CREATE TABLE IF NOT EXISTS devices (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  client_id INTEGER,
  label TEXT,                      -- "MacBook Pro 2019"
  os TEXT,                         -- "mac"|"win"
  fingerprint TEXT UNIQUE,         -- hash of stable fields
  notes TEXT,
  created_at TEXT NOT NULL,
  FOREIGN KEY(client_id) REFERENCES clients(id) ON DELETE SET NULL
);

-- INVOICES
CREATE TABLE IF NOT EXISTS invoices (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  status TEXT NOT NULL,            -- "draft"|"sent"|"paid"|"void"
  currency TEXT NOT NULL DEFAULT 'CAD',
  subtotal_cents INTEGER NOT NULL DEFAULT 0,
  tax_cents INTEGER NOT NULL DEFAULT 0,
  total_cents INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS invoice_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  invoice_id INTEGER NOT NULL,
  label TEXT NOT NULL,
  qty INTEGER NOT NULL DEFAULT 1,
  amount_cents INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  FOREIGN KEY(invoice_id) REFERENCES invoices(id) ON DELETE CASCADE
);

-- DAILY METRICS (rollups)
CREATE TABLE IF NOT EXISTS metrics_daily (
  day TEXT PRIMARY KEY,            -- "YYYY-MM-DD"
  json TEXT NOT NULL,
  created_at TEXT NOT NULL
);

-- FOLLOWUPS
CREATE TABLE IF NOT EXISTS followups (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  type TEXT NOT NULL,          -- "D7" | "D30" | "CUSTOM"
  due_at TEXT NOT NULL,
  status TEXT NOT NULL,        -- "scheduled" | "done" | "canceled"
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_followups_due ON followups(status, due_at);

-- IDEMPOTENCY (prevents double charges/double sessions)
CREATE TABLE IF NOT EXISTS idempotency (
  key TEXT PRIMARY KEY,
  route TEXT NOT NULL,
  request_hash TEXT NOT NULL,
  response_json TEXT NOT NULL,
  created_at TEXT NOT NULL
);

-- DLQ EVENTS (for inspection/replay)
CREATE TABLE IF NOT EXISTS dlq_events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  queue TEXT NOT NULL,
  payload_json TEXT NOT NULL,
  error TEXT,
  created_at TEXT NOT NULL
);

-- CONTROL LANES (session guardrails: auto-revoke after 30m)
CREATE TABLE IF NOT EXISTS control_lanes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  consent_id INTEGER,
  status TEXT NOT NULL,            -- "active" | "revoked" | "expired"
  granted_at TEXT NOT NULL,
  expires_at TEXT NOT NULL,        -- auto-revoke after 30m
  revoked_at TEXT,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_control_lanes_ticket ON control_lanes(ticket_id);
CREATE INDEX IF NOT EXISTS idx_control_lanes_expires ON control_lanes(expires_at);

-- TAG ENUM (controlled vocabulary, no free-text rot)
CREATE TABLE IF NOT EXISTS tag_enum (
  tag TEXT PRIMARY KEY,
  category TEXT NOT NULL,          -- "symptom" | "device" | "software" | "behavior"
  description TEXT,
  created_at TEXT NOT NULL
);

-- Default allowed tags
INSERT OR IGNORE INTO tag_enum (tag, category, description, created_at) VALUES
  ('SLOW_BOOT', 'symptom', 'Machine boots slowly', datetime('now')),
  ('CRASH', 'symptom', 'Unexpected crashes/restarts', datetime('now')),
  ('VIRUS', 'symptom', 'Suspected malware/virus', datetime('now')),
  ('NO_WIFI', 'symptom', 'WiFi connectivity issues', datetime('now')),
  ('NO_AUDIO', 'symptom', 'Sound not working', datetime('now')),
  ('NO_VIDEO', 'symptom', 'Display/graphics issues', datetime('now')),
  ('STORAGE_FULL', 'symptom', 'Disk space exhausted', datetime('now')),
  ('PASSWORD_CHAOS', 'behavior', 'User forgets passwords frequently', datetime('now')),
  ('UPDATE_AVOIDER', 'behavior', 'User delays/skips updates', datetime('now')),
  ('BACKUP_NONE', 'behavior', 'No backup strategy', datetime('now')),
  ('MAC', 'device', 'macOS device', datetime('now')),
  ('WIN', 'device', 'Windows device', datetime('now')),
  ('IPHONE', 'device', 'iPhone/iOS device', datetime('now')),
  ('ANDROID', 'device', 'Android device', datetime('now')),
  ('PRINTER', 'device', 'Printer-related', datetime('now')),
  ('EMAIL', 'software', 'Email client issues', datetime('now')),
  ('BROWSER', 'software', 'Browser-related', datetime('now')),
  ('OFFICE', 'software', 'MS Office / productivity suite', datetime('now')),
  ('ZOOM', 'software', 'Zoom/video conferencing', datetime('now')),
  ('RECURRING', 'pattern', 'Issue has happened before', datetime('now'));

-- FIX RECEIPTS (auto-generated after invoice paid)
CREATE TABLE IF NOT EXISTS fix_receipts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  invoice_id INTEGER NOT NULL,
  receipt_json TEXT NOT NULL,      -- { problem, solution, prevention, timestamps }
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE,
  FOREIGN KEY(invoice_id) REFERENCES invoices(id) ON DELETE CASCADE
);

-- UPLOAD CHUNKS (resumable uploads with checksum)
CREATE TABLE IF NOT EXISTS upload_chunks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  upload_id TEXT NOT NULL,         -- UUID for the upload session
  ticket_id INTEGER NOT NULL,
  chunk_index INTEGER NOT NULL,
  r2_key TEXT NOT NULL,
  checksum TEXT NOT NULL,          -- SHA-256 of chunk
  bytes INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE,
  UNIQUE(upload_id, chunk_index)
);

CREATE INDEX IF NOT EXISTS idx_upload_chunks_upload ON upload_chunks(upload_id);

-- EXPORTS (R2 snapshot + signed URL token in one table)
CREATE TABLE IF NOT EXISTS exports (
  token TEXT PRIMARY KEY,
  ticket_id INTEGER NOT NULL,
  r2_key TEXT NOT NULL,
  redacted INTEGER NOT NULL DEFAULT 0,
  expires_at TEXT NOT NULL,
  created_at TEXT NOT NULL,
  downloaded_at TEXT,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_exports_ticket ON exports(ticket_id);
CREATE INDEX IF NOT EXISTS idx_exports_expires ON exports(expires_at);

-- AUTO-CLOSE GUARD (tickets pending auto-close)
CREATE TABLE IF NOT EXISTS auto_close_queue (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL UNIQUE,
  warn_at TEXT NOT NULL,           -- when to send "will close soon" warning
  close_at TEXT NOT NULL,          -- when to auto-close
  warned INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_auto_close_queue_close ON auto_close_queue(close_at);

-- SLA TARGETS (response/resolution time goals)
CREATE TABLE IF NOT EXISTS sla_targets (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,              -- "standard", "premium", "enterprise"
  first_response_mins INTEGER NOT NULL,   -- target first response time
  resolution_mins INTEGER NOT NULL,       -- target resolution time
  created_at TEXT NOT NULL
);

-- SLA TRACKING (per-ticket SLA status)
CREATE TABLE IF NOT EXISTS sla_tracking (
  ticket_id INTEGER PRIMARY KEY,
  sla_target_id INTEGER,
  first_response_at TEXT,                 -- when first staff response happened
  first_response_breached INTEGER DEFAULT 0,
  resolution_at TEXT,                     -- when resolved
  resolution_breached INTEGER DEFAULT 0,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE,
  FOREIGN KEY(sla_target_id) REFERENCES sla_targets(id)
);

-- CLIENT SENTIMENT (track satisfaction over time)
CREATE TABLE IF NOT EXISTS client_sentiment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  client_id INTEGER NOT NULL,
  ticket_id INTEGER,
  score INTEGER NOT NULL,                 -- -2 to +2 (very negative to very positive)
  source TEXT NOT NULL,                   -- "survey", "ai_detected", "manual"
  notes TEXT,
  created_at TEXT NOT NULL,
  FOREIGN KEY(client_id) REFERENCES clients(id) ON DELETE CASCADE,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_sentiment_client ON client_sentiment(client_id, created_at);

-- CLIENT HEALTH SCORE (aggregate risk/health)
CREATE TABLE IF NOT EXISTS client_health (
  client_id INTEGER PRIMARY KEY,
  health_score INTEGER NOT NULL DEFAULT 100,  -- 0-100 (higher = healthier)
  risk_level TEXT NOT NULL DEFAULT 'low',     -- low/medium/high/critical
  total_tickets INTEGER DEFAULT 0,
  open_tickets INTEGER DEFAULT 0,
  avg_sentiment REAL DEFAULT 0,
  last_ticket_at TEXT,
  updated_at TEXT NOT NULL,
  FOREIGN KEY(client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- ESCALATION CHAINS (auto-escalate stale tickets)
CREATE TABLE IF NOT EXISTS escalation_rules (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  stale_hours INTEGER NOT NULL,           -- escalate after N hours with no update
  escalate_to TEXT NOT NULL,              -- "senior", "manager", "owner"
  notify_webhook TEXT,                    -- optional webhook URL
  active INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS escalations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  rule_id INTEGER NOT NULL,
  escalated_to TEXT NOT NULL,
  notified INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE,
  FOREIGN KEY(rule_id) REFERENCES escalation_rules(id)
);

CREATE INDEX IF NOT EXISTS idx_escalations_ticket ON escalations(ticket_id);

-- TICKET TEMPLATES (quick-create common issues)
CREATE TABLE IF NOT EXISTS ticket_templates (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE,              -- "slow_mac", "wifi_issue", etc.
  name TEXT NOT NULL,
  subject TEXT NOT NULL,
  default_tags TEXT,                      -- JSON array of tags
  playbook_codes TEXT,                    -- JSON array of playbook codes to auto-apply
  sla_target_id INTEGER,
  created_at TEXT NOT NULL,
  FOREIGN KEY(sla_target_id) REFERENCES sla_targets(id)
);

-- WEBHOOKS (push notifications to external services)
CREATE TABLE IF NOT EXISTS webhooks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  url TEXT NOT NULL,
  secret TEXT,                            -- HMAC signing secret
  events TEXT NOT NULL,                   -- JSON array of event types to trigger on
  active INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS webhook_deliveries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  webhook_id INTEGER NOT NULL,
  event_type TEXT NOT NULL,
  payload_json TEXT NOT NULL,
  response_code INTEGER,
  response_body TEXT,
  delivered_at TEXT,
  created_at TEXT NOT NULL,
  FOREIGN KEY(webhook_id) REFERENCES webhooks(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_webhook_deliveries_webhook ON webhook_deliveries(webhook_id, created_at);

-- TICKET DUPLICATES (link related/duplicate tickets)
CREATE TABLE IF NOT EXISTS ticket_links (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  linked_ticket_id INTEGER NOT NULL,
  link_type TEXT NOT NULL,                -- "duplicate", "related", "parent", "child"
  created_by TEXT,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE,
  FOREIGN KEY(linked_ticket_id) REFERENCES tickets(id) ON DELETE CASCADE,
  UNIQUE(ticket_id, linked_ticket_id)
);

-- ACTIVITY HEATMAP (when issues happen)
CREATE TABLE IF NOT EXISTS activity_heatmap (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  day_of_week INTEGER NOT NULL,           -- 0=Sunday, 6=Saturday
  hour_of_day INTEGER NOT NULL,           -- 0-23
  ticket_count INTEGER NOT NULL DEFAULT 0,
  updated_at TEXT NOT NULL,
  UNIQUE(day_of_week, hour_of_day)
);

-- BULK OPERATIONS LOG
CREATE TABLE IF NOT EXISTS bulk_ops (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  operation TEXT NOT NULL,                -- "tag", "close", "assign", "delete"
  ticket_ids TEXT NOT NULL,               -- JSON array
  params_json TEXT,                       -- operation params
  affected_count INTEGER NOT NULL,
  actor_id TEXT NOT NULL,
  created_at TEXT NOT NULL
);

-- SAVED SEARCHES (staff quick filters)
CREATE TABLE IF NOT EXISTS saved_searches (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  query_json TEXT NOT NULL,               -- saved filter criteria
  staff_id TEXT,                          -- null = shared
  created_at TEXT NOT NULL
);

-- Insert default SLA targets
INSERT OR IGNORE INTO sla_targets (id, name, first_response_mins, resolution_mins, created_at)
VALUES 
  (1, 'standard', 240, 2880, datetime('now')),      -- 4h response, 48h resolution
  (2, 'premium', 60, 1440, datetime('now')),        -- 1h response, 24h resolution
  (3, 'enterprise', 15, 480, datetime('now'));      -- 15m response, 8h resolution

-- Insert default escalation rules
INSERT OR IGNORE INTO escalation_rules (id, name, stale_hours, escalate_to, active, created_at)
VALUES
  (1, 'stale_24h', 24, 'senior', 1, datetime('now')),
  (2, 'stale_48h', 48, 'manager', 1, datetime('now')),
  (3, 'critical_4h', 4, 'owner', 1, datetime('now'));

-- =====================================================
-- LEGENDARY UPGRADES
-- =====================================================

-- KNOWLEDGE BASE ARTICLES
CREATE TABLE IF NOT EXISTS kb_articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  slug TEXT NOT NULL UNIQUE,
  title TEXT NOT NULL,
  content TEXT NOT NULL,                  -- Markdown content
  category TEXT,
  tags_json TEXT,                         -- JSON array of tags
  views INTEGER DEFAULT 0,
  helpful_yes INTEGER DEFAULT 0,
  helpful_no INTEGER DEFAULT 0,
  status TEXT NOT NULL DEFAULT 'draft',   -- draft/published/archived
  created_by TEXT,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_kb_articles_status ON kb_articles(status);
CREATE INDEX IF NOT EXISTS idx_kb_articles_category ON kb_articles(category);

-- KB ARTICLE LINKS (suggest articles for tickets)
CREATE TABLE IF NOT EXISTS kb_ticket_links (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  article_id INTEGER NOT NULL,
  suggested_by TEXT NOT NULL,             -- "ai", "staff", "client"
  helpful INTEGER,                        -- 1=yes, 0=no, null=not rated
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE,
  FOREIGN KEY(article_id) REFERENCES kb_articles(id) ON DELETE CASCADE,
  UNIQUE(ticket_id, article_id)
);

-- SCHEDULING / APPOINTMENTS
CREATE TABLE IF NOT EXISTS appointments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER,
  client_id INTEGER,
  staff_id TEXT NOT NULL,
  title TEXT NOT NULL,
  description TEXT,
  start_at TEXT NOT NULL,
  end_at TEXT NOT NULL,
  location TEXT,                          -- "remote", "onsite", address
  status TEXT NOT NULL DEFAULT 'scheduled', -- scheduled/confirmed/completed/cancelled/no_show
  reminder_sent INTEGER DEFAULT 0,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE SET NULL,
  FOREIGN KEY(client_id) REFERENCES clients(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_appointments_staff ON appointments(staff_id, start_at);
CREATE INDEX IF NOT EXISTS idx_appointments_client ON appointments(client_id, start_at);

-- STAFF AVAILABILITY
CREATE TABLE IF NOT EXISTS staff_availability (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  staff_id TEXT NOT NULL,
  day_of_week INTEGER NOT NULL,           -- 0=Sunday, 6=Saturday
  start_time TEXT NOT NULL,               -- "09:00"
  end_time TEXT NOT NULL,                 -- "17:00"
  is_available INTEGER DEFAULT 1,
  UNIQUE(staff_id, day_of_week)
);

-- STAFF BLOCKED TIME (vacations, meetings, etc)
CREATE TABLE IF NOT EXISTS staff_blocked_time (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  staff_id TEXT NOT NULL,
  start_at TEXT NOT NULL,
  end_at TEXT NOT NULL,
  reason TEXT,
  created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_staff_blocked ON staff_blocked_time(staff_id, start_at);

-- EMAIL THREADS (inbound/outbound email tracking)
CREATE TABLE IF NOT EXISTS email_threads (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER,
  thread_id TEXT NOT NULL UNIQUE,         -- Email thread ID for threading
  subject TEXT NOT NULL,
  from_email TEXT NOT NULL,
  to_email TEXT NOT NULL,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_email_threads_ticket ON email_threads(ticket_id);

-- EMAIL MESSAGES
CREATE TABLE IF NOT EXISTS email_messages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  thread_id INTEGER NOT NULL,
  message_id TEXT NOT NULL UNIQUE,        -- Email message ID
  direction TEXT NOT NULL,                -- "inbound" or "outbound"
  from_email TEXT NOT NULL,
  to_email TEXT NOT NULL,
  subject TEXT,
  body_text TEXT,
  body_html TEXT,
  status TEXT NOT NULL DEFAULT 'sent',    -- sent/delivered/bounced/failed
  created_at TEXT NOT NULL,
  FOREIGN KEY(thread_id) REFERENCES email_threads(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_email_messages_thread ON email_messages(thread_id);

-- EMAIL TEMPLATES
CREATE TABLE IF NOT EXISTS email_templates (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  subject TEXT NOT NULL,
  body_text TEXT NOT NULL,
  body_html TEXT,
  variables_json TEXT,                    -- JSON array of variable names
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

-- NOTIFICATIONS (push/email/sms queue)
CREATE TABLE IF NOT EXISTS notifications (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_type TEXT NOT NULL,                -- "client" or "staff"
  user_id TEXT NOT NULL,
  channel TEXT NOT NULL,                  -- "email", "push", "sms", "in_app"
  type TEXT NOT NULL,                     -- "ticket_update", "sla_breach", "appointment_reminder"
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  data_json TEXT,                         -- extra payload
  status TEXT NOT NULL DEFAULT 'pending', -- pending/sent/delivered/failed
  scheduled_at TEXT,                      -- for scheduled notifications
  sent_at TEXT,
  created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_notifications_status ON notifications(status, scheduled_at);
CREATE INDEX IF NOT EXISTS idx_notifications_user ON notifications(user_type, user_id);

-- PUSH SUBSCRIPTIONS (Web Push)
CREATE TABLE IF NOT EXISTS push_subscriptions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_type TEXT NOT NULL,
  user_id TEXT NOT NULL,
  endpoint TEXT NOT NULL,
  keys_json TEXT NOT NULL,                -- {p256dh, auth}
  created_at TEXT NOT NULL,
  UNIQUE(user_type, user_id, endpoint)
);

-- API KEYS (for integrations)
CREATE TABLE IF NOT EXISTS api_keys (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  key_hash TEXT NOT NULL UNIQUE,
  prefix TEXT NOT NULL,                   -- first 8 chars for identification
  scopes_json TEXT NOT NULL,              -- JSON array of allowed scopes
  last_used_at TEXT,
  expires_at TEXT,
  created_by TEXT NOT NULL,
  created_at TEXT NOT NULL
);

-- AUDIT LOG (comprehensive)
CREATE TABLE IF NOT EXISTS audit_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  actor_type TEXT NOT NULL,               -- "staff", "client", "system", "api"
  actor_id TEXT,
  action TEXT NOT NULL,                   -- "create", "update", "delete", "view", "export"
  resource_type TEXT NOT NULL,            -- "ticket", "client", "article", etc
  resource_id TEXT,
  changes_json TEXT,                      -- before/after diff
  ip_address TEXT,
  user_agent TEXT,
  created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_audit_log_resource ON audit_log(resource_type, resource_id);
CREATE INDEX IF NOT EXISTS idx_audit_log_actor ON audit_log(actor_type, actor_id);
CREATE INDEX IF NOT EXISTS idx_audit_log_created ON audit_log(created_at);

-- DATA RETENTION REQUESTS (GDPR)
CREATE TABLE IF NOT EXISTS gdpr_requests (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  client_id INTEGER NOT NULL,
  request_type TEXT NOT NULL,             -- "export", "delete", "restrict"
  status TEXT NOT NULL DEFAULT 'pending', -- pending/processing/completed/rejected
  requested_at TEXT NOT NULL,
  completed_at TEXT,
  notes TEXT,
  FOREIGN KEY(client_id) REFERENCES clients(id)
);

-- REPORTS (scheduled/saved reports)
CREATE TABLE IF NOT EXISTS reports (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  type TEXT NOT NULL,                     -- "ticket_volume", "sla_compliance", "staff_performance"
  params_json TEXT NOT NULL,              -- report parameters
  schedule TEXT,                          -- cron expression for scheduled reports
  last_run_at TEXT,
  created_by TEXT NOT NULL,
  created_at TEXT NOT NULL
);

-- REPORT RUNS (generated report instances)
CREATE TABLE IF NOT EXISTS report_runs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  report_id INTEGER NOT NULL,
  status TEXT NOT NULL DEFAULT 'running', -- running/completed/failed
  result_json TEXT,
  r2_key TEXT,                            -- for large reports stored in R2
  started_at TEXT NOT NULL,
  completed_at TEXT,
  FOREIGN KEY(report_id) REFERENCES reports(id) ON DELETE CASCADE
);

-- AI SUGGESTIONS (for triage, responses, etc)
CREATE TABLE IF NOT EXISTS ai_suggestions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  type TEXT NOT NULL,                     -- "triage", "response", "playbook", "article", "priority"
  suggestion_json TEXT NOT NULL,          -- the AI suggestion
  confidence REAL,                        -- 0.0 to 1.0
  accepted INTEGER,                       -- 1=accepted, 0=rejected, null=pending
  accepted_by TEXT,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_ai_suggestions_ticket ON ai_suggestions(ticket_id);

-- CANNED RESPONSES (quick reply templates)
CREATE TABLE IF NOT EXISTS canned_responses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  content TEXT NOT NULL,
  category TEXT,
  use_count INTEGER DEFAULT 0,
  created_by TEXT,
  created_at TEXT NOT NULL
);

-- SLACK/DISCORD INTEGRATIONS
CREATE TABLE IF NOT EXISTS chat_integrations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  platform TEXT NOT NULL,                 -- "slack", "discord"
  workspace_id TEXT NOT NULL,
  channel_id TEXT NOT NULL,
  channel_name TEXT,
  webhook_url TEXT,
  bot_token TEXT,
  events_json TEXT NOT NULL,              -- which events to post
  active INTEGER DEFAULT 1,
  created_at TEXT NOT NULL,
  UNIQUE(platform, workspace_id, channel_id)
);

-- TICKET TIMERS (time tracking)
CREATE TABLE IF NOT EXISTS ticket_timers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL,
  staff_id TEXT NOT NULL,
  started_at TEXT NOT NULL,
  stopped_at TEXT,
  duration_mins INTEGER,                  -- calculated on stop
  description TEXT,
  billable INTEGER DEFAULT 1,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_ticket_timers_ticket ON ticket_timers(ticket_id);

-- SATISFACTION SURVEYS
CREATE TABLE IF NOT EXISTS surveys (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL UNIQUE,
  token TEXT NOT NULL UNIQUE,
  rating INTEGER,                         -- 1-5 stars
  feedback TEXT,
  submitted_at TEXT,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

-- Insert default email templates
INSERT OR IGNORE INTO email_templates (id, code, name, subject, body_text, variables_json, created_at, updated_at)
VALUES
  (1, 'ticket_created', 'Ticket Created', 'Your support request #{{ticket_id}} has been received', 
   'Hi {{client_name}},\n\nWe have received your support request.\n\nTicket ID: {{ticket_id}}\nSubject: {{subject}}\n\nWe will get back to you shortly.\n\nBest,\nNoizyLab Support',
   '["ticket_id","client_name","subject"]', datetime('now'), datetime('now')),
  (2, 'ticket_resolved', 'Ticket Resolved', 'Your support request #{{ticket_id}} has been resolved',
   'Hi {{client_name}},\n\nYour support request has been resolved.\n\nTicket ID: {{ticket_id}}\nResolution: {{resolution}}\n\nPlease let us know if you have any questions.\n\nBest,\nNoizyLab Support',
   '["ticket_id","client_name","resolution"]', datetime('now'), datetime('now')),
  (3, 'appointment_reminder', 'Appointment Reminder', 'Reminder: Your appointment is coming up',
   'Hi {{client_name}},\n\nThis is a reminder that you have an appointment scheduled:\n\nDate: {{date}}\nTime: {{time}}\nLocation: {{location}}\n\nSee you soon!\n\nBest,\nNoizyLab Support',
   '["client_name","date","time","location"]', datetime('now'), datetime('now'));

-- Insert default canned responses
INSERT OR IGNORE INTO canned_responses (id, code, name, content, category, created_at)
VALUES
  (1, 'greeting', 'Greeting', 'Hi! Thanks for reaching out. I am happy to help you with this.', 'general', datetime('now')),
  (2, 'need_more_info', 'Need More Info', 'Could you please provide more details about the issue? Specifically:\n- When did this start?\n- What were you doing when it happened?\n- Any error messages?', 'general', datetime('now')),
  (3, 'checking', 'Checking On It', 'I am looking into this now. I will update you shortly.', 'status', datetime('now')),
  (4, 'resolved', 'Issue Resolved', 'Great news! The issue has been resolved. Please let me know if you experience any further problems.', 'resolution', datetime('now')),
  (5, 'escalating', 'Escalating', 'I am escalating this to our senior team for further investigation. You will hear back within 24 hours.', 'status', datetime('now'));
