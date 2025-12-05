#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
#                         GORUNFREE SPLITTER
#                    Code → GitHub | Media → 12TB/GDrive
# ═══════════════════════════════════════════════════════════════════════════════

set -e

# CONFIGURATION - EDIT THESE PATHS
SEARCH_ROOT="/Users/m2ultra"
CODE_DEST="$HOME/NOIZYLAB"                    # → GitHub
MEDIA_DEST="/Volumes/12TB/THE_AQUARIUM"       # → Your 12TB drive (change if different)
# MEDIA_DEST="$HOME/Google Drive/THE_AQUARIUM"  # Alternative: Google Drive

GITHUB_REPO="https://github.com/Noizyfish/NOIZYLAB.git"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

echo ""
echo -e "${MAGENTA}╔═══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${MAGENTA}║${NC}              ${GREEN}GORUNFREE SPLITTER${NC}                              ${MAGENTA}║${NC}"
echo -e "${MAGENTA}║${NC}         ${CYAN}Code → GitHub | Media → 12TB${NC}                        ${MAGENTA}║${NC}"
echo -e "${MAGENTA}╚═══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 1: SETUP DESTINATIONS
# ═══════════════════════════════════════════════════════════════════════════════

echo -e "${YELLOW}⚡ PHASE 1: Setting up destinations${NC}"

# Code destination (GitHub repo)
mkdir -p "$CODE_DEST"/{cloudflare/workers,agents,scripts/{mac,windows},configs,docs,projects}
cd "$CODE_DEST"
[ ! -d ".git" ] && git init && git remote add origin "$GITHUB_REPO" 2>/dev/null

# Media destination
if [ -d "/Volumes/12TB" ]; then
    MEDIA_DEST="/Volumes/12TB/THE_AQUARIUM"
    echo "  ✓ Found 12TB drive"
elif [ -d "/Volumes/WD"* ]; then
    MEDIA_DEST="$(ls -d /Volumes/WD* | head -1)/THE_AQUARIUM"
    echo "  ✓ Found WD drive"
elif [ -d "$HOME/Google Drive" ]; then
    MEDIA_DEST="$HOME/Google Drive/THE_AQUARIUM"
    echo "  ✓ Using Google Drive"
elif [ -d "$HOME/Library/CloudStorage/GoogleDrive"* ]; then
    MEDIA_DEST="$(ls -d "$HOME/Library/CloudStorage/GoogleDrive"* | head -1)/My Drive/THE_AQUARIUM"
    echo "  ✓ Using Google Drive (CloudStorage)"
else
    MEDIA_DEST="$HOME/THE_AQUARIUM_MEDIA"
    echo "  ⚠ No external drive found - using $MEDIA_DEST"
fi

mkdir -p "$MEDIA_DEST"/{audio,video,daw_projects,samples}
echo "  ✓ Code → $CODE_DEST"
echo "  ✓ Media → $MEDIA_DEST"

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 2: SCAN AND SORT
# ═══════════════════════════════════════════════════════════════════════════════

echo ""
echo -e "${YELLOW}⚡ PHASE 2: Scanning $SEARCH_ROOT${NC}"

CODE_COUNT=0
AUDIO_COUNT=0
VIDEO_COUNT=0
DAW_COUNT=0

# Find and sort ALL files
find "$SEARCH_ROOT" -type f \
    -not -path "*/Library/*" \
    -not -path "*/node_modules/*" \
    -not -path "*/.git/*" \
    -not -path "*/.Trash/*" \
    -not -path "*/NOIZYLAB/*" \
    -not -path "*/THE_AQUARIUM/*" \
    2>/dev/null | while read -r file; do
    
    filename=$(basename "$file")
    ext="${filename##*.}"
    ext_lower=$(echo "$ext" | tr '[:upper:]' '[:lower:]')
    
    case "$ext_lower" in
        # CODE → GitHub
        py|js|ts|jsx|tsx|mjs|sh|bash|zsh|ps1|bat|cmd|html|css|scss|json|yaml|yml|toml|md|swift|applescript|sql)
            cp "$file" "$CODE_DEST/projects/" 2>/dev/null && echo "  📄 $filename → GitHub"
            ;;
        
        # AUDIO → 12TB/GDrive
        wav|mp3|aif|aiff|flac|m4a|ogg|aac)
            cp "$file" "$MEDIA_DEST/audio/" 2>/dev/null && echo "  🎵 $filename → 12TB"
            ;;
        
        # VIDEO → 12TB/GDrive  
        mov|mp4|avi|mkv|m4v|webm|wmv)
            cp "$file" "$MEDIA_DEST/video/" 2>/dev/null && echo "  🎬 $filename → 12TB"
            ;;
        
        # DAW PROJECTS → 12TB/GDrive
        logicx|ptx|ptf|als|band|sesx|rpp|flp)
            cp -r "$file" "$MEDIA_DEST/daw_projects/" 2>/dev/null && echo "  🎚️ $filename → 12TB"
            ;;
    esac
done

# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 3: PUSH CODE TO GITHUB
# ═══════════════════════════════════════════════════════════════════════════════

echo ""
echo -e "${YELLOW}⚡ PHASE 3: Pushing CODE to GitHub${NC}"

cd "$CODE_DEST"

# Create .gitignore (exclude all media)
cat > .gitignore << 'EOF'
# AUDIO - Goes to 12TB/GDrive NOT GitHub
*.wav
*.mp3
*.aif
*.aiff
*.flac
*.m4a
*.ogg
*.aac

# VIDEO - Goes to 12TB/GDrive NOT GitHub
*.mov
*.mp4
*.avi
*.mkv
*.m4v
*.webm

# DAW PROJECTS - Goes to 12TB/GDrive NOT GitHub
*.logicx
*.ptx
*.ptf
*.als
*.band
*.sesx
*.rpp
*.flp

# System
.DS_Store
Thumbs.db
*.log

# Dependencies
node_modules/
__pycache__/
*.pyc
venv/
.env
EOF

git add -A
git commit -m "⚡ GORUNFREE SPLITTER: Code from GOD @ $(date '+%Y-%m-%d %H:%M')

Code → GitHub
Audio/Video/DAW → 12TB/Google Drive

Fish Music Inc • MC96ECOUNIVERSE" 2>/dev/null || echo "  (no new code changes)"

git branch -M main
git push -u origin main --force 2>/dev/null && echo "  ✓ Pushed to GitHub" || echo "  ⚠ Push failed - check credentials"

# ═══════════════════════════════════════════════════════════════════════════════
# COMPLETE
# ═══════════════════════════════════════════════════════════════════════════════

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}              ⚡ GORUNFREE SPLITTER COMPLETE ⚡${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "  CODE (GitHub):     $CODE_DEST"
echo "                     https://github.com/Noizyfish/NOIZYLAB"
echo ""
echo "  MEDIA (12TB):      $MEDIA_DEST"
echo "    └── audio/       Audio files"
echo "    └── video/       Video files"
echo "    └── daw_projects/ Logic, Pro Tools, etc."
echo ""
echo -e "${GREEN}⚡ EVERYTHING IN THE RIGHT PLACE ⚡${NC}"
echo ""

# Show counts
echo "Summary:"
echo "  Code files:  $(find "$CODE_DEST" -type f -name "*.py" -o -name "*.js" -o -name "*.sh" -o -name "*.md" 2>/dev/null | wc -l | tr -d ' ')"
echo "  Audio files: $(find "$MEDIA_DEST/audio" -type f 2>/dev/null | wc -l | tr -d ' ')"
echo "  Video files: $(find "$MEDIA_DEST/video" -type f 2>/dev/null | wc -l | tr -d ' ')"
echo "  DAW projects: $(find "$MEDIA_DEST/daw_projects" -type f 2>/dev/null | wc -l | tr -d ' ')"
