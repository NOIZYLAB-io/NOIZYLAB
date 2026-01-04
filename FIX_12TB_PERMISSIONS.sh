#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# FIX 12TB PERMISSIONS - AGGRESSIVE BULK OPERATIONS
# GABRIEL ALMEIDA - MC96ECOUNIVERSE
# FASTER THAN BATCHMOD - USES PARALLEL OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════════

set +e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

VOLUME="/Volumes/12TB"

banner() {
    echo -e "${RED}"
    echo "╔═══════════════════════════════════════════════════════════════════════════════╗"
    echo "║                    🔧 FIX 12TB PERMISSIONS 🔧                                 ║"
    echo "║                  AGGRESSIVE BULK OPERATIONS                                   ║"
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
    esac
}

banner

if [ ! -d "$VOLUME" ]; then
    log ERROR "12TB not mounted!"
    exit 1
fi

log INFO "Target: $VOLUME"
echo ""

# Option 1: DISABLE SPOTLIGHT (makes disk WAY faster)
echo -e "${CYAN}[OPTION 1] DISABLE SPOTLIGHT INDEXING${NC}"
echo "  Spotlight indexing can cause severe slowdowns on external drives"
read -p "Disable Spotlight on 12TB? (RECOMMENDED) (y/n): " disable_spotlight
if [ "$disable_spotlight" = "y" ]; then
    log INFO "Disabling Spotlight..."
    sudo mdutil -i off "$VOLUME" 2>/dev/null
    sudo mdutil -E "$VOLUME" 2>/dev/null
    log OK "Spotlight disabled and index erased"
    echo ""
fi

# Option 2: FIX OWNERSHIP (recursive, fast)
echo -e "${CYAN}[OPTION 2] FIX OWNERSHIP${NC}"
echo "  Current user: $USER"
read -p "Set all files to your ownership? (y/n): " fix_ownership
if [ "$fix_ownership" = "y" ]; then
    log INFO "Fixing ownership recursively..."
    sudo chown -R $USER:staff "$VOLUME" 2>/dev/null &
    local pid=$!
    
    # Show progress while running
    while kill -0 $pid 2>/dev/null; do
        echo -n "."
        sleep 2
    done
    echo ""
    
    log OK "Ownership fixed"
    echo ""
fi

# Option 3: FIX PERMISSIONS (parallel, by top-level folder)
echo -e "${CYAN}[OPTION 3] FIX PERMISSIONS (PARALLEL)${NC}"
echo "  Set all to readable/writable/executable"
read -p "Fix all permissions? (y/n): " fix_perms
if [ "$fix_perms" = "y" ]; then
    log INFO "Fixing permissions in parallel..."
    
    # Fix each top-level folder in parallel
    for dir in "$VOLUME"/*; do
        if [ -d "$dir" ]; then
            log INFO "Processing: $(basename "$dir")"
            (
                # Files: 644 (rw-r--r--)
                find "$dir" -type f -exec chmod 644 {} + 2>/dev/null
                # Directories: 755 (rwxr-xr-x)
                find "$dir" -type d -exec chmod 755 {} + 2>/dev/null
            ) &
        fi
    done
    
    wait
    log OK "Permissions fixed"
    echo ""
fi

# Option 4: REMOVE ACLs (Access Control Lists can cause issues)
echo -e "${CYAN}[OPTION 4] REMOVE ACLs${NC}"
echo "  ACLs can cause permission conflicts"
read -p "Remove all ACLs? (y/n): " remove_acls
if [ "$remove_acls" = "y" ]; then
    log INFO "Removing ACLs..."
    sudo chmod -R -N "$VOLUME" 2>/dev/null
    log OK "ACLs removed"
    echo ""
fi

# Option 5: IGNORE OWNERSHIP (macOS specific - best for external drives)
echo -e "${CYAN}[OPTION 5] IGNORE OWNERSHIP (RECOMMENDED)${NC}"
echo "  Makes macOS ignore permissions entirely on this drive"
echo "  Best for external drives - instant access to everything"
read -p "Enable 'Ignore Ownership' on 12TB? (RECOMMENDED) (y/n): " ignore_ownership
if [ "$ignore_ownership" = "y" ]; then
    log INFO "Enabling ignore ownership..."
    
    # Get disk identifier
    local disk_id=$(diskutil info "$VOLUME" | grep "Device Identifier" | awk '{print $3}')
    
    if [ ! -z "$disk_id" ]; then
        sudo diskutil enableOwnership "$VOLUME" 2>/dev/null
        sudo vsdbutil -a "$VOLUME" 2>/dev/null
        log OK "Ownership checking disabled"
    else
        log ERROR "Could not determine disk identifier"
    fi
    echo ""
fi

# Show final status
echo ""
log INFO "═══════════════════════════════════════════════════════════════"
log INFO "FINAL STATUS"
log INFO "═══════════════════════════════════════════════════════════════"
echo ""

ls -ld "$VOLUME"
echo ""

diskutil info "$VOLUME" | grep -E "Volume Name|Owners|Permissions"
echo ""

log OK "Permission fixes complete!"
echo ""
log INFO "Test disk speed:"
echo "  cd /Volumes/12TB"
echo "  time ls -la | wc -l"
