#!/bin/bash
#
# GABRIEL Production Deployment Script
#
# This script handles the complete deployment pipeline:
# 1. Run tests
# 2. Build frontend
# 3. Deploy API to Cloudflare Workers
# 4. Deploy frontend to Cloudflare Pages
# 5. Run smoke tests
# 6. Send notifications
#
# Usage: ./deploy.sh [environment]
#   environment: staging | production (default: staging)

set -e

# Configuration
ENVIRONMENT=${1:-staging}
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
API_DIR="$PROJECT_ROOT/portal/api"
FRONTEND_DIR="$PROJECT_ROOT/portal/frontend"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="$PROJECT_ROOT/deploy_${ENVIRONMENT}_${TIMESTAMP}.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
  local level=$1
  local message=$2
  local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
  
  case $level in
    INFO)  echo -e "${BLUE}[INFO]${NC} $message" | tee -a "$LOG_FILE" ;;
    WARN)  echo -e "${YELLOW}[WARN]${NC} $message" | tee -a "$LOG_FILE" ;;
    ERROR) echo -e "${RED}[ERROR]${NC} $message" | tee -a "$LOG_FILE" ;;
    SUCCESS) echo -e "${GREEN}[SUCCESS]${NC} $message" | tee -a "$LOG_FILE" ;;
  esac
}

# Error handler
handle_error() {
  log ERROR "Deployment failed at step: $1"
  send_notification "❌ GABRIEL deployment to $ENVIRONMENT failed at: $1"
  exit 1
}

# Send notification (Slack/Discord)
send_notification() {
  local message=$1
  
  if [ -n "$SLACK_WEBHOOK_URL" ]; then
    curl -s -X POST -H 'Content-type: application/json' \
      --data "{\"text\":\"$message\"}" \
      "$SLACK_WEBHOOK_URL" > /dev/null
  fi
  
  if [ -n "$DISCORD_WEBHOOK_URL" ]; then
    curl -s -X POST -H 'Content-type: application/json' \
      --data "{\"content\":\"$message\"}" \
      "$DISCORD_WEBHOOK_URL" > /dev/null
  fi
}

# Check prerequisites
check_prerequisites() {
  log INFO "Checking prerequisites..."
  
  # Check Node.js
  if ! command -v node &> /dev/null; then
    handle_error "Node.js not found"
  fi
  
  # Check npm
  if ! command -v npm &> /dev/null; then
    handle_error "npm not found"
  fi
  
  # Check wrangler
  if ! command -v wrangler &> /dev/null; then
    log INFO "Installing wrangler..."
    npm install -g wrangler
  fi
  
  # Check environment variables
  if [ "$ENVIRONMENT" == "production" ]; then
    if [ -z "$CLOUDFLARE_API_TOKEN" ]; then
      handle_error "CLOUDFLARE_API_TOKEN not set"
    fi
    
    if [ -z "$STRIPE_SECRET_KEY" ]; then
      handle_error "STRIPE_SECRET_KEY not set"
    fi
  fi
  
  log SUCCESS "Prerequisites check passed"
}

# Run tests
run_tests() {
  log INFO "Running tests..."
  
  cd "$PROJECT_ROOT"
  
  # Run unit tests
  log INFO "Running unit tests..."
  npm test -- --passWithNoTests || handle_error "Unit tests"
  
  # Run E2E tests (only in staging)
  if [ "$ENVIRONMENT" == "staging" ]; then
    log INFO "Running E2E tests..."
    npm run test:e2e -- --reporter=list || handle_error "E2E tests"
  fi
  
  log SUCCESS "All tests passed"
}

# Build frontend
build_frontend() {
  log INFO "Building frontend..."
  
  cd "$FRONTEND_DIR"
  
  # Install dependencies
  npm ci
  
  # Set environment variables
  if [ "$ENVIRONMENT" == "production" ]; then
    export VITE_API_URL="https://api.gabriel.noizylab.com"
    export VITE_STRIPE_PUBLIC_KEY="$STRIPE_PUBLIC_KEY"
  else
    export VITE_API_URL="https://api-staging.gabriel.noizylab.com"
    export VITE_STRIPE_PUBLIC_KEY="$STRIPE_PUBLIC_KEY_TEST"
  fi
  
  # Build
  npm run build || handle_error "Frontend build"
  
  # Verify build output
  if [ ! -d "dist" ]; then
    handle_error "Frontend build output not found"
  fi
  
  log SUCCESS "Frontend built successfully"
}

# Deploy API to Cloudflare Workers
deploy_api() {
  log INFO "Deploying API to Cloudflare Workers..."
  
  cd "$API_DIR"
  
  # Install dependencies
  npm ci
  
  # Deploy with wrangler
  if [ "$ENVIRONMENT" == "production" ]; then
    wrangler deploy --env production || handle_error "API deployment"
  else
    wrangler deploy --env staging || handle_error "API deployment"
  fi
  
  log SUCCESS "API deployed successfully"
}

# Deploy frontend to Cloudflare Pages
deploy_frontend() {
  log INFO "Deploying frontend to Cloudflare Pages..."
  
  cd "$FRONTEND_DIR"
  
  if [ "$ENVIRONMENT" == "production" ]; then
    wrangler pages deploy dist --project-name=gabriel-portal --branch=main || handle_error "Frontend deployment"
  else
    wrangler pages deploy dist --project-name=gabriel-portal --branch=staging || handle_error "Frontend deployment"
  fi
  
  log SUCCESS "Frontend deployed successfully"
}

# Run smoke tests
run_smoke_tests() {
  log INFO "Running smoke tests..."
  
  local api_url
  local frontend_url
  
  if [ "$ENVIRONMENT" == "production" ]; then
    api_url="https://api.gabriel.noizylab.com"
    frontend_url="https://gabriel.noizylab.com"
  else
    api_url="https://api-staging.gabriel.noizylab.com"
    frontend_url="https://staging.gabriel.noizylab.com"
  fi
  
  # Test API health
  log INFO "Testing API health endpoint..."
  local api_response=$(curl -s -o /dev/null -w "%{http_code}" "$api_url/api/health")
  if [ "$api_response" != "200" ]; then
    handle_error "API health check (got $api_response)"
  fi
  
  # Test frontend
  log INFO "Testing frontend..."
  local frontend_response=$(curl -s -o /dev/null -w "%{http_code}" "$frontend_url")
  if [ "$frontend_response" != "200" ]; then
    handle_error "Frontend health check (got $frontend_response)"
  fi
  
  # Test scan endpoint (expect 401 without auth)
  log INFO "Testing scan endpoint auth..."
  local scan_response=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$api_url/api/scan")
  if [ "$scan_response" != "401" ]; then
    log WARN "Scan endpoint returned unexpected status: $scan_response"
  fi
  
  log SUCCESS "Smoke tests passed"
}

# Create deployment record
create_deployment_record() {
  log INFO "Creating deployment record..."
  
  local git_commit=$(git rev-parse HEAD)
  local git_branch=$(git rev-parse --abbrev-ref HEAD)
  local deployer=${GITHUB_ACTOR:-$(whoami)}
  
  cat > "$PROJECT_ROOT/deployments/${ENVIRONMENT}_${TIMESTAMP}.json" << EOF
{
  "environment": "$ENVIRONMENT",
  "timestamp": "$TIMESTAMP",
  "commit": "$git_commit",
  "branch": "$git_branch",
  "deployer": "$deployer",
  "status": "success"
}
EOF
  
  log SUCCESS "Deployment record created"
}

# Main deployment pipeline
main() {
  echo ""
  echo "╔═══════════════════════════════════════════════════════════════╗"
  echo "║              GABRIEL DEPLOYMENT PIPELINE                      ║"
  echo "║                                                               ║"
  echo "║  Environment: $ENVIRONMENT                                         ║"
  echo "║  Timestamp: $TIMESTAMP                                  ║"
  echo "╚═══════════════════════════════════════════════════════════════╝"
  echo ""
  
  log INFO "Starting deployment to $ENVIRONMENT..."
  send_notification "🚀 Starting GABRIEL deployment to $ENVIRONMENT"
  
  # Create deployments directory if it doesn't exist
  mkdir -p "$PROJECT_ROOT/deployments"
  
  # Run deployment steps
  check_prerequisites
  
  if [ "$SKIP_TESTS" != "true" ]; then
    run_tests
  else
    log WARN "Skipping tests (SKIP_TESTS=true)"
  fi
  
  build_frontend
  deploy_api
  deploy_frontend
  run_smoke_tests
  create_deployment_record
  
  echo ""
  echo "╔═══════════════════════════════════════════════════════════════╗"
  echo "║              DEPLOYMENT COMPLETE! ✅                          ║"
  echo "╚═══════════════════════════════════════════════════════════════╝"
  echo ""
  
  if [ "$ENVIRONMENT" == "production" ]; then
    log SUCCESS "Production deployment complete!"
    log INFO "Frontend: https://gabriel.noizylab.com"
    log INFO "API: https://api.gabriel.noizylab.com"
    send_notification "✅ GABRIEL deployed to production successfully!"
  else
    log SUCCESS "Staging deployment complete!"
    log INFO "Frontend: https://staging.gabriel.noizylab.com"
    log INFO "API: https://api-staging.gabriel.noizylab.com"
    send_notification "✅ GABRIEL deployed to staging successfully!"
  fi
}

# Run main function
main
