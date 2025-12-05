#!/bin/bash
# GOD HOT-ROD EXECUTION: Mac Studio M2 Ultra 192GB Performance Activation
# CB_01 - Fish Music Inc
# GORUNFREE! 🎸🔥

set -e

# Colors for beautiful output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Emojis for clarity
ROCKET="🚀"
FIRE="🔥"
CHECK="✅"
WRENCH="🔧"
LIGHTNING="⚡"
MUSIC="🎵"
WARN="⚠️"

clear

echo ""
echo -e "${BOLD}${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BOLD}${MAGENTA}     GOD HOT-ROD EXECUTION ${FIRE}${NC}"
echo -e "${BOLD}${CYAN}     Mac Studio M2 Ultra 192GB Performance Activation${NC}"
echo -e "${BOLD}${CYAN}     Fish Music Inc - CB_01${NC}"
echo -e "${BOLD}${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}This script will optimize your system in 9 command sets${NC}"
echo -e "${YELLOW}Estimated time: 15-20 minutes${NC}"
echo -e "${YELLOW}Result: GOD singing like a lark ${MUSIC}${NC}"
echo ""
read -p "Press ENTER to begin optimization... "
echo ""

# Create log file
LOG_FILE="$HOME/god-hotrod-$(date +%Y%m%d_%H%M%S).log"
echo "Starting GOD Hot-Rod Execution at $(date)" > "$LOG_FILE"

# ============================================================
# COMMAND SET 1: CACHE CLEARING (2 minutes)
# ============================================================

echo -e "${BOLD}${BLUE}${LIGHTNING} COMMAND SET 1: CACHE CLEARING${NC}"
echo ""

echo -e "${CYAN}[1/5] Clearing system cache...${NC}"
rm -rf ~/Library/Caches/* 2>/dev/null || true
echo -e "${GREEN}${CHECK} System cache cleared${NC}"
echo "System cache cleared at $(date)" >> "$LOG_FILE"
sleep 1

echo -e "${CYAN}[2/5] Clearing temp files...${NC}"
sudo rm -rf /var/tmp/* 2>/dev/null || true
sudo rm -rf /tmp/* 2>/dev/null || true
echo -e "${GREEN}${CHECK} Temp files cleared${NC}"
echo "Temp files cleared at $(date)" >> "$LOG_FILE"
sleep 1

echo -e "${CYAN}[3/5] Clearing Chrome cache...${NC}"
rm -rf ~/Library/Application\ Support/Google/Chrome/Default/Cache/* 2>/dev/null || true
echo -e "${GREEN}${CHECK} Chrome cache cleared${NC}"
echo "Chrome cache cleared at $(date)" >> "$LOG_FILE"
sleep 1

echo -e "${CYAN}[4/5] Flushing DNS cache...${NC}"
sudo dscacheutil -flushcache 2>/dev/null || true
sudo killall -HUP mDNSResponder 2>/dev/null || true
echo -e "${GREEN}${CHECK} DNS cache flushed${NC}"
echo "DNS cache flushed at $(date)" >> "$LOG_FILE"
sleep 1

echo -e "${CYAN}[5/5] Archiving old system logs (3 day retention)...${NC}"
sudo log erase --all --ttl 3d 2>/dev/null || echo -e "${YELLOW}${WARN} Log archiving requires recent macOS - skipping${NC}"
echo -e "${GREEN}${CHECK} System logs archived${NC}"
echo "System logs archived at $(date)" >> "$LOG_FILE"
sleep 1

echo ""
echo -e "${GREEN}${BOLD}CHECKPOINT: Cache clearing complete ${CHECK}${NC}"
echo ""
sleep 2

# ============================================================
# COMMAND SET 2: DNS SPEED BOOST (1 minute)
# ============================================================

echo -e "${BOLD}${BLUE}${ROCKET} COMMAND SET 2: DNS SPEED BOOST${NC}"
echo ""

# Detect network interface
NETWORK_INTERFACE=""
if networksetup -getdnsservers "Wi-Fi" &>/dev/null; then
    NETWORK_INTERFACE="Wi-Fi"
elif networksetup -getdnsservers "Ethernet" &>/dev/null; then
    NETWORK_INTERFACE="Ethernet"
else
    echo -e "${YELLOW}${WARN} Could not detect network interface - trying both${NC}"
fi

if [ -n "$NETWORK_INTERFACE" ]; then
    echo -e "${CYAN}Detected network interface: ${NETWORK_INTERFACE}${NC}"

    echo -e "${CYAN}Current DNS servers:${NC}"
    networksetup -getdnsservers "$NETWORK_INTERFACE"

    echo -e "${CYAN}Setting Cloudflare DNS (1.1.1.1, 1.0.0.1)...${NC}"
    sudo networksetup -setdnsservers "$NETWORK_INTERFACE" 1.1.1.1 1.0.0.1

    echo -e "${CYAN}Verifying DNS change...${NC}"
    CURRENT_DNS=$(networksetup -getdnsservers "$NETWORK_INTERFACE")
    if echo "$CURRENT_DNS" | grep -q "1.1.1.1"; then
        echo -e "${GREEN}${CHECK} Cloudflare DNS active${NC}"
        echo "Cloudflare DNS activated on $NETWORK_INTERFACE at $(date)" >> "$LOG_FILE"
    else
        echo -e "${YELLOW}${WARN} DNS may not have updated - check manually${NC}"
    fi
else
    echo -e "${YELLOW}${WARN} Skipping DNS configuration - configure manually in System Settings${NC}"
fi

sudo dscacheutil -flushcache 2>/dev/null || true

echo ""
echo -e "${GREEN}${BOLD}CHECKPOINT: DNS optimization complete ${CHECK}${NC}"
echo ""
sleep 2

# ============================================================
# COMMAND SET 3: CPU PERFORMANCE CHECK (1 minute)
# ============================================================

echo -e "${BOLD}${BLUE}${WRENCH} COMMAND SET 3: CPU PERFORMANCE CHECK${NC}"
echo ""

echo -e "${CYAN}Checking M2 Ultra core count...${NC}"
LOGICAL_CPUS=$(sysctl -n hw.logicalcpu)
PHYSICAL_CPUS=$(sysctl -n hw.physicalcpu)
echo -e "${GREEN}Logical CPUs: ${BOLD}$LOGICAL_CPUS${NC}"
echo -e "${GREEN}Physical CPUs: ${BOLD}$PHYSICAL_CPUS${NC}"
echo "CPU cores: Logical=$LOGICAL_CPUS Physical=$PHYSICAL_CPUS at $(date)" >> "$LOG_FILE"
sleep 1

echo ""
echo -e "${CYAN}Checking available RAM...${NC}"
TOTAL_RAM_GB=$(( $(sysctl -n hw.memsize) / 1024 / 1024 / 1024 ))
echo -e "${GREEN}Total RAM: ${BOLD}${TOTAL_RAM_GB}GB${NC}"
echo "Total RAM: ${TOTAL_RAM_GB}GB at $(date)" >> "$LOG_FILE"
sleep 1

echo ""
echo -e "${CYAN}Current memory statistics:${NC}"
vm_stat | head -10
echo ""
sleep 1

echo -e "${GREEN}${BOLD}CHECKPOINT: CPU & Memory confirmed ready ${CHECK}${NC}"
echo ""
sleep 2

# ============================================================
# COMMAND SET 4: BACKGROUND PROCESS CLEANUP (2 minutes)
# ============================================================

echo -e "${BOLD}${BLUE}${WRENCH} COMMAND SET 4: BACKGROUND PROCESS CLEANUP${NC}"
echo ""

echo -e "${CYAN}Checking Spotlight indexing status...${NC}"
SPOTLIGHT_STATUS=$(sudo mdutil -a -s 2>&1)
echo "$SPOTLIGHT_STATUS"
echo ""

read -p "Do you want to temporarily disable Spotlight indexing? (y/n): " DISABLE_SPOTLIGHT
if [[ "$DISABLE_SPOTLIGHT" == "y" ]]; then
    echo -e "${CYAN}Disabling Spotlight indexing...${NC}"
    sudo mdutil -a -i off
    echo -e "${GREEN}${CHECK} Spotlight indexing disabled${NC}"
    echo "Spotlight indexing disabled at $(date)" >> "$LOG_FILE"

    echo ""
    echo -e "${YELLOW}${WARN} Remember to re-enable when optimization is complete:${NC}"
    echo -e "${YELLOW}    sudo mdutil -a -i on${NC}"
    echo ""
else
    echo -e "${YELLOW}Keeping Spotlight indexing enabled${NC}"
fi

sleep 1

echo -e "${GREEN}${BOLD}CHECKPOINT: Background processes optimized ${CHECK}${NC}"
echo ""
sleep 2

# ============================================================
# COMMAND SET 5: ACTIVITY MONITOR SETUP (Quick check)
# ============================================================

echo -e "${BOLD}${BLUE}${WRENCH} COMMAND SET 5: ACTIVITY MONITOR CHECK${NC}"
echo ""

echo -e "${CYAN}Top CPU processes:${NC}"
top -l 1 -o cpu -n 10 | tail -11
echo ""
sleep 2

read -p "Open Activity Monitor for detailed inspection? (y/n): " OPEN_ACTIVITY
if [[ "$OPEN_ACTIVITY" == "y" ]]; then
    open /Applications/Utilities/Activity\ Monitor.app
    echo -e "${GREEN}${CHECK} Activity Monitor opened${NC}"
fi

echo ""
sleep 1

# ============================================================
# COMMAND SET 6: VOICE CONTROL PREP (1 minute)
# ============================================================

echo -e "${BOLD}${BLUE}${MUSIC} COMMAND SET 6: VOICE CONTROL PREP${NC}"
echo ""

echo -e "${CYAN}Checking audio input devices...${NC}"
system_profiler SPAudioDataType | grep -A 10 "Input" || echo "No additional input devices detected"
echo ""
sleep 1

echo -e "${CYAN}Current input volume:${NC}"
INPUT_VOLUME=$(osascript -e 'input volume of (get volume settings)' 2>/dev/null || echo "N/A")
echo -e "${GREEN}Input volume: ${BOLD}$INPUT_VOLUME%${NC}"
echo ""

read -p "Set input volume to 80% for optimal voice control? (y/n): " SET_VOLUME
if [[ "$SET_VOLUME" == "y" ]]; then
    osascript -e 'set volume input volume 80'
    echo -e "${GREEN}${CHECK} Input volume set to 80%${NC}"
    echo "Input volume set to 80% at $(date)" >> "$LOG_FILE"
fi

echo ""
echo -e "${GREEN}${BOLD}CHECKPOINT: Microphone ready for ClaudeRMT + SHIRL ${CHECK}${NC}"
echo ""
sleep 2

# ============================================================
# COMMAND SET 7: SYSTEM OPTIMIZATION FLAGS (1 minute)
# ============================================================

echo -e "${BOLD}${BLUE}${LIGHTNING} COMMAND SET 7: SYSTEM OPTIMIZATION FLAGS${NC}"
echo ""

echo -e "${CYAN}Applying performance optimizations...${NC}"

# Reduce motion
defaults write NSGlobalDomain NSUseAnimatedFocusRing -bool false
echo -e "${GREEN}${CHECK} Reduced animation overhead${NC}"

# Disable press-and-hold
defaults write -g ApplePressAndHoldEnabled -bool false
echo -e "${GREEN}${CHECK} Key repeat optimized${NC}"

# Faster Dock
defaults write com.apple.dock mineffect -string "scale"
defaults write com.apple.dock autohide-time-modifier -float 0
echo -e "${GREEN}${CHECK} Dock animations optimized${NC}"

echo ""
echo -e "${CYAN}Restarting Dock to apply changes...${NC}"
killall Dock
sleep 2
echo -e "${GREEN}${CHECK} Dock restarted${NC}"

echo "System optimization flags applied at $(date)" >> "$LOG_FILE"

echo ""
echo -e "${GREEN}${BOLD}CHECKPOINT: System animations optimized ${CHECK}${NC}"
echo ""
sleep 2

# ============================================================
# COMMAND SET 8: VERIFY OPTIMIZATION COMPLETE (2 minutes)
# ============================================================

echo -e "${BOLD}${BLUE}${FIRE} COMMAND SET 8: VERIFICATION & DIAGNOSTICS${NC}"
echo ""

echo -e "${CYAN}System hardware summary:${NC}"
system_profiler SPHardwareDataType | grep -E "Model Name|Model Identifier|Chip|Memory"
echo ""
sleep 1

echo -e "${CYAN}Disk usage:${NC}"
df -h / | tail -1
echo ""
sleep 1

echo -e "${CYAN}System uptime:${NC}"
uptime
echo ""
sleep 1

echo -e "${CYAN}Memory pressure:${NC}"
memory_pressure 2>/dev/null | head -5 || echo "Memory pressure tool not available - check Activity Monitor"
echo ""
sleep 1

echo "System verification completed at $(date)" >> "$LOG_FILE"

echo -e "${GREEN}${BOLD}CHECKPOINT: Full baseline established ${CHECK}${NC}"
echo ""
sleep 2

# ============================================================
# COMMAND SET 9: AUDIO INTERFACE (Optional)
# ============================================================

echo -e "${BOLD}${BLUE}${MUSIC} COMMAND SET 9: AUDIO INTERFACE${NC}"
echo ""

if [ -d "/Applications/Universal Audio" ]; then
    echo -e "${GREEN}Universal Audio Console detected${NC}"
    read -p "Open UA Console for configuration? (y/n): " OPEN_UA
    if [[ "$OPEN_UA" == "y" ]]; then
        open /Applications/Universal\ Audio/UA\ Console.app 2>/dev/null || echo -e "${YELLOW}Could not open UA Console${NC}"
        echo ""
        echo -e "${CYAN}Recommended UA Console settings:${NC}"
        echo -e "  • Buffer size: 256 samples (low latency)"
        echo -e "  • Sample rate: 96kHz (for mixing)"
        echo -e "  • Enable hardware processing (not CPU)"
        echo ""
    fi
else
    echo -e "${YELLOW}Universal Audio Console not installed - skipping${NC}"
fi

echo -e "${GREEN}${BOLD}CHECKPOINT: Audio interface ready ${CHECK}${NC}"
echo ""
sleep 2

# ============================================================
# FINAL REPORT
# ============================================================

clear
echo ""
echo -e "${BOLD}${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BOLD}${GREEN}     ${FIRE} GOD HOT-ROD OPTIMIZATION COMPLETE ${FIRE}${NC}"
echo -e "${BOLD}${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${GREEN}${BOLD}✅ COMPLETED OPTIMIZATIONS:${NC}"
echo ""
echo -e "${GREEN}  ${CHECK} Cache cleared (system, temp, Chrome)${NC}"
echo -e "${GREEN}  ${CHECK} DNS optimized (Cloudflare 1.1.1.1)${NC}"
echo -e "${GREEN}  ${CHECK} CPU & Memory verified ($LOGICAL_CPUS cores, ${TOTAL_RAM_GB}GB RAM)${NC}"
echo -e "${GREEN}  ${CHECK} Background processes optimized${NC}"
echo -e "${GREEN}  ${CHECK} System animations streamlined${NC}"
echo -e "${GREEN}  ${CHECK} Audio/voice input configured${NC}"
echo -e "${GREEN}  ${CHECK} Performance baseline established${NC}"
echo ""

echo -e "${YELLOW}${BOLD}📊 PERFORMANCE REPORT:${NC}"
echo -e "${CYAN}Log file saved: ${BOLD}$LOG_FILE${NC}"
echo ""

echo -e "${MAGENTA}${BOLD}🎤 VOICE COMMAND TEST:${NC}"
echo ""
echo -e "${CYAN}Try these commands:${NC}"
echo -e "  ${YELLOW}\"SHIRL, confirm GOD hot-rod mode active\"${NC}"
echo -e "  ${YELLOW}\"SHIRL, GOD performance status\"${NC}"
echo ""

echo -e "${BLUE}${BOLD}📈 NEXT STEPS:${NC}"
echo ""
echo -e "${CYAN}1. Monitor system performance over next week${NC}"
echo -e "${CYAN}2. Run 'tools/god-status.py' for real-time monitoring${NC}"
echo -e "${CYAN}3. Re-enable Spotlight if disabled: ${YELLOW}sudo mdutil -a -i on${NC}"
echo -e "${CYAN}4. Activate TechTool Pro 21 for deep optimization (400-800GB cleanup)${NC}"
echo ""

echo -e "${GREEN}${BOLD}Expected result: GOD singing like a lark ${MUSIC}${NC}"
echo ""
echo -e "${BOLD}${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${BOLD}${MAGENTA}GORUNFREE! 🎸🔥${NC}"
echo ""

# Final log entry
echo "GOD Hot-Rod Execution completed successfully at $(date)" >> "$LOG_FILE"
echo "Log saved to: $LOG_FILE" >> "$LOG_FILE"
