#!/bin/bash
# AUTOMATED BACKUP SYSTEM
# Protects all AI GENIUS files with versioning
# FORT KNOX security protocol

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m'

# Backup configuration
BACKUP_ROOT=~/ai-genius-backups
DAILY_DIR=$BACKUP_ROOT/daily
WEEKLY_DIR=$BACKUP_ROOT/weekly
MONTHLY_DIR=$BACKUP_ROOT/monthly
EMERGENCY_DIR=$BACKUP_ROOT/emergency

# Retention policy
KEEP_DAILY=7
KEEP_WEEKLY=4
KEEP_MONTHLY=12

# Directories to backup
BACKUP_SOURCES=(
    ~/ai-genius
    ~/ai-genius-pro
    ~/noizylab-perfect
    ~/.ai-genius-stats.json
    ~/.ai-genius.log
)

mkdir -p "$DAILY_DIR" "$WEEKLY_DIR" "$MONTHLY_DIR" "$EMERGENCY_DIR"

echo -e "${PURPLE}╔═══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                                                               ║${NC}"
echo -e "${PURPLE}║         💾 AUTOMATED BACKUP SYSTEM 💾                         ║${NC}"
echo -e "${PURPLE}║                                                               ║${NC}"
echo -e "${PURPLE}║         FORT KNOX Security Protocol Active                    ║${NC}"
echo -e "${PURPLE}║                                                               ║${NC}"
echo -e "${PURPLE}╚═══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Determine backup type
BACKUP_TYPE=${1:-"daily"}
TODAY=$(date +%Y-%m-%d)
NOW=$(date +%Y-%m-%d_%H-%M-%S)

case $BACKUP_TYPE in
    daily)
        BACKUP_DIR="$DAILY_DIR/$NOW"
        echo -e "${CYAN}📅 Running DAILY backup${NC}"
        ;;
    weekly)
        BACKUP_DIR="$WEEKLY_DIR/$NOW"
        echo -e "${CYAN}📆 Running WEEKLY backup${NC}"
        ;;
    monthly)
        BACKUP_DIR="$MONTHLY_DIR/$NOW"
        echo -e "${CYAN}📆 Running MONTHLY backup${NC}"
        ;;
    emergency)
        BACKUP_DIR="$EMERGENCY_DIR/$NOW"
        echo -e "${RED}🚨 Running EMERGENCY backup${NC}"
        ;;
    *)
        echo -e "${RED}Invalid backup type. Use: daily, weekly, monthly, emergency${NC}"
        exit 1
        ;;
esac

echo ""
mkdir -p "$BACKUP_DIR"

# Backup function with progress
backup_source() {
    SOURCE=$1
    NAME=$(basename "$SOURCE")
    
    if [ ! -e "$SOURCE" ]; then
        echo -e "${YELLOW}⚠ Skipping $NAME (not found)${NC}"
        return
    fi
    
    echo -n "  Backing up $NAME... "
    
    if [ -d "$SOURCE" ]; then
        # Directory backup with tar
        tar -czf "$BACKUP_DIR/${NAME}.tar.gz" -C "$(dirname "$SOURCE")" "$NAME" 2>/dev/null
        SIZE=$(du -sh "$BACKUP_DIR/${NAME}.tar.gz" 2>/dev/null | cut -f1)
    else
        # File backup
        cp "$SOURCE" "$BACKUP_DIR/${NAME}"
        SIZE=$(du -sh "$BACKUP_DIR/${NAME}" 2>/dev/null | cut -f1)
    fi
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ ($SIZE)${NC}"
    else
        echo -e "${RED}✗ Failed${NC}"
    fi
}

# Perform backups
echo -e "${CYAN}Backing up sources...${NC}"
for SOURCE in "${BACKUP_SOURCES[@]}"; do
    backup_source "$SOURCE"
done

# Create backup manifest
echo -e "${CYAN}Creating manifest...${NC}"
cat > "$BACKUP_DIR/MANIFEST.txt" << EOFMANIFEST
AI GENIUS BACKUP MANIFEST
========================

Backup Type: $BACKUP_TYPE
Timestamp: $NOW
Date: $(date)

SOURCES BACKED UP:
-----------------
EOFMANIFEST

for SOURCE in "${BACKUP_SOURCES[@]}"; do
    if [ -e "$SOURCE" ]; then
        echo "✓ $(basename "$SOURCE")" >> "$BACKUP_DIR/MANIFEST.txt"
    else
        echo "✗ $(basename "$SOURCE") (not found)" >> "$BACKUP_DIR/MANIFEST.txt"
    fi
done

cat >> "$BACKUP_DIR/MANIFEST.txt" << EOFMANIFEST

BACKUP LOCATION:
---------------
$BACKUP_DIR

TOTAL SIZE:
----------
$(du -sh "$BACKUP_DIR" | cut -f1)

RESTORE INSTRUCTIONS:
--------------------
To restore this backup:
1. cd $BACKUP_DIR
2. tar -xzf ai-genius.tar.gz -C ~/
3. tar -xzf ai-genius-pro.tar.gz -C ~/
4. tar -xzf noizylab-perfect.tar.gz -C ~/

Or run: ~/ai-genius-backups/restore-backup.sh $NOW

VERIFICATION:
------------
MD5 checksums:
EOFMANIFEST

# Add checksums
cd "$BACKUP_DIR"
for file in *.tar.gz; do
    if [ -f "$file" ]; then
        md5sum "$file" 2>/dev/null | sed 's/^/  /' >> MANIFEST.txt
    fi
done

echo -e "${GREEN}✓ Manifest created${NC}"

# Clean old backups based on retention policy
echo ""
echo -e "${CYAN}Cleaning old backups...${NC}"

case $BACKUP_TYPE in
    daily)
        CLEANUP_DIR=$DAILY_DIR
        KEEP=$KEEP_DAILY
        ;;
    weekly)
        CLEANUP_DIR=$WEEKLY_DIR
        KEEP=$KEEP_WEEKLY
        ;;
    monthly)
        CLEANUP_DIR=$MONTHLY_DIR
        KEEP=$KEEP_MONTHLY
        ;;
    emergency)
        # Never auto-clean emergency backups
        CLEANUP_DIR=""
        ;;
esac

if [ ! -z "$CLEANUP_DIR" ]; then
    COUNT=$(ls -1 "$CLEANUP_DIR" 2>/dev/null | wc -l)
    if [ $COUNT -gt $KEEP ]; then
        TO_DELETE=$((COUNT - KEEP))
        ls -1t "$CLEANUP_DIR" | tail -$TO_DELETE | while read OLD_BACKUP; do
            echo -n "  Removing old backup: $OLD_BACKUP... "
            rm -rf "$CLEANUP_DIR/$OLD_BACKUP"
            echo -e "${GREEN}✓${NC}"
        done
    else
        echo -e "${GREEN}✓ No cleanup needed ($COUNT backups, keeping $KEEP)${NC}"
    fi
fi

# Create restore script
cat > "$BACKUP_ROOT/restore-backup.sh" << 'EOFRESTORE'
#!/bin/bash
# Restore from backup

GREEN='\033[0;32m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

if [ -z "$1" ]; then
    echo -e "${RED}Usage: $0 <backup-timestamp>${NC}"
    echo ""
    echo "Available backups:"
    ls -1 ~/ai-genius-backups/*/ 2>/dev/null | grep -o "[0-9].*" | sort -r | head -20
    exit 1
fi

BACKUP_TS=$1
FOUND=0

for TYPE in daily weekly monthly emergency; do
    BACKUP_DIR=~/ai-genius-backups/$TYPE/$BACKUP_TS
    if [ -d "$BACKUP_DIR" ]; then
        FOUND=1
        break
    fi
done

if [ $FOUND -eq 0 ]; then
    echo -e "${RED}Backup not found: $BACKUP_TS${NC}"
    exit 1
fi

echo -e "${CYAN}Restoring from: $BACKUP_DIR${NC}"
echo ""

read -p "This will overwrite current files. Continue? (yes/no): " CONFIRM
if [ "$CONFIRM" != "yes" ]; then
    echo "Cancelled"
    exit 0
fi

cd "$BACKUP_DIR"

for archive in *.tar.gz; do
    if [ -f "$archive" ]; then
        echo -n "Restoring $archive... "
        tar -xzf "$archive" -C ~/ 2>/dev/null
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓${NC}"
        else
            echo -e "${RED}✗${NC}"
        fi
    fi
done

# Restore individual files
for file in .ai-genius*; do
    if [ -f "$file" ]; then
        cp "$file" ~/
    fi
done

echo ""
echo -e "${GREEN}✓ Restore complete${NC}"
echo ""
echo "Restored files:"
echo "  ~/ai-genius/"
echo "  ~/ai-genius-pro/"
echo "  ~/noizylab-perfect/"
echo ""
EOFRESTORE
chmod +x "$BACKUP_ROOT/restore-backup.sh"

# Summary
echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}${BOLD}✅ BACKUP COMPLETE${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${CYAN}Backup Location:${NC}    $BACKUP_DIR"
echo -e "${CYAN}Backup Type:${NC}        $BACKUP_TYPE"
echo -e "${CYAN}Timestamp:${NC}          $NOW"
echo -e "${CYAN}Total Size:${NC}         $(du -sh "$BACKUP_DIR" | cut -f1)"
echo ""
echo -e "${CYAN}Backup Statistics:${NC}"
echo -e "  Daily backups:    $(ls -1 "$DAILY_DIR" 2>/dev/null | wc -l)"
echo -e "  Weekly backups:   $(ls -1 "$WEEKLY_DIR" 2>/dev/null | wc -l)"
echo -e "  Monthly backups:  $(ls -1 "$MONTHLY_DIR" 2>/dev/null | wc -l)"
echo -e "  Emergency backups: $(ls -1 "$EMERGENCY_DIR" 2>/dev/null | wc -l)"
echo ""
echo -e "${CYAN}To restore this backup:${NC}"
echo "  $BACKUP_ROOT/restore-backup.sh $NOW"
echo ""
echo -e "${CYAN}To view manifest:${NC}"
echo "  cat $BACKUP_DIR/MANIFEST.txt"
echo ""

# Create cron job file for automated backups
cat > "$BACKUP_ROOT/setup-auto-backup.sh" << 'EOFCRON'
#!/bin/bash
# Setup automated backups

BACKUP_SCRIPT=~/ai-genius-backups/backup.sh

# Copy this script to backup directory
cp "$(dirname "$0")"/../noizylab-perfect/automated-backup.sh "$BACKUP_SCRIPT"
chmod +x "$BACKUP_SCRIPT"

echo "Setting up automated backups..."

# Add to crontab
(crontab -l 2>/dev/null; echo "# AI GENIUS Automated Backups") | crontab -
(crontab -l 2>/dev/null; echo "0 2 * * * $BACKUP_SCRIPT daily >/dev/null 2>&1") | crontab -
(crontab -l 2>/dev/null; echo "0 3 * * 0 $BACKUP_SCRIPT weekly >/dev/null 2>&1") | crontab -
(crontab -l 2>/dev/null; echo "0 4 1 * * $BACKUP_SCRIPT monthly >/dev/null 2>&1") | crontab -

echo "✓ Automated backups configured"
echo ""
echo "Schedule:"
echo "  Daily:   2:00 AM every day"
echo "  Weekly:  3:00 AM every Sunday"
echo "  Monthly: 4:00 AM first day of month"
echo ""
echo "To check: crontab -l"
echo "To disable: crontab -r"
EOFCRON
chmod +x "$BACKUP_ROOT/setup-auto-backup.sh"

echo -e "${YELLOW}💡 Tip: Run $BACKUP_ROOT/setup-auto-backup.sh to enable automated backups${NC}"
echo ""
