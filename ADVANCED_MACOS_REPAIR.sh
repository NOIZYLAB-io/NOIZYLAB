#!/bin/bash
# 🔥 ADVANCED MACOS PREFERENCE REPAIR
# For when basic fix doesn't work
# Includes cache clearing + state reset

echo "🔥 ADVANCED MACOS PREFERENCE REPAIR"
echo "========================================"
echo ""
echo "⚠️  WARNING: This is the DEEP repair"
echo "Only run if basic fix didn't work"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 1
fi

echo ""
echo "🔧 Starting advanced repair..."
echo ""

# Kill all preference daemons
echo "1️⃣ Killing all preference daemons..."
killall cfprefsd 2>/dev/null
killall "System Settings" 2>/dev/null
sleep 2
echo "✅ Daemons killed"

# Remove System Settings caches
echo ""
echo "2️⃣ Clearing System Settings caches..."
if [ -d ~/Library/Caches/com.apple.systempreferences ]; then
    rm -rf ~/Library/Caches/com.apple.systempreferences
    echo "✅ Cache cleared"
else
    echo "⚠️  Cache not found"
fi

# Remove saved state
echo ""
echo "3️⃣ Clearing saved application state..."
if [ -d ~/Library/Saved\ Application\ State/com.apple.systempreferences.savedState ]; then
    rm -rf ~/Library/Saved\ Application\ State/com.apple.systempreferences.savedState
    echo "✅ Saved state cleared"
else
    echo "⚠️  Saved state not found"
fi

# Remove main plist
echo ""
echo "4️⃣ Removing corrupted plist..."
PLIST="$HOME/Library/Preferences/com.apple.systempreferences.plist"
if [ -f "$PLIST" ]; then
    # Backup first
    BACKUP="$PLIST.backup.advanced.$(date +%Y%m%d_%H%M%S)"
    cp "$PLIST" "$BACKUP"
    echo "💾 Backup: $BACKUP"
    
    rm "$PLIST"
    echo "✅ Plist removed"
else
    echo "⚠️  Plist not found"
fi

# Clear LaunchServices database (safe)
echo ""
echo "5️⃣ Rebuilding LaunchServices database..."
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -kill -r -domain local -domain system -domain user
echo "✅ LaunchServices rebuilt"

# Reset preference cache
echo ""
echo "6️⃣ Resetting preference cache..."
rm -rf ~/Library/Caches/com.apple.LaunchServices.dv
echo "✅ Preference cache reset"

echo ""
echo "========================================"
echo "✅ ADVANCED REPAIR COMPLETE!"
echo ""
echo "🎯 FINAL STEPS:"
echo "  1. Restart your Mac (recommended)"
echo "  2. Open System Settings"
echo "  3. All items should now appear"
echo ""
echo "🔄 Restart now? (y/n)"
read -p "> " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🔄 Restarting in 10 seconds..."
    echo "Press Ctrl+C to cancel"
    sleep 10
    sudo shutdown -r now
else
    echo "✅ Manual restart recommended"
    echo "🚀 Opening System Settings..."
    sleep 2
    open "/System/Applications/System Settings.app"
fi
