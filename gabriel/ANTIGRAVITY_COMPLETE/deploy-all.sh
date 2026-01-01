#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# 🔥 MC96ECOUNIVERSE MASTER DEPLOYMENT - GORUNFREE
# Deploy ALL workers to Cloudflare Edge in one command
# ═══════════════════════════════════════════════════════════════════════════════

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# ASCII Art Banner
echo -e "${PURPLE}"
cat << 'EOF'
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   ███╗   ███╗ ██████╗ █████╗  ██████╗ ███████╗ ██████╗██╗   ██╗              ║
║   ████╗ ████║██╔════╝██╔══██╗██╔════╝ ██╔════╝██╔════╝██║   ██║              ║
║   ██╔████╔██║██║     ╚██████║███████╗ █████╗  ██║     ██║   ██║              ║
║   ██║╚██╔╝██║██║      ╚═══██║██╔═══██╗██╔══╝  ██║     ██║   ██║              ║
║   ██║ ╚═╝ ██║╚██████╗ █████╔╝╚██████╔╝███████╗╚██████╗╚██████╔╝              ║
║   ╚═╝     ╚═╝ ╚═════╝ ╚════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝               ║
║                                                                               ║
║   ╔════════════════════════════════════════════════════════════════════════╗  ║
║   ║  🔥 MASTER DEPLOYMENT - GORUNFREE 🔥                                   ║  ║
║   ║  Deploy ALL Workers to Cloudflare Edge                                  ║  ║
║   ╚════════════════════════════════════════════════════════════════════════╝  ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKERS_DIR="${SCRIPT_DIR}"

# Worker definitions
declare -A WORKERS=(
  ["command-center"]="Unified Dashboard & Gateway"
  ["antigravity"]="Command Hub + Circle of 8"
  ["gorunfree"]="Voice Command Processor"
  ["noizylab"]="Main AI Gateway"
  ["mc96-network"]="Multi-Model Network"
  ["media-vault"]="Cloud Storage Gateway"
  ["task-commander"]="Automation Hub + Cron"
  ["neural-gateway"]="AI Model Router"
  ["sonic-engine"]="Audio Processing Hub"
  ["dazeflow"]="Truth Capture System"
)

# Status tracking
DEPLOYED=0
FAILED=0
SKIPPED=0

# Functions
log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

check_wrangler() {
  if ! command -v wrangler &> /dev/null; then
    log_error "wrangler CLI not found. Install with: npm install -g wrangler"
    exit 1
  fi
  log_info "wrangler version: $(wrangler --version)"
}

deploy_worker() {
  local worker=$1
  local description=$2
  local worker_path="${WORKERS_DIR}/${worker}"
  
  echo ""
  echo -e "${CYAN}═══════════════════════════════════════════════════════════════════════════════${NC}"
  echo -e "${BOLD}Deploying: ${worker}${NC} - ${description}"
  echo -e "${CYAN}═══════════════════════════════════════════════════════════════════════════════${NC}"
  
  if [ ! -d "$worker_path" ]; then
    log_warning "Worker directory not found: ${worker_path}"
    ((SKIPPED++))
    return
  fi
  
  if [ ! -f "${worker_path}/wrangler.toml" ]; then
    log_warning "wrangler.toml not found in ${worker_path}"
    ((SKIPPED++))
    return
  fi
  
  cd "$worker_path"
  
  # Install dependencies if package.json exists
  if [ -f "package.json" ]; then
    log_info "Installing dependencies..."
    npm install --silent 2>/dev/null || true
  fi
  
  # Deploy
  log_info "Deploying to Cloudflare..."
  if wrangler deploy 2>&1; then
    log_success "${worker} deployed successfully!"
    ((DEPLOYED++))
  else
    log_error "Failed to deploy ${worker}"
    ((FAILED++))
  fi
  
  cd "$WORKERS_DIR"
}

deploy_main_worker() {
  echo ""
  echo -e "${CYAN}═══════════════════════════════════════════════════════════════════════════════${NC}"
  echo -e "${BOLD}Deploying: MAIN WORKER${NC} - NOIZYLAB HOTROD v5.0"
  echo -e "${CYAN}═══════════════════════════════════════════════════════════════════════════════${NC}"
  
  local main_worker="${SCRIPT_DIR}/../workers/noizylab-main"
  
  if [ -d "$main_worker" ]; then
    cd "$main_worker"
    if wrangler deploy 2>&1; then
      log_success "MAIN WORKER deployed successfully!"
      ((DEPLOYED++))
    else
      log_error "Failed to deploy MAIN WORKER"
      ((FAILED++))
    fi
    cd "$WORKERS_DIR"
  else
    log_warning "Main worker directory not found"
    ((SKIPPED++))
  fi
}

print_summary() {
  echo ""
  echo -e "${PURPLE}═══════════════════════════════════════════════════════════════════════════════${NC}"
  echo -e "${BOLD}                        DEPLOYMENT SUMMARY                                      ${NC}"
  echo -e "${PURPLE}═══════════════════════════════════════════════════════════════════════════════${NC}"
  echo ""
  echo -e "  ${GREEN}✓ Deployed:${NC}  ${DEPLOYED}"
  echo -e "  ${RED}✗ Failed:${NC}    ${FAILED}"
  echo -e "  ${YELLOW}○ Skipped:${NC}   ${SKIPPED}"
  echo ""
  
  if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}╔═══════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                    🔥 ALL DEPLOYMENTS SUCCESSFUL! 🔥                          ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════════════════════════════════════╝${NC}"
  else
    echo -e "${RED}╔═══════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║                    ⚠️  SOME DEPLOYMENTS FAILED ⚠️                              ║${NC}"
    echo -e "${RED}╚═══════════════════════════════════════════════════════════════════════════════╝${NC}"
  fi
  
  echo ""
  echo -e "${CYAN}Live Workers:${NC}"
  echo "  • https://noizylab.rsplowman.workers.dev (Main)"
  echo "  • https://antigravity.rsplowman.workers.dev"
  echo "  • https://gorunfree.rsplowman.workers.dev"
  echo "  • https://mc96-network.rsplowman.workers.dev"
  echo "  • https://media-vault.rsplowman.workers.dev"
  echo ""
  echo -e "${PURPLE}GORUNFREE • MC96ECOUNIVERSE • Happy New Year 2026!${NC}"
}

# Main execution
main() {
  echo -e "${BOLD}Starting MC96ECOUNIVERSE Master Deployment...${NC}"
  echo ""
  
  check_wrangler
  
  # Parse arguments
  case "$1" in
    --main-only)
      deploy_main_worker
      ;;
    --antigravity-only)
      deploy_worker "antigravity" "${WORKERS[antigravity]}"
      ;;
    --all|"")
      # Deploy all ANTIGRAVITY workers
      for worker in "${!WORKERS[@]}"; do
        deploy_worker "$worker" "${WORKERS[$worker]}"
      done
      # Deploy main worker
      deploy_main_worker
      ;;
    --help|-h)
      echo "Usage: $0 [OPTIONS]"
      echo ""
      echo "Options:"
      echo "  --all              Deploy all workers (default)"
      echo "  --main-only        Deploy only the main worker"
      echo "  --antigravity-only Deploy only ANTIGRAVITY workers"
      echo "  --help, -h         Show this help"
      exit 0
      ;;
    *)
      log_error "Unknown option: $1"
      echo "Use --help for usage information"
      exit 1
      ;;
  esac
  
  print_summary
}

main "$@"
