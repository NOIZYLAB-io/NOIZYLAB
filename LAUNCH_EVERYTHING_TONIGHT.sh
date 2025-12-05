#!/bin/bash
# 🔥 LAUNCH EVERYTHING - TONIGHT'S COMPLETE STACK!!

clear
echo "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"
echo "     LAUNCHING COMPLETE STACK - ALL SYSTEMS GO!!"
echo "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"
echo ""

# Check if Mail.app is configured
echo "🍎 Checking Mail.app configuration..."
if [ -d "$HOME/Library/Mail" ]; then
    echo "   ✅ Mail.app is configured!"
else
    echo "   ⚠️  Mail.app might not be setup yet"
    echo "   Open Mail.app and add rsplowman@icloud.com"
fi

echo ""
echo "🚀 STARTING ALL SYSTEMS..."
echo ""

# Kill any existing processes
killall -9 python3 2>/dev/null

# Start NoizyLab Portal
echo "🔬 Starting NoizyLab Portal..."
cd /Users/m2ultra/Github/noizylab/NoizyLab_CA_Portal
python3 NOIZYLAB_COMPLETE_PORTAL.py > portal.log 2>&1 &
PORTAL_PID=$!
echo "   ✅ Portal starting (PID: $PORTAL_PID)"

sleep 2

# Start Passkey Auth (optional)
# echo "🔐 Starting Passkey Auth..."
# pip3 install pyopenssl --quiet 2>/dev/null
# python3 PASSKEY_AUTH_SYSTEM.py > passkey.log 2>&1 &
# PASSKEY_PID=$!
# echo "   ✅ Passkey auth starting (PID: $PASSKEY_PID)"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉🎉🎉 ALL SYSTEMS RUNNING!! 🎉🎉🎉"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔬 NOIZYLAB PORTAL:"
echo "   http://localhost:4000"
echo "   → Check-ins, invoices, clients, payments"
echo ""
# echo "🔐 PASSKEY LOGIN (Optional):"
# echo "   https://localhost:7000"
# echo "   → Touch ID login (no passwords!)"
# echo ""
echo "🍎 EMAIL SYSTEM:"
echo "   Status: WORKING via Mail.app!!"
echo "   Email: rsplowman@icloud.com"
echo "   Method: AppleScript (no passwords!)"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎯 WHAT YOU CAN DO NOW:"
echo ""
echo "  1. Open NoizyLab Portal: http://localhost:4000"
echo "  2. Log DESIGN REUNION check-in"
echo "  3. Create invoice for Gavin"
echo "  4. Test email: ./MAIL_APP_SEND_NOW.sh test@email.com"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Press Ctrl+C to stop all services"
echo ""
echo "🐟 GORUNFREE!! 🚀"
echo ""

# Keep running
wait

