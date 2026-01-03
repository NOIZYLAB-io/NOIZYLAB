#!/bin/bash
# Quick Spam Filter - Fast deletion of Bounce-21 spam
# ====================================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
FILTER_SCRIPT="$SCRIPT_DIR/imessage-spam-filter.sh"

echo "📱 Quick Spam Filter - Removing Bounce-21 spam..."
echo ""

# Run the main script with auto-delete for Bounce-21
cd "$SCRIPT_DIR"

# Quick scan first
echo "Scanning for Bounce-21 messages..."
COUNT=$(sqlite3 "$HOME/Library/Messages/chat.db" "SELECT COUNT(*) FROM message WHERE text LIKE '%Bounce-21%';" 2>/dev/null || echo "0")

if [ "$COUNT" = "0" ] || [ -z "$COUNT" ]; then
    echo "✅ No Bounce-21 spam found!"
    exit 0
fi

echo "Found $COUNT Bounce-21 messages"
echo ""
read -p "Delete them? (yes/no): " confirm

if [ "$confirm" = "yes" ]; then
    # Create backup
    mkdir -p "$HOME/Library/Messages/backups"
    BACKUP="$HOME/Library/Messages/backups/chat_$(date +%Y%m%d_%H%M%S).db"
    cp "$HOME/Library/Messages/chat.db" "$BACKUP"
    echo "✅ Backup created: $BACKUP"
    
    # Delete Bounce-21 messages
    DELETED=$(sqlite3 "$HOME/Library/Messages/chat.db" "DELETE FROM message WHERE text LIKE '%Bounce-21%'; SELECT changes();")
    
    echo "✅ Deleted $DELETED Bounce-21 spam messages"
    
    # Optimize database
    sqlite3 "$HOME/Library/Messages/chat.db" "VACUUM;" 2>/dev/null
    echo "✅ Database optimized"
else
    echo "Cancelled"
fi

