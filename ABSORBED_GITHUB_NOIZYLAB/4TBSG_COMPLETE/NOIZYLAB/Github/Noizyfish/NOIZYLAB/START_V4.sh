#!/bin/bash
# Start NoizyLab V4 - Enterprise Edition
# =======================================

BASE="/Users/m2ultra/NOIZYLAB"

echo "🚀 Starting NoizyLab V4 - Enterprise Edition"
echo "============================================="
echo ""

# Check Redis
if ! command -v redis-cli &> /dev/null; then
    echo "⚠️  Redis not found. Install with: brew install redis"
    echo "   Starting without Redis caching..."
else
    if ! redis-cli ping &> /dev/null; then
        echo "📦 Starting Redis..."
        redis-server --daemonize yes
        sleep 2
    fi
    echo "✅ Redis running"
fi

# Optimize database
echo "⚡ Optimizing database..."
cd "$BASE/performance"
python3 optimizer.py > /tmp/optimizer.log 2>&1
echo "✅ Database optimized"

# Start V4 API
echo "📡 Starting V4 API Server..."
cd "$BASE/email-intelligence"
python3 api_server_v4.py > /tmp/api-v4.log 2>&1 &
API_PID=$!
echo "   API Server: PID $API_PID (http://localhost:8000)"

sleep 2

# Start V4 Dashboard
echo "📊 Starting V4 Dashboard..."
streamlit run dashboard_v4.py --server.port 8501 > /tmp/dashboard-v4.log 2>&1 &
DASHBOARD_PID=$!
echo "   Dashboard: PID $DASHBOARD_PID (http://localhost:8501)"

# Start Mobile API
echo "📱 Starting Mobile API..."
cd "$BASE/mobile"
python3 ios-shortcuts.py > /tmp/mobile-api.log 2>&1 &
MOBILE_PID=$!
echo "   Mobile API: PID $MOBILE_PID (http://localhost:8002)"

# Start Webhook Hub
echo "🔗 Starting Webhook Hub..."
cd "$BASE/integrations"
python3 webhook-hub.py > /tmp/webhook-hub.log 2>&1 &
WEBHOOK_PID=$!
echo "   Webhook Hub: PID $WEBHOOK_PID (http://localhost:8001)"

echo ""
echo "✨ All V4 services started!"
echo ""
echo "Access Points:"
echo "  📡 V4 API: http://localhost:8000"
echo "  📊 V4 Dashboard: http://localhost:8501"
echo "  📱 Mobile API: http://localhost:8002"
echo "  🔗 Webhook Hub: http://localhost:8001"
echo ""
echo "Logs:"
echo "  tail -f /tmp/api-v4.log"
echo "  tail -f /tmp/dashboard-v4.log"
echo "  tail -f /tmp/mobile-api.log"
echo "  tail -f /tmp/webhook-hub.log"
echo ""
echo "To stop all: pkill -f 'api_server_v4|dashboard_v4|ios-shortcuts|webhook-hub'"
echo ""

