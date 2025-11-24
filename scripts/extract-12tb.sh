#!/bin/bash
#===============================================================================
# NOIZYLAB 12TB DRIVE EXTRACTION TOOL
# Complete scan, heal, optimize, and migrate for /Volumes/12TB
#===============================================================================

set -e

# Configuration
SOURCE_DIR="/Volumes/12TB"
DEST_DIR="/Users/m2ultra/NOIZYLAB"
BACKUP_DIR="/Users/m2ultra/NOIZYLAB_BACKUPS"
LOG_DIR="$DEST_DIR/.migration-logs"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="$LOG_DIR/12tb_migration_$TIMESTAMP.log"
REPORT_FILE="$LOG_DIR/12tb_report_$TIMESTAMP.md"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Statistics
TOTAL_FILES=0
TOTAL_SIZE=0
HEALED_FILES=0
DUPLICATES_FOUND=0
PROJECTS_FOUND=0
SECRETS_FOUND=0
MOVED_FILES=0
ERRORS=0

#===============================================================================
# LOGGING
#===============================================================================

log() { echo -e "${CYAN}[$(date +'%H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"; }
log_success() { echo -e "${GREEN}[✓]${NC} $1" | tee -a "$LOG_FILE"; }
log_warning() { echo -e "${YELLOW}[!]${NC} $1" | tee -a "$LOG_FILE"; }
log_error() { echo -e "${RED}[✗]${NC} $1" | tee -a "$LOG_FILE"; ((ERRORS++)); }

print_banner() {
    echo -e "${PURPLE}${BOLD}"
    cat << 'EOF'
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║     ███╗   ██╗ ██████╗ ██╗███████╗██╗   ██╗██╗      █████╗ ██████╗           ║
║     ████╗  ██║██╔═══██╗██║╚══███╔╝╚██╗ ██╔╝██║     ██╔══██╗██╔══██╗          ║
║     ██╔██╗ ██║██║   ██║██║  ███╔╝  ╚████╔╝ ██║     ███████║██████╔╝          ║
║     ██║╚██╗██║██║   ██║██║ ███╔╝    ╚██╔╝  ██║     ██╔══██║██╔══██╗          ║
║     ██║ ╚████║╚██████╔╝██║███████╗   ██║   ███████╗██║  ██║██████╔╝          ║
║     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝           ║
║                                                                               ║
║                    12TB DRIVE EXTRACTION & MIGRATION                          ║
║              SCAN • HEAL • OPTIMIZE • SECURE • MIGRATE                        ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

print_section() {
    echo "" | tee -a "$LOG_FILE"
    echo -e "${PURPLE}╔═══════════════════════════════════════════════════════════════════╗${NC}" | tee -a "$LOG_FILE"
    echo -e "${PURPLE}║  $1$(printf '%*s' $((63 - ${#1})) '')║${NC}" | tee -a "$LOG_FILE"
    echo -e "${PURPLE}╚═══════════════════════════════════════════════════════════════════╝${NC}" | tee -a "$LOG_FILE"
    echo "" | tee -a "$LOG_FILE"
}

print_progress() {
    local current=$1
    local total=$2
    local width=50
    local percentage=$((current * 100 / total))
    local filled=$((current * width / total))
    local empty=$((width - filled))

    printf "\r${CYAN}[${NC}"
    printf "%${filled}s" | tr ' ' '█'
    printf "%${empty}s" | tr ' ' '░'
    printf "${CYAN}]${NC} ${percentage}%% (${current}/${total})"
}

#===============================================================================
# PHASE 1: VALIDATION
#===============================================================================

phase_validate() {
    print_section "PHASE 1: VALIDATION"

    # Check source
    if [ ! -d "$SOURCE_DIR" ]; then
        log_error "Source drive not found: $SOURCE_DIR"
        echo ""
        echo -e "${YELLOW}Please ensure your 12TB drive is mounted at /Volumes/12TB${NC}"
        echo "You can check mounted volumes with: ls /Volumes/"
        exit 1
    fi
    log_success "Source drive found: $SOURCE_DIR"

    # Get drive info
    local drive_size=$(df -h "$SOURCE_DIR" 2>/dev/null | tail -1 | awk '{print $2}')
    local drive_used=$(df -h "$SOURCE_DIR" 2>/dev/null | tail -1 | awk '{print $3}')
    local drive_free=$(df -h "$SOURCE_DIR" 2>/dev/null | tail -1 | awk '{print $4}')

    log "Drive size: $drive_size"
    log "Used: $drive_used"
    log "Free: $drive_free"

    # Create directories
    mkdir -p "$DEST_DIR"
    mkdir -p "$LOG_DIR"
    mkdir -p "$BACKUP_DIR"

    log_success "Destination ready: $DEST_DIR"
    log_success "Logs directory: $LOG_DIR"

    # Check destination space
    local dest_free=$(df -h "$DEST_DIR" 2>/dev/null | tail -1 | awk '{print $4}')
    log "Destination free space: $dest_free"
}

#===============================================================================
# PHASE 2: SCANNING
#===============================================================================

phase_scan() {
    print_section "PHASE 2: DEEP SCAN"

    local scan_file="$LOG_DIR/scan_12tb_$TIMESTAMP.txt"

    log "Scanning $SOURCE_DIR for all code files..."
    log "This may take a while for a 12TB drive..."

    # Find all code files
    find "$SOURCE_DIR" \
        -path '*/node_modules' -prune -o \
        -path '*/.git' -prune -o \
        -path '*/__pycache__' -prune -o \
        -path '*/venv' -prune -o \
        -path '*/.venv' -prune -o \
        -path '*/.next' -prune -o \
        -path '*/dist' -prune -o \
        -path '*/build' -prune -o \
        -path '*/.Trash' -prune -o \
        -path '*/vendor' -prune -o \
        -path '*/.Spotlight-V100' -prune -o \
        -path '*/.fseventsd' -prune -o \
        -type f \( \
            -name "*.js" -o -name "*.jsx" -o -name "*.ts" -o -name "*.tsx" -o -name "*.mjs" -o \
            -name "*.py" -o -name "*.pyw" -o -name "*.pyx" -o \
            -name "*.rb" -o -name "*.erb" -o \
            -name "*.php" -o -name "*.phtml" -o \
            -name "*.go" -o -name "*.rs" -o \
            -name "*.java" -o -name "*.kt" -o -name "*.scala" -o \
            -name "*.swift" -o -name "*.m" -o -name "*.mm" -o \
            -name "*.c" -o -name "*.cpp" -o -name "*.cc" -o -name "*.h" -o -name "*.hpp" -o \
            -name "*.cs" -o -name "*.fs" -o \
            -name "*.html" -o -name "*.htm" -o -name "*.css" -o -name "*.scss" -o -name "*.sass" -o -name "*.less" -o \
            -name "*.vue" -o -name "*.svelte" -o -name "*.astro" -o \
            -name "*.json" -o -name "*.yml" -o -name "*.yaml" -o -name "*.toml" -o -name "*.xml" -o \
            -name "*.md" -o -name "*.mdx" -o -name "*.rst" -o \
            -name "*.sql" -o -name "*.graphql" -o -name "*.prisma" -o \
            -name "*.sh" -o -name "*.bash" -o -name "*.zsh" -o \
            -name "*.sol" -o -name "*.vy" -o \
            -name "*.dart" -o -name "*.lua" -o -name "*.r" -o -name "*.R" -o \
            -name "*.ex" -o -name "*.exs" -o -name "*.erl" -o \
            -name "*.hs" -o -name "*.elm" -o -name "*.clj" -o \
            -name "Dockerfile" -o -name "Makefile" -o -name "Rakefile" -o \
            -name "package.json" -o -name "tsconfig.json" -o \
            -name "requirements.txt" -o -name "Cargo.toml" -o -name "go.mod" -o \
            -name ".gitignore" -o -name ".dockerignore" -o -name ".env*" \
        \) -print 2>/dev/null | while read -r file; do
            echo "$file" >> "$scan_file"
            ((TOTAL_FILES++))
            if [ $((TOTAL_FILES % 1000)) -eq 0 ]; then
                echo -ne "\r${CYAN}Files found: $TOTAL_FILES${NC}"
            fi
        done

    echo ""

    if [ -f "$scan_file" ]; then
        TOTAL_FILES=$(wc -l < "$scan_file" | tr -d ' ')
        TOTAL_SIZE=$(cat "$scan_file" | head -10000 | xargs -I {} stat -f%z "{}" 2>/dev/null | awk '{s+=$1}END{print s}' || echo "0")
    fi

    log_success "Scan complete: $TOTAL_FILES code files found"

    # Count projects
    PROJECTS_FOUND=$(find "$SOURCE_DIR" -name "package.json" -not -path "*/node_modules/*" 2>/dev/null | wc -l | tr -d ' ')
    local python_projects=$(find "$SOURCE_DIR" \( -name "requirements.txt" -o -name "setup.py" -o -name "pyproject.toml" \) 2>/dev/null | wc -l | tr -d ' ')
    local git_repos=$(find "$SOURCE_DIR" -name ".git" -type d 2>/dev/null | wc -l | tr -d ' ')

    log "Node.js projects: $PROJECTS_FOUND"
    log "Python projects: $python_projects"
    log "Git repositories: $git_repos"

    # File type breakdown
    echo "" >> "$LOG_FILE"
    echo "=== FILE TYPE BREAKDOWN ===" >> "$LOG_FILE"
    if [ -f "$scan_file" ]; then
        cat "$scan_file" | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -30 >> "$LOG_FILE"
    fi
}

#===============================================================================
# PHASE 3: HEALING
#===============================================================================

phase_heal() {
    print_section "PHASE 3: HEALING FILES"

    local scan_file="$LOG_DIR/scan_12tb_$TIMESTAMP.txt"

    if [ ! -f "$scan_file" ]; then
        log_warning "No scan file found, skipping healing"
        return
    fi

    log "Fixing file permissions, line endings, and encoding..."

    local count=0
    local total=$(wc -l < "$scan_file" | tr -d ' ')

    # Fix permissions on directories first
    log "Setting directory permissions (755)..."
    find "$SOURCE_DIR" -type d \
        -not -path '*/node_modules/*' \
        -not -path '*/.git/*' \
        -exec chmod 755 {} \; 2>/dev/null &

    # Process files
    while IFS= read -r file; do
        ((count++))
        if [ $((count % 500)) -eq 0 ]; then
            print_progress $count $total
        fi

        if [ ! -f "$file" ]; then
            continue
        fi

        # Make readable
        if [ ! -r "$file" ]; then
            chmod u+r "$file" 2>/dev/null && ((HEALED_FILES++))
        fi

        # Fix permissions based on type
        local ext="${file##*.}"
        case "$ext" in
            sh|bash|py|rb|pl)
                chmod 755 "$file" 2>/dev/null
                ;;
            *)
                chmod 644 "$file" 2>/dev/null
                ;;
        esac

    done < "$scan_file"

    echo ""
    log_success "Healing complete: $HEALED_FILES files fixed"

    # Remove quarantine flags (macOS)
    log "Removing quarantine flags..."
    xattr -rd com.apple.quarantine "$SOURCE_DIR" 2>/dev/null || true

    # Remove ACLs
    log "Cleaning ACLs..."
    chmod -RN "$SOURCE_DIR" 2>/dev/null || true

    # Clean junk files
    log "Removing junk files (.DS_Store, ._*, Thumbs.db)..."
    find "$SOURCE_DIR" -name ".DS_Store" -delete 2>/dev/null || true
    find "$SOURCE_DIR" -name "._*" -delete 2>/dev/null || true
    find "$SOURCE_DIR" -name "Thumbs.db" -delete 2>/dev/null || true
    find "$SOURCE_DIR" -name "desktop.ini" -delete 2>/dev/null || true

    log_success "Junk files cleaned"
}

#===============================================================================
# PHASE 4: OPTIMIZATION (Deduplication)
#===============================================================================

phase_optimize() {
    print_section "PHASE 4: OPTIMIZATION"

    local scan_file="$LOG_DIR/scan_12tb_$TIMESTAMP.txt"
    local hash_file="$LOG_DIR/hashes_12tb_$TIMESTAMP.txt"
    local dup_file="$LOG_DIR/duplicates_12tb_$TIMESTAMP.txt"

    if [ ! -f "$scan_file" ]; then
        log_warning "No scan file found, skipping optimization"
        return
    fi

    log "Computing file hashes to find duplicates..."
    log "Processing large drive - this will take time..."

    local count=0
    local total=$(wc -l < "$scan_file" | tr -d ' ')

    # Only hash files over 1KB to save time
    while IFS= read -r file; do
        ((count++))
        if [ $((count % 200)) -eq 0 ]; then
            print_progress $count $total
        fi

        if [ -f "$file" ] && [ -r "$file" ]; then
            local size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null || echo "0")
            if [ "$size" -gt 1024 ]; then
                local hash=$(md5 -q "$file" 2>/dev/null || md5sum "$file" 2>/dev/null | cut -d' ' -f1)
                if [ -n "$hash" ]; then
                    echo "$hash|$size|$file" >> "$hash_file"
                fi
            fi
        fi
    done < "$scan_file"

    echo ""

    # Find duplicates
    if [ -f "$hash_file" ]; then
        log "Analyzing hashes for duplicates..."

        cut -d'|' -f1 "$hash_file" | sort | uniq -d > "$LOG_DIR/dup_hashes.tmp"
        DUPLICATES_FOUND=$(wc -l < "$LOG_DIR/dup_hashes.tmp" | tr -d ' ')

        if [ "$DUPLICATES_FOUND" -gt 0 ]; then
            echo "DUPLICATE FILES REPORT" > "$dup_file"
            echo "Generated: $(date)" >> "$dup_file"
            echo "========================" >> "$dup_file"

            while read -r hash; do
                echo "" >> "$dup_file"
                echo "Hash: $hash" >> "$dup_file"
                grep "^$hash|" "$hash_file" | cut -d'|' -f3 >> "$dup_file"
            done < "$LOG_DIR/dup_hashes.tmp"

            log_warning "Found $DUPLICATES_FOUND sets of duplicate files"
            log "Duplicate report: $dup_file"
        else
            log_success "No duplicates found"
        fi

        rm -f "$LOG_DIR/dup_hashes.tmp"
    fi
}

#===============================================================================
# PHASE 5: SECURITY SCAN
#===============================================================================

phase_security() {
    print_section "PHASE 5: SECURITY SCAN"

    local scan_file="$LOG_DIR/scan_12tb_$TIMESTAMP.txt"
    local secrets_file="$LOG_DIR/secrets_12tb_$TIMESTAMP.txt"

    log "Scanning for exposed secrets, API keys, and passwords..."

    local patterns=(
        'api[_-]?key["\s]*[:=]["\s]*[A-Za-z0-9_-]{20,}'
        'AKIA[0-9A-Z]{16}'
        'ghp_[A-Za-z0-9]{36}'
        'sk_live_[0-9a-zA-Z]{24}'
        'password["\s]*[:=]["\s]*[^\s]{8,}'
        '-----BEGIN RSA PRIVATE KEY-----'
        '-----BEGIN OPENSSH PRIVATE KEY-----'
        'postgres://[^:]+:[^@]+@'
        'mysql://[^:]+:[^@]+@'
        'mongodb://[^:]+:[^@]+@'
    )

    > "$secrets_file"

    for pattern in "${patterns[@]}"; do
        local results=$(grep -rliE "$pattern" "$SOURCE_DIR" \
            --include="*.js" --include="*.ts" --include="*.py" --include="*.go" \
            --include="*.env*" --include="*.yml" --include="*.yaml" --include="*.json" \
            --exclude-dir=node_modules --exclude-dir=.git \
            2>/dev/null | head -50 || true)

        if [ -n "$results" ]; then
            echo "=== Pattern: ${pattern:0:40}... ===" >> "$secrets_file"
            echo "$results" >> "$secrets_file"
            SECRETS_FOUND=$((SECRETS_FOUND + $(echo "$results" | wc -l)))
        fi
    done

    if [ $SECRETS_FOUND -gt 0 ]; then
        log_warning "Found $SECRETS_FOUND files with potential secrets!"
        log "Review: $secrets_file"
    else
        log_success "No exposed secrets detected"
    fi

    # Check for sensitive files
    log "Checking for sensitive files..."
    local sensitive=$(find "$SOURCE_DIR" \( \
        -name "id_rsa" -o -name "id_dsa" -o -name "*.pem" -o -name "*.key" -o \
        -name "credentials.json" -o -name ".env.production" \
    \) -not -path '*/.git/*' 2>/dev/null | head -20)

    if [ -n "$sensitive" ]; then
        log_warning "Found sensitive files:"
        echo "$sensitive" | head -10
    fi
}

#===============================================================================
# PHASE 6: MIGRATION
#===============================================================================

phase_migrate() {
    print_section "PHASE 6: MIGRATION"

    local scan_file="$LOG_DIR/scan_12tb_$TIMESTAMP.txt"

    if [ ! -f "$scan_file" ]; then
        log_error "No scan file found, cannot proceed with migration"
        return 1
    fi

    log "Organizing and moving files to $DEST_DIR..."

    # Create directory structure
    mkdir -p "$DEST_DIR/code/projects"
    mkdir -p "$DEST_DIR/code/scripts"
    mkdir -p "$DEST_DIR/code/configs"
    mkdir -p "$DEST_DIR/code/libraries"
    mkdir -p "$DEST_DIR/code/docs"
    mkdir -p "$DEST_DIR/code/misc"

    local count=0
    local total=$(wc -l < "$scan_file" | tr -d ' ')

    while IFS= read -r file; do
        ((count++))
        if [ $((count % 500)) -eq 0 ]; then
            print_progress $count $total
        fi

        if [ ! -f "$file" ]; then
            continue
        fi

        # Get relative path
        local rel_path="${file#$SOURCE_DIR/}"
        local dir_name=$(dirname "$rel_path")
        local base_name=$(basename "$file")
        local ext="${base_name##*.}"

        # Determine destination
        local dest_subdir="code/projects"

        if [[ "$dir_name" == "." || -z "$dir_name" ]]; then
            case "$ext" in
                sh|bash|py|rb|pl) dest_subdir="code/scripts" ;;
                md|txt|rst) dest_subdir="code/docs" ;;
                json|yml|yaml|toml|ini) dest_subdir="code/configs" ;;
                *) dest_subdir="code/misc" ;;
            esac
        fi

        # Create destination and copy
        local final_dest="$DEST_DIR/$dest_subdir/$rel_path"
        local final_dir=$(dirname "$final_dest")

        mkdir -p "$final_dir" 2>/dev/null

        if cp -p "$file" "$final_dest" 2>/dev/null; then
            ((MOVED_FILES++))
        else
            log_error "Failed to copy: $file"
        fi

    done < "$scan_file"

    echo ""
    log_success "Migration complete: $MOVED_FILES files moved"
}

#===============================================================================
# PHASE 7: REPORT GENERATION
#===============================================================================

phase_report() {
    print_section "PHASE 7: GENERATING REPORT"

    cat > "$REPORT_FILE" << EOF
# NOIZYLAB 12TB Drive Migration Report

**Generated:** $(date)
**Source:** $SOURCE_DIR
**Destination:** $DEST_DIR

## Summary

| Metric | Value |
|--------|-------|
| Total Files Scanned | $TOTAL_FILES |
| Files Healed | $HEALED_FILES |
| Duplicate Sets | $DUPLICATES_FOUND |
| Potential Secrets | $SECRETS_FOUND |
| Files Migrated | $MOVED_FILES |
| Errors | $ERRORS |

## Directory Structure

\`\`\`
$DEST_DIR/
├── code/
│   ├── projects/    # Full project directories
│   ├── scripts/     # Standalone scripts (.sh, .py, etc.)
│   ├── configs/     # Configuration files
│   ├── libraries/   # Shared libraries
│   ├── docs/        # Documentation
│   └── misc/        # Other code files
└── .migration-logs/ # Migration logs and reports
\`\`\`

## Logs

- Full log: \`$LOG_FILE\`
- Scan results: \`$LOG_DIR/scan_12tb_$TIMESTAMP.txt\`
- Duplicates: \`$LOG_DIR/duplicates_12tb_$TIMESTAMP.txt\`
- Secrets: \`$LOG_DIR/secrets_12tb_$TIMESTAMP.txt\`

## Next Steps

1. Review secrets report and rotate any exposed credentials
2. Check duplicate report and clean if needed
3. Verify important projects transferred correctly
4. Run \`noizylab git update $DEST_DIR\` to update git repos
5. Setup automated backups: \`noizylab automation install\`

---
*Generated by NOIZYLAB 12TB Extractor*
EOF

    log_success "Report saved: $REPORT_FILE"
}

#===============================================================================
# MAIN
#===============================================================================

main() {
    print_banner

    log "Starting 12TB drive extraction and migration..."
    log "Source: $SOURCE_DIR"
    log "Destination: $DEST_DIR"
    log "Log: $LOG_FILE"

    # Run all phases
    phase_validate
    phase_scan
    phase_heal
    phase_optimize
    phase_security
    phase_migrate
    phase_report

    # Final summary
    echo ""
    echo -e "${GREEN}${BOLD}"
    echo "╔═══════════════════════════════════════════════════════════════════╗"
    echo "║                   12TB MIGRATION COMPLETE!                        ║"
    echo "╠═══════════════════════════════════════════════════════════════════╣"
    printf "║  Files Scanned:    %-10s                                   ║\n" "$TOTAL_FILES"
    printf "║  Files Healed:     %-10s                                   ║\n" "$HEALED_FILES"
    printf "║  Duplicates:       %-10s                                   ║\n" "$DUPLICATES_FOUND"
    printf "║  Secrets Found:    %-10s                                   ║\n" "$SECRETS_FOUND"
    printf "║  Files Migrated:   %-10s                                   ║\n" "$MOVED_FILES"
    printf "║  Errors:           %-10s                                   ║\n" "$ERRORS"
    echo "╠═══════════════════════════════════════════════════════════════════╣"
    echo "║  Report: $REPORT_FILE"
    echo "╚═══════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"

    if [ $SECRETS_FOUND -gt 0 ]; then
        echo -e "${RED}${BOLD}⚠️  WARNING: $SECRETS_FOUND files contain potential secrets!${NC}"
        echo -e "${YELLOW}Review: $LOG_DIR/secrets_12tb_$TIMESTAMP.txt${NC}"
    fi

    if [ $ERRORS -gt 0 ]; then
        echo -e "${YELLOW}⚠️  $ERRORS errors occurred during migration. Check logs.${NC}"
    fi

    echo ""
    log_success "All done! Your code is now in $DEST_DIR"
}

# Handle arguments
case "${1:-}" in
    --help|-h)
        echo "NOIZYLAB 12TB Drive Extractor"
        echo ""
        echo "Usage: $0 [options]"
        echo ""
        echo "Options:"
        echo "  --help      Show this help"
        echo "  --dry-run   Scan only, don't move files"
        echo "  --scan      Quick scan without processing"
        echo ""
        echo "Default:"
        echo "  Source:      /Volumes/12TB"
        echo "  Destination: /Users/m2ultra/NOIZYLAB"
        exit 0
        ;;
    --dry-run)
        print_banner
        phase_validate
        phase_scan
        log_warning "DRY RUN - No files were moved"
        exit 0
        ;;
    --scan)
        print_banner
        phase_validate
        phase_scan
        exit 0
        ;;
    *)
        main
        ;;
esac
