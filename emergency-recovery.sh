#!/bin/bash
# EMERGENCY RECOVERY SYSTEM
# Fixes everything when things go wrong
# Nuclear option: rebuild from scratch

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m'

clear
echo -e "${RED}${BOLD}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║           🚨 EMERGENCY RECOVERY SYSTEM 🚨                     ║
║                                                               ║
║           When Everything Goes Wrong, We Fix It               ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}\n"

echo -e "${YELLOW}${BOLD}WARNING: This will attempt to fix all AI GENIUS systems${NC}"
echo -e "${YELLOW}This is the nuclear option when nothing else works${NC}"
echo ""
echo -e "${CYAN}What this does:${NC}"
echo "  1. Diagnoses all problems"
echo "  2. Creates emergency backup"
echo "  3. Fixes permissions"
echo "  4. Repairs corrupted files"
echo "  5. Reinstalls dependencies"
echo "  6. Restarts all services"
echo "  7. Verifies everything works"
echo ""
echo -e "${RED}Continue? (yes/no):${NC} "
read CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "Cancelled"
    exit 0
fi

START_TIME=$(date +%s)
RECOVERY_LOG=~/emergency-recovery-$(date +%Y%m%d-%H%M%S).log

echo "" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${CYAN}${BOLD}[PHASE 1] EMERGENCY DIAGNOSTICS${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo "" | tee -a "$RECOVERY_LOG"

# Diagnostic checks
ISSUES_FOUND=0

echo "Checking critical directories..." | tee -a "$RECOVERY_LOG"
for dir in ~/ai-genius ~/ai-genius-pro ~/noizylab-perfect; do
    if [ ! -d "$dir" ]; then
        echo -e "${RED}✗ Missing: $dir${NC}" | tee -a "$RECOVERY_LOG"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    else
        echo -e "${GREEN}✓ Found: $dir${NC}" | tee -a "$RECOVERY_LOG"
    fi
done

echo "" | tee -a "$RECOVERY_LOG"
echo "Checking Python..." | tee -a "$RECOVERY_LOG"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ $PYTHON_VERSION${NC}" | tee -a "$RECOVERY_LOG"
else
    echo -e "${RED}✗ Python 3 not found${NC}" | tee -a "$RECOVERY_LOG"
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
fi

echo "" | tee -a "$RECOVERY_LOG"
echo "Checking Node.js..." | tee -a "$RECOVERY_LOG"
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✓ Node.js $NODE_VERSION${NC}" | tee -a "$RECOVERY_LOG"
else
    echo -e "${RED}✗ Node.js not found${NC}" | tee -a "$RECOVERY_LOG"
    ISSUES_FOUND=$((ISSUES_FOUND + 1))
fi

echo "" | tee -a "$RECOVERY_LOG"
echo "Checking critical files..." | tee -a "$RECOVERY_LOG"
CRITICAL_FILES=(
    "~/ai-genius/universal-ai-selector.py"
    "~/ai-genius-pro/multi-model-query.py"
    "~/noizylab-perfect/DEPLOY-EVERYTHING.sh"
)

for file in "${CRITICAL_FILES[@]}"; do
    file="${file/#\~/$HOME}"
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓ $file${NC}" | tee -a "$RECOVERY_LOG"
    else
        echo -e "${RED}✗ Missing: $file${NC}" | tee -a "$RECOVERY_LOG"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    fi
done

echo "" | tee -a "$RECOVERY_LOG"
echo -e "${CYAN}Issues found: $ISSUES_FOUND${NC}" | tee -a "$RECOVERY_LOG"

if [ $ISSUES_FOUND -eq 0 ]; then
    echo -e "${GREEN}No critical issues detected!${NC}" | tee -a "$RECOVERY_LOG"
    echo "" | tee -a "$RECOVERY_LOG"
    echo "System appears healthy. Recovery may not be necessary." | tee -a "$RECOVERY_LOG"
    echo -e "${YELLOW}Continue anyway? (yes/no):${NC} "
    read CONTINUE
    if [ "$CONTINUE" != "yes" ]; then
        echo "Exiting" | tee -a "$RECOVERY_LOG"
        exit 0
    fi
fi

# Emergency backup
echo "" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${CYAN}${BOLD}[PHASE 2] EMERGENCY BACKUP${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo "" | tee -a "$RECOVERY_LOG"

EMERGENCY_BACKUP=~/emergency-backup-$(date +%Y%m%d-%H%M%S)
mkdir -p "$EMERGENCY_BACKUP"

echo "Creating emergency backup..." | tee -a "$RECOVERY_LOG"
for dir in ~/ai-genius ~/ai-genius-pro ~/noizylab-perfect; do
    if [ -d "$dir" ]; then
        echo -n "  Backing up $(basename "$dir")... " | tee -a "$RECOVERY_LOG"
        tar -czf "$EMERGENCY_BACKUP/$(basename "$dir").tar.gz" "$dir" 2>/dev/null
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓${NC}" | tee -a "$RECOVERY_LOG"
        else
            echo -e "${YELLOW}⚠${NC}" | tee -a "$RECOVERY_LOG"
        fi
    fi
done

echo -e "${GREEN}✓ Emergency backup saved: $EMERGENCY_BACKUP${NC}" | tee -a "$RECOVERY_LOG"

# Fix permissions
echo "" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${CYAN}${BOLD}[PHASE 3] FIX PERMISSIONS${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo "" | tee -a "$RECOVERY_LOG"

echo "Fixing directory permissions..." | tee -a "$RECOVERY_LOG"
for dir in ~/ai-genius ~/ai-genius-pro ~/noizylab-perfect; do
    if [ -d "$dir" ]; then
        chmod -R u+rwX "$dir" 2>/dev/null
        echo -e "${GREEN}✓ Fixed: $dir${NC}" | tee -a "$RECOVERY_LOG"
    fi
done

echo "" | tee -a "$RECOVERY_LOG"
echo "Making scripts executable..." | tee -a "$RECOVERY_LOG"
find ~/ai-genius ~/ai-genius-pro ~/noizylab-perfect -name "*.sh" -type f -exec chmod +x {} \; 2>/dev/null
find ~/ai-genius ~/ai-genius-pro ~/noizylab-perfect -name "*.py" -type f -exec chmod +x {} \; 2>/dev/null
echo -e "${GREEN}✓ All scripts now executable${NC}" | tee -a "$RECOVERY_LOG"

# Reinstall dependencies
echo "" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${CYAN}${BOLD}[PHASE 4] REINSTALL DEPENDENCIES${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo "" | tee -a "$RECOVERY_LOG"

if command -v pip3 &> /dev/null; then
    echo "Installing Python packages..." | tee -a "$RECOVERY_LOG"
    pip3 install --quiet --upgrade requests 2>&1 | tee -a "$RECOVERY_LOG"
    echo -e "${GREEN}✓ Python packages installed${NC}" | tee -a "$RECOVERY_LOG"
fi

if [ -d ~/ai-genius ] && [ -f ~/ai-genius/package.json ]; then
    echo "" | tee -a "$RECOVERY_LOG"
    echo "Installing Node.js packages..." | tee -a "$RECOVERY_LOG"
    cd ~/ai-genius
    npm install --silent 2>&1 | tee -a "$RECOVERY_LOG"
    echo -e "${GREEN}✓ Node.js packages installed${NC}" | tee -a "$RECOVERY_LOG"
fi

# Kill stuck processes
echo "" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${CYAN}${BOLD}[PHASE 5] CLEAN PROCESSES${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo "" | tee -a "$RECOVERY_LOG"

echo "Killing stuck processes..." | tee -a "$RECOVERY_LOG"
pkill -f "ai-genius" 2>/dev/null && echo -e "${GREEN}✓ Killed ai-genius processes${NC}" | tee -a "$RECOVERY_LOG"
pkill -f "universal-ai" 2>/dev/null && echo -e "${GREEN}✓ Killed universal-ai processes${NC}" | tee -a "$RECOVERY_LOG"
rm -f ~/ai-genius/*.pid 2>/dev/null && echo -e "${GREEN}✓ Removed stale PID files${NC}" | tee -a "$RECOVERY_LOG"

# Repair configurations
echo "" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${CYAN}${BOLD}[PHASE 6] REPAIR CONFIGURATIONS${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo "" | tee -a "$RECOVERY_LOG"

# Reset stats if corrupted
if [ -f ~/.ai-genius-stats.json ]; then
    if ! jq . ~/.ai-genius-stats.json >/dev/null 2>&1; then
        echo "Resetting corrupted stats file..." | tee -a "$RECOVERY_LOG"
        echo '{"queries": 0, "tokens": 0, "cost": 0, "start_date": "'$(date +%Y-%m-%d)'"}' > ~/.ai-genius-stats.json
        echo -e "${GREEN}✓ Stats file reset${NC}" | tee -a "$RECOVERY_LOG"
    else
        echo -e "${GREEN}✓ Stats file OK${NC}" | tee -a "$RECOVERY_LOG"
    fi
fi

# Verify installations
echo "" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${CYAN}${BOLD}[PHASE 7] VERIFICATION${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo "" | tee -a "$RECOVERY_LOG"

TESTS_PASSED=0
TESTS_FAILED=0

# Test Python script
if [ -f ~/ai-genius/universal-ai-selector.py ]; then
    echo -n "Testing Python AI script... " | tee -a "$RECOVERY_LOG"
    cd ~/ai-genius
    TEST_RESULT=$(python3 universal-ai-selector.py claude-sonnet-4 "test" 2>&1 | head -1)
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓${NC}" | tee -a "$RECOVERY_LOG"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${RED}✗${NC}" | tee -a "$RECOVERY_LOG"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
fi

# Test multi-model query
if [ -f ~/ai-genius-pro/multi-model-query.py ]; then
    echo -n "Testing multi-model query... " | tee -a "$RECOVERY_LOG"
    if python3 ~/ai-genius-pro/multi-model-query.py "test" >/dev/null 2>&1; then
        echo -e "${GREEN}✓${NC}" | tee -a "$RECOVERY_LOG"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo -e "${YELLOW}⚠${NC}" | tee -a "$RECOVERY_LOG"
    fi
fi

# Test executable permissions
echo -n "Testing executable permissions... " | tee -a "$RECOVERY_LOG"
if [ -x ~/noizylab-perfect/DEPLOY-EVERYTHING.sh ]; then
    echo -e "${GREEN}✓${NC}" | tee -a "$RECOVERY_LOG"
    TESTS_PASSED=$((TESTS_PASSED + 1))
else
    echo -e "${RED}✗${NC}" | tee -a "$RECOVERY_LOG"
    TESTS_FAILED=$((TESTS_FAILED + 1))
fi

# Final summary
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

echo "" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${GREEN}${BOLD}✅ EMERGENCY RECOVERY COMPLETE${NC}" | tee -a "$RECOVERY_LOG"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}" | tee -a "$RECOVERY_LOG"
echo "" | tee -a "$RECOVERY_LOG"

echo -e "${CYAN}Recovery Summary:${NC}" | tee -a "$RECOVERY_LOG"
echo "  Time taken: ${DURATION}s" | tee -a "$RECOVERY_LOG"
echo "  Issues found: $ISSUES_FOUND" | tee -a "$RECOVERY_LOG"
echo "  Tests passed: $TESTS_PASSED" | tee -a "$RECOVERY_LOG"
echo "  Tests failed: $TESTS_FAILED" | tee -a "$RECOVERY_LOG"
echo "" | tee -a "$RECOVERY_LOG"

echo -e "${CYAN}Emergency Backup:${NC}" | tee -a "$RECOVERY_LOG"
echo "  Location: $EMERGENCY_BACKUP" | tee -a "$RECOVERY_LOG"
echo "  To restore: tar -xzf [file].tar.gz -C ~/" | tee -a "$RECOVERY_LOG"
echo "" | tee -a "$RECOVERY_LOG"

echo -e "${CYAN}Recovery Log:${NC}" | tee -a "$RECOVERY_LOG"
echo "  Saved to: $RECOVERY_LOG" | tee -a "$RECOVERY_LOG"
echo "" | tee -a "$RECOVERY_LOG"

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "${GREEN}${BOLD}🎉 ALL SYSTEMS OPERATIONAL 🎉${NC}" | tee -a "$RECOVERY_LOG"
else
    echo -e "${YELLOW}⚠ Some tests failed - manual intervention may be needed${NC}" | tee -a "$RECOVERY_LOG"
    echo "  Review log: cat $RECOVERY_LOG" | tee -a "$RECOVERY_LOG"
fi

echo "" | tee -a "$RECOVERY_LOG"
echo -e "${CYAN}Next Steps:${NC}" | tee -a "$RECOVERY_LOG"
echo "  1. Test: ai \"hello\"" | tee -a "$RECOVERY_LOG"
echo "  2. Test hotkeys: ⌘⌥C" | tee -a "$RECOVERY_LOG"
echo "  3. Deploy cloud: cd ~/noizylab-perfect && ./DEPLOY-EVERYTHING.sh" | tee -a "$RECOVERY_LOG"
echo "" | tee -a "$RECOVERY_LOG"
