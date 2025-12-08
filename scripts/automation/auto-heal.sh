#!/bin/bash
# Auto-Heal Script - Runs healing automatically
# =============================================

BASE="/Users/m2ultra/NOIZYLAB"

echo "🌍 Auto-Healing NoizyLab..."
cd "$BASE"

# Run healer
python3 health/healtheworld.py

# Restart services if needed
if ! curl -s http://localhost:8000/ >/dev/null 2>&1; then
    echo "🔄 Restarting services..."
    "$BASE/START_V4.sh" >/dev/null 2>&1 &
fi

echo "✅ Auto-heal complete!"

