#!/usr/bin/env bash
# D1 SUPERTOOL v2: safer, louder, auto-backup version
# Usage:
#   ./d1-super.sh [DB_NAME] [BINDING] [WRANGLER_TOML]
# Defaults:
#   DB_NAME       = noizylab-ultimate
#   BINDING       = DB
#   WRANGLER_TOML = wrangler.toml

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

DB_NAME="${1:-noizylab-ultimate}"
BINDING="${2:-DB}"
WRANGLER_TOML="${3:-wrangler.toml}"
LOG_FILE="$SCRIPT_DIR/d1-super.log"

log() {
  echo "$@" | tee -a "$LOG_FILE"
}

log ""
log "🚀 D1 SUPERTOOL v2"
log "   Project dir : $SCRIPT_DIR"
log "   DB Name     : $DB_NAME"
log "   Binding     : $BINDING"
log "   Config file : $WRANGLER_TOML"
log "   Log file    : $LOG_FILE"
log "────────────────────────────────────────"

# 1) Sanity checks
if ! command -v wrangler >/dev/null 2>&1; then
  log "❌ wrangler not found. Install Cloudflare Wrangler first."
  exit 1
fi

if ! command -v jq >/dev/null 2>&1; then
  log "❌ jq not found. Install jq (brew install jq) and rerun. (brew install jq)"
  exit 1
fi

log "👤 Wrangler account:"
if ! wrangler whoami 2>&1 | tee -a "$LOG_FILE"; then
  log "❌ wrangler whoami failed. Make sure you're logged in (wrangler login)."
  exit 1
fi

# 2) Check if DB exists
log ""
log "🔎 Checking for existing D1 database: $DB_NAME"

DB_JSON="$(wrangler d1 list --json 2>>"$LOG_FILE" || echo "[]")"

DB_ID="$(
  echo "$DB_JSON" | jq -r --arg NAME "$DB_NAME" '.[] | select(.name == $NAME) | .uuid' | head -n1
)"

if [[ -n "${DB_ID:-}" ]]; then
  log "✅ Database already exists."
  log "   Name: $DB_NAME"
  log "   ID  : $DB_ID"
else
  log "🆕 Database not found in list. Attempting to create..."
  if ! CREATE_JSON="$(wrangler d1 create "$DB_NAME" --json 2>>"$LOG_FILE")"; then
    log "❌ wrangler d1 create failed."
    log "   Wrangler may think the DB exists in another account or region."
    log "   Check the Cloudflare dashboard for a D1 DB named: $DB_NAME"
    exit 1
  fi

  DB_ID="$(
    echo "$CREATE_JSON" | jq -r '.uuid // .id // .database_id // empty'
  )"

  if [[ -z "${DB_ID:-}" ]]; then
    log "❌ Could not parse database ID from create response:"
    echo "$CREATE_JSON" | tee -a "$LOG_FILE"
    exit 1
  fi

  log "✅ Created D1 database:"
  log "   Name: $DB_NAME"
  log "   ID  : $DB_ID"
fi

log ""

# 3) Ensure wrangler.toml exists (and backup if it does)
if [[ -f "$WRANGLER_TOML" ]]; then
  TS="$(date +%Y%m%d-%H%M%S)"
  BACKUP="${WRANGLER_TOML}.bak-${TS}"
  cp "$WRANGLER_TOML" "$BACKUP"
  log "🛟 Existing $WRANGLER_TOML backed up as:"
  log "   $BACKUP"
else
  log "📄 $WRANGLER_TOML not found. Creating a fresh one..."
  cat > "$WRANGLER_TOML" <<EOF_INNER
name = "noizylab-ultimate-worker"
main = "src/index.ts"
compatibility_date = "2025-01-01"

EOF_INNER
fi

# 4) Check if there is already a D1 binding pointing to this DB
if grep -q "database_id *= *\"$DB_ID\"" "$WRANGLER_TOML"; then
  log "ℹ️ wrangler.toml already has a D1 block with this database_id."
else
  log "🧩 Appending D1 database block to $WRANGLER_TOML..."
  cat >> "$WRANGLER_TOML" <<EOF_INNER

[[d1_databases]]
binding = "$BINDING"
database_name = "$DB_NAME"
database_id = "$DB_ID"
EOF_INNER
  log "✅ D1 block appended."
fi

log ""
log "📌 FINAL STATUS"
log "   DB Name      : $DB_NAME"
log "   DB ID        : $DB_ID"
log "   Binding      : $BINDING"
log "   Config file  : $WRANGLER_TOML"
log "   Log file     : $LOG_FILE"
log ""
log "👉 In your Worker, you can now use: env.$BINDING"
log "   Example:"
log "     const { results } = await env.$BINDING.prepare('SELECT 1 as x').all();"
log ""
log "🎉 D1 SUPERTOOL v2 complete."
