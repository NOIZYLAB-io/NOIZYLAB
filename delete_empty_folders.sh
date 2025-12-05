#!/bin/bash
# Delete all empty folders

ROOT="/Volumes/MAG 4TB"
LOG="/Volumes/MAG 4TB/NoizyWorkspace/deleted_empty_folders.log"

echo "DELETING EMPTY FOLDERS" | tee "$LOG"
echo "Root: $ROOT" | tee -a "$LOG"
echo "Started: $(date)" | tee -a "$LOG"
echo "========================================" | tee -a "$LOG"

# Find and count empty directories first
echo -e "\nFinding empty directories..." | tee -a "$LOG"
EMPTY_DIRS=$(find "$ROOT" -type d -empty -not -path "*/.*" 2>/dev/null)
COUNT=$(echo "$EMPTY_DIRS" | grep -c '^' 2>/dev/null || echo "0")

echo "Found $COUNT empty directories" | tee -a "$LOG"

if [ "$COUNT" -gt 0 ]; then
    echo -e "\nDeleting empty directories..." | tee -a "$LOG"
    
    # Delete them and log
    find "$ROOT" -type d -empty -not -path "*/.*" -print -delete 2>/dev/null | tee -a "$LOG"
    
    # Run multiple passes to catch nested empty directories
    for i in {1..5}; do
        REMAINING=$(find "$ROOT" -type d -empty -not -path "*/.*" 2>/dev/null | wc -l | tr -d ' ')
        if [ "$REMAINING" -gt 0 ]; then
            echo -e "\nPass $i: Found $REMAINING more empty directories" | tee -a "$LOG"
            find "$ROOT" -type d -empty -not -path "*/.*" -print -delete 2>/dev/null | tee -a "$LOG"
        else
            break
        fi
    done
fi

# Final check
FINAL=$(find "$ROOT" -type d -empty -not -path "*/.*" 2>/dev/null | wc -l | tr -d ' ')

echo -e "\n========================================" | tee -a "$LOG"
echo "COMPLETE" | tee -a "$LOG"
echo "Remaining empty directories: $FINAL" | tee -a "$LOG"
echo "Finished: $(date)" | tee -a "$LOG"
echo "Log saved to: $LOG" | tee -a "$LOG"

