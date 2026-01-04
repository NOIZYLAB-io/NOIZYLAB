#!/bin/bash
# ==============================================================================
# GORUNFREE MASTER - THE REAL ONE
# Built: 2026-01-04
# Author: Claude + Rob Plowman
#
# ONE COMMAND. EVERYTHING EXECUTES. NO BULLSHIT.
# ==============================================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NOIZYLAB_ROOT="$(dirname "$SCRIPT_DIR")"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${PURPLE}⚡ GORUNFREE MASTER${NC}"
echo -e "${PURPLE}   $(date '+%Y-%m-%d %H:%M:%S')${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════════${NC}"
echo ""

# -----------------------------------------------------------------------------
# PHASE 1: SYSTEM OPTIMIZATION
# -----------------------------------------------------------------------------
echo -e "${CYAN}[1/5] OPTIMIZING SYSTEM...${NC}"

# Kill CPU hogs (Chrome helpers, Adobe bloat)
BLOAT_KILLED=0
for proc in "Chrome Helper" "Adobe" "Creative Cloud" "Dropbox" "OneDrive"; do
    if pgrep -f "$proc" > /dev/null 2>&1; then
        pkill -f "$proc" 2>/dev/null && ((BLOAT_KILLED++)) || true
    fi
done
echo -e "      ${GREEN}✓${NC} Killed $BLOAT_KILLED bloat processes"

# Clear disk cache (works on macOS)
sudo purge 2>/dev/null && echo -e "      ${GREEN}✓${NC} Disk cache flushed" || echo -e "      ${YELLOW}⚠${NC} Purge needs sudo"

# -----------------------------------------------------------------------------
# PHASE 2: VERIFY INFRASTRUCTURE
# -----------------------------------------------------------------------------
echo -e "${CYAN}[2/5] VERIFYING INFRASTRUCTURE...${NC}"

# Check noizy.ai
NOIZY_STATUS=$(curl -s -m 5 https://noizy.ai/ 2>/dev/null) || NOIZY_STATUS="TIMEOUT"
if echo "$NOIZY_STATUS" | grep -q "HEAVEN"; then
    VERSION=$(echo "$NOIZY_STATUS" | grep -o '"version":[0-9]*' | cut -d':' -f2)
    echo -e "      ${GREEN}✓${NC} noizy.ai ONLINE (v${VERSION})"
else
    echo -e "      ${RED}✗${NC} noizy.ai OFFLINE"
fi

# Check heaven subdomain
HEAVEN_CODE=$(curl -s -m 5 -o /dev/null -w "%{http_code}" https://heaven.noizy.ai/ 2>/dev/null)
if [ "$HEAVEN_CODE" = "200" ]; then
    echo -e "      ${GREEN}✓${NC} heaven.noizy.ai ONLINE"
else
    echo -e "      ${YELLOW}⚠${NC} heaven.noizy.ai status $HEAVEN_CODE (needs fix)"
fi

# -----------------------------------------------------------------------------
# PHASE 3: SYNC STATE
# -----------------------------------------------------------------------------
echo -e "${CYAN}[3/5] SYNCING STATE...${NC}"

# Check if archive is running
if pgrep -f "rsync.*CODEMASTER" > /dev/null 2>&1; then
    echo -e "      ${YELLOW}⚠${NC} Archive transfer in progress"
else
    echo -e "      ${GREEN}✓${NC} No pending transfers"
fi

# Git status
cd "$NOIZYLAB_ROOT"
if git status --porcelain | grep -q .; then
    CHANGES=$(git status --porcelain | wc -l | tr -d ' ')
    echo -e "      ${YELLOW}⚠${NC} $CHANGES uncommitted changes in NOIZYLAB"
else
    echo -e "      ${GREEN}✓${NC} NOIZYLAB repo clean"
fi

# -----------------------------------------------------------------------------
# PHASE 4: MEMORY CHECK
# -----------------------------------------------------------------------------
echo -e "${CYAN}[4/5] CHECKING RESOURCES...${NC}"

# Disk space
DISK_FREE=$(df -h / | tail -1 | awk '{print $4}')
echo -e "      ${GREEN}✓${NC} Disk free: $DISK_FREE"

# Memory pressure
MEM_FREE=$(memory_pressure 2>/dev/null | grep "System-wide memory free percentage" | awk '{print $5}') || MEM_FREE="N/A"
echo -e "      ${GREEN}✓${NC} Memory free: $MEM_FREE"

# Top CPU process
TOP_PROC=$(ps aux | sort -nrk 3 | head -2 | tail -1 | awk '{print $11}' | xargs basename 2>/dev/null) || TOP_PROC="unknown"
TOP_CPU=$(ps aux | sort -nrk 3 | head -2 | tail -1 | awk '{print $3}')
echo -e "      ${BLUE}ℹ${NC} Top CPU: $TOP_PROC (${TOP_CPU}%)"

# -----------------------------------------------------------------------------
# PHASE 5: READY STATE
# -----------------------------------------------------------------------------
echo -e "${CYAN}[5/5] ENTERING FLOW STATE...${NC}"

# Log this session
echo "$(date '+%Y-%m-%d %H:%M:%S') - GORUNFREE executed" >> "$NOIZYLAB_ROOT/logs/gorunfree.log"
echo -e "      ${GREEN}✓${NC} Session logged"

# Final status
echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ GORUNFREE COMPLETE${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "   ${CYAN}AGENTS:${NC}      GABRIEL, SHIRL, POPS, ENGR_KEITH, DREAM"
echo -e "   ${CYAN}SYSTEM:${NC}      M2 Ultra @ $MEM_FREE memory free"
echo -e "   ${CYAN}STATUS:${NC}      Ready for flow"
echo ""
echo -e "   ${YELLOW}TODAY'S MISSION:${NC}"
echo -e "   → Record Anthropic Fellows video"
echo -e "   → Fix heaven.noizy.ai (status $HEAVEN_CODE)"
echo -e "   → Complete CODEMASTER archive"
echo ""
echo -e "${PURPLE}🔥 GORUNFREE - ONE COMMAND. EVERYTHING EXECUTES.${NC}"
echo ""
