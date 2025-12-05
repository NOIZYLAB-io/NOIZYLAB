#!/bin/bash
# ==========================================================
# SUPER MOUNT & SYNC - GABRIEL NODE
# ==========================================================

declare -A SHARES=(
  ["SharedMusic"]="192.168.1.24:rsp_ms"
  ["SharedDocs"]="192.168.1.24:rsp_ms"
)

for NAME in "${!SHARES[@]}"; do
  IP="${SHARES[$NAME]%%:*}"
  USER="${SHARES[$NAME]##*:}"
  MOUNT="/Volumes/$NAME"

  ping -c1 -W1 "$IP" >/dev/null 2>&1 || { echo "❌ $IP offline"; continue; }

  [[ -d "$MOUNT" ]] || mkdir -p "$MOUNT"
  mount | grep -q "on $MOUNT" && { echo "✅ $NAME already mounted"; continue; }

  echo "⚡ Mounting $NAME..."
  mount_smbfs "//$USER@$IP/$NAME" "$MOUNT" && echo "💽 $NAME mounted at $MOUNT" || echo "🚫 Mount failed: $NAME"
done

echo "🔄 Sync check complete — ready for agent ops."
