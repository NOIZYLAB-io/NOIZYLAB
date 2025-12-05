#!/bin/bash
# Master Upgrade Script - Upgrade ALL NoizyLab Tools
# ===================================================

set -e

BASE="/Users/m2ultra/NOIZYLAB"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${CYAN}${BOLD}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║         🚀 MASTER UPGRADE - All NoizyLab Tools              ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Upgrade Universal Blocker
echo -e "${BOLD}1. Upgrading Universal Blocker...${NC}"
cd "$BASE/universal-blocker"
if [ -f "setup-blocker-v2.sh" ]; then
    ./setup-blocker-v2.sh --auto-setup 2>&1 | head -10
    echo -e "${GREEN}✔️${NC} Universal Blocker V2 ready"
else
    echo -e "${BLUE}→${NC} V2 already exists"
fi
echo ""

# Upgrade iMessage Spam Filter
echo -e "${BOLD}2. Upgrading iMessage Spam Filter...${NC}"
cd "$BASE/imessage-spam-filter"
if [ -f "imessage-spam-filter-v2.sh" ]; then
    echo -e "${GREEN}✔️${NC} iMessage Spam Filter V2 ready"
    echo "   Run: ./imessage-spam-filter-v2.sh"
else
    echo -e "${BLUE}→${NC} V2 already exists"
fi
echo ""

# Upgrade SuperCodes
echo -e "${BOLD}3. Checking SuperCodes...${NC}"
cd "$BASE/noizylab-os"
if [ -d "supercodes" ]; then
    echo -e "${GREEN}✔️${NC} SuperCodes ready"
    echo "   Run: ./scripts/supercode"
else
    echo -e "${BLUE}→${NC} SuperCodes already set up"
fi
echo ""

# Create unified launcher
echo -e "${BOLD}4. Creating Unified Launcher...${NC}"
cat > "$BASE/launch" << 'LAUNCHER'
#!/bin/bash
# NoizyLab Unified Launcher

BASE="/Users/m2ultra/NOIZYLAB"

echo "NoizyLab Tools:"
echo "  1) Universal Blocker V2"
echo "  2) iMessage Spam Filter V2"
echo "  3) SuperCodes"
echo "  4) All Tools Status"
echo ""
read -p "Choice: " choice

case "$choice" in
    1) cd "$BASE/universal-blocker" && ./setup-blocker-v2.sh ;;
    2) cd "$BASE/imessage-spam-filter" && ./imessage-spam-filter-v2.sh ;;
    3) cd "$BASE/noizylab-os" && ./scripts/supercode ;;
    4)
        echo "Status:"
        [ -f "$BASE/universal-blocker/setup-blocker-v2.sh" ] && echo "  ✔️ Universal Blocker V2" || echo "  ❌ Missing"
        [ -f "$BASE/imessage-spam-filter/imessage-spam-filter-v2.sh" ] && echo "  ✔️ iMessage Filter V2" || echo "  ❌ Missing"
        [ -d "$BASE/noizylab-os/supercodes" ] && echo "  ✔️ SuperCodes" || echo "  ❌ Missing"
        ;;
esac
LAUNCHER

chmod +x "$BASE/launch"
echo -e "${GREEN}✔️${NC} Unified launcher created: ~/NOIZYLAB/launch"
echo ""

echo -e "${GREEN}✨ All upgrades complete!${NC}"
echo ""
echo "Quick access:"
echo "  ~/NOIZYLAB/launch          - Unified launcher"
echo "  ~/NOIZYLAB/universal-blocker/setup-blocker-v2.sh"
echo "  ~/NOIZYLAB/imessage-spam-filter/imessage-spam-filter-v2.sh"
echo "  ~/NOIZYLAB/noizylab-os/scripts/supercode"
echo ""

