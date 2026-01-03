#!/bin/bash
# ============================================================
# MC96 ECOUNIVERSE - Launch Script
# GORUNFREE - One command = everything done
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CORE_DIR="${SCRIPT_DIR}/core"
CONFIG_DIR="${SCRIPT_DIR}/configs"

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║             ███╗   ███╗ ██████╗ █████╗  ██████╗              ║"
echo "║             ████╗ ████║██╔════╝██╔══██╗██╔════╝              ║"
echo "║             ██╔████╔██║██║     ╚██████║███████╗              ║"
echo "║             ██║╚██╔╝██║██║      ╚═══██║██╔═══██╗             ║"
echo "║             ██║ ╚═╝ ██║╚██████╗ █████╔╝╚██████╔╝             ║"
echo "║             ╚═╝     ╚═╝ ╚═════╝ ╚════╝  ╚═════╝              ║"
echo "║                                                              ║"
echo "║                    E C O U N I V E R S E                     ║"
echo "║                                                              ║"
echo "║           Network Controller • System Intelligence           ║"
echo "║                                                              ║"
echo "║                      GORUNFREE                               ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.9+."
    exit 1
fi

# Check for optional dependencies
echo "Checking dependencies..."

UVLOOP_STATUS="❌"
ORJSON_STATUS="❌"

python3 -c "import uvloop" 2>/dev/null && UVLOOP_STATUS="✅"
python3 -c "import orjson" 2>/dev/null && ORJSON_STATUS="✅"

echo ""
echo "  uvloop (async):     ${UVLOOP_STATUS}"
echo "  orjson (fast JSON): ${ORJSON_STATUS}"
echo ""

# Optional: Install missing deps
if [ "$1" == "--install" ]; then
    echo "Installing optional dependencies..."
    pip3 install uvloop orjson --quiet
    echo "✅ Dependencies installed."
    echo ""
fi

# Change to script directory
cd "$SCRIPT_DIR"

# Launch MC96
echo "🚀 Starting MC96 ECOUNIVERSE..."
echo ""

python3 "${CORE_DIR}/mc96.py"
