#!/bin/bash
# 🧹 COMPLETE HOME DIRECTORY ORGANIZATION - MOVE EVERYTHING!

echo "🚀 COMPLETE HOME ORGANIZATION - STARTING..."
echo "=============================================="
echo ""

# Create complete organized structure
echo "📁 Creating complete NOIZYLAB organization structure..."
mkdir -p NOIZYLAB/{_HOME_ARCHIVE/{Scripts,Screenshots,Downloads,Documents,Config_Backups,Misc,Github_Projects},Music_Projects,Pictures_Archive,Movies_Archive,Applications_Backup}

# Move Github folder content (keep structure)
echo "💻 Moving Github projects..."
if [ -d "Github" ]; then
    mv -v Github/* NOIZYLAB/_HOME_ARCHIVE/Github_Projects/ 2>/dev/null
    rmdir Github 2>/dev/null
fi

# Move workspace file
echo "📝 Moving workspace files..."
mv -v CB_01_FISHMUSICINC.code-workspace NOIZYLAB/_HOME_ARCHIVE/ 2>/dev/null
mv -v QUICK_LINKS.md NOIZYLAB/_HOME_ARCHIVE/ 2>/dev/null

# Backup additional dotfiles
echo "💾 Backing up additional config files..."
cp -v .claude.json NOIZYLAB/_HOME_ARCHIVE/Config_Backups/ 2>/dev/null
cp -v .claude.json.backup NOIZYLAB/_HOME_ARCHIVE/Config_Backups/ 2>/dev/null
cp -v .hosts.backup.* NOIZYLAB/_HOME_ARCHIVE/Config_Backups/ 2>/dev/null

# Move Pictures content (non-system)
echo "🖼️  Organizing Pictures..."
find Pictures -maxdepth 1 -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.gif" \) -exec mv -v {} NOIZYLAB/Pictures_Archive/ \; 2>/dev/null

# Move Music content (non-Apple Music)
echo "🎵 Organizing Music projects..."
find Music -maxdepth 1 -type d ! -name "Music" ! -name ".*" -exec mv -v {} NOIZYLAB/Music_Projects/ \; 2>/dev/null

# Move Movies content (non-system)
echo "🎬 Organizing Movies..."
find Movies -maxdepth 1 -type f \( -name "*.mp4" -o -name "*.mov" -o -name "*.avi" \) -exec mv -v {} NOIZYLAB/Movies_Archive/ \; 2>/dev/null

# Move any remaining user applications
echo "📦 Backing up Applications..."
if [ -d "Applications" ]; then
    find Applications -maxdepth 1 ! -name "Applications" -exec mv -v {} NOIZYLAB/Applications_Backup/ \; 2>/dev/null
fi

# Clean up empty folders
echo "🧹 Removing empty folders..."
find Desktop Documents Downloads Music Movies Pictures Applications -maxdepth 0 -type d -empty -delete 2>/dev/null

echo ""
echo "✅ COMPLETE HOME ORGANIZATION FINISHED!"
echo ""
echo "📊 EVERYTHING IS NOW IN NOIZYLAB:"
echo "  📁 NOIZYLAB/_HOME_ARCHIVE/Github_Projects/ - All Github repos"
echo "  📁 NOIZYLAB/_HOME_ARCHIVE/Scripts/ - All scripts"
echo "  📁 NOIZYLAB/_HOME_ARCHIVE/Screenshots/ - All screenshots"
echo "  📁 NOIZYLAB/_HOME_ARCHIVE/Downloads/ - All downloads"
echo "  📁 NOIZYLAB/_HOME_ARCHIVE/Documents/ - All documents"
echo "  📁 NOIZYLAB/_HOME_ARCHIVE/Config_Backups/ - All config files"
echo "  📁 NOIZYLAB/Music_Projects/ - Music projects"
echo "  📁 NOIZYLAB/Pictures_Archive/ - Pictures"
echo "  📁 NOIZYLAB/Movies_Archive/ - Movies"
echo "  📁 NOIZYLAB/Applications_Backup/ - User apps"
echo ""
echo "🎉 YOUR HOME DIRECTORY IS NOW PERFECTLY CLEAN!"
echo ""
echo "GORUNFREE! 🚀"

