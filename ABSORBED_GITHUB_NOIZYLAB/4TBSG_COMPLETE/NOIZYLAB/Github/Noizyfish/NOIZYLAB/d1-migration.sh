#!/bin/bash
# D1 DATABASE MIGRATION SCRIPT
# Creates and applies D1 database migrations

set -e

DB_NAME="${1:-noizylab-db}"
MIGRATION_NAME="${2:-$(date +%Y%m%d%H%M%S)}"

echo "🗄️  Creating D1 migration: $MIGRATION_NAME"

# Create migration directory
mkdir -p migrations/sql

# Initial schema migration
cat > "migrations/sql/${MIGRATION_NAME}_initial.sql" << 'EOF'
-- NOIZYLAB OS Initial Schema

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
  id TEXT PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  created_at INTEGER DEFAULT (unixepoch()),
  updated_at INTEGER DEFAULT (unixepoch())
);

-- Intake submissions
CREATE TABLE IF NOT EXISTS intake_submissions (
  id TEXT PRIMARY KEY,
  client_id TEXT,
  form_data TEXT NOT NULL,
  status TEXT DEFAULT 'pending',
  created_at INTEGER DEFAULT (unixepoch()),
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- Events
CREATE TABLE IF NOT EXISTS events (
  id TEXT PRIMARY KEY,
  client_id TEXT,
  event_type TEXT NOT NULL,
  event_data TEXT,
  created_at INTEGER DEFAULT (unixepoch()),
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- AI interactions
CREATE TABLE IF NOT EXISTS ai_interactions (
  id TEXT PRIMARY KEY,
  client_id TEXT,
  provider TEXT NOT NULL,
  prompt TEXT NOT NULL,
  response TEXT,
  tokens_used INTEGER,
  created_at INTEGER DEFAULT (unixepoch()),
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_clients_email ON clients(email);
CREATE INDEX IF NOT EXISTS idx_intake_client ON intake_submissions(client_id);
CREATE INDEX IF NOT EXISTS idx_events_client ON events(client_id);
CREATE INDEX IF NOT EXISTS idx_ai_client ON ai_interactions(client_id);
EOF

echo "✅ Migration created: migrations/sql/${MIGRATION_NAME}_initial.sql"
echo ""
echo "📋 To apply migration:"
echo "   wrangler d1 migrations apply $DB_NAME --local"
echo "   wrangler d1 migrations apply $DB_NAME --remote"

