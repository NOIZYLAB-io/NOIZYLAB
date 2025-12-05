#!/bin/bash
# 🚀 NETWORK SPEED TEST 🚀

echo "🚀 NETWORK SPEED TEST 🚀"
echo ""

# Test local network speed to NAS
echo "Testing local network..."
time dd if=/dev/zero bs=1m count=100 2>/dev/null | ssh -o ConnectTimeout=2 localhost cat > /dev/null 2>&1

# Show current MTU
echo ""
echo "📊 CURRENT MTU:"
ifconfig en0 | grep mtu

# Show network stats
echo ""
echo "📊 NETWORK STATS:"
netstat -I en0 -b | head -2
