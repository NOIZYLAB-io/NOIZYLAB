#!/bin/bash
# 🚀 FISH MUSIC EMAIL PLATFORM - ONE-COMMAND LAUNCHER

clear
echo "🐟 FISH MUSIC ULTIMATE EMAIL PLATFORM"
echo "======================================"
echo ""

# Check if config is setup
if grep -q "YOUR_APP_PASSWORD_HERE" ultimate_email_config.json 2>/dev/null; then
    echo "⚠️  CONFIGURATION NEEDED!"
    echo ""
    echo "Please edit ultimate_email_config.json first:"
    echo "1. Add your Gmail App Password"
    echo "2. Set 'enabled: true'"
    echo ""
    echo "Then run this script again."
    exit 1
fi

echo "✅ Configuration detected"
echo ""
echo "🚀 LAUNCHING COMPLETE SYSTEM..."
echo ""

# Install dependencies if needed
echo "📦 Checking dependencies..."
pip3 install flask dnspython --quiet 2>/dev/null
echo "✅ Dependencies ready"
echo ""

# Start queue worker in background
echo "🔄 Starting email queue worker..."
python3 EMAIL_QUEUE_SYSTEM.py start > queue.log 2>&1 &
QUEUE_PID=$!
echo "✅ Queue worker started (PID: $QUEUE_PID)"

# Give it a second to start
sleep 2

# Start web dashboard
echo "🌐 Starting web dashboard..."
echo ""
echo "=============================================="
echo "🎉 FISH MUSIC EMAIL PLATFORM IS RUNNING!"
echo "=============================================="
echo ""
echo "📊 Web Dashboard:  http://localhost:5000"
echo "📧 Send emails from the dashboard"
echo "🔗 Webhook endpoints ready"
echo "📈 Real-time analytics active"
echo ""
echo "Press Ctrl+C to stop all services"
echo "=============================================="
echo ""

# Trap Ctrl+C to clean up
trap "echo ''; echo '🛑 Stopping services...'; kill $QUEUE_PID 2>/dev/null; echo '✅ Services stopped'; exit 0" INT

# Start dashboard (this blocks)
python3 ULTIMATE_WEB_DASHBOARD.py

