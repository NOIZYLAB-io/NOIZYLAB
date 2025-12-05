#!/bin/bash
# MASTER_CONTROL_CENTER_X1000.sh - Ultimate control center

CODE_MASTER="/Users/rsp_ms/CODE_MASTER"

while true; do
    clear
    echo "╔══════════════════════════════════════════════════════════════════════╗"
    echo "║     🎛️ MASTER CONTROL CENTER X1000                                   ║"
    echo "╚══════════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "  📚 CODE MANAGEMENT:"
    echo "    1) Browse Code"
    echo "    2) Find Code"
    echo "    3) Analyze Code Quality"
    echo "    4) Code Health Monitor"
    echo "    5) Code Metrics"
    echo ""
    echo "  📊 ANALYSIS:"
    echo "    6) Intelligent Code Analyzer"
    echo "    7) Generate Documentation"
    echo "    8) Code Statistics Dashboard"
    echo ""
    echo "  🚀 ACTIONS:"
    echo "    9) Generate Master Index"
    echo "    10) Organize Code"
    echo "    11) Backup All"
    echo "    12) Run All Tests"
    echo ""
    echo "  ⚙️ SYSTEM:"
    echo "    13) Health Check"
    echo "    14) Performance Monitor"
    echo "    15) Auto Update"
    echo ""
    echo "  0) Exit"
    echo ""
    read -p "Select option: " choice
    
    case $choice in
        1) bash "$CODE_MASTER/scripts/BROWSE_CODE_X1000.sh";;
        2) read -p "Search term: " term && bash "$CODE_MASTER/scripts/FIND_CODE_X1000.sh" "$term";;
        3) bash "$CODE_MASTER/scripts/ANALYZE_CODE_QUALITY_X1000.sh";;
        4) bash "$CODE_MASTER/scripts/CODE_HEALTH_MONITOR_X1000.sh";;
        5) bash "$CODE_MASTER/scripts/CODE_METRICS_X1000.sh"; read -p "Press Enter...";;
        6) bash "$CODE_MASTER/scripts/INTELLIGENT_CODE_ANALYZER_X1000.sh"; read -p "Press Enter...";;
        7) bash "$CODE_MASTER/scripts/AUTO_DOCUMENT_ALL_X1000.sh"; read -p "Press Enter...";;
        8) bash "$CODE_MASTER/scripts/CODE_STATS_DASHBOARD_X1000.sh";;
        9) python3 "$CODE_MASTER/scripts/EXTRACT_MASTER_CODE_LIST.py"; read -p "Press Enter...";;
        10) bash "$CODE_MASTER/scripts/SMART_ORGANIZER_X1000.sh"; read -p "Press Enter...";;
        11) bash "$CODE_MASTER/scripts/AUTO_BACKUP_X1000.sh"; read -p "Press Enter...";;
        12) bash "$CODE_MASTER/scripts/TEST_ALL_SCRIPTS.sh"; read -p "Press Enter...";;
        13) bash "$CODE_MASTER/scripts/HEALTH_CHECK.sh"; read -p "Press Enter...";;
        14) bash "$CODE_MASTER/scripts/PERF_MONITOR_X1000.sh";;
        15) bash "$CODE_MASTER/scripts/AUTO_UPDATE_X1000.sh"; read -p "Press Enter...";;
        0) exit 0;;
        *) echo "Invalid option"; sleep 1;;
    esac
done
