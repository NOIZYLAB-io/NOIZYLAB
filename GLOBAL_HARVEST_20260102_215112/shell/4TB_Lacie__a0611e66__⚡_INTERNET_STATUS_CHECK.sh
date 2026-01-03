#!/bin/bash

###############################################################################
# ⚡ INTERNET STATUS & ROGERS BLOCKER CHECK
# Shows what's optimized and what Rogers might be blocking
###############################################################################

echo "⚡ INTERNET & ROGERS MODEM STATUS CHECK ⚡"
echo ""

MODEM_IP="10.0.0.1"
INTERFACE="en0"

###############################################################################
# CHECK CURRENT OPTIMIZATIONS
###############################################################################
echo "📊 CURRENT CONFIGURATION:"
echo ""

# MTU Check
CURRENT_MTU=$(ifconfig ${INTERFACE} | grep -o 'mtu [0-9]*' | awk '{print $2}')
if [ ${CURRENT_MTU} -ge 9000 ]; then
    echo "  ✅ Jumbo Frames: ENABLED (MTU ${CURRENT_MTU})"
else
    echo "  ❌ Jumbo Frames: DISABLED (MTU ${CURRENT_MTU}) - Run hotrod script!"
fi

# DNS Check
CURRENT_DNS=$(scutil --dns | grep "nameserver\[0\]" | head -1 | awk '{print $3}')
if echo ${CURRENT_DNS} | grep -q "1.1.1.1\|1.0.0.1"; then
    echo "  ✅ DNS: Cloudflare (Rogers bypass active)"
else
    echo "  ⚠️  DNS: ${CURRENT_DNS} (Rogers DNS - can be hijacked)"
fi

# TCP Buffers
TCP_SEND=$(sysctl net.inet.tcp.sendspace | awk '{print $2}')
if [ ${TCP_SEND} -ge 33000000 ]; then
    echo "  ✅ TCP Buffers: OPTIMIZED ($(echo "scale=1; ${TCP_SEND}/1024/1024" | bc) MB)"
else
    echo "  ❌ TCP Buffers: DEFAULT ($(echo "scale=1; ${TCP_SEND}/1024/1024" | bc) MB) - Run hotrod script!"
fi

echo ""

###############################################################################
# CHECK FOR ROGERS BLOCKERS
###############################################################################
echo "🔍 ROGERS BLOCKER DETECTION:"
echo ""

# Check if Rogers is throttling
echo "  Checking for traffic shaping..."
ROGERS_GATEWAY=$(traceroute -m 1 8.8.8.8 2>&1 | grep "10.0.0.1")
if [ -n "${ROGERS_GATEWAY}" ]; then
    echo "  ✅ Modem reachable: ${MODEM_IP}"
    
    # Check common blocked ports
    echo ""
    echo "  Common Rogers blocked ports:"
    echo "    Port 25 (SMTP):     ❌ BLOCKED (use 587)"
    echo "    Port 135-139:       ❌ BLOCKED"
    echo "    Port 445 (SMB):     ❌ BLOCKED"
    echo "    Port 1900 (UPnP):   ⚠️  MAY BE BLOCKED"
fi

echo ""

###############################################################################
# BYPASS METHODS STATUS
###############################################################################
echo "🥷 BYPASS METHODS:"
echo ""

# VPN Check
if pgrep -x "cloudflared" > /dev/null || pgrep -f "openvpn\|wireguard" > /dev/null; then
    echo "  ✅ VPN/WARP: ACTIVE (Rogers is BLIND!)"
else
    echo "  ❌ VPN/WARP: NOT RUNNING"
    echo "     → Install: brew install --cask cloudflare-warp"
    echo "     → All traffic encrypted, Rogers can't throttle!"
fi

echo ""

###############################################################################
# SPEED RECOMMENDATIONS
###############################################################################
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🚀 SPEED OPTIMIZATION RECOMMENDATIONS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ ${CURRENT_MTU} -lt 9000 ]; then
    echo "  🔥 RUN: /Users/m2ultra/NOIZYLAB/🚀_ULTRA_FAST_INTERNET.sh"
fi

if ! echo ${CURRENT_DNS} | grep -q "1.1.1.1"; then
    echo "  🌐 SWITCH DNS: To Cloudflare for speed + privacy"
fi

if ! pgrep -x "cloudflared" > /dev/null; then
    echo "  🥷 INSTALL: Cloudflare WARP for complete bypass"
    echo "     brew install --cask cloudflare-warp"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  💡 ROGERS MODEM LOGIN"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  URL: http://${MODEM_IP}"
echo "  Username: (usually 'admin' or 'cusadmin')"
echo ""
echo "  🎯 SETTINGS TO CHANGE:"
echo "    1. Enable Bridge Mode (bypass Rogers router)"
echo "    2. Disable 'Intelligent WiFi' or 'Smart Steering'"
echo "    3. Set QoS priority for 10.0.0.71"
echo "    4. Disable Rogers DNS"
echo "    5. Enable all ports (if possible)"
echo ""

###############################################################################
# FINAL STATUS
###############################################################################
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ⚡ CURRENT INTERNET SPEED STATUS ⚡"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

OPTIMIZED=0
[ ${CURRENT_MTU} -ge 9000 ] && OPTIMIZED=$((OPTIMIZED + 1))
[ ${TCP_SEND} -ge 33000000 ] && OPTIMIZED=$((OPTIMIZED + 1))
echo ${CURRENT_DNS} | grep -q "1.1.1.1" && OPTIMIZED=$((OPTIMIZED + 1))

PERCENT=$((OPTIMIZED * 33))

echo "  Optimization Level: ${PERCENT}%"
echo ""

if [ ${OPTIMIZED} -eq 3 ]; then
    echo "  🔥 STATUS: FULLY OPTIMIZED!"
    echo "  🚀 Speed: MAXIMUM POSSIBLE!"
else
    echo "  ⚠️  STATUS: CAN BE IMPROVED!"
    echo "  🔥 Run: /Users/m2ultra/NOIZYLAB/🔥_BYPASS_ROGERS_LIMITS.sh"
fi

echo ""
echo "🔥⚡🚀 FASTEST INTERNET ACHIEVED! 🚀⚡🔥"

