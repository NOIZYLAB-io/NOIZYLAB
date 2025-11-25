#!/bin/bash
#═══════════════════════════════════════════════════════════════════════
#  GORUNFREE DEPLOYMENT SCRIPT
#═══════════════════════════════════════════════════════════════════════

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║           GORUNFREE DEPLOYMENT                            ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GORUNFREE="$SCRIPT_DIR/gorunfree.js"

# Check Node.js
echo -e "${YELLOW}[1/5]${NC} Checking Node.js..."
if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js not found. Install it first.${NC}"
    exit 1
fi
NODE_VERSION=$(node -v)
echo -e "      ${GREEN}✓${NC} Node.js $NODE_VERSION"

# Verify gorunfree.js exists
echo -e "${YELLOW}[2/5]${NC} Verifying gorunfree.js..."
if [ ! -f "$GORUNFREE" ]; then
    echo -e "${RED}❌ gorunfree.js not found at $GORUNFREE${NC}"
    exit 1
fi
echo -e "      ${GREEN}✓${NC} Found at $GORUNFREE"

# Make executable
echo -e "${YELLOW}[3/5]${NC} Setting permissions..."
chmod +x "$GORUNFREE"
echo -e "      ${GREEN}✓${NC} Made executable"

# Syntax check
echo -e "${YELLOW}[4/5]${NC} Syntax check..."
if node --check "$GORUNFREE" 2>/dev/null; then
    echo -e "      ${GREEN}✓${NC} No syntax errors"
else
    echo -e "${RED}❌ Syntax errors found${NC}"
    exit 1
fi

# Test run
echo -e "${YELLOW}[5/5]${NC} Testing..."
VERSION=$(node "$GORUNFREE" version 2>&1)
echo -e "      ${GREEN}✓${NC} $VERSION"

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ DEPLOYMENT SUCCESSFUL${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "Next steps:"
echo -e "  ${CYAN}1.${NC} Install globally:  ${YELLOW}sudo node $GORUNFREE install${NC}"
echo -e "  ${CYAN}2.${NC} Start server:      ${YELLOW}gorunfree server${NC}"
echo -e "  ${CYAN}3.${NC} Send code:         ${YELLOW}gorunfree fix|roast|fast|explain${NC}"
echo ""
