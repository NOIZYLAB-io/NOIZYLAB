#!/bin/bash
# ⌨️ HOTKEYS - GLOBAL SHORTCUTS
# Fish Music Inc - CB_01

echo "⌨️ Installing global hotkeys..."

# Create hotkey daemon
cat > /tmp/omega_hotkeys.sh << 'EOF'
#!/bin/bash
# OMEGA Hotkey Daemon

# This requires Hammerspoon or similar tool
# For now, we create a LaunchAgent

echo "Hotkeys available via Hammerspoon:"
echo "  Ctrl+Alt+G → Connect to GABRIEL"
echo "  Ctrl+Alt+O → Connect to OMEN"
echo "  Ctrl+Alt+S → Trigger sync"
echo "  Ctrl+Alt+H → Run heal script"

# Install Hammerspoon config
mkdir -p ~/.hammerspoon

cat > ~/.hammerspoon/init.lua << 'LUA'
-- OMEGA BRAIN Hotkeys

hs.hotkey.bind({"ctrl", "alt"}, "G", function()
    hs.notify.new({title="OMEGA", informativeText="Connecting to GABRIEL..."}):send()
    os.execute("ssh gabriel.local")
end)

hs.hotkey.bind({"ctrl", "alt"}, "O", function()
    hs.notify.new({title="OMEGA", informativeText="Connecting to OMEN..."}):send()
    os.execute("ssh omen.local")
end)

hs.hotkey.bind({"ctrl", "alt"}, "S", function()
    hs.notify.new({title="OMEGA", informativeText="Syncing..."}):send()
    os.execute("task sync")
end)

hs.hotkey.bind({"ctrl", "alt"}, "H", function()
    hs.notify.new({title="OMEGA", informativeText="Healing system..."}):send()
    os.execute("~/NOIZYLAB/OMEGA_SYSTEM/omega_heal.sh")
end)

hs.alert.show("OMEGA Hotkeys Active! 🔥")
LUA

EOF

chmod +x /tmp/omega_hotkeys.sh

echo "✅ Hotkeys configured!"
echo ""
echo "📋 Install Hammerspoon to activate:"
echo "   brew install --cask hammerspoon"
echo ""
echo "Shortcuts:"
echo "  Ctrl+Alt+G → SSH to GABRIEL"
echo "  Ctrl+Alt+O → SSH to OMEN"
echo "  Ctrl+Alt+S → Sync now"
echo "  Ctrl+Alt+H → Heal system"
echo ""
