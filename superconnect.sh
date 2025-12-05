#!/bin/bash
# 🚀 NOIZYLAB SUPERCONNECT
# Move media to 12TB, push code to GitHub, create aliases

set -e

echo "🚀 NOIZYLAB SUPERCONNECT ACTIVATED"
echo "=================================="

# === 1. MOVE AUDIO/VIDEO TO 12TB ===
echo ""
echo "📦 STEP 1: Moving audio/video to 12TB..."

MEDIA_DEST="/Volumes/12TB/NOIZYLAB_MEDIA"
mkdir -p "$MEDIA_DEST/Audio" "$MEDIA_DEST/Video" "$MEDIA_DEST/Projects"

# Find and move audio files
find /Users/m2ultra -maxdepth 6 -type f \( \
    -name "*.wav" -o -name "*.mp3" -o -name "*.aif" -o -name "*.aiff" \
    -o -name "*.m4a" -o -name "*.flac" -o -name "*.ogg" \
\) 2>/dev/null | while read file; do
    if [[ ! "$file" =~ "/Volumes/" ]]; then
        mv "$file" "$MEDIA_DEST/Audio/" 2>/dev/null && echo "  ✅ Moved: $(basename "$file")" || true
    fi
done

# Find and move video files  
find /Users/m2ultra -maxdepth 6 -type f \( \
    -name "*.mp4" -o -name "*.mov" -o -name "*.avi" -o -name "*.mkv" \
\) 2>/dev/null | while read file; do
    if [[ ! "$file" =~ "/Volumes/" ]]; then
        mv "$file" "$MEDIA_DEST/Video/" 2>/dev/null && echo "  ✅ Moved: $(basename "$file")" || true
    fi
done

echo "✅ Media migration complete"

# === 2. PUSH CODE TO GITHUB ===
echo ""
echo "📤 STEP 2: Pushing all code to GitHub..."

cd /Users/m2ultra/.claude-worktrees/NOIZYLAB/tender-banach
git add -A
git commit -m "🚀 SUPERCONNECT: Full system sync - $(date '+%Y-%m-%d %H:%M')" || true
git push -u origin tender-banach

echo "✅ Code pushed to github.com/Noizyfish/NOIZYLAB"

# === 3. CREATE ALIASES ===
echo ""
echo "🔗 STEP 3: Creating superconnect aliases..."

ALIASES_FILE="$HOME/.noizylab_aliases"

cat > "$ALIASES_FILE" << 'ALIASES'
# 🚀 NOIZYLAB SUPERCONNECT ALIASES

# Quick navigation
alias nl='cd /Users/m2ultra/.claude-worktrees/NOIZYLAB/tender-banach'
alias nlm='cd /Volumes/12TB/NOIZYLAB_MEDIA'
alias nl6='cd /Volumes/6TB'
alias nl12='cd /Volumes/12TB'

# Agent commands
alias nla='python3 /Users/m2ultra/.claude-worktrees/NOIZYLAB/tender-banach/agent/noizylab_agent.py'
alias nls='python3 /Users/m2ultra/.claude-worktrees/NOIZYLAB/tender-banach/agent/flows/system_monitor.py'
alias nlt='python3 /Users/m2ultra/.claude-worktrees/NOIZYLAB/tender-banach/scripts/turbo.py'
alias nlo='python3 /Users/m2ultra/.claude-worktrees/NOIZYLAB/tender-banach/scripts/optimizer.py'

# CLI shortcuts
alias noizy='/Users/m2ultra/.claude-worktrees/NOIZYLAB/tender-banach/noizylab'
alias noizy-status='noizy status'
alias noizy-media='noizy media --stats'
alias noizy-git='noizy git --sync-all'

# Git turbo
alias gs='git status -sb'
alias gp='git push'
alias ga='git add -A'
alias gc='git commit -m'
alias gac='git add -A && git commit -m'
alias gpush='git add -A && git commit -m "sync" && git push'

# Quick system
alias cpu='top -l 1 | head -10'
alias mem='vm_stat | head -5'
alias disk='df -h | grep -E "12TB|6TB|Macintosh"'

# Media shortcuts
alias media-audio='ls -lh /Volumes/12TB/NOIZYLAB_MEDIA/Audio/'
alias media-video='ls -lh /Volumes/12TB/NOIZYLAB_MEDIA/Video/'
alias media-stats='du -sh /Volumes/12TB/NOIZYLAB_MEDIA/*'

# GORUNFREE
alias gorunfree='nlt && nlo'
alias turbo='nlt'
alias fire='gorunfree'

echo "🔥 NOIZYLAB aliases loaded! GORUNFREE!"
ALIASES

# Add to .zshrc if not already there
if ! grep -q "noizylab_aliases" "$HOME/.zshrc" 2>/dev/null; then
    echo "" >> "$HOME/.zshrc"
    echo "# NOIZYLAB SUPERCONNECT" >> "$HOME/.zshrc"
    echo "source ~/.noizylab_aliases" >> "$HOME/.zshrc"
fi

# Load now
source "$ALIASES_FILE"

echo "✅ Aliases created and loaded"

# === SUMMARY ===
echo ""
echo "🎯 SUPERCONNECT COMPLETE!"
echo "========================="
echo "  📦 Media → /Volumes/12TB/NOIZYLAB_MEDIA"
echo "  📤 Code  → github.com/Noizyfish/NOIZYLAB"
echo "  🔗 Aliases → ~/.noizylab_aliases"
echo ""
echo "Quick commands:"
echo "  nl      - Go to NOIZYLAB"
echo "  nlm     - Go to media"
echo "  noizy   - CLI tool"
echo "  turbo   - 50x analyzer"
echo "  fire    - Run everything"
echo ""
echo "🔥 GORUNFREE!"
