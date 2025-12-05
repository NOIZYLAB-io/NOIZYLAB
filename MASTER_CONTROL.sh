#!/bin/bash
# MASTER_CONTROL.sh
# Master control panel for all systems

clear

CODE_MASTER="/Volumes/4TB_02/CODE_MASTER"

cat << 'EOF'
╔══════════════════════════════════════════════════════════════════════╗
║     🎛️  MASTER CONTROL PANEL X1000                                    ║
╚══════════════════════════════════════════════════════════════════════╝
EOF

echo ""
echo "📊 System Status:"
df -h / | tail -1 | awk '{print "   System: " $4 " free (" $5 " used)"}'
df -h /Volumes/4TB_02 2>/dev/null | tail -1 | awk '{print "   External: " $4 " free (" $5 " used)"}'
echo ""

echo "🎛️  Control Options:"
echo ""
echo "   1) 🚀 WARP SPEED START (All Systems)"
echo "   2) ⚡ HYPER DRIVE UPGRADE"
echo "   3) 🧠 SMART UPGRADER"
echo "   4) ⚡ POWER OPTIMIZER"
echo "   5) 🧠 INTELLIGENT MOVER"
echo "   6) 📊 DASHBOARD"
echo "   7) 🏥 HEALTH CHECK"
echo "   8) 📈 PERFORMANCE MONITOR"
echo "   9) 🔄 CONTINUOUS IMPROVER (Background)"
echo "  10) 📋 SCRIPT INDEX"
echo "   0) ❌ Exit"
echo ""

read -p "Select option: " choice

case $choice in
    1) bash "$CODE_MASTER/WARP_SPEED_START.sh" ;;
    2) bash "$CODE_MASTER/scripts/HYPER_DRIVE_UPGRADE_X1000.sh" ;;
    3) bash "$CODE_MASTER/scripts/SMART_UPGRADER_X1000.sh" ;;
    4) bash "$CODE_MASTER/scripts/POWER_OPTIMIZER_X1000.sh" ;;
    5) bash "$CODE_MASTER/scripts/INTELLIGENT_MOVER_X1000.sh" ;;
    6) bash "$CODE_MASTER/DASHBOARD.sh" ;;
    7) bash "$CODE_MASTER/scripts/HEALTH_CHECK_X1000.sh" ;;
    8) bash "$CODE_MASTER/scripts/PERFORMANCE_MONITOR_X1000.sh" ;;
    9) nohup bash "$CODE_MASTER/scripts/CONTINUOUS_IMPROVER_X1000.sh" > /dev/null 2>&1 & echo "✅ Continuous improver started in background" ;;
   10) cat "$CODE_MASTER/SCRIPT_INDEX.md" | less ;;
    0) exit 0 ;;
    *) echo "❌ Invalid option" ;;
esac

