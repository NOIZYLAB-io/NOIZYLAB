#!/bin/bash
#
# 6TB DRIVE ORGANIZER - FISH MUSIC INC
# Perfect folder structure + permissions + metadata
# GORUNFREE! 🎸🔥
#

set -e

DRIVE="/Volumes/6TB"
LOG="$DRIVE/organize_$(date +%Y%m%d_%H%M%S).log"

echo "========================================" | tee "$LOG"
echo "🔧 6TB DRIVE ORGANIZER - STARTING" | tee -a "$LOG"
echo "========================================" | tee -a "$LOG"

# 1. FIX PERMISSIONS
echo "" | tee -a "$LOG"
echo "🔐 FIXING PERMISSIONS..." | tee -a "$LOG"

# Main folders - read/write for user
chmod -R u+rw "$DRIVE" 2>/dev/null || echo "  Some permissions unchanged (expected)"

echo "  ✅ Permissions updated" | tee -a "$LOG"

# 2. CREATE ORGANIZED STRUCTURE
echo "" | tee -a "$LOG"
echo "📁 ENSURING ORGANIZED STRUCTURE..." | tee -a "$LOG"

mkdir -p "$DRIVE/MUSIC_MASTER/Audio_Samples"
mkdir -p "$DRIVE/MUSIC_MASTER/Kontakt_Libraries"
mkdir -p "$DRIVE/MUSIC_MASTER/Native_Instruments"
mkdir -p "$DRIVE/MUSIC_MASTER/Plugins"
mkdir -p "$DRIVE/MUSIC_MASTER/Projects"
mkdir -p "$DRIVE/MUSIC_MASTER/Stems"
mkdir -p "$DRIVE/ARCHIVE/Backups"
mkdir -p "$DRIVE/ARCHIVE/Old_Projects"
mkdir -p "$DRIVE/WORKING/Active_Projects"
mkdir -p "$DRIVE/WORKING/Design_Reunion"

echo "  ✅ Folder structure ready" | tee -a "$LOG"

# 3. FIX FILE NAMES (remove special chars)
echo "" | tee -a "$LOG"
echo "🏷️  FIXING FILENAMES..." | tee -a "$LOG"

fixed=0
# Find files with problematic characters (safely)
find "$DRIVE" -depth -name "*[<>:\"|?*]*" 2>/dev/null | while read -r file; do
    newname=$(echo "$file" | sed 's/[<>:"|?*]/_/g')
    if [ "$file" != "$newname" ]; then
        mv "$file" "$newname" 2>/dev/null && ((fixed++)) || true
    fi
done

echo "  ✅ Fixed $fixed filenames" | tee -a "$LOG"

# 4. REMOVE EMPTY FOLDERS
echo "" | tee -a "$LOG"
echo "🗑️  REMOVING EMPTY FOLDERS..." | tee -a "$LOG"

removed=$(find "$DRIVE" -type d -empty -delete 2>/dev/null | wc -l)
echo "  ✅ Removed $removed empty folders" | tee -a "$LOG"

# 5. CREATE INDEX
echo "" | tee -a "$LOG"
echo "📋 CREATING FILE INDEX..." | tee -a "$LOG"

# Top-level folders summary
du -sh "$DRIVE"/* 2>/dev/null | sort -hr > "$DRIVE/FOLDER_SIZES.txt"

# Audio file count by type
echo "" >> "$DRIVE/FOLDER_SIZES.txt"
echo "AUDIO FILES BY TYPE:" >> "$DRIVE/FOLDER_SIZES.txt"
find "$DRIVE" -type f -name "*.wav" 2>/dev/null | wc -l | xargs echo "  WAV files:" >> "$DRIVE/FOLDER_SIZES.txt"
find "$DRIVE" -type f -name "*.aif*" 2>/dev/null | wc -l | xargs echo "  AIF files:" >> "$DRIVE/FOLDER_SIZES.txt"
find "$DRIVE" -type f -name "*.mp3" 2>/dev/null | wc -l | xargs echo "  MP3 files:" >> "$DRIVE/FOLDER_SIZES.txt"
find "$DRIVE" -type f -name "*.flac" 2>/dev/null | wc -l | xargs echo "  FLAC files:" >> "$DRIVE/FOLDER_SIZES.txt"

echo "  ✅ Index created: FOLDER_SIZES.txt" | tee -a "$LOG"

# 6. VERIFY HEALTH
echo "" | tee -a "$LOG"
echo "🏥 VERIFYING HEALTH..." | tee -a "$LOG"

# Test write
touch "$DRIVE/.health_test" && rm "$DRIVE/.health_test" && echo "  ✅ Write test: PASS" | tee -a "$LOG" || echo "  ⚠️  Write test: FAIL" | tee -a "$LOG"

# Check disk usage
df -h "$DRIVE" | tail -1 | tee -a "$LOG"

echo "" | tee -a "$LOG"
echo "========================================" | tee -a "$LOG"
echo "✅ ORGANIZATION COMPLETE!" | tee -a "$LOG"
echo "========================================" | tee -a "$LOG"
echo "" | tee -a "$LOG"
echo "📊 RESULTS:" | tee -a "$LOG"
echo "  - Permissions fixed" | tee -a "$LOG"
echo "  - Folders organized" | tee -a "$LOG"
echo "  - Filenames cleaned" | tee -a "$LOG"
echo "  - Empty folders removed" | tee -a "$LOG"
echo "  - Index created" | tee -a "$LOG"
echo "" | tee -a "$LOG"
echo "🔥 GORUNFREE! 🎸" | tee -a "$LOG"
echo "" | tee -a "$LOG"
echo "Log saved: $LOG" | tee -a "$LOG"
