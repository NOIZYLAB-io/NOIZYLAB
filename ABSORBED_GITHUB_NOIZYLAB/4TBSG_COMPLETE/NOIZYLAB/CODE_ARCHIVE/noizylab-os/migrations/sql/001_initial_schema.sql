-- D1 DATABASE MIGRATION SCRIPT
-- Run this once to build your DB

-- clients
CREATE TABLE IF NOT EXISTS clients (
  id TEXT PRIMARY KEY,
  name TEXT,
  email TEXT,
  plan TEXT,
  created_at INTEGER
);

-- tickets
CREATE TABLE IF NOT EXISTS tickets (
  id TEXT PRIMARY KEY,
  client_id TEXT,
  issue TEXT,
  status TEXT,
  priority TEXT,
  created_at INTEGER
);

-- devices
CREATE TABLE IF NOT EXISTS devices (
  id TEXT PRIMARY KEY,
  client_id TEXT,
  type TEXT,
  os TEXT,
  last_scan INTEGER
);

-- events
CREATE TABLE IF NOT EXISTS events (
  id TEXT PRIMARY KEY,
  type TEXT,
  payload TEXT,
  ts INTEGER
);

