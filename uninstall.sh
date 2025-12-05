#!/usr/bin/env bash
#
# HealTheWorld Rollback
# RUN: bash uninstall.sh
# RESULT: Removes venv and optional data (ask confirmation)
# GORUNFREE! 🎸🔥
#

set -euo pipefail

echo ""
echo "=========================================="
echo "🗑️  HealTheWorld - UNINSTALLER"
echo "=========================================="
echo ""

# Remove virtual environment
if [ -d "venv" ]; then
    echo "🗑️  Removing virtual environment..."
    rm -rf venv
    echo "✅ Virtual environment removed"
else
    echo "⚠️  No virtual environment found"
fi

# Ask about data
echo ""
echo "❓ Remove database and uploaded data?"
echo "   Location: ./data/"
read -p "   Remove data? (y/N): " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    if [ -d "data" ]; then
        rm -rf data
        echo "✅ Data directory removed"
    else
        echo "⚠️  No data directory found"
    fi
else
    echo "✅ Data preserved in ./data/"
fi

echo ""
echo "=========================================="
echo "✅ UNINSTALL COMPLETE"
echo "=========================================="
echo ""
echo "To reinstall: bash install.sh"
echo ""
