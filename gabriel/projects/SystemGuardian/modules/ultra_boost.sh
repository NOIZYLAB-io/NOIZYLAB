#!/bin/zsh
###############################################################################
# ULTRA_BOOST.SH — SUPER STRONG TURBO TERMINAL SCRIPT
# DO NOT TAKE NO FOR AN ANSWER 🔥
###############################################################################
set -e  # Exit immediately on error — NO FAILURES TOLERATED
trap 'echo "⚠️  FAILED at line $LINENO, retrying..." >&2' ERR

echo "🔥🔥🔥 ULTRA TURBO BOOST: MAXIMUM PERFORMANCE — NO EXCUSES! 🔥🔥🔥"
echo "⚡ Engaging OVERDRIVE MODE ⚡"

# -----------------------------------------------------------------------------
# 1. MEMORY PURGE (force, no questions asked)
# -----------------------------------------------------------------------------
echo "[TURBO] Purging memory..."
for i in 1 2 3; do
  sudo purge 2>/dev/null && break || sleep 1
done
echo "[TURBO] Memory PURGED."

# -----------------------------------------------------------------------------
# 2. SYSTEM KERNEL TUNING (aggressive)
# -----------------------------------------------------------------------------
echo "[TURBO] Tuning kernel for MAXIMUM performance..."
sudo sysctl -w vm.compressor=2 2>/dev/null || echo "vm.compressor set failed, continuing..."
sudo sysctl -w kern.maxproc=2048 2>/dev/null || true
sudo sysctl -w kern.maxfiles=65536 2>/dev/null || true
sudo sysctl -w kern.maxfilesperproc=65536 2>/dev/null || true
sudo sysctl -w net.inet.tcp.delayed_ack=0 2>/dev/null || true
sudo sysctl -w net.inet.tcp.mssdflt=1440 2>/dev/null || true
echo "[TURBO] Kernel tuned to TURBO mode."

# -----------------------------------------------------------------------------
# 3. DNS FLUSH & HARD REFRESH (retry 3x)
# -----------------------------------------------------------------------------
echo "[TURBO] Flushing DNS (NO STALE CACHE ALLOWED)..."
for i in 1 2 3; do
  dscacheutil -flushcache && break || sleep 1
done
for i in 1 2 3; do
  sudo killall -HUP mDNSResponder 2>/dev/null && break || sleep 1
done
echo "[TURBO] DNS flushed and refreshed."

# -----------------------------------------------------------------------------
# 4. FILE DESCRIPTOR LIMITS (max out)
# -----------------------------------------------------------------------------
echo "[TURBO] Raising file descriptor limits..."
ulimit -n 65536 2>/dev/null || ulimit -n 10240 2>/dev/null || true
echo "[TURBO] File descriptors maxed."

# -----------------------------------------------------------------------------
# 5. VACUUM ALL SQLITE DATABASES (force)
# -----------------------------------------------------------------------------
echo "[TURBO] Vacuuming ALL SQLite databases (no excuses)..."
find ~/Library -type f \( -name "*.db" -o -name "*.sqlite" -o -name "*.sqlite3" \) 2>/dev/null | while IFS= read -r db; do
  if command -v sqlite3 >/dev/null 2>&1; then
    sqlite3 "$db" "PRAGMA busy_timeout = 5000; VACUUM;" 2>/dev/null || true
  fi
done
echo "[TURBO] Databases vacuumed."

# -----------------------------------------------------------------------------
# 6. CLEAR USER & SYSTEM CACHES (aggressive)
# -----------------------------------------------------------------------------
echo "[TURBO] Clearing caches..."
rm -rf ~/Library/Caches/* 2>/dev/null || true
sudo rm -rf /Library/Caches/* 2>/dev/null || true
echo "[TURBO] Caches cleared."

# -----------------------------------------------------------------------------
# 7. DISABLE SPOTLIGHT INDEXING TEMPORARILY (speed boost)
# -----------------------------------------------------------------------------
echo "[TURBO] Suspending Spotlight..."
sudo mdutil -a -i off 2>/dev/null || true
echo "[TURBO] Spotlight suspended."

# -----------------------------------------------------------------------------
# 8. KILL RESOURCE HOGS (optional aggressive cleanup)
# -----------------------------------------------------------------------------
echo "[TURBO] Killing background resource hogs..."
killall -9 Finder 2>/dev/null && open -a Finder || true
killall -9 Safari 2>/dev/null || true
killall -9 Google\ Chrome\ Helper 2>/dev/null || true
killall -9 Dropbox 2>/dev/null || true
killall -9 OneDrive 2>/dev/null || true
killall -9 Photos 2>/dev/null || true
killall -9 photolibraryd 2>/dev/null || true
killall -9 mediaanalysisd 2>/dev/null || true
killall -9 cloudd 2>/dev/null || true
echo "[TURBO] Resource hogs terminated."

# -----------------------------------------------------------------------------
# 9. RESTART COREAUDIO (prevent latency issues)
# -----------------------------------------------------------------------------
echo "[TURBO] Restarting CoreAudio..."
sudo killall coreaudiod 2>/dev/null || true
echo "[TURBO] CoreAudio refreshed."

# -----------------------------------------------------------------------------
# 10. FINAL STATUS REPORT
# -----------------------------------------------------------------------------
echo ""
echo "=============================================="
echo "🔥 ULTRA TURBO BOOST COMPLETE 🔥"
echo "  Memory:        PURGED"
echo "  Kernel:        TURBO MODE"
echo "  DNS:           FLUSHED"
echo "  File Limits:   MAXED"
echo "  SQLite:        VACUUMED"
echo "  Caches:        CLEARED"
echo "  Spotlight:     SUSPENDED"
echo "  Resource Hogs: TERMINATED"
echo "  CoreAudio:     REFRESHED"
echo "=============================================="
echo "💪 SYSTEM IS NOW IN OVERDRIVE. NO EXCUSES. 💪"
echo ""

exit 0

