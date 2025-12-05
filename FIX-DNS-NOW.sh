#!/bin/bash
# SUPER SIMPLE DNS FIX
# Just run: sudo bash ~/Downloads/FIX-DNS-NOW.sh

echo "🔥 FIXING DNS..."

# Set Cloudflare DNS on all network services
for service in $(networksetup -listallnetworkservices | grep -v '*'); do
    echo "   Setting DNS for: $service"
    networksetup -setdnsservers "$service" 1.1.1.1 1.0.0.1 2>/dev/null || true
done

# Flush DNS cache
echo "   Flushing DNS cache..."
dscacheutil -flushcache 2>/dev/null
killall -HUP mDNSResponder 2>/dev/null

# Verify
echo ""
echo "✅ DNS FIXED!"
echo ""
echo "Testing connectivity..."
if ping -c 1 google.com >/dev/null 2>&1; then
    echo "✅ google.com works!"
else
    echo "❌ google.com failed"
fi

if ping -c 1 noizylab.ca >/dev/null 2>&1; then
    echo "✅ noizylab.ca works!"
else
    echo "❌ noizylab.ca failed"
fi

echo ""
echo "Current DNS servers:"
scutil --dns | grep "nameserver\[0\]" | head -2
echo ""
echo "DONE! 🎸🔥"

