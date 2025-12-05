#!/bin/bash
# 🔥 GABRIEL FINAL SETUP SCRIPT
# Fish Music Inc - CB_01

echo "🔥 GABRIEL FINAL SETUP"
echo ""

# Enable SSH
echo "[+] Enabling SSH (Remote Login)..."
sudo systemsetup -setremotelogin on

# Enable Screen Sharing
echo "[+] Enabling Screen Sharing..."
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.screensharing.plist 2>/dev/null || echo "   (Already enabled or needs manual config)"

# Create shared folder
echo "[+] Creating NoizyShare folder..."
mkdir -p ~/NoizyShare
echo "✅ ~/NoizyShare created"

# Enable File Sharing
echo ""
echo "📋 MANUAL STEP REQUIRED:"
echo "   System Settings → General → Sharing → File Sharing → ON"
echo "   Then add: ~/NoizyShare"
echo "   Options → Enable SMB → Check your user"
echo ""
read -p "Press Enter when File Sharing is enabled..."

# Generate SSH key if needed
if [ ! -f ~/.ssh/id_ed25519 ]; then
    echo "[+] Generating SSH key..."
    ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
fi

echo ""
echo "✅ GABRIEL setup complete!"
echo ""
echo "📋 Your SSH Public Key (copy this to OMEN):"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
cat ~/.ssh/id_ed25519.pub
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎯 Next: Run ~/OMEGA_BUILD/omega_start.sh"
echo ""
