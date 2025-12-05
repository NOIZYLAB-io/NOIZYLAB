#!/bin/bash

VM="NOIZYWIN"
LOG="$HOME/noizylog/heal-noizywin.log"
mkdir -p "$(dirname "$LOG")"

echo "$(date): 🔮 Starting NOIZYWIN recovery ritual" >> "$LOG"

STATUS=$(prlctl list --all | grep "$VM" | awk '{print $2}')
echo "$(date): 🧭 Current status: $STATUS" >> "$LOG"

if [ "$STATUS" == "running" ] || [ "$STATUS" == "starting" ]; then
  echo "$(date): 🛑 Stopping VM..." >> "$LOG"
  prlctl stop "$VM" --kill
  sleep 3
fi

echo "$(date): 🔓 Disabling isolation..." >> "$LOG"
prlctl set "$VM" --isolation off

echo "$(date): 🛠️ Installing Parallels Tools..." >> "$LOG"
prlctl installtools "$VM"

echo "$(date): 🔁 Starting VM..." >> "$LOG"
prlctl start "$VM"
sleep 5

echo "$(date): 🧠 Launching Windows shell..." >> "$LOG"
prlctl exec "$VM" "cmd.exe /c start explorer"

echo "$(date): ✅ NOIZYWIN recovery complete" >> "$LOG"
