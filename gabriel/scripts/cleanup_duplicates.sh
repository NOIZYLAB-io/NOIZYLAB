#!/bin/bash
#===============================================================================
# GABRIEL Repository Cleanup & Organization Script
# 
# This script performs a complete reorganization of the GABRIEL repository:
# 1. Removes duplicate files (-2, -3, -4 suffixes)
# 2. Moves UUID-based agent files to archive
# 3. Consolidates valid agents into src/agents/
# 4. Cleans up legacy directories
#
# Author: NOIZYLAB Automation
# Date: January 2, 2026
# Branch: 3-set-up-copilot-instructions
#===============================================================================

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
GABRIEL_ROOT="${GABRIEL_ROOT:-/Users/m2ultra/NOIZYLAB/GABRIEL}"
DRY_RUN="${DRY_RUN:-false}"
VERBOSE="${VERBOSE:-false}"

# Counters
DELETED_COUNT=0
MOVED_COUNT=0
ARCHIVED_COUNT=0

#-------------------------------------------------------------------------------
# Logging functions
#-------------------------------------------------------------------------------
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_action() {
    echo -e "${PURPLE}[ACTION]${NC} $1"
}

#-------------------------------------------------------------------------------
# Helper functions
#-------------------------------------------------------------------------------
safe_delete() {
    local file="$1"
    if [[ "$DRY_RUN" == "true" ]]; then
        log_action "[DRY RUN] Would delete: $file"
    else
        rm -f "$file"
        ((DELETED_COUNT++)) || true
        [[ "$VERBOSE" == "true" ]] && log_info "Deleted: $file"
    fi
}

safe_move() {
    local src="$1"
    local dest="$2"
    local dest_dir
    dest_dir=$(dirname "$dest")
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_action "[DRY RUN] Would move: $src -> $dest"
    else
        mkdir -p "$dest_dir"
        mv "$src" "$dest"
        ((MOVED_COUNT++)) || true
        [[ "$VERBOSE" == "true" ]] && log_info "Moved: $src -> $dest"
    fi
}

safe_archive() {
    local src="$1"
    local dest="$GABRIEL_ROOT/archive/legacy/$(basename "$src")"
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_action "[DRY RUN] Would archive: $src"
    else
        mkdir -p "$GABRIEL_ROOT/archive/legacy"
        mv "$src" "$dest"
        ((ARCHIVED_COUNT++)) || true
        [[ "$VERBOSE" == "true" ]] && log_info "Archived: $src"
    fi
}

#-------------------------------------------------------------------------------
# Phase 1: Remove duplicate files with -N suffixes
#-------------------------------------------------------------------------------
cleanup_duplicate_suffixes() {
    log_info "=== Phase 1: Cleaning duplicate suffix files (-2, -3, -4, etc.) ==="
    
    local target_dir="$GABRIEL_ROOT/11_AGENTS"
    
    if [[ ! -d "$target_dir" ]]; then
        log_warning "Directory not found: $target_dir"
        return
    fi
    
    # Find and delete files with -2, -3, -4, etc. suffixes before extension
    # Pattern: filename-N.ext where N is a digit
    find "$target_dir" -type f -name "*-[0-9].*" -print0 | while IFS= read -r -d '' file; do
        safe_delete "$file"
    done
    
    # Also handle -N-N patterns (e.g., -2-3)
    find "$target_dir" -type f -name "*-[0-9]-[0-9].*" -print0 | while IFS= read -r -d '' file; do
        safe_delete "$file"
    done
    
    log_success "Phase 1 complete: Duplicate suffix cleanup"
}

#-------------------------------------------------------------------------------
# Phase 2: Archive UUID-named agent files
#-------------------------------------------------------------------------------
archive_uuid_files() {
    log_info "=== Phase 2: Archiving UUID-named agent files ==="
    
    local target_dir="$GABRIEL_ROOT/11_AGENTS"
    local archive_dir="$GABRIEL_ROOT/archive/legacy/uuid_agents"
    
    if [[ ! -d "$target_dir" ]]; then
        log_warning "Directory not found: $target_dir"
        return
    fi
    
    mkdir -p "$archive_dir"
    
    # UUID pattern: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx-agent-*
    find "$target_dir" -type f -name "*-agent-*.json" -print0 | while IFS= read -r -d '' file; do
        local filename
        filename=$(basename "$file")
        
        if [[ "$DRY_RUN" == "true" ]]; then
            log_action "[DRY RUN] Would archive UUID file: $filename"
        else
            mv "$file" "$archive_dir/"
            ((ARCHIVED_COUNT++)) || true
        fi
    done
    
    log_success "Phase 2 complete: UUID files archived"
}

#-------------------------------------------------------------------------------
# Phase 3: Consolidate named agents
#-------------------------------------------------------------------------------
consolidate_named_agents() {
    log_info "=== Phase 3: Consolidating named agents ==="
    
    local source_dir="$GABRIEL_ROOT/11_AGENTS"
    local fleet_dir="$GABRIEL_ROOT/src/agents/fleet"
    
    # Named agents to extract (these are the real agents)
    declare -a NAMED_AGENTS=(
        "POPS"
        "SHIRL"
        "ENGR_KEITH"
        "DREAM"
        "GABRIEL"
        "ALEX_WARD"
        "WARDIE"
        "LUCY"
        "FLEET"
    )
    
    mkdir -p "$fleet_dir"
    
    for agent_name in "${NAMED_AGENTS[@]}"; do
        local agent_lower
        agent_lower=$(echo "$agent_name" | tr '[:upper:]' '[:lower:]')
        local agent_dir="$fleet_dir/$agent_lower"
        
        mkdir -p "$agent_dir"
        
        # Find original agent files (no -N suffix)
        if [[ -f "$source_dir/AGENT_${agent_name}.sh" ]]; then
            safe_move "$source_dir/AGENT_${agent_name}.sh" "$agent_dir/${agent_lower}.sh"
        fi
        
        # Move any related MD files
        if [[ -f "$source_dir/${agent_name}_AGENT.md" ]]; then
            safe_move "$source_dir/${agent_name}_AGENT.md" "$agent_dir/README.md"
        fi
    done
    
    log_success "Phase 3 complete: Named agents consolidated"
}

#-------------------------------------------------------------------------------
# Phase 4: Move brain modules
#-------------------------------------------------------------------------------
consolidate_brain_modules() {
    log_info "=== Phase 4: Consolidating brain modules ==="
    
    local source_dir="$GABRIEL_ROOT/11_AGENTS"
    local brain_dir="$GABRIEL_ROOT/src/agents/brain"
    
    mkdir -p "$brain_dir"
    
    # Move brain-related files (original versions only)
    find "$source_dir" -maxdepth 1 -type f \( -name "brain*.py" -o -name "brain*.json" -o -name "brain*.js" \) ! -name "*-[0-9].*" -print0 | while IFS= read -r -d '' file; do
        local filename
        filename=$(basename "$file")
        safe_move "$file" "$brain_dir/$filename"
    done
    
    log_success "Phase 4 complete: Brain modules consolidated"
}

#-------------------------------------------------------------------------------
# Phase 5: Move configuration files
#-------------------------------------------------------------------------------
consolidate_configs() {
    log_info "=== Phase 5: Consolidating configuration files ==="
    
    local source_dir="$GABRIEL_ROOT/11_AGENTS"
    local config_dir="$GABRIEL_ROOT/src/agents/configs"
    
    mkdir -p "$config_dir"
    
    # Move agent config files (original versions only)
    find "$source_dir" -maxdepth 1 -type f -name "agent_config*.py" ! -name "*-[0-9].*" -print0 | while IFS= read -r -d '' file; do
        local filename
        filename=$(basename "$file")
        safe_move "$file" "$config_dir/$filename"
    done
    
    # Move fleet_agents.json
    if [[ -f "$source_dir/fleet_agents.json" ]]; then
        safe_move "$source_dir/fleet_agents.json" "$config_dir/fleet_agents.json"
    fi
    
    log_success "Phase 5 complete: Configs consolidated"
}

#-------------------------------------------------------------------------------
# Phase 6: Archive remaining 11_AGENTS content
#-------------------------------------------------------------------------------
archive_remaining() {
    log_info "=== Phase 6: Archiving remaining 11_AGENTS content ==="
    
    local source_dir="$GABRIEL_ROOT/11_AGENTS"
    local archive_dir="$GABRIEL_ROOT/archive/legacy/11_AGENTS_backup"
    
    if [[ ! -d "$source_dir" ]]; then
        log_warning "Source directory already cleaned: $source_dir"
        return
    fi
    
    # Count remaining files
    local remaining
    remaining=$(find "$source_dir" -type f | wc -l | tr -d ' ')
    
    if [[ "$remaining" -gt 0 ]]; then
        log_info "Archiving $remaining remaining files..."
        
        if [[ "$DRY_RUN" == "true" ]]; then
            log_action "[DRY RUN] Would archive entire 11_AGENTS to: $archive_dir"
        else
            mkdir -p "$archive_dir"
            mv "$source_dir"/* "$archive_dir/" 2>/dev/null || true
            log_success "Remaining files archived to: $archive_dir"
        fi
    fi
    
    log_success "Phase 6 complete: Remaining content archived"
}

#-------------------------------------------------------------------------------
# Phase 7: Clean up legacy directories
#-------------------------------------------------------------------------------
cleanup_legacy_dirs() {
    log_info "=== Phase 7: Cleaning legacy numbered directories ==="
    
    # Directories to potentially archive
    declare -a LEGACY_DIRS=(
        "00_CONTROL_PLANE"
        "10_CORE"
        "11_AGENTS"
        "12_MCP"
        "ANTIGRAVITY_COMPLETE"
        "CODE"
        "CODEMASTER"
    )
    
    for dir_name in "${LEGACY_DIRS[@]}"; do
        local dir_path="$GABRIEL_ROOT/$dir_name"
        
        if [[ -d "$dir_path" ]]; then
            local file_count
            file_count=$(find "$dir_path" -type f | wc -l | tr -d ' ')
            
            if [[ "$file_count" -eq 0 ]]; then
                if [[ "$DRY_RUN" == "true" ]]; then
                    log_action "[DRY RUN] Would remove empty directory: $dir_path"
                else
                    rmdir "$dir_path" 2>/dev/null || log_warning "Could not remove: $dir_path (may not be empty)"
                fi
            else
                log_info "Directory $dir_name has $file_count files - preserving for manual review"
            fi
        fi
    done
    
    log_success "Phase 7 complete: Legacy directories processed"
}

#-------------------------------------------------------------------------------
# Phase 8: Create directory structure index
#-------------------------------------------------------------------------------
create_structure_index() {
    log_info "=== Phase 8: Creating structure index ==="
    
    local index_file="$GABRIEL_ROOT/docs/STRUCTURE.md"
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_action "[DRY RUN] Would create structure index: $index_file"
        return
    fi
    
    cat > "$index_file" << 'EOF'
# GABRIEL Repository Structure

> Auto-generated on $(date +"%Y-%m-%d %H:%M:%S")

## 📁 Directory Layout

```
GABRIEL/
├── .github/                    # GitHub configuration
│   └── copilot-instructions.md # AI coding guidelines
│
├── src/                        # Source code
│   ├── core/                   # Gabriel core system
│   ├── agents/                 # AI agent system
│   │   ├── fleet/              # Named agents (POPS, SHIRL, etc.)
│   │   ├── configs/            # Agent configuration files
│   │   └── brain/              # AI brain modules
│   ├── mcp/                    # MCP server implementations
│   │   └── servers/
│   └── workers/                # Cloudflare workers
│
├── scripts/                    # Shell/automation scripts
│   ├── deploy/                 # Deployment scripts
│   ├── maintenance/            # Maintenance scripts
│   └── setup/                  # Setup scripts
│
├── config/                     # Configuration files
│   └── machines.json
│
├── tools/                      # Standalone tools
│   └── claude-voice-pack/
│
├── infrastructure/             # Infrastructure as code
│   └── cloudflare/
│
├── docs/                       # Documentation
│   ├── architecture/           # System architecture
│   └── agents/                 # Agent documentation
│
├── archive/                    # Historical/deprecated code
│   └── legacy/
│
├── logs/                       # Runtime logs (gitignored)
├── memory/                     # Agent memory (gitignored)
│
├── package.json
├── README.md
└── GABRIEL.code-workspace
```

## 🤖 Agent Fleet

| Agent | Location | Purpose |
|-------|----------|---------|
| POPS | `src/agents/fleet/pops/` | Creative direction |
| SHIRL | `src/agents/fleet/shirl/` | Business operations |
| ENGR_KEITH | `src/agents/fleet/engr_keith/` | Technical engineering |
| DREAM | `src/agents/fleet/dream/` | Visionary planning |
| GABRIEL | `src/core/` | System bridge |

## 📝 Notes

- Legacy code archived in `archive/legacy/`
- UUID-based agent files in `archive/legacy/uuid_agents/`
- Original `11_AGENTS` backup in `archive/legacy/11_AGENTS_backup/`
EOF

    log_success "Structure index created: $index_file"
}

#-------------------------------------------------------------------------------
# Main execution
#-------------------------------------------------------------------------------
main() {
    echo ""
    echo -e "${CYAN}╔═══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║       GABRIEL Repository Cleanup & Organization Script        ║${NC}"
    echo -e "${CYAN}║                     NOIZYLAB Automation                        ║${NC}"
    echo -e "${CYAN}╚═══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    log_info "Working directory: $GABRIEL_ROOT"
    log_info "Dry run mode: $DRY_RUN"
    log_info "Verbose mode: $VERBOSE"
    echo ""
    
    # Verify we're in the right place
    if [[ ! -f "$GABRIEL_ROOT/GABRIEL.code-workspace" ]]; then
        log_error "Not in GABRIEL repository! Expected GABRIEL.code-workspace in: $GABRIEL_ROOT"
        exit 1
    fi
    
    # Run all phases
    cleanup_duplicate_suffixes
    archive_uuid_files
    consolidate_named_agents
    consolidate_brain_modules
    consolidate_configs
    archive_remaining
    cleanup_legacy_dirs
    create_structure_index
    
    # Summary
    echo ""
    echo -e "${GREEN}╔═══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                        SUMMARY                                 ║${NC}"
    echo -e "${GREEN}╠═══════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${GREEN}║  Files deleted:  ${DELETED_COUNT}${NC}"
    echo -e "${GREEN}║  Files moved:    ${MOVED_COUNT}${NC}"
    echo -e "${GREEN}║  Files archived: ${ARCHIVED_COUNT}${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_warning "This was a DRY RUN. No changes were made."
        log_info "To execute for real, run: DRY_RUN=false $0"
    else
        log_success "Cleanup complete! Review the archive/ directory for backed up files."
        log_info "Run 'git status' to see all changes."
    fi
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        --help|-h)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --dry-run    Show what would be done without making changes"
            echo "  --verbose    Show detailed output"
            echo "  --help       Show this help message"
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

main "$@"
