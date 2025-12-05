#!/usr/bin/env bash
# Sync tool from NOIZYLAB to _ORGANIZED

ORGANIZED="/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED"
NOIZYLAB="/Users/m2ultra/NOIZYLAB"

echo "🔄 NOIZYLAB ↔ _ORGANIZED Sync Tool"
echo "===================================="
echo ""

if [ ! -d "$ORGANIZED" ]; then
    echo "❌ _ORGANIZED not found: $ORGANIZED"
    exit 1
fi

echo "📊 Checking sync status..."
python3 "$ORGANIZED/SYNC_WITH_NOIZYLAB.py"

echo ""
echo "💡 To archive a project from NOIZYLAB to _ORGANIZED:"
echo "   1. Choose the project name from above"
echo "   2. Choose appropriate category in _ORGANIZED"
echo "   3. Move project manually or use organizer tools"
echo ""
echo "🎯 Tools available:"
echo "   cd $ORGANIZED"
echo "   ./ORGANIZED_MANAGER.sh"

