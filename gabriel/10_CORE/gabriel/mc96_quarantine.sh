#!/usr/bin/env bash
# ============================================================================
# MC96 QUARANTINE MANAGER v2.0
# ============================================================================
# Safe file quarantine system - NEVER deletes, only moves
# Usage: mc96_quarantine.sh [command] [options]
# ============================================================================

set -euo pipefail

# === CONFIGURATION ===
QUARANTINE_ROOT="$HOME/MC96_Quarantine"
BATCH_SIZE=10
VERSION="2.0.0"

# === COLORS ===
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

log_info()  { echo -e "${BLUE}ℹ${NC} $1"; }
log_ok()    { echo -e "${GREEN}✅${NC} $1"; }
log_warn()  { echo -e "${YELLOW}⚠️${NC} $1"; }
log_error() { echo -e "${RED}❌${NC} $1"; }
log_step()  { echo -e "${CYAN}▶${NC} $1"; }

show_banner() {
    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║           MC96 QUARANTINE MANAGER v${VERSION}                   ║"
    echo "║            Safe File Quarantine System                       ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# === COMMANDS ===

cmd_status() {
    show_banner
    log_info "Quarantine Root: $QUARANTINE_ROOT"
    echo ""

    if [[ ! -d "$QUARANTINE_ROOT" ]]; then
        log_warn "No quarantine directory exists yet"
        return 0
    fi

    log_step "Quarantine Contents:"
    echo ""

    for batch_dir in "$QUARANTINE_ROOT"/*/; do
        [[ -d "$batch_dir" ]] || continue
        batch_name=$(basename "$batch_dir")
        file_count=$(find "$batch_dir" -type f 2>/dev/null | wc -l | tr -d ' ')
        size=$(du -sh "$batch_dir" 2>/dev/null | cut -f1)
        echo "  📁 $batch_name: $file_count files ($size)"
    done

    echo ""
    total_count=$(find "$QUARANTINE_ROOT" -type f 2>/dev/null | wc -l | tr -d ' ')
    total_size=$(du -sh "$QUARANTINE_ROOT" 2>/dev/null | cut -f1)
    log_info "Total: $total_count files ($total_size)"
}

cmd_move() {
    local src="$1"
    local reason="${2:-manual}"

    if [[ ! -e "$src" ]]; then
        log_error "File not found: $src"
        return 1
    fi

    local ts=$(date '+%Y%m%d_%H%M%S')
    local batch_dir="$QUARANTINE_ROOT/${reason}_${ts}"
    mkdir -p "$batch_dir"

    local filename=$(basename "$src")
    local dest="$batch_dir/$filename"

    # Handle name collision
    if [[ -e "$dest" ]]; then
        local hash=$(md5 -q "$src" 2>/dev/null | head -c 8)
        dest="$batch_dir/${hash}_${filename}"
    fi

    mv -v "$src" "$dest"
    log_ok "Quarantined: $src → $dest"

    # Save metadata
    echo "{\"source\": \"$src\", \"quarantined\": \"$(date -Iseconds)\", \"reason\": \"$reason\"}" > "${dest}.meta.json"
}

cmd_restore() {
    local quarantined_file="$1"

    if [[ ! -f "$quarantined_file" ]]; then
        log_error "File not found: $quarantined_file"
        return 1
    fi

    local meta_file="${quarantined_file}.meta.json"
    if [[ -f "$meta_file" ]]; then
        local original=$(jq -r '.source' "$meta_file" 2>/dev/null)
        if [[ -n "$original" && "$original" != "null" ]]; then
            local dest_dir=$(dirname "$original")
            mkdir -p "$dest_dir"
            mv -v "$quarantined_file" "$original"
            rm -f "$meta_file"
            log_ok "Restored: $original"
            return 0
        fi
    fi

    log_warn "No metadata found, restoring to Desktop"
    mv -v "$quarantined_file" "$HOME/Desktop/"
    log_ok "Restored to Desktop"
}

cmd_purge() {
    local batch="$1"
    local batch_dir="$QUARANTINE_ROOT/$batch"

    if [[ ! -d "$batch_dir" ]]; then
        log_error "Batch not found: $batch"
        return 1
    fi

    local file_count=$(find "$batch_dir" -type f -not -name '*.meta.json' | wc -l | tr -d ' ')
    local size=$(du -sh "$batch_dir" 2>/dev/null | cut -f1)

    echo ""
    log_warn "About to PERMANENTLY DELETE:"
    echo "  📁 Batch: $batch"
    echo "  📊 Files: $file_count"
    echo "  💾 Size:  $size"
    echo ""

    read -p "Type 'DELETE' to confirm: " confirm
    if [[ "$confirm" != "DELETE" ]]; then
        log_info "Cancelled"
        return 0
    fi

    rm -rf "$batch_dir"
    log_ok "Purged: $batch"
}

cmd_batch() {
    local script="$1"

    if [[ ! -f "$script" ]]; then
        log_error "Script not found: $script"
        return 1
    fi

    log_step "Processing quarantine script in batches of $BATCH_SIZE"

    # Extract move commands and process in batches
    local count=0
    local batch_count=0

    while IFS= read -r line; do
        if [[ "$line" =~ ^mv ]]; then
            ((count++))

            if ((count % BATCH_SIZE == 0)); then
                ((batch_count++))
                echo ""
                log_info "Completed batch $batch_count ($count files)"
                read -p "Continue? [Y/n] " -n 1 -r
                echo
                if [[ $REPLY =~ ^[Nn]$ ]]; then
                    log_info "Stopped at batch $batch_count"
                    return 0
                fi
            fi

            eval "$line" 2>/dev/null || log_warn "Failed: $line"
        fi
    done < "$script"

    log_ok "Completed $count moves in $((batch_count + 1)) batches"
}

cmd_help() {
    show_banner
    echo "Commands:"
    echo "  status                  Show quarantine status"
    echo "  move <file> [reason]    Quarantine a file"
    echo "  restore <file>          Restore a quarantined file"
    echo "  purge <batch>           Permanently delete a batch"
    echo "  batch <script>          Process quarantine script in batches"
    echo "  help                    Show this help"
    echo ""
    echo "Examples:"
    echo "  $0 status"
    echo "  $0 move /path/to/file duplicate"
    echo "  $0 batch quarantine_script.sh"
    echo "  $0 purge duplicate_20241227_123456"
}

# === MAIN ===
main() {
    local cmd="${1:-status}"
    shift || true

    case "$cmd" in
        status)     cmd_status ;;
        move)       cmd_move "$@" ;;
        restore)    cmd_restore "$@" ;;
        purge)      cmd_purge "$@" ;;
        batch)      cmd_batch "$@" ;;
        help|-h|--help) cmd_help ;;
        *)
            log_error "Unknown command: $cmd"
            cmd_help
            exit 1
            ;;
    esac
}

main "$@"
