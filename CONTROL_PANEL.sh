#!/bin/bash
# MASTER CONTROL PANEL - MC96
# Centralized system control

while true; do
    clear
    echo "╔════════════════════════════════════════════════════╗"
    echo "║  MASTER CONTROL PANEL - MC96                      ║"
    echo "╚════════════════════════════════════════════════════╝"
    echo ""
    echo "  1) Health Check"
    echo "  2) Auto Optimize"
    echo "  3) GHOST Drive Scan"
    echo "  4) Performance Monitor"
    echo "  5) Daily Maintenance"
    echo "  6) Auto Backup"
    echo "  7) Verify Installation"
    echo "  8) View Logs"
    echo "  9) Exit"
    echo ""
    read -p "Select option: " choice
    
    case $choice in
        1) bash "/Volumes/4TB_02/CODE_MASTER/scripts/HEALTH_CHECK.sh"; read -p "Press Enter to continue...";;
        2) bash "/Volumes/4TB_02/CODE_MASTER/scripts/AUTO_OPTIMIZE.sh"; read -p "Press Enter to continue...";;
        3) bash "/Volumes/4TB_02/CODE_MASTER/scripts/ENHANCED_GHOST_SCAN.sh"; read -p "Press Enter to continue...";;
        4) bash "/Volumes/4TB_02/CODE_MASTER/scripts/PERF_MONITOR.sh";;
        5) bash "/Volumes/4TB_02/CODE_MASTER/scripts/DAILY_MAINTENANCE.sh"; read -p "Press Enter to continue...";;
        6) bash "/Volumes/4TB_02/CODE_MASTER/scripts/AUTO_BACKUP.sh"; read -p "Press Enter to continue...";;
        7) bash "/Volumes/4TB_02/CODE_MASTER/scripts/VERIFY_INSTALL.sh"; read -p "Press Enter to continue...";;
        8) ls -lah "/Volumes/4TB_02/CODE_MASTER/logs/" | head -20; read -p "Press Enter to continue...";;
        9) exit 0;;
        *) echo "Invalid option"; sleep 1;;
    esac
done