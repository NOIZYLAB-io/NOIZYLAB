#!/bin/bash
# QUICK_ACCESS_X1000.sh - Quick access to all CODE_MASTER tools

CODE_MASTER="/Users/rsp_ms/CODE_MASTER"

while true; do
    clear
    echo "╔══════════════════════════════════════════════════════════════════════╗"
    echo "║     ⚡ CODE_MASTER QUICK ACCESS X1000                                ║"
    echo "╚══════════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "  📚 DOCUMENTATION:"
    echo "    1) View Master Index"
    echo "    2) Browse Code (Interactive)"
    echo "    3) Search Code"
    echo ""
    echo "  📊 ANALYSIS:"
    echo "    4) Code Statistics Dashboard"
    echo "    5) Code Quality Analysis"
    echo "    6) Generate Master Index"
    echo ""
    echo "  🚀 TOOLS:"
    echo "    7) Master Launcher"
    echo "    8) Health Check"
    echo "    9) Auto Backup"
    echo ""
    echo "  0) Exit"
    echo ""
    read -p "Select option: " choice
    
    case $choice in
        1) open "$CODE_MASTER/docs/CODE_MASTER_INDEX.md" 2>/dev/null || cat "$CODE_MASTER/docs/CODE_MASTER_INDEX.md" | less;;
        2) bash "$CODE_MASTER/scripts/BROWSE_CODE_X1000.sh";;
        3) read -p "Enter search term: " term && bash "$CODE_MASTER/scripts/FIND_CODE_X1000.sh" "$term";;
        4) bash "$CODE_MASTER/scripts/CODE_STATS_DASHBOARD_X1000.sh";;
        5) bash "$CODE_MASTER/scripts/ANALYZE_CODE_QUALITY_X1000.sh";;
        6) python3 "$CODE_MASTER/scripts/EXTRACT_MASTER_CODE_LIST.py";;
        7) bash "$CODE_MASTER/MASTER_LAUNCHER.sh";;
        8) bash "$CODE_MASTER/scripts/HEALTH_CHECK.sh";;
        9) bash "$CODE_MASTER/scripts/AUTO_BACKUP_X1000.sh";;
        0) exit 0;;
        *) echo "Invalid option"; sleep 1;;
    esac
done
