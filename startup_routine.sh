#!/bin/bash
# FISH MUSIC INC - STARTUP ROUTINE
# Run this every time you start working
# Auto-optimizes everything for maximum FLOW
# Created by CB_01 for ROB - GORUNFREE! 🎸🔥

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

clear

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                                                                ║"
echo "║         🎸 FISH MUSIC INC - STARTUP ROUTINE 🎸                 ║"
echo "║                                                                ║"
echo "║              Preparing your system for FLOW...                 ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

sleep 1

# Run quick status
echo "⚡ Running quick status check..."
"$SCRIPT_DIR/quick_status.sh"

echo ""
echo "🎯 Ready to create!"
echo ""
echo "Quick Commands:"
echo "  Launch:  cd ~/CB-01-FISHMUSICINC && ./LAUNCH_FISHMUSICINC.sh"
echo "  Design:  python3 projects/design-reunion/DESIGN_REUNION_TRACKER.py"
echo "  Music:   python3 ai/metadata-scanner/find_all_music.py"
echo ""
echo "GORUNFREE! 🎸🔥"
echo ""

