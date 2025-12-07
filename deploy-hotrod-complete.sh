#!/bin/bash
###############################################################################
# 🔥 HOT ROD FLOW - COMPLETE DEPLOYMENT SCRIPT
# 
# One-click deployment for all NOIZYLAB workers:
# 1. M365 Hub Worker
# 2. SMS Notification Worker
# 3. Stripe Payment Worker
# 4. Unified Dashboard Worker
# 5. Hot Rod Flow Worker (Central Orchestration)
#
# Prerequisites:
# - Wrangler CLI installed (npm install -g wrangler)
# - Cloudflare account authenticated (wrangler login)
# - All secrets configured
#
# Usage:
#   ./deploy-hotrod-complete.sh
#
###############################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Banner
echo -e "${PURPLE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║    🔥 HOT ROD FLOW - COMPLETE DEPLOYMENT 🔥              ║"
echo "║                                                           ║"
echo "║    Deploying 5 Workers + Full Integration                ║"
echo "║    Performance Target: MAXIMUM VELOCITY 🏎️               ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo

# Check if wrangler is installed
if ! command -v wrangler &> /dev/null; then
    echo -e "${RED}❌ Error: Wrangler CLI not found${NC}"
    echo "Please install: npm install -g wrangler"
    exit 1
fi

echo -e "${GREEN}✅ Wrangler CLI found${NC}"

# Check if logged in
if ! wrangler whoami &> /dev/null; then
    echo -e "${YELLOW}⚠️  Not logged in to Cloudflare${NC}"
    echo "Running: wrangler login"
    wrangler login
fi

echo -e "${GREEN}✅ Cloudflare authentication verified${NC}"
echo

# Navigate to cloudflare directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLOUDFLARE_DIR="${SCRIPT_DIR}/cloudflare"

if [ ! -d "$CLOUDFLARE_DIR" ]; then
    echo -e "${RED}❌ Error: cloudflare/ directory not found${NC}"
    exit 1
fi

cd "$CLOUDFLARE_DIR"
echo -e "${CYAN}📁 Working directory: $CLOUDFLARE_DIR${NC}"
echo

# Deployment function
deploy_worker() {
    local name=$1
    local worker_file=$2
    local config_file=$3
    local description=$4
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}🚀 Deploying: ${name}${NC}"
    echo -e "${CYAN}   ${description}${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    if [ ! -f "$worker_file" ]; then
        echo -e "${RED}❌ Error: Worker file not found: $worker_file${NC}"
        return 1
    fi
    
    if [ ! -f "$config_file" ]; then
        echo -e "${RED}❌ Error: Config file not found: $config_file${NC}"
        return 1
    fi
    
    echo -e "${YELLOW}⏳ Deploying...${NC}"
    
    if wrangler deploy "$worker_file" --config "$config_file"; then
        echo -e "${GREEN}✅ Successfully deployed: ${name}${NC}"
        echo
        return 0
    else
        echo -e "${RED}❌ Failed to deploy: ${name}${NC}"
        echo
        return 1
    fi
}

# Track deployment status
DEPLOYED=()
FAILED=()

# 1. Deploy M365 Hub Worker
echo -e "${PURPLE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${PURPLE}   STEP 1/5: M365 HUB WORKER${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════${NC}"
echo
if deploy_worker \
    "M365 Hub" \
    "m365-hub-worker.js" \
    "wrangler-m365-hub.toml" \
    "Central email hub via rsplowman@outlook.com"; then
    DEPLOYED+=("M365 Hub")
else
    FAILED+=("M365 Hub")
fi

# 2. Deploy SMS Notification Worker
echo -e "${PURPLE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${PURPLE}   STEP 2/5: SMS NOTIFICATION WORKER${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════${NC}"
echo
if deploy_worker \
    "SMS Notifications" \
    "sms-notification-worker.js" \
    "wrangler-sms.toml" \
    "Twilio SMS integration for repair updates"; then
    DEPLOYED+=("SMS Notifications")
else
    FAILED+=("SMS Notifications")
fi

# 3. Deploy Stripe Payment Worker
echo -e "${PURPLE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${PURPLE}   STEP 3/5: STRIPE PAYMENT WORKER${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════${NC}"
echo
if deploy_worker \
    "Stripe Payments" \
    "stripe-payment-worker.js" \
    "wrangler-stripe.toml" \
    "Payment processing and invoice generation"; then
    DEPLOYED+=("Stripe Payments")
else
    FAILED+=("Stripe Payments")
fi

# 4. Deploy Unified Dashboard Worker
echo -e "${PURPLE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${PURPLE}   STEP 4/5: UNIFIED DASHBOARD WORKER${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════${NC}"
echo
if deploy_worker \
    "Unified Dashboard" \
    "unified-dashboard-worker.js" \
    "wrangler-dashboard.toml" \
    "Single pane of glass - all systems monitoring"; then
    DEPLOYED+=("Unified Dashboard")
else
    FAILED+=("Unified Dashboard")
fi

# 5. Deploy Hot Rod Flow Worker (Central Orchestration)
echo -e "${PURPLE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${PURPLE}   STEP 5/5: HOT ROD FLOW WORKER (CENTRAL)${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════${NC}"
echo
if deploy_worker \
    "Hot Rod Flow" \
    "hotrod-flow-worker.js" \
    "wrangler-hotrod.toml" \
    "Central orchestration - connects all 7 systems"; then
    DEPLOYED+=("Hot Rod Flow")
else
    FAILED+=("Hot Rod Flow")
fi

# Summary
echo
echo -e "${PURPLE}╔═══════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║               🎯 DEPLOYMENT SUMMARY 🎯                    ║${NC}"
echo -e "${PURPLE}╚═══════════════════════════════════════════════════════════╝${NC}"
echo

echo -e "${GREEN}✅ Successfully Deployed (${#DEPLOYED[@]}/5):${NC}"
for worker in "${DEPLOYED[@]}"; do
    echo -e "   ${GREEN}✓${NC} $worker"
done
echo

if [ ${#FAILED[@]} -gt 0 ]; then
    echo -e "${RED}❌ Failed Deployments (${#FAILED[@]}/5):${NC}"
    for worker in "${FAILED[@]}"; do
        echo -e "   ${RED}✗${NC} $worker"
    done
    echo
fi

# Display worker URLs
if [ ${#DEPLOYED[@]} -gt 0 ]; then
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}📍 WORKER URLs:${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo
    echo -e "${BLUE}M365 Hub:${NC}"
    echo "  https://noizylab-m365-hub.noizylab-ca.workers.dev"
    echo
    echo -e "${BLUE}SMS Notifications:${NC}"
    echo "  https://noizylab-sms-notifications.noizylab-ca.workers.dev"
    echo
    echo -e "${BLUE}Stripe Payments:${NC}"
    echo "  https://noizylab-stripe-payments.noizylab-ca.workers.dev"
    echo
    echo -e "${BLUE}Unified Dashboard:${NC}"
    echo "  https://noizylab-unified-dashboard.noizylab-ca.workers.dev"
    echo
    echo -e "${BLUE}Hot Rod Flow (Central):${NC}"
    echo "  https://noizylab-hotrod-flow.noizylab-ca.workers.dev"
    echo
fi

# Performance targets
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}⚡ PERFORMANCE TARGETS:${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo
echo -e "  ${GREEN}✓${NC} Webhook Speed: ${YELLOW}<50ms${NC}"
echo -e "  ${GREEN}✓${NC} Email Delivery: ${YELLOW}<2s${NC}"
echo -e "  ${GREEN}✓${NC} Database Sync: ${YELLOW}Real-time${NC}"
echo -e "  ${GREEN}✓${NC} Velocity: ${YELLOW}MAXIMUM 🏎️${NC}"
echo

# Next steps
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}📝 NEXT STEPS:${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo
echo "1. Set required secrets (if not already done):"
echo "   ${YELLOW}wrangler secret put M365_PASSWORD --name noizylab-m365-hub${NC}"
echo "   ${YELLOW}wrangler secret put TWILIO_ACCOUNT_SID --name noizylab-sms-notifications${NC}"
echo "   ${YELLOW}wrangler secret put TWILIO_AUTH_TOKEN --name noizylab-sms-notifications${NC}"
echo "   ${YELLOW}wrangler secret put STRIPE_SECRET_KEY --name noizylab-stripe-payments${NC}"
echo
echo "2. Test the unified dashboard:"
echo "   ${YELLOW}open https://noizylab-unified-dashboard.noizylab-ca.workers.dev${NC}"
echo
echo "3. Test Hot Rod Flow:"
echo "   ${YELLOW}curl https://noizylab-hotrod-flow.noizylab-ca.workers.dev/health${NC}"
echo
echo "4. Create a test repair:"
echo "   ${YELLOW}curl -X POST https://noizylab-hotrod-flow.noizylab-ca.workers.dev/api/repair/create \\${NC}"
echo "   ${YELLOW}  -H 'Content-Type: application/json' \\${NC}"
echo "   ${YELLOW}  -d '{\"customer_email\":\"test@example.com\",\"device_type\":\"Intel i9\",\"issue\":\"Won't boot\"}'${NC}"
echo

# Final status
echo
if [ ${#FAILED[@]} -eq 0 ]; then
    echo -e "${GREEN}╔═══════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                                                           ║${NC}"
    echo -e "${GREEN}║    🎉 ALL WORKERS DEPLOYED SUCCESSFULLY! 🎉              ║${NC}"
    echo -e "${GREEN}║                                                           ║${NC}"
    echo -e "${GREEN}║    HOT ROD FLOW = MAXIMUM VELOCITY 🏎️                   ║${NC}"
    echo -e "${GREEN}║                                                           ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════════════════╝${NC}"
    exit 0
else
    echo -e "${YELLOW}╔═══════════════════════════════════════════════════════════╗${NC}"
    echo -e "${YELLOW}║                                                           ║${NC}"
    echo -e "${YELLOW}║    ⚠️  DEPLOYMENT COMPLETED WITH WARNINGS ⚠️            ║${NC}"
    echo -e "${YELLOW}║                                                           ║${NC}"
    echo -e "${YELLOW}║    ${#DEPLOYED[@]}/5 workers deployed successfully                      ║${NC}"
    echo -e "${YELLOW}║    Please check failed deployments above                 ║${NC}"
    echo -e "${YELLOW}║                                                           ║${NC}"
    echo -e "${YELLOW}╚═══════════════════════════════════════════════════════════╝${NC}"
    exit 1
fi
