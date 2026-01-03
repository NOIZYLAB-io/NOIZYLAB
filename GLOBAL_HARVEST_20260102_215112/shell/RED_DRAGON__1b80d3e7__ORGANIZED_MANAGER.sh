#!/usr/bin/env bash
# ==============================================================================
# _ORGANIZED Manager - Master Control for _ORGANIZED Directory
# ==============================================================================

ORGANIZED="/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

log() {
    echo -e "${CYAN}${1}${NC}"
}

log_header() {
    echo ""
    echo -e "${BOLD}${GREEN}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${BOLD}${CYAN}${1}${NC}"
    echo -e "${BOLD}${GREEN}═══════════════════════════════════════════════════════════${NC}"
    echo ""
}

show_menu() {
    clear
    echo "╔═══════════════════════════════════════════════════════════════╗"
    echo "║              🎯 _ORGANIZED DIRECTORY MANAGER                   ║"
    echo "╚═══════════════════════════════════════════════════════════════╝"
    echo ""
    echo "📊 ANALYSIS"
    echo "  1) Analyze Directory          - Full analysis & catalog"
    echo "  2) Find Duplicates            - Find duplicate projects"
    echo "  3) Find Large Files           - Find large files (>50MB)"
    echo "  4) Find Empty Directories     - Find empty projects"
    echo ""
    echo "🧹 CLEANUP"
    echo "  5) Remove .DS_Store           - Clean macOS files"
    echo "  6) Remove Empty Dirs          - Remove empty directories"
    echo "  7) Clean Python Cache         - Remove __pycache__"
    echo ""
    echo "📚 CATALOG"
    echo "  8) Generate Catalog           - Create project catalog"
    echo "  9) View Catalog               - View catalog JSON"
    echo "  10) Search Projects           - Search by name/language"
    echo ""
    echo "🔄 SYNC"
    echo "  11) Sync with NOIZYLAB        - Sync projects"
    echo ""
    echo "  0) Exit"
    echo ""
}

analyze_directory() {
    log_header "📊 ANALYZING _ORGANIZED DIRECTORY"
    cd "$ORGANIZED"
    python3 ANALYZE_ORGANIZED.py
}

find_duplicates() {
    log_header "🔍 FINDING DUPLICATES"
    cd "$ORGANIZED"
    python3 FIND_DUPLICATES.py
}

find_large_files() {
    log_header "📊 FINDING LARGE FILES"
    cd "$ORGANIZED"
    python3 -c "
from pathlib import Path
import os

ORGANIZED = Path('$ORGANIZED')
min_size = 50 * 1024 * 1024  # 50MB

large_files = []
for category in ORGANIZED.iterdir():
    if category.is_dir() and not category.name.startswith('.'):
        for root, dirs, files in os.walk(category):
            dirs[:] = [d for d in dirs if d not in ['node_modules', '.git']]
            for file in files:
                file_path = Path(root) / file
                try:
                    if file_path.stat().st_size >= min_size:
                        size_mb = file_path.stat().st_size / (1024 * 1024)
                        rel_path = file_path.relative_to(ORGANIZED)
                        large_files.append((size_mb, str(rel_path)))
                except:
                    pass

large_files.sort(reverse=True)
print(f'Found {len(large_files)} large files (>50MB):\n')
for size, path in large_files[:20]:
    print(f'  {size:8.1f} MB  →  {path}')
"
}

find_empty_dirs() {
    log_header "🔍 FINDING EMPTY DIRECTORIES"
    cd "$ORGANIZED"
    python3 -c "
from pathlib import Path

ORGANIZED = Path('$ORGANIZED')
empty = []

for category in ORGANIZED.iterdir():
    if category.is_dir() and not category.name.startswith('.'):
        for project in category.iterdir():
            if project.is_dir():
                items = list(project.iterdir())
                if not items or all(item.name in ['.git', '.DS_Store'] for item in items):
                    empty.append(f'{category.name}/{project.name}')

if empty:
    print(f'Found {len(empty)} empty directories:\n')
    for path in empty:
        print(f'  📁 {path}')
else:
    print('✅ No empty directories found!')
"
}

remove_dsstore() {
    log_header "🧹 REMOVING .DS_Store FILES"
    cd "$ORGANIZED"
    count=$(find . -name ".DS_Store" -type f | wc -l | tr -d ' ')
    if [ "$count" -gt 0 ]; then
        find . -name ".DS_Store" -type f -delete
        log "✅ Removed $count .DS_Store files"
    else
        log "✅ No .DS_Store files found"
    fi
}

remove_empty_dirs() {
    log_header "🧹 REMOVING EMPTY DIRECTORIES"
    cd "$ORGANIZED"
    read -p "Are you sure? This will remove empty project directories (y/N): " confirm
    if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
        python3 -c "
from pathlib import Path

ORGANIZED = Path('$ORGANIZED')
removed = []

for category in ORGANIZED.iterdir():
    if category.is_dir() and not category.name.startswith('.'):
        for project in category.iterdir():
            if project.is_dir():
                items = list(project.iterdir())
                if not items or all(item.name in ['.git', '.DS_Store', '.gitignore'] for item in items):
                    removed.append(str(project.relative_to(ORGANIZED)))
                    import shutil
                    shutil.rmtree(project, ignore_errors=True)

print(f'Removed {len(removed)} empty directories')
for path in removed[:10]:
    print(f'  ✓ {path}')
"
    else
        log "Cancelled"
    fi
}

clean_pycache() {
    log_header "🧹 CLEANING PYTHON CACHE"
    cd "$ORGANIZED"
    count=$(find . -type d -name "__pycache__" | wc -l | tr -d ' ')
    if [ "$count" -gt 0 ]; then
        find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
        find . -name "*.pyc" -delete 2>/dev/null || true
        log "✅ Removed Python cache (__pycache__ directories)"
    else
        log "✅ No Python cache found"
    fi
}

generate_catalog() {
    log_header "📚 GENERATING CATALOG"
    cd "$ORGANIZED"
    python3 ANALYZE_ORGANIZED.py
}

view_catalog() {
    log_header "📚 VIEWING CATALOG"
    if [ -f "$ORGANIZED/.catalog.json" ]; then
        python3 -m json.tool "$ORGANIZED/.catalog.json" | less
    else
        log "❌ Catalog not found. Run 'Generate Catalog' first."
    fi
}

search_projects() {
    log_header "🔍 SEARCH PROJECTS"
    read -p "Enter search term (project name or language): " search_term
    cd "$ORGANIZED"
    
    if [ -f ".catalog.json" ]; then
        python3 -c "
import json
import sys

with open('.catalog.json') as f:
    catalog = json.load(f)

term = '$search_term'.lower()
found = []

for name, info in catalog.get('projects', {}).items():
    if term in name.lower() or term in info.get('main_language', '').lower():
        found.append((name, info))

if found:
    print(f'Found {len(found)} projects:\n')
    for name, info in found[:20]:
        print(f'  📦 {name}')
        print(f'      Category: {info[\"category\"]}')
        print(f'      Language: {info.get(\"main_language\", \"Unknown\")}')
        print(f'      Files: {info[\"file_count\"]:,}')
        print(f'      Size: {info[\"size_formatted\"]}')
        print()
else:
    print('No projects found')
"
    else
        log "❌ Catalog not found. Run 'Generate Catalog' first."
    fi
}

sync_with_noizylab() {
    log_header "🔄 SYNC WITH NOIZYLAB"
    log "This would sync projects between _ORGANIZED and NOIZYLAB"
    log "Feature coming soon..."
}

main() {
    cd "$ORGANIZED"
    
    # Check if directory exists
    if [ ! -d "$ORGANIZED" ]; then
        echo "❌ _ORGANIZED directory not found: $ORGANIZED"
        exit 1
    fi
    
    # If argument provided, run directly
    if [ $# -gt 0 ]; then
        case "$1" in
            analyze|1) analyze_directory ;;
            duplicates|2) find_duplicates ;;
            large|3) find_large_files ;;
            empty|4) find_empty_dirs ;;
            dsstore|5) remove_dsstore ;;
            clean|6) remove_empty_dirs ;;
            pycache|7) clean_pycache ;;
            catalog|8) generate_catalog ;;
            view|9) view_catalog ;;
            search|10) search_projects ;;
            sync|11) sync_with_noizylab ;;
            *) echo "Unknown command: $1. Run without args for menu." ;;
        esac
        return
    fi
    
    # Interactive menu
    while true; do
        show_menu
        read -p "Select option: " choice
        echo ""
        
        case "$choice" in
            1) analyze_directory ;;
            2) find_duplicates ;;
            3) find_large_files ;;
            4) find_empty_dirs ;;
            5) remove_dsstore ;;
            6) remove_empty_dirs ;;
            7) clean_pycache ;;
            8) generate_catalog ;;
            9) view_catalog ;;
            10) search_projects ;;
            11) sync_with_noizylab ;;
            0|q|exit) echo "👋 Goodbye!"; exit 0 ;;
            *) echo "❌ Invalid option" ;;
        esac
        
        echo ""
        read -p "Press Enter to continue..."
    done
}

main "$@"

