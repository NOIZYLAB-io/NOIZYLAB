#!/bin/bash

# NOIZYLAB Slack Bot - One-Click Manifest Deploy
# This script helps you create the Slack app with the manifest

MANIFEST_FILE="$HOME/NOIZYLAB/slack-bot/noizylab-manifest.yaml"
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

clear

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 NOIZYLAB Slack Bot - App Manifest Deployment"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ ! -f "$MANIFEST_FILE" ]; then
    echo "❌ Manifest file not found: $MANIFEST_FILE"
    exit 1
fi

echo -e "${GREEN}✅ Found manifest file${NC}"
echo ""
echo -e "${CYAN}📋 DEPLOYMENT STEPS:${NC}"
echo ""
echo "1️⃣  I will copy the manifest to your clipboard"
echo ""
echo "2️⃣  Open this URL in your browser:"
echo -e "   ${YELLOW}https://api.slack.com/apps?new_app=1${NC}"
echo ""
echo "3️⃣  Click: 'From an app manifest'"
echo ""
echo "4️⃣  Select: MC96 Digi Universe (or your workspace)"
echo ""
echo "5️⃣  Paste the manifest (Cmd+V)"
echo ""
echo "6️⃣  Click: Next → Create"
echo ""
echo "7️⃣  Get your 3 tokens:"
echo "   • OAuth & Permissions → Bot User OAuth Token (SLACK_BOT_TOKEN)"
echo "   • Basic Information → Signing Secret (SLACK_SIGNING_SECRET)"
echo "   • Basic Information → App-Level Tokens → Generate (SLACK_APP_TOKEN)"
echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if pbcopy is available (macOS)
if command -v pbcopy &> /dev/null; then
    echo -e "${GREEN}📋 Copying manifest to clipboard...${NC}"
    cat "$MANIFEST_FILE" | pbcopy
    echo -e "${GREEN}✅ Manifest copied! Ready to paste.${NC}"
    echo ""
    
    # Offer to open browser
    echo -e "${YELLOW}Would you like to open the Slack app creation page?${NC}"
    echo -n "Press Enter to open, or Ctrl+C to cancel: "
    read -r
    
    # Open URL
    if command -v open &> /dev/null; then
        open "https://api.slack.com/apps?new_app=1"
        echo -e "${GREEN}✅ Browser opened!${NC}"
        echo ""
        echo -e "${YELLOW}Now:${NC}"
        echo "  1. Choose 'From an app manifest'"
        echo "  2. Select workspace"
        echo "  3. Paste (Cmd+V)"
        echo "  4. Click Create"
    fi
else
    echo -e "${YELLOW}📄 Here's the manifest (copy manually):${NC}"
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    cat "$MANIFEST_FILE"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
fi

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}🎯 NEXT STEPS:${NC}"
echo ""
echo "After creating the app:"
echo ""
echo "1. Configure .env with your 3 tokens:"
echo -e "   ${YELLOW}cd ~/NOIZYLAB/slack-bot && nano .env${NC}"
echo ""
echo "2. Add user IDs (right-click user → Copy member ID):"
echo -e "   ${YELLOW}ADMIN_USERS=U01234567${NC}"
echo -e "   ${YELLOW}ALLOWED_USERS=U01234567,U01234568${NC}"
echo ""
echo "3. Run the bot:"
echo -e "   ${YELLOW}npm run dev${NC}"
echo ""
echo "4. Test in Slack:"
echo -e "   ${YELLOW}/disk-status${NC}"
echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${GREEN}📚 For detailed instructions, see:${NC}"
echo -e "   ${CYAN}~/NOIZYLAB/slack-bot/QUICK_SETUP.md${NC}"
echo ""
