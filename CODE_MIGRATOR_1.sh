#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
#                    CODE MIGRATOR - ORIGINALS TO GITHUB
#                      Moves Files + Creates Aliases
#                           GORUNFREE STYLE
# ═══════════════════════════════════════════════════════════════════════════════
#
# This script:
#   1. Scans /Users/m2ultra for all code
#   2. MOVES originals to ~/NOIZYLAB (git repo)
#   3. Creates ALIASES (symlinks) in original locations
#   4. Pushes to github.com/Noizyfish/NOIZYLAB
#
# Result: Code lives in GitHub, aliases point back so nothing breaks!
#
# Usage: ./CODE_MIGRATOR.sh [scan|migrate|push|full]
# ═══════════════════════════════════════════════════════════════════════════════

set -e

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

SEARCH_ROOT="/Users/m2ultra"
REPO_DIR="$HOME/NOIZYLAB"
GITHUB_REPO="https://github.com/Noizyfish/NOIZYLAB.git"
CATALOG_FILE="$HOME/CODE_CATALOG.txt"
MIGRATION_LOG="$HOME/MIGRATION_LOG.txt"

# Code extensions
CODE_EXTENSIONS="py js ts jsx tsx mjs sh bash zsh ps1 bat cmd html css scss json yaml yml toml md swift applescript scpt sql"

# Skip these directories
SKIP_PATTERN="node_modules|\.git|__pycache__|venv|\.venv|Library|Applications|\.Trash|Movies|Music|Pictures|\.cache|Caches"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

# ─────────────────────────────────────────────────────────────────────────────
# FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

print_banner() {
    echo ""
    echo -e "${MAGENTA}╔═══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${MAGENTA}║${NC}            ${GREEN}CODE MIGRATOR - GITHUB + ALIASES${NC}                 ${MAGENTA}║${NC}"
    echo -e "${MAGENTA}║${NC}         ${CYAN}Originals to GitHub, Aliases Stay${NC}                   ${MAGENTA}║${NC}"
    echo -e "${MAGENTA}╚═══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

cmd_scan() {
    print_banner
    echo -e "${YELLOW}⚡ SCANNING: $SEARCH_ROOT${NC}"
    echo ""
    
    > "$CATALOG_FILE"
    
    # Build find command for all code extensions
    FIND_ARGS=""
    for ext in $CODE_EXTENSIONS; do
        if [ -z "$FIND_ARGS" ]; then
            FIND_ARGS="-name \"*.$ext\""
        else
            FIND_ARGS="$FIND_ARGS -o -name \"*.$ext\""
        fi
    done
    
    # Find all code files, excluding junk directories
    echo "Searching for code files..."
    eval "find \"$SEARCH_ROOT\" -type f \\( $FIND_ARGS \\) 2>/dev/null" | \
        grep -Ev "$SKIP_PATTERN" > "$CATALOG_FILE" || true
    
    TOTAL=$(wc -l < "$CATALOG_FILE" | tr -d ' ')
    
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}SCAN COMPLETE: $TOTAL code files found${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    
    # Show breakdown
    echo -e "${CYAN}By extension:${NC}"
    for ext in py js sh ps1 md json html css ts yaml swift; do
        count=$(grep -c "\.$ext$" "$CATALOG_FILE" 2>/dev/null || echo "0")
        [ "$count" -gt 0 ] && printf "  .%-8s %5s files\n" "$ext" "$count"
    done
    
    echo ""
    echo -e "${CYAN}Top 15 directories:${NC}"
    cat "$CATALOG_FILE" | xargs -I{} dirname {} 2>/dev/null | sort | uniq -c | sort -rn | head -15
    
    echo ""
    echo "Catalog saved: $CATALOG_FILE"
    echo ""
    echo -e "${YELLOW}Run './CODE_MIGRATOR.sh migrate' to move files + create aliases${NC}"
}

cmd_migrate() {
    print_banner
    echo -e "${YELLOW}⚡ MIGRATING: Move Originals + Create Aliases${NC}"
    echo ""
    
    if [ ! -f "$CATALOG_FILE" ]; then
        echo -e "${RED}ERROR: Run './CODE_MIGRATOR.sh scan' first${NC}"
        exit 1
    fi
    
    # Setup repo
    mkdir -p "$REPO_DIR"
    cd "$REPO_DIR"
    
    if [ ! -d ".git" ]; then
        git init
        git remote add origin "$GITHUB_REPO" 2>/dev/null || true
    fi
    
    # Create structure
    mkdir -p {cloudflare/workers,agents,scripts/{mac,windows},configs,docs,projects,collected}
    
    # Create .gitignore
    cat > .gitignore << 'EOF'
# Audio/Video
*.wav
*.mp3
*.aif
*.aiff
*.flac
*.m4a
*.mov
*.mp4
*.avi
*.mkv
*.m4v

# DAW
*.logicx
*.ptx
*.als
*.band

# System
.DS_Store
Thumbs.db
*.log

# Deps
node_modules/
__pycache__/
*.pyc
venv/
.env
EOF
    
    # Clear migration log
    > "$MIGRATION_LOG"
    echo "# Migration Log - $(date)" >> "$MIGRATION_LOG"
    echo "# Original Location -> Repo Location" >> "$MIGRATION_LOG"
    echo "" >> "$MIGRATION_LOG"
    
    MIGRATED=0
    SKIPPED=0
    
    echo "Migrating files..."
    echo ""
    
    while IFS= read -r original_path; do
        if [ ! -f "$original_path" ]; then
            continue
        fi
        
        # Skip if already a symlink
        if [ -L "$original_path" ]; then
            ((SKIPPED++))
            continue
        fi
        
        # Skip if in NOIZYLAB repo already
        if [[ "$original_path" == "$REPO_DIR"* ]]; then
            continue
        fi
        
        filename=$(basename "$original_path")
        ext="${filename##*.}"
        
        # Determine destination folder
        case "$ext" in
            js|mjs|ts|jsx|tsx)
                if grep -q "addEventListener.*fetch\|export default" "$original_path" 2>/dev/null; then
                    dest_dir="cloudflare/workers"
                else
                    dest_dir="projects"
                fi
                ;;
            py) dest_dir="projects" ;;
            sh|bash|zsh) dest_dir="scripts/mac" ;;
            ps1|bat|cmd) dest_dir="scripts/windows" ;;
            md)
                if echo "$filename" | grep -qiE "agent|shirl|pops|engr|dream|gabriel"; then
                    dest_dir="agents"
                else
                    dest_dir="docs"
                fi
                ;;
            json|yaml|yml|toml) dest_dir="configs" ;;
            *) dest_dir="collected" ;;
        esac
        
        dest_path="$REPO_DIR/$dest_dir/$filename"
        
        # Handle duplicates
        if [ -f "$dest_path" ]; then
            base="${filename%.*}"
            counter=1
            while [ -f "$REPO_DIR/$dest_dir/${base}_${counter}.$ext" ]; do
                ((counter++))
            done
            dest_path="$REPO_DIR/$dest_dir/${base}_${counter}.$ext"
        fi
        
        # MOVE the original to repo
        mv "$original_path" "$dest_path" 2>/dev/null || {
            # If move fails, try copy then delete
            cp "$original_path" "$dest_path" 2>/dev/null && rm "$original_path" 2>/dev/null
        }
        
        if [ -f "$dest_path" ]; then
            # CREATE ALIAS (symlink) in original location
            ln -sf "$dest_path" "$original_path" 2>/dev/null
            
            # Log it
            echo "$original_path -> $dest_path" >> "$MIGRATION_LOG"
            
            ((MIGRATED++))
            
            # Progress indicator
            if [ $((MIGRATED % 50)) -eq 0 ]; then
                echo -e "  ${GREEN}✓${NC} Migrated $MIGRATED files..."
            fi
        fi
        
    done < "$CATALOG_FILE"
    
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}MIGRATION COMPLETE${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo "  Files migrated: $MIGRATED"
    echo "  Skipped (already aliases): $SKIPPED"
    echo "  Migration log: $MIGRATION_LOG"
    echo "  Repository: $REPO_DIR"
    echo ""
    
    # Show repo structure
    echo -e "${CYAN}Repository structure:${NC}"
    find "$REPO_DIR" -type f -not -path "*/.git/*" | wc -l | xargs -I{} echo "  Total files: {}"
    echo ""
    
    echo -e "${YELLOW}Run './CODE_MIGRATOR.sh push' to upload to GitHub${NC}"
}

cmd_push() {
    print_banner
    echo -e "${YELLOW}⚡ PUSHING TO GITHUB${NC}"
    echo ""
    
    cd "$REPO_DIR"
    
    # Stage everything
    git add -A
    
    # Show status
    CHANGES=$(git status -s | wc -l | tr -d ' ')
    echo "Changes to commit: $CHANGES files"
    git status -s | head -20
    [ "$CHANGES" -gt 20 ] && echo "... and $((CHANGES - 20)) more"
    echo ""
    
    # Commit
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M")
    git commit -m "⚡ CODE MIGRATOR: Full migration from GOD @ $TIMESTAMP

Originals moved to repo, aliases created in original locations.
Fish Music Inc • MC96ECOUNIVERSE • GORUNFREE" || echo "Nothing new to commit"
    
    # Push
    echo ""
    echo "Pushing to GitHub..."
    git branch -M main
    git push -u origin main --force
    
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✓ PUSHED TO GITHUB${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo "  Repository: https://github.com/Noizyfish/NOIZYLAB"
    echo ""
    echo "  ✓ Originals now in GitHub"
    echo "  ✓ Aliases in original locations still work"
    echo ""
}

cmd_full() {
    cmd_scan
    echo ""
    read -p "Press Enter to MIGRATE (move + create aliases), Ctrl+C to cancel..."
    cmd_migrate
    echo ""
    read -p "Press Enter to PUSH to GitHub, Ctrl+C to cancel..."
    cmd_push
}

cmd_undo() {
    print_banner
    echo -e "${YELLOW}⚡ UNDO: Restore originals from aliases${NC}"
    echo ""
    
    if [ ! -f "$MIGRATION_LOG" ]; then
        echo -e "${RED}No migration log found${NC}"
        exit 1
    fi
    
    RESTORED=0
    while IFS=' -> ' read -r original repo_file; do
        # Skip comments
        [[ "$original" == \#* ]] && continue
        [ -z "$original" ] && continue
        
        # If original is now a symlink, restore
        if [ -L "$original" ] && [ -f "$repo_file" ]; then
            rm "$original"
            mv "$repo_file" "$original"
            ((RESTORED++))
        fi
    done < "$MIGRATION_LOG"
    
    echo "Restored $RESTORED files"
}

# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

case "${1:-help}" in
    scan|s) cmd_scan ;;
    migrate|m) cmd_migrate ;;
    push|p) cmd_push ;;
    full|f) cmd_full ;;
    undo|u) cmd_undo ;;
    *)
        print_banner
        echo "Usage: $0 [command]"
        echo ""
        echo "Commands:"
        echo "  scan     - Find all code files in /Users/m2ultra"
        echo "  migrate  - MOVE originals to ~/NOIZYLAB + create aliases"
        echo "  push     - Push repo to GitHub"
        echo "  full     - Do everything: scan → migrate → push"
        echo "  undo     - Restore originals from aliases"
        echo ""
        echo "GORUNFREE: ./CODE_MIGRATOR.sh full"
        echo ""
        ;;
esac
