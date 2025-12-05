#!/bin/bash
# GOD Find Large Files - Identify space hogs
# CB_01 - Fish Music Inc
# Finds largest files and directories
# GORUNFREE! 🎸🔥

# Colors
G='\033[0;32m'
Y='\033[1;33m'
C='\033[0;36m'
M='\033[0;35m'
B='\033[1m'
NC='\033[0m'

TARGET="${1:-$HOME}"
LIMIT="${2:-20}"

echo ""
echo -e "${B}${M}🔍 GOD LARGE FILE FINDER${NC}"
echo -e "${C}Target: $TARGET${NC}"
echo -e "${C}Showing top $LIMIT items${NC}"
echo ""

echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${B}${Y}📁 LARGEST DIRECTORIES:${NC}"
echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo ""

du -sh "$TARGET"/*/ 2>/dev/null | sort -rh | head -$LIMIT | while read size dir; do
    echo -e "${G}$size${NC}\t$dir"
done

echo ""
echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${B}${Y}📄 LARGEST FILES (>100MB):${NC}"
echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo ""

find "$TARGET" -type f -size +100M 2>/dev/null | head -$LIMIT | while read file; do
    size=$(du -sh "$file" 2>/dev/null | cut -f1)
    echo -e "${G}$size${NC}\t$file"
done | sort -rh | head -$LIMIT

echo ""
echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${B}${Y}📦 POTENTIAL CLEANUP TARGETS:${NC}"
echo -e "${B}${C}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Common large directories
targets=(
    "$HOME/Library/Caches"
    "$HOME/Library/Developer/Xcode/DerivedData"
    "$HOME/Library/Application Support/Docker"
    "$HOME/.npm"
    "$HOME/.Trash"
    "$HOME/Downloads"
)

for t in "${targets[@]}"; do
    if [ -d "$t" ]; then
        size=$(du -sh "$t" 2>/dev/null | cut -f1)
        echo -e "${Y}$size${NC}\t$t"
    fi
done

echo ""
echo -e "${B}${M}GORUNFREE! 🎸🔥${NC}"
echo ""
echo -e "${C}Usage: ./god-find-large.sh [path] [count]${NC}"
echo -e "${C}Example: ./god-find-large.sh /Volumes/MyDrive 50${NC}"
echo ""
