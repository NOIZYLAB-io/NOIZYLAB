#!/bin/bash
# GOD Smart Cleanup - Safe space recovery
# CB_01 - Fish Music Inc
# Identifies and optionally removes safe-to-delete files
# GORUNFREE! 🎸🔥

set -e

# Colors
G='\033[0;32m'
Y='\033[1;33m'
C='\033[0;36m'
M='\033[0;35m'
R='\033[0;31m'
B='\033[1m'
NC='\033[0m'

echo ""
echo -e "${B}${M}🧹 GOD SMART CLEANUP${NC}"
echo -e "${C}Safe space recovery analysis${NC}"
echo ""

# Calculate sizes
echo -e "${B}${C}📊 ANALYZING CLEANUP TARGETS...${NC}"
echo ""

# User caches
USER_CACHE=$(du -sh ~/Library/Caches 2>/dev/null | cut -f1 || echo "0")
echo -e "${Y}User Cache:${NC} $USER_CACHE"

# Chrome cache
CHROME_CACHE="0"
if [ -d ~/Library/Application\ Support/Google/Chrome ]; then
    CHROME_CACHE=$(du -sh ~/Library/Application\ Support/Google/Chrome/Default/Cache 2>/dev/null | cut -f1 || echo "0")
fi
echo -e "${Y}Chrome Cache:${NC} $CHROME_CACHE"

# Xcode derived data (if exists)
XCODE_DATA="0"
if [ -d ~/Library/Developer/Xcode/DerivedData ]; then
    XCODE_DATA=$(du -sh ~/Library/Developer/Xcode/DerivedData 2>/dev/null | cut -f1 || echo "0")
fi
echo -e "${Y}Xcode Derived:${NC} $XCODE_DATA"

# npm cache
NPM_CACHE="0"
if [ -d ~/.npm ]; then
    NPM_CACHE=$(du -sh ~/.npm 2>/dev/null | cut -f1 || echo "0")
fi
echo -e "${Y}npm Cache:${NC} $NPM_CACHE"

# pip cache
PIP_CACHE="0"
if [ -d ~/Library/Caches/pip ]; then
    PIP_CACHE=$(du -sh ~/Library/Caches/pip 2>/dev/null | cut -f1 || echo "0")
fi
echo -e "${Y}pip Cache:${NC} $PIP_CACHE"

# Homebrew cache
BREW_CACHE="0"
if [ -d ~/Library/Caches/Homebrew ]; then
    BREW_CACHE=$(du -sh ~/Library/Caches/Homebrew 2>/dev/null | cut -f1 || echo "0")
fi
echo -e "${Y}Homebrew Cache:${NC} $BREW_CACHE"

# Trash
TRASH_SIZE=$(du -sh ~/.Trash 2>/dev/null | cut -f1 || echo "0")
echo -e "${Y}Trash:${NC} $TRASH_SIZE"

# Downloads (just report, don't delete)
DOWNLOADS_SIZE=$(du -sh ~/Downloads 2>/dev/null | cut -f1 || echo "0")
echo -e "${Y}Downloads:${NC} $DOWNLOADS_SIZE ${C}(not auto-deleted)${NC}"

echo ""
echo -e "${B}${C}═══════════════════════════════════════${NC}"
echo ""

# Menu
echo -e "${B}${G}CLEANUP OPTIONS:${NC}"
echo ""
echo -e "  ${C}1)${NC} Clear user caches (safe)"
echo -e "  ${C}2)${NC} Clear Chrome cache"
echo -e "  ${C}3)${NC} Clear npm cache"
echo -e "  ${C}4)${NC} Clear pip cache"
echo -e "  ${C}5)${NC} Clear Homebrew cache"
echo -e "  ${C}6)${NC} Empty Trash"
echo -e "  ${C}7)${NC} Clear Xcode derived data"
echo -e "  ${C}a)${NC} ALL of the above (recommended)"
echo -e "  ${C}q)${NC} Quit (no changes)"
echo ""

read -p "Select option: " CHOICE

case $CHOICE in
    1)
        echo -e "${C}Clearing user caches...${NC}"
        rm -rf ~/Library/Caches/* 2>/dev/null || true
        echo -e "${G}✅ User caches cleared${NC}"
        ;;
    2)
        echo -e "${C}Clearing Chrome cache...${NC}"
        rm -rf ~/Library/Application\ Support/Google/Chrome/Default/Cache/* 2>/dev/null || true
        echo -e "${G}✅ Chrome cache cleared${NC}"
        ;;
    3)
        echo -e "${C}Clearing npm cache...${NC}"
        npm cache clean --force 2>/dev/null || rm -rf ~/.npm/_cacache 2>/dev/null || true
        echo -e "${G}✅ npm cache cleared${NC}"
        ;;
    4)
        echo -e "${C}Clearing pip cache...${NC}"
        pip3 cache purge 2>/dev/null || rm -rf ~/Library/Caches/pip 2>/dev/null || true
        echo -e "${G}✅ pip cache cleared${NC}"
        ;;
    5)
        echo -e "${C}Clearing Homebrew cache...${NC}"
        brew cleanup --prune=all 2>/dev/null || rm -rf ~/Library/Caches/Homebrew 2>/dev/null || true
        echo -e "${G}✅ Homebrew cache cleared${NC}"
        ;;
    6)
        echo -e "${C}Emptying Trash...${NC}"
        rm -rf ~/.Trash/* 2>/dev/null || true
        echo -e "${G}✅ Trash emptied${NC}"
        ;;
    7)
        echo -e "${C}Clearing Xcode derived data...${NC}"
        rm -rf ~/Library/Developer/Xcode/DerivedData/* 2>/dev/null || true
        echo -e "${G}✅ Xcode derived data cleared${NC}"
        ;;
    a|A)
        echo -e "${C}Running full cleanup...${NC}"
        echo ""

        echo -e "${C}[1/7] User caches...${NC}"
        rm -rf ~/Library/Caches/* 2>/dev/null || true

        echo -e "${C}[2/7] Chrome cache...${NC}"
        rm -rf ~/Library/Application\ Support/Google/Chrome/Default/Cache/* 2>/dev/null || true

        echo -e "${C}[3/7] npm cache...${NC}"
        npm cache clean --force 2>/dev/null || rm -rf ~/.npm/_cacache 2>/dev/null || true

        echo -e "${C}[4/7] pip cache...${NC}"
        pip3 cache purge 2>/dev/null || rm -rf ~/Library/Caches/pip 2>/dev/null || true

        echo -e "${C}[5/7] Homebrew cache...${NC}"
        brew cleanup --prune=all 2>/dev/null || rm -rf ~/Library/Caches/Homebrew 2>/dev/null || true

        echo -e "${C}[6/7] Trash...${NC}"
        rm -rf ~/.Trash/* 2>/dev/null || true

        echo -e "${C}[7/7] Xcode derived data...${NC}"
        rm -rf ~/Library/Developer/Xcode/DerivedData/* 2>/dev/null || true

        echo ""
        echo -e "${G}${B}✅ FULL CLEANUP COMPLETE${NC}"
        ;;
    q|Q)
        echo -e "${Y}No changes made${NC}"
        exit 0
        ;;
    *)
        echo -e "${R}Invalid option${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${B}${C}📊 SPACE RECOVERED:${NC}"
df -h / | tail -1 | awk '{print "Available: " $4}'
echo ""
echo -e "${B}${M}GORUNFREE! 🎸🔥${NC}"
echo ""
