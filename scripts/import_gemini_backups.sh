#!/bin/bash

# NOIZYLAB - OneDrive Gemini Backups Import Script
# Downloads Fish Music Inc & NOIZY art from OneDrive to local workspace

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
PURPLE='\033[0;35m'
BOLD='\033[1m'
NC='\033[0m'

clear

echo ""
echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${PURPLE}🎨 NOIZYLAB - Import Gemini Backups from OneDrive${NC}"
echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# OneDrive link
ONEDRIVE_LINK="https://1drv.ms/f/c/8ee9a16e20ab6669/IgC1mhahpgU-Qo1UD9idWYbyAdwMMLBErzctRcHr2jXLPVA?e=bpk6UK"

# Target directories
NOIZYLAB_ROOT="$HOME/NOIZYLAB"
BUSINESS_DIR="$NOIZYLAB_ROOT/gabriel/_ORGANIZED/business"
ART_DIR="$NOIZYLAB_ROOT/gabriel/_ORGANIZED/media/art"
GEMINI_BACKUPS="$NOIZYLAB_ROOT/gabriel/_ORGANIZED/backups/gemini"

echo -e "${CYAN}📋 What's in the OneDrive folder:${NC}"
echo "   • Gemini conversation backups"
echo "   • Fish Music Inc artwork & assets"
echo "   • NOIZY branding & art files"
echo ""

echo -e "${CYAN}📂 Target directories:${NC}"
echo "   • Gemini backups: $GEMINI_BACKUPS"
echo "   • Fish Music art: $BUSINESS_DIR/fish-music-inc/assets"
echo "   • NOIZY art: $ART_DIR/noizy"
echo ""

# Create directories
echo -e "${YELLOW}📁 Creating directories...${NC}"
mkdir -p "$GEMINI_BACKUPS"
mkdir -p "$BUSINESS_DIR/fish-music-inc/assets"
mkdir -p "$ART_DIR/noizy"
echo -e "${GREEN}✅ Directories ready${NC}"
echo ""

echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BOLD}IMPORT OPTIONS${NC}"
echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${CYAN}Option 1: Manual Download (Recommended)${NC}"
echo ""
echo "1. Open OneDrive link in browser:"
echo -e "   ${YELLOW}$ONEDRIVE_LINK${NC}"
echo ""
echo "2. Click 'Download' to get ZIP file"
echo ""
echo "3. Extract ZIP to Downloads folder"
echo ""
echo "4. Run this script again with the path:"
echo -e "   ${YELLOW}bash $0 ~/Downloads/GeminiBackups${NC}"
echo ""

echo -e "${CYAN}Option 2: OneDrive Desktop App${NC}"
echo ""
echo "If you have OneDrive desktop app:"
echo ""
echo "1. Install OneDrive: https://www.microsoft.com/en-us/microsoft-365/onedrive/download"
echo ""
echo "2. Sign in and sync the folder"
echo ""
echo "3. OneDrive will appear in Finder sidebar"
echo ""
echo "4. Copy files from OneDrive folder to NOIZYLAB:"
echo -e "   ${YELLOW}cp -r ~/OneDrive/GeminiBackups/* $GEMINI_BACKUPS/${NC}"
echo ""

echo -e "${CYAN}Option 3: rclone (Advanced)${NC}"
echo ""
echo "Install rclone for automated sync:"
echo ""
echo "1. Install rclone:"
echo -e "   ${YELLOW}brew install rclone${NC}"
echo ""
echo "2. Configure OneDrive:"
echo -e "   ${YELLOW}rclone config${NC}"
echo ""
echo "3. Sync folder:"
echo -e "   ${YELLOW}rclone sync onedrive:GeminiBackups $GEMINI_BACKUPS${NC}"
echo ""

echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if user provided a source path
if [ -n "$1" ]; then
    SOURCE_PATH="$1"
    
    if [ ! -d "$SOURCE_PATH" ]; then
        echo -e "${RED}❌ Source path not found: $SOURCE_PATH${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✅ Found source directory: $SOURCE_PATH${NC}"
    echo ""
    
    # Detect file types and organize
    echo -e "${YELLOW}🔍 Scanning files...${NC}"
    
    # Count files
    TOTAL_FILES=$(find "$SOURCE_PATH" -type f | wc -l | tr -d ' ')
    GEMINI_FILES=$(find "$SOURCE_PATH" -type f \( -name "*.json" -o -name "*.txt" -o -name "*gemini*" \) | wc -l | tr -d ' ')
    IMAGE_FILES=$(find "$SOURCE_PATH" -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.svg" -o -name "*.ai" -o -name "*.psd" \) | wc -l | tr -d ' ')
    
    echo "   • Total files: $TOTAL_FILES"
    echo "   • Gemini backups: $GEMINI_FILES"
    echo "   • Image files: $IMAGE_FILES"
    echo ""
    
    # Copy files
    echo -e "${YELLOW}📦 Copying files...${NC}"
    
    # Copy Gemini backups
    if [ "$GEMINI_FILES" -gt 0 ]; then
        echo "   • Copying Gemini backups..."
        find "$SOURCE_PATH" -type f \( -name "*.json" -o -name "*.txt" -o -name "*gemini*" \) -exec cp {} "$GEMINI_BACKUPS/" \;
        echo -e "   ${GREEN}✅ Copied $GEMINI_FILES Gemini files${NC}"
    fi
    
    # Copy Fish Music art
    if [ "$IMAGE_FILES" -gt 0 ]; then
        echo "   • Copying Fish Music Inc assets..."
        find "$SOURCE_PATH" -type f \( -iname "*fish*" -o -iname "*fmi*" \) \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.svg" \) -exec cp {} "$BUSINESS_DIR/fish-music-inc/assets/" \; 2>/dev/null
        
        echo "   • Copying NOIZY art..."
        find "$SOURCE_PATH" -type f \( -iname "*noizy*" -o -iname "*noizylab*" \) \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.svg" \) -exec cp {} "$ART_DIR/noizy/" \; 2>/dev/null
        
        echo -e "   ${GREEN}✅ Copied artwork files${NC}"
    fi
    
    echo ""
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}✅ IMPORT COMPLETE!${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    echo -e "${CYAN}📂 Files imported to:${NC}"
    echo "   • Gemini: $GEMINI_BACKUPS"
    echo "   • Fish Music: $BUSINESS_DIR/fish-music-inc/assets"
    echo "   • NOIZY Art: $ART_DIR/noizy"
    echo ""
    
    # Show file counts
    echo -e "${CYAN}📊 Summary:${NC}"
    echo "   • Gemini backups: $(ls "$GEMINI_BACKUPS" 2>/dev/null | wc -l | tr -d ' ') files"
    echo "   • Fish Music assets: $(ls "$BUSINESS_DIR/fish-music-inc/assets" 2>/dev/null | wc -l | tr -d ' ') files"
    echo "   • NOIZY art: $(ls "$ART_DIR/noizy" 2>/dev/null | wc -l | tr -d ' ') files"
    echo ""
    
    # Create index
    echo -e "${YELLOW}📋 Creating index...${NC}"
    cat > "$GEMINI_BACKUPS/README.md" << 'EOF'
# Gemini Backups - NOIZYLAB

This folder contains AI conversation backups from Google Gemini, including:

- Fish Music Inc branding discussions
- NOIZY artwork concepts
- Business strategy conversations
- Technical planning sessions

## Organization

```
gemini/
├── conversations/     # Chat exports
├── prompts/          # Saved prompts
└── outputs/          # Generated content
```

## Usage

These backups serve as:
- Knowledge base for AI training
- Reference for brand guidelines
- History of creative decisions
- Continuity for ongoing projects

Last updated: $(date '+%Y-%m-%d')
EOF
    
    echo -e "${GREEN}✅ Index created${NC}"
    echo ""
    
else
    echo -e "${YELLOW}💡 To import files, run:${NC}"
    echo -e "   ${CYAN}bash $0 /path/to/downloaded/folder${NC}"
    echo ""
    echo -e "${YELLOW}Example:${NC}"
    echo -e "   ${CYAN}bash $0 ~/Downloads/GeminiBackups${NC}"
    echo ""
fi

echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${CYAN}🔗 OneDrive Link:${NC}"
echo -e "   ${YELLOW}$ONEDRIVE_LINK${NC}"
echo ""
echo -e "${CYAN}📚 Next Steps:${NC}"
echo "   1. Download files from OneDrive"
echo "   2. Run: bash $0 ~/Downloads/folder-name"
echo "   3. Files will be organized automatically"
echo ""
