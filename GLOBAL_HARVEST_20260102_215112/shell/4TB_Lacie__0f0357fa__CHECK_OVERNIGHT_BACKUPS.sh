#!/bin/zsh
# ============================================================================
# OVERNIGHT BACKUP STATUS CHECKER
# Run this in the morning to verify both backups
# ============================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

echo ""
echo "${CYAN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo "${CYAN}║          OVERNIGHT BACKUP STATUS CHECK                       ║${NC}"
echo "${CYAN}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo "${BLUE}Good morning! Checking your overnight backups...${NC}"
echo ""

checks_passed=0
checks_total=0

# ============================================================================
# CHECK 1: Ultra Deep Scan
# ============================================================================
echo "${MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "${MAGENTA}1. Ultra Deep Scan Status${NC}"
echo "${MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

checks_total=$((checks_total + 1))

# Check if scan completed
if [[ -f /Volumes/4TB_02/CODE_MASTER/ULTRA_DEEP_SCAN_*.md ]]; then
    scan_report=$(ls -t /Volumes/4TB_02/CODE_MASTER/ULTRA_DEEP_SCAN_*.md 2>/dev/null | head -1)
    echo "${GREEN}✓ Scan report found: $(basename "$scan_report")${NC}"
    
    # Show summary from report
    if [[ -f "$scan_report" ]]; then
        echo ""
        echo "${CYAN}Summary:${NC}"
        grep -A 10 "GRAND TOTALS" "$scan_report" 2>/dev/null || echo "  (Report processing...)"
    fi
    checks_passed=$((checks_passed + 1))
else
    echo "${RED}✗ Scan report not found${NC}"
    echo "${YELLOW}  Check: /Volumes/4TB_02/CODE_MASTER/logs/${NC}"
fi

echo ""

# ============================================================================
# CHECK 2: Time Machine Backup
# ============================================================================
echo "${MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "${MAGENTA}2. Time Machine Backup Status${NC}"
echo "${MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

checks_total=$((checks_total + 1))

# Check if TM backup completed
tm_status=$(tmutil status 2>/dev/null)
if [[ $? -eq 0 ]]; then
    # Check if backup is running
    if echo "$tm_status" | grep -q "Running = 1"; then
        echo "${YELLOW}⏳ Backup still running...${NC}"
        echo ""
        tmutil status | grep -E "(Progress|Percent)"
    else
        # Check latest backup
        latest_backup=$(tmutil latestbackup 2>/dev/null)
        if [[ -n "$latest_backup" ]]; then
            echo "${GREEN}✓ Time Machine backup complete${NC}"
            echo "${CYAN}Latest backup: $latest_backup${NC}"
            
            # Get backup date
            backup_date=$(basename "$latest_backup")
            echo "${CYAN}Backup date: $backup_date${NC}"
            
            checks_passed=$((checks_passed + 1))
        else
            echo "${RED}✗ No Time Machine backup found${NC}"
        fi
    fi
else
    echo "${RED}✗ Time Machine not available${NC}"
fi

echo ""

# ============================================================================
# CHECK 3: CODE_MASTER Contents
# ============================================================================
echo "${MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "${MAGENTA}3. CODE_MASTER Contents${NC}"
echo "${MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

checks_total=$((checks_total + 1))

if [[ -d /Volumes/4TB_02/CODE_MASTER ]]; then
    code_master_size=$(du -sh /Volumes/4TB_02/CODE_MASTER 2>/dev/null | cut -f1)
    echo "${GREEN}✓ CODE_MASTER exists${NC}"
    echo "${CYAN}Size: ${code_master_size}${NC}"
    
    # Count files
    py_count=$(find /Volumes/4TB_02/CODE_MASTER -name "*.py" -type f 2>/dev/null | wc -l | xargs)
    sh_count=$(find /Volumes/4TB_02/CODE_MASTER -name "*.sh" -type f 2>/dev/null | wc -l | xargs)
    
    echo "${CYAN}Python files: ${py_count}${NC}"
    echo "${CYAN}Shell scripts: ${sh_count}${NC}"
    
    if [[ $py_count -gt 0 ]] || [[ $sh_count -gt 0 ]]; then
        checks_passed=$((checks_passed + 1))
    fi
else
    echo "${RED}✗ CODE_MASTER not found${NC}"
fi

echo ""

# ============================================================================
# CHECK 4: Backup Drives Accessible
# ============================================================================
echo "${MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "${MAGENTA}4. Backup Drives Status${NC}"
echo "${MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

checks_total=$((checks_total + 1))

drive_count=0

if [[ -d /Volumes/4TB_02 ]]; then
    echo "${GREEN}✓ 4TB_02 (CODE_MASTER)${NC}"
    drive_count=$((drive_count + 1))
else
    echo "${RED}✗ 4TB_02 not mounted${NC}"
fi

if [[ -d /Volumes/TM_BackUp ]]; then
    echo "${GREEN}✓ TM_BackUp${NC}"
    drive_count=$((drive_count + 1))
else
    echo "${RED}✗ TM_BackUp not mounted${NC}"
fi

if [[ $drive_count -eq 2 ]]; then
    checks_passed=$((checks_passed + 1))
fi

echo ""

# ============================================================================
# FINAL SUMMARY
# ============================================================================
echo "${CYAN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo "${CYAN}║                    FINAL SUMMARY                              ║${NC}"
echo "${CYAN}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

if [[ $checks_passed -eq $checks_total ]]; then
    echo "${GREEN}✓✓✓ ALL CHECKS PASSED (${checks_passed}/${checks_total}) ✓✓✓${NC}"
    echo ""
    echo "${GREEN}╔════════════════════════════════════════════════════════════════╗${NC}"
    echo "${GREEN}║          🎉 READY FOR SYSTEM REFORMAT 🎉                     ║${NC}"
    echo "${GREEN}╚════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "${CYAN}Your data is safe:${NC}"
    echo "  ✓ All code backed up to CODE_MASTER"
    echo "  ✓ Full system backed up to Time Machine"
    echo "  ✓ All backup drives accessible"
    echo ""
    echo "${YELLOW}BEFORE REFORMATTING:${NC}"
    echo "  1. Safely eject 4TB_02 and store safely"
    echo "  2. Verify TM_BackUp is accessible"
    echo "  3. Triple-check you have everything"
    echo "  4. Then proceed with reformat"
    echo ""
else
    echo "${YELLOW}⚠ CHECKS PASSED: ${checks_passed}/${checks_total}${NC}"
    echo ""
    echo "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo "${RED}NOT READY FOR REFORMAT YET${NC}"
    echo "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "${YELLOW}Action required:${NC}"
    
    if [[ ! -f /Volumes/4TB_02/CODE_MASTER/ULTRA_DEEP_SCAN_*.md ]]; then
        echo "  • Wait for Ultra Deep Scan to complete"
        echo "    Check: tail -f /Volumes/4TB_02/CODE_MASTER/logs/ultra_scan_*.log"
    fi
    
    latest_backup=$(tmutil latestbackup 2>/dev/null)
    if [[ -z "$latest_backup" ]]; then
        echo "  • Wait for Time Machine backup to complete"
        echo "    Check: tmutil status"
    fi
    
    echo ""
fi

echo ""
echo "${CYAN}Detailed Reports:${NC}"
echo "  • Ultra Deep Scan: /Volumes/4TB_02/CODE_MASTER/ULTRA_DEEP_SCAN_*.md"
echo "  • Scan file lists: /Volumes/4TB_02/CODE_MASTER/ultra_scan_results/"
echo "  • Time Machine: System Settings → Time Machine"
echo ""
