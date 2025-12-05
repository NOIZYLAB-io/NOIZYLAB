#!/bin/bash
# GOD Network Diagnostics - Full network health check
# CB_01 - Fish Music Inc
# GORUNFREE! 🎸🔥

# Colors
G='\033[0;32m'
Y='\033[1;33m'
C='\033[0;36m'
M='\033[0;35m'
R='\033[0;31m'
B='\033[1m'
NC='\033[0m'

echo ""
echo -e "${B}${M}🌐 GOD NETWORK DIAGNOSTICS${NC}"
echo -e "${C}MC96ECOUNIVERSE Integration${NC}"
echo ""

echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${B}${Y}📡 NETWORK INTERFACES:${NC}"
echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Get active interface
ACTIVE_IF=$(route get default 2>/dev/null | grep interface | awk '{print $2}')
echo -e "${G}Active Interface: ${B}$ACTIVE_IF${NC}"
echo ""

# IP addresses
echo -e "${C}IP Addresses:${NC}"
ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print "  " $2}'
echo ""

# External IP
echo -e "${C}External IP:${NC}"
EXT_IP=$(curl -s --max-time 5 ifconfig.me 2>/dev/null || echo "Could not determine")
echo -e "  ${G}$EXT_IP${NC}"
echo ""

echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${B}${Y}🔧 DNS CONFIGURATION:${NC}"
echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Check Wi-Fi DNS
echo -e "${C}Wi-Fi DNS:${NC}"
networksetup -getdnsservers "Wi-Fi" 2>/dev/null || echo "  Not configured"
echo ""

# Check Ethernet DNS
echo -e "${C}Ethernet DNS:${NC}"
networksetup -getdnsservers "Ethernet" 2>/dev/null || echo "  Not configured"
echo ""

# Check if Cloudflare
DNS_CHECK=$(networksetup -getdnsservers "Wi-Fi" 2>/dev/null | head -1)
if [[ "$DNS_CHECK" == "1.1.1.1" ]]; then
    echo -e "${G}✅ Cloudflare DNS Active (Optimized)${NC}"
else
    echo -e "${Y}⚠️  DNS not optimized - consider Cloudflare (1.1.1.1)${NC}"
fi
echo ""

echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${B}${Y}📶 CONNECTION TESTS:${NC}"
echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Ping tests
echo -e "${C}Testing connectivity...${NC}"
echo ""

# Cloudflare
CF_PING=$(ping -c 3 -t 5 1.1.1.1 2>/dev/null | tail -1 | awk -F'/' '{print $5}')
if [ -n "$CF_PING" ]; then
    echo -e "${G}✅ Cloudflare (1.1.1.1): ${CF_PING}ms${NC}"
else
    echo -e "${R}❌ Cloudflare (1.1.1.1): Failed${NC}"
fi

# Google
GOOGLE_PING=$(ping -c 3 -t 5 8.8.8.8 2>/dev/null | tail -1 | awk -F'/' '{print $5}')
if [ -n "$GOOGLE_PING" ]; then
    echo -e "${G}✅ Google (8.8.8.8): ${GOOGLE_PING}ms${NC}"
else
    echo -e "${R}❌ Google (8.8.8.8): Failed${NC}"
fi

# Apple
APPLE_PING=$(ping -c 3 -t 5 apple.com 2>/dev/null | tail -1 | awk -F'/' '{print $5}')
if [ -n "$APPLE_PING" ]; then
    echo -e "${G}✅ Apple.com: ${APPLE_PING}ms${NC}"
else
    echo -e "${R}❌ Apple.com: Failed${NC}"
fi

echo ""

echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${B}${Y}⚡ SPEED TEST (Quick):${NC}"
echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Quick download test
echo -e "${C}Testing download speed...${NC}"
START=$(date +%s.%N)
curl -s -o /dev/null --max-time 10 "https://speed.cloudflare.com/__down?bytes=10000000" 2>/dev/null
END=$(date +%s.%N)
DURATION=$(echo "$END - $START" | bc 2>/dev/null || echo "0")
if [ "$DURATION" != "0" ] && [ -n "$DURATION" ]; then
    SPEED=$(echo "scale=1; 10 / $DURATION * 8" | bc 2>/dev/null || echo "N/A")
    echo -e "${G}Download: ~${SPEED} Mbps${NC}"
else
    echo -e "${Y}Speed test unavailable${NC}"
fi
echo ""

echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${B}${Y}🔌 CONNECTED DEVICES (Local Network):${NC}"
echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# ARP table
arp -a 2>/dev/null | head -15 | while read line; do
    echo -e "  ${C}$line${NC}"
done
echo ""

echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${B}${Y}📊 NETWORK STATISTICS:${NC}"
echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo ""

netstat -i | head -5
echo ""

echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${G}${B}✅ NETWORK DIAGNOSTICS COMPLETE${NC}"
echo ""
echo -e "${B}${M}GORUNFREE! 🎸🔥${NC}"
echo ""
