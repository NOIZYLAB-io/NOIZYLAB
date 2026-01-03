#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════
# CONDUCTOR + VALIDATOR — INSTANT DEPLOY
# Run on GOD: cd ~/Downloads && bash DEPLOY-CONDUCTOR-VALIDATOR.sh
# ═══════════════════════════════════════════════════════════════════════════

set -e
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'; NC='\033[0m'
WRANGLER="npx wrangler"
command -v wrangler &> /dev/null && WRANGLER="wrangler"

echo -e "${CYAN}══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}  🚀 GORUNFREE — CONDUCTOR + VALIDATOR DEPLOY${NC}"
echo -e "${CYAN}══════════════════════════════════════════════════════════════${NC}"
echo ""

# Auth check
$WRANGLER whoami || { echo -e "${YELLOW}Login required...${NC}"; $WRANGLER login; }

# Extract packages
cd ~/Downloads

echo -e "${YELLOW}📦 Extracting packages...${NC}"
[ -f conductor-v2.zip ] && unzip -o conductor-v2.zip -d conductor 2>/dev/null || true
[ -f validator.zip ] && unzip -o validator.zip -d validator 2>/dev/null || true

# Deploy CONDUCTOR
echo -e "${CYAN}──────────────────────────────────────────────────────────────${NC}"
echo -e "${CYAN}  📋 Deploying CONDUCTOR...${NC}"
echo -e "${CYAN}──────────────────────────────────────────────────────────────${NC}"
cd ~/Downloads/conductor && $WRANGLER deploy
echo -e "${GREEN}✅ CONDUCTOR: https://conductor.fishmusicinc.workers.dev${NC}"
echo ""

# Deploy VALIDATOR
echo -e "${CYAN}──────────────────────────────────────────────────────────────${NC}"
echo -e "${CYAN}  ✓ Deploying VALIDATOR...${NC}"
echo -e "${CYAN}──────────────────────────────────────────────────────────────${NC}"
cd ~/Downloads/validator && $WRANGLER deploy
echo -e "${GREEN}✅ VALIDATOR: https://validator.fishmusicinc.workers.dev${NC}"
echo ""

echo -e "${GREEN}══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  🎉 DONE! Both workers deployed.${NC}"
echo -e "${GREEN}══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "Test commands:"
echo "  curl https://conductor.fishmusicinc.workers.dev/api/status"
echo "  curl https://validator.fishmusicinc.workers.dev/api/status"
echo ""
