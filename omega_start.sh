#!/bin/bash
# 🔥 OMEGA SYSTEM - MASTER BOOT SEQUENCE 🔥
# Fish Music Inc - CB_01

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║          🔥 OMEGA BRAIN INITIALIZATION 🔥                     ║"
echo "║                                                               ║"
echo "║               GABRIEL ↔ OMEN SUPER-MESH                      ║"
echo "║                  Fish Music Inc - CB_01                       ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

OMEGA_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$OMEGA_DIR"

# ==================== PRE-FLIGHT CHECKS ====================
echo "🔍 Pre-flight checks..."
echo ""

# Check if running on macOS
if [[ "$(uname)" != "Darwin" ]]; then
    echo "❌ This script must run on GABRIEL (macOS)"
    exit 1
fi

# Check network interface
INTERFACE=$(route -n get default 2>/dev/null | grep interface | awk '{print $2}')
if [ -z "$INTERFACE" ]; then
    echo "⚠️  Could not detect network interface"
    INTERFACE="en0"
fi

MTU=$(ifconfig "$INTERFACE" 2>/dev/null | grep mtu | awk '{print $6}')
echo "   Network: $INTERFACE (MTU: $MTU)"

if [ "$MTU" -ge 9000 ]; then
    echo "   ✅ Jumbo frames enabled"
else
    echo "   ⚠️  Jumbo frames NOT enabled (MTU should be 9000+)"
fi

echo ""

# ==================== PHASE 1: NETWORK LAYER ====================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🌐 PHASE 1: NETWORK LAYER"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check Tailscale
if command -v tailscale >/dev/null 2>&1; then
    if tailscale status >/dev/null 2>&1; then
        echo "✅ Tailscale: Connected"
    else
        echo "⚠️  Tailscale: Not connected (run: tailscale up)"
    fi
else
    echo "⚠️  Tailscale: Not installed"
fi

echo ""

# ==================== PHASE 2: CORE SERVICES ====================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🧠 PHASE 2: CORE SERVICES"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Start Redis
echo "[1/5] Starting Redis (Shared Memory)..."
if [ -f core/redis/start_redis.sh ]; then
    ./core/redis/start_redis.sh
else
    redis-server --daemonize yes --bind 0.0.0.0 >/dev/null 2>&1 || echo "   (Redis install needed)"
fi
sleep 1
if pgrep -x "redis-server" >/dev/null; then
    echo "      ✅ Redis online (port 6379)"
else
    echo "      ⚠️  Redis not running"
fi

# Start Ray cluster head
echo ""
echo "[2/5] Starting Ray Cluster (Distributed Compute)..."
if [ -f core/ray/start_head.sh ]; then
    ./core/ray/start_head.sh
else
    ray start --head --port=6379 --dashboard-host=0.0.0.0 >/dev/null 2>&1 || echo "   (Ray install needed)"
fi
sleep 2
if ray status >/dev/null 2>&1; then
    echo "      ✅ Ray cluster HEAD online"
    echo "      📊 Dashboard: http://localhost:8265"
else
    echo "      ⚠️  Ray cluster not running"
fi

# Start Syncthing
echo ""
echo "[3/5] Starting Syncthing (Real-time Sync)..."
if [ -f core/syncthing/start_syncthing.sh ]; then
    ./core/syncthing/start_syncthing.sh
else
    syncthing -no-browser >/tmp/syncthing.log 2>&1 &
fi
sleep 2
if pgrep -x "syncthing" >/dev/null; then
    echo "      ✅ Syncthing online"
    echo "      🌐 Web UI: http://localhost:8384"
else
    echo "      ⚠️  Syncthing not running"
fi

# Start MQTT Broker
echo ""
echo "[4/5] Starting MQTT Broker (Telemetry)..."
brew services start mosquitto >/dev/null 2>&1
sleep 1
if lsof -i :1883 >/dev/null 2>&1; then
    echo "      ✅ MQTT broker online (port 1883)"
else
    echo "      ⚠️  MQTT broker not running"
fi

# Start NOIZYLAB Agent
echo ""
echo "[5/5] Starting NOIZYLAB Agent (System Monitor)..."
if [ -f ../agent/noizylab_agent.py ]; then
    cd ../agent
    python3 noizylab_agent.py --machine gabriel >/tmp/noizylab_agent.log 2>&1 &
    cd - >/dev/null
    sleep 2
    if pgrep -f "noizylab_agent.py" >/dev/null; then
        echo "      ✅ NOIZYLAB Agent online"
    else
        echo "      ⚠️  NOIZYLAB Agent failed to start"
    fi
else
    echo "      ⚠️  NOIZYLAB Agent not found"
fi

echo ""

# ==================== PHASE 3: EXTENSIONS ====================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "⚡ PHASE 3: EXTENSIONS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Clipboard sync
if [ -f extensions/clipboard/start_clipboard_sync.sh ]; then
    echo "[+] Clipboard sync..."
    ./extensions/clipboard/start_clipboard_sync.sh
fi

# Dashboard
if [ -f extensions/dashboard/start_netdata.sh ]; then
    echo "[+] Starting dashboard..."
    ./extensions/dashboard/start_netdata.sh
fi

# Semantic FS
if [ -f extensions/semantic_fs/index_files.py ]; then
    echo "[+] Indexing files (semantic)..."
    python3 extensions/semantic_fs/index_files.py &
fi

echo "      ✅ Extensions loaded"
echo ""

# ==================== SYSTEM STATUS ====================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 OMEGA BRAIN STATUS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Services:"
echo "  ├─ Redis         → port 6379           $(pgrep redis-server >/dev/null && echo "✅" || echo "❌")"
echo "  ├─ Ray Cluster   → http://localhost:8265   $(ray status >/dev/null 2>&1 && echo "✅" || echo "❌")"
echo "  ├─ Syncthing     → http://localhost:8384   $(pgrep syncthing >/dev/null && echo "✅" || echo "❌")"
echo "  ├─ MQTT          → port 1883           $(lsof -i :1883 >/dev/null 2>&1 && echo "✅" || echo "❌")"
echo "  └─ NOIZYLAB      → agent running       $(pgrep -f noizylab_agent >/dev/null && echo "✅" || echo "❌")"
echo ""
echo "Network:"
echo "  ├─ Interface     → $INTERFACE"
echo "  ├─ MTU           → $MTU bytes"
echo "  └─ Tailscale     → $(tailscale status >/dev/null 2>&1 && echo "Connected ✅" || echo "Not connected ⚠️")"
echo ""
echo "Logs:"
echo "  ├─ Redis         → /usr/local/var/log/redis.log"
echo "  ├─ Syncthing     → /tmp/syncthing.log"
echo "  ├─ NOIZYLAB      → /tmp/noizylab_agent_gabriel.log"
echo "  └─ OMEGA         → /tmp/omega_system.log"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║              🚀 OMEGA BRAIN ONLINE 🚀                         ║"
echo "║                                                               ║"
echo "║                   GORUNFREE! 🎸🔥                             ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "🎯 Next: Run ./omega_heal.sh to verify connectivity"
echo "   Or: cd ~/OMEGA_BUILD && ./verify.sh"
echo ""
