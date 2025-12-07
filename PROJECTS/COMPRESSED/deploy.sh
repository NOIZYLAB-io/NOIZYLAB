#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════
# NOIZYLAB ULTIMATE - GORUNFREE DEPLOYMENT
# ALL PROBLEMS FIXED - PRODUCTION READY
# ═══════════════════════════════════════════════════════════════════════════

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                          ║"
echo "║    ███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██╗      █████╗ ██████╗       ║"
echo "║    ████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╗██╔══██╗      ║"
echo "║    ██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║     ███████║██████╔╝      ║"
echo "║    ██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║     ██╔══██║██╔══██╗      ║"
echo "║    ██║ ╚████║╚██████╔╝██║███████╗   ██║   ███████╗██║  ██║██████╔╝      ║"
echo "║    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝       ║"
echo "║                                                                          ║"
echo "║    🔥 ULTIMATE EDITION - ALL PROBLEMS FIXED 🔥                          ║"
echo "║                                                                          ║"
echo "║    ✅ Admin Authentication                                               ║"
echo "║    ✅ XSS Protection                                                     ║"
echo "║    ✅ Rate Limiting                                                      ║"
echo "║    ✅ CSRF Protection                                                    ║"
echo "║    ✅ Stripe Webhook Verification                                        ║"
echo "║    ✅ Security Headers                                                   ║"
echo "║    ✅ Input Validation                                                   ║"
echo "║    ✅ Audit Logging                                                      ║"
echo "║                                                                          ║"
echo "╚══════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check for wrangler
if ! command -v wrangler &> /dev/null; then
    echo -e "${YELLOW}📦 Installing Wrangler CLI...${NC}"
    npm install -g wrangler
fi

# Check login
echo -e "${CYAN}🔐 Checking Cloudflare authentication...${NC}"
if ! wrangler whoami 2>/dev/null; then
    echo ""
    echo -e "${YELLOW}⚠️  Need to login to Cloudflare${NC}"
    wrangler login
fi

echo -e "${GREEN}✅ Authenticated with Cloudflare${NC}"
echo ""

# Deploy
echo -e "${CYAN}🚀 Deploying NOIZYLAB ULTIMATE...${NC}"
echo ""
wrangler deploy

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${GREEN}✅ DEPLOYMENT COMPLETE!${NC}"
echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════════════════${NC}"

# Get worker URL
WORKER_URL="https://noizylab.rob-plowman.workers.dev"

echo ""
echo -e "${CYAN}🌐 YOUR LIVE SITE:${NC}"
echo "   $WORKER_URL"
echo ""
echo -e "${CYAN}📍 ENDPOINTS:${NC}"
echo "   /              Customer intake form"
echo "   /status        Customer status check"
echo "   /contact       Contact form"
echo "   /success       Payment confirmation"
echo "   /admin         Admin dashboard (requires password)"
echo "   /admin/ticket/ Individual ticket view"
echo "   /admin/export  Download CSV"
echo "   /health        System status"
echo ""

echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}🔐 REQUIRED: SET ADMIN PASSWORD${NC}"
echo ""
echo "   Run this command now:"
echo ""
echo -e "   ${CYAN}wrangler secret put ADMIN_PASSWORD${NC}"
echo ""
echo "   Then enter a strong password when prompted."
echo "   Username will be: rob"
echo ""
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════════════${NC}"

echo ""
echo -e "${YELLOW}💳 TO ENABLE STRIPE PAYMENTS:${NC}"
echo ""
echo "   1. Go to stripe.com and create/login to account"
echo "   2. Dashboard → Developers → API Keys"
echo "   3. Copy your Secret Key"
echo "   4. Run:"
echo ""
echo -e "   ${CYAN}wrangler secret put STRIPE_SECRET_KEY${NC}"
echo ""
echo "   Test card: 4242 4242 4242 4242"
echo ""

echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}🔒 FOR WEBHOOK SECURITY (recommended):${NC}"
echo ""
echo "   1. Go to stripe.com → Developers → Webhooks"
echo "   2. Add endpoint: $WORKER_URL/webhook"
echo "   3. Select event: checkout.session.completed"
echo "   4. Copy the Signing Secret"
echo "   5. Run:"
echo ""
echo -e "   ${CYAN}wrangler secret put STRIPE_WEBHOOK_SECRET${NC}"
echo ""

echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}🌐 TO CONNECT YOUR DOMAIN:${NC}"
echo ""
echo "   1. Go to Cloudflare Dashboard"
echo "   2. Workers & Pages → noizylab → Settings → Triggers"
echo "   3. Add Custom Domain: noizylab.ca"
echo ""

echo -e "${GREEN}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${GREEN}🧪 TEST IT NOW:${NC}"
echo ""
echo "   1. Open: $WORKER_URL"
echo "   2. Check health: $WORKER_URL/health"
echo "   3. Try admin (after setting password): $WORKER_URL/admin"
echo ""
echo -e "${GREEN}GORUNFREE! 🚀${NC}"
