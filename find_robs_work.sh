#!/bin/bash
# FIND ROB'S 40-YEAR CREATIVE LEGACY
# Searches for audio files without metadata (ROB's originals)

echo "🔍 SEARCHING FOR ROB'S ORIGINAL WORK"
echo "===================================="
echo ""

# Key locations to search
LOCATIONS=(
    "/Volumes/6TB/_ORGANIZED/07_ROB_WORK"
    "/Volumes/4TB_Utility/_MASTER_ARCHIVE/01_ROB_ORIGINAL_WORK"
    "/Volumes/4TB Lacie/_ORGANIZED/01_DESIGN_REUNION"
    "/Volumes/12TB/_ORGANIZED/01_FISHMUSIC"
)

for loc in "${LOCATIONS[@]}"; do
    if [ -d "$loc" ]; then
        echo "📁 $loc"
        count=$(find "$loc" -type f \( -name "*.wav" -o -name "*.aif" -o -name "*.mp3" \) 2>/dev/null | wc -l | tr -d ' ')
        echo "   Audio files: $count"
        echo ""
    fi
done

echo "🎯 KEY PROJECTS FOUND:"
echo ""

# Design Reunion (Gavin project)
if [ -d "/Volumes/4TB Lacie/_ORGANIZED/01_DESIGN_REUNION" ]; then
    echo "✅ DESIGN REUNION PROJECT (for Gavin!)"
    ls "/Volumes/4TB Lacie/_ORGANIZED/01_DESIGN_REUNION/" 2>/dev/null
fi

echo ""
echo "🎉 Search complete!"
