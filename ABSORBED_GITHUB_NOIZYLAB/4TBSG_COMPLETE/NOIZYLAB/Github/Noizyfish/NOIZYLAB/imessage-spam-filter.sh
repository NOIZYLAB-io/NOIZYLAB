#!/bin/bash
# iMessage Spam Filter - Filter and remove spam messages
# ======================================================

set -e

# Configuration
MESSAGES_DB="$HOME/Library/Messages/chat.db"
BACKUP_DIR="$HOME/Library/Messages/backups"
SPAM_PATTERNS=(
    "Bounce-21"
    "Bounce-"
    "bounce"
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
)

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

log() {
    echo -e "${BLUE}[spam-filter]${NC} $1"
}

success() {
    echo -e "${GREEN}✔️${NC} $1"
}

error() {
    echo -e "${RED}❌${NC} $1"
}

warn() {
    echo -e "${YELLOW}⚠️${NC} $1"
}

# Check if Messages database exists
if [ ! -f "$MESSAGES_DB" ]; then
    error "Messages database not found at $MESSAGES_DB"
    exit 1
fi

# Check if sqlite3 is available
if ! command -v sqlite3 >/dev/null 2>&1; then
    error "sqlite3 not found. Install with: brew install sqlite"
    exit 1
fi

# Create backup
backup_database() {
    log "Creating backup..."
    mkdir -p "$BACKUP_DIR"
    BACKUP_FILE="$BACKUP_DIR/chat_$(date +%Y%m%d_%H%M%S).db"
    cp "$MESSAGES_DB" "$BACKUP_FILE"
    success "Backup created: $BACKUP_FILE"
}

# Show menu
show_menu() {
    clear
    echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║                                                              ║${NC}"
    echo -e "${CYAN}║         📱 iMessage Spam Filter                             ║${NC}"
    echo -e "${CYAN}║                                                              ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${BLUE}Options:${NC}"
    echo ""
    echo -e "  ${GREEN}1)${NC} 🔍 Scan for spam messages (preview only)"
    echo -e "  ${GREEN}2)${NC} 🗑️  Delete spam messages"
    echo -e "  ${GREEN}3)${NC} 📊 Show spam statistics"
    echo -e "  ${GREEN}4)${NC} ⚙️  Configure spam patterns"
    echo -e "  ${GREEN}5)${NC} 🔄 Auto-filter (run in background)"
    echo -e "  ${GREEN}6)${NC} 📋 View recent spam messages"
    echo -e "  ${GREEN}0)${NC} 🚪 Exit"
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "${YELLOW}Enter your choice [0-6]:${NC} "
}

# Scan for spam
scan_spam() {
    log "Scanning for spam messages..."
    echo ""
    
    # Build SQL query with all patterns
    PATTERN_CONDITIONS=""
    for pattern in "${SPAM_PATTERNS[@]}"; do
        if [ -n "$PATTERN_CONDITIONS" ]; then
            PATTERN_CONDITIONS="$PATTERN_CONDITIONS OR "
        fi
        PATTERN_CONDITIONS="$PATTERN_CONDITIONS text LIKE '%$pattern%'"
    done
    
    QUERY="SELECT 
        datetime(message.date/1000000000 + strftime('%s', '2001-01-01'), 'unixepoch', 'localtime') as date,
        handle.id as sender,
        message.text as message
    FROM message
    LEFT JOIN handle ON message.handle_id = handle.ROWID
    WHERE ($PATTERN_CONDITIONS)
    ORDER BY message.date DESC
    LIMIT 50;"
    
    COUNT=$(sqlite3 "$MESSAGES_DB" "SELECT COUNT(*) FROM message WHERE ($PATTERN_CONDITIONS);")
    
    echo -e "${YELLOW}Found $COUNT spam messages${NC}"
    echo ""
    
    if [ "$COUNT" -gt 0 ]; then
        sqlite3 -header -column "$MESSAGES_DB" "$QUERY" | head -20
        echo ""
        echo -e "${YELLOW}Showing first 20 results. Total: $COUNT${NC}"
    else
        success "No spam messages found!"
    fi
}

# Delete spam messages
delete_spam() {
    warn "This will DELETE spam messages from your Messages database!"
    read -p "Are you sure? Type 'yes' to continue: " confirm
    
    if [ "$confirm" != "yes" ]; then
        log "Cancelled"
        return
    fi
    
    backup_database
    
    log "Deleting spam messages..."
    
    # Build pattern conditions
    PATTERN_CONDITIONS=""
    for pattern in "${SPAM_PATTERNS[@]}"; do
        if [ -n "$PATTERN_CONDITIONS" ]; then
            PATTERN_CONDITIONS="$PATTERN_CONDITIONS OR "
        fi
        PATTERN_CONDITIONS="$PATTERN_CONDITIONS text LIKE '%$pattern%'"
    done
    
    # Delete messages
    DELETED=$(sqlite3 "$MESSAGES_DB" "DELETE FROM message WHERE ($PATTERN_CONDITIONS); SELECT changes();")
    
    success "Deleted $DELETED spam messages"
    
    # Vacuum database to reclaim space
    log "Optimizing database..."
    sqlite3 "$MESSAGES_DB" "VACUUM;"
    success "Database optimized"
}

# Show statistics
show_stats() {
    log "Spam Statistics"
    echo ""
    
    # Build pattern conditions
    PATTERN_CONDITIONS=""
    for pattern in "${SPAM_PATTERNS[@]}"; do
        if [ -n "$PATTERN_CONDITIONS" ]; then
            PATTERN_CONDITIONS="$PATTERN_CONDITIONS OR "
        fi
        PATTERN_CONDITIONS="$PATTERN_CONDITIONS text LIKE '%$pattern%'"
    done
    
    TOTAL_SPAM=$(sqlite3 "$MESSAGES_DB" "SELECT COUNT(*) FROM message WHERE ($PATTERN_CONDITIONS);")
    TOTAL_MESSAGES=$(sqlite3 "$MESSAGES_DB" "SELECT COUNT(*) FROM message;")
    
    echo "Total messages: $TOTAL_MESSAGES"
    echo "Spam messages: $TOTAL_SPAM"
    
    if [ "$TOTAL_MESSAGES" -gt 0 ]; then
        PERCENTAGE=$(echo "scale=2; $TOTAL_SPAM * 100 / $TOTAL_MESSAGES" | bc)
        echo "Spam percentage: $PERCENTAGE%"
    fi
    
    echo ""
    echo "Breakdown by pattern:"
    for pattern in "${SPAM_PATTERNS[@]}"; do
        COUNT=$(sqlite3 "$MESSAGES_DB" "SELECT COUNT(*) FROM message WHERE text LIKE '%$pattern%';")
        if [ "$COUNT" -gt 0 ]; then
            echo "  • '$pattern': $COUNT messages"
        fi
    done
}

# Configure patterns
configure_patterns() {
    log "Current spam patterns:"
    echo ""
    for i in "${!SPAM_PATTERNS[@]}"; do
        echo "  $((i+1)). ${SPAM_PATTERNS[$i]}"
    done
    echo ""
    echo "To add patterns, edit the SPAM_PATTERNS array in this script."
}

# Auto-filter (background mode)
auto_filter() {
    log "Setting up auto-filter..."
    echo ""
    echo "This will create a launch agent that runs the filter periodically."
    echo ""
    
    LAUNCH_AGENT="$HOME/Library/LaunchAgents/com.noizylab.imessage-spam-filter.plist"
    SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
    
    cat > "$LAUNCH_AGENT" << EOF
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
EOF
    
    success "Launch agent created: $LAUNCH_AGENT"
    echo ""
    echo "To load the agent, run:"
    echo "  launchctl load $LAUNCH_AGENT"
    echo ""
    echo "To unload:"
    echo "  launchctl unload $LAUNCH_AGENT"
}

# View recent spam
view_recent_spam() {
    log "Recent spam messages:"
    echo ""
    
    # Build pattern conditions
    PATTERN_CONDITIONS=""
    for pattern in "${SPAM_PATTERNS[@]}"; do
        if [ -n "$PATTERN_CONDITIONS" ]; then
            PATTERN_CONDITIONS="$PATTERN_CONDITIONS OR "
        fi
        PATTERN_CONDITIONS="$PATTERN_CONDITIONS text LIKE '%$pattern%'"
    done
    
    QUERY="SELECT 
        datetime(message.date/1000000000 + strftime('%s', '2001-01-01'), 'unixepoch', 'localtime') as date,
        handle.id as sender,
        substr(message.text, 1, 100) as preview
    FROM message
    LEFT JOIN handle ON message.handle_id = handle.ROWID
    WHERE ($PATTERN_CONDITIONS)
    ORDER BY message.date DESC
    LIMIT 20;"
    
    sqlite3 -header -column "$MESSAGES_DB" "$QUERY"
}

# Handle command line arguments
if [ "$1" = "--auto-delete" ]; then
    # Auto-delete mode (silent)
    PATTERN_CONDITIONS=""
    for pattern in "${SPAM_PATTERNS[@]}"; do
        if [ -n "$PATTERN_CONDITIONS" ]; then
            PATTERN_CONDITIONS="$PATTERN_CONDITIONS OR "
        fi
        PATTERN_CONDITIONS="$PATTERN_CONDITIONS text LIKE '%$pattern%'"
    done
    
    DELETED=$(sqlite3 "$MESSAGES_DB" "DELETE FROM message WHERE ($PATTERN_CONDITIONS); SELECT changes();")
    
    if [ "$DELETED" -gt 0 ]; then
        echo "$(date): Deleted $DELETED spam messages" >> "$HOME/Library/Messages/spam-filter.log"
    fi
    exit 0
fi

# Interactive mode
while true; do
    show_menu
    read -r choice
    
    case "$choice" in
        1)
            scan_spam
            echo ""
            read -p "Press Enter to continue..."
            ;;
        2)
            delete_spam
            echo ""
            read -p "Press Enter to continue..."
            ;;
        3)
            show_stats
            echo ""
            read -p "Press Enter to continue..."
            ;;
        4)
            configure_patterns
            echo ""
            read -p "Press Enter to continue..."
            ;;
        5)
            auto_filter
            echo ""
            read -p "Press Enter to continue..."
            ;;
        6)
            view_recent_spam
            echo ""
            read -p "Press Enter to continue..."
            ;;
        0|q|exit)
            echo "👋 Goodbye!"
            exit 0
            ;;
        *)
            error "Invalid choice"
            sleep 1
            ;;
    esac
done

