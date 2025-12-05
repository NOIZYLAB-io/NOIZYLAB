#!/bin/bash
# 🌐 NETWORK - MTU CHECK (JUMBO FRAMES)
# Fish Music Inc - CB_01

echo "🔍 Checking MTU (Jumbo Frames)..."
echo ""

# Detect interface
INTERFACE=$(route -n get default 2>/dev/null | grep interface | awk '{print $2}')

if [ -z "$INTERFACE" ]; then
    echo "❌ Could not detect network interface"
    echo "   Available interfaces:"
    ifconfig | grep "^[a-z]" | cut -d: -f1
    exit 1
fi

# Get current MTU
MTU=$(ifconfig "$INTERFACE" | grep mtu | awk '{print $6}')

echo "Interface: $INTERFACE"
echo "Current MTU: $MTU bytes"
echo ""

# Check if jumbo frames enabled
if [ "$MTU" -ge 9000 ]; then
    echo "✅ Jumbo frames ENABLED!"
    echo "   MC96 switch: COMPATIBLE"
else
    echo "⚠️  Jumbo frames NOT enabled"
    echo ""
    echo "   To enable:"
    echo "   sudo networksetup -setMTU $INTERFACE 9000"
fi

echo ""

# Test jumbo frames to target
if [ ! -z "$1" ]; then
    echo "Testing jumbo frames to $1..."
    ping -D -s 8972 -c 5 "$1"
    
    if [ $? -eq 0 ]; then
        echo "✅ Jumbo frames working to $1!"
    else
        echo "❌ Jumbo frames NOT working"
        echo "   Check:"
        echo "   1. MTU on both machines (9000+)"
        echo "   2. MC96 switch jumbo frames enabled"
        echo "   3. All devices in path support jumbo"
    fi
fi

echo ""
echo "🔥 GORUNFREE! 🎸🔥"
