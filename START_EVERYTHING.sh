#!/bin/bash
# Start Everything - Launch All NoizyLab Services
# ===============================================

BASE="/Users/m2ultra/NOIZYLAB"

echo "🚀 Starting All NoizyLab Services..."
echo ""

# Email Intelligence
echo "📧 Starting Email Intelligence..."
cd "$BASE/email-intelligence"
python3 api_server_v3.py > /tmp/email-api.log 2>&1 &
API_PID=$!
echo "   API Server: PID $API_PID"

sleep 2

streamlit run dashboard_v3.py --server.port 8501 > /tmp/email-dashboard.log 2>&1 &
DASHBOARD_PID=$!
echo "   Dashboard: PID $DASHBOARD_PID"
echo ""

# System Monitor
echo "📊 Starting System Monitor..."
cd "$BASE/monitoring"
python3 system-monitor.py > /tmp/system-monitor.log 2>&1 &
MONITOR_PID=$!
echo "   Monitor: PID $MONITOR_PID"
echo ""

# Control Panel
echo "🎛️  Starting Control Panel..."
cd "$BASE/control-panel"
streamlit run control-panel.py --server.port 8502 > /tmp/control-panel.log 2>&1 &
CONTROL_PID=$!
echo "   Control Panel: PID $CONTROL_PID"
echo ""

echo "✨ All services started!"
echo ""
echo "Access:"
echo "  📊 Email Dashboard: http://localhost:8501"
echo "  📡 Email API: http://localhost:8000"
echo "  🎛️  Control Panel: http://localhost:8502"
echo ""
echo "Logs:"
echo "  tail -f /tmp/email-api.log"
echo "  tail -f /tmp/email-dashboard.log"
echo "  tail -f /tmp/control-panel.log"
echo ""
echo "To stop all: pkill -f 'api_server_v3|dashboard_v3|control-panel|system-monitor'"
echo ""

