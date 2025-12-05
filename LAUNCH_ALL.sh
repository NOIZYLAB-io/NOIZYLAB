#!/bin/bash
# Launch All Systems - Ultimate NOIZYLAB Platform

clear
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     🚀 NOIZYLAB ULTIMATE PLATFORM - 1000x UPGRADE            ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "Select system to launch:"
echo ""
echo "  🤖 AI SYSTEMS:"
echo "    1. Ultimate Master System (All-in-One) ⭐"
echo "    2. Advanced AI Engine (ML, NLP, CV)"
echo "    3. AI Trainer (Repair Team Training)"
echo "    4. Universal Problem Solver"
echo ""
echo "  📧 EMAIL SYSTEMS:"
echo "    5. Email Master Control"
echo "    6. Gmail Hot Rod Setup"
echo "    7. Quick Email Setup"
echo ""
echo "  ☁️  CLOUD & MOBILE:"
echo "    8. Cloud Integration"
echo "    9. Mobile App Generator"
echo ""
echo "  🛠️  TOOLS:"
echo "    10. Email Automation"
echo "    11. Backup & Restore"
echo "    12. iOS Profile Generator"
echo ""
echo "  0. Exit"
echo ""
read -p "Select: " choice

cd "$(dirname "$0")"

case $choice in
    1) python3 ultimate_master_system.py ;;
    2) python3 advanced_ai_engine.py ;;
    3) python3 noizylab_ai_trainer.py ;;
    4) python3 universal_problem_solver.py ;;
    5) python3 email_master_control.py ;;
    6) python3 gmail_hotrod_setup.py ;;
    7) python3 quick_email_setup.py ;;
    8) python3 cloud_integration.py ;;
    9) python3 mobile_app_generator.py ;;
    10) python3 email_automation.py ;;
    11) python3 email_backup_restore.py ;;
    12) python3 create_ios_email_profiles.py ;;
    0) echo "👋 Goodbye!"; exit 0 ;;
    *) echo "❌ Invalid choice" ;;
esac

