#!/bin/bash
# Master Launcher - Start Everything in NoizyLab
# ===============================================

BASE="/Users/m2ultra/NOIZYLAB"

echo "🚀 NoizyLab Master Launcher"
echo "============================"
echo ""
echo "Select what to launch:"
echo ""
echo "1) 🚀 Start Everything (All Services)"
echo "2) 📧 Email System Only"
echo "3) ☁️  Cloudflare Dashboard"
echo "4) 🎛️  Master Dashboard"
echo "5) 🔍 Health Monitor"
echo "6) 🌍 Run HealTheWorld"
echo "7) 📊 System Analytics"
echo "8) 🔧 Setup Email Clients"
echo "9) ⚡ Optimize Everything"
echo "0) 📚 View Documentation"
echo ""
read -p "Choice: " choice

case $choice in
    1)
        echo "🚀 Starting Everything..."
        "$BASE/START_EVERYTHING_V6.sh"
        ;;
    2)
        echo "📧 Starting Email System..."
        cd "$BASE/email-intelligence"
        python3 api_server_v4.py &
        sleep 2
        streamlit run dashboard_v4.py --server.port 8501 --server.headless true &
        echo "✅ Email system started"
        echo "   API: http://localhost:8000"
        echo "   Dashboard: http://localhost:8501"
        ;;
    3)
        echo "☁️  Starting Cloudflare Dashboard..."
        cd "$BASE/cloudflare"
        streamlit run cloudflare-dashboard.py --server.port 8504 --server.headless true
        ;;
    4)
        echo "🎛️  Starting Master Dashboard..."
        cd "$BASE/master-dashboard"
        streamlit run master-dashboard.py --server.port 8503 --server.headless true
        ;;
    5)
        echo "🔍 Starting Health Monitor..."
        cd "$BASE/health"
        python3 health-monitor.py
        ;;
    6)
        echo "🌍 Running HealTheWorld..."
        cd "$BASE"
        python3 health/healtheworld.py
        ;;
    7)
        echo "📊 Running System Analytics..."
        cd "$BASE/analytics"
        python3 system-analytics.py
        ;;
    8)
        echo "🔧 Setting Up Email Clients..."
        cd "$BASE/email-intelligence"
        ./setup-all-email-clients.sh
        ;;
    9)
        echo "⚡ Optimizing Everything..."
        cd "$BASE/performance"
        python3 optimizer.py
        ;;
    0)
        echo "📚 Opening Documentation..."
        open "$BASE" 2>/dev/null || echo "Documentation in: $BASE"
        ;;
    *)
        echo "Invalid choice"
        ;;
esac

