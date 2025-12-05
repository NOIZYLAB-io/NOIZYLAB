#!/bin/bash
# FISH MUSIC INC - AUTO BACKUP SYSTEM
# Intelligent backup for critical Fish Music volumes
# Created by CB_01 for ROB - GORUNFREE! 🎸🔥

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo ""
echo "💾 FISH MUSIC INC - AUTO BACKUP SYSTEM"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# Critical volumes to backup
CRITICAL_VOLUMES=(
    "4TB Blue Fish"
    "4TB FISH SG"
    "4TB Big Fish"
    "FISH"
    "4TB Lacie"
)

# Backup destination
BACKUP_DEST="/Volumes/12TB/FISH_BACKUPS"

echo "🔍 Checking critical Fish Music volumes..."
echo ""

for vol in "${CRITICAL_VOLUMES[@]}"; do
    if [ -d "/Volumes/$vol" ]; then
        SIZE=$(du -sh "/Volumes/$vol" 2>/dev/null | awk '{print $1}')
        echo -e "${GREEN}✅ $vol ($SIZE)${NC}"

        # Check if Design 2025 stems
        if [ "$vol" == "4TB Lacie" ]; then
            if [ -d "/Volumes/$vol/ DESIGN 2025" ]; then
                echo -e "   ${BLUE}🎬 Design 2025 stems detected!${NC}"
            fi
        fi
    else
        echo -e "${YELLOW}⚠️  $vol - not mounted${NC}"
    fi
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "💡 To backup a volume:"
echo "   rsync -avh --progress \"/Volumes/SOURCE/\" \"$BACKUP_DEST/SOURCE_BACKUP/\""
echo ""
echo "🎯 Priority: 4TB Lacie (Design 2025 stems) - backup FIRST!"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "GORUNFREE! 🎸🔥"

