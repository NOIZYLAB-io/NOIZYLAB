#!/bin/bash
# NOIZYLAB DATABASE BACKUP SCRIPT
# Creates timestamped backups of the D1 database

set -e

DB_NAME="noizylab-repairs"
BACKUP_DIR="$HOME/noizylab-backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/noizylab_backup_$TIMESTAMP.sql"

echo "🔐 NOIZYLAB Database Backup"
echo "==========================="
echo ""

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

echo "📦 Creating backup..."
echo "Database: $DB_NAME"
echo "Destination: $BACKUP_FILE"
echo ""

# Export database
wrangler d1 export $DB_NAME --remote --output="$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "✅ Backup created successfully!"
    echo ""
    
    # Show backup size
    SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    echo "Backup size: $SIZE"
    echo "Location: $BACKUP_FILE"
    echo ""
    
    # Compress backup
    echo "🗜️  Compressing backup..."
    gzip "$BACKUP_FILE"
    COMPRESSED_FILE="$BACKUP_FILE.gz"
    COMPRESSED_SIZE=$(du -h "$COMPRESSED_FILE" | cut -f1)
    
    echo "✅ Compressed to: $COMPRESSED_SIZE"
    echo "Location: $COMPRESSED_FILE"
    echo ""
    
    # List recent backups
    echo "📂 Recent Backups:"
    ls -lht "$BACKUP_DIR" | head -10
    echo ""
    
    # Cleanup old backups (keep last 30)
    echo "🧹 Cleaning up old backups (keeping last 30)..."
    cd "$BACKUP_DIR"
    ls -t | tail -n +31 | xargs -r rm --
    
    echo ""
    echo "==========================="
    echo "✅ Backup complete!"
    
else
    echo "❌ Backup failed!"
    exit 1
fi

# Optional: Upload to cloud storage
# Uncomment and configure for your cloud provider

# Upload to S3
# echo "☁️  Uploading to S3..."
# aws s3 cp "$COMPRESSED_FILE" s3://your-bucket/noizylab-backups/

# Upload to Google Drive (requires rclone configured)
# echo "☁️  Uploading to Google Drive..."
# rclone copy "$COMPRESSED_FILE" gdrive:NOIZYLAB-Backups/

# Upload to Cloudflare R2 (when enabled)
# wrangler r2 object put noizylab-backups/backup_$TIMESTAMP.sql.gz --file="$COMPRESSED_FILE"

echo ""
echo "💡 To restore from this backup:"
echo "   gunzip $COMPRESSED_FILE"
echo "   wrangler d1 execute $DB_NAME --remote --file=${BACKUP_FILE}"
echo ""
echo "To automate daily backups, add to crontab:"
echo "   0 2 * * * $0"
echo "   (Runs daily at 2 AM)"
