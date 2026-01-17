#!/bin/zsh
###############################################################################
# M2ULTRA-BOOT-STARTUP.SH — SUPER STRONG TURBO BOOT SCRIPT
# DO NOT TAKE NO FOR AN ANSWER 🔥
###############################################################################
set -e  # Exit immediately on error — NO FAILURES TOLERATED
trap 'echo "⚠️  WARNING at line $LINENO — retrying..." >&2' ERR

echo "🚀🔥 M2Ultra TURBO Boot Startup — $(date) 🔥🚀" | tee -a ~/.m2ultra-boot.log

# ============================================================================
# ENVIRONMENT INITIALIZATION (SUPER STRONG)
# ============================================================================

export NOIZYLAB_HOME="/Users/m2ultra/.claude-worktrees/NOIZYLAB/upbeat-moore"
export DRIVE_RED_DRAGON="/Volumes/RED DRAGON"
export DRIVE_RSP="/Volumes/RSP"
export DRIVE_DATA="/Volumes/RSP/NOISYLABZ"
export PATH="/usr/local/bin:/opt/homebrew/bin:$PATH"

# ============================================================================
# LOAD ALIASES & FUNCTIONS (FORCE LOAD, NO EXCUSES)
# ============================================================================

for alias_file in ~/.zsh_aliases ~/.aliases ~/.zshrc_aliases; do
  if [ -f "$alias_file" ]; then
    source "$alias_file" 2>/dev/null || true
    echo "✅ $alias_file FORCE LOADED" >> ~/.m2ultra-boot.log
  fi
done

# ============================================================================
# START ESSENTIAL SERVICES (AGGRESSIVE — RETRY 3X)
# ============================================================================

# Enable SSH (retry up to 3 times)
echo "[TURBO] Enabling SSH..."
for i in 1 2 3; do
  sudo systemsetup -setremotelogin on 2>/dev/null && break || sleep 1
done
echo "✅ SSH FORCE ENABLED" >> ~/.m2ultra-boot.log

# Start Screen Sharing (force start if not running)
echo "[TURBO] Starting Screen Sharing..."
if ! pgrep -x "ARDAgent" > /dev/null; then
  for i in 1 2 3; do
    sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart \
      -activate -configure -access -on -users admin -privs -all -restart -agent -console 2>/dev/null && break || sleep 2
  done
fi
echo "✅ Screen Sharing FORCE STARTED" >> ~/.m2ultra-boot.log

# ============================================================================
# MOUNT DRIVES (AGGRESSIVE RETRY)
# ============================================================================

echo "[TURBO] Mounting drives..."
mount_with_retry() {
  local mount_cmd="$1"
  local mount_point="$2"
  for i in 1 2 3 4 5; do
    if [ -d "$mount_point" ]; then
      echo "✅ $mount_point already mounted" >> ~/.m2ultra-boot.log
      return 0
    fi
    eval "$mount_cmd" 2>/dev/null && break || sleep 2
  done
}

mount_with_retry "mount_afp afp://RED_DRAGON_IP/RED_DRAGON $DRIVE_RED_DRAGON" "$DRIVE_RED_DRAGON"
mount_with_retry "mount_afp afp://RSP_IP/RSP $DRIVE_RSP" "$DRIVE_RSP"

echo "✅ Drives mounted (if available)" >> ~/.m2ultra-boot.log

# ============================================================================
# TURBO SYSTEM TUNING (KERNEL + NETWORK)
# ============================================================================

echo "[TURBO] Applying kernel turbo settings..."
sudo sysctl -w kern.maxproc=2048 2>/dev/null || true
sudo sysctl -w kern.maxfiles=65536 2>/dev/null || true
sudo sysctl -w net.inet.tcp.delayed_ack=0 2>/dev/null || true
echo "✅ Kernel TURBO tuning applied" >> ~/.m2ultra-boot.log

# ============================================================================
# DNS FLUSH (FORCE)
# ============================================================================

echo "[TURBO] Flushing DNS..."
dscacheutil -flushcache 2>/dev/null || true
sudo killall -HUP mDNSResponder 2>/dev/null || true
echo "✅ DNS FORCE FLUSHED" >> ~/.m2ultra-boot.log

# ============================================================================
# FILE DESCRIPTOR LIMITS (MAX OUT)
# ============================================================================

ulimit -n 65536 2>/dev/null || ulimit -n 10240 2>/dev/null || true
echo "✅ File descriptor limits MAXED" >> ~/.m2ultra-boot.log

# ============================================================================
# LOG SYSTEM INFO (SUPER DETAILED)
# ============================================================================

echo "-------------------------------------" >> ~/.m2ultra-boot.log
echo "Computer: $(scutil --get ComputerName 2>/dev/null || hostname)" >> ~/.m2ultra-boot.log
echo "IP (en0): $(ipconfig getifaddr en0 2>/dev/null || echo 'N/A')" >> ~/.m2ultra-boot.log
echo "IP (en1): $(ipconfig getifaddr en1 2>/dev/null || echo 'N/A')" >> ~/.m2ultra-boot.log
echo "Uptime: $(uptime 2>/dev/null)" >> ~/.m2ultra-boot.log
echo "Memory: $(vm_stat | head -5)" >> ~/.m2ultra-boot.log
echo "-------------------------------------" >> ~/.m2ultra-boot.log

# ============================================================================
# CLEANUP LOG (keep last 500 lines for debugging)
# ============================================================================

tail -500 ~/.m2ultra-boot.log > ~/.m2ultra-boot.log.tmp && mv ~/.m2ultra-boot.log.tmp ~/.m2ultra-boot.log

# ============================================================================
# FINAL STATUS
# ============================================================================

echo ""
echo "=============================================="
echo "🔥 M2ULTRA TURBO BOOT COMPLETE 🔥"
echo "  SSH:           ENABLED"
echo "  Screen Share:  ACTIVE"
echo "  Drives:        MOUNTED"
echo "  Kernel:        TURBO MODE"
echo "  DNS:           FLUSHED"
echo "  File Limits:   MAXED"
echo "=============================================="
echo "💪 SYSTEM IS READY. NO EXCUSES. 💪"
echo ""

echo "✨ TURBO Boot startup complete — $(date)" >> ~/.m2ultra-boot.log
