#!/bin/bash
# CLEANUP_SYSTEM_DRIVE.sh
# Emergency system drive cleanup

EXTERNAL="/Volumes/4TB_02"
HOME_DIR="/Users/rsp_ms"

echo "🚨 SYSTEM DRIVE CLEANUP"
echo ""
echo "📊 Current space:"
df -h / | tail -1
echo ""

# Stop processes
echo "🛑 Stopping processes..."
pkill -9 -f "MUSIC_RESCUE" 2>/dev/null || true
pkill -9 -f "rsync" 2>/dev/null || true
sleep 1
echo "✅ Processes stopped"
echo ""

# Clean caches
echo "🧹 Cleaning caches..."
find "$HOME_DIR/Library/Caches" -type f -size +10M -delete 2>/dev/null || true
echo "✅ Caches cleaned"
echo ""

# Clean logs
echo "🧹 Cleaning logs..."
find "$HOME_DIR/Library/Logs" -type f -mtime +3 -delete 2>/dev/null || true
echo "✅ Logs cleaned"
echo ""

# Empty trash
echo "🧹 Emptying trash..."
rm -rf "$HOME_DIR/.Trash"/* 2>/dev/null || true
echo "✅ Trash emptied"
echo ""

# Clean temp
echo "🧹 Cleaning temp files..."
rm -rf /tmp/* 2>/dev/null || true
echo "✅ Temp files cleaned"
echo ""

# Move large files if found
echo "🔍 Finding large files (>100MB)..."
find "$HOME_DIR" -type f -size +100M \
    -not -path "*/Library/*" \
    -not -path "*/.Trash/*" \
    -not -path "*/node_modules/*" \
    2>/dev/null | head -10 | while read file; do
    echo "   Found: $(basename "$file")"
    dest="$EXTERNAL/Large_Files/$(basename "$file")"
    mkdir -p "$EXTERNAL/Large_Files"
    mv -f "$file" "$dest" 2>/dev/null && echo "   ✅ Moved" || echo "   ⚠️  Could not move"
done
echo "✅ Large files processed"
echo ""

echo "📊 Final space:"
df -h / | tail -1
echo ""
echo "✅ Cleanup complete!"

