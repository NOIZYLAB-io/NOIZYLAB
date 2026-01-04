#!/bin/bash

# ═══════════════════════════════════════════════════════════════════
# DISKWARRIOR 5.2 - EMERGENCY BACKUP REPAIR GUIDE
# ═══════════════════════════════════════════════════════════════════
# Use when TechTool Pro 21 fails or as alternative repair strategy
# Running on: Mac Pro 12-core (FISH or RSP)
# ═══════════════════════════════════════════════════════════════════

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

clear

echo -e "${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════════╗
║           DISKWARRIOR 5.2 - EMERGENCY BACKUP GUIDE               ║
║     Alternative Repair Strategy for HFS+ Corruption             ║
╚═══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo -e "${YELLOW}════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}⚠️  WHEN TO USE DISKWARRIOR INSTEAD OF TECHTOOL PRO${NC}"
echo -e "${YELLOW}════════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
USE DISKWARRIOR 5.2 WHEN:

1. TechTool Pro 21 fails to repair a volume
   → Different algorithm may succeed

2. Volume has severe directory corruption
   → DiskWarrior specializes in directory rebuilding

3. "Invalid node structure" or "Keys out of order" errors
   → DiskWarrior's specialty

4. Need second opinion before data recovery service
   → Try DiskWarrior before spending $5000+

5. Volume won't mount at all
   → DiskWarrior can often rebuild unmountable volumes

6. Need to recover data from failing drive
   → DiskWarrior can copy good files to new drive

DO NOT USE DISKWARRIOR FOR:

✗ APFS volumes (not supported)
✗ Internal SSDs on macOS 10.13+ (APFS only)
✗ Routine maintenance (use TTP21 hot rod mode)
✗ Speed optimization (TTP21 is 6-10x faster)

EOF

echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}DISKWARRIOR 5.2 vs TECHTOOL PRO 21.0.6${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
DISKWARRIOR 5.2 ADVANTAGES:
✓ Different repair algorithm (complementary to TTP)
✓ Specializes in directory rebuilding
✓ Preview feature (see results before committing)
✓ Can succeed when other tools fail
✓ Excellent for "Invalid node structure" errors
✓ Strong track record (since 1998)

TECHTOOL PRO 21.0.6 ADVANTAGES:
✓ 6-10x faster with hot rod optimization
✓ More comprehensive test suite
✓ Better for large 50TB+ fleets
✓ Volume + File + Permissions + Surface scans
✓ Better cloning (fixed in 21.0.6)
✓ Active development (Dec 2025 update)
✓ Better progress tracking
✓ Safer GUI (no terminal hanging)

RECOMMENDED STRATEGY:
1. Primary: TechTool Pro 21 hot rod mode (fast, comprehensive)
2. Backup: DiskWarrior 5.2 (if TTP fails or severe corruption)
3. Last Resort: Professional data recovery service

EOF

echo -e "${MAGENTA}════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}DISKWARRIOR 5.2 EMERGENCY WORKFLOW${NC}"
echo -e "${MAGENTA}════════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
STEP 1: PREPARE MAC PRO 12-CORE (FISH/RSP)
──────────────────────────────────────────
• Connect failing drive to Mac Pro
• Ensure DiskWarrior 5.2 is installed
• Have DiskWarrior Recovery USB ready
• Verify sufficient free space for recovery

Commands:
  # Check DiskWarrior installation
  ls -la "/Applications/DiskWarrior.app"
  
  # Check connected drives
  diskutil list
  
  # Check free space
  df -h


STEP 2: BOOT FROM DISKWARRIOR RECOVERY (if needed)
──────────────────────────────────────────────────
• Insert DiskWarrior Recovery USB drive
• Restart Mac Pro
• Hold Option (⌥) key during startup
• Select "DiskWarrior Recovery" from boot menu

Note: Only needed if drive won't mount normally


STEP 3: RUN DISKWARRIOR DIRECTORY REBUILD
─────────────────────────────────────────
1. Launch DiskWarrior application
2. Select the damaged volume from list
3. Click "Rebuild" button
4. Wait for directory scan (can take hours for TB drives)
5. Review Preview window (compare damaged vs rebuilt)
6. Verify all your files appear in Preview
7. Click "Replace" to commit the repair

CRITICAL: Always preview before replacing!


STEP 4: VERIFY REPAIR SUCCESS
─────────────────────────────
After DiskWarrior completes:

  # Verify volume structure
  diskutil verifyVolume /Volumes/[VOLUME_NAME]
  
  # Check file count
  find /Volumes/[VOLUME_NAME] -type f | wc -l
  
  # Test read speed
  time dd if=/Volumes/[VOLUME_NAME]/testfile of=/dev/null bs=1m count=1000


STEP 5: BACKUP IMMEDIATELY
──────────────────────────
If repair successful:

  # Clone drive with TechTool Pro 21 (safer after 21.0.6 fix)
  # OR use Carbon Copy Cloner
  # OR use rsync
  
  rsync -avhP --progress /Volumes/SOURCE/ /Volumes/BACKUP/


STEP 6: OPTIONAL - RUN TECHTOOL PRO FOR VERIFICATION
────────────────────────────────────────────────────
After DiskWarrior repair, transfer drive back to M2 Ultra:

  bash ~/NOIZYLAB/TTP21_HOT_ROD_GUIDE.sh
  
  Run: File Structures + Permissions tests
  (Verify DiskWarrior's work)

EOF

echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}DISKWARRIOR 5.2 CAPABILITIES & LIMITATIONS${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
WHAT DISKWARRIOR CAN FIX:
✓ HFS+ directory corruption
✓ Invalid node structure errors
✓ Keys out of order errors
✓ B-tree corruption
✓ Catalog file damage
✓ Volume won't mount
✓ Files/folders disappeared
✓ Permission issues (some)
✓ Journaling errors

WHAT DISKWARRIOR CANNOT FIX:
✗ APFS volumes (not supported)
✗ Physical drive damage (bad sectors)
✗ Mechanical drive failure
✗ Firmware corruption
✗ Controller failures
✗ Encryption issues (some)
✗ Internal SSDs on macOS 10.13+

SUPPORTED FILE SYSTEMS:
✓ HFS+ (Mac OS Extended)
✓ HFS+ Journaled
✓ HFS+ Case-Sensitive
✓ HFS+ Encrypted (FileVault 2)
✓ Core Storage (Fusion Drive)

SUPPORTED CONNECTIONS:
✓ USB / USB 3.0 / USB-C
✓ Thunderbolt / Thunderbolt 2 / 3 / 4
✓ SATA / eSATA
✓ FireWire 400 / 800

SUPPORTED CONFIGURATIONS:
✓ External volumes
✓ RAID arrays
✓ Disk images
✓ Time Machine backups
✓ FileVault encrypted

EOF

echo -e "${YELLOW}════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}DISKWARRIOR 5.2 OPTIMIZATION FOR MAC PRO${NC}"
echo -e "${YELLOW}════════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
Mac Pro 12-core is less powerful than M2 Ultra, so:

EXPECT LONGER REPAIR TIMES:
• 4TB drive: 4-8 hours (vs 1-2 hours on M2 Ultra with TTP)
• 6TB drive: 6-12 hours
• 12TB drive: 12-24 hours

DO NOT use hot rod optimization on Mac Pro:
• Older architecture (Intel)
• Less RAM than M2 Ultra
• Slower CPU cores

BASIC OPTIMIZATION:
1. Close all other applications
2. Disable Spotlight (if not already):
   sudo mdutil -a -i off
   
3. Disable Time Machine:
   sudo tmutil disable
   
4. Connect via fastest port available:
   Thunderbolt > USB 3.0 > USB 2.0

5. Monitor with Activity Monitor:
   • DiskWarrior should use ~100-200% CPU
   • Memory pressure should be green
   • Disk activity on target volume

6. DO NOT INTERRUPT:
   • No sleep mode
   • Keep Mac Pro powered on
   • Don't disconnect drives during repair

EOF

echo -e "${CYAN}════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}RECOVERY STRATEGY: TTP FAILS SCENARIO${NC}"
echo -e "${CYAN}════════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
IF TECHTOOL PRO 21 FAILS ON M2 ULTRA:

1. TRANSFER DRIVE TO MAC PRO
   • Disconnect from M2 Ultra safely
   • Connect to Mac Pro 12-core
   • Wait for volume to appear (or not)

2. TRY DISKWARRIOR 5.2 FIRST
   • Different algorithm may succeed
   • Specializes in directory corruption
   • Can work on unmountable volumes

3. IF DISKWARRIOR SUCCEEDS:
   • Preview results carefully
   • Verify all files present
   • Replace directory
   • Backup IMMEDIATELY to new drive
   • Transfer back to M2 Ultra for verification

4. IF DISKWARRIOR ALSO FAILS:
   • Note exact error messages
   • Try DiskWarrior recovery from USB
   • Consider Drive Genius (if available)
   • Last resort: Professional data recovery

5. DOCUMENT EVERYTHING:
   • Screenshots of errors
   • SMART data (smartctl -a /dev/diskX)
   • Drive model/serial numbers
   • Symptoms and timeline

COST COMPARISON:
• DiskWarrior repair attempt: $0 (already owned)
• Professional data recovery: $500-$5000+
• ALWAYS try DiskWarrior before paying!

EOF

echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}QUICK REFERENCE: DISKWARRIOR 5.2 COMMANDS${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
CHECK DISKWARRIOR INSTALLATION:
  ls -la "/Applications/DiskWarrior.app"

LIST ALL VOLUMES (FIND TARGET):
  diskutil list

VERIFY VOLUME BEFORE REPAIR:
  diskutil verifyVolume /Volumes/[NAME]

CHECK SMART STATUS:
  diskutil info disk2 | grep SMART
  # OR with smartmontools:
  smartctl -a /dev/disk2

DISABLE SPOTLIGHT (SPEED UP):
  sudo mdutil -i off /Volumes/[NAME]

LAUNCH DISKWARRIOR:
  open -a DiskWarrior

AFTER REPAIR - VERIFY:
  diskutil verifyVolume /Volumes/[NAME]
  diskutil info /Volumes/[NAME]

CLONE TO SAFETY:
  # Use TechTool Pro 21 Volume Cloning
  # OR Carbon Copy Cloner
  # OR rsync

TRANSFER BACK TO M2 ULTRA:
  # Eject safely from Mac Pro
  diskutil eject /Volumes/[NAME]
  
  # Connect to M2 Ultra
  # Verify with TTP21 hot rod

EOF

echo -e "${MAGENTA}════════════════════════════════════════════════════════════${NC}"
echo -e "${MAGENTA}🛡️  DUAL-TOOL STRATEGY = MAXIMUM COVERAGE${NC}"
echo -e "${MAGENTA}════════════════════════════════════════════════════════════${NC}"
echo ""

cat << 'EOF'
YOUR COMPLETE REPAIR ARSENAL:

PRIMARY WEAPON: TechTool Pro 21.0.6 (M2 Ultra)
├─ 6-10x faster with hot rod mode
├─ Comprehensive test suite
├─ Perfect for routine maintenance
└─ Handles 90% of HFS+ issues

BACKUP WEAPON: DiskWarrior 5.2 (Mac Pro 12-core)
├─ Different algorithm
├─ Specializes in directory corruption
├─ Preview before committing
└─ Handles the 10% TTP can't fix

COMPLEMENTARY TOOLS:
├─ Drive Scope 2 (drive identification)
├─ MachineProfile (system diagnostics)
├─ Drive Genius (preventive monitoring)
└─ smartmontools (SMART monitoring)

WHY THIS STRATEGY WORKS:
• Different algorithms = better coverage
• Two different Macs = hardware diversity
• Multiple approaches = higher success rate
• Cost-effective vs data recovery services

BUSINESS VALUE:
For NOIZYLAB AI CPU Repair service:
• "We use multiple professional tools"
• "Two repair algorithms for maximum success"
• "Commercial-grade repair arsenal"
• Justifies premium pricing tiers

EOF

echo -e "${CYAN}════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}🚀 READY TO USE DISKWARRIOR AS BACKUP REPAIR!${NC}"
echo -e "${CYAN}════════════════════════════════════════════════════════════${NC}"
echo ""

echo "Having both TechTool Pro 21 + DiskWarrior 5.2 = Complete coverage!"
echo ""
echo "Next steps:"
echo "  1. Keep TTP21 as primary on M2 Ultra (fast, comprehensive)"
echo "  2. Keep DiskWarrior 5.2 ready on Mac Pro (backup strategy)"
echo "  3. Use DiskWarrior when TTP fails or for severe corruption"
echo ""
echo "Your 40-year archive has maximum protection! 🛡️"
echo ""
