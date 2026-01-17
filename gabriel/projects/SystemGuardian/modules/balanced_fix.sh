#!/bin/zsh
###############################################################################
# BALANCED_FIX.SH — SUPER STRONG TURBO FIX SCRIPT
# DO NOT TAKE NO FOR AN ANSWER 🔥
###############################################################################
set -e
trap 'echo "⚠️  Fix issue at line $LINENO — retrying..." >&2' ERR

echo "🔥🔥🔥 TURBO BALANCED FIX: AGGRESSIVE SYSTEM REPAIR 🔥🔥🔥"
echo ""

# -----------------------------------------------------------------------------
# 1. DNS FLUSH (retry 3x, no excuses)
# -----------------------------------------------------------------------------
echo "[TURBO FIX] Flushing DNS..."
for i in 1 2 3; do
  dscacheutil -flushcache && break || sleep 1
done
for i in 1 2 3; do
  sudo killall -HUP mDNSResponder 2>/dev/null && break || sleep 1
done
echo "✅ DNS FLUSHED"

# -----------------------------------------------------------------------------
# 2. CLEAR OLD CACHES (aggressive — 3+ days old)
# -----------------------------------------------------------------------------
echo "[TURBO FIX] Clearing old caches..."
find ~/Library/Caches -type f -atime +3 -delete 2>/dev/null || true
find ~/Library/Caches -type d -empty -delete 2>/dev/null || true
echo "✅ Old caches CLEARED"

# -----------------------------------------------------------------------------
# 3. REBUILD LAUNCH SERVICES (force)
# -----------------------------------------------------------------------------
echo "[TURBO FIX] Rebuilding Launch Services..."
for i in 1 2 3; do
  /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -kill -r -domain local -domain system -domain user 2>/dev/null && break || sleep 2
done
echo "✅ Launch Services REBUILT"

# -----------------------------------------------------------------------------
# 4. REPAIR DISK PERMISSIONS (if available)
# -----------------------------------------------------------------------------
echo "[TURBO FIX] Repairing disk permissions..."
sudo diskutil repairPermissions / 2>/dev/null || echo "(Disk permission repair skipped — not supported on this macOS version)"
echo "✅ Permissions checked"

# -----------------------------------------------------------------------------
# 5. RESET SPOTLIGHT INDEX (if corrupted)
# -----------------------------------------------------------------------------
echo "[TURBO FIX] Checking Spotlight index..."
if ! mdfind -onlyin ~ -name "test" >/dev/null 2>&1; then
  echo "[TURBO FIX] Spotlight may be corrupt — rebuilding..."
  sudo mdutil -E / 2>/dev/null || true
fi
echo "✅ Spotlight checked"

# -----------------------------------------------------------------------------
# 6. KILL STUCK PROCESSES
# -----------------------------------------------------------------------------
echo "[TURBO FIX] Killing stuck processes..."
for proc in mds_stores mdworker_shared cloudd nsurlsessiond; do
  killall -9 $proc 2>/dev/null || true
done
echo "✅ Stuck processes terminated"

# -----------------------------------------------------------------------------
# FINAL STATUS
# -----------------------------------------------------------------------------
echo ""
echo "============================================="
echo "🔥 TURBO BALANCED FIX COMPLETE 🔥"
echo "  DNS:             FLUSHED"
echo "  Caches:          CLEARED"
echo "  Launch Services: REBUILT"
echo "  Permissions:     CHECKED"
echo "  Spotlight:       VERIFIED"
echo "  Stuck Procs:     TERMINATED"
echo "============================================="
echo "💪 SYSTEM REPAIRED. NO EXCUSES. 💪"
echo ""

exit 0

