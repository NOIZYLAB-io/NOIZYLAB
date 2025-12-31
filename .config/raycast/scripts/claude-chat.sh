#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Claude Chat
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Message (optional)", "optional": true }
# @raycast.packageName AI

# Documentation:
# @raycast.description Open Claude Code in terminal with optional message
# @raycast.author NOIZYLAB

# Open iTerm2 with Claude
osascript << EOF
tell application "iTerm2"
    activate
    tell current window
        create tab with default profile
        tell current session
            write text "claude ${1:+\"$1\"}"
        end tell
    end tell
end tell
EOF

echo "Opened Claude Code"
