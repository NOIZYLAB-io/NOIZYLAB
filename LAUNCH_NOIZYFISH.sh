#!/bin/bash
# 🐟 NOIZYFISH.COM - QUICK LAUNCHER

clear
echo "🐟 NOIZYFISH.COM - LAUNCHING..."
echo "======================================="
echo ""

# Check Flask
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Installing Flask..."
    pip3 install flask --quiet
    echo "✅ Flask installed"
fi

echo "🚀 Starting NoizyFish.com..."
echo ""
echo "=============================================="
echo "🐟 NOIZYFISH.COM IS LIVE!"
echo "=============================================="
echo ""
echo "🌐 Website:        http://localhost:3000"
echo "📧 Email:          rsp@noizyfish.com"
echo "📝 Contact Form:   Integrated & working!"
echo ""
echo "Press Ctrl+C to stop"
echo "=============================================="
echo ""

python3 noizyfish_app.py
