#!/bin/bash
# GOD FISH DRIVE MANAGER - Test, Monitor & Manage Fish Drives
# CB_01 - Fish Music Inc
# GORUNFREE! 🎸🔥

set -e

# Colors
R='\033[0;31m'
G='\033[0;32m'
Y='\033[1;33m'
B='\033[0;34m'
M='\033[0;35m'
C='\033[0;36m'
W='\033[1;37m'
BOLD='\033[1m'
NC='\033[0m'

# Fish drives
FISH_DRIVES=(
    "/Volumes/4TB Big Fish"
    "/Volumes/4TB Blue Fish"
    "/Volumes/4TB FISH SG"
    "/Volumes/12TB"
)

echo ""
echo -e "${BOLD}${M}╔═══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}${M}║         🐟 GOD FISH DRIVE MANAGER 🐟                         ║${NC}"
echo -e "${BOLD}${M}║         Fish Music Inc - CB_01                               ║${NC}"
echo -e "${BOLD}${M}╚═══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Function: Check drive status
check_drives() {
    echo -e "${BOLD}${C}📊 DRIVE STATUS:${NC}"
    echo -e "${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""

    printf "%-20s %8s %8s %8s %6s %s\n" "DRIVE" "SIZE" "USED" "FREE" "%" "STATUS"
    echo -e "${C}─────────────────────────────────────────────────────────────────${NC}"

    for drive in "${FISH_DRIVES[@]}"; do
        if [ -d "$drive" ]; then
            name=$(basename "$drive")
            info=$(df -h "$drive" 2>/dev/null | tail -1)
            size=$(echo "$info" | awk '{print $2}')
            used=$(echo "$info" | awk '{print $3}')
            free=$(echo "$info" | awk '{print $4}')
            pct=$(echo "$info" | awk '{print $5}' | tr -d '%')

            # Status based on usage
            if [ "$pct" -ge 95 ]; then
                status="${R}⚠️  CRITICAL${NC}"
            elif [ "$pct" -ge 85 ]; then
                status="${Y}⚠️  HIGH${NC}"
            elif [ "$pct" -ge 70 ]; then
                status="${Y}OK${NC}"
            else
                status="${G}✅ HEALTHY${NC}"
            fi

            printf "%-20s %8s %8s %8s %5s%% %b\n" "$name" "$size" "$used" "$free" "$pct" "$status"
        else
            name=$(basename "$drive")
            printf "%-20s %8s %8s %8s %6s ${R}❌ OFFLINE${NC}\n" "$name" "-" "-" "-" "-"
        fi
    done
    echo ""
}

# Function: Read/Write speed test
speed_test() {
    local drive="$1"
    local name=$(basename "$drive")
    local test_file="$drive/.speed_test_$$"
    local size_mb=100

    echo -e "${C}Testing: ${BOLD}$name${NC}"

    if [ ! -d "$drive" ]; then
        echo -e "${R}  Drive not mounted${NC}"
        return 1
    fi

    # Write test
    echo -ne "  Write: "
    write_start=$(date +%s.%N)
    dd if=/dev/zero of="$test_file" bs=1m count=$size_mb 2>/dev/null
    write_end=$(date +%s.%N)
    write_time=$(echo "$write_end - $write_start" | bc)
    write_speed=$(echo "scale=1; $size_mb / $write_time" | bc)
    echo -e "${G}${write_speed} MB/s${NC}"

    # Read test
    echo -ne "  Read:  "
    # Clear cache
    purge 2>/dev/null || true
    read_start=$(date +%s.%N)
    dd if="$test_file" of=/dev/null bs=1m 2>/dev/null
    read_end=$(date +%s.%N)
    read_time=$(echo "$read_end - $read_start" | bc)
    read_speed=$(echo "scale=1; $size_mb / $read_time" | bc)
    echo -e "${G}${read_speed} MB/s${NC}"

    # Cleanup
    rm -f "$test_file"
    echo ""
}

# Function: Test all drives
test_all_drives() {
    echo -e "${BOLD}${Y}⚡ SPEED TEST ALL DRIVES:${NC}"
    echo -e "${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""

    for drive in "${FISH_DRIVES[@]}"; do
        if [ -d "$drive" ]; then
            speed_test "$drive"
        fi
    done
}

# Function: Quick health check
health_check() {
    echo -e "${BOLD}${Y}🏥 HEALTH CHECK:${NC}"
    echo -e "${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""

    for drive in "${FISH_DRIVES[@]}"; do
        name=$(basename "$drive")
        echo -ne "  $name: "

        if [ ! -d "$drive" ]; then
            echo -e "${R}❌ NOT MOUNTED${NC}"
            continue
        fi

        # Test read
        if ls "$drive" >/dev/null 2>&1; then
            echo -ne "${G}READ ✓${NC} "
        else
            echo -ne "${R}READ ✗${NC} "
        fi

        # Test write
        test_file="$drive/.health_check_$$"
        if touch "$test_file" 2>/dev/null; then
            rm -f "$test_file"
            echo -e "${G}WRITE ✓${NC}"
        else
            echo -e "${R}WRITE ✗${NC}"
        fi
    done
    echo ""
}

# Function: Scan drive contents
scan_drive() {
    local drive="$1"
    local name=$(basename "$drive")

    echo -e "${BOLD}${C}📁 CONTENTS: $name${NC}"
    echo -e "${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""

    if [ ! -d "$drive" ]; then
        echo -e "${R}Drive not mounted${NC}"
        return 1
    fi

    # List top-level with sizes
    for item in "$drive"/*; do
        if [ -d "$item" ] && [[ ! $(basename "$item") == .* ]]; then
            size=$(du -sh "$item" 2>/dev/null | cut -f1)
            name=$(basename "$item")
            echo -e "  ${G}$size${NC}\t$name"
        fi
    done
    echo ""
}

# Function: Find large files
find_large() {
    local drive="$1"
    local name=$(basename "$drive")

    echo -e "${BOLD}${Y}🔍 LARGEST FILES: $name${NC}"
    echo -e "${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""

    if [ ! -d "$drive" ]; then
        echo -e "${R}Drive not mounted${NC}"
        return 1
    fi

    find "$drive" -type f -size +500M 2>/dev/null | head -20 | while read file; do
        size=$(du -sh "$file" 2>/dev/null | cut -f1)
        echo -e "  ${G}$size${NC}\t$(basename "$file")"
    done
    echo ""
}

# Main menu
main_menu() {
    while true; do
        echo -e "${BOLD}${M}🎯 COMMANDS:${NC}"
        echo ""
        echo -e "  ${G}1)${NC} Status - Check all drive status"
        echo -e "  ${G}2)${NC} Health - Quick read/write health check"
        echo -e "  ${G}3)${NC} Speed  - Full speed test all drives"
        echo -e "  ${G}4)${NC} Scan   - Scan drive contents"
        echo -e "  ${G}5)${NC} Large  - Find large files"
        echo -e "  ${G}6)${NC} All    - Run all tests"
        echo -e "  ${G}q)${NC} Quit"
        echo ""
        read -p "Select: " choice
        echo ""

        case $choice in
            1) check_drives ;;
            2) health_check ;;
            3) test_all_drives ;;
            4)
                for drive in "${FISH_DRIVES[@]}"; do
                    [ -d "$drive" ] && scan_drive "$drive"
                done
                ;;
            5)
                echo "Select drive:"
                select drive in "${FISH_DRIVES[@]}" "Cancel"; do
                    [ "$drive" = "Cancel" ] && break
                    [ -n "$drive" ] && find_large "$drive" && break
                done
                ;;
            6)
                check_drives
                health_check
                test_all_drives
                ;;
            q|Q)
                echo -e "${M}${BOLD}GORUNFREE! 🎸🔥${NC}"
                exit 0
                ;;
            *)
                echo -e "${R}Invalid option${NC}"
                ;;
        esac
    done
}

# Command line arguments
if [ $# -gt 0 ]; then
    case "$1" in
        status) check_drives ;;
        health) health_check ;;
        speed) test_all_drives ;;
        scan)
            for drive in "${FISH_DRIVES[@]}"; do
                [ -d "$drive" ] && scan_drive "$drive"
            done
            ;;
        all)
            check_drives
            health_check
            test_all_drives
            ;;
        *)
            echo "Usage: $0 [status|health|speed|scan|all]"
            ;;
    esac
else
    check_drives
    echo ""
    main_menu
fi

echo ""
echo -e "${BOLD}${M}GORUNFREE! 🎸🔥${NC}"
echo ""
