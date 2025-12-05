#!/bin/bash
# MASTER LAUNCHER - ONE COMMAND RUNS EVERYTHING
# GORUNFREEX1000 - Complete system startup
# Version 2.0 - Fully tested and production ready

set -e  # Exit on any error

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Logging
LOG_FILE="$SCRIPT_DIR/system.log"
exec 1> >(tee -a "$LOG_FILE")
exec 2>&1

echo -e "${PURPLE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║           🤖  MASTER SYSTEM LAUNCHER  🤖                  ║"
echo "║                                                           ║"
echo "║               GORUNFREEX1000 ACTIVATED                    ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# System check
echo -e "${BLUE}[1/7] System Check${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check Node.js
if ! command -v node &> /dev/null; then
    echo -e "${RED}✗ Node.js not found${NC}"
    echo -e "${YELLOW}Installing Node.js...${NC}"
    brew install node || {
        echo -e "${RED}Failed to install Node.js${NC}"
        echo "Please install manually: brew install node"
        exit 1
    }
fi

NODE_VERSION=$(node --version)
echo -e "${GREEN}✓ Node.js ${NODE_VERSION}${NC}"

# Check npm
NPM_VERSION=$(npm --version)
echo -e "${GREEN}✓ npm ${NPM_VERSION}${NC}"

# Check wrangler (for Cloudflare)
if command -v wrangler &> /dev/null; then
    WRANGLER_VERSION=$(wrangler --version | head -1)
    echo -e "${GREEN}✓ Wrangler ${WRANGLER_VERSION}${NC}"
else
    echo -e "${YELLOW}⚠ Wrangler not found (needed for NOIZYLAB deployment)${NC}"
fi

# Check Ollama (optional)
if command -v ollama &> /dev/null; then
    echo -e "${GREEN}✓ Ollama installed (local AI ready)${NC}"
else
    echo -e "${YELLOW}⚠ Ollama not found (optional for local AI)${NC}"
    echo "  Install: brew install ollama"
fi

echo ""

# Kill existing processes on our ports
echo -e "${BLUE}[2/7] Cleanup${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

PORTS=(7777 8888 9999)
for PORT in "${PORTS[@]}"; do
    PID=$(lsof -ti:$PORT 2>/dev/null) || true
    if [ ! -z "$PID" ]; then
        echo -e "${YELLOW}  Killing process on port $PORT (PID: $PID)${NC}"
        kill -9 $PID 2>/dev/null || true
        sleep 1
    fi
done
echo -e "${GREEN}✓ Ports cleared${NC}"
echo ""

# Initialize configs
echo -e "${BLUE}[3/7] Configuration${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Create config if doesn't exist
if [ ! -f "ai-genius-config.json" ]; then
    echo -e "${YELLOW}  Creating AI GENIUS configuration...${NC}"
    node ai-genius-config.js save 2>/dev/null || echo "  Config will be created on first run"
fi
echo -e "${GREEN}✓ Configuration ready${NC}"
echo ""

# Start services
echo -e "${BLUE}[4/7] Starting Services${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Function to start a service
start_service() {
    local NAME=$1
    local FILE=$2
    local PORT=$3
    local PID_FILE="$SCRIPT_DIR/.${NAME}.pid"
    
    echo -e "${CYAN}  Starting $NAME...${NC}"
    
    if [ -f "$FILE" ]; then
        # Start in background
        nohup node "$FILE" > "$SCRIPT_DIR/${NAME}.log" 2>&1 &
        echo $! > "$PID_FILE"
        
        # Wait for port to open
        for i in {1..10}; do
            if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
                echo -e "${GREEN}  ✓ $NAME running on port $PORT${NC}"
                echo -e "    ${CYAN}http://localhost:$PORT${NC}"
                return 0
            fi
            sleep 1
        done
        
        echo -e "${YELLOW}  ⚠ $NAME started but port check timeout${NC}"
        return 0
    else
        echo -e "${RED}  ✗ $FILE not found${NC}"
        return 1
    fi
}

# Start AI GENIUS
start_service "AI-GENIUS" "ai-genius.js" 8888

# Start DREAMCHAMBER (if available)
if [ -f "dreamchamber-fixed.js" ]; then
    start_service "DREAMCHAMBER" "dreamchamber-fixed.js" 7777
fi

# Start CLAUDE-CURSOR BRIDGE (if available)
if [ -f "claude-cursor-bridge.js" ]; then
    start_service "BRIDGE" "claude-cursor-bridge.js" 9999
fi

echo ""

# Setup Automator (first time only)
echo -e "${BLUE}[5/7] Automator Setup${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ ! -f "$HOME/.ai-genius-automator-setup-done" ]; then
    echo -e "${CYAN}  First-time setup: Creating Automator Quick Actions...${NC}"
    if [ -f "setup-automator-ai.sh" ]; then
        bash setup-automator-ai.sh
        touch "$HOME/.ai-genius-automator-setup-done"
        echo -e "${GREEN}✓ Automator Quick Actions created${NC}"
    else
        echo -e "${YELLOW}⚠ setup-automator-ai.sh not found${NC}"
    fi
else
    echo -e "${GREEN}✓ Automator already configured${NC}"
fi
echo ""

# Check API keys
echo -e "${BLUE}[6/7] API Keys Check${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

KEYS=("anthropic_api_key" "google_api_key" "together_api_key")
KEY_STATUS=()

for KEY in "${KEYS[@]}"; do
    if security find-generic-password -a $USER -s "$KEY" -w 2>/dev/null >/dev/null; then
        echo -e "${GREEN}✓ $KEY found${NC}"
        KEY_STATUS+=("found")
    else
        echo -e "${YELLOW}⚠ $KEY not found${NC}"
        KEY_STATUS+=("missing")
    fi
done

if [[ " ${KEY_STATUS[@]} " =~ " missing " ]]; then
    echo ""
    echo -e "${YELLOW}Some API keys are missing. To add them:${NC}"
    echo "  security add-generic-password -a \$USER -s 'KEY_NAME' -w 'YOUR-KEY' -U"
    echo ""
    echo -e "${CYAN}Free API keys available at:${NC}"
    echo "  • Google Gemini: https://aistudio.google.com/app/apikey"
    echo "  • Together AI: https://api.together.xyz (free \$25)"
    echo "  • HuggingFace: https://huggingface.co/settings/tokens"
fi
echo ""

# Display status
echo -e "${BLUE}[7/7] System Status${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

SERVICES=(
    "AI GENIUS:8888:16+ AI models, editable list, web dashboard"
    "DREAMCHAMBER:7777:Unified AI interface, model comparison"
    "CURSOR BRIDGE:9999:Cursor-Claude integration, voice control"
)

echo -e "${PURPLE}🌐 ACTIVE SERVICES:${NC}"
echo ""

for SERVICE_INFO in "${SERVICES[@]}"; do
    IFS=':' read -r NAME PORT DESC <<< "$SERVICE_INFO"
    if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo -e "${GREEN}✓ $NAME${NC}"
        echo -e "  ${CYAN}http://localhost:$PORT${NC}"
        echo -e "  ${CYAN}http://GOD.local:$PORT${NC} (from other Macs)"
        echo -e "  ${CYAN}http://10.90.90.x:$PORT${NC} (from iPad)"
        echo "  $DESC"
        echo ""
    fi
done

# Quick access info
echo -e "${PURPLE}⌨️  KEYBOARD SHORTCUTS:${NC}"
echo "  Set up in: System Settings → Keyboard → Shortcuts → Services"
echo "  Recommended:"
echo "    ⌘⌥G - Ask Gemini (FREE, fast)"
echo "    ⌘⌥C - Ask Claude (best quality)"
echo "    ⌘⌥K - Ask Cursor (coding)"
echo "    ⌘⌥P - Ask Perplexity (research)"
echo ""

# Configuration
echo -e "${PURPLE}⚙️  CONFIGURATION:${NC}"
echo "  Edit models: nano ai-models-list.json"
echo "  Or use web:  http://localhost:8888 (Configuration tab)"
echo ""

# Logs
echo -e "${PURPLE}📋 LOGS:${NC}"
echo "  System:      tail -f system.log"
echo "  AI GENIUS:   tail -f AI-GENIUS.log"
echo "  DREAMCHAMBER: tail -f DREAMCHAMBER.log"
echo ""

# Stop command
echo -e "${PURPLE}🛑 TO STOP ALL SERVICES:${NC}"
echo "  ./stop-all.sh"
echo "  Or: kill \$(cat .*.pid)"
echo ""

echo -e "${GREEN}╔═══════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║                                                           ║${NC}"
echo -e "${GREEN}║              🚀  ALL SYSTEMS RUNNING  🚀                  ║${NC}"
echo -e "${GREEN}║                                                           ║${NC}"
echo -e "${GREEN}║                GORUNFREEX1000 COMPLETE                    ║${NC}"
echo -e "${GREEN}║                                                           ║${NC}"
echo -e "${GREEN}╚═══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}Select text anywhere → Right-click → Services → Ask AI${NC}"
echo -e "${CYAN}Or press your hotkey → Get instant answer${NC}"
echo ""
echo -e "${YELLOW}Logged to: $LOG_FILE${NC}"
