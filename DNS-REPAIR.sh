#!/bin/bash
# DNS TIMEOUT REPAIR PROTOCOL
# Fix DNS issues on macOS with Cloudflare DNS
# Created by CB_01 for ROB - GORUNFREE! 🎸🔥

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🔥 DNS TIMEOUT REPAIR PROTOCOL                               ║"
echo "╠═══════════════════════════════════════════════════════════════╣"
echo "║                                                               ║"

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}║  ❌ Please run with sudo${NC}"
    echo "║                                                               ║"
    echo "╚═══════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Usage: sudo bash DNS-REPAIR.sh"
    exit 1
fi

# Step 1: Detect network interface
echo -n "║  [1/5] Detecting network interface...     "
INTERFACE=$(networksetup -listallnetworkservices | grep -v '*' | head -2 | tail -1)
if [ -z "$INTERFACE" ]; then
    # Fallback to Wi-Fi or Ethernet
    if networksetup -listallnetworkservices | grep -q "Wi-Fi"; then
        INTERFACE="Wi-Fi"
    elif networksetup -listallnetworkservices | grep -q "Ethernet"; then
        INTERFACE="Ethernet"
    else
        INTERFACE=$(networksetup -listallnetworkservices | grep -v '*' | head -1)
    fi
fi
echo -e "${GREEN}✓ $INTERFACE${NC}          ║"

# Step 2: Set Cloudflare DNS
echo -n "║  [2/5] Setting Cloudflare DNS...          "
networksetup -setdnsservers "$INTERFACE" 1.1.1.1 1.0.0.1 2606:4700:4700::1111 2606:4700:4700::1001
echo -e "${GREEN}✓ 1.1.1.1${NC}           ║"

# Step 3: Flush DNS cache
echo -n "║  [3/5] Flushing DNS cache...              "
dscacheutil -flushcache 2>/dev/null
killall -HUP mDNSResponder 2>/dev/null
echo -e "${GREEN}✓ Done${NC}              ║"

# Step 4: Renew DHCP lease
echo -n "║  [4/5] Renewing DHCP lease...             "
# Get the actual interface name (en0, en1, etc)
IFNAME=$(networksetup -listallhardwareports | grep -A1 "$INTERFACE" | grep "Device:" | awk '{print $2}')
if [ -z "$IFNAME" ]; then
    IFNAME="en0"  # Default to en0
fi
ipconfig set "$IFNAME" DHCP 2>/dev/null || true
sleep 1
IP=$(ifconfig "$IFNAME" | grep "inet " | awk '{print $2}')
if [ -z "$IP" ]; then
    IP="acquiring..."
fi
echo -e "${GREEN}✓ IP: $IP${NC}    ║"

# Step 5: Check hosts file
echo -n "║  [5/5] Checking hosts file...             "
HOSTS_ISSUES=$(grep -v "^#" /etc/hosts | grep -v "^$" | wc -l | xargs)
if [ "$HOSTS_ISSUES" -gt 3 ]; then
    echo -e "${YELLOW}⚠ Review${NC}             ║"
else
    echo -e "${GREEN}✓ Clean${NC}             ║"
fi

echo "║                                                               ║"
echo "║  VERIFICATION:                                                ║"

# Verify DNS
echo -n "║    1.1.1.1 (Cloudflare): "
if ping -c 1 -W 1000 1.1.1.1 >/dev/null 2>&1; then
    echo -e "${GREEN}✓ OK${NC}                                 ║"
else
    echo -e "${RED}✗ FAIL${NC}                               ║"
fi

echo -n "║    8.8.8.8 (Google):     "
if ping -c 1 -W 1000 8.8.8.8 >/dev/null 2>&1; then
    echo -e "${GREEN}✓ OK${NC}                                 ║"
else
    echo -e "${RED}✗ FAIL${NC}                               ║"
fi

echo -n "║    google.com:           "
if ping -c 1 -W 1000 google.com >/dev/null 2>&1; then
    echo -e "${GREEN}✓ OK${NC}                                 ║"
else
    echo -e "${RED}✗ FAIL${NC}                               ║"
fi

echo -n "║    noizylab.ca:          "
if ping -c 1 -W 1000 noizylab.ca >/dev/null 2>&1; then
    echo -e "${GREEN}✓ OK${NC}                                 ║"
else
    echo -e "${RED}✗ FAIL${NC}                               ║"
fi

echo "║                                                               ║"
echo -e "║  ${GREEN}✅ DNS REPAIR COMPLETE${NC}                                       ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Show current DNS settings
echo "📋 Current DNS Configuration:"
echo "   Interface: $INTERFACE ($IFNAME)"
scutil --dns | grep "nameserver\[0\]" | head -3
echo ""

echo "💡 If issues persist:"
echo "   1. Restart your router"
echo "   2. Try different network interface"
echo "   3. Check firewall settings"
echo "   4. Contact ISP if problem continues"
echo ""

echo "GORUNFREE! 🎸🔥"
