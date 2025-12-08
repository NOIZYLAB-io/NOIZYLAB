#!/bin/bash
# MAC AUTOMATOR WORKFLOW FOR CLAUDE-CURSOR INTEGRATION
# Save as: ~/Library/Services/Send-to-Claude.workflow

# SETUP INSTRUCTIONS:
# 1. Open Automator (Applications > Automator)
# 2. New Document > Quick Action
# 3. Set "Workflow receives: text" in "any application"
# 4. Add these actions:

# ============================================
# AUTOMATOR WORKFLOW: "Send to Claude"
# ============================================

# Action 1: Run AppleScript
# --------------------------
on run {input, parameters}
    set selectedText to input as text
    
    -- Copy to clipboard
    set the clipboard to selectedText
    
    -- Activate browser with Claude
    tell application "Safari"
        activate
        
        -- Find Claude.ai tab or open new
        set foundTab to false
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "claude.ai" then
                    set current tab of w to t
                    set foundTab to true
                    exit repeat
                end if
            end repeat
            if foundTab then exit repeat
        end repeat
        
        -- If no Claude tab, open one
        if not foundTab then
            tell window 1 to set current tab to (make new tab with properties {URL:"https://claude.ai"})
            delay 2
        end if
    end tell
    
    -- Paste into message box
    tell application "System Events"
        keystroke "v" using command down
        delay 0.5
        keystroke return
    end tell
    
    return input
end run

# ============================================
# SAVE THIS WORKFLOW AS:
# ~/Library/Services/Send-to-Claude.workflow
# ============================================

# After saving:
# 1. System Settings > Keyboard > Shortcuts > Services
# 2. Enable "Send to Claude"
# 3. Assign hotkey (e.g., ⌘⌥C)

# USAGE IN CURSOR:
# 1. Select code
# 2. Right-click > Services > Send to Claude
# OR press your hotkey

# ============================================
# AUTOMATOR WORKFLOW: "Get Claude Response"
# ============================================

# Action 1: Run Shell Script
# ---------------------------
osascript <<EOF
tell application "Safari"
    activate
    delay 0.5
end tell

tell application "System Events"
    -- Select all in last Claude response
    keystroke "a" using command down
    delay 0.2
    keystroke "c" using command down
    delay 0.2
    
    -- Switch back to Cursor
    keystroke tab using command down
    delay 0.5
    
    -- Paste
    keystroke "v" using command down
end tell
EOF

# ============================================
# VOICE TRIGGER VERSION (with Shortcuts.app)
# ============================================

# 1. Open Shortcuts app
# 2. New Shortcut: "Ask Claude"
# 3. Add actions:
#    - Get clipboard
#    - Open URL: https://claude.ai
#    - Set clipboard to "[clipboard]"
#    - Wait 1 second
#    - Type text (enable "Paste from clipboard")
#    - Press Return key
# 4. Add to Siri: "Hey Siri, ask Claude"

# ADVANCED: Auto-sync clipboard between apps
# Create folder action that watches for clipboard changes
# and syncs between Cursor and Claude

cat > ~/claude-cursor-sync.sh << 'SYNCEOF'
#!/bin/bash
# Auto-sync clipboard between Cursor and Claude

LAST_CLIP=""

while true; do
    CURRENT_CLIP=$(pbpaste)
    
    if [ "$CURRENT_CLIP" != "$LAST_CLIP" ]; then
        # Clipboard changed
        
        # If contains "CLAUDE:" prefix, paste to Cursor
        if [[ $CURRENT_CLIP == CLAUDE:* ]]; then
            osascript -e 'tell application "Cursor" to activate'
            sleep 0.5
            # Paste
            osascript -e 'tell application "System Events" to keystroke "v" using command down'
        fi
        
        # If contains "CURSOR:" prefix, send to Claude
        if [[ $CURRENT_CLIP == CURSOR:* ]]; then
            open "https://claude.ai"
            sleep 1
            osascript -e 'tell application "System Events" to keystroke "v" using command down'
            osascript -e 'tell application "System Events" to keystroke return'
        fi
        
        LAST_CLIP="$CURRENT_CLIP"
    fi
    
    sleep 1
done
SYNCEOF

chmod +x ~/claude-cursor-sync.sh

# Run in background:
# nohup ~/claude-cursor-sync.sh &

echo "✅ Automator workflows created"
echo ""
echo "Setup:"
echo "1. Open Automator"
echo "2. Create Quick Actions with scripts above"
echo "3. Assign keyboard shortcuts"
echo "4. Test in Cursor"
