#!/usr/bin/env bash
set -euo pipefail

# Simple HUD for the three chunks. Reports presence of required tools/assets.

has() { command -v "$1" >/dev/null 2>&1; }
exists() { [[ -e "$1" ]]; }

status_line() {
  local name="$1" state="$2" detail="$3"
  printf "%-12s : %-8s : %s\n" "$name" "$state" "$detail"
}

chunk1() {
  local ok=1 missing=()
  for bin in cloudflared; do
    if ! has "$bin"; then ok=0; missing+=("$bin"); fi
  done
  if (( ok )); then
    status_line "CHUNK 1" "ready" "Gateway tooling present (cloudflared detected)."
  else
    status_line "CHUNK 1" "pending" "Missing: ${missing[*]:-none}. Add Zero Trust tunnel tooling."
  fi
}

chunk2() {
  local ok=1 missing=()
  for bin in noizylab-vision noizvox; do
    if ! has "$bin"; then ok=0; missing+=("$bin"); fi
  done
  for asset in diff_baseline.py manifest.yaml; do
    if ! exists "$asset"; then ok=0; missing+=("$asset"); fi
  done
  if (( ok )); then
    status_line "CHUNK 2" "ready" "Vision/intent stack present."
  else
    status_line "CHUNK 2" "pending" "Missing: ${missing[*]:-none}. Place tools/assets in repo."
  fi
}

chunk3() {
  local ok=1 missing=()
  for bin in fish-engine noizylab-admin noizylab-status; do
    if ! has "$bin"; then ok=0; missing+=("$bin"); fi
  done
  for asset in diagnostic_beds/lowpulse.wav trust_signatures/noizylab_resolve.wav; do
    if ! exists "$asset"; then ok=0; missing+=("$asset"); fi
  done
  if (( ok )); then
    status_line "CHUNK 3" "ready" "Pulse stack present."
  else
    status_line "CHUNK 3" "pending" "Missing: ${missing[*]:-none}. Install tools and add audio assets."
  fi
}

main() {
  chunk1
  chunk2
  chunk3
}

main "$@"
