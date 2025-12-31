#!/bin/bash
#═══════════════════════════════════════════════════════════════
# 🤖 CODEMASTER Device Agent - Install Script
#═══════════════════════════════════════════════════════════════

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$SCRIPT_DIR"

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🤖 CODEMASTER DEVICE AGENT INSTALLER                         ║"
echo "╚═══════════════════════════════════════════════════════════════╝"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.9+"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "✅ Python $PYTHON_VERSION found"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv "$AGENT_DIR/venv"
source "$AGENT_DIR/venv/bin/activate"

# Install requirements
echo "📥 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r "$AGENT_DIR/requirements.txt"

# Create systemd service (Linux) or launchd plist (macOS)
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS launchd
    PLIST_PATH="$HOME/Library/LaunchAgents/com.codemaster.device-agent.plist"
    
    cat > "$PLIST_PATH" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.codemaster.device-agent</string>
    <key>ProgramArguments</key>
    <array>
        <string>$AGENT_DIR/venv/bin/python</string>
        <string>$AGENT_DIR/device_agent.py</string>
        <string>run</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>$AGENT_DIR/agent.log</string>
    <key>StandardErrorPath</key>
    <string>$AGENT_DIR/agent_error.log</string>
    <key>WorkingDirectory</key>
    <string>$AGENT_DIR</string>
</dict>
</plist>
EOF
    
    echo "✅ Created launchd plist: $PLIST_PATH"
    echo ""
    echo "📋 To start the agent:"
    echo "   launchctl load $PLIST_PATH"
    echo ""
    echo "📋 To stop the agent:"
    echo "   launchctl unload $PLIST_PATH"
    
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux systemd
    SYSTEMD_PATH="/etc/systemd/system/codemaster-agent.service"
    
    sudo tee "$SYSTEMD_PATH" > /dev/null << EOF
[Unit]
Description=CODEMASTER Device Agent
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$AGENT_DIR
ExecStart=$AGENT_DIR/venv/bin/python $AGENT_DIR/device_agent.py run
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
    
    sudo systemctl daemon-reload
    
    echo "✅ Created systemd service: $SYSTEMD_PATH"
    echo ""
    echo "📋 To start the agent:"
    echo "   sudo systemctl start codemaster-agent"
    echo "   sudo systemctl enable codemaster-agent"
    echo ""
    echo "📋 To check status:"
    echo "   sudo systemctl status codemaster-agent"
fi

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  ✅ INSTALLATION COMPLETE                                     ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "📋 Configure the agent:"
echo "   $AGENT_DIR/venv/bin/python $AGENT_DIR/device_agent.py run \\"
echo "       --fleet-url http://YOUR_FLEET_SERVER:8200 \\"
echo "       --name 'My Device' \\"
echo "       --enrollment-key 'your-key'"
echo ""
