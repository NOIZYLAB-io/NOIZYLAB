#!/bin/bash
# Start iOS Email Setup AI - Quick Launcher
# =========================================

BASE="/Users/m2ultra/NOIZYLAB/cloudflare"

echo "🤖 Starting Email Setup AI for iOS"
echo "=================================="
echo ""

cd "$BASE"

# Get local IP
LOCAL_IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -1)

echo "🚀 Starting local server..."
python3 test-email-setup-ai.py > /tmp/email-setup-ai.log 2>&1 &
SERVER_PID=$!

sleep 3

echo "✅ Server started!"
echo ""
echo "📱 Access from iPad/iPhone:"
echo "   http://${LOCAL_IP}:8788"
echo ""
echo "💻 Or from this Mac:"
echo "   http://localhost:8788"
echo ""
echo "📋 Instructions:"
echo "   1. Open Safari on your iPad or iPhone"
echo "   2. Go to the URL above"
echo "   3. Select your device"
echo "   4. Choose an email"
echo "   5. Get AI setup instructions!"
echo ""
echo "🛑 To stop: pkill -f test-email-setup-ai"
echo ""

