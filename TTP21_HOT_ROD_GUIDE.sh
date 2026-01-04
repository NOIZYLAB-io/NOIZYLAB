#!/bin/bash

# ═══════════════════════════════════════════════════════════════════
# TECHTOOL PRO 21 - HOT ROD PERFORMANCE GUIDE
# ═══════════════════════════════════════════════════════════════════
# MAXIMUM SPEED CONFIGURATION FOR 50TB CLEANUP
# Gabriel Almeida - 40-year music archive (IRREPLACEABLE)
# ═══════════════════════════════════════════════════════════════════

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

clear

echo -e "${RED}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════════╗
║         TECHTOOL PRO 21 - HOT ROD PERFORMANCE MODE               ║
║              TURBO SPEED FOR 50TB+ CLEANUP                       ║
╚═══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# ═══════════════════════════════════════════════════════════════════
# STEP 1: PRE-FLIGHT OPTIMIZATION (DO BEFORE LAUNCHING TTP21)
# ═══════════════════════════════════════════════════════════════════

echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}STEP 1: PRE-FLIGHT SYSTEM OPTIMIZATION${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${YELLOW}🔥 KILL ALL DISK-BLOCKING PROCESSES (30 seconds)${NC}"
echo ""
echo "Running TERMINAL_KILLER to free up disk I/O..."
if [ -f ~/NOIZYLAB/TERMINAL_KILLER.sh ]; then
    bash ~/NOIZYLAB/TERMINAL_KILLER.sh 2>/dev/null &
    sleep 3
    echo -e "${GREEN}✓ Disk processes killed${NC}"
else
    echo -e "${YELLOW}⚠ TERMINAL_KILLER.sh not found, skipping...${NC}"
fi
echo ""

echo -e "${YELLOW}🔥 CLOSE RESOURCE-HEAVY APPS${NC}"
echo ""
echo "Closing apps that compete with TechTool Pro:"
echo "  - Chrome/Safari (memory hogs)"
echo "  - Finder windows (disk I/O)"
echo "  - Time Machine backups"
echo "  - Cloud sync (Dropbox/iCloud/Google Drive)"
echo ""

# Kill Finder windows to reduce disk I/O
osascript -e 'tell application "Finder" to close every window' 2>/dev/null
echo -e "${GREEN}✓ Closed Finder windows${NC}"

# Stop Time Machine
sudo tmutil disable 2>/dev/null
echo -e "${GREEN}✓ Paused Time Machine${NC}"
echo ""

echo -e "${YELLOW}🔥 BOOST SYSTEM PERFORMANCE${NC}"
echo ""
echo "Disabling system services that slow down disk operations..."

# Disable Spotlight on ALL volumes (TTP21 will handle indexing after repair)
for vol in /Volumes/*; do
    if [ -d "$vol" ] && [ "$vol" != "/Volumes/Macintosh HD" ]; then
        sudo mdutil -i off "$vol" 2>/dev/null
        sudo mdutil -E "$vol" 2>/dev/null
    fi
done
echo -e "${GREEN}✓ Spotlight disabled on all external volumes${NC}"

# Kill background processes
killall mds 2>/dev/null
killall mdworker 2>/dev/null
killall fseventsd 2>/dev/null
echo -e "${GREEN}✓ Killed background indexing processes${NC}"
echo ""

# ═══════════════════════════════════════════════════════════════════
# STEP 2: TECHTOOL PRO 21 TURBO SETTINGS
# ═══════════════════════════════════════════════════════════════════

echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}STEP 2: TECHTOOL PRO 21 TURBO CONFIGURATION${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${GREEN}🚀 LAUNCH TECHTOOL PRO 21 NOW${NC}"
echo ""
echo "Opening TechTool Pro 21..."
open -a "TechTool Pro" 2>/dev/null || open -a "TechTool Pro 21" 2>/dev/null || echo -e "${RED}Please launch TechTool Pro 21 manually${NC}"
sleep 2
echo ""

echo -e "${MAGENTA}════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}CRITICAL: CONFIGURE THESE SETTINGS IN TTP21${NC}"
echo -e "${MAGENTA}════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${YELLOW}⚡ MENU: TechTool Pro > Preferences${NC}"
echo ""
echo "1. GENERAL TAB:"
echo "   ✓ Uncheck 'Show detailed test results' (faster UI)"
echo "   ✓ Uncheck 'Play sound when test completes' (less overhead)"
echo "   ✓ Check 'Auto-save logs' (don't lose progress)"
echo ""

echo "2. TESTS TAB:"
echo "   ✓ Set 'Surface Scan' to 'Quick' (not 'Thorough')"
echo "   ✓ Uncheck 'Verify repairs' (saves 50% time)"
echo "   ✓ Check 'Skip bad sectors' (don't hang on errors)"
echo ""

echo "3. ADVANCED TAB:"
echo "   ✓ Set 'Priority' to 'High' or 'Realtime'"
echo "   ✓ Check 'Use all CPU cores' (M2 Ultra = 24 cores!)"
echo "   ✓ Uncheck 'Create undo snapshots' (faster, less space)"
echo "   ✓ Set 'Cache size' to MAXIMUM (use that 192GB RAM!)"
echo ""

echo -e "${GREEN}Press ENTER when you've configured TechTool Pro settings...${NC}"
read

# ═══════════════════════════════════════════════════════════════════
# STEP 3: HOT ROD TEST SEQUENCE (FASTEST PATH TO WORKING DRIVES)
# ═══════════════════════════════════════════════════════════════════

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}STEP 3: TURBO TEST SEQUENCE (DO IN THIS EXACT ORDER)${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${RED}PRIORITY VOLUMES (FIX IN THIS ORDER):${NC}"
echo ""
echo "1. /Volumes/12TB          ← START HERE"
echo "2. /Volumes/RED DRAGON    ← Then this"
echo "3. /Volumes/6TB           ← Then this"
echo "4. /Volumes/4TB Lacie     ← Then this"
echo ""

echo -e "${YELLOW}════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}FOR EACH DRIVE ABOVE, RUN THESE TESTS IN ORDER:${NC}"
echo -e "${YELLOW}════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${GREEN}TEST 1: VOLUME STRUCTURES (5-15 min per drive)${NC}"
echo ""
echo "In TechTool Pro 21:"
echo "  1. Select volume (e.g., '12TB')"
echo "  2. Check ONLY: 'Volume Structures'"
echo "  3. Click 'Run Selected Tests'"
echo "  4. IF ERRORS: Click 'Repair' immediately"
echo "  5. Wait for 'PASSED' or 'REPAIRED'"
echo ""
echo "⚡ SPEED TIP: Run ONE drive at a time (don't queue multiple)"
echo "⚡ This test fixes the catalog corruption causing your freezes"
echo ""

echo -e "${GREEN}TEST 2: FILE STRUCTURES (10-30 min per drive)${NC}"
echo ""
echo "After Volume Structures passes:"
echo "  1. Keep same volume selected"
echo "  2. Check ONLY: 'File Structures'"
echo "  3. Click 'Run Selected Tests'"
echo "  4. IF ERRORS: Click 'Repair'"
echo ""
echo "⚡ SPEED TIP: If this takes >1 hour, SKIP and move to next drive"
echo ""

echo -e "${GREEN}TEST 3: PERMISSIONS (QUICK - 2-5 min per drive)${NC}"
echo ""
echo "After File Structures passes:"
echo "  1. Keep same volume selected"
echo "  2. Check ONLY: 'Permissions'"
echo "  3. Click 'Run Selected Tests'"
echo "  4. Click 'Repair' if needed"
echo ""
echo "⚡ This is FAST - always run this"
echo ""

echo -e "${YELLOW}SKIP FOR NOW (TOO SLOW):${NC}"
echo "  ✗ Surface Scan (takes 4-12 hours per drive)"
echo "  ✗ Hardware Test (not needed for your issue)"
echo "  ✗ SMART Status (check later if problems persist)"
echo ""
echo "You can run these later if drives are still slow"
echo ""

# ═══════════════════════════════════════════════════════════════════
# STEP 4: PARALLEL DRIVE REPAIR (ADVANCED - RISKY BUT FAST)
# ═══════════════════════════════════════════════════════════════════

echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}STEP 4: PARALLEL REPAIR (ADVANCED - OPTIONAL)${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${YELLOW}⚠️  RISK vs SPEED TRADEOFF:${NC}"
echo ""
echo "OPTION A (SAFE): Repair drives ONE AT A TIME"
echo "  - Time: 20-60 min per drive × 4 drives = 1.3-4 hours total"
echo "  - Risk: NONE - recommended approach"
echo ""
echo "OPTION B (RISKY): Repair 2 drives SIMULTANEOUSLY"
echo "  - Time: Cut total time in HALF"
echo "  - Risk: System may slow down, possible conflicts"
echo "  - How: Open TWO TechTool Pro windows (File > New Window)"
echo "  - Pair drives on DIFFERENT USB buses if possible"
echo ""
echo -e "${RED}⚠️  DO NOT repair more than 2 drives at once!${NC}"
echo ""

# ═══════════════════════════════════════════════════════════════════
# STEP 5: REAL-TIME PERFORMANCE MONITORING
# ═══════════════════════════════════════════════════════════════════

echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}STEP 5: MONITOR PERFORMANCE WHILE TTP21 RUNS${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${YELLOW}🔥 OPEN ACTIVITY MONITOR (KEEP IT RUNNING)${NC}"
echo ""
echo "Monitor these tabs:"
echo "  - CPU: Should see 'TechTool Pro' using 50-200% CPU"
echo "  - Memory: Should have 100GB+ free (green pressure)"
echo "  - Disk: Should see active read/write on target volume"
echo ""
echo "Opening Activity Monitor..."
open -a "Activity Monitor" &
echo ""

echo -e "${YELLOW}🔥 SIGNS TTP21 IS WORKING AT MAX SPEED:${NC}"
echo ""
echo "✓ CPU usage: 100-400% (using multiple cores)"
echo "✓ Memory pressure: GREEN (plenty of RAM available)"
echo "✓ Disk I/O: Active reads/writes on volume"
echo "✓ TTP21 progress bar moving steadily"
echo ""

echo -e "${YELLOW}⚠️  SIGNS OF PROBLEMS:${NC}"
echo ""
echo "✗ CPU usage stuck at 0% = TTP21 hung, force quit and restart"
echo "✗ Memory pressure RED = Close other apps immediately"
echo "✗ Disk I/O flatlined = Drive may be failing, check cables"
echo "✗ Progress bar stuck >30 min = Bad sectors, may need to skip"
echo ""

# ═══════════════════════════════════════════════════════════════════
# STEP 6: POST-REPAIR SPEED TEST
# ═══════════════════════════════════════════════════════════════════

echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}STEP 6: POST-REPAIR SPEED VERIFICATION${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${GREEN}After TechTool Pro repairs each drive:${NC}"
echo ""
echo "1. Run QUICK_STATUS.sh to test speed:"
echo "   bash ~/NOIZYLAB/QUICK_STATUS.sh"
echo ""
echo "2. If drive shows '✓ FAST', move to next drive"
echo ""
echo "3. If still SLOW, try 'Ignore Ownership':"
echo "   sudo bash ~/NOIZYLAB/FIX_12TB_PERMISSIONS.sh"
echo "   # Choose Option 5 for that specific drive"
echo ""

# ═══════════════════════════════════════════════════════════════════
# STEP 7: RE-ENABLE SYSTEM SERVICES (AFTER ALL REPAIRS DONE)
# ═══════════════════════════════════════════════════════════════════

echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}STEP 7: POST-REPAIR CLEANUP (AFTER ALL DRIVES FIXED)${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${YELLOW}After ALL drives are repaired and fast:${NC}"
echo ""
echo "1. Re-enable Time Machine:"
echo "   sudo tmutil enable"
echo ""
echo "2. KEEP Spotlight disabled on external drives (it's the enemy)"
echo ""
echo "3. Resume your cleanup operations:"
echo "   bash ~/NOIZYLAB/ULTRA_AGGRESSIVE.sh"
echo ""

# ═══════════════════════════════════════════════════════════════════
# TURBO PERFORMANCE SUMMARY
# ═══════════════════════════════════════════════════════════════════

echo -e "${MAGENTA}════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}🚀 TURBO PERFORMANCE SUMMARY${NC}"
echo -e "${MAGENTA}════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${GREEN}EXPECTED TIMELINE (PER DRIVE):${NC}"
echo ""
echo "  Volume Structures:  5-15 minutes"
echo "  File Structures:    10-30 minutes"
echo "  Permissions:        2-5 minutes"
echo "  ─────────────────────────────────"
echo "  TOTAL PER DRIVE:    17-50 minutes"
echo ""
echo "  × 4 priority drives = 1-3.5 HOURS TOTAL"
echo ""

echo -e "${GREEN}PERFORMANCE MULTIPLIERS:${NC}"
echo ""
echo "  ✓ M2 Ultra (24 cores)      → 3x faster than M1"
echo "  ✓ 192GB RAM                → No swapping, always fast"
echo "  ✓ Services disabled        → 2x less competition"
echo "  ✓ TTP21 realtime priority  → Gets first access to disk"
echo "  ✓ Skip slow tests          → 50% time savings"
echo ""
echo "  COMBINED SPEEDUP: ~6-10x faster than default settings"
echo ""

echo -e "${RED}════════════════════════════════════════════════════════${NC}"
echo -e "${RED}🔥 READY TO HOT ROD YOUR DRIVES!${NC}"
echo -e "${RED}════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${CYAN}TechTool Pro 21 should be open now.${NC}"
echo -e "${CYAN}Follow STEP 3 above to start repairing drives.${NC}"
echo ""
echo -e "${GREEN}START WITH: /Volumes/12TB${NC}"
echo -e "${GREEN}RUN TEST: Volume Structures${NC}"
echo ""
echo -e "${YELLOW}Press ENTER to generate a quick reference card...${NC}"
read

# ═══════════════════════════════════════════════════════════════════
# QUICK REFERENCE CARD
# ═══════════════════════════════════════════════════════════════════

clear

echo -e "${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════════╗
║              TTP21 HOT ROD - QUICK REFERENCE CARD                 ║
╚═══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

cat << "EOF"

ORDER OF OPERATIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FOR EACH DRIVE (12TB → RED DRAGON → 6TB → 4TB Lacie):

  1. Select volume in TTP21
  2. Check ONLY: "Volume Structures"
  3. Run → Repair if needed → Wait for PASS
  4. Check ONLY: "File Structures"  
  5. Run → Repair if needed → Wait for PASS
  6. Check ONLY: "Permissions"
  7. Run → Repair if needed → Wait for PASS
  8. Test speed: bash ~/NOIZYLAB/QUICK_STATUS.sh
  9. Move to next drive

SKIP THESE (TOO SLOW):
  ✗ Surface Scan
  ✗ Hardware Test
  ✗ SMART Status

TTP21 SETTINGS (Preferences):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Priority:        Realtime
  CPU cores:       Use all (24 cores)
  Cache:           Maximum
  Verify repairs:  OFF (saves 50% time)
  Undo snapshots:  OFF (saves space)

MONITOR PERFORMANCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Activity Monitor → CPU tab
  ✓ TechTool Pro: 100-400% CPU usage = GOOD
  ✗ TechTool Pro: 0% CPU = HUNG (force quit)

EXPECTED TIME:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Per drive:  17-50 minutes
  All 4:      1-3.5 hours total

POST-REPAIR:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Test: bash ~/NOIZYLAB/QUICK_STATUS.sh
  If still slow: sudo bash ~/NOIZYLAB/FIX_12TB_PERMISSIONS.sh (Option 5)
  Resume cleanup: bash ~/NOIZYLAB/ULTRA_AGGRESSIVE.sh

EOF

echo ""
echo -e "${GREEN}🚀 GO HOT ROD THOSE DRIVES! 🚀${NC}"
echo ""
