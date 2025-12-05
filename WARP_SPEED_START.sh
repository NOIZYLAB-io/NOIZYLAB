#!/bin/bash
# WARP_SPEED_START.sh
# Start everything at WARP SPEED!

clear

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║     ⚡ WARP SPEED HYPER DRIVE - STARTING ALL                          ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

CODE_MASTER="/Volumes/4TB_02/CODE_MASTER"

# Run Ultimate Master first
echo "🚀 Running Ultimate Master..."
bash "$CODE_MASTER/ULTIMATE_MASTER_X1000.sh"

echo ""
echo "⚡ Running Hyper Drive Upgrade..."
bash "$CODE_MASTER/scripts/HYPER_DRIVE_UPGRADE_X1000.sh"

echo ""
echo "🌍 Starting Auto-Heal System..."
echo "   (Running in background - check logs for status)"
nohup bash "$CODE_MASTER/scripts/AUTOHEAL_WARP_SPEED_X1000.sh" > /dev/null 2>&1 &

echo ""
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║     ✅ WARP SPEED SYSTEM ACTIVE!                                      ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""
echo "📊 System Status:"
df -h / | tail -1
df -h /Volumes/4TB_02 2>/dev/null | tail -1
echo ""
echo "✅ All systems running at WARP SPEED!"

