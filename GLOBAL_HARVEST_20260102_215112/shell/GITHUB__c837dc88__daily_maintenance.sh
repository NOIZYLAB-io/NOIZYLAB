#!/bin/bash
###############################################################################
#  NOIZYLAB DAILY MAINTENANCE
#  Automated system cleanup and optimization
###############################################################################

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="/tmp/noizylab-maintenance"
LOG_FILE="$LOG_DIR/maintenance_$(date +%Y%m%d).log"

mkdir -p "$LOG_DIR"

log() {
    echo "[$(date '+%H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo -e "${GREEN}NOIZYLAB DAILY MAINTENANCE${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo ""

# --- 1. CLEAN CACHES ---
clean_caches() {
    log "Cleaning system caches..."

    # Python cache
    find "$HOME/NOIZYLAB" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find "$HOME/NOIZYLAB" -name "*.pyc" -delete 2>/dev/null || true

    # Node cache
    find "$HOME/NOIZYLAB" -name ".cache" -type d -exec rm -rf {} + 2>/dev/null || true

    # npm cache (selective)
    npm cache clean --force 2>/dev/null || true

    # Homebrew cache
    brew cleanup --prune=7 2>/dev/null || true

    echo -e "${GREEN}[OK] Caches cleaned${NC}"
}

# --- 2. CLEAN LOGS ---
clean_logs() {
    log "Cleaning old logs..."

    # NOIZYLAB logs older than 7 days
    find "$HOME/NOIZYLAB" -name "*.log" -type f -mtime +7 -delete 2>/dev/null || true

    # Maintenance logs older than 30 days
    find "$LOG_DIR" -name "*.log" -type f -mtime +30 -delete 2>/dev/null || true

    # Health check logs
    find /tmp/noizylab-health -name "*.log" -type f -mtime +7 -delete 2>/dev/null || true

    echo -e "${GREEN}[OK] Old logs cleaned${NC}"
}

# --- 3. CLEAN TEMP FILES ---
clean_temp() {
    log "Cleaning temporary files..."

    # DS_Store files
    find "$HOME/NOIZYLAB" -name ".DS_Store" -delete 2>/dev/null || true

    # Backup files
    find "$HOME/NOIZYLAB" -name "*.bak" -type f -mtime +30 -delete 2>/dev/null || true
    find "$HOME/NOIZYLAB" -name "*~" -type f -delete 2>/dev/null || true

    # Empty directories
    find "$HOME/NOIZYLAB" -type d -empty -delete 2>/dev/null || true

    echo -e "${GREEN}[OK] Temp files cleaned${NC}"
}

# --- 4. GIT MAINTENANCE ---
git_maintenance() {
    log "Running git maintenance..."

    cd "$HOME/NOIZYLAB/GABRIEL"
    if [ -d ".git" ]; then
        # Prune remote branches
        git remote prune origin 2>/dev/null || true

        # Garbage collection
        git gc --auto 2>/dev/null || true

        # Show status
        UNCOMMITTED=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
        if [ "$UNCOMMITTED" -gt 0 ]; then
            echo -e "${YELLOW}[!!] $UNCOMMITTED uncommitted changes${NC}"
        fi
    fi

    echo -e "${GREEN}[OK] Git maintenance done${NC}"
}

# --- 5. CHECK DISK SPACE ---
check_disk() {
    log "Checking disk space..."

    DISK_USED=$(df -h / | awk 'NR==2 {gsub(/%/,"",$5); print $5}')
    if [ "$DISK_USED" -gt 90 ]; then
        echo -e "${RED}[!!] Disk usage critical: ${DISK_USED}%${NC}"
    elif [ "$DISK_USED" -gt 80 ]; then
        echo -e "${YELLOW}[!!] Disk usage high: ${DISK_USED}%${NC}"
    else
        echo -e "${GREEN}[OK] Disk usage: ${DISK_USED}%${NC}"
    fi
}

# --- 6. UPDATE HOMEBREW ---
update_homebrew() {
    log "Updating Homebrew..."

    if command -v brew &>/dev/null; then
        brew update 2>/dev/null || true
        OUTDATED=$(brew outdated --quiet | wc -l | tr -d ' ')
        if [ "$OUTDATED" -gt 0 ]; then
            echo -e "${YELLOW}[!!] $OUTDATED outdated packages${NC}"
        else
            echo -e "${GREEN}[OK] All packages up to date${NC}"
        fi
    fi
}

# --- 7. VERIFY CRITICAL FILES ---
verify_files() {
    log "Verifying critical files..."

    CRITICAL_FILES=(
        "$HOME/.env.secrets"
        "$HOME/.zshrc"
        "$HOME/CLAUDE.md"
        "$HOME/NOIZYLAB/GABRIEL/gorunfree"
        "$HOME/NOIZYLAB/GABRIEL/gabriel.py"
    )

    for file in "${CRITICAL_FILES[@]}"; do
        if [ -f "$file" ]; then
            echo -e "  [OK] $(basename "$file")"
        else
            echo -e "  ${RED}[!!] Missing: $file${NC}"
        fi
    done
}

# --- RUN ALL ---
clean_caches
clean_logs
clean_temp
git_maintenance
check_disk
update_homebrew
verify_files

# --- SUMMARY ---
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo -e "${GREEN}MAINTENANCE COMPLETE${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo ""
echo "Log: $LOG_FILE"
log "Maintenance completed"
