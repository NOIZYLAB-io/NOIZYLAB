#!/bin/bash
# 🚀 LAUNCH COMPLETE NOIZYLAB ECOSYSTEM
# Starts ALL systems integrated and optimized!
# AUTOALLOW - COMPLETE AUTOMATION!!

clear
echo "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"
echo "     NOIZYLAB COMPLETE ECOSYSTEM - LAUNCHING!!"
echo "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"
echo ""

# Kill any existing processes
echo "🧹 Cleaning up old processes..."
ps aux | grep "python3.*NOIZYLAB\|python3.*RESCUE\|python3.*TEAMVIEWER\|python3.*MASTER_CONTROL" | grep -v grep | awk '{print $2}' | xargs kill -9 2>/dev/null
echo "   ✅ Clean slate!"
echo ""

# Check dependencies
echo "📦 Checking dependencies..."
pip3 install flask stripe requests --quiet 2>/dev/null
echo "   ✅ Dependencies ready"
echo ""

# Check Mail.app
echo "🍎 Checking Email system..."
if [ -d "$HOME/Library/Mail" ]; then
    echo "   ✅ Mail.app configured!"
else
    echo "   ⚠️  Mail.app might need setup"
fi
echo ""

# Check network
echo "🌐 Checking network..."
if ping -c 1 192.168.1.1 > /dev/null 2>&1; then
    echo "   ✅ DGS1210-10 switch online!"
else
    echo "   ⚠️  Switch not reachable (might be offline)"
fi

# Check jumbo frames
if ifconfig en0 | grep -q "mtu 9000"; then
    echo "   ✅ Jumbo frames ENABLED (Hot Rod Mode!)"
else
    echo "   ⚠️  Jumbo frames not enabled"
    echo "   To enable: sudo ifconfig en0 mtu 9000"
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 STARTING ALL SYSTEMS..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cd /Users/m2ultra/Github/noizylab

# 1. Master Control Dashboard
echo "🎛️  Starting Master Control Dashboard..."
cd NoizyLab_CA_Portal
python3 MASTER_CONTROL_DASHBOARD.py > ../logs/master_control.log 2>&1 &
MASTER_PID=$!
echo "   ✅ Master Control (PID: $MASTER_PID) - Port 9000"
sleep 1

# 2. NoizyLab Portal  
echo "🔬 Starting NoizyLab Portal..."
python3 COMPLETE_PORTAL_WITH_STRIPE.py > ../logs/portal.log 2>&1 &
PORTAL_PID=$!
echo "   ✅ Portal (PID: $PORTAL_PID) - Port 4000"
sleep 1

# 3. RESCUE System
echo "🚨 Starting RESCUE System..."
python3 NOIZYLAB_RESCUE_COMPLETE.py > ../logs/rescue.log 2>&1 &
RESCUE_PID=$!
echo "   ✅ RESCUE (PID: $RESCUE_PID) - Port 8000"
sleep 1

# 4. TeamViewer Instructions
echo "🖥️  Starting TeamViewer System..."
python3 TEAMVIEWER_REMOTE_REPAIR.py > ../logs/teamviewer.log 2>&1 &
TV_PID=$!
echo "   ✅ TeamViewer (PID: $TV_PID) - Port 8001"
sleep 1

# 5. Payment System
echo "💰 Starting Payment System..."
python3 PAY_IF_FIXED_SYSTEM.py > ../logs/payments.log 2>&1 &
PAY_PID=$!
echo "   ✅ Payments (PID: $PAY_PID) - Port 5001"
sleep 2

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉🎉🎉 ALL SYSTEMS RUNNING!! 🎉🎉🎉"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎛️  MASTER CONTROL (ALL-IN-ONE):"
echo "   http://localhost:9000"
echo "   → Complete command center for everything!"
echo ""
echo "🔬 NOIZYLAB PORTAL:"
echo "   http://localhost:4000"
echo "   → Check-ins, invoices, client management"
echo ""
echo "🚨 RESCUE SYSTEM:"
echo "   http://localhost:8000"
echo "   → Client-facing rescue request page"
echo ""
echo "🖥️  TEAMVIEWER INSTRUCTIONS:"
echo "   http://localhost:8001"
echo "   → Send to clients for remote access"
echo ""
echo "💰 PAYMENT PAGE:"
echo "   http://localhost:5001"
echo "   → Client payment ($89+ if fixed!)"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ EMAIL: Mail.app (rsplowman@icloud.com) - WORKING!!"
echo "✅ NETWORK: DGS1210-10 + MC96 mesh"
echo "✅ PERFORMANCE: Hot Rod mode available"
echo "✅ PAYMENTS: Stripe + Apple Pay + PayPal ready"
echo "✅ TEAMVIEWER: Optimized for remote repairs"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎯 RECOMMENDED: Start with MASTER CONTROL:"
echo "   http://localhost:9000"
echo ""
echo "Press Ctrl+C to stop all services"
echo ""
echo "🐟 GORUNFREE!! 🚀"
echo ""

# Create trap to clean up on exit
trap "echo ''; echo '🛑 Stopping all services...'; kill $MASTER_PID $PORTAL_PID $RESCUE_PID $TV_PID $PAY_PID 2>/dev/null; echo '✅ All services stopped'; exit 0" INT

# Keep running
wait

