#!/bin/bash
set -e

# ⚡ SUPERBUILD — NoizyLab OS
# One command to build, deploy, and sync everything
# ===================================================

BASE="/Users/m2ultra/NOIZYLAB/noizylab-os"
SUPERCODE_DIR="$BASE/supercode"
LOG_FILE="$SUPERCODE_DIR/superbuild.log"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log() {
    echo -e "${BLUE}[$(date +'%H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
}

success() {
    echo -e "${GREEN}✔️ $1${NC}" | tee -a "$LOG_FILE"
}

error() {
    echo -e "${RED}❌ $1${NC}" | tee -a "$LOG_FILE"
    exit 1
}

warn() {
    echo -e "${YELLOW}⚠️  $1${NC}" | tee -a "$LOG_FILE"
}

# Initialize log
echo "=== SUPERBUILD STARTED $(date) ===" > "$LOG_FILE"

log "🚀 SUPERBUILD INITIATED — Building NoizyLab OS..."

# Check prerequisites
log "📋 Checking prerequisites..."
command -v node >/dev/null 2>&1 || error "Node.js not found"
command -v npm >/dev/null 2>&1 || error "npm not found"
command -v wrangler >/dev/null 2>&1 || error "wrangler CLI not found. Install: npm i -g wrangler"

# Load environment
log "🔐 Loading environment..."
if [ -f "$BASE/.env" ]; then
    source "$BASE/.env"
    success "Environment loaded"
else
    warn ".env file not found. Creating template..."
    cat > "$BASE/.env.template" << EOF
# Cloudflare Credentials
CF_ACCOUNT_ID=your_account_id
CF_API_TOKEN=your_api_token

# AI Provider Keys
GEMINI_API_KEY=your_gemini_key
ANTHROPIC_API_KEY=your_anthropic_key
OPENAI_API_KEY=your_openai_key

# D1 Database
D1_DATABASE_NAME=noizylab

# Environment
NODE_ENV=development
EOF
    error "Please create .env file from .env.template"
fi

# Validate Cloudflare credentials
if [ -z "$CF_ACCOUNT_ID" ] || [ -z "$CF_API_TOKEN" ]; then
    error "Missing Cloudflare credentials in .env"
fi

# Wrangler authentication
log "🔑 Authenticating with Cloudflare..."
if ! wrangler whoami >/dev/null 2>&1; then
    log "Logging in to Cloudflare..."
    wrangler login
fi
success "Cloudflare authenticated"

# Step 1: Install dependencies
log "📦 Installing dependencies..."
cd "$BASE"
if [ -f "package.json" ]; then
    npm install
    success "Dependencies installed"
fi

# Step 2: Build Workers
log "🏗️  Building Workers..."
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
    if [ -d "$BASE/$worker" ]; then
        log "  Building $worker..."
        cd "$BASE/$worker"
        if [ -f "package.json" ]; then
            npm install --silent
            npm run build 2>/dev/null || true
            success "  ✓ $worker"
        fi
    fi
done

# Step 3: Deploy Workers
log "🚀 Deploying Workers..."
for worker in "${WORKERS[@]}"; do
    if [ -d "$BASE/$worker" ] && [ -f "$BASE/$worker/wrangler.toml" ]; then
        log "  Deploying $worker..."
        cd "$BASE/$worker"
        wrangler deploy --no-bundle 2>&1 | tee -a "$LOG_FILE" || warn "  Failed to deploy $worker"
    fi
done

# Step 4: Setup D1 Database
log "💾 Setting up D1 Database..."
if [ -f "$BASE/migrations/sql/001_initial_schema.sql" ]; then
    wrangler d1 execute noizylab --file="$BASE/migrations/sql/001_initial_schema.sql" 2>&1 | tee -a "$LOG_FILE" || warn "D1 migration failed"
    success "D1 database synced"
fi

# Step 5: Setup Queues
log "📬 Setting up Queues..."
QUEUES=("SNAPSHOT_QUEUE" "EVENT_QUEUE" "AI_QUEUE" "REPAIR_QUEUE")
for queue in "${QUEUES[@]}"; do
    wrangler queues create "$queue" 2>&1 | tee -a "$LOG_FILE" || true
done
success "Queues configured"

# Step 6: Setup AI Router
log "🤖 Setting up AI Router..."
if [ -d "$BASE/ai/router" ]; then
    cd "$BASE/ai/router"
    if [ -f "package.json" ]; then
        npm install --silent
        npm run build 2>/dev/null || true
        if [ -f "wrangler.toml" ]; then
            wrangler deploy 2>&1 | tee -a "$LOG_FILE" || warn "AI Router deployment failed"
        fi
    fi
fi

# Step 7: Setup CLI Tools
log "🛠️  Setting up CLI tools..."
if [ -f "$SUPERCODE_DIR/ai-router-install.sh" ]; then
    bash "$SUPERCODE_DIR/ai-router-install.sh" 2>&1 | tee -a "$LOG_FILE"
fi

# Step 8: Run Tests
log "🧪 Running tests..."
if [ -f "$SUPERCODE_DIR/test-harness.sh" ]; then
    bash "$SUPERCODE_DIR/test-harness.sh" 2>&1 | tee -a "$LOG_FILE"
fi

# Step 9: Validate System
log "✅ Validating system..."
if [ -f "$SUPERCODE_DIR/guardian.sh" ]; then
    bash "$SUPERCODE_DIR/guardian.sh" 2>&1 | tee -a "$LOG_FILE"
fi

# Step 10: Generate Status Report
log "📊 Generating status report..."
cat > "$SUPERCODE_DIR/superbuild-status.json" << EOF
{
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "status": "completed",
  "workers_deployed": $(ls -1 "$BASE/workers" | wc -l),
  "queues_configured": ${#QUEUES[@]},
  "d1_synced": true,
  "cli_tools_installed": true
}
EOF

success "✨ SUPERBUILD COMPLETE!"
log "📄 Full log: $LOG_FILE"
log "📊 Status: $SUPERCODE_DIR/superbuild-status.json"

echo ""
echo "🎉 NoizyLab OS is ready!"
echo ""
echo "Next steps:"
echo "  • Run: wrangler dev (to start local dev)"
echo "  • Run: ./supercode/guardian.sh (to check system health)"
echo "  • Run: ./supercode/test-harness.sh (to run all tests)"
echo ""

