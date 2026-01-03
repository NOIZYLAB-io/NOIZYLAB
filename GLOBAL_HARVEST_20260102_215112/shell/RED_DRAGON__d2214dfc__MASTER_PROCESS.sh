#!/usr/bin/env bash
# MASTER PROCESS - Complete workflow for _noizy_projects

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║     MASTER PROCESS: SCAN → HEAL → OPTIMIZE → HARVEST          ║"
echo "║                  → ABSORB → MOVE                              ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

cd "$SCRIPT_DIR"

echo "📡 Starting complete workflow..."
echo ""

# Dry run first
python3 PROJECT_MASTER_PROCESSOR.py

echo ""
read -p "Execute full process (heal, harvest, absorb, move)? (yes/no): " confirm

if [ "$confirm" = "yes" ]; then
    echo ""
    echo "🚀 EXECUTING COMPLETE WORKFLOW..."
    python3 PROJECT_MASTER_PROCESSOR.py --live
    
    echo ""
    echo "✅ MASTER PROCESS COMPLETE!"
else
    echo "❌ Cancelled"
fi

echo ""

