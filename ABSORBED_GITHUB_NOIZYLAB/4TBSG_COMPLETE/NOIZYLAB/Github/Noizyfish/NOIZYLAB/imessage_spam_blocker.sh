#!/bin/zsh

# iMessage Spam Blocker & Auto-Delete System
# Created: October 11, 2025
# Purpose: Automatically detect, block, and delete spam messages

echo "📱 iMessage Spam Blocker System Starting..."

# Configuration
SPAM_KEYWORDS=(
    "free money"
    "click here"
    "congratulations you won"
    "limited time offer"
    "urgent action required"
    "verify your account"
    "suspended account"
    "confirm identity"
    "bitcoin"
    "cryptocurrency"
    "investment opportunity"
    "act now"
    "call immediately"
    "tax refund"
    "amazon delivery"
    "package delivery"
    "shipment delayed"
)

SPAM_PATTERNS=(
    ".*[0-9]{10,}.*"  # Long number sequences
    ".*bit\.ly.*"     # Shortened URLs
    ".*tinyurl.*"
    ".*goo\.gl.*"
    ".*t\.co.*"
    ".*[A-Z]{5,}.*"   # All caps words
)

# Function to check if message contains spam indicators
is_spam_message() {
    local message="$1"
    local sender="$2"
    
    # Convert to lowercase for comparison
    local lower_message=$(echo "$message" | tr '[:upper:]' '[:lower:]')
    
    # Check for spam keywords
    for keyword in "${SPAM_KEYWORDS[@]}"; do
        if [[ "$lower_message" == *"$keyword"* ]]; then
            echo "SPAM DETECTED: Keyword '$keyword' found"
            return 0
        fi
    done
    
    # Check for spam patterns
    for pattern in "${SPAM_PATTERNS[@]}"; do
        if [[ "$message" =~ $pattern ]]; then
            echo "SPAM DETECTED: Pattern '$pattern' matched"
            return 0
        fi
    done
    
    # Check if sender is not in contacts
    if ! contacts -m "$sender" &>/dev/null; then
        echo "UNKNOWN SENDER: $sender not in contacts"
        return 0
    fi
    
    return 1
}

# Function to block and delete spam messages
block_and_delete() {
    local sender="$1"
    local message_id="$2"
    
    echo "🚫 Blocking sender: $sender"
    echo "🗑️ Deleting message ID: $message_id"
    
    # Block the sender (add to blocked list)
    osascript -e "
    tell application \"Messages\"
        try
            set targetBuddy to buddy \"$sender\"
            block targetBuddy
        on error
            display notification \"Failed to block $sender\" with title \"Spam Blocker\"
        end try
    end tell"
    
    # Delete the message
    osascript -e "
    tell application \"Messages\"
        try
            delete message id \"$message_id\"
        on error
            display notification \"Failed to delete message from $sender\" with title \"Spam Blocker\"
        end try
    end tell"
}

# Main monitoring function
monitor_messages() {
    echo "👁️ Starting message monitoring..."
    
    while true; do
        # Get recent messages using AppleScript
        osascript -e "
        tell application \"Messages\"
            set recentMessages to {}
            repeat with i from 1 to count of text chats
                try
                    set currentChat to text chat i
                    set lastMessage to last message of currentChat
                    set messageText to text of lastMessage
                    set senderHandle to handle of sender of lastMessage
                    set messageDate to time sent of lastMessage
                    
                    -- Check if message is from last 5 minutes
                    set currentTime to current date
                    set timeDiff to (currentTime - messageDate)
                    
                    if timeDiff < 300 then -- 5 minutes
                        set end of recentMessages to {messageText, senderHandle, id of lastMessage}
                    end if
                end try
            end repeat
            return recentMessages
        end tell" | while IFS=$'\t' read -r message sender msg_id; do
            
            if [[ -n "$message" && -n "$sender" ]]; then
                echo "📧 Checking message from: $sender"
                echo "📝 Content: $message"
                
                if is_spam_message "$message" "$sender"; then
                    echo "⚠️ SPAM DETECTED!"
                    block_and_delete "$sender" "$msg_id"
                    
                    # Log the spam
                    echo "$(date): BLOCKED $sender - $message" >> "./spam_log.txt"
                    
                    # Send notification
                    osascript -e "display notification \"Blocked spam from $sender\" with title \"iMessage Spam Blocker\" sound name \"Funk\""
                else
                    echo "✅ Message appears legitimate"
                fi
            fi
        done
        
        # Wait 30 seconds before checking again
        sleep 30
    done
}

# Start the monitoring system
monitor_messages