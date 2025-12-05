#!/bin/bash
# ⚠️  DELETE ABSORBED SOURCES
# Only run AFTER verifying successful merge!

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${RED}⚠️  WARNING: SOURCE DELETION SCRIPT${NC}"
echo "================================================"
echo ""
echo "This will DELETE the following directories:"
echo "  1. /Users/m2ultra/NOIZYLAB"
echo "  2. /Users/m2ultra/Github/noizylab"
echo ""
echo -e "${YELLOW}These contain ~426GB of data!${NC}"
echo ""
echo -e "${RED}Make sure you have:${NC}"
echo "  ✓ Verified the merge was successful"
echo "  ✓ Checked all code is in Github/Noizyfish/NOIZYLAB"
echo "  ✓ Committed and pushed to remote"
echo "  ✓ Made backups if needed"
echo ""
read -p "Type 'DELETE NOW' to proceed: " confirm

if [ "$confirm" != "DELETE NOW" ]; then
    echo "Cancelled. No files deleted."
    exit 1
fi

echo ""
echo -e "${RED}🔥 DELETING SOURCES...${NC}"

SOURCE1="/Users/m2ultra/NOIZYLAB"
SOURCE2="/Users/m2ultra/Github/noizylab"

if [ -d "$SOURCE1" ]; then
    echo "Removing $SOURCE1..."
    rm -rf "$SOURCE1"
    echo -e "${GREEN}✓ Deleted $SOURCE1${NC}"
fi

if [ -d "$SOURCE2" ]; then
    echo "Removing $SOURCE2..."
    rm -rf "$SOURCE2"
    echo -e "${GREEN}✓ Deleted $SOURCE2${NC}"
fi

echo ""
echo -e "${GREEN}🎉 CLEANUP COMPLETE!${NC}"
echo "Freed up ~426GB of disk space"
echo ""
echo "All code is now in:"
echo "  /Users/m2ultra/Github/Noizyfish/NOIZYLAB"
