#!/bin/zsh
###############################################################################
# SYSTEM_STABLE.SH — SUPER STRONG TURBO STABILITY CHECKER
# DO NOT TAKE NO FOR AN ANSWER 🔥
# Returns 0 if stable, 1 if NOT stable
###############################################################################

echo "🔥 TURBO STABILITY CHECK 🔥"
echo ""

STABLE=1

# -----------------------------------------------------------------------------
# 1. CPU IDLE CHECK (retry 3x for accuracy)
# -----------------------------------------------------------------------------
echo "[CHECK] CPU idle..."
CPU_IDLE=0
for i in 1 2 3; do
  CPU_IDLE=$(ps -A -o %cpu | awk '{s+=$1} END {printf "%.0f", 100-s}' 2>/dev/null || echo "0")
  if [ -n "$CPU_IDLE" ] && [ "$CPU_IDLE" -ge 50 ]; then
    break
  fi
  sleep 1
done
if [ -z "$CPU_IDLE" ] || [ "$CPU_IDLE" -lt 50 ]; then
  echo "  ❌ CPU too busy (idle: ${CPU_IDLE}%)"
  STABLE=0
else
  echo "  ✅ CPU OK (idle: ${CPU_IDLE}%)"
fi

# -----------------------------------------------------------------------------
# 2. MEMORY CHECK (aggressive threshold)
# -----------------------------------------------------------------------------
echo "[CHECK] Memory..."
MEMORY_FREE=$(memory_pressure 2>/dev/null | grep "System-wide memory free percentage" | awk '{print $5}' | sed 's/%//' || echo "100")
if [ -z "$MEMORY_FREE" ]; then
  MEMORY_FREE=100
fi
if [ "$MEMORY_FREE" -lt 15 ]; then
  echo "  ❌ Memory critically low (free: ${MEMORY_FREE}%)"
  STABLE=0
else
  echo "  ✅ Memory OK (free: ${MEMORY_FREE}%)"
fi

# -----------------------------------------------------------------------------
# 3. RUNAWAY PROCESS CHECK
# -----------------------------------------------------------------------------
echo "[CHECK] Runaway processes..."
RUNAWAY=$(ps aux | awk 'NR>1 {if ($3 > 60.0 || $4 > 60.0) print $2}' | wc -l | tr -d ' ')
if [ "$RUNAWAY" -gt 2 ]; then
  echo "  ❌ Too many runaway processes ($RUNAWAY)"
  STABLE=0
else
  echo "  ✅ Runaway processes OK ($RUNAWAY)"
fi

# -----------------------------------------------------------------------------
# 4. DISK SPACE CHECK
# -----------------------------------------------------------------------------
echo "[CHECK] Disk space..."
DISK_USED=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
if [ -n "$DISK_USED" ] && [ "$DISK_USED" -gt 95 ]; then
  echo "  ❌ Disk nearly full (${DISK_USED}% used)"
  STABLE=0
else
  echo "  ✅ Disk OK (${DISK_USED}% used)"
fi

# -----------------------------------------------------------------------------
# 5. NETWORK CHECK
# -----------------------------------------------------------------------------
echo "[CHECK] Network..."
NETWORK_OK=0
for target in 8.8.8.8 1.1.1.1; do
  if ping -c 1 -W 2 "$target" >/dev/null 2>&1; then
    NETWORK_OK=1
    break
  fi
done
if [ $NETWORK_OK -eq 0 ]; then
  echo "  ❌ Network unreachable"
  STABLE=0
else
  echo "  ✅ Network OK"
fi

# -----------------------------------------------------------------------------
# FINAL VERDICT
# -----------------------------------------------------------------------------
echo ""
if [ $STABLE -eq 1 ]; then
  echo "============================================="
  echo "🔥 SYSTEM STABLE 🔥"
  echo "============================================="
  exit 0
else
  echo "============================================="
  echo "⚠️  SYSTEM UNSTABLE ⚠️"
  echo "============================================="
  exit 1
fi

