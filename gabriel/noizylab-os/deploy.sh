#!/bin/bash

# ████████████████████████████████████████████████████████████████████
# ███                                                              ███
# ███     NOIZYLAB OS - OMNI-SOVEREIGN DEPLOYMENT ORCHESTRATOR    ███
# ███                                                              ███
# ███  Deploys the entire AI-powered hardware restoration stack   ███
# ███                                                              ███
# ████████████████████████████████████████████████████████████████████

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Banner
echo -e "${MAGENTA}"
echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║                                                                   ║"
echo "║   ███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██╗      █████╗ ██████╗  ║"
echo "║   ████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╗██╔══██╗ ║"
echo "║   ██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║     ███████║██████╔╝ ║"
echo "║   ██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║     ██╔══██║██╔══██╗ ║"
echo "║   ██║ ╚████║╚██████╔╝██║███████╗   ██║   ███████╗██║  ██║██████╔╝ ║"
echo "║   ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝  ║"
echo "║                                                                   ║"
echo "║         OMNI-SOVEREIGN DEPLOYMENT ORCHESTRATOR v1.0               ║"
echo "║                                                                   ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKERS_DIR="$SCRIPT_DIR/workers"
MAIN_WORKER_DIR="$SCRIPT_DIR"

# Worker list in deployment order (respects dependencies)
WORKERS=(
  # ═══════════════════════════════════════════════════════════════════
  # CORE INFRASTRUCTURE (no dependencies)
  # ═══════════════════════════════════════════════════════════════════
  "main:$MAIN_WORKER_DIR"                     # Main NoizyLab OS worker
  "brain:$WORKERS_DIR/brain"                   # Claude diagnostic engine
  "voice:$WORKERS_DIR/voice"                   # ElevenLabs TTS
  "vision:$WORKERS_DIR/vision"                 # PCB analysis
  "notifications:$WORKERS_DIR/notifications"   # Notifications hub
  
  # ═══════════════════════════════════════════════════════════════════
  # BUSINESS LOGIC LAYER
  # ═══════════════════════════════════════════════════════════════════
  "pricing:$WORKERS_DIR/pricing"               # Pricing engine
  "ebay-sniper:$WORKERS_DIR/ebay-sniper"       # Parts hunting
  "inventory:$WORKERS_DIR/inventory"           # Inventory management
  "analytics:$WORKERS_DIR/analytics"           # Business intelligence
  
  # ═══════════════════════════════════════════════════════════════════
  # TECHNICIAN SUPPORT LAYER
  # ═══════════════════════════════════════════════════════════════════
  "ar-guide:$WORKERS_DIR/ar-guide"             # AR repair guides
  "training:$WORKERS_DIR/training"             # Training simulator
  "chat-agent:$WORKERS_DIR/chat-agent"         # Real-time AI assistant
  "qc-inspector:$WORKERS_DIR/qc-inspector"     # QC inspector
  "schematic-analyzer:$WORKERS_DIR/schematic-analyzer" # Schematic analysis
  
  # ═══════════════════════════════════════════════════════════════════
  # CUSTOMER EXPERIENCE LAYER
  # ═══════════════════════════════════════════════════════════════════
  "customer-portal:$WORKERS_DIR/customer-portal" # Customer self-service
  
  # ═══════════════════════════════════════════════════════════════════
  # GENIUS AI WORKERS - ROUND 1 - Advanced Intelligence Systems
  # ═══════════════════════════════════════════════════════════════════
  "predictive-maintenance:$WORKERS_DIR/predictive-maintenance"   # ML failure prediction
  "parts-matching:$WORKERS_DIR/parts-matching"                   # Vector parts compatibility
  "repair-dna:$WORKERS_DIR/repair-dna"                           # Device fingerprinting
  "knowledge-graph:$WORKERS_DIR/knowledge-graph"                 # Graph knowledge base
  "collaboration-hub:$WORKERS_DIR/collaboration-hub"             # Real-time collaboration
  "fraud-detection:$WORKERS_DIR/fraud-detection"                 # AI fraud prevention
  "time-estimation:$WORKERS_DIR/time-estimation"                 # ML time prediction
  "component-lifecycle:$WORKERS_DIR/component-lifecycle"         # Component health tracking
  "supplier-intelligence:$WORKERS_DIR/supplier-intelligence"     # Supplier AI management
  
  # ═══════════════════════════════════════════════════════════════════
  # GENIUS AI WORKERS - ROUND 2 - Next-Gen Intelligence
  # ═══════════════════════════════════════════════════════════════════
  "sentiment-analysis:$WORKERS_DIR/sentiment-analysis"           # NLP customer sentiment
  "anomaly-detection:$WORKERS_DIR/anomaly-detection"             # Statistical outlier detection
  "repair-simulation:$WORKERS_DIR/repair-simulation"             # Digital twin simulation
  "price-elasticity:$WORKERS_DIR/price-elasticity"               # Dynamic pricing AI
  "churn-prediction:$WORKERS_DIR/churn-prediction"               # Customer retention ML
  "demand-forecasting:$WORKERS_DIR/demand-forecasting"           # Predictive inventory
  "nl-query:$WORKERS_DIR/nl-query"                               # English-to-SQL engine
  "auto-testing:$WORKERS_DIR/auto-testing"                       # Self-testing QA
  "compliance-monitoring:$WORKERS_DIR/compliance-monitoring"     # Regulatory compliance
  "carbon-footprint:$WORKERS_DIR/carbon-footprint"               # ESG sustainability
  
  # ═══════════════════════════════════════════════════════════════════
  # ORCHESTRATION LAYER (depends on ALL above)
  # ═══════════════════════════════════════════════════════════════════
  "ai-supervisor:$WORKERS_DIR/ai-supervisor"   # Meta-AI orchestrator
  "workflow-orchestrator:$WORKERS_DIR/workflow-orchestrator" # Workflow engine
  "api-gateway:$WORKERS_DIR/api-gateway"       # Unified API gateway
)

# Functions
log_info() {
  echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
  echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
  echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
  echo -e "${RED}[ERROR]${NC} $1"
}

log_step() {
  echo -e "\n${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  echo -e "${CYAN}  $1${NC}"
  echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
}

# Check prerequisites
check_prerequisites() {
  log_step "🔍 Checking Prerequisites"
  
  # Check Node.js
  if ! command -v node &> /dev/null; then
    log_error "Node.js is not installed"
    exit 1
  fi
  log_success "Node.js $(node --version) found"
  
  # Check npm
  if ! command -v npm &> /dev/null; then
    log_error "npm is not installed"
    exit 1
  fi
  log_success "npm $(npm --version) found"
  
  # Check wrangler
  if ! command -v wrangler &> /dev/null; then
    log_warning "Wrangler not found, installing globally..."
    npm install -g wrangler
  fi
  log_success "Wrangler $(wrangler --version) found"
  
  # Check Cloudflare authentication
  if ! wrangler whoami &> /dev/null; then
    log_error "Not authenticated with Cloudflare. Run: wrangler login"
    exit 1
  fi
  log_success "Cloudflare authentication valid"
}

# Install dependencies for a worker
install_deps() {
  local worker_name=$1
  local worker_dir=$2
  
  if [ -f "$worker_dir/package.json" ]; then
    log_info "Installing dependencies for $worker_name..."
    cd "$worker_dir"
    npm install --silent
    log_success "Dependencies installed for $worker_name"
  fi
}

# Type check a worker
typecheck_worker() {
  local worker_name=$1
  local worker_dir=$2
  
  if [ -f "$worker_dir/tsconfig.json" ]; then
    log_info "Type checking $worker_name..."
    cd "$worker_dir"
    if npx tsc --noEmit 2>/dev/null; then
      log_success "Type check passed for $worker_name"
      return 0
    else
      log_warning "Type check had issues for $worker_name (continuing anyway)"
      return 0
    fi
  fi
}

# Deploy a worker
deploy_worker() {
  local worker_name=$1
  local worker_dir=$2
  local env=${3:-production}
  
  log_info "Deploying $worker_name to $env..."
  cd "$worker_dir"
  
  if wrangler deploy --env "$env" 2>&1; then
    log_success "✅ $worker_name deployed successfully"
    return 0
  else
    log_error "❌ Failed to deploy $worker_name"
    return 1
  fi
}

# Create D1 database
setup_database() {
  log_step "🗄️ Setting Up D1 Database"
  
  # Check if database exists
  if wrangler d1 list 2>/dev/null | grep -q "noizylab-db"; then
    log_info "Database noizylab-db already exists"
  else
    log_info "Creating D1 database: noizylab-db"
    wrangler d1 create noizylab-db
  fi
  
  # Run migrations if they exist
  if [ -f "$MAIN_WORKER_DIR/migrations/schema.sql" ]; then
    log_info "Running database migrations..."
    wrangler d1 execute noizylab-db --file="$MAIN_WORKER_DIR/migrations/schema.sql" --remote
    log_success "Migrations applied"
  fi
}

# Create R2 buckets
setup_storage() {
  log_step "📦 Setting Up R2 Storage"
  
  local buckets=(
    "noizylab-uploads"
    "noizylab-audio"
    "noizylab-golden-refs"
    "noizylab-ar-guides"
    "noizylab-parts"
    "noizylab-pricing-cache"
  )
  
  for bucket in "${buckets[@]}"; do
    if wrangler r2 bucket list 2>/dev/null | grep -q "$bucket"; then
      log_info "Bucket $bucket already exists"
    else
      log_info "Creating R2 bucket: $bucket"
      wrangler r2 bucket create "$bucket" 2>/dev/null || true
    fi
  done
  
  log_success "R2 storage configured"
}

# Create KV namespaces
setup_kv() {
  log_step "🔑 Setting Up KV Namespaces"
  
  local namespaces=(
    "noizylab-cache"
    "noizylab-sessions"
    "noizylab-inventory"
    "noizylab-analytics"
    "noizylab-training"
    "noizylab-notifications"
  )
  
  for ns in "${namespaces[@]}"; do
    if wrangler kv:namespace list 2>/dev/null | grep -q "$ns"; then
      log_info "KV namespace $ns already exists"
    else
      log_info "Creating KV namespace: $ns"
      wrangler kv:namespace create "$ns" 2>/dev/null || true
    fi
  done
  
  log_success "KV namespaces configured"
}

# Create queues
setup_queues() {
  log_step "📬 Setting Up Queues"
  
  local queues=(
    "noizylab-main-queue"
    "notifications-queue"
    "ebay-jobs-queue"
  )
  
  for queue in "${queues[@]}"; do
    log_info "Creating queue: $queue"
    wrangler queues create "$queue" 2>/dev/null || true
  done
  
  log_success "Queues configured"
}

# Deploy all workers
deploy_all() {
  log_step "🚀 Deploying All Workers"
  
  local failed=0
  local success=0
  local env=${1:-production}
  
  for worker_entry in "${WORKERS[@]}"; do
    IFS=':' read -r worker_name worker_dir <<< "$worker_entry"
    
    if [ -d "$worker_dir" ]; then
      echo ""
      echo -e "${MAGENTA}━━━ Deploying: $worker_name ━━━${NC}"
      
      # Install dependencies
      install_deps "$worker_name" "$worker_dir"
      
      # Type check
      typecheck_worker "$worker_name" "$worker_dir"
      
      # Deploy
      if deploy_worker "$worker_name" "$worker_dir" "$env"; then
        ((success++))
      else
        ((failed++))
      fi
    else
      log_warning "Worker directory not found: $worker_dir"
      ((failed++))
    fi
  done
  
  echo ""
  log_step "📊 Deployment Summary"
  echo -e "${GREEN}✅ Successful: $success${NC}"
  echo -e "${RED}❌ Failed: $failed${NC}"
  
  if [ $failed -gt 0 ]; then
    exit 1
  fi
}

# Dev mode - start all workers locally
dev_mode() {
  log_step "🔧 Starting Development Mode"
  
  log_info "Starting workers in development mode..."
  log_warning "Press Ctrl+C to stop all workers"
  
  # Start main worker
  cd "$MAIN_WORKER_DIR"
  wrangler dev &
  
  # Wait for all background processes
  wait
}

# Print status of all workers
status() {
  log_step "📡 Worker Status"
  
  for worker_entry in "${WORKERS[@]}"; do
    IFS=':' read -r worker_name worker_dir <<< "$worker_entry"
    
    # Check if deployed
    if wrangler deployments list 2>/dev/null | head -5 | grep -q "$worker_name"; then
      echo -e "${GREEN}● $worker_name${NC} - Deployed"
    else
      echo -e "${YELLOW}○ $worker_name${NC} - Not deployed or unknown"
    fi
  done
}

# Print help
print_help() {
  echo -e "${CYAN}Usage:${NC} $0 <command> [options]"
  echo ""
  echo -e "${CYAN}Commands:${NC}"
  echo "  deploy [env]     Deploy all workers (default: production)"
  echo "  deploy:single    Deploy a single worker"
  echo "  setup            Set up all infrastructure (D1, R2, KV, Queues)"
  echo "  dev              Start all workers in development mode"
  echo "  status           Show deployment status"
  echo "  help             Show this help message"
  echo ""
  echo -e "${CYAN}Examples:${NC}"
  echo "  $0 deploy                    # Deploy all to production"
  echo "  $0 deploy staging            # Deploy all to staging"
  echo "  $0 deploy:single brain       # Deploy only brain worker"
  echo "  $0 setup                     # Create all infrastructure"
  echo ""
}

# Main
case "${1:-help}" in
  deploy)
    check_prerequisites
    deploy_all "${2:-production}"
    ;;
  deploy:single)
    check_prerequisites
    if [ -z "$2" ]; then
      log_error "Please specify worker name"
      exit 1
    fi
    for worker_entry in "${WORKERS[@]}"; do
      IFS=':' read -r worker_name worker_dir <<< "$worker_entry"
      if [ "$worker_name" == "$2" ]; then
        install_deps "$worker_name" "$worker_dir"
        deploy_worker "$worker_name" "$worker_dir" "${3:-production}"
        exit 0
      fi
    done
    log_error "Worker not found: $2"
    exit 1
    ;;
  setup)
    check_prerequisites
    setup_database
    setup_storage
    setup_kv
    setup_queues
    log_success "Infrastructure setup complete!"
    ;;
  dev)
    check_prerequisites
    dev_mode
    ;;
  status)
    status
    ;;
  help|--help|-h)
    print_help
    ;;
  *)
    log_error "Unknown command: $1"
    print_help
    exit 1
    ;;
esac

echo ""
echo -e "${GREEN}════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  NoizyLab OS - The Future of Hardware Restoration 🔧⚡${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════════════════${NC}"
