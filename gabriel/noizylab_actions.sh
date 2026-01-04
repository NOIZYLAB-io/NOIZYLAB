#!/usr/bin/env bash
set -euo pipefail

# Runner for the ritual commands with guardrails and clear error output.
# Usage:
#   ./noizylab_actions.sh chunk2   # run vision/intent sequence
#   ./noizylab_actions.sh chunk3   # run pulse/zen-lock sequence
#   ./noizylab_actions.sh chunk2 --dry-run  # print what would run

DRY=0
cmd="${1:-}"
shift || true

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY=1; shift;;
    *) break;;
  esac
done

need() { command -v "$1" >/dev/null 2>&1; }
fail() { echo "ERROR: $*" >&2; exit 1; }
info() { echo "INFO: $*"; }

run_or_echo() {
  if [[ "$DRY" -eq 1 ]]; then
    echo "[dry-run] $*"
  else
    eval "$@"
  fi
}

chunk2() {
  local missing=()
  need noizylab-vision || missing+=("noizylab-vision")
  need noizvox || missing+=("noizvox")
  [[ -f diff_baseline.py ]] || missing+=("diff_baseline.py")
  [[ -f manifest.yaml ]] || missing+=("manifest.yaml")
  if [[ ${#missing[@]} -gt 0 ]]; then
    fail "Chunk 2 missing: ${missing[*]}"
  fi

  info "Launching Gemini 3 Flash forensic overlay"
  run_or_echo 'noizylab-vision --mode "ghost-trace" --ref-board "M1_LOGIC_BOARD_GOLDEN" --predictive-jitter-comp --latency-target 8ms'

  info "Engaging sub-vocal aura analysis"
  run_or_echo 'noizvox --calibrate --mic "P24_PLANAR" --intent-model "SOVEREIGN_RECON" --sensitivity 0.98'

  info "Locking forensic baseline"
  run_or_echo 'python3 diff_baseline.py --baseline ./manifest.yaml --strict'
}

chunk3() {
  local missing=()
  need fish-engine || missing+=("fish-engine")
  need noizylab-admin || missing+=("noizylab-admin")
  need noizylab-status || missing+=("noizylab-status")
  [[ -f diagnostic_beds/lowpulse.wav ]] || missing+=("diagnostic_beds/lowpulse.wav")
  [[ -f trust_signatures/noizylab_resolve.wav ]] || missing+=("trust_signatures/noizylab_resolve.wav")
  if [[ ${#missing[@]} -gt 0 ]]; then
    fail "Chunk 3 missing: ${missing[*]}"
  fi

  info "Activating vestibular sedation (30Hz sub-bass)"
  run_or_echo 'fish-engine play --asset "diagnostic_beds/lowpulse.wav" --frequency-modulate --bio-sync "P24_HEARTBEAT"'

  info "Engaging ZEN_LOCK (zero-notification)"
  run_or_echo 'noizylab-admin --zen-lock --prioritize-friction-delta'

  info "Evaluating integrity and emitting trust signature if perfect"
  run_or_echo '[[ $(noizylab-status --integrity) == "100.0" ]] && fish-engine play --asset "trust_signatures/noizylab_resolve.wav"'
}

case "$cmd" in
  chunk2) chunk2 ;;
  chunk3) chunk3 ;;
  *) echo "Usage: $0 {chunk2|chunk3} [--dry-run]" >&2; exit 1 ;;
esac
