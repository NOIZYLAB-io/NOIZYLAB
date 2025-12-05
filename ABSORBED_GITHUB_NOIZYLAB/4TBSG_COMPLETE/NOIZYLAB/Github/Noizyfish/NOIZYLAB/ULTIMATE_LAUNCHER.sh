#!/bin/bash
# ULTIMATE LAUNCHER - ONE COMMAND TO RULE THEM ALL
clear
echo "=========================================="
echo "🚀 NOIZYLAB ULTIMATE SYSTEM LAUNCHER"
echo "=========================================="
echo ""
echo "What do you want to do?"
echo ""
echo "1. 🎛️  Master Control Center (Dashboard)"
echo "2. 🏥 Health Check (Domain & Email)"
echo "3. 📊 Start 24/7 Monitoring"
echo "4. 🔗 Services Integration (X4 Speed)"
echo "5. 📧 Outlook Setup Guide"
echo "6. 🤖 AI Gateway (Deploy/Test)"
echo "7. 💾 Backup Everything"
echo "8. 📈 Generate Analytics"
echo "9. 🔧 Install/Update All Systems"
echo "0. 🚪 Exit"
echo ""
read -p "Select (0-9): " choice

BASE="/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB"

case $choice in
    1) python3 "$BASE/MASTER_CONTROL_CENTER.py" ;;
    2) python3 "$BASE/ADVANCED_DOMAIN_EMAIL_MANAGER.py" ;;
    3) python3 "$BASE/DOMAIN_EMAIL_MONITOR_24_7.py" ;;
    4) source "$BASE/.env_services" && python3 "$BASE/MASTER_SERVICES_INTEGRATION_X4.py" ;;
    5) cat "$BASE/outlook_configs/MASTER_SETUP_GUIDE.md" | less ;;
    6) bash "$BASE/DEPLOY_AI_GATEWAY.sh" ;;
    7) python3 -c "from importlib import import_module; m=import_module('ADVANCED_DOMAIN_EMAIL_MANAGER'); m.backup_email_configuration()" ;;
    8) python3 -c "from importlib import import_module; m=import_module('ADVANCED_DOMAIN_EMAIL_MANAGER'); m.generate_domain_analytics()" ;;
    9) bash "$BASE/INSTALL_EVERYTHING.sh" ;;
    0) echo "Goodbye! 👋"; exit 0 ;;
    *) echo "Invalid choice"; exit 1 ;;
esac

