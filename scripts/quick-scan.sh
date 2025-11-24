#!/bin/bash
#===============================================================================
# NOIZYLAB QUICK SCAN - Preview what will be extracted
#===============================================================================

SOURCE_DIR="/Volumes/4TBSG"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}"
echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║              NOIZYLAB QUICK SCAN - Preview Mode                   ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

if [ ! -d "$SOURCE_DIR" ]; then
    echo -e "${RED}ERROR: $SOURCE_DIR not found!${NC}"
    echo "Make sure your 4TB drive is mounted."
    exit 1
fi

echo -e "${BLUE}Scanning $SOURCE_DIR...${NC}\n"

# Quick count by file type
echo -e "${YELLOW}=== CODE FILES BY TYPE ===${NC}"
find "$SOURCE_DIR" \
    -path '*/node_modules' -prune -o \
    -path '*/.git' -prune -o \
    -path '*/__pycache__' -prune -o \
    -path '*/venv' -prune -o \
    -path '*/.Trash' -prune -o \
    -type f \( \
        -name "*.js" -o -name "*.ts" -o -name "*.jsx" -o -name "*.tsx" -o \
        -name "*.py" -o -name "*.rb" -o -name "*.php" -o -name "*.go" -o \
        -name "*.rs" -o -name "*.java" -o -name "*.swift" -o \
        -name "*.c" -o -name "*.cpp" -o -name "*.h" -o \
        -name "*.html" -o -name "*.css" -o -name "*.scss" -o \
        -name "*.json" -o -name "*.yml" -o -name "*.yaml" -o \
        -name "*.md" -o -name "*.sql" -o -name "*.sh" \
    \) -print 2>/dev/null | sed 's/.*\.//' | sort | uniq -c | sort -rn

echo ""
echo -e "${YELLOW}=== TOP-LEVEL DIRECTORIES ===${NC}"
ls -la "$SOURCE_DIR" 2>/dev/null | head -20

echo ""
echo -e "${YELLOW}=== POTENTIAL PROJECTS (containing package.json) ===${NC}"
find "$SOURCE_DIR" -name "package.json" -not -path "*/node_modules/*" 2>/dev/null | head -20

echo ""
echo -e "${YELLOW}=== POTENTIAL PYTHON PROJECTS ===${NC}"
find "$SOURCE_DIR" \( -name "requirements.txt" -o -name "setup.py" -o -name "pyproject.toml" \) 2>/dev/null | head -20

echo ""
echo -e "${YELLOW}=== DISK USAGE ===${NC}"
du -sh "$SOURCE_DIR" 2>/dev/null

echo ""
echo -e "${GREEN}Quick scan complete!${NC}"
echo -e "Run ${CYAN}./extract-and-move-code.sh${NC} to perform full extraction."
