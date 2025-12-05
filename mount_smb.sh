#!/bin/bash
# 📁 SMB - MOUNT GABRIEL SHARE
# Fish Music Inc - CB_01
# For use on OMEN (Windows) - converts to .bat

if [[ "$(uname)" == "Darwin" ]]; then
    echo "⚠️  This script is for Windows (OMEN)"
    echo "   On Mac, use: open smb://gabriel.local/NoizyShare"
    exit 0
fi

# Windows command (if running in WSL or Git Bash):
echo "Mounting GABRIEL share as Z: drive..."
net use Z: \\\\gabriel.local\\NoizyShare /persistent:yes

if [ $? -eq 0 ]; then
    echo "✅ Z: drive mounted!"
    echo "   Files from GABRIEL now accessible at Z:\\"
else
    echo "❌ Mount failed"
    echo "   Check:"
    echo "   1. File Sharing enabled on GABRIEL"
    echo "   2. Network connectivity"
    echo "   3. SMB enabled in GABRIEL sharing options"
fi
