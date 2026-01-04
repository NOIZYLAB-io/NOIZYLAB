#!/bin/bash

###############################################################################
# NOIZYLAB SLACK BOT - QUICK SETUP
# 
# Automated setup script for NOIZYLAB AI Copilot Slack bot
# Installs dependencies, configures environment, and provides setup instructions
#
# Usage: bash ~/NOIZYLAB/SETUP_SLACK_BOT.sh
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

# Config
BOT_DIR="$HOME/NOIZYLAB/slack-bot"
SCRIPTS_DIR="$HOME/NOIZYLAB"

echo ""
echo -e "${PURPLE}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                                                          ║${NC}"
echo -e "${PURPLE}║        🤖 NOIZYLAB AI COPILOT - SLACK BOT SETUP         ║${NC}"
echo -e "${PURPLE}║                                                          ║${NC}"
echo -e "${PURPLE}║    AI-Powered Disk Repair & Monitoring for Slack        ║${NC}"
echo -e "${PURPLE}║                                                          ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""

###############################################################################
# STEP 1: CHECK PREREQUISITES
###############################################################################

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}STEP 1: Checking Prerequisites${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check Node.js
if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js not found${NC}"
    echo -e "${YELLOW}Installing Node.js via Homebrew...${NC}"
    brew install node
else
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✅ Node.js installed:${NC} $NODE_VERSION"
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo -e "${RED}❌ npm not found${NC}"
    exit 1
else
    NPM_VERSION=$(npm --version)
    echo -e "${GREEN}✅ npm installed:${NC} $NPM_VERSION"
fi

# Check ngrok (optional for testing)
if ! command -v ngrok &> /dev/null; then
    echo -e "${YELLOW}⚠️  ngrok not found (optional for local testing)${NC}"
    echo -e "${YELLOW}   Install with: brew install ngrok/ngrok/ngrok${NC}"
else
    echo -e "${GREEN}✅ ngrok installed${NC}"
fi

echo ""

###############################################################################
# STEP 2: INSTALL DEPENDENCIES
###############################################################################

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}STEP 2: Installing Dependencies${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

cd "$BOT_DIR"

if [ -d "node_modules" ]; then
    echo -e "${YELLOW}⚠️  node_modules exists, removing...${NC}"
    rm -rf node_modules package-lock.json
fi

echo -e "${BLUE}📦 Installing npm packages...${NC}"
npm install

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Dependencies installed successfully${NC}"
else
    echo -e "${RED}❌ Failed to install dependencies${NC}"
    exit 1
fi

echo ""

###############################################################################
# STEP 3: VERIFY NOIZYLAB SCRIPTS
###############################################################################

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}STEP 3: Verifying NOIZYLAB Scripts${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check critical scripts
SCRIPTS=(
    "TTP21_HOT_ROD_GUIDE.sh"
    "QUICK_STATUS.sh"
    "ULTRA_AGGRESSIVE.sh"
    "DISKWARRIOR_EMERGENCY_GUIDE.sh"
)

for script in "${SCRIPTS[@]}"; do
    SCRIPT_PATH="$SCRIPTS_DIR/$script"
    if [ -f "$SCRIPT_PATH" ]; then
        echo -e "${GREEN}✅${NC} $script"
        # Make executable if not already
        chmod +x "$SCRIPT_PATH"
    else
        echo -e "${RED}❌${NC} $script ${RED}(MISSING!)${NC}"
    fi
done

echo ""

###############################################################################
# STEP 4: CONFIGURE ENVIRONMENT
###############################################################################

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}STEP 4: Environment Configuration${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [ -f "$BOT_DIR/.env" ]; then
    echo -e "${YELLOW}⚠️  .env file already exists${NC}"
    echo -e "${YELLOW}   Backing up to .env.backup...${NC}"
    cp "$BOT_DIR/.env" "$BOT_DIR/.env.backup"
fi

echo -e "${BLUE}📝 Creating .env from template...${NC}"
cp "$BOT_DIR/.env.example" "$BOT_DIR/.env"

echo -e "${GREEN}✅ .env file created${NC}"
echo ""
echo -e "${YELLOW}⚠️  IMPORTANT: You need to configure your Slack tokens!${NC}"
echo ""
echo -e "${CYAN}Edit .env file:${NC}"
echo -e "  nano $BOT_DIR/.env"
echo ""
echo -e "${CYAN}Or use VS Code:${NC}"
echo -e "  code $BOT_DIR/.env"
echo ""

###############################################################################
# STEP 5: SLACK APP SETUP INSTRUCTIONS
###############################################################################

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}STEP 5: Slack App Setup Instructions${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${PURPLE}🔧 CREATE SLACK APP:${NC}"
echo -e "1. Go to: ${BLUE}https://api.slack.com/apps${NC}"
echo -e "2. Click: ${GREEN}Create New App${NC} → ${GREEN}From scratch${NC}"
echo -e "3. Name: ${CYAN}NOIZYLAB AI Copilot${NC}"
echo -e "4. Workspace: ${CYAN}MC96 Digi Universe${NC}"
echo ""

echo -e "${PURPLE}🔌 ENABLE SOCKET MODE:${NC}"
echo -e "1. Go to: ${CYAN}Socket Mode${NC} in app settings"
echo -e "2. Toggle: ${GREEN}Enable Socket Mode${NC} ON"
echo -e "3. Generate: ${GREEN}App-Level Token${NC} (name: noizylab-socket)"
echo -e "4. Copy token → Add to .env as ${YELLOW}SLACK_APP_TOKEN${NC}"
echo ""

echo -e "${PURPLE}🔐 BOT PERMISSIONS:${NC}"
echo -e "Go to: ${CYAN}OAuth & Permissions${NC} → Add Bot Token Scopes:"
echo -e "  • ${GREEN}app_mentions:read${NC} - Detect @noizylab mentions"
echo -e "  • ${GREEN}chat:write${NC} - Post messages"
echo -e "  • ${GREEN}commands${NC} - Slash commands"
echo -e "  • ${GREEN}files:read${NC} - Read status files"
echo -e "  • ${GREEN}files:write${NC} - Save reports"
echo -e "  • ${GREEN}channels:read${NC} - List channels"
echo -e "  • ${GREEN}channels:history${NC} - Read messages"
echo ""

echo -e "${PURPLE}⚡ SLASH COMMANDS:${NC}"
echo -e "Go to: ${CYAN}Slash Commands${NC} → Create these commands:"
echo -e "  • ${CYAN}/disk-status${NC} - Quick health check"
echo -e "  • ${CYAN}/noizylab-repair${NC} - TechTool Pro 21 hot rod repair"
echo -e "  • ${CYAN}/cleanup-all${NC} - Aggressive cleanup"
echo -e "  • ${CYAN}/diskwarrior-emergency${NC} - DiskWarrior backup repair"
echo ""
echo -e "${YELLOW}Note: With Socket Mode, you don't need Request URLs!${NC}"
echo ""

echo -e "${PURPLE}📡 EVENT SUBSCRIPTIONS:${NC}"
echo -e "Go to: ${CYAN}Event Subscriptions${NC} → Subscribe to bot events:"
echo -e "  • ${GREEN}app_mention${NC} - Respond to @noizylab mentions"
echo -e "  • ${GREEN}message.channels${NC} - Listen to channels (optional)"
echo ""

echo -e "${PURPLE}🚀 INSTALL TO WORKSPACE:${NC}"
echo -e "1. Go to: ${CYAN}Install App${NC}"
echo -e "2. Click: ${GREEN}Install to Workspace${NC}"
echo -e "3. Authorize permissions"
echo -e "4. Copy ${YELLOW}Bot User OAuth Token${NC} → Add to .env as ${YELLOW}SLACK_BOT_TOKEN${NC}"
echo ""

###############################################################################
# STEP 6: QUICK START
###############################################################################

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}STEP 6: Quick Start${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${GREEN}Once you've configured .env with your tokens:${NC}"
echo ""
echo -e "${PURPLE}📝 EDIT CONFIG:${NC}"
echo -e "  nano $BOT_DIR/.env"
echo ""

echo -e "${PURPLE}🚀 RUN BOT (Development):${NC}"
echo -e "  cd $BOT_DIR"
echo -e "  npm run dev"
echo ""

echo -e "${PURPLE}🚀 RUN BOT (Production):${NC}"
echo -e "  cd $BOT_DIR"
echo -e "  npm start"
echo ""

echo -e "${PURPLE}🧪 TEST COMMANDS:${NC}"
echo -e "  In Slack:"
echo -e "    ${CYAN}/disk-status${NC}"
echo -e "    ${CYAN}@noizylab help${NC}"
echo -e "    ${CYAN}@noizylab my 12TB drive is frozen${NC}"
echo ""

###############################################################################
# STEP 7: NEXT STEPS
###############################################################################

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}STEP 7: Next Steps${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${GREEN}✅ Bot files created:${NC}"
echo -e "  📄 $BOT_DIR/package.json"
echo -e "  📄 $BOT_DIR/app.js"
echo -e "  📄 $BOT_DIR/.env.example"
echo -e "  📄 $BOT_DIR/.env (needs tokens)"
echo -e "  📄 $BOT_DIR/README.md"
echo -e "  📄 $BOT_DIR/.gitignore"
echo ""

echo -e "${YELLOW}⚠️  TODO:${NC}"
echo -e "  1️⃣  Configure Slack tokens in .env"
echo -e "  2️⃣  Create Slack app at https://api.slack.com/apps"
echo -e "  3️⃣  Enable Socket Mode (no public endpoint needed!)"
echo -e "  4️⃣  Add slash commands & event subscriptions"
echo -e "  5️⃣  Install app to MC96 Digi Universe workspace"
echo -e "  6️⃣  Run bot: ${CYAN}npm run dev${NC}"
echo -e "  7️⃣  Test in Slack: ${CYAN}/disk-status${NC}"
echo ""

echo -e "${GREEN}📚 Documentation:${NC}"
echo -e "  📖 README: $BOT_DIR/README.md"
echo -e "  📖 Enterprise Guide: $SCRIPTS_DIR/SLACK_ENTERPRISE_GUIDE.md"
echo -e "  📖 Slack Bolt Docs: https://slack.dev/bolt-js/"
echo ""

echo -e "${PURPLE}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                                                          ║${NC}"
echo -e "${PURPLE}║        ✨ PHINEAS POTTS STANDARD: MAGICAL! ✨           ║${NC}"
echo -e "${PURPLE}║                                                          ║${NC}"
echo -e "${PURPLE}║    🚗 "Good enough" is NOT acceptable. Only            ║${NC}"
echo -e "${PURPLE}║       MAGICAL performance will do!                      ║${NC}"
echo -e "${PURPLE}║                                                          ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
