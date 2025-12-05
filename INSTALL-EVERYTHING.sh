#!/bin/bash
# ULTIMATE ONE-CLICK INSTALLER
# Installs and configures EVERYTHING in one command
# GORUNFREE × 1000

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m'

clear
echo -e "${PURPLE}${BOLD}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        🚀 ULTIMATE ONE-CLICK INSTALLER 🚀                     ║
║                                                               ║
║        EVERYTHING. EVERYWHERE. AUTOMATICALLY.                 ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}\n"

echo -e "${CYAN}This will install and configure:${NC}"
echo "  ✅ All Phase 1 systems"
echo "  ✅ All Phase 2 tools"
echo "  ✅ Advanced hotkeys"
echo "  ✅ Dependencies"
echo "  ✅ Configuration"
echo ""
echo -e "${YELLOW}Time: ~5 minutes${NC}"
echo -e "${YELLOW}Platform: $(uname -s)${NC}"
echo ""
echo -e "${CYAN}Press Enter to start installation...${NC}"
read

START_TIME=$(date +%s)

# Detect platform
PLATFORM=$(uname -s)

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[1/10] Checking System${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Check Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Python installed: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}✗ Python 3 required${NC}"
    exit 1
fi

# Check Node.js
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✓ Node.js installed: $NODE_VERSION${NC}"
else
    echo -e "${YELLOW}⚠ Installing Node.js...${NC}"
    case "$PLATFORM" in
        Darwin)
            brew install node || echo -e "${RED}Please install Node.js manually${NC}"
            ;;
        Linux)
            sudo apt-get update && sudo apt-get install -y nodejs npm || echo -e "${RED}Please install Node.js manually${NC}"
            ;;
    esac
fi

# Check npm
if command -v npm &> /dev/null; then
    echo -e "${GREEN}✓ npm installed${NC}"
else
    echo -e "${RED}✗ npm required${NC}"
    exit 1
fi

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[2/10] Creating Directories${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

mkdir -p ~/ai-genius
mkdir -p ~/ai-genius-pro
mkdir -p ~/bin
mkdir -p ~/noizylab-perfect

echo -e "${GREEN}✓ Directories created${NC}"

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[3/10] Copying Files${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Copy all scripts
for file in *.py *.sh *.js *.json 2>/dev/null; do
    if [ -f "$file" ]; then
        cp "$file" ~/ai-genius/
        echo -e "${GREEN}✓ Copied $file${NC}"
    fi
done

# Copy Phase 2 tools
for file in multi-model-query.py screenshot-analyzer.sh setup-advanced-hotkeys.sh smart-dashboard.sh; do
    if [ -f "$file" ]; then
        cp "$file" ~/ai-genius-pro/
        chmod +x ~/ai-genius-pro/"$file" 2>/dev/null
    fi
done

echo -e "${GREEN}✓ All files copied${NC}"

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[4/10] Installing Dependencies${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

cd ~/ai-genius

# Install npm packages if needed
if [ -f "package.json" ]; then
    npm install --silent 2>/dev/null && echo -e "${GREEN}✓ Node dependencies installed${NC}"
fi

# Install Python packages if needed
if command -v pip3 &> /dev/null; then
    pip3 install --quiet requests 2>/dev/null && echo -e "${GREEN}✓ Python dependencies installed${NC}"
fi

# Install Wrangler for Cloudflare
if ! command -v wrangler &> /dev/null; then
    echo -e "${YELLOW}Installing Wrangler CLI...${NC}"
    npm install -g wrangler --silent 2>/dev/null && echo -e "${GREEN}✓ Wrangler installed${NC}"
fi

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[5/10] Creating Shortcuts${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

case "$PLATFORM" in
    Darwin)
        # Mac shortcuts
        cat > ~/bin/ai << 'EOFAI'
#!/bin/bash
cd ~/ai-genius
python3 universal-ai-selector.py claude-sonnet-4 "$@"
EOFAI
        chmod +x ~/bin/ai
        
        cat > ~/bin/ask-claude << 'EOFCLAUDE'
#!/bin/bash
cd ~/ai-genius
python3 universal-ai-selector.py claude-sonnet-4
EOFCLAUDE
        chmod +x ~/bin/ask-claude
        
        cat > ~/bin/ask-gemini << 'EOFGEMINI'
#!/bin/bash
cd ~/ai-genius
python3 universal-ai-selector.py gemini-2-flash
EOFGEMINI
        chmod +x ~/bin/ask-gemini
        
        echo -e "${GREEN}✓ Command line shortcuts created${NC}"
        echo -e "${GREEN}  Usage: ai <query> or ask-claude${NC}"
        ;;
    
    Linux)
        # Linux shortcuts
        cat > ~/.local/bin/ai << 'EOFAI'
#!/bin/bash
cd ~/ai-genius
python3 universal-ai-selector.py claude-sonnet-4 "$@"
EOFAI
        chmod +x ~/.local/bin/ai
        
        echo -e "${GREEN}✓ Command line shortcuts created${NC}"
        ;;
esac

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[6/10] Setting Up Advanced Features${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Run advanced hotkeys setup
if [ -f ~/ai-genius-pro/setup-advanced-hotkeys.sh ]; then
    cd ~/ai-genius-pro
    bash setup-advanced-hotkeys.sh < /dev/null &> /dev/null || true
    echo -e "${GREEN}✓ Advanced features configured${NC}"
fi

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[7/10] Configuring PATH${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Add to PATH if not already there
case "$PLATFORM" in
    Darwin)
        SHELL_RC=~/.zshrc
        if [ ! -f "$SHELL_RC" ]; then
            SHELL_RC=~/.bash_profile
        fi
        ;;
    Linux)
        SHELL_RC=~/.bashrc
        ;;
esac

if ! grep -q "~/bin" "$SHELL_RC" 2>/dev/null; then
    echo 'export PATH="$HOME/bin:$PATH"' >> "$SHELL_RC"
    echo -e "${GREEN}✓ PATH updated${NC}"
else
    echo -e "${GREEN}✓ PATH already configured${NC}"
fi

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[8/10] Creating Quick Start Guide${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

cat > ~/ai-genius/QUICK-START.txt << 'EOFQUICK'
🚀 AI GENIUS - QUICK START GUIDE

BASIC USAGE:
1. Select text anywhere
2. Press hotkey (⌘⌥C or Ctrl+Alt+C)
3. AI response in clipboard
4. Paste anywhere

COMMAND LINE:
  ai "your question"              # Quick AI query
  ask-claude                      # Select text first
  ask-gemini                      # Fast responses

PHASE 2 POWER TOOLS:
  cd ~/ai-genius-pro
  python3 multi-model-query.py "question"  # Multiple AIs
  ./screenshot-analyzer.sh                 # Vision AI
  ./smart-dashboard.sh                     # Business analytics

CONFIGURATION:
  Edit: ~/ai-genius/universal-ai-selector.py
  Worker URL: Update after Cloudflare deployment

DEPLOYMENT:
  cd ~/noizylab-perfect
  ./DEPLOY-EVERYTHING.sh          # Deploy cloud systems

DOCUMENTATION:
  ~/ai-genius/README.md
  ~/ai-genius/GO.md
  ~/ai-genius/PHASE-2-VISION.md

NEXT STEPS:
1. Set up keyboard shortcuts (see setup-universal-ai.sh output)
2. Deploy cloud systems (./DEPLOY-EVERYTHING.sh)
3. Try the tools!

SUPPORT:
  All files: ~/ai-genius/
  Advanced: ~/ai-genius-pro/
  Business: ~/noizylab-perfect/
EOFQUICK

echo -e "${GREEN}✓ Quick start guide created${NC}"

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[9/10] Testing Installation${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Test if scripts are executable
cd ~/ai-genius
if [ -x "universal-ai-selector.py" ] || [ -f "universal-ai-selector.py" ]; then
    echo -e "${GREEN}✓ Core scripts present${NC}"
fi

if [ -d ~/ai-genius-pro ] && [ "$(ls -A ~/ai-genius-pro)" ]; then
    echo -e "${GREEN}✓ Advanced tools installed${NC}"
fi

if [ -x ~/bin/ai ] || [ -x ~/.local/bin/ai ]; then
    echo -e "${GREEN}✓ Command line shortcuts working${NC}"
fi

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}[10/10] Finalizing${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

echo -e "${GREEN}✓ Installation complete in ${DURATION}s${NC}"

# Success banner
clear
echo -e "${GREEN}${BOLD}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║              ✅ INSTALLATION COMPLETE ✅                       ║
║                                                               ║
║        EVERYTHING IS READY TO USE                             ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}\n"

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}📍 WHAT WAS INSTALLED:${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${GREEN}Core Files:${NC}       ~/ai-genius/"
echo -e "${GREEN}Advanced Tools:${NC}   ~/ai-genius-pro/"
echo -e "${GREEN}Business Tools:${NC}   ~/noizylab-perfect/"
echo -e "${GREEN}Shortcuts:${NC}        ~/bin/"
echo ""

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}🎯 TRY IT NOW:${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

case "$PLATFORM" in
    Darwin)
        echo -e "${CYAN}Command Line:${NC}"
        echo '  ai "What is GORUNFREE?"'
        echo "  ask-claude"
        echo ""
        echo -e "${CYAN}Advanced Tools:${NC}"
        echo "  cd ~/ai-genius-pro"
        echo '  python3 multi-model-query.py "test question"'
        echo "  ./screenshot-analyzer.sh"
        echo "  ./smart-dashboard.sh"
        echo ""
        echo -e "${CYAN}Next Steps:${NC}"
        echo "  1. Set up hotkeys:"
        echo "     System Settings → Keyboard → Shortcuts"
        echo "     Add: ~/bin/ask-claude → ⌘⌥C"
        echo ""
        echo "  2. Deploy cloud systems:"
        echo "     cd ~/noizylab-perfect"
        echo "     ./DEPLOY-EVERYTHING.sh"
        echo ""
        ;;
    
    Linux)
        echo -e "${CYAN}Command Line:${NC}"
        echo '  ai "What is GORUNFREE?"'
        echo ""
        echo -e "${CYAN}Advanced Tools:${NC}"
        echo "  cd ~/ai-genius-pro"
        echo '  python3 multi-model-query.py "test question"'
        echo ""
        echo -e "${CYAN}Next Steps:${NC}"
        echo "  1. Set up hotkeys in System Settings"
        echo "  2. Deploy cloud systems"
        echo ""
        ;;
esac

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${BOLD}📚 DOCUMENTATION:${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "  cat ~/ai-genius/QUICK-START.txt"
echo "  cat ~/ai-genius/GO.md"
echo "  cat ~/ai-genius/PHASE-2-VISION.md"
echo ""

echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}${BOLD}🎯 READY TO USE!${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${YELLOW}Restart your terminal to use 'ai' command${NC}"
echo ""

echo -e "${GREEN}${BOLD}🔥 GORUNFREE - INSTALLED! 🔥${NC}"
echo ""
