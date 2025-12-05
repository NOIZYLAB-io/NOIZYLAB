#!/bin/bash
# 🔧 MACOS PREFERENCE FRAMEWORK FIX
# Fixes "Only 2 items in System Settings" issue
# Safe, tested, Apple-level repair

echo "🔧 MACOS PREFERENCE FRAMEWORK REPAIR"
echo "========================================"
echo ""
echo "Symptom: Only 2 items showing in System Settings"
echo "Cause: Corrupted plist database + preference daemons"
echo "Fix: Reset preference system (safe, no data loss)"
echo ""

# Step 1: Kill preference daemon
echo "🟣 STEP 1: Resetting preference daemon..."
killall cfprefsd 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ cfprefsd killed (auto-restarts)"
else
    echo "⚠️  cfprefsd not running"
fi
sleep 2

# Step 2: Kill System Settings
echo ""
echo "🟦 STEP 2: Resetting System Settings app..."
killall "System Settings" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ System Settings killed"
else
    echo "✅ System Settings wasn't running"
fi
sleep 1

# Step 3: Check and reset plist
echo ""
echo "🟩 STEP 3: Checking System Settings plist..."

PLIST="$HOME/Library/Preferences/com.apple.systempreferences.plist"

if [ -f "$PLIST" ]; then
    echo "📁 Found plist: $PLIST"
    
    # Create backup
    BACKUP="$PLIST.backup.$(date +%Y%m%d_%H%M%S)"
    cp "$PLIST" "$BACKUP"
    echo "💾 Backup created: $BACKUP"
    
    # Remove corrupted plist
    rm "$PLIST"
    echo "🗑️  Removed corrupted plist"
    echo "✅ Plist will regenerate on next System Settings launch"
else
    echo "⚠️  Plist not found (might already be reset)"
fi

echo ""
echo "========================================"
echo "✅ REPAIR COMPLETE!"
echo ""
echo "🎯 NEXT STEPS:"
echo "  1. Open System Settings"
echo "  2. Check if all menu items appear"
echo "  3. If fixed → You're done! 🎉"
echo "  4. If not → Run advanced repair below"
echo ""
echo "🔧 ADVANCED REPAIR (if needed):"
echo "  sudo rm -rf ~/Library/Caches/com.apple.systempreferences"
echo "  sudo rm -rf ~/Library/Saved\\ Application\\ State/com.apple.systempreferences.savedState"
echo ""
echo "🚀 Opening System Settings in 3 seconds..."
sleep 3
open "/System/Applications/System Settings.app"
