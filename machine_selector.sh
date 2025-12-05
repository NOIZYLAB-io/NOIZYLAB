#!/bin/bash
# Machine Status Selector
# Usage: machine_selector.sh [MACHINE_ID]
# If no machine specified, shows all

MACHINE="${1:-}"
cd /Users/m2ultra/NOIZYLAB/backend

if [ -z "$MACHINE" ]; then
    echo "🔍 ALL MACHINES STATUS"
    python3 nlctl.py status
else
    echo "🔍 STATUS: $MACHINE"
    python3 nlctl.py status "$MACHINE"
fi
