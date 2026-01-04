#!/usr/bin/env bash
set -euo pipefail

# Sovereign Interface orchestrator: status + chunk runners with graceful fallback.
# Usage:
#   ./sovereign_portal.sh status
#   ./sovereign_portal.sh chunk2 [--dry-run]
#   ./sovereign_portal.sh chunk3 [--dry-run]
#   ./sovereign_portal.sh all [--dry-run]

DRY=0
cmd="${1:-}"
shift || true

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY=1; shift;;
    *) break;;
  esac
done

fail() { echo "ERROR: $*" >&2; exit 1; }
info() { echo "INFO: $*"; }
warn() { echo "WARN: $*" >&2; }

need_actions() {
  [[ -x "./noizylab_actions.sh" ]] || fail "noizylab_actions.sh not executable; ensure it exists and chmod +x"
}

run_chunk() {
  local chunk="$1"
  if [[ "$DRY" -eq 1 ]]; then
    info "Dry-run: $chunk"
    ./noizylab_actions.sh "$chunk" --dry-run
    return
  fi

  if ./noizylab_actions.sh "$chunk"; then
    info "$chunk completed"
  else
    warn "$chunk failed; rerunning in dry-run to show required tools/assets"
    ./noizylab_actions.sh "$chunk" --dry-run || true
  fi
}

case "$cmd" in
  status)
    ./noizylab_vitals.sh
    ;;
  chunk2)
    need_actions
    run_chunk chunk2
    ;;
  chunk3)
    need_actions
    run_chunk chunk3
    ;;
  all)
    need_actions
    run_chunk chunk2
    run_chunk chunk3
    ;;
  *)
    echo "Usage: $0 {status|chunk2|chunk3|all} [--dry-run]" >&2
    exit 1
    ;;
esac
