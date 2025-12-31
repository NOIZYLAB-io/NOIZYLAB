#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Quick Note
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 📝
# @raycast.argument1 { "type": "text", "placeholder": "Note content" }
# @raycast.packageName Productivity

# Documentation:
# @raycast.description Add a quick note with timestamp
# @raycast.author NOIZYLAB

notes_file="$HOME/.notes"
timestamp=$(date '+%Y-%m-%d %H:%M')

echo "[$timestamp] $1" >> "$notes_file"
echo "Note saved!"
