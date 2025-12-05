#!/bin/bash
# Find all mounted volumes and external drives
# Help locate ROB's 40 years of music across all storage

echo ""
echo "🔍 FINDING ALL VOLUMES & DRIVES"
echo "================================"
echo ""

echo "📀 Mounted Volumes:"
echo "-------------------"
ls -la /Volumes/ | grep "^d" | awk '{print $NF}' | grep -v "^\\.$" | grep -v "^\\.\\.$" | while read vol; do
    if [ -d "/Volumes/$vol" ]; then
        size=$(du -sh "/Volumes/$vol" 2>/dev/null | awk '{print $1}')
        echo "  • $vol ($size)"
    fi
done

echo ""
echo "💾 System Disk Info:"
echo "--------------------"
df -h | grep -E "^/dev/" | awk '{print "  • " $1 " - " $2 " total, " $4 " free, mounted at " $9}'

echo ""
echo "🎵 Looking for music directories..."
echo "------------------------------------"

# Search for common music folder names
for vol in /Volumes/*; do
    if [ -d "$vol" ]; then
        echo ""
        echo "Searching: $vol"
        find "$vol" -maxdepth 2 -type d \( -iname "*music*" -o -iname "*audio*" -o -iname "*sessions*" -o -iname "*stems*" -o -iname "*projects*" -o -iname "*design*" -o -iname "*fuel*" -o -iname "*mcdonalds*" \) 2>/dev/null | while read dir; do
            size=$(du -sh "$dir" 2>/dev/null | awk '{print $1}')
            echo "  ✨ $dir ($size)"
        done
    fi
done

echo ""
echo "✅ Scan complete!"
echo ""

