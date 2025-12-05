#!/bin/bash
# 🗄️ 6TB MASTER CONTROL SYSTEM 🗄️

clear

cat << "EOF"
================================================================================
🗄️ 6TB COMPLETE DRIVE ORGANIZATION SYSTEM 🗄️
================================================================================

⭐⭐⭐ HARD RULE ⭐⭐⭐
ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!

MASTER SYSTEM FEATURES:
✓ Scans ENTIRE 6TB drive
✓ Finds ALL WAV files everywhere
✓ Database indexing for fast queries
✓ Parallel processing
✓ Crash recovery
✓ Progress tracking
✓ Identifies ALL your original compositions
✓ Organizes commercial samples by source
✓ Generates comprehensive reports

================================================================================
MENU:
================================================================================

1. 🔍 FULL 6TB SCAN (Scan entire drive)
2. 📊 QUERY DATABASE (Search and stats)
3. 🔨 REBUILD STRUCTURE (Organize files)
4. 📄 GENERATE REPORTS
5. ⚡ Quick Stats
6. Exit

EOF

echo -n "Choose option (1-6): "
read choice

cd "$(dirname "$0")"

case $choice in
    1)
        echo ""
        echo "🔍 Starting FULL 6TB SCAN..."
        echo "This will take 10-30 minutes depending on file count."
        echo ""
        echo "Press Enter to start, or Ctrl+C to cancel..."
        read
        /usr/bin/python3 6TB_SCANNER.py
        ;;
    2)
        echo ""
        /usr/bin/python3 6TB_QUERY.py
        ;;
    3)
        echo ""
        echo "🔨 REBUILD STRUCTURE"
        echo "This will organize all files based on the database."
        echo ""
        /usr/bin/python3 6TB_REBUILD.py
        ;;
    4)
        echo ""
        echo "📄 Generating reports..."
        /usr/bin/python3 6TB_REBUILD.py html
        /usr/bin/python3 6TB_QUERY.py export
        echo ""
        echo "✓ Reports generated in 6TB_REPORTS/"
        ;;
    5)
        echo ""
        /usr/bin/python3 6TB_QUERY.py stats
        ;;
    6)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid option"
        ;;
esac

echo ""
echo "Press Enter to return to menu..."
read

exec "$0"

