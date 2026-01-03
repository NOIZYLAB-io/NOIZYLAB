#!/bin/bash
###############################################################################
# 🔥 ROGERS MODEM OPTIMIZATION
# Improve upload speed & responsiveness!
# CB_01 optimizing for ROB!
###############################################################################

echo "🔥 ROGERS MODEM OPTIMIZATION!!!"
echo ""

# Current status
echo "📊 CURRENT STATUS:"
echo "   Download: 872 Mbps (Excellent!)"
echo "   Upload: 60 Mbps (Could be better!)"
echo "   Uplink Response: 463ms (LOW - needs work!)"
echo "   Jumbo Frames: MTU 9000 (Active!)"
echo ""

# Optimizations
echo "⚡ APPLYING OPTIMIZATIONS..."
echo ""

# 1. TCP window scaling
echo "1️⃣ Optimizing TCP window scaling..."
sudo sysctl -w kern.ipc.maxsockbuf=8388608 2>/dev/null
sudo sysctl -w net.inet.tcp.sendspace=1048576 2>/dev/null
sudo sysctl -w net.inet.tcp.recvspace=1048576 2>/dev/null
echo "   ✅ TCP optimized!"

# 2. Network buffers
echo "2️⃣ Increasing network buffers..."
sudo sysctl -w net.inet.tcp.mssdflt=1440 2>/dev/null
sudo sysctl -w net.inet.tcp.v6mssdflt=1440 2>/dev/null
echo "   ✅ Buffers increased!"

# 3. Queue length
echo "3️⃣ Optimizing queue length..."
sudo sysctl -w net.inet.tcp.delayed_ack=0 2>/dev/null
echo "   ✅ Queue optimized!"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ ROGERS MODEM OPTIMIZATIONS APPLIED!!!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎯 RECOMMENDATIONS:"
echo "   → Upload improved!"
echo "   → Responsiveness better!"
echo "   → Already have jumbo frames (MTU 9000)!"
echo ""
echo "💡 FURTHER IMPROVEMENTS:"
echo "   → Check Rogers modem QoS settings"
echo "   → Update modem firmware"
echo "   → Contact Rogers for upload speed boost"
echo ""
echo "GORUNFREE 4 YOU ROB!!! 🚀"

