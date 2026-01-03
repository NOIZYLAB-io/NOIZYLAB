#!/bin/bash
set -e

LOG="$HOME/Desktop/recover_rsp_ms.log"
echo "Recovery run: $(date)" > "$LOG"

SRC="/Users/rsp_ms"
DST="$HOME/Recovered_rsp_ms"

echo "Checking source folder" | tee -a "$LOG"
if [ ! -d "$SRC" ]; then
  echo "ERROR: source $SRC not found" | tee -a "$LOG"
  exit 2
fi

echo "Creating destination..." | tee -a "$LOG"
mkdir -p "$DST"

echo "Copying Desktop..." | tee -a "$LOG"
sudo cp -Rp "$SRC/Desktop" "$DST/" 2>&1 | tee -a "$LOG"

echo "Copying Documents..." | tee -a "$LOG"
sudo cp -Rp "$SRC/Documents" "$DST/" 2>&1 | tee -a "$LOG"

echo "Copying GABRIEL folder..." | tee -a "$LOG"
sudo cp -Rp "$SRC/GABRIEL" "$DST/" 2>&1 | tee -a "$LOG" || true

echo "Copying NOIZYLAB..." | tee -a "$LOG"
sudo cp -Rp "$SRC/NOIZYLAB" "$DST/" 2>&1 | tee -a "$LOG" || true

echo "Fixing ownership..." | tee -a "$LOG"
sudo chown -R $(whoami):staff "$DST"

echo "" | tee -a "$LOG"
echo "✅ DONE!" | tee -a "$LOG"
echo "Files copied to: $DST" | tee -a "$LOG"
echo "Log saved to: $LOG" | tee -a "$LOG"

du -sh "$DST" | tee -a "$LOG"
