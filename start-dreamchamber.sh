#!/bin/bash
# THE DREAMCHAMBER LAUNCHER
# GORUNFREE X1000

echo "✨ THE DREAMCHAMBER ✨"
echo "====================="
echo ""
echo "Starting unified AI interface..."
echo ""

# Check if node is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found"
    echo "Install: brew install node"
    exit 1
fi

# Start the server
cd "$(dirname "$0")"
node dreamchamber.js

# Note: Server runs on port 7777
# Access at:
#   http://localhost:7777 (from GOD)
#   http://GOD.local:7777 (from other Macs)
#   http://10.90.90.x:7777 (from iPad)
