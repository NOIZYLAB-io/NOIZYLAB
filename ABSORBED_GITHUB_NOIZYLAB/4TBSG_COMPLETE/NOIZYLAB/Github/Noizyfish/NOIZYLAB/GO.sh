#!/usr/bin/env bash
# ==============================================================================
# 🚀 GO - Unified NOIZYLAB Launcher
# ==============================================================================
# One command to rule them all - Quick access to everything
# ==============================================================================

NOIZYLAB="/Users/m2ultra/NOIZYLAB"

show_menu() {
    echo "╔═══════════════════════════════════════════════════════════════╗"
    echo "║                  🚀 NOIZYLAB CONTROL CENTER                   ║"
    echo "╚═══════════════════════════════════════════════════════════════╝"
    echo ""
    echo "📦 ORGANIZATION & UPGRADE"
    echo "  1) Upgrade Everything          - Run master upgrade"
    echo "  2) Quick Cleanup               - Fast cleanup"
    echo "  3) Organize Files              - Python organizer"
    echo ""
    echo "🔍 ANALYSIS & MONITORING"
    echo "  4) Disk Usage Analyzer (Fast)  - Quick disk analysis"
    echo "  5) Check Agents                - Check running processes"
    echo "  6) Performance Monitor         - System performance"
    echo ""
    echo "🤖 AGENTS"
    echo "  7) GABRIEL                     - GABRIEL agent"
    echo "  8) MC96                        - MC96 agent"
    echo ""
    echo "📄 DOCUMENTATION"
    echo "  9) Quick Reference             - Command reference"
    echo "  10) View README                - Full documentation"
    echo ""
    echo "🧹 MAINTENANCE"
    echo "  11) Clean & Organize           - Full cleanup"
    echo "  12) Optimize Databases         - Database optimization"
    echo ""
    echo "  0) Exit"
    echo ""
}

upgrade_all() {
    echo "🚀 Upgrading everything..."
    cd "$NOIZYLAB" && ./MASTER_UPGRADE_ALL.sh
}

quick_cleanup() {
    echo "🧹 Quick cleanup..."
    cd "$NOIZYLAB" && ./FAST_CLEANUP.sh
}

organize_files() {
    echo "📦 Organizing files..."
    cd "$NOIZYLAB" && python3 QUICK_ORGANIZE.py
}

disk_analyzer() {
    echo "📊 Analyzing disk usage..."
    cd "$NOIZYLAB" && python3 IMPROVED_DISK_ANALYZER.py
}

check_agents() {
    echo "🔍 Checking agents..."
    cd "$NOIZYLAB" && python3 CHECK_AGENTS.py
}

performance_monitor() {
    echo "⚡ Performance monitor..."
    cd "$NOIZYLAB" && python3 PERFORMANCE_MONITOR.py
}

gabriel_agent() {
    echo "🟣 GABRIEL Agent"
    echo "Available commands: scan, heal, organize, workflow, status"
    echo ""
    read -p "Enter command (or 'help'): " cmd
    if [ "$cmd" = "help" ] || [ -z "$cmd" ]; then
        cd "$NOIZYLAB" && node gabriel-cli.mjs
    else
        cd "$NOIZYLAB" && node gabriel-cli.mjs $cmd
    fi
}

mc96_agent() {
    echo "🔵 MC96 Agent"
    echo "Available commands: agent, migrate, deploy, generate"
    echo ""
    read -p "Enter command (or 'help'): " cmd
    if [ "$cmd" = "help" ] || [ -z "$cmd" ]; then
        cd "$NOIZYLAB" && node mc96-cli.mjs
    else
        cd "$NOIZYLAB" && node mc96-cli.mjs $cmd
    fi
}

show_quick_ref() {
    if [ -f "$NOIZYLAB/QUICK_REFERENCE.md" ]; then
        cat "$NOIZYLAB/QUICK_REFERENCE.md"
    else
        echo "📚 Quick Reference not found. Run upgrade first!"
    fi
}

show_readme() {
    if [ -f "$NOIZYLAB/README_UPGRADED.md" ]; then
        cat "$NOIZYLAB/README_UPGRADED.md"
    elif [ -f "$NOIZYLAB/README.md" ]; then
        cat "$NOIZYLAB/README.md"
    else
        echo "📄 README not found"
    fi
}

clean_organize() {
    echo "🧹 Full cleanup and organization..."
    quick_cleanup
    organize_files
}

optimize_dbs() {
    echo "💾 Optimizing databases..."
    cd "$NOIZYLAB"
    for db in *.db; do
        if [ -f "$db" ]; then
            sqlite3 "$db" "VACUUM; ANALYZE; REINDEX;" 2>/dev/null && echo "  ✓ Optimized: $db" || true
        fi
    done
    echo "✅ Done"
}

main() {
    cd "$NOIZYLAB"
    
    # If argument provided, run directly
    if [ $# -gt 0 ]; then
        case "$1" in
            upgrade|upgrade-all|1) upgrade_all ;;
            cleanup|clean|2) quick_cleanup ;;
            organize|org|3) organize_files ;;
            analyze|disk|4) disk_analyzer ;;
            agents|check|5) check_agents ;;
            perf|performance|6) performance_monitor ;;
            gabriel|7) gabriel_agent ;;
            mc96|8) mc96_agent ;;
            ref|reference|9) show_quick_ref ;;
            readme|10) show_readme ;;
            cleanall|11) clean_organize ;;
            optimize|12) optimize_dbs ;;
            *) echo "Unknown command: $1. Run without args for menu." ;;
        esac
        return
    fi
    
    # Interactive menu
    while true; do
        show_menu
        read -p "Select option: " choice
        echo ""
        
        case "$choice" in
            1) upgrade_all ;;
            2) quick_cleanup ;;
            3) organize_files ;;
            4) disk_analyzer ;;
            5) check_agents ;;
            6) performance_monitor ;;
            7) gabriel_agent ;;
            8) mc96_agent ;;
            9) show_quick_ref ;;
            10) show_readme ;;
            11) clean_organize ;;
            12) optimize_dbs ;;
            0|q|exit) echo "👋 Goodbye!"; exit 0 ;;
            *) echo "❌ Invalid option" ;;
        esac
        
        echo ""
        read -p "Press Enter to continue..."
        clear
    done
}

main "$@"

