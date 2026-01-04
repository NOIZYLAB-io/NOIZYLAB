#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# HUNT EMPTY FOLDERS - Find and delete empty directories across ALL volumes
# GABRIEL ALMEIDA - MC96ECOUNIVERSE
# USES TIMEOUTS TO PREVENT HANGING
# ═══════════════════════════════════════════════════════════════════════════════

set +e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m'

EMPTY_FOUND=()
TOTAL_EMPTY=0

banner() {
    echo -e "${PURPLE}"
    echo "╔═══════════════════════════════════════════════════════════════════════════════╗"
    echo "║                       🔍 HUNT EMPTY FOLDERS 🔍                                ║"
    echo "║                  FIND & DESTROY ACROSS ALL VOLUMES                            ║"
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
        FOUND) echo -e "${RED}[📁]${NC} $msg" ;;
        KILL)  echo -e "${RED}[💀]${NC} $msg" ;;
    esac
}

hunt_volume() {
    local volume="$1"
    local max_depth="${2:-3}"
    
    if [ ! -d "$volume" ]; then
        log WARN "Not found: $volume"
        return
    fi
    
    log INFO "Hunting: $volume (depth $max_depth)"
    
    # Use timeout to prevent hanging
    local empty_dirs=$(timeout 30 find "$volume" -maxdepth $max_depth -type d -empty 2>/dev/null)
    
    if [ $? -eq 124 ]; then
        log ERROR "Timeout on: $volume (drive too slow/unresponsive)"
        return
    fi
    
    if [ -z "$empty_dirs" ]; then
        log OK "No empty folders found"
        return
    fi
    
    local count=0
    while IFS= read -r dir; do
        if [ ! -z "$dir" ]; then
            log FOUND "$dir"
            EMPTY_FOUND+=("$dir")
            ((count++))
            ((TOTAL_EMPTY++))
        fi
    done <<< "$empty_dirs"
    
    if [ $count -gt 0 ]; then
        log WARN "Found $count empty folders on $volume"
    fi
}

delete_empty() {
    if [ ${#EMPTY_FOUND[@]} -eq 0 ]; then
        log OK "No empty folders to delete!"
        return
    fi
    
    echo ""
    log WARN "Found $TOTAL_EMPTY empty folders total"
    echo ""
    
    read -p "Delete all empty folders? (y/n): " confirm
    if [ "$confirm" != "y" ]; then
        log INFO "Skipped deletion"
        return
    fi
    
    echo ""
    log INFO "Deleting empty folders..."
    
    local deleted=0
    local failed=0
    
    for dir in "${EMPTY_FOUND[@]}"; do
        if [ -d "$dir" ]; then
            if rmdir "$dir" 2>/dev/null; then
                log KILL "Deleted: $dir"
                ((deleted++))
            else
                log ERROR "Failed: $dir"
                ((failed++))
            fi
        fi
    done
    
    echo ""
    log OK "Deleted: $deleted folders"
    if [ $failed -gt 0 ]; then
        log WARN "Failed: $failed folders (may contain hidden files)"
    fi
}

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN HUNT
# ═══════════════════════════════════════════════════════════════════════════════

banner

# All known volumes (from inventory)
VOLUMES=(
    "/Volumes/12TB"
    "/Volumes/RED DRAGON"
    "/Volumes/4TB Lacie"
    "/Volumes/4TBSG"
    "/Volumes/JOE"
    "/Volumes/SOUND_DESIGN"
    "/Volumes/SAMPLE_MASTER"
    "/Volumes/6TB"
    "/Volumes/MAG 4TB"
    "/Volumes/EW"
    "/Volumes/4TB FISH SG"
    "/Volumes/4TB Blue Fish"
)

# Hunt each volume
for vol in "${VOLUMES[@]}"; do
    hunt_volume "$vol" 3
    echo ""
done

# Summary and delete
echo ""
log INFO "═══════════════════════════════════════════════════════════════"
log INFO "HUNT COMPLETE"
log INFO "═══════════════════════════════════════════════════════════════"
delete_empty

echo ""
log OK "Hunt complete! All volumes scanned."
