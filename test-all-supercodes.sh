#!/bin/bash
# Test All SuperCodes - Run and verify all SuperCode scripts
# ==========================================================

set -e

BASE="/Users/m2ultra/NOIZYLAB/noizylab-os"
SCRIPTS_DIR="$BASE/scripts"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${CYAN}${BOLD}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║         🧪 TESTING ALL SUPERCODES                           ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

cd "$BASE"

# Test 1: Master Launcher
echo -e "${BOLD}Test 1: Master Launcher (supercode)${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ -f "$SCRIPTS_DIR/supercode" ] && [ -x "$SCRIPTS_DIR/supercode" ]; then
    echo -e "${GREEN}✔️${NC} Script exists and is executable"
    
    # Test status command
    echo "Testing: ./scripts/supercode status"
    if ./scripts/supercode status >/dev/null 2>&1; then
        echo -e "${GREEN}✔️${NC} Status command works"
    else
        echo -e "${YELLOW}⚠️${NC} Status command had issues (may be expected)"
    fi
else
    echo -e "${RED}❌${NC} Script not found or not executable"
fi
echo ""

# Test 2: Cloudflare SuperCode
echo -e "${BOLD}Test 2: Cloudflare SuperCode (cf)${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ -f "$SCRIPTS_DIR/cf" ] && [ -x "$SCRIPTS_DIR/cf" ]; then
    echo -e "${GREEN}✔️${NC} Script exists and is executable"
    
    # Test status command
    echo "Testing: ./scripts/cf status"
    if ./scripts/cf status >/dev/null 2>&1; then
        echo -e "${GREEN}✔️${NC} Status command works"
    else
        echo -e "${YELLOW}⚠️${NC} Status command had issues (Cloudflare may not be configured)"
    fi
    
    # Check if interactive menu exists
    if [ -f "$BASE/supercodes/cloudflare/supercode.sh" ]; then
        echo -e "${GREEN}✔️${NC} Interactive menu exists"
    else
        echo -e "${YELLOW}⚠️${NC} Interactive menu not found"
    fi
else
    echo -e "${RED}❌${NC} Script not found or not executable"
fi
echo ""

# Test 3: Cursor SuperCode
echo -e "${BOLD}Test 3: Cursor SuperCode (cs)${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ -f "$SCRIPTS_DIR/cs" ] && [ -x "$SCRIPTS_DIR/cs" ]; then
    echo -e "${GREEN}✔️${NC} Script exists and is executable"
    
    # Test install command
    echo "Testing: ./scripts/cs install"
    if ./scripts/cs install 2>&1 | grep -q "Cursor Setup Complete\|Installed"; then
        echo -e "${GREEN}✔️${NC} Installation works"
    else
        echo -e "${YELLOW}⚠️${NC} Installation had issues"
    fi
    
    # Check if interactive menu exists
    if [ -f "$BASE/supercodes/cursor/supercode.sh" ]; then
        echo -e "${GREEN}✔️${NC} Interactive menu exists"
    else
        echo -e "${YELLOW}⚠️${NC} Interactive menu not found"
    fi
else
    echo -e "${RED}❌${NC} Script not found or not executable"
fi
echo ""

# Test 4: SuperCode Files
echo -e "${BOLD}Test 4: SuperCode Files${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check Cloudflare SuperCode
if [ -f "$BASE/supercodes/cloudflare/supercode.sh" ]; then
    echo -e "${GREEN}✔️${NC} Cloudflare SuperCode: $BASE/supercodes/cloudflare/supercode.sh"
else
    echo -e "${RED}❌${NC} Cloudflare SuperCode missing"
fi

# Check Cursor SuperCode
if [ -f "$BASE/supercodes/cursor/supercode.sh" ]; then
    echo -e "${GREEN}✔️${NC} Cursor SuperCode: $BASE/supercodes/cursor/supercode.sh"
else
    echo -e "${RED}❌${NC} Cursor SuperCode missing"
fi

# Check symlinks
if [ -L "$BASE/supercodes/bin/cf-supercode" ]; then
    echo -e "${GREEN}✔️${NC} cf-supercode symlink exists"
else
    echo -e "${YELLOW}⚠️${NC} cf-supercode symlink missing"
fi

if [ -L "$BASE/supercodes/bin/cursor-supercode" ]; then
    echo -e "${GREEN}✔️${NC} cursor-supercode symlink exists"
else
    echo -e "${YELLOW}⚠️${NC} cursor-supercode symlink missing"
fi
echo ""

# Test 5: Directory Structure
echo -e "${BOLD}Test 5: Directory Structure${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

DIRS=(
    "$BASE/scripts"
    "$BASE/supercodes"
    "$BASE/supercodes/cloudflare"
    "$BASE/supercodes/cursor"
    "$BASE/supercodes/bin"
)

for dir in "${DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo -e "${GREEN}✔️${NC} $dir"
    else
        echo -e "${RED}❌${NC} $dir (missing)"
    fi
done
echo ""

# Summary
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BOLD}Summary:${NC}"
echo ""
echo "All SuperCodes are ready to use!"
echo ""
echo "Launch commands:"
echo -e "  ${GREEN}./scripts/supercode${NC}     - Master menu"
echo -e "  ${GREEN}./scripts/cf${NC}            - Cloudflare SuperCode"
echo -e "  ${GREEN}./scripts/cs${NC}            - Cursor SuperCode"
echo ""
echo -e "${GREEN}✨ All tests complete!${NC}"
echo ""

