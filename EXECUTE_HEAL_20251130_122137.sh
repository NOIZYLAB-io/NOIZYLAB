#!/usr/bin/env bash
# =============================================================================
# 🔥 MASTER HEAL & UPDATE EXECUTION SCRIPT
# Generated: 2025-11-30 12:24:17
# For: Rob Plowman - NOIZYLAB & Fish Music Inc
# =============================================================================

set -euo pipefail

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

log() { echo -e "${CYAN}[$(date +'%H:%M:%S')]${NC} $1"; }
success() { echo -e "${GREEN}✅${NC} $1"; }
warning() { echo -e "${YELLOW}⚠️${NC} $1"; }
error() { echo -e "${RED}❌${NC} $1"; }

echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║           🔥 MASTER HEAL & UPDATE EXECUTION 🔥                    ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo ""

# Check volumes
if [ ! -d "/Volumes/SAMPLE_MASTER" ]; then
    error "SAMPLE_MASTER not mounted!"
    exit 1
fi

if [ ! -d "/Volumes/6TB" ]; then
    error "6TB not mounted!"
    exit 1
fi

success "Both volumes mounted"
echo ""

# Check available space
AVAIL=$(df -g /Volumes/SAMPLE_MASTER | tail -1 | awk '{print $4}')
log "SAMPLE_MASTER available space: ${AVAIL} GB"
echo ""

# Create target structure
log "Creating target folder structure..."
mkdir -p "/Volumes/SAMPLE_MASTER/01_Native_Instruments"
mkdir -p "/Volumes/SAMPLE_MASTER/02_8Dio"
mkdir -p "/Volumes/SAMPLE_MASTER/03_Spectrasonics"
mkdir -p "/Volumes/SAMPLE_MASTER/04_Toontrack"
mkdir -p "/Volumes/SAMPLE_MASTER/05_Orchestral"
mkdir -p "/Volumes/SAMPLE_MASTER/06_Drums_Percussion"
mkdir -p "/Volumes/SAMPLE_MASTER/07_Synths_Keys"
mkdir -p "/Volumes/SAMPLE_MASTER/08_Guitars_Bass"
mkdir -p "/Volumes/SAMPLE_MASTER/09_Vocals_Choir"
mkdir -p "/Volumes/SAMPLE_MASTER/10_World_Ethnic"
mkdir -p "/Volumes/SAMPLE_MASTER/11_SFX_Cinematic"
mkdir -p "/Volumes/SAMPLE_MASTER/12_Loops_Construction"
mkdir -p "/Volumes/SAMPLE_MASTER/13_Nexus_reFX"
mkdir -p "/Volumes/SAMPLE_MASTER/99_Archives"

success "Folder structure created"
echo ""

# Migration function
migrate_library() {
    local SOURCE="$1"
    local TARGET="$2"
    local NAME="$3"
    
    if [ ! -d "$SOURCE" ]; then
        warning "Source not found: $SOURCE"
        return 1
    fi
    
    log "Migrating: $NAME"
    log "  From: $SOURCE"
    log "  To: $TARGET"
    
    mkdir -p "$TARGET"
    
    # Use rsync for reliable transfer with progress
    rsync -av --progress "$SOURCE/" "$TARGET/" 2>&1 | tail -5
    
    if [ $? -eq 0 ]; then
        success "Completed: $NAME"
    else
        error "Failed: $NAME"
        return 1
    fi
    echo ""
}

echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║                    STARTING MIGRATIONS                            ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo ""

migrate_library \
    "/Volumes/6TB/_NI_2026/LIBRARIES/Native Instruments/COMPLETE" \
    "/Volumes/SAMPLE_MASTER/01_Native_Instruments/COMPLETE" \
    "COMPLETE"

migrate_library \
    "/Volumes/6TB/_NI_2026/LIBRARIES/8Dio/PARTIAL/8Dio Libraries" \
    "/Volumes/SAMPLE_MASTER/02_8Dio" \
    "8Dio Libraries"

migrate_library \
    "/Volumes/6TB/Superior Drummer" \
    "/Volumes/SAMPLE_MASTER/04_Toontrack/Superior_Drummer" \
    "Superior Drummer"

migrate_library \
    "/Volumes/6TB/KONTAKT_LAB/DEEP_ORGANIZED" \
    "/Volumes/SAMPLE_MASTER/05_Orchestral/_DEEP_ORGANIZED" \
    "DEEP_ORGANIZED"


echo ""
echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║                    MIGRATION COMPLETE                             ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo ""

# Final stats
log "Final SAMPLE_MASTER usage:"
df -h /Volumes/SAMPLE_MASTER

echo ""
success "🔥 HEAL & UPDATE COMPLETE! 🔥"
