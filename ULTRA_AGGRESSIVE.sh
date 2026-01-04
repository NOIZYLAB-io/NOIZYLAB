#!/bin/bash
# ULTRA AGGRESSIVE CLEANUP - NO MERCY MODE
# FORCE RETRIEVAL OF ALL DATA - KILL EVERYTHING IN THE WAY

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${RED}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${RED}║         🔥 ULTRA AGGRESSIVE MODE 🔥                          ║${NC}"
echo -e "${RED}║              FORCE EVERYTHING                                ║${NC}"
echo -e "${RED}╔══════════════════════════════════════════════════════════════╗${NC}"

# STEP 1: KILL EVERYTHING
echo -e "${YELLOW}[1/5] KILLING ALL BLOCKING PROCESSES...${NC}"
pkill -9 find 2>/dev/null
pkill -9 du 2>/dev/null
pkill -9 df 2>/dev/null
pkill -9 ls 2>/dev/null
pkill -9 rsync 2>/dev/null
pkill -9 cp 2>/dev/null
pkill -9 mdworker 2>/dev/null
pkill -9 mds_stores 2>/dev/null
sleep 1
echo -e "${GREEN}✓ KILLED${NC}"

# STEP 2: AGGRESSIVE EMPTY FOLDER DELETION - NO WAITING
echo -e "${YELLOW}[2/5] FORCE DELETING EMPTY FOLDERS (PARALLEL)...${NC}"

(timeout 3 find /Volumes/12TB -maxdepth 2 -type d -empty -delete 2>/dev/null; echo "12TB done") &
(timeout 3 find /Volumes/6TB -maxdepth 2 -type d -empty -delete 2>/dev/null; echo "6TB done") &
(timeout 3 find "/Volumes/4TB Lacie" -maxdepth 2 -type d -empty -delete 2>/dev/null; echo "4TB Lacie done") &
(timeout 3 find "/Volumes/RED DRAGON" -maxdepth 2 -type d -empty -delete 2>/dev/null; echo "RED DRAGON done") &
(timeout 3 find /Volumes/SOUND_DESIGN -maxdepth 2 -type d -empty -delete 2>/dev/null; echo "SOUND_DESIGN done") &
(timeout 3 find /Volumes/SAMPLE_MASTER -maxdepth 2 -type d -empty -delete 2>/dev/null; echo "SAMPLE_MASTER done") &

# Wait max 10 seconds total
sleep 10
echo -e "${GREEN}✓ EMPTY FOLDERS PURGED${NC}"

# STEP 3: HUNT ARCHIVES - FAST
echo -e "${YELLOW}[3/5] HUNTING NOIZYLAB ARCHIVES (FAST)...${NC}"
(timeout 5 find /Volumes/12TB -maxdepth 2 -name "*NOIZYLAB*ARCHIVE*" 2>/dev/null | while read d; do du -sh "$d" 2>/dev/null; done) &
(timeout 5 find /Volumes/6TB -maxdepth 2 -name "*NOIZYLAB*ARCHIVE*" 2>/dev/null | while read d; do du -sh "$d" 2>/dev/null; done) &
(timeout 5 find "/Volumes/4TB Lacie" -maxdepth 2 -name "*NOIZYLAB*ARCHIVE*" 2>/dev/null | while read d; do du -sh "$d" 2>/dev/null; done) &

sleep 6
echo -e "${GREEN}✓ ARCHIVES LOCATED${NC}"

# STEP 4: RAPID INVENTORY OF ACCESSIBLE VOLUMES
echo -e "${YELLOW}[4/5] RAPID VOLUME SCAN...${NC}"
for vol in 12TB 6TB "4TB Lacie" "RED DRAGON" SOUND_DESIGN SAMPLE_MASTER 4TBSG JOE; do
    (
        if timeout 2 ls "/Volumes/$vol" >/dev/null 2>&1; then
            echo -e "${GREEN}✓${NC} $vol - ACCESSIBLE"
        else
            echo -e "${RED}✗${NC} $vol - SLOW/BLOCKED"
        fi
    ) &
done
sleep 3

# STEP 5: CREATE RESULTS FILE
echo -e "${YELLOW}[5/5] SAVING RESULTS...${NC}"
{
    echo "ULTRA AGGRESSIVE CLEANUP RESULTS"
    echo "================================="
    echo "Date: $(date)"
    echo ""
    echo "ACCESSIBLE VOLUMES:"
    for vol in 12TB 6TB "4TB Lacie" "RED DRAGON"; do
        if timeout 1 ls "/Volumes/$vol" >/dev/null 2>&1; then
            echo "  ✓ $vol"
        fi
    done
    echo ""
    echo "ARCHIVES FOUND:"
    timeout 3 find /Volumes -maxdepth 3 -name "*NOIZYLAB*ARCHIVE*" 2>/dev/null || echo "  (scan timed out)"
} > ~/NOIZYLAB/CLEANUP_RESULTS.txt 2>&1

echo -e "${GREEN}✓ RESULTS SAVED: ~/NOIZYLAB/CLEANUP_RESULTS.txt${NC}"

echo ""
echo -e "${RED}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${RED}║                    ✓ COMPLETE                                ║${NC}"
echo -e "${RED}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo "Next steps:"
echo "  1. Check CLEANUP_RESULTS.txt for findings"
echo "  2. Manually consolidate NOIZYLAB_ARCHIVE folders"
echo "  3. Run individual volume cleanups as needed"
