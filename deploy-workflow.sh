#!/bin/bash
# DEPLOY NOIZYLAB WORKFLOWS
# Complete business automation orchestration
# GORUNFREEX1000 - Zero friction deployment

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${PURPLE}${BOLD}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        🔄  NOIZYLAB WORKFLOWS DEPLOYMENT  🔄                  ║
║                                                               ║
║         Complete Business Process Automation                  ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}\n"

cd NOIZYLAB_FLOW

echo -e "${BLUE}[1/6] Installing Dependencies${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
npm install
echo -e "${GREEN}✓ Dependencies installed${NC}\n"

echo -e "${BLUE}[2/6] Checking Wrangler Authentication${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if ! wrangler whoami &> /dev/null; then
    echo -e "${YELLOW}Not logged in. Opening browser...${NC}"
    wrangler login
else
    echo -e "${GREEN}✓ Already authenticated${NC}"
fi
echo ""

echo -e "${BLUE}[3/6] Creating D1 Database${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${CYAN}Do you want to create a new D1 database? (y/n)${NC}"
read -r CREATE_DB

if [ "$CREATE_DB" = "y" ] || [ "$CREATE_DB" = "Y" ]; then
    wrangler d1 create noizylab
    echo -e "${YELLOW}Copy the database_id and update wrangler.toml${NC}"
    echo -e "${YELLOW}Press Enter when ready...${NC}"
    read
fi
echo -e "${GREEN}✓ Database ready${NC}\n"

echo -e "${BLUE}[4/6] Setting Up Database Schema${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Create schema file
cat > schema.sql << 'EOFSCHEMA'
-- Repairs table
CREATE TABLE IF NOT EXISTS repairs (
    repair_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    tech_id TEXT,
    device_type TEXT NOT NULL,
    issue TEXT NOT NULL,
    status TEXT NOT NULL,
    urgency TEXT DEFAULT 'normal',
    repair_notes TEXT,
    parts_used TEXT,
    time_spent REAL,
    final_price REAL,
    payment_status TEXT DEFAULT 'pending',
    created_at TEXT NOT NULL,
    assigned_at TEXT,
    completed_at TEXT
);

-- Technicians table
CREATE TABLE IF NOT EXISTS technicians (
    tech_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    skill_level INTEGER DEFAULT 5,
    current_repairs INTEGER DEFAULT 0,
    status TEXT DEFAULT 'available',
    created_at TEXT NOT NULL
);

-- Repair parts table
CREATE TABLE IF NOT EXISTS repair_parts (
    part_id TEXT PRIMARY KEY,
    repair_id TEXT NOT NULL,
    part_name TEXT NOT NULL,
    cost REAL NOT NULL,
    FOREIGN KEY (repair_id) REFERENCES repairs(repair_id)
);

-- Analytics table
CREATE TABLE IF NOT EXISTS repair_analytics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    repair_id TEXT NOT NULL,
    total_time REAL NOT NULL,
    final_price REAL NOT NULL,
    quality_score INTEGER,
    tech_id TEXT,
    completed_at TEXT NOT NULL,
    FOREIGN KEY (repair_id) REFERENCES repairs(repair_id)
);

-- Insert sample technician
INSERT OR IGNORE INTO technicians (tech_id, name, email, skill_level, created_at)
VALUES ('TECH-001', 'John Smith', 'john@noizylab.com', 8, datetime('now'));
EOFSCHEMA

# Execute schema
wrangler d1 execute noizylab --file=schema.sql
echo -e "${GREEN}✓ Database schema created${NC}\n"

echo -e "${BLUE}[5/6] Configuring API Keys${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Claude API key (you have this)
CLAUDE_KEY="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"

echo -e "${CYAN}Setting Claude API key...${NC}"
echo "$CLAUDE_KEY" | wrangler secret put ANTHROPIC_API_KEY

echo ""
echo -e "${YELLOW}Add optional API keys? (y/n)${NC}"
read -r ADD_KEYS

if [ "$ADD_KEYS" = "y" ] || [ "$ADD_KEYS" = "Y" ]; then
    echo ""
    echo -e "${CYAN}SendGrid API Key (for emails):${NC}"
    echo "Get at: https://app.sendgrid.com/settings/api_keys"
    read -p "Key (or skip): " SENDGRID_KEY
    if [ ! -z "$SENDGRID_KEY" ]; then
        echo "$SENDGRID_KEY" | wrangler secret put SENDGRID_API_KEY
    fi

    echo ""
    echo -e "${CYAN}Stripe API Key (for payments):${NC}"
    echo "Get at: https://dashboard.stripe.com/apikeys"
    read -p "Key (or skip): " STRIPE_KEY
    if [ ! -z "$STRIPE_KEY" ]; then
        echo "$STRIPE_KEY" | wrangler secret put STRIPE_API_KEY
    fi

    echo ""
    echo -e "${CYAN}EasyPost API Key (for shipping):${NC}"
    echo "Get at: https://www.easypost.com/account/api-keys"
    read -p "Key (or skip): " EASYPOST_KEY
    if [ ! -z "$EASYPOST_KEY" ]; then
        echo "$EASYPOST_KEY" | wrangler secret put EASYPOST_API_KEY
    fi
fi

echo -e "${GREEN}✓ API keys configured${NC}\n"

echo -e "${BLUE}[6/6] Deploying Workflow${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
wrangler deploy
WORKER_URL=$(wrangler deployments list 2>/dev/null | grep "https://" | head -1 | awk '{print $2}' || echo "")

echo -e "${GREEN}✓ Workflow deployed${NC}\n"

# Success banner
echo -e "${GREEN}${BOLD}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        ✅  NOIZYLAB WORKFLOWS DEPLOYED  ✅                    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}\n"

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}WORKFLOW ENDPOINTS:${NC}"
echo ""
if [ ! -z "$WORKER_URL" ]; then
    echo "  Create Repair:   $WORKER_URL/api/repair/create"
    echo "  Check Status:    $WORKER_URL/api/repair/status/{id}"
    echo "  Get Result:      $WORKER_URL/api/repair/result/{id}"
    echo ""
else
    echo "  Your worker URL will be available after deployment"
    echo ""
fi

echo -e "${CYAN}${BOLD}WORKFLOW FEATURES:${NC}"
echo "  ✅ Automated repair intake"
echo "  ✅ AI-powered diagnosis (Claude)"
echo "  ✅ Smart tech assignment"
echo "  ✅ Progress monitoring"
echo "  ✅ Quality checks"
echo "  ✅ Automated invoicing"
echo "  ✅ Payment tracking"
echo "  ✅ Shipping integration"
echo "  ✅ Review requests"
echo "  ✅ Analytics tracking"
echo ""

echo -e "${CYAN}${BOLD}TEST THE WORKFLOW:${NC}"
echo ""
echo 'curl -X POST $WORKER_URL/api/repair/create \'
echo "  -H 'Content-Type: application/json' \\"
echo '  -d '"'"'{
    "customerId": "CUST-001",
    "customerEmail": "customer@example.com",
    "customerName": "John Doe",
    "deviceType": "Intel i9-12900K",
    "issue": "System won'"'"'t boot, possible bent pins",
    "urgency": "normal"
  }'"'"
echo ""

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${GREEN}${BOLD}🚀 WORKFLOW AUTOMATION COMPLETE 🚀${NC}"
echo ""
echo -e "${YELLOW}Next: Integrate with customer portal for automatic workflow triggers${NC}"
echo ""
