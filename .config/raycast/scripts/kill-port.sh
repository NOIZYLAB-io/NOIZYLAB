#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Kill Port
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 🔪
# @raycast.argument1 { "type": "text", "placeholder": "Port number" }
# @raycast.packageName Developer

# Documentation:
# @raycast.description Kill process running on a specific port
# @raycast.author NOIZYLAB

port="$1"

pid=$(lsof -ti ":$port" 2>/dev/null)

if [[ -n "$pid" ]]; then
    kill -9 $pid
    echo "Killed process $pid on port $port"
else
    echo "No process found on port $port"
fi
