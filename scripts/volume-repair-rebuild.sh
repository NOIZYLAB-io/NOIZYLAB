#!/bin/bash
#===============================================================================
# NOIZYLAB VOLUME REPAIR & REBUILD
# Complete volume restoration with all agents deployed
#===============================================================================

set -e

# Configuration
VOLUME="${1:-/Volumes/12TB}"
DEST_DIR="/Users/m2ultra/NOIZYLAB"
SCRIPTS_DIR="$(cd "$(dirname "$0")" && pwd)"
NOIZYLAB_DIR="$HOME/.noizylab"
LOG_DIR="$NOIZYLAB_DIR/logs"
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Counters
DIRS_FIXED=0
FILES_FIXED=0
ACLS_REMOVED=0
XATTRS_REMOVED=0
AGENTS_INSTALLED=0
ERRORS=0

#===============================================================================
# BANNER
#===============================================================================

print_banner() {
    echo -e "${RED}${BOLD}"
    cat << 'EOF'
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║    ██╗   ██╗ ██████╗ ██╗     ██╗   ██╗███╗   ███╗███████╗                     ║
║    ██║   ██║██╔═══██╗██║     ██║   ██║████╗ ████║██╔════╝                     ║
║    ██║   ██║██║   ██║██║     ██║   ██║██╔████╔██║█████╗                       ║
║    ╚██╗ ██╔╝██║   ██║██║     ██║   ██║██║╚██╔╝██║██╔══╝                       ║
║     ╚████╔╝ ╚██████╔╝███████╗╚██████╔╝██║ ╚═╝ ██║███████╗                     ║
║      ╚═══╝   ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝                     ║
║                                                                               ║
║              REPAIR & REBUILD WITH ALL AGENTS                                 ║
║     Permissions • ACLs • Attributes • Agents • Automation                     ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

print_phase() {
    local phase=$1
    local title=$2
    echo ""
    echo -e "${PURPLE}${BOLD}═══════════════════════════════════════════════════════════════════${NC}"
    echo -e "${PURPLE}${BOLD}  PHASE $phase: $title${NC}"
    echo -e "${PURPLE}${BOLD}═══════════════════════════════════════════════════════════════════${NC}"
    echo ""
}

log() { echo -e "${CYAN}[$(date +'%H:%M:%S')]${NC} $1"; }
log_success() { echo -e "${GREEN}[✓]${NC} $1"; }
log_warning() { echo -e "${YELLOW}[!]${NC} $1"; }
log_error() { echo -e "${RED}[✗]${NC} $1"; ((ERRORS++)); }

#===============================================================================
# PHASE 1: VALIDATION
#===============================================================================

phase_validate() {
    print_phase 1 "VALIDATION"

    # Check if running as root for full permissions
    if [ "$EUID" -ne 0 ]; then
        log_warning "Not running as root. Some operations may fail."
        log_warning "For full repair, run: sudo $0 $VOLUME"
    fi

    # Check volume
    if [ ! -d "$VOLUME" ]; then
        log_error "Volume not found: $VOLUME"
        echo ""
        echo -e "${YELLOW}Available volumes:${NC}"
        ls -la /Volumes/ 2>/dev/null || echo "  Cannot list /Volumes"
        exit 1
    fi
    log_success "Volume found: $VOLUME"

    # Get volume info
    local vol_size=$(df -h "$VOLUME" 2>/dev/null | tail -1 | awk '{print $2}')
    local vol_used=$(df -h "$VOLUME" 2>/dev/null | tail -1 | awk '{print $3}')
    local vol_free=$(df -h "$VOLUME" 2>/dev/null | tail -1 | awk '{print $4}')
    local vol_pct=$(df -h "$VOLUME" 2>/dev/null | tail -1 | awk '{print $5}')

    echo ""
    echo -e "${CYAN}Volume Information:${NC}"
    echo "  Size: $vol_size"
    echo "  Used: $vol_used ($vol_pct)"
    echo "  Free: $vol_free"

    # Get disk identifier
    if command -v diskutil &>/dev/null; then
        local disk_id=$(diskutil info "$VOLUME" 2>/dev/null | grep "Device Identifier" | awk '{print $NF}')
        local fs_type=$(diskutil info "$VOLUME" 2>/dev/null | grep "Type (Bundle)" | awk '{print $NF}')
        echo "  Disk: $disk_id"
        echo "  Filesystem: $fs_type"
    fi

    # Create directories
    mkdir -p "$NOIZYLAB_DIR"
    mkdir -p "$LOG_DIR"
    mkdir -p "$LAUNCH_AGENTS_DIR"
    mkdir -p "$DEST_DIR"

    log_success "Directories ready"
}

#===============================================================================
# PHASE 2: DISK REPAIR (macOS)
#===============================================================================

phase_disk_repair() {
    print_phase 2 "DISK VERIFICATION & REPAIR"

    if ! command -v diskutil &>/dev/null; then
        log_warning "diskutil not available (not macOS?), skipping disk repair"
        return
    fi

    local disk_id=$(diskutil info "$VOLUME" 2>/dev/null | grep "Device Identifier" | awk '{print $NF}')

    if [ -z "$disk_id" ]; then
        log_warning "Could not determine disk identifier"
        return
    fi

    log "Disk identifier: $disk_id"

    # Verify volume
    log "Verifying volume..."
    if diskutil verifyVolume "$VOLUME" 2>&1 | tee -a "$LOG_DIR/disk_repair_$TIMESTAMP.log"; then
        log_success "Volume verification complete"
    else
        log_warning "Volume verification reported issues"
    fi

    # Repair if running as root
    if [ "$EUID" -eq 0 ]; then
        log "Repairing volume..."
        diskutil repairVolume "$VOLUME" 2>&1 | tee -a "$LOG_DIR/disk_repair_$TIMESTAMP.log" || true
        log_success "Volume repair complete"
    else
        log_warning "Run as root to repair volume: sudo diskutil repairVolume $VOLUME"
    fi
}

#===============================================================================
# PHASE 3: PERMISSION REPAIR
#===============================================================================

phase_permissions() {
    print_phase 3 "PERMISSION REPAIR"

    log "Fixing directory permissions (755)..."
    local dir_count=0
    find "$VOLUME" -type d 2>/dev/null | while read -r dir; do
        if chmod 755 "$dir" 2>/dev/null; then
            ((dir_count++))
            ((DIRS_FIXED++))
        fi
        [ $((dir_count % 1000)) -eq 0 ] && echo -ne "\r${CYAN}Directories: $dir_count${NC}"
    done
    echo ""
    log_success "Fixed $DIRS_FIXED directories"

    log "Fixing file permissions..."
    local file_count=0

    # Regular files: 644
    find "$VOLUME" -type f \
        -not -name "*.sh" -not -name "*.bash" -not -name "*.py" \
        -not -name "*.rb" -not -name "*.pl" \
        -not -path '*/.git/*' \
        2>/dev/null | while read -r file; do
        if chmod 644 "$file" 2>/dev/null; then
            ((file_count++))
            ((FILES_FIXED++))
        fi
        [ $((file_count % 1000)) -eq 0 ] && echo -ne "\r${CYAN}Files: $file_count${NC}"
    done
    echo ""

    # Executable scripts: 755
    log "Making scripts executable (755)..."
    find "$VOLUME" -type f \( \
        -name "*.sh" -o -name "*.bash" -o -name "*.zsh" -o \
        -name "*.py" -o -name "*.rb" -o -name "*.pl" \
    \) 2>/dev/null | while read -r script; do
        chmod 755 "$script" 2>/dev/null
    done

    log_success "Fixed $FILES_FIXED files"
}

#===============================================================================
# PHASE 4: ACL CLEANUP
#===============================================================================

phase_acls() {
    print_phase 4 "ACL CLEANUP"

    log "Removing all ACLs from volume..."

    if chmod -RN "$VOLUME" 2>/dev/null; then
        log_success "ACLs removed successfully"
    else
        log_warning "Some ACLs could not be removed (may need root)"

        # Try file by file
        log "Attempting file-by-file ACL removal..."
        find "$VOLUME" -type f 2>/dev/null | head -10000 | while read -r file; do
            chmod -N "$file" 2>/dev/null && ((ACLS_REMOVED++))
        done
        log "Removed ACLs from $ACLS_REMOVED files"
    fi
}

#===============================================================================
# PHASE 5: EXTENDED ATTRIBUTES
#===============================================================================

phase_xattrs() {
    print_phase 5 "EXTENDED ATTRIBUTES CLEANUP"

    if ! command -v xattr &>/dev/null; then
        log_warning "xattr not available, skipping"
        return
    fi

    local xattrs_to_remove=(
        "com.apple.quarantine"
        "com.apple.metadata:kMDItemWhereFroms"
        "com.apple.metadata:kMDItemDownloadedDate"
        "com.apple.FinderInfo"
        "com.apple.lastuseddate#PS"
        "com.apple.metadata:_kMDItemUserTags"
    )

    for attr in "${xattrs_to_remove[@]}"; do
        log "Removing $attr..."
        xattr -rd "$attr" "$VOLUME" 2>/dev/null || true
        ((XATTRS_REMOVED++))
    done

    log_success "Extended attributes cleaned"
}

#===============================================================================
# PHASE 6: FILE LOCKS
#===============================================================================

phase_locks() {
    print_phase 6 "FILE LOCK REMOVAL"

    if ! command -v chflags &>/dev/null; then
        log_warning "chflags not available, skipping"
        return
    fi

    log "Removing user immutable flags..."
    chflags -R nouchg "$VOLUME" 2>/dev/null || true

    log "Removing system immutable flags..."
    if [ "$EUID" -eq 0 ]; then
        chflags -R noschg "$VOLUME" 2>/dev/null || true
    fi

    log "Removing hidden flags..."
    chflags -R nohidden "$VOLUME" 2>/dev/null || true

    log_success "File locks removed"
}

#===============================================================================
# PHASE 7: JUNK CLEANUP
#===============================================================================

phase_cleanup() {
    print_phase 7 "JUNK FILE CLEANUP"

    local junk_removed=0

    log "Removing .DS_Store files..."
    find "$VOLUME" -name ".DS_Store" -delete 2>/dev/null
    junk_removed=$((junk_removed + $(find "$VOLUME" -name ".DS_Store" 2>/dev/null | wc -l)))

    log "Removing AppleDouble files (._*)..."
    find "$VOLUME" -name "._*" -delete 2>/dev/null

    log "Removing Thumbs.db..."
    find "$VOLUME" -name "Thumbs.db" -delete 2>/dev/null
    find "$VOLUME" -name "thumbs.db" -delete 2>/dev/null

    log "Removing desktop.ini..."
    find "$VOLUME" -name "desktop.ini" -delete 2>/dev/null
    find "$VOLUME" -name "Desktop.ini" -delete 2>/dev/null

    log "Removing system folders..."
    rm -rf "$VOLUME/.Spotlight-V100" 2>/dev/null || true
    rm -rf "$VOLUME/.fseventsd" 2>/dev/null || true
    rm -rf "$VOLUME/.Trashes" 2>/dev/null || true
    rm -rf "$VOLUME/.TemporaryItems" 2>/dev/null || true
    rm -rf "$VOLUME/__MACOSX" 2>/dev/null || true

    log "Removing empty directories..."
    find "$VOLUME" -type d -empty -delete 2>/dev/null || true

    log_success "Junk files cleaned"
}

#===============================================================================
# PHASE 8: INSTALL ALL AGENTS
#===============================================================================

phase_agents() {
    print_phase 8 "DEPLOYING ALL AGENTS"

    # Agent: Volume Monitor
    log "Installing Volume Monitor Agent..."
    cat > "$LAUNCH_AGENTS_DIR/com.noizylab.volume-monitor.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizylab.volume-monitor</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>-c</string>
        <string>[ -d "$VOLUME" ] &amp;&amp; echo "\$(date): Volume mounted" >> $LOG_DIR/volume-monitor.log || echo "\$(date): Volume NOT mounted" >> $LOG_DIR/volume-monitor.log</string>
    </array>
    <key>StartInterval</key>
    <integer>300</integer>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOF
    ((AGENTS_INSTALLED++))

    # Agent: Daily Backup
    log "Installing Daily Backup Agent..."
    cat > "$LAUNCH_AGENTS_DIR/com.noizylab.backup-12tb.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizylab.backup-12tb</string>
    <key>ProgramArguments</key>
    <array>
        <string>$SCRIPTS_DIR/backup-sync.sh</string>
        <string>backup</string>
        <string>$VOLUME</string>
        <string>$DEST_DIR/backups</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>2</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>$LOG_DIR/backup-12tb.log</string>
    <key>StandardErrorPath</key>
    <string>$LOG_DIR/backup-12tb.error.log</string>
</dict>
</plist>
EOF
    ((AGENTS_INSTALLED++))

    # Agent: Hourly Sync
    log "Installing Hourly Sync Agent..."
    cat > "$LAUNCH_AGENTS_DIR/com.noizylab.sync-12tb.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizylab.sync-12tb</string>
    <key>ProgramArguments</key>
    <array>
        <string>$SCRIPTS_DIR/backup-sync.sh</string>
        <string>sync</string>
        <string>$VOLUME</string>
        <string>$DEST_DIR/code</string>
    </array>
    <key>StartInterval</key>
    <integer>3600</integer>
    <key>StandardOutPath</key>
    <string>$LOG_DIR/sync-12tb.log</string>
    <key>StandardErrorPath</key>
    <string>$LOG_DIR/sync-12tb.error.log</string>
</dict>
</plist>
EOF
    ((AGENTS_INSTALLED++))

    # Agent: Weekly Integrity Check
    log "Installing Weekly Integrity Agent..."
    cat > "$LAUNCH_AGENTS_DIR/com.noizylab.integrity-12tb.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizylab.integrity-12tb</string>
    <key>ProgramArguments</key>
    <array>
        <string>$SCRIPTS_DIR/integrity-checker.sh</string>
        <string>verify</string>
        <string>$VOLUME</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>0</integer>
        <key>Hour</key>
        <integer>3</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>$LOG_DIR/integrity-12tb.log</string>
    <key>StandardErrorPath</key>
    <string>$LOG_DIR/integrity-12tb.error.log</string>
</dict>
</plist>
EOF
    ((AGENTS_INSTALLED++))

    # Agent: Weekly Security Scan
    log "Installing Weekly Security Agent..."
    cat > "$LAUNCH_AGENTS_DIR/com.noizylab.security-12tb.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizylab.security-12tb</string>
    <key>ProgramArguments</key>
    <array>
        <string>$SCRIPTS_DIR/security-scanner.sh</string>
        <string>scan</string>
        <string>$VOLUME</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>6</integer>
        <key>Hour</key>
        <integer>4</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>$LOG_DIR/security-12tb.log</string>
    <key>StandardErrorPath</key>
    <string>$LOG_DIR/security-12tb.error.log</string>
</dict>
</plist>
EOF
    ((AGENTS_INSTALLED++))

    # Agent: Git Repository Updates
    log "Installing Git Update Agent..."
    cat > "$LAUNCH_AGENTS_DIR/com.noizylab.git-12tb.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizylab.git-12tb</string>
    <key>ProgramArguments</key>
    <array>
        <string>$SCRIPTS_DIR/git-manager.sh</string>
        <string>fetch</string>
        <string>$VOLUME</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>1</integer>
        <key>Hour</key>
        <integer>6</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>$LOG_DIR/git-12tb.log</string>
    <key>StandardErrorPath</key>
    <string>$LOG_DIR/git-12tb.error.log</string>
</dict>
</plist>
EOF
    ((AGENTS_INSTALLED++))

    # Agent: Monthly Duplicate Scan
    log "Installing Monthly Duplicate Agent..."
    cat > "$LAUNCH_AGENTS_DIR/com.noizylab.duplicates-12tb.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizylab.duplicates-12tb</string>
    <key>ProgramArguments</key>
    <array>
        <string>$SCRIPTS_DIR/duplicate-cleaner.sh</string>
        <string>scan</string>
        <string>$VOLUME</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Day</key>
        <integer>1</integer>
        <key>Hour</key>
        <integer>5</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>$LOG_DIR/duplicates-12tb.log</string>
    <key>StandardErrorPath</key>
    <string>$LOG_DIR/duplicates-12tb.error.log</string>
</dict>
</plist>
EOF
    ((AGENTS_INSTALLED++))

    # Agent: Permission Repair (Weekly)
    log "Installing Weekly Permission Repair Agent..."
    cat > "$LAUNCH_AGENTS_DIR/com.noizylab.permissions-12tb.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizylab.permissions-12tb</string>
    <key>ProgramArguments</key>
    <array>
        <string>$SCRIPTS_DIR/quick-fix-permissions.sh</string>
        <string>$VOLUME</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>3</integer>
        <key>Hour</key>
        <integer>4</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>$LOG_DIR/permissions-12tb.log</string>
    <key>StandardErrorPath</key>
    <string>$LOG_DIR/permissions-12tb.error.log</string>
</dict>
</plist>
EOF
    ((AGENTS_INSTALLED++))

    # Agent: Code Statistics (Monthly)
    log "Installing Monthly Stats Agent..."
    cat > "$LAUNCH_AGENTS_DIR/com.noizylab.stats-12tb.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizylab.stats-12tb</string>
    <key>ProgramArguments</key>
    <array>
        <string>$SCRIPTS_DIR/code-stats.sh</string>
        <string>report</string>
        <string>$VOLUME</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Day</key>
        <integer>15</integer>
        <key>Hour</key>
        <integer>6</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>$LOG_DIR/stats-12tb.log</string>
    <key>StandardErrorPath</key>
    <string>$LOG_DIR/stats-12tb.error.log</string>
</dict>
</plist>
EOF
    ((AGENTS_INSTALLED++))

    log_success "Created $AGENTS_INSTALLED agents"
}

#===============================================================================
# PHASE 9: LOAD AGENTS
#===============================================================================

phase_load_agents() {
    print_phase 9 "LOADING AGENTS"

    log "Loading all NOIZYLAB agents..."

    for plist in "$LAUNCH_AGENTS_DIR"/com.noizylab.*.plist; do
        if [ -f "$plist" ]; then
            local name=$(basename "$plist" .plist)

            # Unload if already loaded
            launchctl unload "$plist" 2>/dev/null || true

            # Load agent
            if launchctl load "$plist" 2>/dev/null; then
                log_success "Loaded: $name"
            else
                log_warning "Could not load: $name"
            fi
        fi
    done

    echo ""
    log "Active agents:"
    launchctl list | grep noizylab || echo "  (none running yet)"
}

#===============================================================================
# PHASE 10: VERIFICATION
#===============================================================================

phase_verify() {
    print_phase 10 "VERIFICATION"

    log "Verifying volume status..."

    # Check permissions
    local test_file=$(find "$VOLUME" -type f 2>/dev/null | head -1)
    if [ -n "$test_file" ] && [ -r "$test_file" ]; then
        log_success "Files are readable"
    else
        log_warning "Some files may not be readable"
    fi

    # Check agents
    local loaded_agents=$(launchctl list | grep -c noizylab 2>/dev/null || echo "0")
    log "Loaded agents: $loaded_agents"

    # Volume health
    if command -v diskutil &>/dev/null; then
        local vol_status=$(diskutil info "$VOLUME" 2>/dev/null | grep "Volume Free Space" | awk -F: '{print $2}' | xargs)
        log "Volume free space: $vol_status"
    fi

    log_success "Verification complete"
}

#===============================================================================
# FINAL REPORT
#===============================================================================

generate_report() {
    local report="$LOG_DIR/repair_report_$TIMESTAMP.md"

    cat > "$report" << EOF
# NOIZYLAB Volume Repair & Rebuild Report

**Generated:** $(date)
**Volume:** $VOLUME

## Repair Summary

| Action | Count |
|--------|-------|
| Directories Fixed | $DIRS_FIXED |
| Files Fixed | $FILES_FIXED |
| ACLs Removed | $ACLS_REMOVED |
| XAttrs Cleaned | $XATTRS_REMOVED |
| Agents Installed | $AGENTS_INSTALLED |
| Errors | $ERRORS |

## Installed Agents

| Agent | Schedule | Task |
|-------|----------|------|
| volume-monitor | Every 5 min | Check volume mount status |
| backup-12tb | Daily 2 AM | Incremental backup |
| sync-12tb | Hourly | Smart sync to NOIZYLAB |
| integrity-12tb | Sunday 3 AM | File integrity check |
| security-12tb | Saturday 4 AM | Security scan |
| git-12tb | Monday 6 AM | Fetch all git repos |
| duplicates-12tb | 1st of month 5 AM | Duplicate scan |
| permissions-12tb | Wednesday 4 AM | Permission repair |
| stats-12tb | 15th of month 6 AM | Code statistics |

## Agent Commands

\`\`\`bash
# List agents
launchctl list | grep noizylab

# Check agent status
launchctl list com.noizylab.backup-12tb

# Run agent manually
launchctl start com.noizylab.backup-12tb

# Stop agent
launchctl stop com.noizylab.backup-12tb

# Unload agent
launchctl unload ~/Library/LaunchAgents/com.noizylab.backup-12tb.plist

# View logs
tail -f ~/.noizylab/logs/*.log
\`\`\`

## Next Steps

1. Monitor agents: \`tail -f ~/.noizylab/logs/*.log\`
2. Run initial extraction: \`./scripts/extract-12tb.sh\`
3. Check for secrets: \`noizylab security scan $VOLUME\`

---
*Generated by NOIZYLAB Volume Repair & Rebuild*
EOF

    log_success "Report saved: $report"
}

#===============================================================================
# MAIN
#===============================================================================

main() {
    print_banner

    echo -e "${CYAN}Volume: $VOLUME${NC}"
    echo -e "${CYAN}Destination: $DEST_DIR${NC}"
    echo ""

    # Run all phases
    phase_validate
    phase_disk_repair
    phase_permissions
    phase_acls
    phase_xattrs
    phase_locks
    phase_cleanup
    phase_agents
    phase_load_agents
    phase_verify
    generate_report

    # Final summary
    echo ""
    echo -e "${GREEN}${BOLD}"
    echo "╔═══════════════════════════════════════════════════════════════════╗"
    echo "║              VOLUME REPAIR & REBUILD COMPLETE!                    ║"
    echo "╠═══════════════════════════════════════════════════════════════════╣"
    printf "║  Directories Fixed:  %-10s                                 ║\n" "$DIRS_FIXED"
    printf "║  Files Fixed:        %-10s                                 ║\n" "$FILES_FIXED"
    printf "║  Agents Installed:   %-10s                                 ║\n" "$AGENTS_INSTALLED"
    printf "║  Errors:             %-10s                                 ║\n" "$ERRORS"
    echo "╠═══════════════════════════════════════════════════════════════════╣"
    echo "║  Logs: ~/.noizylab/logs/                                         ║"
    echo "╚═══════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"

    echo ""
    echo -e "${CYAN}Scheduled Agents:${NC}"
    echo "  • Volume Monitor     - Every 5 minutes"
    echo "  • Backup            - Daily 2:00 AM"
    echo "  • Sync              - Every hour"
    echo "  • Integrity Check   - Sunday 3:00 AM"
    echo "  • Security Scan     - Saturday 4:00 AM"
    echo "  • Git Fetch         - Monday 6:00 AM"
    echo "  • Duplicate Scan    - 1st of month 5:00 AM"
    echo "  • Permission Repair - Wednesday 4:00 AM"
    echo "  • Code Statistics   - 15th of month 6:00 AM"
    echo ""

    if [ $ERRORS -gt 0 ]; then
        echo -e "${YELLOW}⚠️  $ERRORS errors occurred. Check logs for details.${NC}"
    fi

    echo -e "${GREEN}Volume is repaired and all agents are deployed!${NC}"
}

# Handle arguments
case "${1:-}" in
    --help|-h)
        echo "NOIZYLAB Volume Repair & Rebuild"
        echo ""
        echo "Usage: $0 [volume_path]"
        echo ""
        echo "Default: /Volumes/12TB"
        echo ""
        echo "For full repair, run as root:"
        echo "  sudo $0 /Volumes/12TB"
        exit 0
        ;;
    *)
        main
        ;;
esac
