#!/bin/zsh
# ============================================================================
# START TIME MACHINE BACKUP - AUTOMATED
# Date: November 19, 2025
# ============================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

echo "${CYAN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo "${CYAN}║          TIME MACHINE BACKUP - AUTOMATED START               ║${NC}"
echo "${CYAN}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if TM_BackUp is mounted
if [[ ! -d "/Volumes/TM_BackUp" ]]; then
    echo "${RED}✗ ERROR: TM_BackUp drive not found${NC}"
    echo "${YELLOW}Please connect the Time Machine backup drive and try again.${NC}"
    exit 1
fi

echo "${GREEN}✓ TM_BackUp drive detected${NC}"
echo ""

# Check available space
echo "${BLUE}Checking available space...${NC}"
df -h /Volumes/TM_BackUp/ | tail -1
echo ""

# Get system size
system_size=$(df -h / | tail -1 | awk '{print $2}')
tm_avail=$(df -h /Volumes/TM_BackUp/ | tail -1 | awk '{print $4}')

echo "${CYAN}System drive size: ${system_size}${NC}"
echo "${CYAN}TM_BackUp available: ${tm_avail}${NC}"
echo ""

# Configure Time Machine
echo "${BLUE}Configuring Time Machine...${NC}"
sudo tmutil setdestination /Volumes/TM_BackUp/

if [[ $? -eq 0 ]]; then
    echo "${GREEN}✓ Time Machine destination set${NC}"
else
    echo "${RED}✗ Failed to set destination${NC}"
    exit 1
fi

# Enable Time Machine
echo "${BLUE}Enabling Time Machine...${NC}"
sudo tmutil enable

echo ""
echo "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "${YELLOW}Starting Time Machine backup...${NC}"
echo "${YELLOW}This will run in the background. Safe to close terminal.${NC}"
echo "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Start backup (non-blocking so it runs in background)
sudo tmutil startbackup &
BACKUP_PID=$!

echo "${GREEN}✓ Backup started (PID: ${BACKUP_PID})${NC}"
echo ""
echo "${CYAN}To monitor progress, run:${NC}"
echo "  tmutil status"
echo ""
echo "${CYAN}To watch in real-time:${NC}"
echo "  watch -n 10 tmutil status"
echo ""
echo "${CYAN}To check when complete:${NC}"
echo "  tmutil latestbackup"
echo ""
echo "${GREEN}✓ You can now let this run overnight!${NC}"
echo ""
