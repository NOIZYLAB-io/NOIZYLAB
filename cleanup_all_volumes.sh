#!/bin/bash
# MC96 VOLUME CLEANUP SCRIPT
# Removes .DS_Store, empty folders, and organizes

echo "🧹 MC96 VOLUME CLEANUP"
echo "======================"

VOLUMES=(
    "/Volumes/6TB"
    "/Volumes/4TB_Utility"
    "/Volumes/4TB Big Fish"
    "/Volumes/4TB Blue Fish"
    "/Volumes/4TBSG"
    "/Volumes/4TB Lacie"
    "/Volumes/MAG 4TB"
    "/Volumes/12TB"
    "/Volumes/4TB_02"
    "/Volumes/RED DRAGON"
)

for vol in "${VOLUMES[@]}"; do
    if [ -d "$vol" ]; then
        echo "Cleaning $vol..."
        # Remove .DS_Store files
        find "$vol" -name ".DS_Store" -delete 2>/dev/null
        # Remove empty directories (careful!)
        find "$vol" -type d -empty -delete 2>/dev/null
        echo "  ✅ Done"
    fi
done

echo ""
echo "🎉 Cleanup complete!"
