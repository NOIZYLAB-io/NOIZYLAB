#!/bin/bash
#
# ONE COMMAND - COMPLETE 6TB SCAN & HEAL & ORGANIZE
# FISH MUSIC INC - GORUNFREE! 🎸🔥
#

echo ""
echo "=========================================="
echo "🚀 6TB COMPLETE SCAN + HEAL + ORGANIZE"
echo "=========================================="
echo ""

# 1. Run Python scanner
echo "🔍 STEP 1/2: SCANNING & ANALYZING..."
echo ""
python3 /Volumes/6TB/SCAN_AND_HEAL_6TB.py

# 2. Run organizer
echo ""
echo "🔧 STEP 2/2: ORGANIZING..."
echo ""
bash /Volumes/6TB/ORGANIZE_6TB.sh

echo ""
echo "=========================================="
echo "✅ COMPLETE! 6TB IS PERFECTED"
echo "=========================================="
echo ""
echo "📊 Check these files:"
echo "  - SCAN_REPORT_*.json (detailed analysis)"
echo "  - SCAN_REPORT_*.txt (human-readable)"
echo "  - FOLDER_SIZES.txt (folder index)"
echo "  - organize_*.log (organization log)"
echo ""
echo "🔥 GORUNFREE! 🎸"
echo ""
