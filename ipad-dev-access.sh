#!/bin/bash

# =============================================================================
# iPad Development Access Setup
# Enables iPad to access macOS development environment
# =============================================================================

echo "📱 iPad Development Access Setup"
echo "================================"
echo ""
echo "This script sets up remote access from iPad to your Mac"
echo "for development work (Claude/Cursor-like functionality)"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ This script is for macOS only"
    exit 1
fi

echo "Setting up iPad development access..."
echo ""

# 1. Enable SSH
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1. Enabling SSH..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if SSH is enabled
if sudo systemsetup -getremotelogin | grep -q "On"; then
    echo -e "${GREEN}✅ SSH is already enabled${NC}"
else
    echo "Enabling SSH..."
    sudo systemsetup -setremotelogin on
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ SSH enabled${NC}"
    else
        echo "❌ Failed to enable SSH. Please enable manually:"
        echo "   System Settings → General → Sharing → Remote Login"
        exit 1
    fi
fi

# Get current user
CURRENT_USER=$(whoami)
echo "Current user: $CURRENT_USER"

# Get IP address
IP_ADDRESS=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "NOT_FOUND")
if [ "$IP_ADDRESS" != "NOT_FOUND" ]; then
    echo -e "${GREEN}✅ Local IP Address: $IP_ADDRESS${NC}"
else
    echo -e "${YELLOW}⚠️  Could not detect IP address${NC}"
    echo "   Find it manually: System Settings → Network"
fi

echo ""

# 2. Create SSH key pair for iPad (if needed)
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "2. SSH Key Setup (Optional - for passwordless access)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

SSH_DIR="$HOME/.ssh"
IPAD_KEY="$SSH_DIR/id_rsa_ipad"

if [ ! -f "$IPAD_KEY" ]; then
    echo "Creating SSH key pair for iPad..."
    ssh-keygen -t rsa -b 4096 -f "$IPAD_KEY" -N "" -C "ipad-dev-access"
    echo -e "${GREEN}✅ SSH key created: $IPAD_KEY${NC}"
    echo ""
    echo "Add this public key to authorized_keys:"
    cat "$IPAD_KEY.pub" >> "$SSH_DIR/authorized_keys"
    echo -e "${GREEN}✅ Public key added to authorized_keys${NC}"
else
    echo -e "${GREEN}✅ SSH key already exists${NC}"
fi

echo ""

# 3. Create connection script
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "3. Creating connection information..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

CONNECTION_INFO="$HOME/NOIZYLAB/ipad-dev-setup/ipad-connection-info.txt"

cat > "$CONNECTION_INFO" << EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📱 iPad to Mac Connection Information
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SSH Connection:
--------------
Host: $IP_ADDRESS (or use hostname: $(hostname).local)
Port: 22
User: $CURRENT_USER

SSH Command (from iPad terminal app):
  ssh $CURRENT_USER@$IP_ADDRESS

Or using hostname:
  ssh $CURRENT_USER@$(hostname).local


SSH Key (for passwordless access):
----------------------------------
Private Key Location: $IPAD_KEY
Public Key Location: $IPAD_KEY.pub

Copy the private key to your iPad for passwordless SSH access.


Web-Based Development Options:
------------------------------
1. VS Code Server (code-server)
   URL: http://$IP_ADDRESS:8080
   (Requires code-server installation)

2. Jupyter Notebook
   URL: http://$IP_ADDRESS:8888
   (If installed)

3. Web-based Terminal
   Use SSH terminal app on iPad


Recommended iPad Apps:
---------------------
1. Blink Shell (SSH terminal) - Best for development
2. Termius (SSH client)
3. Prompt 3 (SSH client)
4. Working Copy (Git client)
5. Textastic (Code editor)


File Access:
-----------
Use SFTP client on iPad:
- Host: $IP_ADDRESS
- Port: 22
- User: $CURRENT_USER
- Protocol: SFTP

Recommended SFTP apps:
- FileBrowser
- Documents by Readdle
- Transmit


Next Steps:
----------
1. Install Blink Shell or Termius on iPad
2. Connect using SSH credentials above
3. Navigate to: cd ~/NOIZYLAB
4. Start coding!


Troubleshooting:
--------------
If connection fails:
- Ensure Mac and iPad are on same WiFi network
- Check firewall settings
- Verify SSH is enabled: System Settings → Sharing → Remote Login

EOF

echo -e "${GREEN}✅ Connection info saved to: $CONNECTION_INFO${NC}"
echo ""

# 4. Display connection info
cat "$CONNECTION_INFO"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Next: Install Blink Shell or Termius on your iPad"
echo "      and connect using the information above"
echo ""

