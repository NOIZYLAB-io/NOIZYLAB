#!/bin/bash
# FISH MUSIC INC - QUICK STATUS
# Ultra-fast system status check
# Created by CB_01 for ROB - GORUNFREE! 🎸🔥

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo ""
echo "⚡ FISH MUSIC INC - QUICK STATUS"
echo "════════════════════════════════════════════════════"

# Network
MTU=$(ifconfig en0 | grep mtu | awk '{print $4}')
IP=$(ifconfig en0 | grep "inet " | awk '{print $2}')
if [ "$MTU" -eq 9000 ]; then
    echo -e "🌐 Network:  ${GREEN}✅ HOT ROD (MTU $MTU @ $IP)${NC}"
else
    echo -e "🌐 Network:  ${YELLOW}⚠️  Standard (MTU $MTU)${NC}"
fi

# DNS
if scutil --dns | grep -q "1.1.1.1"; then
    echo -e "🔧 DNS:      ${GREEN}✅ Cloudflare (1.1.1.1)${NC}"
else
    echo -e "🔧 DNS:      ${YELLOW}⚠️  Not optimal${NC}"
fi

# Volumes
VOL_COUNT=$(ls /Volumes/ 2>/dev/null | wc -l | xargs)
echo -e "💾 Volumes:  ${GREEN}✅ $VOL_COUNT mounted${NC}"

# 4TB Lacie check
if ls /Volumes/ 2>/dev/null | grep -q "4TB Lacie"; then
    echo -e "🎬 Design:   ${GREEN}✅ 4TB Lacie mounted (stems ready!)${NC}"
else
    echo -e "🎬 Design:   ${YELLOW}⚠️  4TB Lacie not mounted${NC}"
fi

# Disk space
DISK=$(df -h / | tail -1 | awk '{print $5}')
echo -e "💽 Disk:     ${GREEN}✅ $DISK used${NC}"

# Git status
cd "$(dirname "$0")/../.."
if git status --porcelain | grep -q .; then
    CHANGES=$(git status --porcelain | wc -l | xargs)
    echo -e "📦 Git:      ${YELLOW}⚠️  $CHANGES uncommitted changes${NC}"
else
    echo -e "📦 Git:      ${GREEN}✅ Clean${NC}"
fi

echo "════════════════════════════════════════════════════"
echo "GORUNFREE! 🎸🔥"
echo ""

