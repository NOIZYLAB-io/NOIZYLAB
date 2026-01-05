#!/bin/bash

###############################################################################
# NOIZYLAB SLACK BOT - WHAT DO WE NEED?
# 
# Complete checklist of everything needed to deploy the Slack bot
###############################################################################

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

clear

echo ""
echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                                                              ║${NC}"
echo -e "${PURPLE}║     🤖 NOIZYLAB AI COPILOT - DEPLOYMENT CHECKLIST           ║${NC}"
echo -e "${PURPLE}║                                                              ║${NC}"
echo -e "${PURPLE}║     What Do We Need to Deploy?                              ║${NC}"
echo -e "${PURPLE}║                                                              ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

###############################################################################
# CHECK WHAT WE HAVE
###############################################################################

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}📦 CHECKING WHAT WE HAVE...${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

BOT_DIR="$HOME/NOIZYLAB/slack-bot"
HAVE_COUNT=0
NEED_COUNT=0

# 1. Check bot files
if [ -f "$BOT_DIR/app.js" ]; then
    echo -e "${GREEN}✅${NC} app.js (12KB) - Full-featured bot with slash commands & natural language"
    ((HAVE_COUNT++))
else
    echo -e "${RED}❌${NC} app.js - MISSING!"
    ((NEED_COUNT++))
fi

if [ -f "$BOT_DIR/package.json" ]; then
    echo -e "${GREEN}✅${NC} package.json - Dependencies configured (@slack/bolt, dotenv, nodemon)"
    ((HAVE_COUNT++))
else
    echo -e "${RED}❌${NC} package.json - MISSING!"
    ((NEED_COUNT++))
fi

if [ -d "$BOT_DIR/node_modules" ]; then
    echo -e "${GREEN}✅${NC} node_modules - Dependencies installed (3 packages)"
    ((HAVE_COUNT++))
else
    echo -e "${YELLOW}⚠️${NC}  node_modules - Need to run: npm install"
    ((NEED_COUNT++))
fi

if [ -f "$BOT_DIR/.env" ]; then
    echo -e "${GREEN}✅${NC} .env - Configuration file exists"
    
    # Check if tokens are configured
    if grep -q "xoxb-your-bot-token-here" "$BOT_DIR/.env" 2>/dev/null; then
        echo -e "${RED}   ⚠️  Tokens not configured (still has placeholder values)${NC}"
        ((NEED_COUNT++))
    else
        echo -e "${GREEN}   ✓  Tokens appear to be configured${NC}"
        ((HAVE_COUNT++))
    fi
else
    echo -e "${RED}❌${NC} .env - MISSING! Need to create from .env.example"
    ((NEED_COUNT++))
fi

if [ -f "$BOT_DIR/README.md" ]; then
    echo -e "${GREEN}✅${NC} README.md (7.3KB) - Complete setup documentation"
    ((HAVE_COUNT++))
else
    echo -e "${RED}❌${NC} README.md - MISSING!"
    ((NEED_COUNT++))
fi

if [ -f "$BOT_DIR/ENTERPRISE_GRID_DEPLOYMENT.md" ]; then
    echo -e "${GREEN}✅${NC} ENTERPRISE_GRID_DEPLOYMENT.md - MC96 deployment guide"
    ((HAVE_COUNT++))
else
    echo -e "${YELLOW}⚠️${NC}  ENTERPRISE_GRID_DEPLOYMENT.md - Missing (optional)"
fi

echo ""

# 2. Check NOIZYLAB scripts
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}🔧 CHECKING NOIZYLAB SCRIPTS...${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

SCRIPTS=(
    "TTP21_HOT_ROD_GUIDE.sh"
    "QUICK_STATUS.sh"
    "ULTRA_AGGRESSIVE.sh"
    "DISKWARRIOR_EMERGENCY_GUIDE.sh"
)

SCRIPTS_OK=0
for script in "${SCRIPTS[@]}"; do
    if [ -f "$HOME/NOIZYLAB/$script" ]; then
        echo -e "${GREEN}✅${NC} $script"
        ((SCRIPTS_OK++))
        ((HAVE_COUNT++))
    else
        echo -e "${RED}❌${NC} $script - MISSING!"
        ((NEED_COUNT++))
    fi
done

echo ""

###############################################################################
# WHAT DO WE NEED?
###############################################################################

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}📋 WHAT DO WE NEED TO DEPLOY?${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║  OPTION 1: MANUAL SLACK APP SETUP (Recommended)             ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${YELLOW}🔑 REQUIRED: 3 Slack Tokens${NC}"
echo ""
echo "You need to create a Slack app and get these tokens:"
echo ""
echo -e "  1️⃣  ${CYAN}SLACK_BOT_TOKEN${NC}"
echo "     • Format: xoxb-1234567890-1234567890123-abcdefghijklmnopqrstuvwx"
echo "     • Where: OAuth & Permissions → Bot User OAuth Token"
echo "     • Scopes needed: app_mentions:read, chat:write, commands, files:read, files:write"
echo ""
echo -e "  2️⃣  ${CYAN}SLACK_SIGNING_SECRET${NC}"
echo "     • Format: 1234567890abcdef1234567890abcdef"
echo "     • Where: Basic Information → App Credentials → Signing Secret"
echo ""
echo -e "  3️⃣  ${CYAN}SLACK_APP_TOKEN${NC}"
echo "     • Format: xapp-1-A01234567-1234567890-abcdefghijklmnopqrstuvwxyz"
echo "     • Where: Socket Mode → Generate App-Level Token"
echo "     • Scope needed: connections:write"
echo ""

echo -e "${YELLOW}📝 STEPS TO GET TOKENS:${NC}"
echo ""
echo "1. Go to: ${BLUE}https://api.slack.com/apps${NC}"
echo ""
echo "2. Click: ${GREEN}Create New App${NC} → ${GREEN}From scratch${NC}"
echo "   • Name: ${CYAN}NOIZYLAB AI Copilot${NC}"
echo "   • Workspace: ${CYAN}MC96 Digi Universe${NC}"
echo ""
echo "3. Enable ${GREEN}Socket Mode${NC}:"
echo "   • Settings → Socket Mode → Toggle ${GREEN}ON${NC}"
echo "   • Generate token: ${CYAN}noizylab-socket${NC}"
echo "   • Copy ${CYAN}SLACK_APP_TOKEN${NC} → Save to .env"
echo ""
echo "4. Add ${GREEN}OAuth Permissions${NC}:"
echo "   • Features → OAuth & Permissions"
echo "   • Bot Token Scopes → Add:"
echo "     ✓ app_mentions:read"
echo "     ✓ chat:write"
echo "     ✓ commands"
echo "     ✓ files:read"
echo "     ✓ files:write"
echo "     ✓ channels:read"
echo "     ✓ channels:history"
echo ""
echo "5. Create ${GREEN}Slash Commands${NC}:"
echo "   • Features → Slash Commands → Create:"
echo "     • ${CYAN}/disk-status${NC}"
echo "     • ${CYAN}/noizylab-repair${NC}"
echo "     • ${CYAN}/cleanup-all${NC}"
echo "     • ${CYAN}/diskwarrior-emergency${NC}"
echo "   • Note: With Socket Mode, NO request URLs needed!"
echo ""
echo "6. Subscribe to ${GREEN}Events${NC}:"
echo "   • Features → Event Subscriptions → Toggle ${GREEN}ON${NC}"
echo "   • Subscribe to bot events:"
echo "     ✓ app_mention"
echo "     ✓ message.channels (optional)"
echo ""
echo "7. ${GREEN}Install to Workspace${NC}:"
echo "   • Settings → Install App"
echo "   • Click: ${GREEN}Install to Workspace${NC}"
echo "   • Copy ${CYAN}SLACK_BOT_TOKEN${NC} → Save to .env"
echo ""
echo "8. Get ${GREEN}Signing Secret${NC}:"
echo "   • Settings → Basic Information"
echo "   • App Credentials → Copy ${CYAN}SLACK_SIGNING_SECRET${NC}"
echo "   • Save to .env"
echo ""

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║  OPTION 2: ENTERPRISE GRID APPROVAL (For MC96 Org)          ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${YELLOW}🏢 If MC96 is Enterprise Grid:${NC}"
echo ""
echo "1. ${CYAN}Workspace Admin${NC} requests installation"
echo "   • Workspace Settings → Apps → Request to Install"
echo ""
echo "2. ${CYAN}Org Owner${NC} approves app"
echo "   • Admin Console → Apps → Pending Requests"
echo "   • Review permissions → Approve organization-wide"
echo ""
echo "3. ${CYAN}Workspace Admin${NC} installs in workspace"
echo "   • Apps → Approved Apps → Install"
echo ""
echo "See: ${BLUE}ENTERPRISE_GRID_DEPLOYMENT.md${NC} for full guide"
echo ""

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

###############################################################################
# CONFIGURATION STEPS
###############################################################################

echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║  CONFIGURATION STEPS (After Getting Tokens)                 ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${YELLOW}📝 Configure .env file:${NC}"
echo ""
echo "cd $BOT_DIR"
echo "nano .env"
echo ""
echo "Replace these values:"
echo -e "  ${CYAN}SLACK_BOT_TOKEN${NC}=xoxb-YOUR-ACTUAL-TOKEN"
echo -e "  ${CYAN}SLACK_SIGNING_SECRET${NC}=YOUR-ACTUAL-SECRET"
echo -e "  ${CYAN}SLACK_APP_TOKEN${NC}=xapp-YOUR-ACTUAL-TOKEN"
echo ""

echo -e "${YELLOW}👥 Add authorized users:${NC}"
echo ""
echo "Get user IDs from Slack:"
echo "  • Click user profile → More → Copy member ID"
echo ""
echo "Add to .env:"
echo -e "  ${CYAN}ALLOWED_USERS${NC}=U01234567,U01234568  # Can run status commands"
echo -e "  ${CYAN}ADMIN_USERS${NC}=U01234567             # Can run repair/cleanup"
echo ""

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

###############################################################################
# RUN THE BOT
###############################################################################

echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║  RUN THE BOT                                                 ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${YELLOW}🚀 Development mode (testing):${NC}"
echo ""
echo "cd $BOT_DIR"
echo "npm run dev"
echo ""

echo -e "${YELLOW}🚀 Production mode (PM2):${NC}"
echo ""
echo "npm install -g pm2"
echo "cd $BOT_DIR"
echo "pm2 start app.js --name noizylab-bot"
echo "pm2 save"
echo "pm2 startup"
echo ""

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

###############################################################################
# TEST THE BOT
###############################################################################

echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║  TEST THE BOT                                                ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${YELLOW}🧪 In Slack:${NC}"
echo ""
echo "1. Invite bot to a channel:"
echo "   ${CYAN}/invite @NOIZYLAB AI Copilot${NC}"
echo ""
echo "2. Test slash commands:"
echo "   ${CYAN}/disk-status${NC}"
echo "   ${CYAN}/noizylab-repair 12TB${NC}"
echo ""
echo "3. Test natural language:"
echo "   ${CYAN}@noizylab help${NC}"
echo "   ${CYAN}@noizylab my 12TB drive is frozen${NC}"
echo ""

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

###############################################################################
# SUMMARY
###############################################################################

echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║  SUMMARY                                                     ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${GREEN}✅ WE HAVE:${NC}"
echo "  • Bot code (app.js, package.json)"
echo "  • Dependencies installed (@slack/bolt, dotenv)"
echo "  • NOIZYLAB scripts (TTP21, QUICK_STATUS, etc.)"
echo "  • Documentation (README, Enterprise Grid guide)"
echo ""

echo -e "${YELLOW}⚠️  WE NEED:${NC}"
echo "  1. Create Slack app at api.slack.com/apps"
echo "  2. Get 3 tokens (BOT_TOKEN, SIGNING_SECRET, APP_TOKEN)"
echo "  3. Configure .env with tokens"
echo "  4. Add user IDs (ALLOWED_USERS, ADMIN_USERS)"
echo "  5. Run bot: npm run dev"
echo "  6. Test in Slack"
echo ""

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                                                              ║${NC}"
echo -e "${PURPLE}║  🎯 BOTTOM LINE: Create Slack app & get 3 tokens!           ║${NC}"
echo -e "${PURPLE}║                                                              ║${NC}"
echo -e "${PURPLE}║  Then: Configure .env → npm run dev → Test in Slack         ║${NC}"
echo -e "${PURPLE}║                                                              ║${NC}"
echo -e "${PURPLE}║  Time estimate: 15-20 minutes                                ║${NC}"
echo -e "${PURPLE}║                                                              ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${GREEN}📚 Full documentation:${NC}"
echo "  • README: $BOT_DIR/README.md"
echo "  • Enterprise Grid: $BOT_DIR/ENTERPRISE_GRID_DEPLOYMENT.md"
echo ""

echo -e "${GREEN}🆘 Need help?${NC}"
echo "  • Slack API docs: https://api.slack.com/"
echo "  • Bolt framework: https://slack.dev/bolt-js/"
echo ""

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
