#!/bin/bash
# ════════════════════════════════════════════════════════════════════════════
# 📦 MOVE/COPY ALL CODE, THEN DELETE AND CLEAN DISK
# ════════════════════════════════════════════════════════════════════════════
#
# This script:
# 1. Finds all code files (.py, .js, .ts, .mjs, .sh, etc.)
# 2. Copies them to a consolidated CODE_ARCHIVE directory
# 3. Removes duplicates
# 4. Deletes original files after verification
# 5. Cleans up empty directories
#
# Created by: CLAUDE (Code Assistant - Deep Analysis)
# ════════════════════════════════════════════════════════════════════════════

BASE="/Users/m2ultra/NOIZYLAB"
ARCHIVE_DIR="$BASE/CODE_ARCHIVE"
LOG_DIR="$BASE/logs"
mkdir -p "$ARCHIVE_DIR" "$LOG_DIR"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="$LOG_DIR/move_and_clean_${TIMESTAMP}.log"
DRY_RUN=${1:-false}

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Code file extensions
CODE_EXTENSIONS="py|js|ts|tsx|jsx|mjs|cjs|sh|bash|zsh|rb|go|rs|java|kt|swift|php|r|sql|html|css|scss|sass|less|vue|svelte|json|yaml|yml|toml|xml|md|txt|conf|config|ini|env"

# Directories to exclude
EXCLUDE_DIRS="node_modules|.git|.venv|venv|__pycache__|.pytest_cache|dist|build|.next|.nuxt|.cache|logs|CODE_ARCHIVE|backups|.DS_Store|*.pyc|*.pyo|*.log"

echo -e "${CYAN}${BOLD}╔═══════════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}${BOLD}║                                                                           ║${NC}"
echo -e "${CYAN}${BOLD}║         📦 MOVE/COPY ALL CODE & CLEAN DISK                                 ║${NC}"
echo -e "${CYAN}${BOLD}║                                                                           ║${NC}"
echo -e "${CYAN}${BOLD}╚═══════════════════════════════════════════════════════════════════════════╝${NC}"
echo ""

if [ "$DRY_RUN" = "true" ] || [ "$DRY_RUN" = "--dry-run" ]; then
    echo -e "${YELLOW}⚠️  DRY RUN MODE - No files will be deleted${NC}"
    echo ""
fi

echo -e "${BLUE}📋 Log file: $LOG_FILE${NC}"
echo -e "${BLUE}📦 Archive directory: $ARCHIVE_DIR${NC}"
echo ""

# Function to log
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

# Function to get file hash
get_hash() {
    md5 -q "$1" 2>/dev/null || md5sum "$1" 2>/dev/null | cut -d' ' -f1
}

# Step 1: Find and copy all code files
echo -e "${MAGENTA}${BOLD}═══════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}${BOLD}  STEP 1: FINDING AND COPYING ALL CODE FILES${NC}"
echo -e "${MAGENTA}${BOLD}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""

log "Starting code collection..."
TOTAL_FILES=0
COPIED_FILES=0
DUPLICATE_FILES=0
declare -A file_hashes
declare -A file_paths

# Find all code files
while IFS= read -r -d '' file; do
    # Skip excluded directories
    if echo "$file" | grep -qE "($EXCLUDE_DIRS)"; then
        continue
    fi
    
    TOTAL_FILES=$((TOTAL_FILES + 1))
    
    # Get relative path from BASE
    rel_path="${file#$BASE/}"
    archive_path="$ARCHIVE_DIR/$rel_path"
    archive_dir="$(dirname "$archive_path")"
    
    # Create directory structure
    mkdir -p "$archive_dir"
    
    # Get file hash to detect duplicates
    file_hash=$(get_hash "$file")
    
    if [ -n "${file_hashes[$file_hash]}" ]; then
        # Duplicate found
        DUPLICATE_FILES=$((DUPLICATE_FILES + 1))
        log "DUPLICATE: $rel_path (same as ${file_paths[$file_hash]})"
        echo -e "${YELLOW}  ⚠️  Duplicate: ${rel_path:0:60}...${NC}"
    else
        # Copy file
        if cp "$file" "$archive_path" 2>/dev/null; then
            COPIED_FILES=$((COPIED_FILES + 1))
            file_hashes[$file_hash]=1
            file_paths[$file_hash]="$rel_path"
            
            if [ $((COPIED_FILES % 100)) -eq 0 ]; then
                echo -e "${GREEN}  ✅ Copied $COPIED_FILES files...${NC}"
            fi
        else
            log "ERROR: Failed to copy $rel_path"
            echo -e "${RED}  ❌ Failed: ${rel_path:0:60}...${NC}"
        fi
    fi
done < <(find "$BASE" -type f \( -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.tsx" -o -name "*.jsx" -o -name "*.mjs" -o -name "*.cjs" -o -name "*.sh" -o -name "*.bash" -o -name "*.zsh" -o -name "*.rb" -o -name "*.go" -o -name "*.rs" -o -name "*.java" -o -name "*.kt" -o -name "*.swift" -o -name "*.php" -o -name "*.r" -o -name "*.sql" -o -name "*.html" -o -name "*.css" -o -name "*.scss" -o -name "*.sass" -o -name "*.less" -o -name "*.vue" -o -name "*.svelte" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" -o -name "*.toml" -o -name "*.xml" -o -name "*.md" -o -name "*.txt" -o -name "*.conf" -o -name "*.config" -o -name "*.ini" -o -name "*.env" \) -print0 2>/dev/null)

echo ""
echo -e "${GREEN}✅ Step 1 Complete:${NC}"
echo -e "   ${CYAN}Total files found:${NC} $TOTAL_FILES"
echo -e "   ${CYAN}Files copied:${NC} $COPIED_FILES"
echo -e "   ${CYAN}Duplicates skipped:${NC} $DUPLICATE_FILES"
echo ""

# Step 2: Verify archive
echo -e "${MAGENTA}${BOLD}═══════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}${BOLD}  STEP 2: VERIFYING ARCHIVE${NC}"
echo -e "${MAGENTA}${BOLD}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""

ARCHIVE_SIZE=$(du -sh "$ARCHIVE_DIR" 2>/dev/null | cut -f1)
ARCHIVE_COUNT=$(find "$ARCHIVE_DIR" -type f | wc -l | tr -d ' ')

log "Archive verification: $ARCHIVE_COUNT files, $ARCHIVE_SIZE"
echo -e "${GREEN}✅ Archive verified:${NC}"
echo -e "   ${CYAN}Files in archive:${NC} $ARCHIVE_COUNT"
echo -e "   ${CYAN}Archive size:${NC} $ARCHIVE_SIZE"
echo ""

# Step 3: Delete original files (if not dry run)
if [ "$DRY_RUN" != "true" ] && [ "$DRY_RUN" != "--dry-run" ]; then
    echo -e "${MAGENTA}${BOLD}═══════════════════════════════════════════════════════════════════════════${NC}"
    echo -e "${MAGENTA}${BOLD}  STEP 3: DELETING ORIGINAL FILES${NC}"
    echo -e "${MAGENTA}${BOLD}═══════════════════════════════════════════════════════════════════════════${NC}"
    echo ""
    
    echo -e "${YELLOW}⚠️  This will delete original code files!${NC}"
    echo -e "${YELLOW}   Archive is safe at: $ARCHIVE_DIR${NC}"
    echo ""
    read -p "Continue with deletion? (yes/no): " confirm
    
    if [ "$confirm" = "yes" ]; then
        DELETED_COUNT=0
        
        # Delete files that were successfully copied
        while IFS= read -r -d '' file; do
            if echo "$file" | grep -qE "($EXCLUDE_DIRS)"; then
                continue
            fi
            
            rel_path="${file#$BASE/}"
            archive_path="$ARCHIVE_DIR/$rel_path"
            
            # Only delete if archive copy exists and matches
            if [ -f "$archive_path" ]; then
                if [ "$(get_hash "$file")" = "$(get_hash "$archive_path")" ]; then
                    if rm "$file" 2>/dev/null; then
                        DELETED_COUNT=$((DELETED_COUNT + 1))
                        log "DELETED: $rel_path"
                        
                        if [ $((DELETED_COUNT % 100)) -eq 0 ]; then
                            echo -e "${GREEN}  ✅ Deleted $DELETED_COUNT files...${NC}"
                        fi
                    fi
                fi
            fi
        done < <(find "$BASE" -type f \( -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.tsx" -o -name "*.jsx" -o -name "*.mjs" -o -name "*.cjs" -o -name "*.sh" -o -name "*.bash" -o -name "*.zsh" -o -name "*.rb" -o -name "*.go" -o -name "*.rs" -o -name "*.java" -o -name "*.kt" -o -name "*.swift" -o -name "*.php" -o -name "*.r" -o -name "*.sql" -o -name "*.html" -o -name "*.css" -o -name "*.scss" -o -name "*.sass" -o -name "*.less" -o -name "*.vue" -o -name "*.svelte" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" -o -name "*.toml" -o -name "*.xml" -o -name "*.md" -o -name "*.txt" -o -name "*.conf" -o -name "*.config" -o -name "*.ini" -o -name "*.env" \) -print0 2>/dev/null)
        
        echo ""
        echo -e "${GREEN}✅ Step 3 Complete:${NC}"
        echo -e "   ${CYAN}Files deleted:${NC} $DELETED_COUNT"
        echo ""
    else
        echo -e "${YELLOW}⚠️  Deletion cancelled${NC}"
        echo ""
    fi
else
    echo -e "${YELLOW}⚠️  DRY RUN: Skipping deletion${NC}"
    echo ""
fi

# Step 4: Clean up empty directories
echo -e "${MAGENTA}${BOLD}═══════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}${BOLD}  STEP 4: CLEANING UP EMPTY DIRECTORIES${NC}"
echo -e "${MAGENTA}${BOLD}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""

if [ "$DRY_RUN" != "true" ] && [ "$DRY_RUN" != "--dry-run" ]; then
    EMPTY_DELETED=0
    
    # Find and delete empty directories (excluding protected ones)
    while IFS= read -r -d '' dir; do
        if echo "$dir" | grep -qE "(node_modules|\.git|\.venv|venv|__pycache__|\.pytest_cache|dist|build|\.next|\.nuxt|\.cache|logs|CODE_ARCHIVE|backups)"; then
            continue
        fi
        
        if rmdir "$dir" 2>/dev/null; then
            EMPTY_DELETED=$((EMPTY_DELETED + 1))
            log "DELETED EMPTY DIR: ${dir#$BASE/}"
        fi
    done < <(find "$BASE" -type d -empty -print0 2>/dev/null)
    
    echo -e "${GREEN}✅ Step 4 Complete:${NC}"
    echo -e "   ${CYAN}Empty directories removed:${NC} $EMPTY_DELETED"
    echo ""
else
    EMPTY_COUNT=$(find "$BASE" -type d -empty 2>/dev/null | grep -vE "(node_modules|\.git|\.venv|venv|__pycache__|\.pytest_cache|dist|build|\.next|\.nuxt|\.cache|logs|CODE_ARCHIVE|backups)" | wc -l | tr -d ' ')
    echo -e "${YELLOW}⚠️  DRY RUN: Would delete $EMPTY_COUNT empty directories${NC}"
    echo ""
fi

# Step 5: Run final cleanup
echo -e "${MAGENTA}${BOLD}═══════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}${BOLD}  STEP 5: FINAL CLEANUP${NC}"
echo -e "${MAGENTA}${BOLD}═══════════════════════════════════════════════════════════════════════════${NC}"
echo ""

# Run the delete-empty-folders script
if [ -f "$BASE/delete-empty-folders.sh" ]; then
    echo -e "${BLUE}Running delete-empty-folders.sh...${NC}"
    "$BASE/delete-empty-folders.sh" >> "$LOG_FILE" 2>&1
    echo -e "${GREEN}✅ Final cleanup complete${NC}"
    echo ""
fi

# Summary
echo -e "${CYAN}${BOLD}╔═══════════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}${BOLD}║                                                                           ║${NC}"
echo -e "${CYAN}${BOLD}║         ✅ CODE MOVE & CLEAN COMPLETE!                                     ║${NC}"
echo -e "${CYAN}${BOLD}║                                                                           ║${NC}"
echo -e "${CYAN}${BOLD}╚═══════════════════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${GREEN}${BOLD}📊 Summary:${NC}"
echo ""
echo -e "  ${CYAN}•${NC} Total files found: ${BOLD}$TOTAL_FILES${NC}"
echo -e "  ${CYAN}•${NC} Files copied to archive: ${BOLD}$COPIED_FILES${NC}"
echo -e "  ${CYAN}•${NC} Duplicates skipped: ${BOLD}$DUPLICATE_FILES${NC}"
echo -e "  ${CYAN}•${NC} Archive location: ${BOLD}$ARCHIVE_DIR${NC}"
echo -e "  ${CYAN}•${NC} Archive size: ${BOLD}$ARCHIVE_SIZE${NC}"
echo ""

if [ "$DRY_RUN" != "true" ] && [ "$DRY_RUN" != "--dry-run" ]; then
    echo -e "  ${CYAN}•${NC} Original files deleted: ${BOLD}$DELETED_COUNT${NC}"
    echo -e "  ${CYAN}•${NC} Empty directories removed: ${BOLD}$EMPTY_DELETED${NC}"
fi

echo ""
echo -e "${BLUE}📋 Log file: $LOG_FILE${NC}"
echo ""
echo -e "${YELLOW}💡 To restore files from archive:${NC}"
echo -e "   ${CYAN}cp -r $ARCHIVE_DIR/* $BASE/${NC}"
echo ""

log "Code move and clean complete"

