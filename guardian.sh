#!/bin/bash
set -e

echo "🛡️  NoizyLab OS Guardian Running..."
echo ""

BASE="/Users/m2ultra/NOIZYLAB/noizylab-os"
ERRORS=0
WARNINGS=0

check() {
  if [ ! -f "$1" ] && [ ! -d "$1" ]; then
    echo "❌ Missing: $1"
    ((ERRORS++))
    return 1
  else
    echo "✔️  $1"
    return 0
  fi
}

check_warn() {
  if [ ! -f "$1" ] && [ ! -d "$1" ]; then
    echo "⚠️  Missing: $1"
    ((WARNINGS++))
    return 1
  else
    echo "✔️  $1"
    return 0
  fi
}

# Core directories
echo "📁 Checking core directories..."
check "$BASE/workers"
check "$BASE/ai"
check "$BASE/d1" || check_warn "$BASE/db"
check "$BASE/scripts"
check "$BASE/supercode"

# Workers
echo ""
echo "🏗️  Checking Workers..."
WORKERS=(
    "workers/ai-super-worker"
    "workers/super-worker"
    "workers/intake"
    "workers/mc96"
    "workers/teamviewer"
    "workers/agent-arbiter"
    "workers/dreamchamber"
    "workers/events"
)

for worker in "${WORKERS[@]}"; do
    check_warn "$BASE/$worker"
done

# CLI tools
echo ""
echo "🛠️  Checking CLI tools..."
check_warn "/usr/local/bin/cfw"
check_warn "/usr/local/bin/gemini"
check_warn "/usr/local/bin/claude"
check_warn "/usr/local/bin/wrangler"

# Configuration files
echo ""
echo "⚙️  Checking configuration..."
check_warn "$BASE/.env"
check_warn "$BASE/wrangler.toml"
check_warn "$BASE/package.json"

# AI Router
echo ""
echo "🤖 Checking AI Router..."
check_warn "$BASE/ai/router"
check_warn "$BASE/ai/router/wrangler.toml"

# Database
echo ""
echo "💾 Checking database..."
check_warn "$BASE/migrations/sql/001_initial_schema.sql"
check_warn "$BASE/db/schema/init.sql"

# Scripts
echo ""
echo "📜 Checking scripts..."
check "$BASE/scripts/deploy.sh"
check_warn "$BASE/scripts/validate-setup.sh"

# Environment variables
echo ""
echo "🔐 Checking environment..."
if [ -f "$BASE/.env" ]; then
    source "$BASE/.env"
    
    [ -z "$CF_ACCOUNT_ID" ] && echo "⚠️  CF_ACCOUNT_ID not set" && ((WARNINGS++)) || echo "✔️  CF_ACCOUNT_ID"
    [ -z "$CF_API_TOKEN" ] && echo "⚠️  CF_API_TOKEN not set" && ((WARNINGS++)) || echo "✔️  CF_API_TOKEN"
    [ -z "$GEMINI_API_KEY" ] && echo "⚠️  GEMINI_API_KEY not set (optional)" || echo "✔️  GEMINI_API_KEY"
    [ -z "$ANTHROPIC_API_KEY" ] && echo "⚠️  ANTHROPIC_API_KEY not set (optional)" || echo "✔️  ANTHROPIC_API_KEY"
else
    echo "❌ .env file not found"
    ((ERRORS++))
fi

# Cloudflare authentication
echo ""
echo "☁️  Checking Cloudflare connection..."
if command -v wrangler >/dev/null 2>&1; then
    if wrangler whoami >/dev/null 2>&1; then
        echo "✔️  Authenticated with Cloudflare"
    else
        echo "⚠️  Not authenticated with Cloudflare (run: wrangler login)"
        ((WARNINGS++))
    fi
else
    echo "❌ wrangler CLI not found"
    ((ERRORS++))
fi

# Summary
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo "✨ SYSTEM HEALTHY — All checks passed!"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo "⚠️  SYSTEM OPERATIONAL — $WARNINGS warning(s)"
    exit 0
else
    echo "❌ SYSTEM UNHEALTHY — $ERRORS error(s), $WARNINGS warning(s)"
    exit 1
fi

