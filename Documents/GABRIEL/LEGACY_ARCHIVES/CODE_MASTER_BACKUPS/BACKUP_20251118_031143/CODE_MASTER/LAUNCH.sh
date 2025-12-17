#!/bin/bash
# CODE_MASTER QUICK LAUNCHER
# Quick access to all tools

echo "╔════════════════════════════════════════════════════╗"
echo "║  CODE_MASTER QUICK LAUNCHER                        ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""
echo "Select an option:"
echo "  1) Health Check"
echo "  2) Auto Optimize"
echo "  3) Scan GHOST Drive"
echo "  4) Fix VS Code Terminal"
echo "  5) Monitor System"
echo "  6) View Logs"
echo "  7) Exit"
echo ""
read -p "Choice: " choice

case $choice in
    1) bash "$HOME/CODE_MASTER/scripts/HEALTH_CHECK.sh" ;;
    2) bash "$HOME/CODE_MASTER/scripts/AUTO_OPTIMIZE.sh" ;;
    3) bash "$HOME/CODE_MASTER/scripts/FIX_GHOST_DRIVE.sh" ;;
    4) pwsh "$HOME/CODE_MASTER/scripts/FIX_VSCODE_TERMINAL_CORRUPTION.ps1" ;;
    5) bash "$HOME/CODE_MASTER/scripts/MONITOR_SYSTEM.sh" ;;
    6) ls -lah "$HOME/CODE_MASTER/logs/" | head -20 ;;
    7) exit 0 ;;
    *) echo "Invalid choice" ;;
esac

