#!/bin/bash
# START_HERE.sh - Main launcher from new location

clear

CODE_MASTER="/Volumes/4TB_02/CODE_MASTER"

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║     🚀 CODE_MASTER X1000 - NEW LOCATION                              ║"
echo "║     📍 Location: $CODE_MASTER                                        ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

if [ -f "$CODE_MASTER/scripts/START_HERE_X1000.sh" ]; then
    bash "$CODE_MASTER/scripts/START_HERE_X1000.sh"
else
    echo "⚠️  Main launcher not found. Available scripts:"
    ls -1 "$CODE_MASTER/scripts"/*.sh 2>/dev/null | head -10
fi

