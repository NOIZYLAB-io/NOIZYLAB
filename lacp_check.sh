#!/bin/bash
# 🌐 NETWORK - LACP CHECK
# Fish Music Inc - CB_01

echo "🔍 Checking LACP (Link Aggregation)..."
echo ""

# Check if running on macOS
if [[ "$(uname)" != "Darwin" ]]; then
    echo "⚠️  This script is for macOS (GABRIEL)"
    exit 0
fi

# List network interfaces
echo "Network Interfaces:"
networksetup -listallhardwareports

echo ""
echo "Active Interfaces:"
ifconfig | grep "^[a-z]" | grep -v "lo0" | cut -d: -f1

echo ""
echo "📊 Link Status:"
for iface in $(ifconfig | grep "^en" | cut -d: -f1); do
    STATUS=$(ifconfig "$iface" | grep status | awk '{print $2}')
    MTU=$(ifconfig "$iface" | grep mtu | awk '{print $6}')
    echo "   $iface: $STATUS (MTU: $MTU)"
done

echo ""
echo "💡 Note: LACP requires multiple physical ports"
echo "   Mac Studio typically uses single gigabit port"
echo "   MC96 supports LACP on ports 9-10"
echo ""
echo "🔥 GORUNFREE! 🎸🔥"
