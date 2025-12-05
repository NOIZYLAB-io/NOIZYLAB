#!/bin/bash
# 🔄 SYNCTHING - REAL-TIME SYNC
# Fish Music Inc - CB_01

echo "🔄 Starting Syncthing..."

# Kill existing
pkill -x syncthing

# Start Syncthing
syncthing \
    -no-browser \
    -logflags=0 \
    >/tmp/syncthing.log 2>&1 &

sleep 2

# Verify
if pgrep -x "syncthing" >/dev/null; then
    echo "✅ Syncthing online"
    echo "   Web UI: http://localhost:8384"
    echo "   API: http://localhost:8384/rest/"
else
    echo "❌ Syncthing failed to start"
    echo "   Check: /tmp/syncthing.log"
    exit 1
fi
