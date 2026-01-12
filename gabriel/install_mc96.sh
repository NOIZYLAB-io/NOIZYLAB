#!/bin/bash
# 🔥 MC96 HOT ROD TERMINAL INSTALLER
# Run this to set up the mc96 command globally

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MC96_PATH="$SCRIPT_DIR/mc96"

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  🔥 MC96 HOT ROD TERMINAL INSTALLER                          ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Make executable
chmod +x "$MC96_PATH"
chmod +x "$SCRIPT_DIR/mc96_terminal.py"
echo "✅ Made scripts executable"

# Create symlink in /usr/local/bin
if [ -d "/usr/local/bin" ]; then
    sudo ln -sf "$MC96_PATH" /usr/local/bin/mc96
    echo "✅ Created symlink: /usr/local/bin/mc96"
else
    echo "⚠️  /usr/local/bin doesn't exist, adding to PATH via .zshrc"
fi

# Add to .zshrc
ZSHRC="$HOME/.zshrc"
ALIAS_LINE="alias mc96='python3 $SCRIPT_DIR/mc96_terminal.py'"
EXPORT_LINE="export PATH=\"\$PATH:$SCRIPT_DIR\""

# Check if already in .zshrc
if grep -q "mc96_terminal.py" "$ZSHRC" 2>/dev/null; then
    echo "✅ Already in .zshrc"
else
    echo "" >> "$ZSHRC"
    echo "# 🔥 MC96 Hot Rod Terminal" >> "$ZSHRC"
    echo "$ALIAS_LINE" >> "$ZSHRC"
    echo "$EXPORT_LINE" >> "$ZSHRC"
    echo "✅ Added to ~/.zshrc"
fi

# Add quick aliases
if ! grep -q "# MC96 Quick Aliases" "$ZSHRC" 2>/dev/null; then
    cat >> "$ZSHRC" << 'EOF'

# MC96 Quick Aliases
alias s='mc96 status'
alias sp='mc96 speak'
alias a='mc96 ask'
alias g='mc96 gabriel'
alias sv='mc96 server start'
alias hr='mc96 hotrod'
EOF
    echo "✅ Added quick aliases (s, sp, a, g, sv, hr)"
fi

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  ✅ INSTALLATION COMPLETE!                                   ║"
echo "╠══════════════════════════════════════════════════════════════╣"
echo "║  Run: source ~/.zshrc                                        ║"
echo "║  Then: mc96                                                  ║"
echo "╚══════════════════════════════════════════════════════════════╝"
