#!/bin/bash
# NOIZY-RR (Repair Rob) Installer
# Run: curl -sL raw.githubusercontent.com/NOIZYLAB-io/NOIZYLAB/main/gabriel/install_rr.sh | bash

set -e

echo "███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗      ██████╗ ██████╗"
echo "████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝      ██╔══██╗██╔══██╗"
echo "██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ █████╗██████╔╝██████╔╝"
echo "██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ╚════╝██╔══██╗██╔══██╗"
echo "██║ ╚████║╚██████╔╝██║███████╗   ██║         ██║  ██║██║  ██║"
echo "╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝         ╚═╝  ╚═╝╚═╝  ╚═╝"
echo ""
echo "Installing NOIZY-RR (Repair Rob)..."
echo ""

# Create directory
mkdir -p ~/.noizy_rr

# Download or copy
if [ -f ~/NOIZYLAB/gabriel/noizy_rr.py ]; then
    cp ~/NOIZYLAB/gabriel/noizy_rr.py ~/.noizy_rr/
else
    curl -sL https://raw.githubusercontent.com/NOIZYLAB-io/NOIZYLAB/main/gabriel/noizy_rr.py -o ~/.noizy_rr/noizy_rr.py
fi

chmod +x ~/.noizy_rr/noizy_rr.py

# Add to PATH
if ! grep -q "alias rr=" ~/.zshrc 2>/dev/null; then
    cat >> ~/.zshrc << 'EOF'

# NOIZY-RR (Repair Rob)
alias rr='python3 ~/.noizy_rr/noizy_rr.py'
alias repair='rr'
alias fixme='rr "what'\''s wrong"'
EOF
    echo "✅ Added aliases to ~/.zshrc"
fi

# Test voice
echo ""
echo "Testing voice..."
say -v Daniel "Repair Rob online" 2>/dev/null || echo "(Voice not available)"

echo ""
echo "✅ NOIZY-RR INSTALLED!"
echo ""
echo "Commands:"
echo "  rr                    Interactive mode"
echo "  rr what's wrong       Quick diagnostic"
echo "  rr fix wifi           Fix WiFi"
echo "  rr why slow           Performance check"
echo "  rr help               All commands"
echo ""
echo "Quick aliases:"
echo "  fixme                 = rr \"what's wrong\""
echo "  repair                = rr"
echo ""
echo "🔧 Repair Rob ready. Source your shell or open new terminal."
echo ""
