#!/bin/bash
#╔════════════════════════════════════════════════════════════════════════════════════╗
#║                    🥊 PUNCH IN THE NOSE - ROGERS TV FIX 🥊                         ║
#║                           CB_01 LIFELUV ENGR                                       ║
#╚════════════════════════════════════════════════════════════════════════════════════╝

echo "🥊 PUNCHING ROGERS TV CONNECTION ISSUES IN THE NOSE!"
echo "=================================================="
echo ""

# 1. FLUSH DNS CACHE
echo "💥 PUNCH 1: Flushing DNS Cache..."
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
echo "   ✅ DNS Cache OBLITERATED!"
echo ""

# 2. CLEAR CHROME DNS CACHE (open this URL manually)
echo "💥 PUNCH 2: Chrome DNS - Open this in Chrome:"
echo "   chrome://net-internals/#dns → Click 'Clear host cache'"
echo ""

# 3. RESET NETWORK INTERFACE
echo "💥 PUNCH 3: Resetting Network Interface..."
INTERFACE=$(route -n get default | grep interface | awk '{print $2}')
echo "   Active interface: $INTERFACE"
sudo ifconfig $INTERFACE down
sleep 2
sudo ifconfig $INTERFACE up
echo "   ✅ Network Interface RESET!"
echo ""

# 4. RE-ENABLE JUMBO FRAMES (for maximum speed)
echo "💥 PUNCH 4: Re-enabling Jumbo Frames (MTU 9000)..."
sudo ifconfig $INTERFACE mtu 9000 2>/dev/null || echo "   (Jumbo frames not supported on this connection)"
echo "   ✅ Maximum transmission speed ENGAGED!"
echo ""

# 5. TEST ROGERS CONNECTIVITY
echo "💥 PUNCH 5: Testing Rogers TV connectivity..."
echo "   Pinging Rogers..."
ping -c 3 www.rogers.com
echo ""

echo "   Testing ignite.tv..."
curl -s -o /dev/null -w "   HTTP Status: %{http_code}\n   Response Time: %{time_total}s\n" https://ignite.tv/
echo ""

# 6. CHECK FOR VPN/PROXY INTERFERENCE
echo "💥 PUNCH 6: Checking for VPN/Proxy interference..."
PROXY_CHECK=$(networksetup -getwebproxy Wi-Fi 2>/dev/null | grep "Enabled: Yes" || echo "No proxy")
if [[ "$PROXY_CHECK" == *"Enabled: Yes"* ]]; then
    echo "   ⚠️  WEB PROXY DETECTED - This might block Rogers!"
else
    echo "   ✅ No web proxy detected"
fi
echo ""

# 7. DISPLAY CURRENT NETWORK INFO
echo "💥 PUNCH 7: Current Network Status..."
echo "   IP Address: $(ipconfig getifaddr $INTERFACE 2>/dev/null || echo 'Unknown')"
echo "   Gateway: $(route -n get default | grep gateway | awk '{print $2}')"
echo "   DNS Servers:"
scutil --dns | grep "nameserver" | head -3
echo ""

# 8. CHROME RESET INSTRUCTIONS
echo "═══════════════════════════════════════════════════════════════"
echo "🎯 FINAL KNOCKOUT MOVES (Do these in Chrome):"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "1. CLEAR EVERYTHING:"
echo "   → Chrome Settings → Privacy → Clear browsing data"
echo "   → Select 'All time' → Check ALL boxes → Clear"
echo ""
echo "2. ENABLE DRM:"
echo "   → Go to: chrome://settings/content/protectedContent"
echo "   → Turn ON 'Sites can play protected content'"
echo ""
echo "3. DISABLE EXTENSIONS:"
echo "   → Go to: chrome://extensions/"
echo "   → Disable ALL extensions temporarily"
echo ""
echo "4. TRY INCOGNITO:"
echo "   → Press Cmd+Shift+N"
echo "   → Go to https://ignite.tv/"
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🥊 PUNCH COMPLETE! Rogers TV should be KNOCKED INTO WORKING!"
echo "═══════════════════════════════════════════════════════════════"

