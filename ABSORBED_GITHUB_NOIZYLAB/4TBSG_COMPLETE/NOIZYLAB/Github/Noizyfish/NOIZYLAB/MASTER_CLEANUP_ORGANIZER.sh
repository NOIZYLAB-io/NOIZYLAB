#!/usr/bin/env bash
# ==============================================================================
# NOIZYLAB MASTER CLEANUP & ORGANIZER
# ==============================================================================
# Comprehensive cleanup and organization system for NOIZYLAB
# Analyzes disk usage, removes duplicates, organizes files, and generates reports
#
# Usage: ./MASTER_CLEANUP_ORGANIZER.sh [--analyze-only] [--dry-run]
# ==============================================================================

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Paths
BASE="/Users/m2ultra"
NOIZYLAB="$BASE/NOIZYLAB"
LOG_DIR="$NOIZYLAB/logs/cleanup"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
LOG_FILE="$LOG_DIR/master-cleanup-${TIMESTAMP}.log"
REPORT_FILE="$NOIZYLAB/CLEANUP_REPORT_${TIMESTAMP}.md"

# Flags
ANALYZE_ONLY=0
DRY_RUN=0

# Create log directory
mkdir -p "$LOG_DIR"

# Logging function
log() {
    echo -e "${2:-$CYAN}${1}${NC}" | tee -a "$LOG_FILE"
}

log_header() {
    echo "" | tee -a "$LOG_FILE"
    log "═══════════════════════════════════════════════════════════" "$BOLD"
    log "$1" "$BOLD$CYAN"
    log "═══════════════════════════════════════════════════════════" "$BOLD"
    echo "" | tee -a "$LOG_FILE"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --analyze-only)
            ANALYZE_ONLY=1
            shift
            ;;
        --dry-run)
            DRY_RUN=1
            shift
            ;;
        *)
            log "Unknown option: $1" "$RED"
            exit 1
            ;;
    esac
done

# ==============================================================================
# STEP 1: DISK USAGE ANALYSIS
# ==============================================================================

analyze_disk_usage() {
    log_header "📊 STEP 1: ANALYZING DISK USAGE"
    
    log "Analyzing /Users/m2ultra directory structure..."
    
    # Find top 20 largest directories
    log "Top 20 largest directories in /Users/m2ultra:" "$BOLD"
    du -h -d 1 "$BASE" 2>/dev/null | sort -rh | head -20 | while read size path; do
        log "  $size  →  $path" "$YELLOW"
    done | tee -a "$LOG_FILE"
    
    # Find top 20 largest directories in NOIZYLAB
    log "\nTop 20 largest directories in NOIZYLAB:" "$BOLD"
    du -h -d 1 "$NOIZYLAB" 2>/dev/null | sort -rh | head -20 | while read size path; do
        log "  $size  →  $path" "$YELLOW"
    done | tee -a "$LOG_FILE"
    
    # Find large files (>100MB)
    log "\nLarge files (>100MB) in NOIZYLAB:" "$BOLD"
    find "$NOIZYLAB" -type f -size +100M -exec ls -lh {} \; 2>/dev/null | \
        awk '{print $5, $9}' | sort -rh | head -20 | while read size path; do
        log "  $size  →  $path" "$YELLOW"
    done | tee -a "$LOG_FILE"
    
    # Count file types
    log "\nFile type distribution in NOIZYLAB:" "$BOLD"
    find "$NOIZYLAB" -type f -name "*.*" 2>/dev/null | \
        sed 's/.*\.//' | sort | uniq -c | sort -rn | head -20 | while read count ext; do
        log "  $ext: $count files" "$CYAN"
    done | tee -a "$LOG_FILE"
    
    log "✅ Disk usage analysis complete"
}

# ==============================================================================
# STEP 2: FIND DUPLICATES
# ==============================================================================

find_duplicates() {
    log_header "🔍 STEP 2: FINDING DUPLICATE FILES"
    
    local dup_file="$LOG_DIR/duplicates-${TIMESTAMP}.txt"
    
    log "Scanning for duplicate files (this may take a while)..."
    
    # Find duplicates by name first
    log "Finding duplicate filenames..."
    find "$NOIZYLAB" -type f -name "*.sh" -o -name "*.py" -o -name "*.js" -o -name "*.md" 2>/dev/null | \
        awk -F'/' '{print $NF, $0}' | sort | \
        awk 'BEGIN{prev=""} {if ($1==prev_name) print prev; print $0; prev=$0; prev_name=$1}' | \
        uniq -d -f1 | awk '{print $2}' | sort -u > "$dup_file" || true
    
    local dup_count=$(wc -l < "$dup_file" | tr -d ' ')
    
    if [ "$dup_count" -gt 0 ]; then
        log "Found $dup_count potentially duplicate files:" "$YELLOW"
        head -20 "$dup_file" | while read file; do
            log "  → $file" "$CYAN"
        done
        log "\nFull list saved to: $dup_file"
    else
        log "✅ No obvious duplicates found by filename"
    fi
}

# ==============================================================================
# STEP 3: CLEAN TEMPORARY FILES
# ==============================================================================

clean_temp_files() {
    log_header "🧹 STEP 3: CLEANING TEMPORARY FILES"
    
    local cleaned=0
    local space_saved=0
    
    # Python cache
    log "Removing Python cache files..."
    if [ "$DRY_RUN" -eq 0 ]; then
        local pycache_count=$(find "$NOIZYLAB" -type d -name "__pycache__" 2>/dev/null | wc -l | tr -d ' ')
        if [ "$pycache_count" -gt 0 ]; then
            find "$NOIZYLAB" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
            cleaned=$((cleaned + pycache_count))
            log "  ✓ Removed $pycache_count __pycache__ directories"
        fi
        
        find "$NOIZYLAB" -name "*.pyc" -delete 2>/dev/null || true
        find "$NOIZYLAB" -name "*.pyo" -delete 2>/dev/null || true
    else
        local pycache_count=$(find "$NOIZYLAB" -type d -name "__pycache__" 2>/dev/null | wc -l | tr -d ' ')
        if [ "$pycache_count" -gt 0 ]; then
            log "  [DRY RUN] Would remove $pycache_count __pycache__ directories" "$YELLOW"
        fi
    fi
    
    # Node modules
    log "Checking for node_modules directories..."
    local node_modules=$(find "$NOIZYLAB" -type d -name "node_modules" -prune 2>/dev/null | wc -l | tr -d ' ')
    if [ "$node_modules" -gt 0 ]; then
        log "  Found $node_modules node_modules directories" "$YELLOW"
        if [ "$DRY_RUN" -eq 0 ]; then
            log "  [SKIP] Not removing node_modules (may contain dependencies)" "$YELLOW"
        fi
    fi
    
    # .DS_Store files
    log "Removing .DS_Store files..."
    if [ "$DRY_RUN" -eq 0 ]; then
        local dsstore_count=$(find "$NOIZYLAB" -name ".DS_Store" 2>/dev/null | wc -l | tr -d ' ')
        if [ "$dsstore_count" -gt 0 ]; then
            find "$NOIZYLAB" -name ".DS_Store" -delete 2>/dev/null || true
            log "  ✓ Removed $dsstore_count .DS_Store files"
        fi
    else
        local dsstore_count=$(find "$NOIZYLAB" -name ".DS_Store" 2>/dev/null | wc -l | tr -d ' ')
        if [ "$dsstore_count" -gt 0 ]; then
            log "  [DRY RUN] Would remove $dsstore_count .DS_Store files" "$YELLOW"
        fi
    fi
    
    # Old log files (>30 days)
    log "Removing old log files (>30 days)..."
    if [ "$DRY_RUN" -eq 0 ]; then
        find "$NOIZYLAB" -name "*.log" -mtime +30 -delete 2>/dev/null || true
        log "  ✓ Removed old log files"
    else
        local old_logs=$(find "$NOIZYLAB" -name "*.log" -mtime +30 2>/dev/null | wc -l | tr -d ' ')
        if [ "$old_logs" -gt 0 ]; then
            log "  [DRY RUN] Would remove $old_logs old log files" "$YELLOW"
        fi
    fi
    
    # Temporary files
    log "Removing temporary files..."
    if [ "$DRY_RUN" -eq 0 ]; then
        find "$NOIZYLAB" -name "*.tmp" -delete 2>/dev/null || true
        find "$NOIZYLAB" -name "*.swp" -delete 2>/dev/null || true
        find "$NOIZYLAB" -name "*.swo" -delete 2>/dev/null || true
        find "$NOIZYLAB" -name "*~" -delete 2>/dev/null || true
        log "  ✓ Removed temporary files"
    else
        log "  [DRY RUN] Would remove temporary files" "$YELLOW"
    fi
    
    log "✅ Temporary file cleanup complete"
}

# ==============================================================================
# STEP 4: ORGANIZE SCRIPTS
# ==============================================================================

organize_scripts() {
    log_header "📦 STEP 4: ORGANIZING SCRIPTS"
    
    local scripts_dir="$NOIZYLAB/scripts"
    mkdir -p "$scripts_dir"
    
    log "Finding and organizing scripts..."
    
    # Find all scripts in root
    local scripts_found=0
    
    # Shell scripts
    for script in "$NOIZYLAB"/*.sh; do
        if [ -f "$script" ]; then
            local basename=$(basename "$script")
            if [ "$basename" != "MASTER_CLEANUP_ORGANIZER.sh" ] && [ "$basename" != "media_offload.sh" ]; then
                scripts_found=$((scripts_found + 1))
                if [ "$DRY_RUN" -eq 0 ]; then
                    mv "$script" "$scripts_dir/" 2>/dev/null || true
                    log "  ✓ Moved: $basename → scripts/"
                else
                    log "  [DRY RUN] Would move: $basename → scripts/" "$YELLOW"
                fi
            fi
        fi
    done
    
    # Python scripts in root (non-project files)
    for script in "$NOIZYLAB"/*.py; do
        if [ -f "$script" ]; then
            local basename=$(basename "$script")
            scripts_found=$((scripts_found + 1))
            if [ "$DRY_RUN" -eq 0 ]; then
                mv "$script" "$scripts_dir/" 2>/dev/null || true
                log "  ✓ Moved: $basename → scripts/"
            else
                log "  [DRY RUN] Would move: $basename → scripts/" "$YELLOW"
            fi
        fi
    done
    
    if [ "$scripts_found" -eq 0 ]; then
        log "  ✓ No loose scripts found in root"
    else
        log "  ✓ Organized $scripts_found scripts"
    fi
    
    log "✅ Script organization complete"
}

# ==============================================================================
# STEP 5: ORGANIZE DOCUMENTATION
# ==============================================================================

organize_docs() {
    log_header "📄 STEP 5: ORGANIZING DOCUMENTATION"
    
    local docs_dir="$NOIZYLAB/docs"
    mkdir -p "$docs_dir"
    
    log "Finding and organizing documentation..."
    
    local docs_found=0
    
    # Move markdown files from root
    for doc in "$NOIZYLAB"/*.md; do
        if [ -f "$doc" ]; then
            local basename=$(basename "$doc")
            if [ "$basename" != "README.md" ] && [ "$basename" != "STRUCTURE.md" ]; then
                docs_found=$((docs_found + 1))
                if [ "$DRY_RUN" -eq 0 ]; then
                    mv "$doc" "$docs_dir/" 2>/dev/null || true
                    log "  ✓ Moved: $basename → docs/"
                else
                    log "  [DRY RUN] Would move: $basename → docs/" "$YELLOW"
                fi
            fi
        fi
    done
    
    if [ "$docs_found" -eq 0 ]; then
        log "  ✓ No loose documentation found in root"
    else
        log "  ✓ Organized $docs_found documentation files"
    fi
    
    log "✅ Documentation organization complete"
}

# ==============================================================================
# STEP 6: CONSOLIDATE DUPLICATE SCRIPTS
# ==============================================================================

consolidate_duplicates() {
    log_header "🔄 STEP 6: CONSOLIDATING DUPLICATE SCRIPTS"
    
    log "Identifying duplicate/versioned scripts..."
    
    # Find versioned scripts (e.g., MASTER_UPGRADE.sh, MASTER_UPGRADE_V3.sh)
    local versioned_scripts=$(find "$NOIZYLAB" -maxdepth 1 -type f \( -name "*_V*.sh" -o -name "*_v*.sh" -o -name "*_V*.py" \) 2>/dev/null)
    
    if [ -n "$versioned_scripts" ]; then
        log "Found versioned scripts:" "$YELLOW"
        echo "$versioned_scripts" | while read script; do
            log "  → $(basename "$script")" "$CYAN"
        done
        
        if [ "$DRY_RUN" -eq 0 ]; then
            local archive_dir="$NOIZYLAB/.archive/old-versions"
            mkdir -p "$archive_dir"
            
            echo "$versioned_scripts" | while read script; do
                local basename=$(basename "$script")
                mv "$script" "$archive_dir/" 2>/dev/null || true
                log "  ✓ Archived: $basename"
            done
        else
            log "  [DRY RUN] Would archive versioned scripts" "$YELLOW"
        fi
    else
        log "  ✓ No obvious duplicate scripts found"
    fi
    
    log "✅ Duplicate consolidation complete"
}

# ==============================================================================
# STEP 7: FIND LARGE MEDIA FILES
# ==============================================================================

find_large_media() {
    log_header "🎬 STEP 7: FINDING LARGE MEDIA FILES"
    
    local media_report="$LOG_DIR/large-media-${TIMESTAMP}.txt"
    
    log "Scanning for large media files (>50MB)..."
    
    # Find large media files
    find "$NOIZYLAB" -type f \( \
        -iname "*.mp4" -o -iname "*.mov" -o -iname "*.avi" -o -iname "*.mkv" -o \
        -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.heic" -o \
        -iname "*.zip" -o -iname "*.tar.gz" -o -iname "*.dmg" \
    \) -size +50M 2>/dev/null | \
        xargs ls -lh 2>/dev/null | \
        awk '{print $5, $9}' | sort -rh > "$media_report" || true
    
    local media_count=$(wc -l < "$media_report" | tr -d ' ')
    
    if [ "$media_count" -gt 0 ]; then
        log "Found $media_count large media/archive files (>50MB):" "$YELLOW"
        head -20 "$media_report" | while read size path; do
            log "  $size  →  $path" "$CYAN"
        done
        log "\nFull list saved to: $media_report"
        log "\n💡 Tip: Use media_offload.sh to move media files to external drive"
    else
        log "  ✓ No large media files found"
    fi
}

# ==============================================================================
# STEP 8: GENERATE REPORT
# ==============================================================================

generate_report() {
    log_header "📊 STEP 8: GENERATING CLEANUP REPORT"
    
    local total_size=$(du -sh "$NOIZYLAB" 2>/dev/null | awk '{print $1}')
    
    cat > "$REPORT_FILE" << EOF
# NOIZYLAB Cleanup Report
**Generated:** $(date)
**Timestamp:** $TIMESTAMP

## Summary

- **Total NOIZYLAB Size:** $total_size
- **Log File:** $LOG_FILE
- **Mode:** $([ "$DRY_RUN" -eq 1 ] && echo "DRY RUN" || echo "LIVE")

## What Was Done

1. ✅ Disk usage analysis completed
2. ✅ Duplicate files identified
3. ✅ Temporary files cleaned
4. ✅ Scripts organized
5. ✅ Documentation organized
6. ✅ Duplicate scripts consolidated
7. ✅ Large media files identified

## Next Steps

### If you found large media files:
\`\`\`bash
cd $NOIZYLAB
./media_offload.sh --audit "/Users/m2ultra" "/Volumes/12TB"
\`\`\`

### To review what was cleaned:
\`\`\`bash
cat $LOG_FILE
\`\`\`

## Recommendations

1. **Move media files** to external drive if using media_offload.sh
2. **Review archived scripts** in .archive/old-versions/ before deleting
3. **Consolidate projects** if you find duplicate project directories
4. **Archive old projects** that are no longer active

---
*Generated by MASTER_CLEANUP_ORGANIZER.sh*
EOF

    log "✅ Report generated: $REPORT_FILE"
}

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

main() {
    log_header "🚀 NOIZYLAB MASTER CLEANUP & ORGANIZER"
    log "Started at: $(date)"
    log "Mode: $([ "$DRY_RUN" -eq 1 ] && echo "DRY RUN" || echo "LIVE")"
    log "Analyze Only: $([ "$ANALYZE_ONLY" -eq 1 ] && echo "YES" || echo "NO")"
    
    # Run analysis
    analyze_disk_usage
    find_duplicates
    find_large_media
    
    # Only run cleanup if not analyze-only
    if [ "$ANALYZE_ONLY" -eq 0 ]; then
        clean_temp_files
        organize_scripts
        organize_docs
        consolidate_duplicates
    fi
    
    # Generate report
    generate_report
    
    log_header "✅ CLEANUP COMPLETE"
    log "Report saved to: $REPORT_FILE"
    log "Log saved to: $LOG_FILE"
    log "Completed at: $(date)"
    
    if [ "$DRY_RUN" -eq 1 ]; then
        log "\n⚠️  This was a DRY RUN. Run without --dry-run to apply changes." "$YELLOW"
    fi
}

# Run main
main

