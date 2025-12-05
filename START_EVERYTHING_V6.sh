#!/bin/bash
# Start Everything V6 - Launch All NoizyLab Systems
# =================================================

BASE="/Users/m2ultra/NOIZYLAB"

echo "🚀 Starting NoizyLab V6 - Everything!"
echo "======================================"
echo ""

# Heal first
echo "🌍 Healing system..."
python3 "$BASE/health/healtheworld.py" >/dev/null 2>&1
echo "✅ Healed"
echo ""

# Start V4 API
echo "📡 Starting V4 API..."
cd "$BASE/email-intelligence"
nohup python3 api_server_v4.py > /tmp/api-v4.log 2>&1 &
API_PID=$!
echo "   ✅ API: PID $API_PID"
sleep 2

# Start Dashboard
echo "📊 Starting Email Dashboard..."
nohup streamlit run dashboard_v4.py --server.port 8501 --server.headless true > /tmp/dashboard-v4.log 2>&1 &
DASH_PID=$!
echo "   ✅ Dashboard: PID $DASH_PID"
sleep 2

# Start Master Dashboard
echo "🎛️  Starting Master Dashboard..."
cd "$BASE/master-dashboard"
nohup streamlit run master-dashboard.py --server.port 8503 --server.headless true > /tmp/master-dashboard.log 2>&1 &
MASTER_PID=$!
echo "   ✅ Master Dashboard: PID $MASTER_PID"
sleep 2

# Start Mobile API
echo "📱 Starting Mobile API..."
cd "$BASE/mobile"
nohup python3 ios-shortcuts.py > /tmp/mobile-api.log 2>&1 &
MOBILE_PID=$!
echo "   ✅ Mobile API: PID $MOBILE_PID"
sleep 2

# Start Webhook Hub
echo "🔗 Starting Webhook Hub..."
cd "$BASE/integrations"
nohup python3 webhook-hub.py > /tmp/webhook-hub.log 2>&1 &
WEBHOOK_PID=$!
echo "   ✅ Webhook Hub: PID $WEBHOOK_PID"
sleep 2

# Start Auto-Monitor
echo "🔍 Starting Auto-Monitor..."
cd "$BASE/automation"
nohup python3 auto-monitor.py > /tmp/auto-monitor.log 2>&1 &
MONITOR_PID=$!
echo "   ✅ Auto-Monitor: PID $MONITOR_PID"
echo ""

echo "✨ ALL SYSTEMS STARTED!"
echo "======================"
echo ""
echo "🌐 Access Points:"
echo "   📡 V4 API: http://localhost:8000"
echo "   📊 Email Dashboard: http://localhost:8501"
echo "   🎛️  Master Dashboard: http://localhost:8503"
echo "   📱 Mobile API: http://localhost:8002"
echo "   🔗 Webhook Hub: http://localhost:8001"
echo ""
echo "📋 Logs:"
echo "   tail -f /tmp/api-v4.log"
echo "   tail -f /tmp/dashboard-v4.log"
echo "   tail -f /tmp/master-dashboard.log"
echo "   tail -f /tmp/auto-monitor.log"
echo ""
echo "🛑 Stop All: pkill -f 'api_server_v4|dashboard_v4|master-dashboard|ios-shortcuts|webhook-hub|auto-monitor'"
echo ""

