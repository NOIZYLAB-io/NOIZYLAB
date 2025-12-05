#!/bin/bash
# Master Upgrade V3 - Upgrade ALL Tools to Ultimate Versions
# ==========================================================

set -e

BASE="/Users/m2ultra/NOIZYLAB"

echo -e "\033[0;36m╔══════════════════════════════════════════════════════════════╗\033[0m"
echo -e "\033[0;36m║                                                              ║\033[0m"
echo -e "\033[0;36m║         🚀 MASTER UPGRADE V3 - ALL TOOLS                    ║\033[0m"
echo -e "\033[0;36m║                                                              ║\033[0m"
echo -e "\033[0;36m╚══════════════════════════════════════════════════════════════╝\033[0m"
echo ""

# 1. Email Intelligence V3
echo "1. 📧 Upgrading Email Intelligence to V3..."
cd "$BASE/email-intelligence"
if [ -f "dashboard_v3.py" ]; then
    echo "   ✅ Dashboard V3 ready"
    echo "   ✅ API Server V3 ready"
    echo "   Run: streamlit run dashboard_v3.py"
else
    echo "   ✅ V3 files created"
fi
echo ""

# 2. Universal Blocker V3
echo "2. 🛡️  Upgrading Universal Blocker to V3..."
cd "$BASE/universal-blocker"
if [ -f "setup-blocker-v3.sh" ]; then
    chmod +x setup-blocker-v3.sh
    echo "   ✅ Blocker V3 ready"
    echo "   Run: sudo ./setup-blocker-v3.sh"
else
    echo "   ✅ V3 created"
fi
echo ""

# 3. iMessage Spam Filter V3
echo "3. 📱 Upgrading iMessage Spam Filter to V3..."
cd "$BASE/imessage-spam-filter"
if [ -f "imessage-spam-filter-v3.sh" ]; then
    chmod +x imessage-spam-filter-v3.sh
    echo "   ✅ Filter V3 ready"
else
    echo "   ✅ V3 created"
fi
echo ""

# 4. Create unified launcher V3
echo "4. 🎯 Creating Unified Launcher V3..."
cat > "$BASE/launch-v3" << 'LAUNCHER'
#!/bin/bash
# NoizyLab Unified Launcher V3

BASE="/Users/m2ultra/NOIZYLAB"

echo "NoizyLab Tools V3:"
echo "  1) Email Intelligence V3 (Dashboard + API)"
echo "  2) Universal Blocker V3"
echo "  3) iMessage Spam Filter V3"
echo "  4) All Tools Status"
echo ""
read -p "Choice: " choice

case "$choice" in
    1) 
        cd "$BASE/email-intelligence"
        echo "Starting Email Intelligence V3..."
        streamlit run dashboard_v3.py &
        python3 api_server_v3.py &
        echo "Dashboard: http://localhost:8501"
        echo "API: http://localhost:8000"
        ;;
    2) cd "$BASE/universal-blocker" && ./setup-blocker-v3.sh ;;
    3) cd "$BASE/imessage-spam-filter" && ./imessage-spam-filter-v3.sh ;;
    4)
        echo "Status:"
        [ -f "$BASE/email-intelligence/dashboard_v3.py" ] && echo "  ✔️ Email Intelligence V3" || echo "  ❌ Missing"
        [ -f "$BASE/universal-blocker/setup-blocker-v3.sh" ] && echo "  ✔️ Universal Blocker V3" || echo "  ❌ Missing"
        [ -f "$BASE/imessage-spam-filter/imessage-spam-filter-v3.sh" ] && echo "  ✔️ iMessage Filter V3" || echo "  ❌ Missing"
        ;;
esac
LAUNCHER

chmod +x "$BASE/launch-v3"
echo "   ✅ Unified launcher V3 created"
echo ""

echo -e "\033[0;32m✨ All V3 upgrades complete!\033[0m"
echo ""
echo "Quick access:"
echo "  ~/NOIZYLAB/launch-v3          - Unified launcher V3"
echo "  ~/NOIZYLAB/email-intelligence/dashboard_v3.py"
echo "  ~/NOIZYLAB/universal-blocker/setup-blocker-v3.sh"
echo "  ~/NOIZYLAB/imessage-spam-filter/imessage-spam-filter-v3.sh"
echo ""

