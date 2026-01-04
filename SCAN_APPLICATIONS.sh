#!/bin/bash

# ═══════════════════════════════════════════════════════════════════
# SCAN APPLICATIONS - INVENTORY ALL AVAILABLE TOOLS
# ═══════════════════════════════════════════════════════════════════
# Created for: Gabriel Almeida - NOIZYLAB AI CPU Repair
# Purpose: Discover all repair/diagnostic/creative tools installed
# ═══════════════════════════════════════════════════════════════════

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

OUTPUT_FILE="$HOME/NOIZYLAB/APPLICATIONS_INVENTORY.txt"

clear

echo -e "${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════════╗
║              APPLICATIONS INVENTORY SCAN                          ║
║          Discovering All Available Tools & Utilities             ║
╚═══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo -e "${YELLOW}Scanning /Applications folder...${NC}"
echo ""

# Initialize output file
echo "═══════════════════════════════════════════════════════════════════" > "$OUTPUT_FILE"
echo "NOIZYLAB APPLICATIONS INVENTORY" >> "$OUTPUT_FILE"
echo "Generated: $(date)" >> "$OUTPUT_FILE"
echo "═══════════════════════════════════════════════════════════════════" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# ═══════════════════════════════════════════════════════════════════
# CATEGORY 1: DISK REPAIR & DIAGNOSTIC TOOLS
# ═══════════════════════════════════════════════════════════════════

echo -e "${GREEN}🔧 DISK REPAIR & DIAGNOSTIC TOOLS:${NC}"
echo "" >> "$OUTPUT_FILE"
echo "🔧 DISK REPAIR & DIAGNOSTIC TOOLS:" >> "$OUTPUT_FILE"
echo "─────────────────────────────────────────────────────────────────" >> "$OUTPUT_FILE"

DISK_TOOLS=(
    "TechTool Pro.app"
    "TechTool Pro 21.app"
    "Drive Genius.app"
    "Drive Genius 7.app"
    "DiskWarrior.app"
    "Disk Utility.app"
    "DriveDx.app"
    "SMART Utility.app"
    "Onyx.app"
    "CleanMyMac X.app"
    "DaisyDisk.app"
    "OmniDiskSweeper.app"
)

for app in "${DISK_TOOLS[@]}"; do
    if [ -d "/Applications/$app" ]; then
        echo -e "  ${GREEN}✓${NC} $app"
        echo "✓ $app" >> "$OUTPUT_FILE"
    fi
done
echo "" >> "$OUTPUT_FILE"

# ═══════════════════════════════════════════════════════════════════
# CATEGORY 2: DATA RECOVERY TOOLS
# ═══════════════════════════════════════════════════════════════════

echo ""
echo -e "${GREEN}🚑 DATA RECOVERY TOOLS:${NC}"
echo "🚑 DATA RECOVERY TOOLS:" >> "$OUTPUT_FILE"
echo "─────────────────────────────────────────────────────────────────" >> "$OUTPUT_FILE"

RECOVERY_TOOLS=(
    "Disk Drill.app"
    "Data Rescue.app"
    "EaseUS Data Recovery.app"
    "PhotoRec.app"
    "R-Studio.app"
    "Stellar Data Recovery.app"
    "Prosoft Data Rescue.app"
)

for app in "${RECOVERY_TOOLS[@]}"; do
    if [ -d "/Applications/$app" ]; then
        echo -e "  ${GREEN}✓${NC} $app"
        echo "✓ $app" >> "$OUTPUT_FILE"
    fi
done
echo "" >> "$OUTPUT_FILE"

# ═══════════════════════════════════════════════════════════════════
# CATEGORY 3: BACKUP & CLONING TOOLS
# ═══════════════════════════════════════════════════════════════════

echo ""
echo -e "${GREEN}💾 BACKUP & CLONING TOOLS:${NC}"
echo "💾 BACKUP & CLONING TOOLS:" >> "$OUTPUT_FILE"
echo "─────────────────────────────────────────────────────────────────" >> "$OUTPUT_FILE"

BACKUP_TOOLS=(
    "Carbon Copy Cloner.app"
    "SuperDuper!.app"
    "ChronoSync.app"
    "Acronis True Image.app"
    "Time Machine.app"
    "Backblaze.app"
    "Arq.app"
    "Get Backup Pro.app"
)

for app in "${BACKUP_TOOLS[@]}"; do
    if [ -d "/Applications/$app" ]; then
        echo -e "  ${GREEN}✓${NC} $app"
        echo "✓ $app" >> "$OUTPUT_FILE"
    fi
done
echo "" >> "$OUTPUT_FILE"

# ═══════════════════════════════════════════════════════════════════
# CATEGORY 4: AUDIO/VIDEO PRODUCTION TOOLS
# ═══════════════════════════════════════════════════════════════════

echo ""
echo -e "${GREEN}🎵 AUDIO/VIDEO PRODUCTION:${NC}"
echo "🎵 AUDIO/VIDEO PRODUCTION:" >> "$OUTPUT_FILE"
echo "─────────────────────────────────────────────────────────────────" >> "$OUTPUT_FILE"

PRODUCTION_TOOLS=(
    "Logic Pro.app"
    "Pro Tools.app"
    "Ableton Live.app"
    "FL Studio.app"
    "Studio One.app"
    "Cubase.app"
    "Reaper.app"
    "GarageBand.app"
    "Final Cut Pro.app"
    "Adobe Premiere Pro.app"
    "DaVinci Resolve.app"
    "Compressor.app"
    "Motion.app"
)

for app in "${PRODUCTION_TOOLS[@]}"; do
    if [ -d "/Applications/$app" ]; then
        echo -e "  ${GREEN}✓${NC} $app"
        echo "✓ $app" >> "$OUTPUT_FILE"
    fi
done
echo "" >> "$OUTPUT_FILE"

# ═══════════════════════════════════════════════════════════════════
# CATEGORY 5: SYSTEM MONITORING & OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════

echo ""
echo -e "${GREEN}📊 SYSTEM MONITORING & OPTIMIZATION:${NC}"
echo "📊 SYSTEM MONITORING & OPTIMIZATION:" >> "$OUTPUT_FILE"
echo "─────────────────────────────────────────────────────────────────" >> "$OUTPUT_FILE"

MONITORING_TOOLS=(
    "Activity Monitor.app"
    "iStat Menus.app"
    "MenuMeters.app"
    "Intel Power Gadget.app"
    "Macs Fan Control.app"
    "Sensei.app"
    "CleanMyMac X.app"
    "AppCleaner.app"
    "The Unarchiver.app"
)

for app in "${MONITORING_TOOLS[@]}"; do
    if [ -d "/Applications/$app" ]; then
        echo -e "  ${GREEN}✓${NC} $app"
        echo "✓ $app" >> "$OUTPUT_FILE"
    fi
done
echo "" >> "$OUTPUT_FILE"

# ═══════════════════════════════════════════════════════════════════
# CATEGORY 6: DEVELOPMENT & AUTOMATION TOOLS
# ═══════════════════════════════════════════════════════════════════

echo ""
echo -e "${GREEN}💻 DEVELOPMENT & AUTOMATION:${NC}"
echo "💻 DEVELOPMENT & AUTOMATION:" >> "$OUTPUT_FILE"
echo "─────────────────────────────────────────────────────────────────" >> "$OUTPUT_FILE"

DEV_TOOLS=(
    "Visual Studio Code.app"
    "Xcode.app"
    "Sublime Text.app"
    "BBEdit.app"
    "Terminal.app"
    "iTerm.app"
    "Docker.app"
    "GitHub Desktop.app"
    "Sourcetree.app"
    "Homebrew.app"
    "Python.app"
)

for app in "${DEV_TOOLS[@]}"; do
    if [ -d "/Applications/$app" ]; then
        echo -e "  ${GREEN}✓${NC} $app"
        echo "✓ $app" >> "$OUTPUT_FILE"
    fi
done
echo "" >> "$OUTPUT_FILE"

# ═══════════════════════════════════════════════════════════════════
# FULL APPLICATION LIST (EVERYTHING)
# ═══════════════════════════════════════════════════════════════════

echo ""
echo -e "${CYAN}Generating complete application list...${NC}"
echo "" >> "$OUTPUT_FILE"
echo "═══════════════════════════════════════════════════════════════════" >> "$OUTPUT_FILE"
echo "COMPLETE APPLICATION LIST (ALL .app BUNDLES):" >> "$OUTPUT_FILE"
echo "═══════════════════════════════════════════════════════════════════" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# List ALL applications
ls -1 /Applications/ | grep ".app$" | sort >> "$OUTPUT_FILE" 2>/dev/null

# Also check /Applications/Utilities/
echo "" >> "$OUTPUT_FILE"
echo "UTILITIES FOLDER:" >> "$OUTPUT_FILE"
echo "─────────────────────────────────────────────────────────────────" >> "$OUTPUT_FILE"
ls -1 /Applications/Utilities/ | grep ".app$" | sort >> "$OUTPUT_FILE" 2>/dev/null

# ═══════════════════════════════════════════════════════════════════
# COMMAND-LINE TOOLS (HOMEBREW)
# ═══════════════════════════════════════════════════════════════════

echo "" >> "$OUTPUT_FILE"
echo "═══════════════════════════════════════════════════════════════════" >> "$OUTPUT_FILE"
echo "COMMAND-LINE TOOLS (HOMEBREW):" >> "$OUTPUT_FILE"
echo "═══════════════════════════════════════════════════════════════════" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

if command -v brew &> /dev/null; then
    echo -e "${CYAN}Checking Homebrew installations...${NC}"
    brew list --formula 2>/dev/null >> "$OUTPUT_FILE"
else
    echo "Homebrew not installed" >> "$OUTPUT_FILE"
fi

# ═══════════════════════════════════════════════════════════════════
# SUMMARY & RECOMMENDATIONS
# ═══════════════════════════════════════════════════════════════════

echo "" >> "$OUTPUT_FILE"
echo "═══════════════════════════════════════════════════════════════════" >> "$OUTPUT_FILE"
echo "NOIZYLAB AI CPU REPAIR - TOOL RECOMMENDATIONS:" >> "$OUTPUT_FILE"
echo "═══════════════════════════════════════════════════════════════════" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cat >> "$OUTPUT_FILE" << 'EOF'
RECOMMENDED TOOL COMBINATIONS FOR DIFFERENT SCENARIOS:

1. FROZEN/SLOW DRIVES (Your current issue):
   Primary: TechTool Pro 21 → Volume Structures test
   Secondary: Drive Genius → DrivePulse monitoring
   Fallback: DiskWarrior → Directory rebuild
   Automation: ~/NOIZYLAB/TTP21_HOT_ROD_GUIDE.sh

2. DATA RECOVERY (Deleted/corrupted files):
   Primary: Disk Drill → GUI-based, user-friendly
   Secondary: PhotoRec/TestDisk → Command-line, powerful
   Advanced: R-Studio → Professional-grade
   Emergency: Partner with DriveSavers/Ontrack labs

3. PREVENTIVE MAINTENANCE:
   Daily: Drive Genius DrivePulse → SMART monitoring
   Weekly: TechTool Pro → Quick scan
   Monthly: Carbon Copy Cloner → Full system backup
   Continuous: ~/NOIZYLAB/QUICK_STATUS.sh (automated)

4. PERFORMANCE OPTIMIZATION:
   Monitoring: iStat Menus → Real-time system stats
   Cleanup: CleanMyMac X → Remove junk files
   Diagnostics: Activity Monitor → Process management
   Automation: ~/NOIZYLAB/ULTRA_AGGRESSIVE.sh

5. AUDIO/VIDEO ARCHIVE PROTECTION (40-year collection):
   Primary backup: Carbon Copy Cloner → Bootable clone
   Cloud backup: Backblaze → Unlimited cloud storage
   Version control: ChronoSync → Incremental backups
   Integrity checks: DaisyDisk → Visual space analysis

EOF

# ═══════════════════════════════════════════════════════════════════
# FINALIZE OUTPUT
# ═══════════════════════════════════════════════════════════════════

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ SCAN COMPLETE!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}Full inventory saved to:${NC}"
echo -e "${CYAN}$OUTPUT_FILE${NC}"
echo ""
echo -e "${YELLOW}View the full report:${NC}"
echo -e "${CYAN}cat $OUTPUT_FILE${NC}"
echo ""
echo -e "${YELLOW}Or open in default text editor:${NC}"
echo -e "${CYAN}open $OUTPUT_FILE${NC}"
echo ""

# Display summary count
APP_COUNT=$(ls -1 /Applications/ 2>/dev/null | grep ".app$" | wc -l | xargs)
UTIL_COUNT=$(ls -1 /Applications/Utilities/ 2>/dev/null | grep ".app$" | wc -l | xargs)
TOTAL=$((APP_COUNT + UTIL_COUNT))

echo -e "${GREEN}📊 SUMMARY:${NC}"
echo -e "  Applications folder: ${CYAN}$APP_COUNT${NC} apps"
echo -e "  Utilities folder: ${CYAN}$UTIL_COUNT${NC} apps"
echo -e "  ${YELLOW}TOTAL: $TOTAL applications${NC}"
echo ""

echo -e "${MAGENTA}═══════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}NEXT STEPS:${NC}"
echo -e "${MAGENTA}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo "1. Review the inventory to see what tools you have"
echo "2. Run TechTool Pro 21 to fix your frozen drives"
echo "3. Set up Drive Genius for ongoing monitoring"
echo "4. Configure automated backups with Carbon Copy Cloner"
echo ""
echo -e "${GREEN}🚀 Ready to build NOIZYLAB AI CPU Repair with these tools!${NC}"
echo ""
