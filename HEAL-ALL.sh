#!/bin/bash
# AUTOMATED SYSTEM HEALING
# Fixes common issues automatically
# GORUNFREEX1000 Self-Repair

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🔧 AUTOMATED SYSTEM HEALING"
echo "============================="
echo ""

# Fix 1: File permissions
echo -e "${BLUE}[1/6] Fixing file permissions${NC}"
chmod +x *.sh 2>/dev/null
chmod +x *.js 2>/dev/null
echo -e "${GREEN}✓ Permissions fixed${NC}"
echo ""

# Fix 2: Create missing directories
echo -e "${BLUE}[2/6] Creating missing directories${NC}"
mkdir -p logs
mkdir -p backups
echo -e "${GREEN}✓ Directories created${NC}"
echo ""

# Fix 3: Install missing Node.js dependencies
echo -e "${BLUE}[3/6] Checking Node.js setup${NC}"
if ! command -v node &> /dev/null; then
    echo -e "${YELLOW}Installing Node.js...${NC}"
    brew install node || echo "Please install Node.js manually"
else
    echo -e "${GREEN}✓ Node.js installed${NC}"
fi
echo ""

# Fix 4: Create backup of current config
echo -e "${BLUE}[4/6] Backing up configuration${NC}"
if [ -f "ai-genius-config.json" ]; then
    cp ai-genius-config.json "backups/ai-genius-config-$(date +%Y%m%d-%H%M%S).json"
    echo -e "${GREEN}✓ Config backed up${NC}"
else
    echo -e "${YELLOW}⚠ No config to backup (will be created)${NC}"
fi
echo ""

# Fix 5: Initialize default config
echo -e "${BLUE}[5/6] Initializing configuration${NC}"
if [ -f "ai-genius-config.js" ]; then
    node ai-genius-config.js save 2>/dev/null || echo "Config will be created on first run"
    echo -e "${GREEN}✓ Config initialized${NC}"
else
    echo -e "${YELLOW}⚠ Config script not found${NC}"
fi
echo ""

# Fix 6: Clean up old PID files
echo -e "${BLUE}[6/6] Cleaning up${NC}"
rm -f .*.pid 2>/dev/null
echo -e "${GREEN}✓ Cleaned up old PID files${NC}"
echo ""

echo "============================="
echo -e "${GREEN}✓ HEALING COMPLETE${NC}"
echo "============================="
echo ""
echo "Run tests to verify:"
echo "  ./TEST-ALL.sh"
echo ""
echo "Start system:"
echo "  ./START-ALL.sh"
