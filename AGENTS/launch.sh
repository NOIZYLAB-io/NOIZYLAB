#!/bin/bash
# NOIZYLAB Agent Launcher
# Usage: ./launch.sh [agent_name] [--cloud]

NOIZYLAB="/Users/m2ultra/NOIZYLAB"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if --cloud flag is present
USE_CLOUD=false
if [[ "$*" == *"--cloud"* ]]; then
  USE_CLOUD=true
fi

# Remove --cloud from args
AGENT_NAME=$(echo "$1" | sed 's/--cloud//' | xargs)

case "$AGENT_NAME" in
  gabriel|GABRIEL)
    if [ "$USE_CLOUD" = true ]; then
      echo "☁️  Delegating to cloud GABRIEL..."
      python3 "$SCRIPT_DIR/cloud-delegate.py" --agent gabriel --action health
    else
      echo "🚀 Launching GABRIEL locally..."
      python3 "$NOIZYLAB/GABRIEL/tools/gabriel_control.py"
    fi
    ;;
  mc96|MC96)
    if [ "$USE_CLOUD" = true ]; then
      echo "☁️  Delegating to cloud MC96..."
      python3 "$SCRIPT_DIR/cloud-delegate.py" --agent mc96 --action vault-status
    else
      echo "🚀 Launching MC96 locally..."
      python3 "$NOIZYLAB/MC96/vault/organize_code.py"
    fi
    ;;
  systemguardian|system-guardian|SystemGuardian)
    if [ "$USE_CLOUD" = true ]; then
      echo "☁️  Delegating to cloud SystemGuardian..."
      python3 "$SCRIPT_DIR/cloud-delegate.py" --agent systemGuardian --action status
    else
      echo "⚠️  SystemGuardian only available in cloud mode"
      echo "Run: $0 systemguardian --cloud"
      exit 1
    fi
    ;;
  all)
    if [ "$USE_CLOUD" = true ]; then
      echo "☁️  Delegating to all cloud agents..."
      python3 "$SCRIPT_DIR/cloud-delegate.py" --agent gabriel --action health
      python3 "$SCRIPT_DIR/cloud-delegate.py" --agent mc96 --action vault-status
      python3 "$SCRIPT_DIR/cloud-delegate.py" --agent systemGuardian --action status
    else
      echo "🚀 Launching ALL local agents..."
      python3 "$NOIZYLAB/GABRIEL/tools/gabriel_control.py" &
      echo "All local agents started."
    fi
    ;;
  cloud-health)
    echo "🏥 Checking cloud health..."
    python3 "$SCRIPT_DIR/cloud-delegate.py" --health
    ;;
  cloud-list)
    echo "📋 Listing cloud agents..."
    python3 "$SCRIPT_DIR/cloud-delegate.py" --list
    ;;
  list)
    echo "Available agents:"
    echo "  - gabriel          : Zero Latency Voice + Control (local or --cloud)"
    echo "  - mc96             : Core Universe Engine (local or --cloud)"
    echo "  - systemguardian   : System Monitoring (--cloud only)"
    echo ""
    echo "Cloud commands:"
    echo "  - cloud-health     : Check cloud worker health"
    echo "  - cloud-list       : List available cloud agents"
    echo ""
    echo "Examples:"
    echo "  $0 gabriel         # Run locally"
    echo "  $0 gabriel --cloud # Delegate to cloud"
    echo "  $0 systemguardian --cloud"
    ;;
  *)
    echo "NOIZYLAB Agent Launcher"
    echo "Usage: $0 {gabriel|mc96|systemguardian|all|cloud-health|cloud-list|list} [--cloud]"
    echo ""
    echo "Add --cloud flag to delegate to cloud agent instead of running locally"
    exit 1
    ;;
esac
