#!/bin/bash
# Quick SPF Setup Helper for noizyfish.com
# =========================================

DOMAIN="noizyfish.com"
GODADDY_URL="https://dcc.godaddy.com/control/portfolio/${DOMAIN}/settings"

echo "🚀 Quick SPF Setup for ${DOMAIN}"
echo "================================"
echo ""
echo "📋 Recommended SPF Record (Microsoft 365 Only):"
echo "   v=spf1 include:spf.protection.outlook.com -all"
echo ""
echo "📋 Hybrid SPF Record (Microsoft 365 + GoDaddy):"
echo "   v=spf1 include:spf.protection.outlook.com include:secureserver.net -all"
echo ""
echo "🔗 GoDaddy DNS Settings:"
echo "   ${GODADDY_URL}"
echo ""
echo "📝 Setup Steps:"
echo "   1. Go to GoDaddy DNS settings (link above)"
echo "   2. Add TXT record:"
echo "      Type: TXT"
echo "      Name: @"
echo "      Value: v=spf1 include:spf.protection.outlook.com -all"
echo "   3. Save and wait 5-15 minutes"
echo ""
echo "✅ Verify with:"
echo "   dig TXT ${DOMAIN} | grep spf"
echo ""
echo "🔍 Check existing records first:"
echo "   dig TXT ${DOMAIN}"
echo ""

# Check if dig is available
if command -v dig &> /dev/null; then
    echo "📊 Current DNS Records:"
    dig TXT ${DOMAIN} +short 2>/dev/null | grep -i spf || echo "   No SPF record found yet"
    echo ""
fi

echo "💡 Tip: Use Microsoft 365 only unless you actually send from GoDaddy!"
echo ""

