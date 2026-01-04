#!/bin/bash
# ==============================================================================
# NOIZYLAB QUICK STATUS - One-liner system check
# Usage: status.sh
# ==============================================================================

# Colors
G='\033[0;32m'
Y='\033[1;33m'
R='\033[0;31m'
N='\033[0m'

# Quick checks
NOIZY=$(curl -s -m 3 https://noizy.ai/ 2>/dev/null | grep -q "HEAVEN" && echo "✅" || echo "❌")
HEAVEN=$(curl -s -m 3 -o /dev/null -w "%{http_code}" https://heaven.noizy.ai/ 2>/dev/null)
MEM=$(memory_pressure 2>/dev/null | grep "free percentage" | awk '{print $5}' || echo "?")
DISK=$(df -h / | tail -1 | awk '{print $4}')

echo ""
echo "⚡ NOIZYLAB STATUS $(date '+%H:%M')"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "   noizy.ai     $NOIZY"
echo "   heaven       $([[ $HEAVEN == "200" ]] && echo "✅" || echo "⚠️ $HEAVEN")"
echo "   memory       $MEM"
echo "   disk         $DISK"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
