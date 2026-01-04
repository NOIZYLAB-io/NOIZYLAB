#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# TERMINAL KILLER - FORCE KILL HANGING PROCESSES & CLEANUP
# GABRIEL ALMEIDA - MC96ECOUNIVERSE
# USE WHEN TERMINAL IS FROZEN OR HANGING
# ═══════════════════════════════════════════════════════════════════════════════

set +e  # Don't exit on error

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m'

banner() {
    echo -e "${RED}"
    echo "╔═══════════════════════════════════════════════════════════════════════════════╗"
    echo "║                          🔥 TERMINAL KILLER 🔥                                ║"
    echo "║                       FORCE KILL HANGING PROCESSES                            ║"
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
        KILL)  echo -e "${RED}[💀]${NC} $msg" ;;
    esac
}

banner

# ═══════════════════════════════════════════════════════════════════════════════
# KILL HANGING DISK OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════════

log INFO "Searching for hanging disk operations..."

# Kill du (disk usage) commands
DU_PROCS=$(ps aux | grep -E "du -sh|du -h" | grep -v grep | awk '{print $2}')
if [ ! -z "$DU_PROCS" ]; then
    for pid in $DU_PROCS; do
        log KILL "Killing du process: $pid"
        kill -9 $pid 2>/dev/null || true
    done
    log OK "Killed du processes"
else
    log INFO "No du processes found"
fi

# Kill find commands
FIND_PROCS=$(ps aux | grep "find /Volumes" | grep -v grep | awk '{print $2}')
if [ ! -z "$FIND_PROCS" ]; then
    for pid in $FIND_PROCS; do
        log KILL "Killing find process: $pid"
        kill -9 $pid 2>/dev/null || true
    done
    log OK "Killed find processes"
else
    log INFO "No find processes found"
fi

# Kill ls commands on slow volumes
LS_PROCS=$(ps aux | grep "ls /Volumes" | grep -v grep | awk '{print $2}')
if [ ! -z "$LS_PROCS" ]; then
    for pid in $LS_PROCS; do
        log KILL "Killing ls process: $pid"
        kill -9 $pid 2>/dev/null || true
    done
    log OK "Killed ls processes"
else
    log INFO "No ls processes found"
fi

# Kill df commands
DF_PROCS=$(ps aux | grep "df -h" | grep -v grep | awk '{print $2}')
if [ ! -z "$DF_PROCS" ]; then
    for pid in $DF_PROCS; do
        log KILL "Killing df process: $pid"
        kill -9 $pid 2>/dev/null || true
    done
    log OK "Killed df processes"
else
    log INFO "No df processes found"
fi

# ═══════════════════════════════════════════════════════════════════════════════
# KILL RSYNC & COPY OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════════

log INFO "Checking for rsync/copy operations..."

RSYNC_PROCS=$(ps aux | grep rsync | grep -v grep | awk '{print $2}')
if [ ! -z "$RSYNC_PROCS" ]; then
    for pid in $RSYNC_PROCS; do
        log KILL "Killing rsync process: $pid"
        kill -9 $pid 2>/dev/null || true
    done
    log OK "Killed rsync processes"
else
    log INFO "No rsync processes found"
fi

CP_PROCS=$(ps aux | grep "cp -r" | grep -v grep | awk '{print $2}')
if [ ! -z "$CP_PROCS" ]; then
    for pid in $CP_PROCS; do
        log KILL "Killing cp process: $pid"
        kill -9 $pid 2>/dev/null || true
    done
    log OK "Killed cp processes"
else
    log INFO "No cp processes found"
fi

# ═══════════════════════════════════════════════════════════════════════════════
# KILL SPOTLIGHT INDEXING (IF SLOWING DOWN DISK)
# ═══════════════════════════════════════════════════════════════════════════════

log INFO "Checking for Spotlight indexing..."

MDWORKER_PROCS=$(ps aux | grep mdworker | grep -v grep | awk '{print $2}')
if [ ! -z "$MDWORKER_PROCS" ]; then
    log WARN "Found Spotlight indexing processes (may be slowing disk)"
    read -p "Kill Spotlight indexing? (y/n): " confirm
    if [ "$confirm" = "y" ]; then
        for pid in $MDWORKER_PROCS; do
            log KILL "Killing mdworker process: $pid"
            kill -9 $pid 2>/dev/null || true
        done
        log OK "Killed Spotlight processes (they will restart)"
    fi
else
    log INFO "No Spotlight processes found"
fi

# ═══════════════════════════════════════════════════════════════════════════════
# CHECK FOR UNRESPONSIVE NETWORK MOUNTS
# ═══════════════════════════════════════════════════════════════════════════════

log INFO "Checking for unresponsive network mounts..."

mount | grep "on /Volumes" | grep -E "afp|smb|nfs" | while read line; do
    volume=$(echo "$line" | awk '{print $3}')
    log INFO "Testing: $volume"
    
    timeout 2 ls "$volume" >/dev/null 2>&1
    if [ $? -ne 0 ]; then
        log WARN "Unresponsive: $volume"
        echo "  Consider unmounting with: sudo umount -f \"$volume\""
    else
        log OK "Responsive: $volume"
    fi
done

# ═══════════════════════════════════════════════════════════════════════════════
# SHOW REMAINING DISK-RELATED PROCESSES
# ═══════════════════════════════════════════════════════════════════════════════

echo ""
log INFO "Remaining disk-related processes:"
echo ""
ps aux | grep -E "du|find|ls|df|rsync|cp" | grep -v grep | grep -v "TERMINAL_KILLER" || log OK "None found"

# ═══════════════════════════════════════════════════════════════════════════════
# CLEANUP & EXIT
# ═══════════════════════════════════════════════════════════════════════════════

echo ""
log OK "Terminal cleanup complete!"
echo ""
log INFO "Tips:"
echo "  • Use Ctrl+C to stop hanging commands in future"
echo "  • Add 'timeout 30' before slow commands"
echo "  • Use '2>/dev/null' to suppress errors on network drives"
echo ""

# Show which volumes are currently accessible
log INFO "Quick volume check:"
timeout 3 ls /Volumes/ 2>/dev/null | while read vol; do
    if timeout 1 ls "/Volumes/$vol" >/dev/null 2>&1; then
        echo -e "  ${GREEN}✓${NC} $vol"
    else
        echo -e "  ${RED}✗${NC} $vol (slow/unresponsive)"
    fi
done

echo ""
log OK "Ready to continue!"
