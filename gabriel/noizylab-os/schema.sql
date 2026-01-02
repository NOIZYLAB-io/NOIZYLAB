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
