#!/bin/bash
###############################################################################
# NoizyLab Dependencies Installer
###############################################################################

set -e

echo "📦 Installing NoizyLab Dependencies..."
echo "======================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Core dependencies
echo "📥 Installing core dependencies..."
pip3 install --upgrade pip

pip3 install \
    requests \
    psutil \
    pandas \
    numpy \
    rich \
    click

echo ""
echo "📥 Installing Slack dependencies..."
pip3 install \
    slack-sdk \
    fastapi \
    uvicorn[standard] \
    pydantic \
    python-multipart \
    streamlit \
    plotly

echo ""
echo "📥 Installing network dependencies..."
pip3 install \
    pysnmp \
    netifaces

echo ""
echo "📥 Installing optional dependencies..."
pip3 install \
    sqlite3 \
    aiohttp \
    websockets

echo ""
echo "✅ All dependencies installed!"
echo ""
echo "🎯 Next steps:"
echo "  1. Configure Slack tokens (see README.md)"
echo "  2. Run: ./LAUNCH_NOIZYLAB_COMPLETE.sh"
echo ""

