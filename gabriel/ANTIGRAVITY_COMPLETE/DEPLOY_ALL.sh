#!/usr/bin/env bash
#═══════════════════════════════════════════════════════════════════════════════
# ANTIGRAVITY COMPLETE - DEPLOY ALL WORKERS
# MC96ECOUNIVERSE Command Hub + Circle of 8 + Full Network
#═══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"

echo "═══════════════════════════════════════════════════════════════"
echo "  ⚡ ANTIGRAVITY COMPLETE - FULL DEPLOYMENT ⚡"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Deploying 4 workers to Cloudflare:"
echo "  • antigravity     - Command Hub + Circle of 8"
echo "  • gorunfree       - Voice Command Processor"  
echo "  • noizylab        - Repair Service System"
echo "  • mc96-network    - Network Orchestrator"
echo ""

# Check wrangler
if ! command -v wrangler &>/dev/null; then
  echo "ERROR: wrangler not found. Install with: npm i -g wrangler"
  exit 1
fi

# Deploy each worker
deploy_worker() {
  local name="$1"
  local dir="${ROOT}/${name}"
  
  if [[ ! -d "$dir" ]]; then
    echo "⚠️  Skipping $name (directory not found)"
    return 0
  fi
  
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Deploying: $name"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  
  cd "$dir"
  
  # Install deps if package.json exists
  if [[ -f package.json ]]; then
    npm install --silent 2>/dev/null || true
  fi
  
  # Deploy
  if wrangler deploy 2>&1; then
    echo "✅ $name deployed"
  else
    echo "❌ $name failed"
    return 1
  fi
  
  cd "$ROOT"
  echo ""
}

# Deploy all workers
deploy_worker "antigravity"
deploy_worker "gorunfree"
deploy_worker "noizylab"
deploy_worker "mc96-network"

echo "═══════════════════════════════════════════════════════════════"
echo "  ✅ DEPLOYMENT COMPLETE"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Workers deployed:"
echo "  https://antigravity.rsplowman.workers.dev"
echo "  https://gorunfree.rsplowman.workers.dev"
echo "  https://noizylab.rsplowman.workers.dev"
echo "  https://mc96-network.rsplowman.workers.dev"
echo ""
echo "📌 NEXT: Set secrets:"
echo "  cd antigravity && wrangler secret put ANTHROPIC_API_KEY"
echo ""
echo "🔮 CIRCLE OF 8 ACTIVATED"
