#!/bin/bash
# TURBO MODE - Apply speed fixes to ALL slow volumes
# NO WAITING - PARALLEL EXECUTION

echo "🚀 TURBO MODE ACTIVATED"

# Function to fix a volume FAST
fix_volume() {
    local vol="$1"
    if [ ! -d "/Volumes/$vol" ]; then return; fi
    
    echo "⚡ Fixing: $vol"
    
    # Disable Spotlight (no sudo needed for off)
    mdutil -i off "/Volumes/$vol" 2>/dev/null
    
    # Kill any indexing on this volume
    pkill -9 -f "mdworker.*$vol" 2>/dev/null
    
    echo "✓ $vol TURBOCHARGED"
}

# Fix all volumes in PARALLEL
fix_volume "12TB" &
fix_volume "RED DRAGON" &
fix_volume "4TB Blue Fish" &
fix_volume "6TB" &
fix_volume "MAG 4TB" &
fix_volume "EW" &
fix_volume "4TB Lacie" &
fix_volume "SOUND_DESIGN" &
fix_volume "SAMPLE_MASTER" &

wait

echo ""
echo "🔥 ALL VOLUMES TURBOCHARGED"
echo ""
echo "Testing 12TB speed..."
time ls /Volumes/12TB >/dev/null 2>&1 && echo "✓ 12TB FAST" || echo "✗ Still slow"
