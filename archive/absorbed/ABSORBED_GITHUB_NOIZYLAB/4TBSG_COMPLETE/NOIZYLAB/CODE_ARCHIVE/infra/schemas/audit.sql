CREATE TABLE IF NOT EXISTS requests (
  id TEXT PRIMARY KEY,
  agent TEXT NOT NULL,
  method TEXT,
  path TEXT,
  ts INTEGER,
  ms INTEGER,
  status INTEGER
);
CREATE TABLE IF NOT EXISTS traces (
  id TEXT,
  step INTEGER,
  label TEXT,
  data TEXT,
  ts INTEGER,
  PRIMARY KEY (id, step)
);

