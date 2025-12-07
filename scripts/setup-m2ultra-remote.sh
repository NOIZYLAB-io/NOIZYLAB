#!/bin/zsh
# M2Ultra Remote Desktop Setup
# Enable screen sharing, VNC, and SSH for remote access on macOS

set -e

echo "🖥️  M2Ultra Remote Desktop Setup"
echo "================================"

# Enable Screen Sharing (Remote Management)
echo "🔧 Enabling Screen Sharing (macOS Remote Desktop)..."
sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart -activate -configure -access -on -users admin -privs -all -restart -agent -console

echo "✅ Screen Sharing enabled"

# Enable SSH
echo "🔐 Enabling SSH..."
sudo systemsetup -setremotelogin on

echo "✅ SSH enabled"

# Start VNC service (if needed)
echo "📡 VNC setup info..."
echo "VNC is available through Screen Sharing or can be configured separately"

# Display connection info
echo ""
echo "📊 M2Ultra Connection Information:"
echo "=================================="
hostname=$(scutil --get ComputerName)
ip_address=$(ipconfig getifaddr en0 || echo "WiFi - Check System Preferences")
echo "Computer Name: $hostname"
echo "IP Address: $ip_address"
echo "SSH: ssh $(whoami)@$ip_address"
echo "Screen Sharing: vnc://$ip_address"

# Add to aliases
echo ""
echo "📝 Adding shortcuts to ~/.zsh_aliases..."

cat >> ~/.zsh_aliases << 'EOF'

# M2Ultra Remote Access
alias m2-info="echo 'M2Ultra: $(scutil --get ComputerName) @ $(ipconfig getifaddr en0)'"
alias m2-vnc="open 'vnc://$(ipconfig getifaddr en0)'"
EOF

source ~/.zsh_aliases

echo "✅ Aliases configured"

echo ""
echo "✨ Setup Complete!"
echo "Remote Desktop is now available on your M2Ultra machine"
