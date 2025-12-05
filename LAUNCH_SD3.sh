#!/bin/bash
# INSTANT SUPERIOR DRUMMER 3 LAUNCHER

clear

cat << 'EOF'
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║      🥁 SUPERIOR DRUMMER 3 - INSTANT LAUNCHER 🥁               ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝

Choose your tool:

  1. 🚀 Instant Info        (2 seconds - Quick overview)
  2. 🎯 Quick Finder        (Interactive groove browser)
  3. 📊 Full Manager        (Complete management suite)
  4. 📁 Open in Finder      (Browse files directly)
  5. 📄 View Reports        (All saved reports)

  0. Exit

EOF

read -p "Choice: " choice

case $choice in
    1)
        bash "/Volumes/MAG 4TB/NoizyWorkspace/noizyfish_aquarium/PY/sd3_instant.sh"
        ;;
    2)
        python3 "/Volumes/MAG 4TB/NoizyWorkspace/noizyfish_aquarium/PY/sd3_quick.py"
        ;;
    3)
        python3 "/Volumes/MAG 4TB/NoizyWorkspace/noizyfish_aquarium/PY/superior_drummer_manager.py"
        ;;
    4)
        open "/Volumes/MAG 4TB/_EZ Drummer/Midi/000011@SUPERIOR_DRUMMER_3"
        echo "✅ Opened in Finder!"
        ;;
    5)
        cat "/Volumes/MAG 4TB/NoizyWorkspace/SUPERIOR_DRUMMER_QUICK_REF.txt"
        echo ""
        echo "Other reports:"
        ls -lh "/Volumes/MAG 4TB/NoizyWorkspace/" | grep -i "superior"
        ;;
    0)
        echo "👋 Bye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice"
        ;;
esac

echo ""
read -p "Press Enter to continue..."

