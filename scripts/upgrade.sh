#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════════
# 🚀 NOIZYLAB SUPER UPGRADE & IMPROVE
# ═══════════════════════════════════════════════════════════════════════════════
# The ultimate macOS optimization script for M2 Ultra
# 
# Features:
#   • Homebrew update & cleanup
#   • Python packages upgrade
#   • Node.js packages upgrade  
#   • System caches cleanup
#   • DNS flush
#   • LaunchServices rebuild
#   • Spotlight optimization
#   • Memory purge
#   • Developer tools check
#   • NOIZYLAB environment setup
#
# Usage: bash upgrade.sh [--full | --quick | --dev | --clean]
# ═══════════════════════════════════════════════════════════════════════════════

set -euo pipefail

# Colors
RED='\033[0;91m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
BLUE='\033[0;94m'
MAGENTA='\033[0;95m'
CYAN='\033[0;96m'
RESET='\033[0m'
BOLD='\033[1m'

# Config
TS="$(date +%Y%m%d-%H%M%S)"
LOGDIR="$HOME/.noizylab/logs"
mkdir -p "$LOGDIR"
LOGFILE="$LOGDIR/upgrade-$TS.log"
MODE="${1:-full}"

# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

banner() {
    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════════════╗"
    echo "║  🚀 NOIZYLAB SUPER UPGRADE & IMPROVE                                 ║"
    echo "║  Mode: $MODE | $(date)                          ║"
    echo "╚══════════════════════════════════════════════════════════════════════╝"
    echo -e "${RESET}"
}

log() { 
    echo -e "${GREEN}[✓]${RESET} $1" | tee -a "$LOGFILE"
}

warn() {
    echo -e "${YELLOW}[!]${RESET} $1" | tee -a "$LOGFILE"
}

error() {
    echo -e "${RED}[✗]${RESET} $1" | tee -a "$LOGFILE"
}

section() {
    echo "" | tee -a "$LOGFILE"
    echo -e "${MAGENTA}━━━ $1 ━━━${RESET}" | tee -a "$LOGFILE"
}

spin() {
    local pid=$1
    local msg=$2
    local spinstr='⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
    while [ -d /proc/$pid ] 2>/dev/null || kill -0 $pid 2>/dev/null; do
        for i in $(seq 0 9); do
            printf "\r${CYAN}[${spinstr:$i:1}]${RESET} $msg"
            sleep 0.1
        done
    done
    printf "\r"
}

# ═══════════════════════════════════════════════════════════════════════════════
# SYSTEM INFO
# ═══════════════════════════════════════════════════════════════════════════════

show_system_info() {
    section "SYSTEM INFO"
    
    echo -e "  ${CYAN}Machine:${RESET}  $(scutil --get ComputerName 2>/dev/null || hostname)"
    echo -e "  ${CYAN}macOS:${RESET}    $(sw_vers -productVersion) ($(sw_vers -buildVersion))"
    echo -e "  ${CYAN}Chip:${RESET}     $(sysctl -n machdep.cpu.brand_string 2>/dev/null || echo 'Apple Silicon')"
    echo -e "  ${CYAN}Memory:${RESET}   $(( $(sysctl -n hw.memsize) / 1073741824 )) GB"
    echo -e "  ${CYAN}Disk:${RESET}     $(df -h / | awk 'NR==2 {print $4 " available of " $2}')"
    
    # Uptime
    local uptime_secs=$(sysctl -n kern.boottime | awk '{print $4}' | tr -d ',')
    local now=$(date +%s)
    local uptime_days=$(( (now - uptime_secs) / 86400 ))
    echo -e "  ${CYAN}Uptime:${RESET}   $uptime_days days"
}

# ═══════════════════════════════════════════════════════════════════════════════
# HOMEBREW
# ═══════════════════════════════════════════════════════════════════════════════

upgrade_homebrew() {
    section "HOMEBREW"
    
    if ! command -v brew &>/dev/null; then
        warn "Homebrew not installed. Installing..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    
    log "Updating Homebrew..."
    brew update 2>&1 | tee -a "$LOGFILE" || true
    
    log "Upgrading packages..."
    brew upgrade 2>&1 | tee -a "$LOGFILE" || true
    
    log "Upgrading casks..."
    brew upgrade --cask 2>&1 | tee -a "$LOGFILE" || true
    
    log "Cleaning up..."
    brew cleanup -s 2>&1 | tee -a "$LOGFILE" || true
    brew autoremove 2>&1 | tee -a "$LOGFILE" || true
    
    # Check for issues
    brew doctor 2>&1 | head -5 | tee -a "$LOGFILE" || true
    
    log "Homebrew done! $(brew list | wc -l | tr -d ' ') packages installed"
}

# ═══════════════════════════════════════════════════════════════════════════════
# PYTHON
# ═══════════════════════════════════════════════════════════════════════════════

upgrade_python() {
    section "PYTHON"
    
    if ! command -v python3 &>/dev/null; then
        warn "Python3 not found"
        return
    fi
    
    log "Python: $(python3 --version)"
    
    log "Upgrading pip..."
    python3 -m pip install --upgrade pip 2>&1 | tail -1 | tee -a "$LOGFILE" || true
    
    log "Upgrading core packages..."
    python3 -m pip install --upgrade setuptools wheel 2>&1 | tail -1 | tee -a "$LOGFILE" || true
    
    # Upgrade all outdated packages
    log "Checking for outdated packages..."
    outdated=$(python3 -m pip list --outdated --format=json 2>/dev/null | python3 -c "import sys,json; print(' '.join([p['name'] for p in json.load(sys.stdin)]))" 2>/dev/null || echo "")
    
    if [ -n "$outdated" ]; then
        log "Upgrading: $outdated"
        python3 -m pip install --upgrade $outdated 2>&1 | tail -3 | tee -a "$LOGFILE" || true
    else
        log "All Python packages up to date!"
    fi
    
    # NOIZYLAB essentials
    log "Ensuring NOIZYLAB Python deps..."
    python3 -m pip install --quiet edge-tts gtts pydub openai google-generativeai requests aiohttp flask flask-cors 2>&1 || true
    
    log "Python done!"
}

# ═══════════════════════════════════════════════════════════════════════════════
# NODE.JS
# ═══════════════════════════════════════════════════════════════════════════════

upgrade_node() {
    section "NODE.JS"
    
    if ! command -v node &>/dev/null; then
        warn "Node.js not found"
        return
    fi
    
    log "Node: $(node --version) | npm: $(npm --version)"
    
    log "Updating npm..."
    npm install -g npm@latest 2>&1 | tail -1 | tee -a "$LOGFILE" || true
    
    log "Updating global packages..."
    npm update -g 2>&1 | tail -3 | tee -a "$LOGFILE" || true
    
    # Clean npm cache
    npm cache clean --force 2>&1 | tee -a "$LOGFILE" || true
    
    log "Node.js done!"
}

# ═══════════════════════════════════════════════════════════════════════════════
# RUST
# ═══════════════════════════════════════════════════════════════════════════════

upgrade_rust() {
    section "RUST"
    
    if ! command -v rustup &>/dev/null; then
        warn "Rust not installed"
        return
    fi
    
    log "Updating Rust..."
    rustup update 2>&1 | tail -3 | tee -a "$LOGFILE" || true
    
    log "Rust: $(rustc --version)"
}

# ═══════════════════════════════════════════════════════════════════════════════
# SYSTEM CLEANUP
# ═══════════════════════════════════════════════════════════════════════════════

cleanup_system() {
    section "SYSTEM CLEANUP"
    
    # DNS flush
    log "Flushing DNS cache..."
    sudo dscacheutil -flushcache 2>/dev/null || true
    sudo killall -HUP mDNSResponder 2>/dev/null || true
    
    # QuickLook cache
    log "Clearing QuickLook cache..."
    qlmanage -r cache 2>/dev/null || true
    
    # Font cache
    log "Clearing font cache..."
    sudo atsutil databases -remove 2>/dev/null || true
    
    # System caches (safe ones)
    log "Clearing user caches..."
    rm -rf ~/Library/Caches/com.apple.Safari/Cache.db 2>/dev/null || true
    rm -rf ~/Library/Caches/Google/Chrome/Default/Cache/* 2>/dev/null || true
    rm -rf ~/Library/Caches/com.spotify.client/Data/* 2>/dev/null || true
    
    # Developer caches
    log "Clearing developer caches..."
    rm -rf ~/Library/Developer/Xcode/DerivedData/* 2>/dev/null || true
    rm -rf ~/Library/Developer/Xcode/Archives/* 2>/dev/null || true
    rm -rf ~/Library/Caches/com.apple.dt.Xcode/* 2>/dev/null || true
    
    # npm/pip caches
    rm -rf ~/.npm/_cacache/* 2>/dev/null || true
    rm -rf ~/Library/Caches/pip/* 2>/dev/null || true
    
    log "Cleanup done!"
}

# ═══════════════════════════════════════════════════════════════════════════════
# SYSTEM OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════════════

optimize_system() {
    section "SYSTEM OPTIMIZATION"
    
    # Memory purge
    log "Purging inactive memory..."
    sudo purge 2>/dev/null || true
    
    # LaunchServices rebuild
    log "Rebuilding LaunchServices..."
    /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister \
        -kill -r -domain local -domain system -domain user 2>/dev/null || true
    
    # Spotlight optimization
    log "Optimizing Spotlight..."
    sudo mdutil -i on / 2>/dev/null || true
    
    # Disable on external volumes
    for vol in /Volumes/*; do
        if [ "$vol" != "/Volumes/Macintosh HD" ] && [ -d "$vol" ]; then
            sudo mdutil -i off "$vol" 2>/dev/null || true
        fi
    done
    
    # Time Machine local snapshots cleanup
    log "Cleaning Time Machine local snapshots..."
    tmutil listlocalsnapshots / 2>/dev/null | grep -v "Snapshots" | while read snap; do
        sudo tmutil deletelocalsnapshots "${snap#com.apple.TimeMachine.}" 2>/dev/null || true
    done
    
    log "Optimization done!"
}

# ═══════════════════════════════════════════════════════════════════════════════
# DEV TOOLS CHECK
# ═══════════════════════════════════════════════════════════════════════════════

check_dev_tools() {
    section "DEVELOPER TOOLS"
    
    local tools=(
        "git:Git"
        "python3:Python"
        "node:Node.js"
        "npm:npm"
        "rustc:Rust"
        "go:Go"
        "docker:Docker"
        "code:VS Code"
        "az:Azure CLI"
        "gh:GitHub CLI"
        "wrangler:Cloudflare Wrangler"
    )
    
    for tool in "${tools[@]}"; do
        local cmd="${tool%%:*}"
        local name="${tool##*:}"
        if command -v "$cmd" &>/dev/null; then
            local ver=$("$cmd" --version 2>/dev/null | head -1 | cut -d' ' -f1-3 || echo "installed")
            echo -e "  ${GREEN}✓${RESET} $name: $ver"
        else
            echo -e "  ${RED}✗${RESET} $name: not installed"
        fi
    done
}

# ═══════════════════════════════════════════════════════════════════════════════
# NOIZYLAB SETUP
# ═══════════════════════════════════════════════════════════════════════════════

setup_noizylab() {
    section "NOIZYLAB ENVIRONMENT"
    
    # Create directories
    mkdir -p ~/.noizylab/{logs,cleanspace/diagnostics,cache}
    mkdir -p ~/NOIZYLAB/{GABRIEL,MC96,PROJECTS}
    
    log "NOIZYLAB directories ready"
    
    # Check CLEANSPACE
    if [ -f ~/NOIZYLAB/scripts/cleanspace.py ]; then
        log "CLEANSPACE: ✓ installed"
    else
        warn "CLEANSPACE: not found"
    fi
    
    # Check MC96
    if [ -f ~/NOIZYLAB/GABRIEL/mc96_terminal.py ]; then
        log "MC96 Terminal: ✓ installed"
    else
        warn "MC96 Terminal: not found"
    fi
    
    # Check TitanHive
    if [ -f ~/NOIZYLAB/GABRIEL/titanhive/voice.py ]; then
        log "TitanHive Voice: ✓ installed"
    else
        warn "TitanHive Voice: not found"
    fi
}

# ═══════════════════════════════════════════════════════════════════════════════
# DISK SPACE REPORT
# ═══════════════════════════════════════════════════════════════════════════════

disk_report() {
    section "DISK SPACE"
    
    echo -e "  ${CYAN}Root (/)${RESET}"
    df -h / | awk 'NR==2 {printf "    Used: %s / %s (%s)\n    Free: %s\n", $3, $2, $5, $4}'
    
    echo ""
    echo -e "  ${CYAN}Largest directories in ~/${RESET}"
    du -sh ~/Library ~/Documents ~/Downloads ~/Desktop ~/NOIZYLAB 2>/dev/null | sort -rh | head -5 | while read size dir; do
        echo "    $size  $(basename "$dir")"
    done
}

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

main() {
    banner
    show_system_info
    
    case "$MODE" in
        --quick|-q)
            upgrade_homebrew
            cleanup_system
            ;;
        --dev|-d)
            upgrade_homebrew
            upgrade_python
            upgrade_node
            upgrade_rust
            check_dev_tools
            ;;
        --clean|-c)
            cleanup_system
            optimize_system
            disk_report
            ;;
        --full|-f|*)
            upgrade_homebrew
            upgrade_python
            upgrade_node
            upgrade_rust
            cleanup_system
            optimize_system
            check_dev_tools
            setup_noizylab
            disk_report
            ;;
    esac
    
    echo ""
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════════════════╗${RESET}"
    echo -e "${GREEN}║  ✅ UPGRADE & IMPROVE COMPLETE!                                      ║${RESET}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -e "  Log saved to: ${CYAN}$LOGFILE${RESET}"
    echo ""
    echo -e "  ${YELLOW}Recommended:${RESET} Restart your Mac for full effect"
    echo ""
}

# Run with sudo check for system operations
if [ "$MODE" != "--help" ] && [ "$MODE" != "-h" ]; then
    # Request sudo upfront
    sudo -v 2>/dev/null || true
    # Keep sudo alive
    while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &
fi

main "$@"
