#!/bin/bash
# ==============================================================================
# ARCHIVE NOIZYLAB BLOAT
# Moves large directories to RED DRAGON for archival
# ==============================================================================

ARCHIVE_DIR="/Volumes/RED DRAGON/M2ULTRA_ARCHIVE_20260104/NOIZYLAB_BLOAT"
LOG_FILE="/Users/m2ultra/NOIZYLAB/logs/archive_bloat.log"

echo "$(date): Starting bloat archive" | tee -a "$LOG_FILE"

# 1. Archive GABRIEL/CODEMASTER (115GB)
echo "$(date): Archiving GABRIEL/CODEMASTER (115GB)..." | tee -a "$LOG_FILE"
rsync -av --progress /Users/m2ultra/NOIZYLAB/GABRIEL/CODEMASTER "$ARCHIVE_DIR/" 2>&1 | tee -a "$LOG_FILE"

if [ $? -eq 0 ]; then
    echo "$(date): CODEMASTER archived successfully" | tee -a "$LOG_FILE"
    echo "$(date): Removing original..." | tee -a "$LOG_FILE"
    rm -rf /Users/m2ultra/NOIZYLAB/GABRIEL/CODEMASTER
    echo "$(date): Original removed" | tee -a "$LOG_FILE"
else
    echo "$(date): ERROR archiving CODEMASTER" | tee -a "$LOG_FILE"
fi

# 2. Archive GABRIEL/ANTIGRAVITY_COMPLETE (1.6GB)
echo "$(date): Archiving ANTIGRAVITY_COMPLETE (1.6GB)..." | tee -a "$LOG_FILE"
rsync -av --progress /Users/m2ultra/NOIZYLAB/GABRIEL/ANTIGRAVITY_COMPLETE "$ARCHIVE_DIR/" 2>&1 | tee -a "$LOG_FILE"

if [ $? -eq 0 ]; then
    echo "$(date): ANTIGRAVITY_COMPLETE archived successfully" | tee -a "$LOG_FILE"
    echo "$(date): Removing original..." | tee -a "$LOG_FILE"
    rm -rf /Users/m2ultra/NOIZYLAB/GABRIEL/ANTIGRAVITY_COMPLETE
    echo "$(date): Original removed" | tee -a "$LOG_FILE"
else
    echo "$(date): ERROR archiving ANTIGRAVITY_COMPLETE" | tee -a "$LOG_FILE"
fi

echo "$(date): Archive complete!" | tee -a "$LOG_FILE"
echo "$(date): Freed approximately 117GB" | tee -a "$LOG_FILE"

# Play completion sound
afplay /System/Library/Sounds/Glass.aiff 2>/dev/null || true
