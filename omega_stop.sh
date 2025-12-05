#!/bin/bash
# 🔥 OMEGA SYSTEM - MASTER SHUTDOWN 🔥
# Fish Music Inc - CB_01

echo ""
echo "🛑 Shutting down OMEGA BRAIN..."
echo ""

# Stop NOIZYLAB Agent
echo "[1/5] Stopping NOIZYLAB Agent..."
pkill -f "noizylab_agent.py"
echo "      ✅ Agent stopped"

# Stop MQTT
echo "[2/5] Stopping MQTT broker..."
brew services stop mosquitto >/dev/null 2>&1
echo "      ✅ MQTT stopped"

# Stop Syncthing
echo "[3/5] Stopping Syncthing..."
pkill -x "syncthing"
echo "      ✅ Syncthing stopped"

# Stop Ray
echo "[4/5] Stopping Ray cluster..."
ray stop >/dev/null 2>&1
echo "      ✅ Ray stopped"

# Stop Redis
echo "[5/5] Stopping Redis..."
redis-cli shutdown >/dev/null 2>&1
echo "      ✅ Redis stopped"

echo ""
echo "✅ OMEGA BRAIN offline"
echo ""
echo "🔥 GORUNFREE! 🎸🔥"
echo ""
