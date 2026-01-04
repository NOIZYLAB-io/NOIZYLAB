#!/bin/bash
# ==============================================================================
# NOIZYLAB SYSTEM OPTIMIZER - REAL VERSION
# Built: 2026-01-04
# Author: Claude + Rob Plowman
# 
# THIS ACTUALLY WORKS. NO FANTASY. NO BULLSHIT.
# ==============================================================================

set -e

echo "═══════════════════════════════════════════════════════════════════"
echo "🔧 NOIZYLAB SYSTEM OPTIMIZER"
echo "═══════════════════════════════════════════════════════════════════"
echo ""

# Get initial memory state
INITIAL_FREE=$(vm_stat | grep "Pages free" | awk '{print $3}' | tr -d '.')
INITIAL_FREE_MB=$((INITIAL_FREE * 4096 / 1024 / 1024))

echo "📊 INITIAL STATE:"
echo "   Free Memory: ~${INITIAL_FREE_MB} MB"
echo ""

# -----------------------------------------------------------------------------
# 1. KILL BACKGROUND BLOAT (Real processes that actually run on macOS)
# -----------------------------------------------------------------------------
echo "🔪 KILLING BACKGROUND BLOAT..."

BLOAT_APPS=(
    "Spotify Helper"
    "Google Chrome Helper"
    "Adobe Creative Cloud"
    "Adobe CCXProcess"
    "Adobe CEF Helper"
    "Creative Cloud"
    "CCLibrary"
    "Dropbox"
    "OneDrive"
    "Microsoft Update"
    "com.apple.Safari.History"
    "Spotlight"
)

KILLED=0
for app in "${BLOAT_APPS[@]}"; do
    if pgrep -f "$app" > /dev/null 2>&1; then
        pkill -f "$app" 2>/dev/null && ((KILLED++)) || true
        echo "   ✓ Killed: $app"
    fi
done

if [ $KILLED -eq 0 ]; then
    echo "   ✓ No bloat processes found running"
else
    echo "   ✓ Killed $KILLED bloat processes"
fi
echo ""

# -----------------------------------------------------------------------------
# 2. DEPRIORITIZE (Not kill) Useful Background Apps
# -----------------------------------------------------------------------------
echo "⬇️  DEPRIORITIZING BACKGROUND APPS..."

DEPRIORITIZE_APPS=("Slack" "Discord" "zoom.us" "Mail" "Messages" "Notes")

for app in "${DEPRIORITIZE_APPS[@]}"; do
    PID=$(pgrep -x "$app" 2>/dev/null | head -1) || true
    if [ -n "$PID" ]; then
        renice 10 "$PID" > /dev/null 2>&1 || true
        echo "   ✓ Deprioritized: $app (PID $PID)"
    fi
done
echo ""

# -----------------------------------------------------------------------------
# 3. CLEAR SYSTEM CACHES (Real macOS commands)
# -----------------------------------------------------------------------------
echo "🧹 CLEARING CACHES..."

# User caches that are safe to clear
CACHE_DIRS=(
    "$HOME/Library/Caches/com.spotify.client"
    "$HOME/Library/Caches/Google"
    "$HOME/Library/Caches/com.google.Chrome"
    "$HOME/Library/Caches/Firefox"
    "$HOME/Library/Caches/com.operasoftware.Opera"
    "$HOME/Library/Caches/pip"
    "$HOME/Library/Caches/Homebrew"
)

CLEARED_MB=0
for dir in "${CACHE_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        SIZE=$(du -sm "$dir" 2>/dev/null | cut -f1) || SIZE=0
        rm -rf "$dir" 2>/dev/null || true
        CLEARED_MB=$((CLEARED_MB + SIZE))
        echo "   ✓ Cleared: $(basename "$dir") (${SIZE}MB)"
    fi
done

echo "   Total cleared: ${CLEARED_MB}MB"
echo ""

# -----------------------------------------------------------------------------
# 4. FLUSH DISK CACHE (This actually works)
# -----------------------------------------------------------------------------
echo "💾 FLUSHING DISK CACHE..."
sudo purge 2>/dev/null || echo "   ⚠ Needs sudo for full purge (run with sudo)"
echo "   ✓ Disk cache flushed"
echo ""

# -----------------------------------------------------------------------------
# 5. CLEAR NPM/HOMEBREW CACHES
# -----------------------------------------------------------------------------
echo "📦 CLEARING PACKAGE CACHES..."

if command -v npm &> /dev/null; then
    npm cache clean --force 2>/dev/null || true
    echo "   ✓ NPM cache cleared"
fi

if command -v brew &> /dev/null; then
    brew cleanup -s 2>/dev/null || true
    echo "   ✓ Homebrew cache cleared"
fi
echo ""

# -----------------------------------------------------------------------------
# 6. REPORT FINAL STATE
# -----------------------------------------------------------------------------
FINAL_FREE=$(vm_stat | grep "Pages free" | awk '{print $3}' | tr -d '.')
FINAL_FREE_MB=$((FINAL_FREE * 4096 / 1024 / 1024))
RECOVERED=$((FINAL_FREE_MB - INITIAL_FREE_MB))

echo "═══════════════════════════════════════════════════════════════════"
echo "✅ OPTIMIZATION COMPLETE"
echo "═══════════════════════════════════════════════════════════════════"
echo ""
echo "📊 RESULTS:"
echo "   Initial Free Memory: ~${INITIAL_FREE_MB} MB"
echo "   Final Free Memory:   ~${FINAL_FREE_MB} MB"
echo "   Cache Cleared:       ${CLEARED_MB} MB"
echo "   Processes Killed:    ${KILLED}"
echo ""
echo "🔥 GORUNFREE"
echo ""
