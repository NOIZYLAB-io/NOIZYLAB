#!/bin/bash
# NOIZYLAB Agent Launcher (runs locally, no CI/billing needed)
# Usage: ./launch.sh {gabriel|mc96|all|list}

# Override with NOIZYLAB=/path; default is the repo root above this script.
NOIZYLAB="${NOIZYLAB:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

GABRIEL_SCRIPT="$NOIZYLAB/GABRIEL/tools/gabriel_control.py"
MC96_SCRIPT="$NOIZYLAB/MC96/vault/organize_code.py"

run_agent() {
  local name="$1" script="$2"
  if [ ! -f "$script" ]; then
    echo "❌ $name: script not found: $script" >&2
    return 1
  fi
  echo "🚀 Launching $name..."
  python3 "$script"
}

case "$1" in
  gabriel|GABRIEL)
    run_agent GABRIEL "$GABRIEL_SCRIPT"
    ;;
  mc96|MC96)
    run_agent MC96 "$MC96_SCRIPT"
    ;;
  all)
    echo "🚀 Launching ALL agents..."
    run_agent GABRIEL "$GABRIEL_SCRIPT" & p1=$!
    run_agent MC96 "$MC96_SCRIPT" & p2=$!
    rc=0
    wait "$p1" || rc=1
    wait "$p2" || rc=1
    exit "$rc"
    ;;
  list)
    echo "Available agents:"
    echo "  - gabriel : Zero Latency Voice + Control"
    echo "  - mc96    : Core Universe Engine"
    ;;
  *)
    echo "NOIZYLAB Agent Launcher"
    echo "Usage: $0 {gabriel|mc96|all|list}"
    exit 1
    ;;
esac
