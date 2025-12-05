#!/bin/bash
# 🔥 OMEGA SYSTEM - SELF-HEALING 🔥
# Fish Music Inc - CB_01

echo ""
echo "🔧 OMEGA BRAIN SELF-HEAL SEQUENCE"
echo ""

# ==================== NETWORK HEAL ====================
echo "[1/5] Healing network stack..."
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
echo "      ✅ DNS flushed"

# Test connectivity
echo "      Testing gateway..."
ping -c 3 192.168.1.1 >/dev/null 2>&1 && echo "      ✅ Gateway reachable" || echo "      ❌ Gateway unreachable"

# ==================== SERVICE HEAL ====================
echo ""
echo "[2/5] Checking core services..."

# Redis
if ! pgrep -x "redis-server" >/dev/null; then
    echo "      [!] Restarting Redis..."
    redis-server --daemonize yes --bind 0.0.0.0
fi

# Ray
if ! ray status >/dev/null 2>&1; then
    echo "      [!] Restarting Ray..."
    ray start --head --port=6379 --dashboard-host=0.0.0.0 >/dev/null 2>&1
fi

# Syncthing
if ! pgrep -x "syncthing" >/dev/null; then
    echo "      [!] Restarting Syncthing..."
    syncthing -no-browser >/tmp/syncthing.log 2>&1 &
fi

# MQTT
if ! lsof -i :1883 >/dev/null 2>&1; then
    echo "      [!] Restarting MQTT..."
    brew services restart mosquitto >/dev/null 2>&1
fi

# NOIZYLAB Agent
if ! pgrep -f "noizylab_agent.py" >/dev/null; then
    echo "      [!] Restarting NOIZYLAB Agent..."
    cd ../agent
    python3 noizylab_agent.py --machine gabriel >/tmp/noizylab_agent.log 2>&1 &
    cd - >/dev/null
fi

echo "      ✅ Services healed"

# ==================== SMB HEAL ====================
echo ""
echo "[3/5] Checking SMB..."
if sharing -l >/dev/null 2>&1; then
    echo "      ✅ SMB shares active"
else
    echo "      ⚠️  SMB may need manual configuration"
fi

# ==================== MTU HEAL ====================
echo ""
echo "[4/5] Verifying jumbo frames..."
INTERFACE=$(route -n get default 2>/dev/null | grep interface | awk '{print $2}')
CURRENT_MTU=$(ifconfig "$INTERFACE" 2>/dev/null | grep mtu | awk '{print $6}')

if [ "$CURRENT_MTU" -lt 9000 ]; then
    echo "      [!] Setting MTU to 9000..."
    sudo networksetup -setMTU "$INTERFACE" 9000 2>/dev/null || echo "      (Needs manual config)"
else
    echo "      ✅ MTU: $CURRENT_MTU (Jumbo enabled)"
fi

# ==================== SYNC HEAL ====================
echo ""
echo "[5/5] Checking Syncthing sync..."
if curl -s http://localhost:8384/rest/system/status >/dev/null 2>&1; then
    echo "      ✅ Syncthing API responding"
else
    echo "      ⚠️  Syncthing may need restart"
fi

# ==================== FINAL STATUS ====================
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ OMEGA BRAIN HEAL COMPLETE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔥 System Status:"
pgrep -x "redis-server" >/dev/null && echo "   ✅ Redis" || echo "   ❌ Redis"
ray status >/dev/null 2>&1 && echo "   ✅ Ray" || echo "   ❌ Ray"
pgrep -x "syncthing" >/dev/null && echo "   ✅ Syncthing" || echo "   ❌ Syncthing"
lsof -i :1883 >/dev/null 2>&1 && echo "   ✅ MQTT" || echo "   ❌ MQTT"
pgrep -f "noizylab_agent" >/dev/null && echo "   ✅ NOIZYLAB Agent" || echo "   ❌ NOIZYLAB Agent"
echo ""
echo "🔥 GORUNFREE! 🎸🔥"
echo ""
