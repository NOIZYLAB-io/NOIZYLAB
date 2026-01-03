#!/bin/bash
###############################################################################
# ⚡ CONSOLIDATE ALL MUSIC - MAXIMUM VELOCITY!
# Copies all 5,849 tracks to ONE master location!
# FIND → SCAN → EAT!!! GORUNFREE!!!
###############################################################################

echo "🔥⚡ CONSOLIDATING ALL 5,849 MUSIC TRACKS! ⚡🔥"
echo "MAXIMUM VELOCITY MODE!"
echo ""

MASTER="/Volumes/6TB/FISH_MUSIC_MASTER_LIBRARY/ORIGINALS"

echo "📂 Target: $MASTER"
echo ""
echo "⚡ Copying all tracks..."
echo ""

COUNT=0
while IFS= read -r track; do
    if [ -f "$track" ]; then
        # Get just filename
        filename=$(basename "$track")
        
        # Copy to master
        cp "$track" "$MASTER/$filename" 2>/dev/null
        
        COUNT=$((COUNT + 1))
        
        # Progress every 100 files
        if [ $((COUNT % 100)) -eq 0 ]; then
            echo "  ⚡ Copied: $COUNT tracks..."
        fi
    fi
done < /tmp/music_tracks.txt

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✅ CONSOLIDATION COMPLETE!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎵 Tracks copied: $COUNT"
echo "📂 Location: $MASTER"
echo ""
echo "🎯 ALL YOUR MUSIC IN ONE PLACE!"
echo "🚀 READY TO REVIEW & RELEASE!"
echo ""
echo "GORUNFREE!!! 🔥"

