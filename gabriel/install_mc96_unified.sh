#!/bin/bash
# MC96 UNIFIED INSTALLER
# Run: bash install_mc96_unified.sh

set -e
echo "█▀▄▀█ █▀▀ █▀▀ █▀▀"
echo "█ ▀ █ █   ▀▀█ █▀▀"  
echo "▀   ▀ ▀▀▀ ▀▀▀ ▀▀▀"
echo ""

# Setup directories
mkdir -p ~/.mc96/{sessions,captures}

# Make executable
chmod +x ~/NOIZYLAB/gabriel/mc96_unified.py

# Create symlink in /usr/local/bin
echo "🔗 Installing mc96 command..."
sudo ln -sf ~/NOIZYLAB/gabriel/mc96_unified.py /usr/local/bin/mc96 2>/dev/null || {
    mkdir -p ~/bin
    ln -sf ~/NOIZYLAB/gabriel/mc96_unified.py ~/bin/mc96
    echo "export PATH=\"\$HOME/bin:\$PATH\"" >> ~/.zshrc
}

# Add aliases
if ! grep -q "alias mc96=" ~/.zshrc 2>/dev/null; then
    cat >> ~/.zshrc << 'EOF'

# MC96 UNIFIED
alias mc96='python3 ~/NOIZYLAB/gabriel/mc96_unified.py'
alias 96='mc96'
alias recall='mc96 recall'
alias wtf='mc96 wtf'
EOF
fi

echo ""
echo "✅ MC96 UNIFIED INSTALLED"
echo ""
echo "Commands:"
echo "  mc96              Status"
echo "  mc96 recall today Git/session recall"
echo "  mc96 new 'Title'  Start session"
echo "  mc96 add file.py  Track file"
echo "  mc96 wtf 'error'  Capture issue"
echo "  mc96 calendar     View schedule"
echo "  mc96 push         Git commit+push"
echo "  mc96 upgrade      System update"
echo ""
echo "🔮 ONE TOOL. ALL POWER."
