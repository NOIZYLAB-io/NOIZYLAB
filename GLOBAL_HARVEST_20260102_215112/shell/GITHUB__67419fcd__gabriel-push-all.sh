#!/bin/bash
# ============================================================================
# MC96ECOUNIVERSE - Push GABRIEL to all devices
# ============================================================================

GABRIEL_SRC="/Users/m2ultra/NOIZYLAB/GABRIEL"
LOG_FILE="/tmp/gabriel-sync.log"

echo "=== GABRIEL SYNC - $(date) ===" >> "$LOG_FILE"

# Sync to DaFixer (if online)
if tailscale ping dafixer --timeout=2s &>/dev/null; then
    echo "[SYNC] Pushing to DaFixer..." >> "$LOG_FILE"
    rsync -avz --delete \
        --exclude '.git' \
        --exclude 'node_modules' \
        --exclude '__pycache__' \
        --exclude '*.pyc' \
        --exclude '.env*' \
        --exclude 'memcell_data/*.json' \
        "$GABRIEL_SRC/" dafixer:/Users/m2ultra/NOIZYLAB/GABRIEL/ >> "$LOG_FILE" 2>&1
else
    echo "[SKIP] DaFixer offline" >> "$LOG_FILE"
fi

# Sync to GABRIEL-WSL (if online)
if tailscale ping gabriel-wsl --timeout=2s &>/dev/null; then
    echo "[SYNC] Pushing to GABRIEL-WSL..." >> "$LOG_FILE"
    rsync -avz --delete \
        --exclude '.git' \
        --exclude 'node_modules' \
        --exclude '__pycache__' \
        --exclude '*.pyc' \
        --exclude '.env*' \
        --exclude 'memcell_data/*.json' \
        "$GABRIEL_SRC/" gabriel-wsl:~/NOIZYLAB/GABRIEL/ >> "$LOG_FILE" 2>&1
else
    echo "[SKIP] GABRIEL-WSL offline" >> "$LOG_FILE"
fi

echo "=== Sync complete ===" >> "$LOG_FILE"
