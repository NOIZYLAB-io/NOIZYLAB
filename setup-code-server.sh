#!/bin/bash

# =============================================================================
# Code Server Setup for iPad Web Access
# Installs code-server (VS Code in browser) for iPad development
# =============================================================================

echo "🌐 Code Server Setup (VS Code in Browser)"
echo "========================================="
echo ""
echo "This installs code-server, which gives you VS Code in a web browser"
echo "Perfect for iPad development!"
echo ""

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew not found. Installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Check if code-server is installed
if command -v code-server &> /dev/null; then
    echo "✅ code-server is already installed"
    code-server --version
else
    echo "Installing code-server..."
    brew install code-server
    if [ $? -eq 0 ]; then
        echo "✅ code-server installed"
    else
        echo "❌ Installation failed"
        exit 1
    fi
fi

echo ""

# Create code-server config directory
CONFIG_DIR="$HOME/.config/code-server"
mkdir -p "$CONFIG_DIR"

# Create config file
CONFIG_FILE="$CONFIG_DIR/config.yaml"

cat > "$CONFIG_FILE" << EOF
bind-addr: 0.0.0.0:8080
auth: password
password: CHANGE_THIS_PASSWORD
cert: false
EOF

echo "✅ Configuration file created: $CONFIG_FILE"
echo ""
echo "⚠️  IMPORTANT: Edit the password in the config file!"
echo "   File: $CONFIG_FILE"
echo "   Change 'CHANGE_THIS_PASSWORD' to a secure password"
echo ""

# Create startup script
START_SCRIPT="$HOME/NOIZYLAB/ipad-dev-setup/start-code-server.sh"

cat > "$START_SCRIPT" << 'EOF'
#!/bin/bash

# Start code-server
echo "Starting code-server..."
echo "Access at: http://YOUR_IP:8080"
echo ""

# Get IP address
IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "localhost")
echo "Your Mac IP: $IP"
echo "Access from iPad: http://$IP:8080"
echo ""
echo "Press Ctrl+C to stop"
echo ""

code-server --bind-addr 0.0.0.0:8080
EOF

chmod +x "$START_SCRIPT"

echo "✅ Startup script created: $START_SCRIPT"
echo ""

# Create systemd service (optional, for auto-start)
SERVICE_FILE="$HOME/NOIZYLAB/ipad-dev-setup/code-server.service"

cat > "$SERVICE_FILE" << EOF
[Unit]
Description=Code Server
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$HOME/NOIZYLAB
ExecStart=$(which code-server) --bind-addr 0.0.0.0:8080
Restart=always

[Install]
WantedBy=default.target
EOF

echo "✅ Service file created: $SERVICE_FILE"
echo ""

# Display instructions
cat << EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📱 Setup Complete!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next Steps:
----------
1. Edit password in config file:
   nano $CONFIG_FILE
   (Change 'CHANGE_THIS_PASSWORD' to your password)

2. Start code-server:
   $START_SCRIPT

3. Access from iPad:
   - Open Safari/Chrome on iPad
   - Go to: http://YOUR_MAC_IP:8080
   - Enter password you set in config

4. Start coding on iPad! 🎉

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Security Note:
--------------
- Change the default password!
- Consider using HTTPS (requires SSL certificate)
- Only use on trusted networks
- Consider firewall rules for port 8080

EOF

