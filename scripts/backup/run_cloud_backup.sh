#!/bin/bash
# ☁️ CLOUD BACKUP - AUTOMATED BACKUPS
# Fish Music Inc - CB_01

echo "☁️ OMEGA CLOUD BACKUP"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

BACKUP_SOURCE="/Users/m2ultra/NOIZYLAB"
BACKUP_DEST="/Volumes/4TB_02/Backups/OMEGA_$(date +%Y%m%d_%H%M%S)"

echo "Source:      $BACKUP_SOURCE"
echo "Destination: $BACKUP_DEST"
echo ""

# Create backup directory
echo "[+] Creating backup directory..."
mkdir -p "$BACKUP_DEST"

# Use rsync for efficient backup
echo "[+] Starting backup (rsync)..."
rsync -avz \
    --progress \
    --exclude='.git' \
    --exclude='node_modules' \
    --exclude='__pycache__' \
    --exclude='.DS_Store' \
    "$BACKUP_SOURCE/" \
    "$BACKUP_DEST/"

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Backup complete!"
    echo "   Location: $BACKUP_DEST"
    
    # Calculate size
    SIZE=$(du -sh "$BACKUP_DEST" | awk '{print $1}')
    echo "   Size: $SIZE"
    
    # Create backup log
    echo "$(date): Backup complete - $SIZE" >> ~/Library/Logs/OMEGA/backup.log
else
    echo ""
    echo "❌ Backup failed!"
    exit 1
fi

echo ""
echo "🔥 GORUNFREE! 🎸🔥"
