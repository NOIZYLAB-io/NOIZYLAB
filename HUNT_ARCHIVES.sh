#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# HUNT NOIZYLAB ARCHIVES - Find all NOIZYLAB_ARCHIVE folders and consolidate
# GABRIEL ALMEIDA - MC96ECOUNIVERSE
# ═══════════════════════════════════════════════════════════════════════════════

set +e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m'

ARCHIVES_FOUND=()

banner() {
    echo -e "${PURPLE}"
    echo "╔═══════════════════════════════════════════════════════════════════════════════╗"
    echo "║                   📦 HUNT NOIZYLAB ARCHIVES 📦                                ║"
    echo "║               FIND & CONSOLIDATE DUPLICATE ARCHIVES                           ║"
    echo "╚═══════════════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

log() {
    local level=$1
    local msg=$2
    case $level in
        OK)    echo -e "${GREEN}[✓]${NC} $msg" ;;
        WARN)  echo -e "${YELLOW}[!]${NC} $msg" ;;
        ERROR) echo -e "${RED}[✗]${NC} $msg" ;;
        INFO)  echo -e "${CYAN}[→]${NC} $msg" ;;
        FOUND) echo -e "${YELLOW}[📦]${NC} $msg" ;;
    esac
}

hunt_archives() {
    local volume="$1"
    
    if [ ! -d "$volume" ]; then
        return
    fi
    
    log INFO "Hunting archives on: $volume"
    
    # Search for NOIZYLAB_ARCHIVE* folders (timeout to prevent hanging)
    local archives=$(timeout 20 find "$volume" -maxdepth 2 -type d -name "*NOIZYLAB*ARCHIVE*" 2>/dev/null)
    
    if [ $? -eq 124 ]; then
        log ERROR "Timeout on: $volume"
        return
    fi
    
    if [ -z "$archives" ]; then
        log INFO "No archives found"
        return
    fi
    
    while IFS= read -r archive; do
        if [ ! -z "$archive" ]; then
            # Get size
            local size=$(timeout 5 du -sh "$archive" 2>/dev/null | awk '{print $1}')
            if [ -z "$size" ]; then
                size="unknown"
            fi
            
            log FOUND "$archive ($size)"
            ARCHIVES_FOUND+=("$archive|$size")
        fi
    done <<< "$archives"
}

show_summary() {
    echo ""
    log INFO "═══════════════════════════════════════════════════════════════"
    log INFO "ARCHIVE SUMMARY"
    log INFO "═══════════════════════════════════════════════════════════════"
    
    if [ ${#ARCHIVES_FOUND[@]} -eq 0 ]; then
        log OK "No duplicate archives found!"
        return
    fi
    
    echo ""
    local total_size=0
    for archive in "${ARCHIVES_FOUND[@]}"; do
        IFS='|' read -r path size <<< "$archive"
        echo -e "${CYAN}Location:${NC} $path"
        echo -e "${YELLOW}Size:${NC}     $size"
        echo ""
    done
    
    log WARN "Found ${#ARCHIVES_FOUND[@]} NOIZYLAB_ARCHIVE locations"
    echo ""
    
    if [ ${#ARCHIVES_FOUND[@]} -gt 1 ]; then
        log INFO "Consolidation recommendations:"
        echo "  1. Keep the LARGEST archive (most complete)"
        echo "  2. Compare contents before deleting"
        echo "  3. Use 'rsync -avh --dry-run' to check differences"
        echo "  4. Move smaller archives to single location"
        echo ""
        log WARN "Suggested target: RED DRAGON (3.3TB free)"
    fi
}

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN HUNT
# ═══════════════════════════════════════════════════════════════════════════════

banner

# All known volumes
VOLUMES=(
    "/Volumes/12TB"
    "/Volumes/RED DRAGON"
    "/Volumes/4TB Lacie"
    "/Volumes/4TBSG"
    "/Volumes/JOE"
    "/Volumes/6TB"
    "/Volumes/MAG 4TB"
    "/Volumes/EW"
)

# Hunt each volume
for vol in "${VOLUMES[@]}"; do
    hunt_archives "$vol"
done

# Show summary
show_summary

echo ""
log OK "Archive hunt complete!"
