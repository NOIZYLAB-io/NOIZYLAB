#!/bin/bash
# 🧹 HOME DIRECTORY CLEANUP & ORGANIZATION MASTER SCRIPT

echo "🧹 NOIZYLAB HOME CLEANUP - STARTING..."
echo "======================================="
echo ""

# Create organized structure in NOIZYLAB
mkdir -p NOIZYLAB/_HOME_ARCHIVE/{Scripts,Screenshots,Downloads,Documents,Config_Backups,Misc}

echo "📁 Created organization structure"
echo ""

# Move stray Python scripts to NOIZYLAB
echo "🐍 Moving Python scripts..."
mv -v ai_tandem.py NOIZYLAB/_HOME_ARCHIVE/Scripts/ 2>/dev/null
mv -v downloads_scan_report.json NOIZYLAB/_HOME_ARCHIVE/Misc/ 2>/dev/null

# Move Desktop screenshots
echo "📸 Organizing Desktop screenshots..."
mv -v Desktop/*.png NOIZYLAB/_HOME_ARCHIVE/Screenshots/ 2>/dev/null

# Move SPEECH folder
echo "🗣️  Moving SPEECH folder..."
mv -v Desktop/SPEECH NOIZYLAB/_HOME_ARCHIVE/ 2>/dev/null

# Handle Downloads
echo "⬇️  Organizing Downloads..."
mkdir -p NOIZYLAB/_HOME_ARCHIVE/Downloads/Installers
mv -v Downloads/*.dmg NOIZYLAB/_HOME_ARCHIVE/Downloads/Installers/ 2>/dev/null
mv -v Downloads/*.zip NOIZYLAB/_HOME_ARCHIVE/Downloads/ 2>/dev/null
mv -v Downloads/speech_control.py NOIZYLAB/_HOME_ARCHIVE/Scripts/ 2>/dev/null
mv -v Downloads/*INSTRUCTIONS*.txt NOIZYLAB/_HOME_ARCHIVE/Downloads/ 2>/dev/null
mv -v Downloads/README.md NOIZYLAB/_HOME_ARCHIVE/Downloads/ 2>/dev/null
mv -v Downloads/_START_HERE.txt NOIZYLAB/_HOME_ARCHIVE/Downloads/ 2>/dev/null

# Move specific project folders
echo "📦 Moving project folders..."
mv -v Downloads/ROB-PLOWMAN-GORUNFREE-SINGLE-CLI NOIZYLAB/_HOME_ARCHIVE/ 2>/dev/null
mv -v Downloads/G_DLS NOIZYLAB/_HOME_ARCHIVE/ 2>/dev/null

# Move Documents content
echo "📄 Organizing Documents..."
mv -v "Documents/CUSTOM FOLDERS" NOIZYLAB/_HOME_ARCHIVE/Documents/ 2>/dev/null
mv -v "Documents/Dadroit JSON Generator" NOIZYLAB/_HOME_ARCHIVE/Documents/ 2>/dev/null
mv -v "Documents/Text - Sorted By MyQuickMac Neo" NOIZYLAB/_HOME_ARCHIVE/Documents/ 2>/dev/null

# Backup important dotfiles (but keep originals)
echo "💾 Backing up config files..."
cp -v .zshrc NOIZYLAB/_HOME_ARCHIVE/Config_Backups/ 2>/dev/null
cp -v .zsh_history NOIZYLAB/_HOME_ARCHIVE/Config_Backups/ 2>/dev/null
cp -v QUICK_LINKS.md NOIZYLAB/_HOME_ARCHIVE/ 2>/dev/null

# Move iMessageSpamFilter
echo "📧 Moving iMessageSpamFilter..."
mv -v iMessageSpamFilter NOIZYLAB/_HOME_ARCHIVE/ 2>/dev/null

echo ""
echo "✅ HOME CLEANUP COMPLETE!"
echo ""
echo "📊 SUMMARY:"
echo "  - Scripts moved to NOIZYLAB/_HOME_ARCHIVE/Scripts/"
echo "  - Screenshots moved to NOIZYLAB/_HOME_ARCHIVE/Screenshots/"
echo "  - Downloads organized in NOIZYLAB/_HOME_ARCHIVE/Downloads/"
echo "  - Documents moved to NOIZYLAB/_HOME_ARCHIVE/Documents/"
echo "  - Config backups in NOIZYLAB/_HOME_ARCHIVE/Config_Backups/"
echo ""
echo "✅ Your home directory is now clean!"
echo "✅ Everything important is in NOIZYLAB/_HOME_ARCHIVE/"
echo ""
echo "GORUNFREE! 🚀"

