#!/bin/zsh
# AutoKeep script for FishMusic Cockpit
# This script will periodically archive cockpit logs and scripts for backup.

COCKPIT_DIR="$HOME/fishmusic-cockpit"
ARCHIVE_DIR="$COCKPIT_DIR/archive"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

mkdir -p "$ARCHIVE_DIR"

# Archive logs and scripts
zip -r "$ARCHIVE_DIR/cockpit_backup_$TIMESTAMP.zip" "$COCKPIT_DIR/logs" "$COCKPIT_DIR/scanner" "$COCKPIT_DIR/tracer" "$COCKPIT_DIR/syncer" 2>/dev/null

echo "Cockpit logs and scripts archived to $ARCHIVE_DIR/cockpit_backup_$TIMESTAMP.zip"
