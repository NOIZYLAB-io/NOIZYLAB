#!/bin/bash
# iMessage Spam Filter V3 - Ultimate Upgrade
# ===========================================

set -e

MESSAGES_DB="$HOME/Library/Messages/chat.db"
BACKUP_DIR="$HOME/Library/Messages/backups"
LOG_FILE="$HOME/Library/Messages/spam-filter.log"
AUTO_FILTER_FILE="$HOME/Library/LaunchAgents/com.noizylab.imessage-spam-filter.plist"

# Enhanced patterns
SPAM_PATTERNS=(
    "Bounce-21" "bounce-" "unsubscribe" "click here" "limited time"
    "act now" "urgent" "congratulations" "you won" "prize"
    "free money" "claim now" "verify account" "suspended"
)

# AI-like scoring function
score_spam() {
    local text="$1"
    local sender="$2"
    local score=0
    
    # Pattern matching
    for pattern in "${SPAM_PATTERNS[@]}"; do
        if echo "$text" | grep -qi "$pattern"; then
            ((score += 10))
        fi
    done
    
    # URL count
    url_count=$(echo "$text" | grep -oE 'https?://[^[:space:]]+' | wc -l | tr -d ' ')
    ((score += url_count * 5))
    
    # Caps ratio
    caps=$(echo "$text" | grep -o '[A-Z]' | wc -l | tr -d ' ')
    total=$(echo "$text" | wc -c | tr -d ' ')
    if [ "$total" -gt 0 ]; then
        ratio=$((caps * 100 / total))
        if [ "$ratio" -gt 50 ]; then
            ((score += 10))
        fi
    fi
    
    echo "$score"
}

# Smart delete with scoring
smart_delete_v3() {
    log "🧠 Smart delete V3 - AI-like scoring..."
    
    backup_database
    
    DELETED=0
    HIGH_SCORE=0
    MEDIUM_SCORE=0
    
    # Process messages
    sqlite3 "$MESSAGES_DB" "SELECT ROWID, text, handle.id FROM message LEFT JOIN handle ON message.handle_id = handle.ROWID WHERE text IS NOT NULL" | while IFS="|" read -r rowid text sender; do
        score=$(score_spam "$text" "$sender")
        
        if [ "$score" -ge 30 ]; then
            sqlite3 "$MESSAGES_DB" "DELETE FROM message WHERE ROWID = $rowid" 2>/dev/null
            ((DELETED++))
            ((HIGH_SCORE++))
        elif [ "$score" -ge 15 ]; then
            ((MEDIUM_SCORE++))
        fi
    done
    
    success "Deleted $DELETED high-score spam (score >= 30)"
    log "Medium-risk: $MEDIUM_SCORE messages"
    
    # Optimize
    sqlite3 "$MESSAGES_DB" "VACUUM;" 2>/dev/null
}

# Auto-filter with smart scheduling
enable_auto_filter_v3() {
    log "🔄 Enabling auto-filter V3..."
    
    SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
    
    cat > "$AUTO_FILTER_FILE" << PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizylab.imessage-spam-filter</string>
    <key>ProgramArguments</key>
    <array>
        <string>$SCRIPT_PATH</string>
        <string>--auto-delete</string>
    </array>
    <key>StartInterval</key>
    <integer>1800</integer>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
PLIST
    
    launchctl load "$AUTO_FILTER_FILE" 2>/dev/null || launchctl load -w "$AUTO_FILTER_FILE"
    success "Auto-filter enabled (runs every 30 minutes)"
}

# Main
if [ "$1" = "--auto-delete" ]; then
    smart_delete_v3
    exit 0
fi

# Interactive menu
clear
echo "📱 iMessage Spam Filter V3"
echo ""
echo "1) 🧠 Smart Delete (AI scoring)"
echo "2) 🔄 Enable Auto-Filter"
echo "3) 📊 Statistics"
echo ""
read -p "Choice: " choice

case "$choice" in
    1) smart_delete_v3 ;;
    2) enable_auto_filter_v3 ;;
    3) 
        TOTAL=$(sqlite3 "$MESSAGES_DB" "SELECT COUNT(*) FROM message;" 2>/dev/null || echo "0")
        SPAM=$(sqlite3 "$MESSAGES_DB" "SELECT COUNT(*) FROM message WHERE text LIKE '%Bounce-21%';" 2>/dev/null || echo "0")
        echo "Total: $TOTAL | Bounce-21: $SPAM"
        ;;
esac

