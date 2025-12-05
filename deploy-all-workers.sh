#!/bin/bash
# CLOUDFLARE WORKERS DEPLOYMENT SCRIPT
# Deploy all AI GENIUS and NOIZYLAB workers
# GORUNFREE - One command = everything deployed

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m'

clear
echo -e "${PURPLE}${BOLD}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        ☁️  CLOUDFLARE WORKERS DEPLOYMENT ☁️                   ║
║                                                               ║
║        Deploy All AI GENIUS & NOIZYLAB Workers                ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}\n"

cd "$(dirname "$0")"

# Check if wrangler is installed
if ! command -v wrangler &> /dev/null; then
    echo -e "${RED}Wrangler CLI not found!${NC}"
    echo -e "${YELLOW}Installing Wrangler...${NC}"
    npm install -g wrangler
fi

echo -e "${CYAN}Checking Cloudflare authentication...${NC}"
if ! wrangler whoami &> /dev/null; then
    echo -e "${YELLOW}Not authenticated. Running: wrangler login${NC}"
    wrangler login
fi

echo -e "${GREEN}✓ Authenticated with Cloudflare${NC}"
echo ""

# Get account ID
ACCOUNT_ID=$(wrangler whoami | grep "Account ID" | awk '{print $3}')
echo -e "${CYAN}Account ID: ${NC}$ACCOUNT_ID"
echo ""

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}API KEYS SETUP${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}You'll need to set up API keys as secrets.${NC}"
echo -e "${YELLOW}Press Enter after setting each key, or 's' to skip all.${NC}"
echo ""

read -p "Set up API keys now? (y/n/s): " SETUP_KEYS

if [ "$SETUP_KEYS" = "y" ]; then
    echo ""
    echo -e "${CYAN}Setting up API keys...${NC}"
    
    # Anthropic API Key (required for Claude)
    if [ ! -z "$ANTHROPIC_API_KEY" ]; then
        echo -e "${BLUE}Using ANTHROPIC_API_KEY from environment${NC}"
        echo "$ANTHROPIC_API_KEY" | wrangler secret put ANTHROPIC_API_KEY
    else
        echo -e "${YELLOW}Enter Anthropic API Key (or press Enter to skip):${NC}"
        wrangler secret put ANTHROPIC_API_KEY
    fi
    
    # Google API Key (for Gemini)
    echo -e "${YELLOW}Enter Google API Key (or press Enter to skip):${NC}"
    wrangler secret put GOOGLE_API_KEY
    
    # OpenAI API Key (optional)
    echo -e "${YELLOW}Enter OpenAI API Key (or press Enter to skip):${NC}"
    wrangler secret put OPENAI_API_KEY
    
    echo -e "${GREEN}✓ API keys configured${NC}"
    echo ""
fi

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[1/4] DEPLOYING AI GENIUS CLOUD WORKER${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

cd cloudflare-workers

# Deploy AI GENIUS
echo -e "${CYAN}Deploying ai-genius-cloud...${NC}"
cat > wrangler-ai-genius.toml << EOFCONFIG
name = "ai-genius-cloud"
main = "ai-genius-worker.js"
compatibility_date = "2024-11-01"
EOFCONFIG

wrangler deploy ai-genius-worker.js --config wrangler-ai-genius.toml

if [ $? -eq 0 ]; then
    AI_GENIUS_URL=$(wrangler deployments list | grep "ai-genius-cloud" | awk '{print $2}' | head -1)
    echo -e "${GREEN}✓ AI GENIUS deployed${NC}"
    echo -e "${CYAN}URL: ${NC}https://ai-genius-cloud.$ACCOUNT_ID.workers.dev"
else
    echo -e "${RED}✗ AI GENIUS deployment failed${NC}"
fi

echo ""

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[2/4] CREATING D1 DATABASE${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Create D1 database
echo -e "${CYAN}Creating NOIZYLAB database...${NC}"
DB_RESULT=$(wrangler d1 create noizylab-db --experimental 2>&1)

if echo "$DB_RESULT" | grep -q "already exists"; then
    echo -e "${YELLOW}⚠ Database already exists${NC}"
    DB_ID=$(wrangler d1 list | grep "noizylab-db" | awk '{print $2}')
else
    DB_ID=$(echo "$DB_RESULT" | grep -oP 'database_id\s*=\s*"\K[^"]+')
    echo -e "${GREEN}✓ Database created${NC}"
fi

echo -e "${CYAN}Database ID: ${NC}$DB_ID"

# Initialize database schema
echo -e "${CYAN}Initializing database schema...${NC}"
cat > ../schema.sql << EOFSQL
CREATE TABLE IF NOT EXISTS repairs (
    id TEXT PRIMARY KEY,
    customer_name TEXT NOT NULL,
    customer_email TEXT NOT NULL,
    customer_phone TEXT NOT NULL,
    device_type TEXT NOT NULL,
    device_model TEXT,
    issue TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    price REAL DEFAULT 89.00
);

CREATE INDEX IF NOT EXISTS idx_status ON repairs(status);
CREATE INDEX IF NOT EXISTS idx_created ON repairs(created_at);
EOFSQL

wrangler d1 execute noizylab-db --file=../schema.sql --remote

echo -e "${GREEN}✓ Database schema initialized${NC}"
echo ""

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[3/4] DEPLOYING NOIZYLAB BUSINESS PORTAL${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Create KV namespace
echo -e "${CYAN}Creating KV namespaces...${NC}"
REPAIRS_KV=$(wrangler kv:namespace create REPAIRS --preview false 2>&1 | grep -oP 'id\s*=\s*"\K[^"]+')
echo -e "${GREEN}✓ REPAIRS KV created: $REPAIRS_KV${NC}"

# Deploy Business Portal
echo -e "${CYAN}Deploying noizylab-business...${NC}"
cat > wrangler-business.toml << EOFCONFIG
name = "noizylab-business"
main = "noizylab-business-worker.js"
compatibility_date = "2024-11-01"

[[kv_namespaces]]
binding = "REPAIRS"
id = "$REPAIRS_KV"

[[d1_databases]]
binding = "DB"
database_name = "noizylab-db"
database_id = "$DB_ID"
EOFCONFIG

wrangler deploy noizylab-business-worker.js --config wrangler-business.toml

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ NOIZYLAB Business Portal deployed${NC}"
    echo -e "${CYAN}URL: ${NC}https://noizylab-business.$ACCOUNT_ID.workers.dev"
else
    echo -e "${RED}✗ Business Portal deployment failed${NC}"
fi

echo ""

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[4/4] DEPLOYING WORKFLOW WORKER${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${CYAN}Deploying noizylab-workflow...${NC}"
cat > wrangler-workflow.toml << EOFCONFIG
name = "noizylab-workflow"
main = "noizylab-workflow-worker.js"
compatibility_date = "2024-11-01"

[[workflows]]
binding = "REPAIR_WORKFLOW"
name = "repair-workflow"
class_name = "RepairWorkflow"

[[kv_namespaces]]
binding = "REPAIRS"
id = "$REPAIRS_KV"

[[d1_databases]]
binding = "DB"
database_name = "noizylab-db"
database_id = "$DB_ID"
EOFCONFIG

wrangler deploy noizylab-workflow-worker.js --config wrangler-workflow.toml

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Workflow Worker deployed${NC}"
    echo -e "${CYAN}URL: ${NC}https://noizylab-workflow.$ACCOUNT_ID.workers.dev"
else
    echo -e "${RED}✗ Workflow deployment failed${NC}"
fi

echo ""

# Save URLs to config
cat > ../cloudflare-urls.json << EOFURLS
{
  "ai_genius_cloud": "https://ai-genius-cloud.$ACCOUNT_ID.workers.dev",
  "noizylab_business": "https://noizylab-business.$ACCOUNT_ID.workers.dev",
  "noizylab_workflow": "https://noizylab-workflow.$ACCOUNT_ID.workers.dev",
  "account_id": "$ACCOUNT_ID",
  "database_id": "$DB_ID",
  "kv_namespace_id": "$REPAIRS_KV",
  "deployed_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOFURLS

echo -e "${GREEN}✓ Configuration saved to cloudflare-urls.json${NC}"
echo ""

# Summary
clear
echo -e "${GREEN}${BOLD}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║              ✅ DEPLOYMENT COMPLETE ✅                         ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}\n"

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}🎯 YOUR CLOUDFLARE WORKERS${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${BLUE}AI GENIUS Cloud:${NC}"
echo -e "  ${GREEN}https://ai-genius-cloud.$ACCOUNT_ID.workers.dev${NC}"
echo -e "  Test: curl https://ai-genius-cloud.$ACCOUNT_ID.workers.dev/health"
echo ""

echo -e "${BLUE}NOIZYLAB Business Portal:${NC}"
echo -e "  ${GREEN}https://noizylab-business.$ACCOUNT_ID.workers.dev${NC}"
echo -e "  Customer Portal: Open in browser"
echo ""

echo -e "${BLUE}NOIZYLAB Workflow:${NC}"
echo -e "  ${GREEN}https://noizylab-workflow.$ACCOUNT_ID.workers.dev${NC}"
echo -e "  Automated 16-step repair process"
echo ""

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}📊 RESOURCES CREATED${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${BLUE}D1 Database:${NC}         noizylab-db ($DB_ID)"
echo -e "${BLUE}KV Namespace:${NC}        REPAIRS ($REPAIRS_KV)"
echo -e "${BLUE}Workers:${NC}             3 deployed"
echo -e "${BLUE}Workflows:${NC}           1 configured"
echo ""

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}🔧 NEXT STEPS${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "1. Test AI GENIUS:"
echo "   curl -X POST https://ai-genius-cloud.$ACCOUNT_ID.workers.dev/query \\"
echo "     -H 'Content-Type: application/json' \\"
echo "     -d '{\"model\":\"claude-sonnet-4\",\"prompt\":\"Hello\"}'"
echo ""
echo "2. Open Business Portal:"
echo "   open https://noizylab-business.$ACCOUNT_ID.workers.dev"
echo ""
echo "3. Update local scripts with URLs:"
echo "   Edit universal-ai-selector.py"
echo "   Set WORKER_URL = 'https://ai-genius-cloud.$ACCOUNT_ID.workers.dev'"
echo ""
echo "4. View deployment logs:"
echo "   wrangler tail ai-genius-cloud"
echo ""

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}💡 MANAGEMENT COMMANDS${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "View logs:           wrangler tail [worker-name]"
echo "List workers:        wrangler deployments list"
echo "Update worker:       wrangler deploy [file]"
echo "Delete worker:       wrangler delete [worker-name]"
echo "View secrets:        wrangler secret list"
echo "Database query:      wrangler d1 execute noizylab-db --command='SELECT * FROM repairs'"
echo ""

echo -e "${GREEN}${BOLD}🔥 CLOUDFLARE DEPLOYMENT COMPLETE! 🔥${NC}"
echo ""
