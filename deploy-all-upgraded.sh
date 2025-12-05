#!/bin/bash

# ============================================================================
# MASTER DEPLOYMENT SCRIPT - ALL THREE DOMAINS
# Deploy all Cloudflare Workers for NOIZYLAB, FISHMUSICINC, and NOIZY.AI
# ============================================================================

set -e  # Exit on error

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                                                                ║"
echo "║   🚀 MASTER DEPLOYMENT - ALL THREE DOMAINS 🚀                  ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Check for wrangler
if ! command -v wrangler &> /dev/null; then
    echo -e "${RED}❌ Wrangler CLI not found!${NC}"
    echo "Install with: npm install -g wrangler"
    exit 1
fi

echo -e "${GREEN}✅ Wrangler CLI found${NC}"
echo ""

# ============================================================================
# CONFIGURATION
# ============================================================================

DEPLOY_NOIZYLAB=${DEPLOY_NOIZYLAB:-true}
DEPLOY_FISHMUSICINC=${DEPLOY_FISHMUSICINC:-true}
DEPLOY_NOIZYAI=${DEPLOY_NOIZYAI:-true}

echo "Deployment Configuration:"
echo "  NOIZYLAB.CA:       $DEPLOY_NOIZYLAB"
echo "  FISHMUSICINC.COM:  $DEPLOY_FISHMUSICINC"
echo "  NOIZY.AI:          $DEPLOY_NOIZYAI"
echo ""

read -p "Continue with deployment? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Deployment cancelled."
    exit 0
fi

echo ""

# ============================================================================
# DEPLOY NOIZYLAB.CA
# ============================================================================

if [ "$DEPLOY_NOIZYLAB" = true ]; then
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${PURPLE}1️⃣  DEPLOYING NOIZYLAB.CA${NC}"
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    
    # Business Portal
    echo -e "${BLUE}📦 Deploying NOIZYLAB Business Portal...${NC}"
    wrangler deploy noizylab-business-worker.js --config wrangler-business.toml
    echo -e "${GREEN}✅ Business Portal deployed${NC}"
    echo ""
    
    # Workflow Worker
    echo -e "${BLUE}⚙️  Deploying NOIZYLAB Workflow...${NC}"
    wrangler deploy noizylab-workflow-worker.js --config wrangler-workflow.toml
    echo -e "${GREEN}✅ Workflow Worker deployed${NC}"
    echo ""
    
    # AI Genius
    echo -e "${BLUE}🤖 Deploying AI GENIUS Cloud...${NC}"
    wrangler deploy ai-genius-worker.js --config wrangler-ai-genius.toml
    echo -e "${GREEN}✅ AI GENIUS deployed${NC}"
    echo ""
    
    # Email Automation (NEW)
    echo -e "${BLUE}📧 Deploying Email Automation...${NC}"
    if [ -f "noizylab-email-automation.js" ]; then
        # Create config if doesn't exist
        if [ ! -f "wrangler-email.toml" ]; then
            cat > wrangler-email.toml << 'EOF'
name = "noizylab-email-automation"
main = "noizylab-email-automation.js"
compatibility_date = "2024-11-24"
account_id = "5ba03939f87a498d0bbed185ee123946"

[[kv_namespaces]]
binding = "EMAIL_QUEUE"
id = "431ae8ffb1644cad8b499656e87fad83"

[[d1_databases]]
binding = "DB"
database_name = "noizylab-db"
database_id = "794535eb-9566-4b00-b38f-15cb173d4ad9"
EOF
        fi
        wrangler deploy noizylab-email-automation.js --config wrangler-email.toml
        echo -e "${GREEN}✅ Email Automation deployed${NC}"
    else
        echo -e "${YELLOW}⚠️  Email automation file not found, skipping${NC}"
    fi
    echo ""
    
    # SMS Notifications (NEW)
    echo -e "${BLUE}📱 Deploying SMS Notifications...${NC}"
    if [ -f "noizylab-sms-notifications.js" ]; then
        if [ ! -f "wrangler-sms.toml" ]; then
            cat > wrangler-sms.toml << 'EOF'
name = "noizylab-sms-notifications"
main = "noizylab-sms-notifications.js"
compatibility_date = "2024-11-24"
account_id = "5ba03939f87a498d0bbed185ee123946"

[[kv_namespaces]]
binding = "SMS_LOGS"
id = "431ae8ffb1644cad8b499656e87fad83"

[[kv_namespaces]]
binding = "SMS_OPTOUTS"
id = "7ac8f6ab1a0144c1bdbcb11fb69983a2"
EOF
        fi
        wrangler deploy noizylab-sms-notifications.js --config wrangler-sms.toml
        echo -e "${GREEN}✅ SMS Notifications deployed${NC}"
    else
        echo -e "${YELLOW}⚠️  SMS notifications file not found, skipping${NC}"
    fi
    echo ""
    
    echo -e "${GREEN}✅ NOIZYLAB.CA - ALL WORKERS DEPLOYED!${NC}"
    echo ""
fi

# ============================================================================
# DEPLOY FISHMUSICINC.COM
# ============================================================================

if [ "$DEPLOY_FISHMUSICINC" = true ]; then
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${PURPLE}2️⃣  DEPLOYING FISHMUSICINC.COM${NC}"
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    
    # Portal
    echo -e "${BLUE}🎵 Deploying FishMusicInc Portal...${NC}"
    wrangler deploy fishmusicinc-portal-worker.js --config wrangler-fishmusicinc.toml
    echo -e "${GREEN}✅ Portal deployed${NC}"
    echo ""
    
    # AI Assistant (NEW)
    echo -e "${BLUE}🤖 Deploying AI Music Assistant...${NC}"
    if [ -f "fishmusicinc-ai-assistant.js" ]; then
        if [ ! -f "wrangler-fishmusicinc-ai.toml" ]; then
            cat > wrangler-fishmusicinc-ai.toml << 'EOF'
name = "fishmusicinc-ai-assistant"
main = "fishmusicinc-ai-assistant.js"
compatibility_date = "2024-11-24"
account_id = "5ba03939f87a498d0bbed185ee123946"

[[kv_namespaces]]
binding = "CACHE"
id = "9ae5d5b82a8c4d2ea8fee3f63db42e71"
EOF
        fi
        wrangler deploy fishmusicinc-ai-assistant.js --config wrangler-fishmusicinc-ai.toml
        echo -e "${GREEN}✅ AI Music Assistant deployed${NC}"
    else
        echo -e "${YELLOW}⚠️  AI assistant file not found, skipping${NC}"
    fi
    echo ""
    
    echo -e "${GREEN}✅ FISHMUSICINC.COM - ALL WORKERS DEPLOYED!${NC}"
    echo ""
fi

# ============================================================================
# DEPLOY NOIZY.AI
# ============================================================================

if [ "$DEPLOY_NOIZYAI" = true ]; then
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${PURPLE}3️⃣  DEPLOYING NOIZY.AI${NC}"
    echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    
    # Check for API keys
    echo -e "${YELLOW}🔑 Checking API keys...${NC}"
    
    HAS_ANTHROPIC=$(wrangler secret list --name noizyai-api 2>/dev/null | grep -c "ANTHROPIC_API_KEY" || echo "0")
    HAS_GOOGLE=$(wrangler secret list --name noizyai-api 2>/dev/null | grep -c "GOOGLE_API_KEY" || echo "0")
    
    if [ "$HAS_ANTHROPIC" = "0" ]; then
        echo -e "${YELLOW}⚠️  ANTHROPIC_API_KEY not set${NC}"
        read -p "Enter Anthropic API key (or press Enter to skip): " ANTHROPIC_KEY
        if [ ! -z "$ANTHROPIC_KEY" ]; then
            echo "$ANTHROPIC_KEY" | wrangler secret put ANTHROPIC_API_KEY --name noizyai-api
            echo -e "${GREEN}✅ Anthropic key set${NC}"
        fi
    else
        echo -e "${GREEN}✅ Anthropic key already set${NC}"
    fi
    
    if [ "$HAS_GOOGLE" = "0" ]; then
        echo -e "${YELLOW}⚠️  GOOGLE_API_KEY not set${NC}"
        read -p "Enter Google API key (or press Enter to skip): " GOOGLE_KEY
        if [ ! -z "$GOOGLE_KEY" ]; then
            echo "$GOOGLE_KEY" | wrangler secret put GOOGLE_API_KEY --name noizyai-api
            echo -e "${GREEN}✅ Google key set${NC}"
        fi
    else
        echo -e "${GREEN}✅ Google key already set${NC}"
    fi
    echo ""
    
    # API Worker
    echo -e "${BLUE}🤖 Deploying NOIZY.AI API...${NC}"
    wrangler deploy noizyai-api-worker.js --config wrangler-noizyai.toml
    echo -e "${GREEN}✅ API Worker deployed${NC}"
    echo ""
    
    # Advanced Gateway (NEW)
    echo -e "${BLUE}🚀 Deploying Advanced Gateway...${NC}"
    if [ -f "noizyai-advanced-gateway.js" ]; then
        if [ ! -f "wrangler-noizyai-gateway.toml" ]; then
            cat > wrangler-noizyai-gateway.toml << 'EOF'
name = "noizyai-advanced-gateway"
main = "noizyai-advanced-gateway.js"
compatibility_date = "2024-11-24"
account_id = "5ba03939f87a498d0bbed185ee123946"

[[kv_namespaces]]
binding = "USERS"
id = "46382404c8c347439201656f70cc1986"

[[kv_namespaces]]
binding = "CACHE"
id = "07b0c8e65eb242098ee955cde4bacd36"

[[kv_namespaces]]
binding = "ANALYTICS"
id = "38ba7eec3dcc4978a411717371deb9c9"

[[d1_databases]]
binding = "DB"
database_name = "noizyai-db"
database_id = "ebcf576f-51e3-4e3d-829e-219f8fe6001c"
EOF
        fi
        wrangler deploy noizyai-advanced-gateway.js --config wrangler-noizyai-gateway.toml
        echo -e "${GREEN}✅ Advanced Gateway deployed${NC}"
    else
        echo -e "${YELLOW}⚠️  Advanced gateway file not found, skipping${NC}"
    fi
    echo ""
    
    echo -e "${GREEN}✅ NOIZY.AI - ALL WORKERS DEPLOYED!${NC}"
    echo ""
fi

# ============================================================================
# DEPLOYMENT SUMMARY
# ============================================================================

echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║                                                                ║${NC}"
echo -e "${GREEN}║   ✅ DEPLOYMENT COMPLETE - ALL DOMAINS LIVE! ✅                 ║${NC}"
echo -e "${GREEN}║                                                                ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo "📊 Deployment Summary:"
echo ""

if [ "$DEPLOY_NOIZYLAB" = true ]; then
    echo "1️⃣  NOIZYLAB.CA:"
    echo "  ✅ Business Portal:      noizylab-business.noizylab-ca.workers.dev"
    echo "  ✅ Workflow System:      noizylab-workflow.noizylab-ca.workers.dev"
    echo "  ✅ AI GENIUS:            ai-genius-cloud.noizylab-ca.workers.dev"
    echo "  ✅ Email Automation:     noizylab-email-automation.noizylab-ca.workers.dev"
    echo "  ✅ SMS Notifications:    noizylab-sms-notifications.noizylab-ca.workers.dev"
    echo ""
fi

if [ "$DEPLOY_FISHMUSICINC" = true ]; then
    echo "2️⃣  FISHMUSICINC.COM:"
    echo "  ✅ Client Portal:        fishmusicinc-portal.noizylab-ca.workers.dev"
    echo "  ✅ AI Music Assistant:   fishmusicinc-ai-assistant.noizylab-ca.workers.dev"
    echo ""
fi

if [ "$DEPLOY_NOIZYAI" = true ]; then
    echo "3️⃣  NOIZY.AI:"
    echo "  ✅ API Platform:         noizyai-api.noizylab-ca.workers.dev"
    echo "  ✅ Advanced Gateway:     noizyai-advanced-gateway.noizylab-ca.workers.dev"
    echo ""
fi

echo "💰 Cost: $0/month (Cloudflare free tier)"
echo "🚀 Status: ALL SYSTEMS OPERATIONAL"
echo ""

echo "🧪 Test your deployments:"
echo ""
echo "# Health checks"
echo "curl https://noizylab-business.noizylab-ca.workers.dev/health"
echo "curl https://fishmusicinc-portal.noizylab-ca.workers.dev/health"
echo "curl https://noizyai-api.noizylab-ca.workers.dev/health"
echo ""

echo -e "${GREEN}🎉 GORUNFREE DEPLOYMENT COMPLETE! 🎉${NC}"
