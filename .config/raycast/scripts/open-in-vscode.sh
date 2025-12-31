#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Open in VS Code
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 💻
# @raycast.argument1 { "type": "text", "placeholder": "Path or current dir", "optional": true }
# @raycast.packageName Developer

# Documentation:
# @raycast.description Open a folder in VS Code Insiders
# @raycast.author NOIZYLAB

path="${1:-.}"

if [[ "$path" == "." ]]; then
    # Get current Finder directory or use home
    path=$(osascript -e 'tell application "Finder" to get POSIX path of (insertion location as text)' 2>/dev/null || echo "$HOME")
fi

code-insiders "$path"
echo "Opened $path in VS Code Insiders"
