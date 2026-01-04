#!/bin/bash

# ═══════════════════════════════════════════════════════════════════
# TECHTOOL PRO 21 - EMERGENCY DISK RECOVERY PLAN
# ═══════════════════════════════════════════════════════════════════
# For: Gabriel Almeida (40-year music career - IRREPLACEABLE audio/video)
# Problem: All external drives FROZEN despite Spotlight disabled
# Solution: Use TechTool Pro 21 to repair disk structure & permissions
# ═══════════════════════════════════════════════════════════════════

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════════╗
║                 TECHTOOL PRO 21 RECOVERY PLAN                     ║
║                   FOR FROZEN EXTERNAL DRIVES                      ║
╚═══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# ═══════════════════════════════════════════════════════════════════
# PHASE 1: TECHTOOL PRO 21 OPERATIONS (DO IN THIS ORDER)
# ═══════════════════════════════════════════════════════════════════

echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}PHASE 1: TECHTOOL PRO 21 CRITICAL OPERATIONS${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${GREEN}STEP 1: LAUNCH TECHTOOL PRO 21${NC}"
echo "1. Open TechTool Pro 21"
echo "2. Enter admin password when prompted"
echo ""

echo -e "${GREEN}STEP 2: RUN VOLUME STRUCTURES TEST (CRITICAL)${NC}"
echo "This fixes corrupted disk catalogs that freeze macOS:"
echo ""
echo "For EACH frozen drive (12TB, RED DRAGON, 6TB, 4TB Lacie):"
echo "  1. Select the volume in TechTool Pro"
echo "  2. Check: 'Volume Structures'"
echo "  3. Click 'Run Selected Tests'"
echo "  4. If errors found, click 'Repair'"
echo ""
echo "⚠️  THIS IS THE MOST IMPORTANT TEST - fixes catalog corruption"
echo ""

echo -e "${GREEN}STEP 3: RUN FILE STRUCTURES TEST${NC}"
echo "After Volume Structures, run File Structures:"
echo "  1. Select same volumes"
echo "  2. Check: 'File Structures'"
echo "  3. Click 'Run Selected Tests'"
echo "  4. If errors found, click 'Repair'"
echo ""

echo -e "${GREEN}STEP 4: FIX PERMISSIONS (TECHTOOL METHOD)${NC}"
echo "TechTool's permission repair is more thorough than diskutil:"
echo "  1. Select volumes"
echo "  2. Check: 'Permissions'"
echo "  3. Click 'Run Selected Tests'"
echo "  4. Click 'Repair' for any issues"
echo ""

echo -e "${GREEN}STEP 5: SURFACE SCAN (IF TIME PERMITS)${NC}"
echo "Optional but recommended for aging drives:"
echo "  1. Select volumes"
echo "  2. Check: 'Surface Scan'"
echo "  3. Click 'Run Selected Tests'"
echo "  4. This will take HOURS but finds bad sectors"
echo ""

# ═══════════════════════════════════════════════════════════════════
# PHASE 2: POST-TECHTOOL VERIFICATION
# ═══════════════════════════════════════════════════════════════════

echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}PHASE 2: POST-REPAIR VERIFICATION${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${GREEN}After TechTool repairs, run these commands:${NC}"
echo ""
echo "1. Test drive speed:"
echo "   bash ~/NOIZYLAB/QUICK_STATUS.sh"
echo ""
echo "2. If still slow, try 'Ignore Ownership':"
echo "   sudo bash ~/NOIZYLAB/FIX_12TB_PERMISSIONS.sh"
echo "   # Choose Option 5 for each slow drive"
echo ""
echo "3. Verify no hanging processes:"
echo "   bash ~/NOIZYLAB/TERMINAL_KILLER.sh"
echo ""

# ═══════════════════════════════════════════════════════════════════
# PHASE 3: RESUME CLEANUP OPERATIONS
# ═══════════════════════════════════════════════════════════════════

echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}PHASE 3: RESUME CLEANUP (AFTER DRIVES WORKING)${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo "Once drives are responsive, resume cleanup:"
echo ""
echo "1. Hunt for empty folders:"
echo "   bash ~/NOIZYLAB/HUNT_EMPTY_FOLDERS.sh"
echo ""
echo "2. Consolidate NOIZYLAB_ARCHIVE (46GB across 3 drives):"
echo "   bash ~/NOIZYLAB/HUNT_ARCHIVES.sh"
echo ""
echo "3. Run master cleanup sweep:"
echo "   bash ~/NOIZYLAB/ULTRA_AGGRESSIVE.sh"
echo ""

# ═══════════════════════════════════════════════════════════════════
# PRIORITY VOLUMES (DO THESE FIRST)
# ═══════════════════════════════════════════════════════════════════

echo -e "${RED}═══════════════════════════════════════════════════════════${NC}"
echo -e "${RED}PRIORITY ORDER (FIX IN THIS SEQUENCE):${NC}"
echo -e "${RED}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo "1. /Volumes/12TB          ← HIGHEST PRIORITY (main storage)"
echo "2. /Volumes/RED DRAGON    ← Second (3.2TB free)"
echo "3. /Volumes/6TB           ← Third (backup storage)"
echo "4. /Volumes/4TB Lacie     ← Fourth (archive storage)"
echo ""

# ═══════════════════════════════════════════════════════════════════
# WHY TECHTOOL PRO 21 IS THE RIGHT TOOL
# ═══════════════════════════════════════════════════════════════════

echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}WHY TECHTOOL PRO 21?${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo "✓ Repairs corrupted HFS+ catalog files (your exact issue)"
echo "✓ Fixes disk structures that Disk Utility can't reach"
echo "✓ More thorough than 'diskutil repairVolume'"
echo "✓ Can repair drives WHILE MOUNTED (no unmount needed)"
echo "✓ Finds bad sectors causing hang-ups"
echo "✓ Industry standard for Mac disk recovery"
echo ""

# ═══════════════════════════════════════════════════════════════════
# ALTERNATIVES IF TECHTOOL DOESN'T FIX IT
# ═══════════════════════════════════════════════════════════════════

echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}IF TECHTOOL DOESN'T FIX THE PROBLEM:${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo "Last resort options:"
echo ""
echo "1. REFORMAT TO APFS (fastest but requires backup):"
echo "   - APFS is 10x faster than HFS+ for large drives"
echo "   - Use Time Machine or Carbon Copy Cloner to backup first"
echo ""
echo "2. CHECK USB/THUNDERBOLT CABLES:"
echo "   - Bad cables cause freezing"
echo "   - Try different ports/cables"
echo ""
echo "3. TEST DRIVE HARDWARE:"
echo "   - Drives might be failing (SMART status)"
echo "   - TechTool can check this too"
echo ""

# ═══════════════════════════════════════════════════════════════════
# DOWNLOAD LINK
# ═══════════════════════════════════════════════════════════════════

echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}DOWNLOAD TECHTOOL PRO 21:${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo "https://www.micromat.com/products/techtool-pro"
echo ""
echo "Price: ~\$100 (worth every penny for your 40-year archive)"
echo "Free trial available to test before buying"
echo ""

echo -e "${BLUE}Press any key to continue...${NC}"
read -n 1 -s

echo ""
echo -e "${GREEN}✓ RECOVERY PLAN READY${NC}"
echo ""
echo "Start TechTool Pro 21 now and follow PHASE 1 above."
echo ""
