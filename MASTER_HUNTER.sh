#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# MASTER HUNTER - Run all cleanup and hunt scripts
# GABRIEL ALMEIDA - MC96ECOUNIVERSE
# ═══════════════════════════════════════════════════════════════════════════════

set +e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m'

banner() {
    echo -e "${PURPLE}"
    echo "╔═══════════════════════════════════════════════════════════════════════════════╗"
    echo "║                          🎯 MASTER HUNTER 🎯                                  ║"
    echo "║                    COMPREHENSIVE CLEANUP & HARVEST                            ║"
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
        STEP)  echo -e "${PURPLE}[>>]${NC} $msg" ;;
    esac
}

run_script() {
    local script="$1"
    local name="$2"
    
    if [ ! -f "$script" ]; then
        log ERROR "Script not found: $script"
        return 1
    fi
    
    echo ""
    log STEP "Running: $name"
    echo ""
    
    chmod +x "$script"
    bash "$script"
    
    local exit_code=$?
    if [ $exit_code -eq 0 ]; then
        log OK "Completed: $name"
    else
        log WARN "Finished with warnings: $name (exit code: $exit_code)"
    fi
}

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

banner

cd ~/NOIZYLAB || exit 1

log INFO "Starting comprehensive hunt and cleanup..."
log INFO "Working directory: $(pwd)"
echo ""

# Interactive menu
while true; do
    echo ""
    echo -e "${CYAN}┌─────────────────────────────────────────────────────────────┐${NC}"
    echo -e "${CYAN}│  MASTER HUNTER - SELECT OPERATION                           │${NC}"
    echo -e "${CYAN}├─────────────────────────────────────────────────────────────┤${NC}"
    echo -e "${CYAN}│${NC}  1) 🔥 Kill Hanging Processes (TERMINAL_KILLER)           ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  2) 🔍 Hunt Empty Folders (All Volumes)                   ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  3) 📦 Hunt NOIZYLAB Archives (Find Duplicates)           ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  4) ⚡ Run ALL Hunts (Full Sweep)                         ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  5) 📊 Storage Status (Quick Check)                       ${CYAN}│${NC}"
    echo -e "${CYAN}│${NC}  0) Exit                                                  ${CYAN}│${NC}"
    echo -e "${CYAN}└─────────────────────────────────────────────────────────────┘${NC}"
    echo ""
    
    read -p "Select option: " choice
    
    case $choice in
        1)
            run_script "./TERMINAL_KILLER.sh" "Terminal Killer"
            ;;
        2)
            run_script "./HUNT_EMPTY_FOLDERS.sh" "Hunt Empty Folders"
            ;;
        3)
            run_script "./HUNT_ARCHIVES.sh" "Hunt Archives"
            ;;
        4)
            log INFO "Running FULL SWEEP..."
            run_script "./TERMINAL_KILLER.sh" "Terminal Killer"
            run_script "./HUNT_ARCHIVES.sh" "Hunt Archives"
            run_script "./HUNT_EMPTY_FOLDERS.sh" "Hunt Empty Folders"
            log OK "Full sweep complete!"
            ;;
        5)
            log INFO "Storage Status:"
            echo ""
            timeout 5 df -h 2>/dev/null | grep -E "Filesystem|/Volumes" | head -15 || log WARN "Timeout - drives slow"
            ;;
        0)
            log OK "Exiting Master Hunter"
            break
            ;;
        *)
            log ERROR "Invalid option"
            ;;
    esac
done

echo ""
log OK "Master Hunter complete!"
