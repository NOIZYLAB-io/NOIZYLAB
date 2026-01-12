#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# 🧠 MEMCELL INSTALLER - THE NOIZYLAB TIME CAPSULE
# ═══════════════════════════════════════════════════════════════════════════════

set -e

echo "
███╗   ███╗███████╗███╗   ███╗ ██████╗███████╗██╗     ██╗     
████╗ ████║██╔════╝████╗ ████║██╔════╝██╔════╝██║     ██║     
██╔████╔██║█████╗  ██╔████╔██║██║     █████╗  ██║     ██║     
██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║     ██╔══╝  ██║     ██║     
██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╗███████╗███████╗███████╗
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝╚══════╝╚══════╝╚══════╝

         🔮 INSTALLING THE NOIZYLAB TIME CAPSULE 🔮
              Powered by THE CIRCLE OF 8
"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MEMCELL_HOME="$HOME/.memcell"

# Create MEMCELL home
echo "📁 Creating MEMCELL home directory..."
mkdir -p "$MEMCELL_HOME"/{captures,chats,index}

# Make executable
echo "🔧 Setting permissions..."
chmod +x "$SCRIPT_DIR/memcell"
chmod +x "$SCRIPT_DIR/memcell.py"

# Add to PATH via aliases
echo "🔗 Setting up aliases..."

ALIAS_BLOCK='
# ═══════════════════════════════════════════════════════════════
# 🧠 MEMCELL - THE NOIZYLAB TIME CAPSULE
# ═══════════════════════════════════════════════════════════════
export MEMCELL_HOME="$HOME/.memcell"
alias memcell="python3 ~/NOIZYLAB/gabriel/memcell/memcell.py"
alias mc="memcell"
alias remember="memcell recall"
alias snapshot="memcell capture"
alias plan="memcell schedule"
alias history="memcell timeline"
alias family="memcell family"

# Quick recall shortcuts
alias yesterday="memcell recall yesterday"
alias lastweek="memcell recall \"last week\""
alias monday="memcell recall monday"
'

# Check shell and add aliases
if [[ -f "$HOME/.zshrc" ]]; then
    if ! grep -q "MEMCELL" "$HOME/.zshrc"; then
        echo "$ALIAS_BLOCK" >> "$HOME/.zshrc"
        echo "✅ Added to ~/.zshrc"
    else
        echo "ℹ️  MEMCELL already in ~/.zshrc"
    fi
fi

if [[ -f "$HOME/.bashrc" ]]; then
    if ! grep -q "MEMCELL" "$HOME/.bashrc"; then
        echo "$ALIAS_BLOCK" >> "$HOME/.bashrc"
        echo "✅ Added to ~/.bashrc"
    fi
fi

# Create Apple Calendar (optional)
echo ""
echo "📅 Creating NOIZYLAB calendar..."
osascript -e 'tell application "Calendar" to make new calendar with properties {name:"NOIZYLAB"}' 2>/dev/null || echo "ℹ️  Calendar may already exist or Calendar.app not available"

# Initial capture
echo ""
echo "🧠 Running initial capture..."
python3 "$SCRIPT_DIR/memcell.py" capture || true

# Setup daily capture via launchd
echo ""
echo "⏰ Setting up daily auto-capture..."

PLIST_PATH="$HOME/Library/LaunchAgents/io.noizylab.memcell.plist"
cat > "$PLIST_PATH" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>io.noizylab.memcell</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>$SCRIPT_DIR/memcell.py</string>
        <string>capture</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>23</integer>
        <key>Minute</key>
        <integer>55</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>$MEMCELL_HOME/capture.log</string>
    <key>StandardErrorPath</key>
    <string>$MEMCELL_HOME/capture.error.log</string>
</dict>
</plist>
EOF

launchctl unload "$PLIST_PATH" 2>/dev/null || true
launchctl load "$PLIST_PATH" 2>/dev/null || echo "ℹ️  Auto-capture will start after restart"

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "✅ MEMCELL INSTALLED SUCCESSFULLY!"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "🧠 THE TIME CAPSULE IS READY"
echo ""
echo "Commands:"
echo "  memcell capture              Snapshot today"
echo "  memcell recall \"monday\"      What happened Monday?"
echo "  memcell recall \"dec 15\"      What happened Dec 15?"
echo "  memcell schedule \"task\" --at \"tomorrow 9am\""
echo "  memcell timeline             Last 7 days visual"
echo "  memcell family               Circle of 8 status"
echo ""
echo "Quick aliases:"
echo "  mc, remember, snapshot, plan, history, family"
echo "  yesterday, lastweek, monday"
echo ""
echo "📍 Data stored in: $MEMCELL_HOME"
echo "⏰ Auto-capture: Daily at 11:55 PM"
echo ""
echo "🔄 Restart your terminal or run: source ~/.zshrc"
echo ""
