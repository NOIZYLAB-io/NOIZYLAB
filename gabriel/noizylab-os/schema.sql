-- NoizyLab OS - D1 Schema
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS tickets (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  public_id TEXT NOT NULL UNIQUE,
  status TEXT NOT NULL,
  channel TEXT NOT NULL, -- help/hello/rsp/portal
  subject TEXT,
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
  mime TEXT,
  size INTEGER,
  created_at TEXT NOT NULL,
  FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

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
