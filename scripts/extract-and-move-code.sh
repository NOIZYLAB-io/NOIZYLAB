#!/bin/bash
#===============================================================================
# NOIZYLAB CODE EXTRACTION & MIGRATION TOOL
# Scans, heals, optimizes, and moves all code from source to destination
#===============================================================================

set -e

# Configuration
SOURCE_DIR="/Volumes/4TBSG"
DEST_DIR="/Users/m2ultra/NOIZYLAB"
LOG_DIR="$DEST_DIR/.migration-logs"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="$LOG_DIR/migration_$TIMESTAMP.log"
REPORT_FILE="$LOG_DIR/report_$TIMESTAMP.md"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Code file extensions to extract
CODE_EXTENSIONS=(
    # Web
    "js" "jsx" "ts" "tsx" "mjs" "cjs"
    "html" "htm" "css" "scss" "sass" "less"
    "vue" "svelte" "astro"
    # Backend
    "py" "pyw" "pyx" "pxd"
    "rb" "erb" "rake"
    "php" "phtml"
    "go" "mod" "sum"
    "rs" "toml"
    "java" "kt" "kts" "scala" "clj" "cljs"
    "cs" "fs" "vb"
    "swift" "m" "mm" "h"
    "c" "cpp" "cc" "cxx" "hpp" "hxx"
    # Shell & Config
    "sh" "bash" "zsh" "fish" "ps1" "psm1" "bat" "cmd"
    "yml" "yaml" "json" "jsonc" "json5"
    "xml" "xsl" "xslt"
    "ini" "cfg" "conf" "config"
    "env" "env.local" "env.example"
    # Data & DB
    "sql" "prisma" "graphql" "gql"
    # Docs & Markup
    "md" "mdx" "rst" "txt" "tex"
    # DevOps
    "dockerfile" "docker-compose" "Makefile" "Rakefile" "Gemfile"
    "tf" "tfvars" "hcl"
    # Mobile
    "dart" "gradle"
    # Other
    "r" "R" "jl" "lua" "pl" "pm" "ex" "exs" "erl" "hrl"
    "hs" "lhs" "elm" "ml" "mli" "nim" "zig" "v"
    "sol" "vy" # Solidity, Vyper (blockchain)
)

# Config files (no extension)
CONFIG_FILES=(
    "Dockerfile" "Makefile" "Rakefile" "Gemfile" "Podfile"
    "Vagrantfile" "Procfile" "Brewfile"
    ".gitignore" ".gitattributes" ".gitmodules"
    ".dockerignore" ".npmignore" ".eslintrc" ".prettierrc"
    ".babelrc" ".editorconfig" ".env" ".nvmrc"
    "package.json" "tsconfig.json" "jsconfig.json"
    "composer.json" "Cargo.toml" "go.mod" "requirements.txt"
    "setup.py" "pyproject.toml" "poetry.lock"
)

# Directories to skip
SKIP_DIRS=(
    "node_modules" ".git" "__pycache__" ".pytest_cache"
    "venv" ".venv" "env" ".env" "virtualenv"
    ".idea" ".vscode" ".vs"
    "dist" "build" "out" "target" "bin" "obj"
    ".next" ".nuxt" ".svelte-kit" ".astro"
    "vendor" "packages" ".pub-cache"
    ".Trash" ".Spotlight-V100" ".fseventsd"
    "System Volume Information" "\$RECYCLE.BIN"
    ".cache" "cache" "tmp" "temp"
    "coverage" ".nyc_output"
)

# Counters
TOTAL_FILES=0
TOTAL_SIZE=0
HEALED_FILES=0
DUPLICATES_FOUND=0
ERRORS=0

#===============================================================================
# UTILITY FUNCTIONS
#===============================================================================

log() {
    echo -e "${CYAN}[$(date +'%H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
}

log_success() {
    echo -e "${GREEN}[✓]${NC} $1" | tee -a "$LOG_FILE"
}

log_warning() {
    echo -e "${YELLOW}[!]${NC} $1" | tee -a "$LOG_FILE"
}

log_error() {
    echo -e "${RED}[✗]${NC} $1" | tee -a "$LOG_FILE"
    ((ERRORS++))
}

log_info() {
    echo -e "${BLUE}[i]${NC} $1" | tee -a "$LOG_FILE"
}

print_banner() {
    echo -e "${PURPLE}"
    echo "╔═══════════════════════════════════════════════════════════════════╗"
    echo "║                    NOIZYLAB CODE EXTRACTOR                        ║"
    echo "║              Scan • Heal • Optimize • Migrate                     ║"
    echo "╚═══════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_section() {
    echo -e "\n${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${PURPLE}  $1${NC}"
    echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
}

human_size() {
    local bytes=$1
    if [ $bytes -ge 1073741824 ]; then
        echo "$(echo "scale=2; $bytes/1073741824" | bc) GB"
    elif [ $bytes -ge 1048576 ]; then
        echo "$(echo "scale=2; $bytes/1048576" | bc) MB"
    elif [ $bytes -ge 1024 ]; then
        echo "$(echo "scale=2; $bytes/1024" | bc) KB"
    else
        echo "$bytes bytes"
    fi
}

#===============================================================================
# VALIDATION
#===============================================================================

validate_paths() {
    print_section "VALIDATING PATHS"

    # Check source
    if [ ! -d "$SOURCE_DIR" ]; then
        log_error "Source directory not found: $SOURCE_DIR"
        echo -e "${YELLOW}Make sure your 4TB drive is mounted at /Volumes/4TBSG${NC}"
        exit 1
    fi
    log_success "Source found: $SOURCE_DIR"

    # Check/create destination
    if [ ! -d "$DEST_DIR" ]; then
        log_info "Creating destination directory: $DEST_DIR"
        mkdir -p "$DEST_DIR"
    fi
    log_success "Destination ready: $DEST_DIR"

    # Create log directory
    mkdir -p "$LOG_DIR"
    log_success "Log directory ready: $LOG_DIR"

    # Check disk space
    local source_size=$(du -sk "$SOURCE_DIR" 2>/dev/null | cut -f1 || echo "0")
    local dest_free=$(df -k "$DEST_DIR" | tail -1 | awk '{print $4}')

    log_info "Source size: $(human_size $((source_size * 1024)))"
    log_info "Destination free: $(human_size $((dest_free * 1024)))"
}

#===============================================================================
# SCANNING
#===============================================================================

build_find_pattern() {
    local pattern=""

    # Add extension patterns
    for ext in "${CODE_EXTENSIONS[@]}"; do
        if [ -z "$pattern" ]; then
            pattern="-name '*.$ext'"
        else
            pattern="$pattern -o -name '*.$ext'"
        fi
    done

    # Add config file patterns
    for file in "${CONFIG_FILES[@]}"; do
        pattern="$pattern -o -name '$file'"
    done

    echo "$pattern"
}

build_prune_pattern() {
    local prune=""
    for dir in "${SKIP_DIRS[@]}"; do
        if [ -z "$prune" ]; then
            prune="-name '$dir' -prune"
        else
            prune="$prune -o -name '$dir' -prune"
        fi
    done
    echo "$prune"
}

scan_source() {
    print_section "SCANNING SOURCE DIRECTORY"

    log "Scanning $SOURCE_DIR for code files..."
    log "This may take a while for large drives..."

    local scan_file="$LOG_DIR/scan_$TIMESTAMP.txt"
    local count=0

    # Build find command dynamically
    local prune_cmd=""
    for dir in "${SKIP_DIRS[@]}"; do
        prune_cmd="$prune_cmd -path '*/$dir' -prune -o"
    done

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
        -type f \( \
            -name "*.js" -o -name "*.jsx" -o -name "*.ts" -o -name "*.tsx" -o \
            -name "*.py" -o -name "*.rb" -o -name "*.php" -o -name "*.go" -o \
            -name "*.rs" -o -name "*.java" -o -name "*.kt" -o -name "*.swift" -o \
            -name "*.c" -o -name "*.cpp" -o -name "*.h" -o -name "*.hpp" -o \
            -name "*.cs" -o -name "*.sh" -o -name "*.bash" -o \
            -name "*.html" -o -name "*.css" -o -name "*.scss" -o \
            -name "*.json" -o -name "*.yml" -o -name "*.yaml" -o \
            -name "*.md" -o -name "*.sql" -o -name "*.graphql" -o \
            -name "*.vue" -o -name "*.svelte" -o \
            -name "*.toml" -o -name "*.xml" -o \
            -name "Dockerfile" -o -name "Makefile" -o \
            -name "*.env*" -o -name "*.config.*" -o \
            -name "package.json" -o -name "tsconfig.json" -o \
            -name "requirements.txt" -o -name "Cargo.toml" -o \
            -name "go.mod" -o -name "*.sol" -o \
            -name ".gitignore" -o -name ".dockerignore" \
        \) -print 2>/dev/null | while read -r file; do
            echo "$file" >> "$scan_file"
            ((count++))
            if [ $((count % 1000)) -eq 0 ]; then
                echo -ne "\r${CYAN}Files found: $count${NC}"
            fi
        done

    echo ""

    if [ -f "$scan_file" ]; then
        TOTAL_FILES=$(wc -l < "$scan_file" | tr -d ' ')
        TOTAL_SIZE=$(cat "$scan_file" | xargs -I {} stat -f%z "{}" 2>/dev/null | awk '{s+=$1}END{print s}' || echo "0")
    fi

    log_success "Scan complete: $TOTAL_FILES code files found"
    log_info "Total size: $(human_size ${TOTAL_SIZE:-0})"

    # Generate file type breakdown
    echo "" >> "$LOG_FILE"
    echo "=== FILE TYPE BREAKDOWN ===" >> "$LOG_FILE"
    if [ -f "$scan_file" ]; then
        cat "$scan_file" | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -30 >> "$LOG_FILE"
    fi
}

#===============================================================================
# HEALING
#===============================================================================

heal_file() {
    local file="$1"
    local healed=false

    # Skip binary files
    if file "$file" | grep -q "binary"; then
        return 0
    fi

    # Fix line endings (CRLF -> LF)
    if file "$file" | grep -q "CRLF"; then
        sed -i '' 's/\r$//' "$file" 2>/dev/null && healed=true
    fi

    # Fix file permissions (make readable)
    if [ ! -r "$file" ]; then
        chmod u+r "$file" 2>/dev/null && healed=true
    fi

    # Fix UTF-8 BOM
    if head -c 3 "$file" | od -An -tx1 | grep -q "ef bb bf"; then
        tail -c +4 "$file" > "$file.tmp" && mv "$file.tmp" "$file" && healed=true
    fi

    # Fix trailing whitespace in specific file types
    local ext="${file##*.}"
    case "$ext" in
        js|ts|jsx|tsx|py|rb|go|rs|java|php|css|scss|html|json|yml|yaml|md)
            if grep -q '[[:space:]]$' "$file" 2>/dev/null; then
                sed -i '' 's/[[:space:]]*$//' "$file" 2>/dev/null && healed=true
            fi
            ;;
    esac

    if [ "$healed" = true ]; then
        ((HEALED_FILES++))
        return 1
    fi
    return 0
}

heal_files() {
    print_section "HEALING FILES"

    local scan_file="$LOG_DIR/scan_$TIMESTAMP.txt"

    if [ ! -f "$scan_file" ]; then
        log_warning "No scan file found, skipping healing"
        return
    fi

    log "Healing files (fixing line endings, permissions, encoding)..."

    local count=0
    local total=$(wc -l < "$scan_file" | tr -d ' ')

    while IFS= read -r file; do
        ((count++))
        if [ $((count % 100)) -eq 0 ]; then
            echo -ne "\r${CYAN}Progress: $count/$total files checked${NC}"
        fi
        heal_file "$file"
    done < "$scan_file"

    echo ""
    log_success "Healing complete: $HEALED_FILES files fixed"
}

#===============================================================================
# OPTIMIZATION (Deduplication)
#===============================================================================

find_duplicates() {
    print_section "FINDING DUPLICATES"

    local scan_file="$LOG_DIR/scan_$TIMESTAMP.txt"
    local dup_file="$LOG_DIR/duplicates_$TIMESTAMP.txt"

    if [ ! -f "$scan_file" ]; then
        log_warning "No scan file found, skipping deduplication"
        return
    fi

    log "Calculating file hashes to find duplicates..."

    # Create hash file
    local hash_file="$LOG_DIR/hashes_$TIMESTAMP.txt"
    local count=0
    local total=$(wc -l < "$scan_file" | tr -d ' ')

    while IFS= read -r file; do
        ((count++))
        if [ $((count % 100)) -eq 0 ]; then
            echo -ne "\r${CYAN}Hashing: $count/$total${NC}"
        fi

        if [ -f "$file" ] && [ -r "$file" ]; then
            local hash=$(md5 -q "$file" 2>/dev/null || md5sum "$file" 2>/dev/null | cut -d' ' -f1)
            if [ -n "$hash" ]; then
                echo "$hash $file" >> "$hash_file"
            fi
        fi
    done < "$scan_file"

    echo ""

    # Find duplicates
    if [ -f "$hash_file" ]; then
        log "Analyzing hashes for duplicates..."

        sort "$hash_file" | awk '{
            hash = $1
            file = substr($0, index($0, $2))
            if (hash in seen) {
                print hash " (DUPLICATE) " file
                print hash " (ORIGINAL)  " seen[hash]
            } else {
                seen[hash] = file
            }
        }' > "$dup_file"

        DUPLICATES_FOUND=$(grep -c "DUPLICATE" "$dup_file" 2>/dev/null || echo "0")

        log_success "Duplicate analysis complete: $DUPLICATES_FOUND duplicates found"

        if [ "$DUPLICATES_FOUND" -gt 0 ]; then
            log_info "Duplicate list saved to: $dup_file"
        fi
    fi
}

#===============================================================================
# MIGRATION
#===============================================================================

organize_and_move() {
    print_section "ORGANIZING & MOVING CODE"

    local scan_file="$LOG_DIR/scan_$TIMESTAMP.txt"

    if [ ! -f "$scan_file" ]; then
        log_error "No scan file found, cannot proceed with migration"
        return 1
    fi

    log "Organizing files by project structure..."

    # Create destination directories
    mkdir -p "$DEST_DIR/code"
    mkdir -p "$DEST_DIR/code/projects"
    mkdir -p "$DEST_DIR/code/scripts"
    mkdir -p "$DEST_DIR/code/configs"
    mkdir -p "$DEST_DIR/code/docs"
    mkdir -p "$DEST_DIR/code/misc"

    local count=0
    local moved=0
    local skipped=0
    local total=$(wc -l < "$scan_file" | tr -d ' ')

    while IFS= read -r file; do
        ((count++))

        if [ $((count % 100)) -eq 0 ]; then
            echo -ne "\r${CYAN}Progress: $count/$total (moved: $moved, skipped: $skipped)${NC}"
        fi

        if [ ! -f "$file" ]; then
            ((skipped++))
            continue
        fi

        # Determine relative path from source
        local rel_path="${file#$SOURCE_DIR/}"
        local dir_name=$(dirname "$rel_path")
        local base_name=$(basename "$file")
        local ext="${base_name##*.}"

        # Determine destination based on file type and structure
        local dest_subdir="code/projects"

        # Check if it's a standalone script
        if [[ "$dir_name" == "." || "$dir_name" == "" ]]; then
            case "$ext" in
                sh|bash|py|rb|pl)
                    dest_subdir="code/scripts"
                    ;;
                md|txt|rst)
                    dest_subdir="code/docs"
                    ;;
                json|yml|yaml|toml|ini|cfg)
                    dest_subdir="code/configs"
                    ;;
                *)
                    dest_subdir="code/misc"
                    ;;
            esac
        fi

        # Create destination directory structure
        local final_dest="$DEST_DIR/$dest_subdir/$rel_path"
        local final_dir=$(dirname "$final_dest")

        mkdir -p "$final_dir" 2>/dev/null

        # Copy file (using cp to preserve original)
        if cp -p "$file" "$final_dest" 2>/dev/null; then
            ((moved++))
        else
            ((skipped++))
            echo "Failed to copy: $file" >> "$LOG_FILE"
        fi

    done < "$scan_file"

    echo ""
    log_success "Migration complete: $moved files moved, $skipped skipped"
}

#===============================================================================
# REPORTING
#===============================================================================

generate_report() {
    print_section "GENERATING REPORT"

    cat > "$REPORT_FILE" << EOF
# NOIZYLAB Code Migration Report

**Generated:** $(date)
**Source:** $SOURCE_DIR
**Destination:** $DEST_DIR

## Summary

| Metric | Value |
|--------|-------|
| Total Files Scanned | $TOTAL_FILES |
| Total Size | $(human_size ${TOTAL_SIZE:-0}) |
| Files Healed | $HEALED_FILES |
| Duplicates Found | $DUPLICATES_FOUND |
| Errors | $ERRORS |

## Directory Structure

\`\`\`
$DEST_DIR/
├── code/
│   ├── projects/    # Full project directories
│   ├── scripts/     # Standalone scripts
│   ├── configs/     # Configuration files
│   ├── docs/        # Documentation files
│   └── misc/        # Other code files
└── .migration-logs/ # Migration logs and reports
\`\`\`

## File Type Distribution

$(if [ -f "$LOG_DIR/scan_$TIMESTAMP.txt" ]; then
    echo '```'
    cat "$LOG_DIR/scan_$TIMESTAMP.txt" | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -20
    echo '```'
fi)

## Logs

- Full log: \`$LOG_FILE\`
- Scan results: \`$LOG_DIR/scan_$TIMESTAMP.txt\`
- Duplicates: \`$LOG_DIR/duplicates_$TIMESTAMP.txt\`

## Next Steps

1. Review the migrated code in \`$DEST_DIR/code/\`
2. Check duplicates file and remove unnecessary copies
3. Verify important projects transferred correctly
4. Update any hardcoded paths in configuration files

---
*Generated by NOIZYLAB Code Extractor*
EOF

    log_success "Report saved to: $REPORT_FILE"
}

#===============================================================================
# MAIN
#===============================================================================

main() {
    print_banner

    log "Starting code extraction and migration..."
    log "Source: $SOURCE_DIR"
    log "Destination: $DEST_DIR"

    # Run all steps
    validate_paths
    scan_source
    heal_files
    find_duplicates
    organize_and_move
    generate_report

    print_section "COMPLETE"

    echo -e "${GREEN}"
    echo "╔═══════════════════════════════════════════════════════════════════╗"
    echo "║                    MIGRATION COMPLETE!                            ║"
    echo "╠═══════════════════════════════════════════════════════════════════╣"
    echo "║  Files Processed: $(printf '%-10s' $TOTAL_FILES)                                   ║"
    echo "║  Files Healed:    $(printf '%-10s' $HEALED_FILES)                                   ║"
    echo "║  Duplicates:      $(printf '%-10s' $DUPLICATES_FOUND)                                   ║"
    echo "║  Errors:          $(printf '%-10s' $ERRORS)                                   ║"
    echo "╠═══════════════════════════════════════════════════════════════════╣"
    echo "║  Report: $REPORT_FILE"
    echo "╚═══════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"

    log "All done! Check $DEST_DIR for your migrated code."
}

# Run with error handling
if [ "$1" == "--dry-run" ]; then
    log_info "DRY RUN MODE - No files will be moved"
    DRY_RUN=true
fi

main "$@"
