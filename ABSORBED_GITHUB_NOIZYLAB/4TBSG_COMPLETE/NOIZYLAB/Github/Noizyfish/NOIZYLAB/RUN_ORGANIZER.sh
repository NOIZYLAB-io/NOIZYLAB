#!/bin/bash
# Quick Launcher for ULTIMATE_MASTER_ORGANIZER

echo "🔥 ULTIMATE MASTER ORGANIZER - QUICK LAUNCHER 🔥"
echo ""

# Find Python
if command -v python3 &> /dev/null; then
    PYTHON=python3
elif command -v python &> /dev/null; then
    PYTHON=python
else
    echo "❌ Python not found!"
    exit 1
fi

echo "✓ Using: $PYTHON"
echo ""

# Check which drive we're on
if [ -f "./ULTIMATE_MASTER_ORGANIZER.py" ]; then
    SCRIPT="./ULTIMATE_MASTER_ORGANIZER.py"
elif [ -f "/Volumes/12TB 1/ULTIMATE_MASTER_ORGANIZER.py" ]; then
    SCRIPT="/Volumes/12TB 1/ULTIMATE_MASTER_ORGANIZER.py"
elif [ -f "/Volumes/RED DRAGON/ULTIMATE_MASTER_ORGANIZER.py" ]; then
    SCRIPT="/Volumes/RED DRAGON/ULTIMATE_MASTER_ORGANIZER.py"
else
    echo "❌ ULTIMATE_MASTER_ORGANIZER.py not found!"
    exit 1
fi

echo "✓ Found script: $SCRIPT"
echo ""

# Make executable
chmod +x "$SCRIPT"

# Run it
exec $PYTHON "$SCRIPT" "$@"
