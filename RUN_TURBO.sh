#!/bin/bash
# TURBO LAUNCHER - 25X FASTER!

clear

cat << "EOF"
================================================================================
🚀 TURBO WAV ORGANIZER - 25X FASTER! ⚡
================================================================================

⭐⭐⭐ HARD RULE ⭐⭐⭐
ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!

SPEED FEATURES:
⚡ Parallel processing (uses ALL CPU cores)
⚡ Header-only scanning (minimal file reads)
⚡ Batch operations
⚡ Optimized for maximum speed
⚡ Processes 100+ files per second!

================================================================================
EOF

echo ""
echo "Ready to organize at TURBO speed?"
echo "Press ENTER to launch..."
read

cd "$(dirname "$0")"

echo ""
echo "🚀 TURBO MODE ACTIVATED! ⚡"
echo ""

time /usr/bin/python3 TURBO_ORGANIZER.py

echo ""
echo "================================================================================"
echo "⚡ TURBO COMPLETE!"
echo "================================================================================"
echo ""
echo "Press any key to close..."
read -n 1

