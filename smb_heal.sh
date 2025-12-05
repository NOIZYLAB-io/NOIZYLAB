#!/bin/bash
# 📁 SMB - HEAL CONNECTION
# Fish Music Inc - CB_01

echo "🔧 Healing SMB connection..."
echo ""

if [[ "$(uname)" == "Darwin" ]]; then
    # macOS (GABRIEL)
    echo "[+] Restarting SMB service..."
    sudo launchctl unload /System/Library/LaunchDaemons/com.apple.smbd.plist 2>/dev/null
    sudo launchctl load /System/Library/LaunchDaemons/com.apple.smbd.plist 2>/dev/null
    
    echo "[+] Flushing SMB cache..."
    sudo dscacheutil -flushcache
    
    echo "✅ SMB service restarted on GABRIEL"
else
    # Windows (OMEN)
    echo "[+] Unmounting Z: drive..."
    net use Z: /delete /yes
    
    echo "[+] Remounting..."
    net use Z: \\\\gabriel.local\\NoizyShare /persistent:yes
    
    if [ $? -eq 0 ]; then
        echo "✅ SMB reconnected"
    else
        echo "❌ SMB mount failed - check GABRIEL"
    fi
fi

echo ""
echo "🔥 GORUNFREE! 🎸🔥"
