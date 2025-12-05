#!/bin/bash
# FISH MUSIC INC - DAILY OPTIMIZER
# HARD RULE #20: Automatic daily optimization
# Run this every morning or as cron job
# Created by CB_01 for ROB - GORUNFREE! 🎸🔥

set -e

echo ""
echo "🔥 FISH MUSIC INC - DAILY OPTIMIZER"
echo "═══════════════════════════════════════════════════════════════"
echo "HARD RULE #20: Daily health check, clean, heal, optimize"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 1. Check network optimization
echo -e "${BLUE}[1/7] Checking network...${NC}"
CURRENT_MTU=$(ifconfig en0 | grep mtu | awk '{print $4}')
if [ "$CURRENT_MTU" -eq 9000 ]; then
    echo -e "   ${GREEN}✅ HOT ROD MODE active (MTU 9000)${NC}"
else
    echo -e "   ${YELLOW}⚠️  MTU not optimized - run: sudo ./mc96_optimize.sh${NC}"
fi

# 2. Check DNS
echo -e "${BLUE}[2/7] Checking DNS...${NC}"
if scutil --dns | grep -q "1.1.1.1"; then
    echo -e "   ${GREEN}✅ Cloudflare DNS active${NC}"
else
    echo -e "   ${YELLOW}⚠️  DNS not optimal - run: sudo bash ~/Downloads/FIX-DNS-NOW.sh${NC}"
fi

# 3. Check disk space
echo -e "${BLUE}[3/7] Checking disk space...${NC}"
DISK_USAGE=$(df -h / | tail -1 | awk '{print $5}' | sed 's/%//')
if [ "$DISK_USAGE" -lt 80 ]; then
    echo -e "   ${GREEN}✅ Disk space healthy (${DISK_USAGE}% used)${NC}"
else
    echo -e "   ${YELLOW}⚠️  Disk space high (${DISK_USAGE}% used)${NC}"
fi

# 4. Check git status
echo -e "${BLUE}[4/7] Checking Git status...${NC}"
cd "$SCRIPT_DIR/../.."
if git status --porcelain | grep -q .; then
    UNCOMMITTED=$(git status --porcelain | wc -l | xargs)
    echo -e "   ${YELLOW}⚠️  $UNCOMMITTED uncommitted changes${NC}"
else
    echo -e "   ${GREEN}✅ Git clean - all committed${NC}"
fi

# 5. Check mounted volumes
echo -e "${BLUE}[5/7] Checking volumes...${NC}"
VOLUME_COUNT=$(ls /Volumes/ 2>/dev/null | wc -l | xargs)
echo -e "   ${GREEN}✅ $VOLUME_COUNT volumes mounted${NC}"
if ls /Volumes/ 2>/dev/null | grep -q "4TB Lacie"; then
    echo -e "   ${GREEN}✅ 4TB Lacie mounted (Design 2025 stems!)${NC}"
fi

# 6. Run master dashboard
echo -e "${BLUE}[6/7] System status check...${NC}"
cd "$SCRIPT_DIR"
python3 master_dashboard.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "   ${GREEN}✅ All systems operational${NC}"
else
    echo -e "   ${YELLOW}⚠️  Check master dashboard${NC}"
fi

# 7. Clean temporary files
echo -e "${BLUE}[7/7] Cleaning temporary files...${NC}"
find "$SCRIPT_DIR/../.." -name "*.pyc" -delete 2>/dev/null
find "$SCRIPT_DIR/../.." -name "__pycache__" -type d -delete 2>/dev/null
find "$SCRIPT_DIR/../.." -name ".DS_Store" -delete 2>/dev/null
echo -e "   ${GREEN}✅ Cleaned temporary files${NC}"

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo -e "${GREEN}✅ DAILY OPTIMIZATION COMPLETE!${NC}"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "📊 Quick Commands:"
echo "   ./LAUNCH_FISHMUSICINC.sh              # Master control"
echo "   python3 master_dashboard.py            # Full dashboard"
echo "   sudo ./mc96_optimize.sh                # Optimize network"
echo ""
echo "GORUNFREE! 🎸🔥"

