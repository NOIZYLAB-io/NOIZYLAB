#!/bin/bash
set -e
echo "🔧 Installing Noizy.ai Mission Control..."
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt stripe fastapi pyyaml jwt

echo "✅ Environment ready."
echo "Starting MCP + Mission Control..."
nohup python3 mcp_server.py &
nohup python3 mission_control.py &
echo "🎛️  Mission Control is live at http://127.0.0.1:8765/dashboard"