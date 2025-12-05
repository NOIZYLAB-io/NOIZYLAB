#!/bin/bash

# GABRIEL CLEANUP - Delete Empty Folders
# Works in /Users/m2ultra/NOIZYLAB

ROOT="/Users/m2ultra/NOIZYLAB"

echo "🧹 GABRIEL CLEANUP - Deleting Empty Folders"
echo "=========================================="
echo "📂 Root: $ROOT"
echo ""

# Find and delete empty folders (excluding protected dirs)
find "$ROOT" -type d -empty \
  -not -path "*/node_modules/*" \
  -not -path "*/.git/*" \
  -not -path "*/.DS_Store/*" \
  -not -path "*/dist/*" \
  -not -path "*/build/*" \
  -not -path "*/.gabriel/*" \
  -print0 | while IFS= read -r -d '' dir; do
  rmdir "$dir" 2>/dev/null && echo "🗑️  Deleted: $dir" || true
done

echo ""
echo "✅ Cleanup complete!"

