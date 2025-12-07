#!/bin/bash
# 🔥 HOT ROD FLOW DEPLOYMENT SCRIPT
# Deploys the complete Hot Rod Flow integration system

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${MAGENTA}"
echo "🔥🔥🔥 DEPLOYING HOT ROD FLOW 🔥🔥🔥"
echo "=================================="
echo -e "${NC}"
echo ""
echo -e "${CYAN}Central Hub: ${GREEN}rsplowman@outlook.com${NC}"
echo -e "${CYAN}Systems: ${GREEN}7 connected${NC}"
echo -e "${CYAN}Velocity: ${GREEN}MAXIMUM${NC}"
echo ""

# Check if we're in the right directory
if [ ! -f "HOT_ROD_FLOW.md" ]; then
    echo -e "${RED}Error: HOT_ROD_FLOW.md not found. Please run from repository root.${NC}"
    exit 1
fi

# Check if cloudflare directory exists
if [ ! -d "cloudflare" ]; then
    echo -e "${RED}Error: cloudflare directory not found.${NC}"
    exit 1
fi

cd cloudflare

echo -e "${BLUE}📋 Pre-Deployment Checklist${NC}"
echo "=============================="
echo ""

# Check if wrangler is installed
if ! command -v wrangler &> /dev/null; then
    echo -e "${YELLOW}⚠️  Wrangler not found. Installing...${NC}"
    npm install -g wrangler
else
    echo -e "${GREEN}✓${NC} Wrangler installed"
fi

# Check if logged in to Cloudflare
echo ""
echo -e "${BLUE}🔐 Checking Cloudflare authentication...${NC}"
if ! wrangler whoami &> /dev/null; then
    echo -e "${YELLOW}⚠️  Not logged in to Cloudflare. Please login:${NC}"
    wrangler login
else
    echo -e "${GREEN}✓${NC} Authenticated with Cloudflare"
fi

echo ""
echo -e "${BLUE}📦 Setting up Cloudflare Resources${NC}"
echo "===================================="
echo ""

# Create D1 Database
echo -e "${CYAN}Creating D1 Database...${NC}"
DB_OUTPUT=$(wrangler d1 create noizylab-hotrod 2>&1 || echo "EXISTS")
if echo "$DB_OUTPUT" | grep -q "database_id"; then
    DB_ID=$(echo "$DB_OUTPUT" | grep "database_id" | cut -d'"' -f4)
    echo -e "${GREEN}✓${NC} D1 Database created: $DB_ID"
    
    # Update wrangler.toml with database ID
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s/your-database-id/$DB_ID/" wrangler-hotrod.toml
    else
        sed -i "s/your-database-id/$DB_ID/" wrangler-hotrod.toml
    fi
else
    echo -e "${YELLOW}⚠️  Database might already exist${NC}"
fi

# Create database schema
echo ""
echo -e "${CYAN}Creating database schema...${NC}"
wrangler d1 execute noizylab-hotrod --command "
CREATE TABLE IF NOT EXISTS repairs (
  id TEXT PRIMARY KEY,
  customer_email TEXT,
  device TEXT,
  issue TEXT,
  status TEXT,
  created_at TEXT,
  updated_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_repairs_status ON repairs(status);
CREATE INDEX IF NOT EXISTS idx_repairs_created ON repairs(created_at);
" 2>&1 || echo -e "${YELLOW}⚠️  Schema might already exist${NC}"

echo -e "${GREEN}✓${NC} Database schema ready"

# Create KV Namespaces
echo ""
echo -e "${CYAN}Creating KV Namespaces...${NC}"

# Email Queue KV
EMAIL_QUEUE_OUTPUT=$(wrangler kv:namespace create EMAIL_QUEUE 2>&1 || echo "EXISTS")
if echo "$EMAIL_QUEUE_OUTPUT" | grep -q "id"; then
    EMAIL_QUEUE_ID=$(echo "$EMAIL_QUEUE_OUTPUT" | grep "id" | cut -d'"' -f4 | head -1)
    echo -e "${GREEN}✓${NC} EMAIL_QUEUE KV created: $EMAIL_QUEUE_ID"
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "0,/your-email-queue-kv-id/s//$EMAIL_QUEUE_ID/" wrangler-hotrod.toml
    else
        sed -i "0,/your-email-queue-kv-id/s//$EMAIL_QUEUE_ID/" wrangler-hotrod.toml
    fi
fi

# Analytics KV
ANALYTICS_OUTPUT=$(wrangler kv:namespace create ANALYTICS 2>&1 || echo "EXISTS")
if echo "$ANALYTICS_OUTPUT" | grep -q "id"; then
    ANALYTICS_ID=$(echo "$ANALYTICS_OUTPUT" | grep "id" | cut -d'"' -f4 | head -1)
    echo -e "${GREEN}✓${NC} ANALYTICS KV created: $ANALYTICS_ID"
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "0,/your-analytics-kv-id/s//$ANALYTICS_ID/" wrangler-hotrod.toml
    else
        sed -i "0,/your-analytics-kv-id/s//$ANALYTICS_ID/" wrangler-hotrod.toml
    fi
fi

# Notifications KV
NOTIFICATIONS_OUTPUT=$(wrangler kv:namespace create NOTIFICATIONS 2>&1 || echo "EXISTS")
if echo "$NOTIFICATIONS_OUTPUT" | grep -q "id"; then
    NOTIFICATIONS_ID=$(echo "$NOTIFICATIONS_OUTPUT" | grep "id" | cut -d'"' -f4 | head -1)
    echo -e "${GREEN}✓${NC} NOTIFICATIONS KV created: $NOTIFICATIONS_ID"
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "0,/your-notifications-kv-id/s//$NOTIFICATIONS_ID/" wrangler-hotrod.toml
    else
        sed -i "0,/your-notifications-kv-id/s//$NOTIFICATIONS_ID/" wrangler-hotrod.toml
    fi
fi

echo ""
echo -e "${BLUE}🚀 Deploying Hot Rod Flow Worker${NC}"
echo "=================================="
echo ""

# Deploy the worker
wrangler deploy --config wrangler-hotrod.toml

echo ""
echo -e "${GREEN}✅ HOT ROD FLOW DEPLOYED!${NC}"
echo ""

# Get the worker URL
WORKER_URL=$(wrangler deployments list --config wrangler-hotrod.toml 2>&1 | grep -o 'https://[^ ]*' | head -1 || echo "noizylab-hotrod-flow.workers.dev")

echo -e "${BLUE}🔗 Endpoints:${NC}"
echo "   ${WORKER_URL}/health"
echo "   ${WORKER_URL}/api/flow/hub/status"
echo "   ${WORKER_URL}/api/flow/repair/new"
echo "   ${WORKER_URL}/api/flow/repair/status"
echo "   ${WORKER_URL}/api/flow/email/send"
echo "   ${WORKER_URL}/api/flow/analytics/event"
echo "   ${WORKER_URL}/api/flow/sync/all"
echo ""

# Test health endpoint
echo -e "${BLUE}🏥 Testing Health Endpoint${NC}"
echo "=========================="
echo ""

sleep 2  # Give worker time to start

if command -v curl &> /dev/null; then
    echo -e "${CYAN}Testing: ${WORKER_URL}/health${NC}"
    curl -s "${WORKER_URL}/health" | jq '.' 2>/dev/null || curl -s "${WORKER_URL}/health"
    echo ""
else
    echo -e "${YELLOW}⚠️  curl not found, skipping health check${NC}"
fi

echo ""
echo -e "${MAGENTA}🔥 ALL SYSTEMS GO! 🔥${NC}"
echo ""
echo -e "${CYAN}Central Hub: ${GREEN}rsplowman@outlook.com${NC}"
echo -e "${CYAN}Status: ${GREEN}ACTIVE${NC}"
echo -e "${CYAN}Velocity: ${GREEN}MAXIMUM 🏎️${NC}"
echo ""
echo -e "${BLUE}📚 Documentation:${NC}"
echo "   ../HOT_ROD_FLOW.md"
echo ""
echo -e "${BLUE}🔧 Management:${NC}"
echo "   wrangler tail --config wrangler-hotrod.toml  # View logs"
echo "   wrangler d1 execute noizylab-hotrod --command 'SELECT * FROM repairs'  # Query DB"
echo ""
echo -e "${GREEN}Deployment complete! 🎉${NC}"

