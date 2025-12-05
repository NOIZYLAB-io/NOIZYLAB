#!/bin/bash
# MOVE_IT_NOW.sh - Simple, direct file mover

BACKUP="/Volumes/4TB_02/CODE_MASTER/System_Backup"
mkdir -p "$BACKUP"

echo "🚨 MOVING FILES NOW!"

# Move Downloads
if [ -d "/Users/rsp_ms/Downloads" ]; then
    echo "Moving Downloads..."
    mv /Users/rsp_ms/Downloads "$BACKUP/Downloads" 2>/dev/null || \
    (cp -R /Users/rsp_ms/Downloads "$BACKUP/Downloads" && rm -rf /Users/rsp_ms/Downloads)
    echo "✅ Downloads moved"
fi

# Move Desktop files
if [ -d "/Users/rsp_ms/Desktop" ]; then
    echo "Moving Desktop..."
    mkdir -p "$BACKUP/Desktop"
    find /Users/rsp_ms/Desktop -type f -exec mv {} "$BACKUP/Desktop/" \; 2>/dev/null
    echo "✅ Desktop moved"
fi

# Move Music (to MUSIC_RESCUE)
if [ -d "/Users/rsp_ms/Music" ]; then
    echo "Moving Music to MUSIC_RESCUE..."
    mkdir -p "/Volumes/4TB_02/MUSIC_RESCUE/System_Music"
    mv /Users/rsp_ms/Music/* "/Volumes/4TB_02/MUSIC_RESCUE/System_Music/" 2>/dev/null || \
    (cp -R /Users/rsp_ms/Music/* "/Volumes/4TB_02/MUSIC_RESCUE/System_Music/" && rm -rf /Users/rsp_ms/Music/*)
    echo "✅ Music moved"
fi

echo ""
echo "✅ DONE!"
df -h / | tail -1

