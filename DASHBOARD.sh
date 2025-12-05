#!/bin/bash
# Master Dashboard

clear

CODE_MASTER="/Volumes/4TB_02/CODE_MASTER"

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║     📊 CODE_MASTER DASHBOARD X1000                                    ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

echo "💾 Disk Space:"
echo "   System Drive:"
df -h / | tail -1 | awk '{print "      Free: " $4 " / Total: " $2 " (" $5 " used)"}'
echo "   External Drive:"
df -h /Volumes/4TB_02 2>/dev/null | tail -1 | awk '{print "      Free: " $4 " / Total: " $2 " (" $5 " used)"}'
echo ""

echo "📂 CODE_MASTER:"
du -sh "$CODE_MASTER" 2>/dev/null | awk '{print "   Size: " $1}'
SCRIPT_COUNT=$(find "$CODE_MASTER/scripts" -name "*.sh" 2>/dev/null | wc -l | xargs)
echo "   Scripts: $SCRIPT_COUNT"
echo ""

echo "🔄 Auto-Heal Status:"
ps aux | grep -q "AUTOHEAL_WARP_SPEED" && echo "   ✅ Active" || echo "   ⚠️  Not running"
echo ""

echo "📋 Quick Actions:"
echo "   1) Start WARP SPEED"
echo "   2) Run Health Check"
echo "   3) Performance Monitor"
echo "   4) View Script Index"
echo "   0) Exit"
echo ""

read -p "Select: " choice

case $choice in
    1) bash "$CODE_MASTER/WARP_SPEED_START.sh" ;;
    2) bash "$CODE_MASTER/scripts/HEALTH_CHECK_X1000.sh" ;;
    3) bash "$CODE_MASTER/scripts/PERFORMANCE_MONITOR_X1000.sh" ;;
    4) cat "$CODE_MASTER/SCRIPT_INDEX.md" | less ;;
    0) exit 0 ;;
esac
