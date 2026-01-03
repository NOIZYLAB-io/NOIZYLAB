#!/usr/bin/env bash
# ============================================================================
# MC96 TRUTH SCANNER v2.0 - With Tailscale Integration
# ============================================================================
# Scans directories, generates checksums, and syncs via Tailscale
# Usage: mc96_truth_scanner.sh [--sync] [--roots "dir1 dir2"]
# ============================================================================

set -euo pipefail

# === CONFIGURATION ===
VERSION="2.0.0"
SCRIPT_NAME="mc96_truth_scanner"

# Default scan roots - override with --roots
DEFAULT_ROOTS=(
  "$HOME/NOIZYLAB"
  "$HOME/Documents"
  "$HOME/Desktop"
)

# Output directory
OUT_DIR="$HOME/MC96_TruthScans"

# Tailscale settings
TAILSCALE_SYNC_TARGET=""  # Set to tailscale hostname to enable sync
TAILSCALE_SYNC_PATH="/MC96_TruthScans"

# === COLORS ===
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# === FUNCTIONS ===
log_info()  { echo -e "${BLUE}ℹ${NC} $1"; }
log_ok()    { echo -e "${GREEN}✅${NC} $1"; }
log_warn()  { echo -e "${YELLOW}⚠️${NC} $1"; }
log_error() { echo -e "${RED}❌${NC} $1"; }
log_step()  { echo -e "${CYAN}▶${NC} $1"; }

show_banner() {
    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║           MC96 TRUTH SCANNER v${VERSION}                        ║"
    echo "║        File Integrity & Deduplication System                 ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

check_tailscale() {
    if command -v tailscale &> /dev/null; then
        TS_STATUS=$(tailscale status --json 2>/dev/null | jq -r '.Self.Online // false' 2>/dev/null || echo "false")
        if [[ "$TS_STATUS" == "true" ]]; then
            TS_IP=$(tailscale ip -4 2>/dev/null || echo "unknown")
            TS_HOSTNAME=$(tailscale status --json 2>/dev/null | jq -r '.Self.HostName // "unknown"' 2>/dev/null)
            log_ok "Tailscale connected: ${TS_HOSTNAME} (${TS_IP})"
            return 0
        fi
    fi
    log_warn "Tailscale not connected - sync disabled"
    return 1
}

install_tailscale() {
    log_step "Installing Tailscale..."
    if [[ "$(uname)" == "Darwin" ]]; then
        if command -v brew &> /dev/null; then
            brew install tailscale
            log_ok "Tailscale installed via Homebrew"
            log_info "Run: sudo tailscaled & tailscale up"
        else
            log_error "Homebrew not found. Install from: https://tailscale.com/download"
            return 1
        fi
    else
        curl -fsSL https://tailscale.com/install.sh | sh
    fi
}

scan_directory() {
    local ROOT="$1"
    local REPORT="$2"
    local ERR_LOG="$3"
    local HOST="$4"
    local count=0
    local errors=0

    log_step "Scanning: $ROOT"

    if [[ ! -e "$ROOT" ]]; then
        echo "SKIP missing: $ROOT" >> "$ERR_LOG"
        log_warn "Directory missing: $ROOT"
        return
    fi

    while IFS= read -r -d '' f; do
        # Get file stats
        st="$(stat -f $'%N\t%z\t%Sm\t%p\t%Su\t%Sg' -t '%Y-%m-%d %H:%M:%S' "$f" 2>>"$ERR_LOG" || true)"
        if [[ -z "$st" ]]; then
            echo "STAT_FAIL	$ROOT	$f" >> "$ERR_LOG"
            ((errors++))
            continue
        fi

        # Calculate SHA256
        h="$(shasum -a 256 "$f" 2>>"$ERR_LOG" | awk '{print $1}' || true)"
        if [[ -z "$h" ]]; then
            echo "HASH_FAIL	$ROOT	$f" >> "$ERR_LOG"
            ((errors++))
            continue
        fi

        # Parse stats and write record
        IFS=$'\t' read -r p size mtime mode user group <<< "$st"
        printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" \
            "$HOST" "$ROOT" "$p" "$size" "$mtime" "$mode" "$user" "$group" "$h" >> "$REPORT"

        ((count++))

        # Progress indicator every 100 files
        if ((count % 100 == 0)); then
            echo -ne "\r${CYAN}▶${NC} Processed: $count files..."
        fi
    done < <(find "$ROOT" -xdev -type f -print0 2>>"$ERR_LOG")

    echo -ne "\r"
    log_ok "Scanned $count files from $ROOT (errors: $errors)"
}

sync_to_tailscale() {
    local REPORT="$1"
    local TARGET="$2"

    if [[ -z "$TARGET" ]]; then
        log_warn "No Tailscale sync target configured"
        return 1
    fi

    log_step "Syncing to Tailscale: $TARGET"

    # Use rsync over Tailscale
    if rsync -avz --progress \
        "$OUT_DIR/" \
        "${TARGET}:${TAILSCALE_SYNC_PATH}/" 2>/dev/null; then
        log_ok "Synced to $TARGET"
    else
        log_error "Sync failed to $TARGET"
        return 1
    fi
}

generate_summary() {
    local REPORT="$1"
    local SUMMARY="${REPORT%.tsv}_summary.txt"

    log_step "Generating summary..."

    {
        echo "═══════════════════════════════════════════════════════════════"
        echo "MC96 TRUTH SCANNER SUMMARY"
        echo "═══════════════════════════════════════════════════════════════"
        echo "Report: $(basename "$REPORT")"
        echo "Generated: $(date)"
        echo "Host: $(scutil --get ComputerName 2>/dev/null || hostname)"
        echo ""
        echo "STATISTICS:"
        echo "───────────────────────────────────────────────────────────────"
        echo "Total files: $(tail -n +2 "$REPORT" | wc -l | tr -d ' ')"
        echo "Total size: $(tail -n +2 "$REPORT" | awk -F'\t' '{sum+=$4} END {printf "%.2f GB", sum/1024/1024/1024}')"
        echo "Unique hashes: $(tail -n +2 "$REPORT" | awk -F'\t' '{print $9}' | sort -u | wc -l | tr -d ' ')"
        echo ""
        echo "BY ROOT DIRECTORY:"
        echo "───────────────────────────────────────────────────────────────"
        tail -n +2 "$REPORT" | awk -F'\t' '{roots[$2]++; sizes[$2]+=$4} END {for(r in roots) printf "  %-40s %6d files  %8.2f GB\n", r, roots[r], sizes[r]/1024/1024/1024}'
        echo ""
        echo "TOP 10 LARGEST FILES:"
        echo "───────────────────────────────────────────────────────────────"
        tail -n +2 "$REPORT" | sort -t$'\t' -k4 -rn | head -10 | awk -F'\t' '{printf "  %8.2f MB  %s\n", $4/1024/1024, $3}'
        echo ""
        echo "═══════════════════════════════════════════════════════════════"
    } > "$SUMMARY"

    log_ok "Summary: $SUMMARY"
    cat "$SUMMARY"
}

# === MAIN ===
main() {
    local SYNC_ENABLED=false
    local ROOTS=("${DEFAULT_ROOTS[@]}")

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --sync)
                SYNC_ENABLED=true
                shift
                ;;
            --target)
                TAILSCALE_SYNC_TARGET="$2"
                shift 2
                ;;
            --roots)
                IFS=' ' read -ra ROOTS <<< "$2"
                shift 2
                ;;
            --install-tailscale)
                install_tailscale
                exit 0
                ;;
            --help|-h)
                echo "Usage: $0 [OPTIONS]"
                echo ""
                echo "Options:"
                echo "  --sync                  Sync results via Tailscale"
                echo "  --target HOST           Tailscale hostname for sync"
                echo "  --roots \"dir1 dir2\"     Override default scan roots"
                echo "  --install-tailscale     Install Tailscale"
                echo "  --help                  Show this help"
                exit 0
                ;;
            *)
                log_error "Unknown option: $1"
                exit 1
                ;;
        esac
    done

    show_banner

    # Setup
    mkdir -p "$OUT_DIR"
    TS="$(date '+%Y-%m-%d_%H%M%S')"
    HOST="$(scutil --get ComputerName 2>/dev/null || hostname)"
    REPORT="$OUT_DIR/${HOST}_truth_${TS}.tsv"
    ERR_LOG="$OUT_DIR/${HOST}_truth_${TS}.errors.log"

    log_info "Host: $HOST"
    log_info "Output: $OUT_DIR"
    log_info "Roots: ${ROOTS[*]}"
    echo ""

    # Check Tailscale
    if [[ "$SYNC_ENABLED" == true ]]; then
        check_tailscale || true
    fi
    echo ""

    # Initialize report
    echo -e "host\troot\tpath\tsize\tmtime\tmode\tuser\tgroup\tsha256" > "$REPORT"
    : > "$ERR_LOG"

    # Scan each root
    for ROOT in "${ROOTS[@]}"; do
        scan_directory "$ROOT" "$REPORT" "$ERR_LOG" "$HOST"
    done
    echo ""

    # Generate checksum of report
    shasum -a 256 "$REPORT" | tee "$REPORT.sha256" > /dev/null

    # Generate summary
    generate_summary "$REPORT"
    echo ""

    # Output files
    log_ok "Report: $REPORT"
    log_ok "Checksum: $REPORT.sha256"
    [[ -s "$ERR_LOG" ]] && log_warn "Errors: $ERR_LOG" || rm -f "$ERR_LOG"

    # Sync if enabled
    if [[ "$SYNC_ENABLED" == true ]] && [[ -n "$TAILSCALE_SYNC_TARGET" ]]; then
        echo ""
        sync_to_tailscale "$REPORT" "$TAILSCALE_SYNC_TARGET"
    fi

    echo ""
    log_ok "Scan complete!"
}

main "$@"
