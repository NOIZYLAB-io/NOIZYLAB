#!/bin/bash
# MASTER SCRIPT - Execute full organization workflow

set -e

echo "================================================================================"
echo "🎵 WAV FILE ORGANIZATION SYSTEM 🎵"
echo "================================================================================"
echo ""
echo "⭐⭐⭐ HARD RULE ⭐⭐⭐"
echo "ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!"
echo ""
echo "================================================================================"
echo ""

cd "/Volumes/4TBSG/KTK 2026 TO SORT"

# Step 1: Preview
echo "STEP 1: PREVIEW SCAN"
echo "================================================================================"
/usr/bin/python3 preview_organization.py
echo ""
echo "Press ENTER to continue with full organization, or Ctrl+C to cancel..."
read

# Step 2: Full Organization
echo ""
echo "STEP 2: FULL ORGANIZATION"
echo "================================================================================"
/usr/bin/python3 organize_by_metadata.py

echo ""
echo "================================================================================"
echo "✓ ORGANIZATION COMPLETE!"
echo "================================================================================"
echo ""
echo "Check your results in: ORGANIZED_WAVES/"
echo ""
echo "Press any key to close..."
read -n 1

