#!/bin/bash
# iMessage Spam Filter V2 - Enhanced with AI Detection & Auto-Filtering
# ======================================================================

set -e

MESSAGES_DB="$HOME/Library/Messages/chat.db"
BACKUP_DIR="$HOME/Library/Messages/backups"
LOG_FILE="$HOME/Library/Messages/spam-filter.log"
AUTO_FILTER_FILE="$HOME/Library/LaunchAgents/com.noizylab.imessage-spam-filter.plist"

# Enhanced spam patterns with AI-like detection
SPAM_PATTERNS=(
    "Bounce-21"
    "bounce-"
    "unsubscribe"
    "click here"
    "limited time"
    "act now"
    "urgent"
    "congratulations"
    "you won"
    "prize"
    "free money"
    "claim now"
    "verify account"
    "suspended"
    "expired"
    "renew now"
    "your account"
    "immediate action"
    "click below"
    "limited offer"
)

# Suspicious sender patterns
SUSPICIOUS_SENDERS=(
    "@.*\.tk$"
    "@.*\.ml$"
    "@.*\.ga$"
    "@.*\.cf$"
    "noreply"
    "no-reply"
    "donotreply"
)

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

log() {
    echo -e "${BLUE}[spam-filter-v2]${NC} $1" | tee -a "$LOG_FILE"
}

success() {
    echo -e "${GREEN}✔️${NC} $1" | tee -a "$LOG_FILE"
}

error() {
    echo -e "${RED}❌${NC} $1" | tee -a "$LOG_FILE"
}

warn() {
    echo -e "${YELLOW}⚠️${NC} $1" | tee -a "$LOG_FILE"
}

# AI-like spam detection (heuristic scoring)
detect_spam_score() {
    local text="$1"
    local sender="$2"
    local score=0
    
    # Check patterns
    for pattern in "${SPAM_PATTERNS[@]}"; do
        if echo "$text" | grep -qi "$pattern"; then
            ((score += 10))
        fi
    done
    
    # Check sender
    for sus_sender in "${SUSPICIOUS_SENDERS[@]}"; do
        if echo "$sender" | grep -qiE "$sus_sender"; then
            ((score += 15))
        fi
    done
    
    # Check for URLs (spam often has many)
    url_count=$(echo "$text" | grep -oE 'https?://[^[:space:]]+' | wc -l | tr -d ' ')
    if [ "$url_count" -gt 2 ]; then
        ((score += 5 * url_count))
    fi
    
    # Check for excessive caps
    caps_ratio=$(echo "$text" | grep -o '[A-Z]' | wc -l | tr -d ' ')
    total_chars=$(echo "$text" | wc -c | tr -d ' ')
    if [ "$total_chars" -gt 0 ]; then
        ratio=$((caps_ratio * 100 / total_chars))
        if [ "$ratio" -gt 50 ]; then
            ((score += 10))
        fi
    fi
    
    # Check for phone numbers (spam often includes them)
    if echo "$text" | grep -qE '[0-9]{3}[-. ]?[0-9]{3}[-. ]?[0-9]{4}'; then
        ((score += 5))
    fi
    
    echo "$score"
}

# Enhanced scan with scoring
scan_spam_enhanced() {
    log "🔍 Enhanced spam scan with AI-like detection..."
    echo ""
    
    # Build query
    PATTERN_CONDITIONS=""
    for pattern in "${SPAM_PATTERNS[@]}"; do
        if [ -n "$PATTERN_CONDITIONS" ]; then
            PATTERN_CONDITIONS="$PATTERN_CONDITIONS OR "
        fi
        PATTERN_CONDITIONS="$PATTERN_CONDITIONS text LIKE '%$pattern%'"
    done
    
    QUERY="SELECT 
        message.ROWID,
        datetime(message.date/1000000000 + strftime('%s', '2001-01-01'), 'unixepoch', 'localtime') as date,
        handle.id as sender,
        message.text as message
    FROM message
    LEFT JOIN handle ON message.handle_id = handle.ROWID
    WHERE ($PATTERN_CONDITIONS)
    ORDER BY message.date DESC
    LIMIT 100;"
    
    # Get messages and score them
    HIGH_SCORE=0
    MEDIUM_SCORE=0
    LOW_SCORE=0
    
    sqlite3 -separator "|" "$MESSAGES_DB" "$QUERY" | while IFS="|" read -r rowid date sender text; do
        score=$(detect_spam_score "$text" "$sender")
        
        if [ "$score" -ge 30 ]; then
            ((HIGH_SCORE++))
            echo -e "${RED}🔴 HIGH ($score):${NC} $sender - ${text:0:60}..."
        elif [ "$score" -ge 15 ]; then
            ((MEDIUM_SCORE++))
            echo -e "${YELLOW}🟡 MEDIUM ($score):${NC} $sender - ${text:0:60}..."
        else
            ((LOW_SCORE++))
            echo -e "${GREEN}🟢 LOW ($score):${NC} $sender - ${text:0:60}..."
        fi
    done
    
    echo ""
    echo "Spam Scores:"
    echo "  🔴 High risk: $HIGH_SCORE"
    echo "  🟡 Medium risk: $MEDIUM_SCORE"
    echo "  🟢 Low risk: $LOW_SCORE"
}

# Smart delete (only high-score spam)
smart_delete() {
    log "🧠 Smart delete - removing high-score spam only..."
    
    warn "This will delete messages with spam score >= 30"
    read -p "Continue? [y/N]: " confirm
    
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        log "Cancelled"
        return
    fi
    
    backup_database
    
    DELETED=0
    
    # Get all messages and score them
    PATTERN_CONDITIONS=""
    for pattern in "${SPAM_PATTERNS[@]}"; do
        if [ -n "$PATTERN_CONDITIONS" ]; then
            PATTERN_CONDITIONS="$PATTERN_CONDITIONS OR "
        fi
        PATTERN_CONDITIONS="$PATTERN_CONDITIONS text LIKE '%$pattern%'"
    done
    
    QUERY="SELECT message.ROWID, message.text, handle.id
    FROM message
    LEFT JOIN handle ON message.handle_id = handle.ROWID
    WHERE ($PATTERN_CONDITIONS);"
    
    sqlite3 -separator "|" "$MESSAGES_DB" "$QUERY" | while IFS="|" read -r rowid text sender; do
        score=$(detect_spam_score "$text" "$sender")
        
        if [ "$score" -ge 30 ]; then
            sqlite3 "$MESSAGES_DB" "DELETE FROM message WHERE ROWID = $rowid;" 2>/dev/null
            ((DELETED++))
        fi
    done
    
    success "Deleted $DELETED high-score spam messages"
    
    # Optimize
    sqlite3 "$MESSAGES_DB" "VACUUM;" 2>/dev/null
}

# Auto-filter with launch agent
enable_auto_filter() {
    log "🔄 Enabling auto-filter..."
    
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
    <integer>3600</integer>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
PLIST
    
    launchctl load "$AUTO_FILTER_FILE" 2>/dev/null || true
    success "Auto-filter enabled (runs every hour)"
}

# Backup database
backup_database() {
    mkdir -p "$BACKUP_DIR"
    BACKUP="$BACKUP_DIR/chat_$(date +%Y%m%d_%H%M%S).db"
    cp "$MESSAGES_DB" "$BACKUP"
    success "Backup: $BACKUP"
}

# Auto-delete mode
if [ "$1" = "--auto-delete" ]; then
    smart_delete
    exit 0
fi

# Enhanced menu
clear
echo -e "${CYAN}${BOLD}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║         📱 iMessage Spam Filter V2                          ║"
echo "║         Enhanced with AI-like Detection                      ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""
echo "Options:"
echo "  1) 🔍 Enhanced Scan (with spam scoring)"
echo "  2) 🧠 Smart Delete (high-score only)"
echo "  3) 🗑️  Delete All Spam"
echo "  4) 🔄 Enable Auto-Filter"
echo "  5) 📊 Statistics"
echo "  0) Exit"
echo ""
read -p "Choice: " choice

case "$choice" in
    1) scan_spam_enhanced ;;
    2) smart_delete ;;
    3) 
        backup_database
        # Delete all matching patterns
        PATTERN_CONDITIONS=""
        for pattern in "${SPAM_PATTERNS[@]}"; do
            if [ -n "$PATTERN_CONDITIONS" ]; then
                PATTERN_CONDITIONS="$PATTERN_CONDITIONS OR "
            fi
            PATTERN_CONDITIONS="$PATTERN_CONDITIONS text LIKE '%$pattern%'"
        done
        DELETED=$(sqlite3 "$MESSAGES_DB" "DELETE FROM message WHERE ($PATTERN_CONDITIONS); SELECT changes();")
        success "Deleted $DELETED messages"
        sqlite3 "$MESSAGES_DB" "VACUUM;"
        ;;
    4) enable_auto_filter ;;
    5)
        TOTAL=$(sqlite3 "$MESSAGES_DB" "SELECT COUNT(*) FROM message;")
        SPAM=$(sqlite3 "$MESSAGES_DB" "SELECT COUNT(*) FROM message WHERE text LIKE '%Bounce-21%';")
        echo "Total messages: $TOTAL"
        echo "Bounce-21 spam: $SPAM"
        ;;
esac

