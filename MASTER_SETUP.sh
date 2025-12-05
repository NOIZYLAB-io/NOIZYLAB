#!/bin/bash
# MASTER SETUP - Does Everything Perfectly
# One script to rule them all

set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  🚀 NOIZYLAB OS - MASTER SETUP${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}\n"

cd "$ROOT"

# Run complete setup
echo -e "${GREEN}Running complete Cloudflare AI + Gemini setup...${NC}\n"
./scripts/setup-cloudflare-gemini.sh

# Validate
echo -e "\n${GREEN}Validating setup...${NC}\n"
./scripts/validate-setup.sh

echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ MASTER SETUP COMPLETE!${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}\n"

echo "📋 Next Steps:"
echo "  1. Get Gemini API Key: https://aistudio.google.com/app/apikey"
echo "  2. Update wrangler.toml with your IDs"
echo "  3. Test: cd workers/ai-super-worker && wrangler dev"
echo "  4. Deploy: ./scripts/deploy-ai.sh"
echo ""

