#!/bin/bash
# MEGA LAUNCHER - Runs the enhanced organizer

clear

cat << "EOF"
================================================================================
🎵 MEGA ULTIMATE WAV ORGANIZER v2.0 🎵
================================================================================

⭐⭐⭐ HARD RULE ⭐⭐⭐
ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!

ENHANCED FEATURES:
✓ Progress bars and real-time feedback
✓ MD5 checksums for file verification
✓ Duplicate detection (save disk space!)
✓ Audio analysis (detect silence, peaks)
✓ Beautiful HTML report
✓ Undo capability (safety net)
✓ Advanced validation

================================================================================
EOF

echo ""
echo "Press ENTER to start, or Ctrl+C to cancel..."
read

cd "$(dirname "$0")"

echo ""
echo "🚀 Launching MEGA organizer..."
echo ""

/usr/bin/python3 MEGA_ULTIMATE_ORGANIZER.py

echo ""
echo "================================================================================
echo "✓ COMPLETE!"
echo "================================================================================"
echo ""
echo "Press any key to close..."
read -n 1

