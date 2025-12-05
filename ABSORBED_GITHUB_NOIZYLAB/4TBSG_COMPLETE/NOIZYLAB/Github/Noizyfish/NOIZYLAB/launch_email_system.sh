#!/bin/bash
# Email System Launcher
# Quick launch script for all email tools

clear
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          🚀 EMAIL MASTER CONTROL SYSTEM LAUNCHER              ║"
echo "║              rsplowman@gmail.com                              ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "Select a tool to launch:"
echo ""
echo "  1. 🎯 Master Control Center (Recommended - All Features)"
echo "  2. 🔥 Hot Rod Setup (Advanced Gmail Configuration)"
echo "  3. 📧 Quick Email Setup (Step-by-Step Account Setup)"
echo "  4. 🤖 Automation System (Email Automation Rules)"
echo "  5. 💾 Backup & Restore (Configuration Management)"
echo "  6. 📚 View Documentation"
echo "  7. 🔗 Open Gmail Settings"
echo "  0. Exit"
echo ""
read -p "Enter choice: " choice

case $choice in
    1)
        echo "🚀 Launching Master Control Center..."
        python3 "$(dirname "$0")/email_master_control.py"
        ;;
    2)
        echo "🔥 Launching Hot Rod Setup..."
        python3 "$(dirname "$0")/gmail_hotrod_setup.py"
        ;;
    3)
        echo "📧 Launching Quick Email Setup..."
        python3 "$(dirname "$0")/quick_email_setup.py"
        ;;
    4)
        echo "🤖 Launching Automation System..."
        python3 "$(dirname "$0")/email_automation.py"
        ;;
    5)
        echo "💾 Launching Backup & Restore..."
        python3 "$(dirname "$0")/email_backup_restore.py"
        ;;
    6)
        echo "📚 Opening documentation..."
        open "$(dirname "$0")/README_MASTER.md" 2>/dev/null || \
        cat "$(dirname "$0")/README_MASTER.md"
        ;;
    7)
        echo "🔗 Opening Gmail Settings..."
        open "https://mail.google.com/mail/u/0/#settings/all"
        ;;
    0)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

