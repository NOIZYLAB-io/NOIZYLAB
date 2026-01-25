#!/bin/bash
# NOIZYLAB Agent Launcher
# Usage: ./launch.sh [agent_name]

NOIZYLAB="/Users/m2ultra/NOIZYLAB"

case "$1" in
  gabriel|GABRIEL)
    echo "🚀 Launching GABRIEL..."
    python3 "$NOIZYLAB/GABRIEL/tools/gabriel_control.py"
    ;;
  mc96|MC96)
    echo "🚀 Launching MC96..."
    python3 "$NOIZYLAB/MC96/vault/organize_code.py"
    ;;
  cloud-agent|cloud)
    echo "🚀 Launching Cloud Agent Client..."
    python3 "$NOIZYLAB/cloud_agent_client.py"
    ;;
  cloud-status)
    echo "🔍 Checking Cloud Agent Status..."
    python3 "$NOIZYLAB/cloud_agent_client.py" --status
    ;;
  all)
    echo "🚀 Launching ALL agents..."
    python3 "$NOIZYLAB/GABRIEL/tools/gabriel_control.py" &
    echo "All agents started."
    ;;
  list)
    echo "Available agents:"
    echo "  - gabriel      : Zero Latency Voice + Control"
    echo "  - mc96         : Core Universe Engine"
    echo "  - cloud-agent  : Cloudflare Worker Agent (Remote)"
    echo "  - cloud-status : Check Cloud Agent Status"
    ;;
  *)
    echo "NOIZYLAB Agent Launcher"
    echo "Usage: $0 {gabriel|mc96|cloud-agent|cloud-status|all|list}"
    exit 1
    ;;
esac
