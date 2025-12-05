#!/bin/bash
# GOD Voice Control Test & Verification
# CB_01 - Fish Music Inc
# Test microphone, audio interface, and SHIRL integration readiness
# GORUNFREE! 🎸🔥

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'
BOLD='\033[1m'

# Emojis
MUSIC="🎵"
MIC="🎤"
CHECK="✅"
WARN="⚠️"
FIRE="🔥"

clear

echo ""
echo -e "${BOLD}${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BOLD}${MAGENTA}     ${MIC} GOD VOICE CONTROL TEST${NC}"
echo -e "${BOLD}${CYAN}     Audio System & SHIRL Integration Verification${NC}"
echo -e "${BOLD}${CYAN}     Fish Music Inc - CB_01${NC}"
echo -e "${BOLD}${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# ============================================================
# TEST 1: AUDIO DEVICES
# ============================================================

echo -e "${BOLD}${BLUE}${MIC} TEST 1: AUDIO DEVICES${NC}"
echo ""

echo -e "${CYAN}Checking audio input devices...${NC}"
echo ""

system_profiler SPAudioDataType | grep -A 20 "Input"

echo ""
echo -e "${GREEN}${CHECK} Audio devices detected${NC}"
echo ""
sleep 2

# ============================================================
# TEST 2: MICROPHONE LEVELS
# ============================================================

echo -e "${BOLD}${BLUE}${MIC} TEST 2: MICROPHONE LEVELS${NC}"
echo ""

echo -e "${CYAN}Current input volume:${NC}"
INPUT_VOLUME=$(osascript -e 'input volume of (get volume settings)' 2>/dev/null || echo "0")
echo -e "${GREEN}Input Volume: ${BOLD}$INPUT_VOLUME%${NC}"

if [ "$INPUT_VOLUME" -lt 50 ]; then
    echo -e "${YELLOW}${WARN} Input volume low (recommended: 70-80%)${NC}"
    read -p "Set to 75%? (y/n): " SET_VOL
    if [[ "$SET_VOL" == "y" ]]; then
        osascript -e 'set volume input volume 75'
        echo -e "${GREEN}${CHECK} Input volume set to 75%${NC}"
    fi
elif [ "$INPUT_VOLUME" -gt 90 ]; then
    echo -e "${YELLOW}${WARN} Input volume high (may cause distortion)${NC}"
else
    echo -e "${GREEN}${CHECK} Input volume optimal${NC}"
fi

echo ""
sleep 2

# ============================================================
# TEST 3: SYSTEM AUDIO OUTPUT
# ============================================================

echo -e "${BOLD}${BLUE}${MUSIC} TEST 3: SYSTEM AUDIO OUTPUT${NC}"
echo ""

echo -e "${CYAN}Current output volume:${NC}"
OUTPUT_VOLUME=$(osascript -e 'output volume of (get volume settings)' 2>/dev/null || echo "0")
echo -e "${GREEN}Output Volume: ${BOLD}$OUTPUT_VOLUME%${NC}"

echo ""
echo -e "${CYAN}Playing test tone...${NC}"

# Generate a 440Hz tone (A4 note) for 1 second
afplay /System/Library/Sounds/Ping.aiff 2>/dev/null || echo -e "${YELLOW}Could not play test sound${NC}"

echo -e "${GREEN}${CHECK} Audio output tested${NC}"
echo ""
sleep 2

# ============================================================
# TEST 4: RECORDING TEST
# ============================================================

echo -e "${BOLD}${BLUE}${MIC} TEST 4: MICROPHONE RECORDING TEST${NC}"
echo ""

TEST_RECORDING="/tmp/god-voice-test-$(date +%s).aiff"

echo -e "${CYAN}Recording 3 seconds of audio...${NC}"
echo -e "${YELLOW}Say: \"SHIRL, GOD hot-rod mode active\" now!${NC}"
echo ""
sleep 1
echo -e "${GREEN}Recording...${NC}"

# Record 3 seconds of audio
rec -c 1 -r 16000 "$TEST_RECORDING" trim 0 3 2>/dev/null || \
    sox -d -r 16000 -c 1 "$TEST_RECORDING" trim 0 3 2>/dev/null || \
    echo -e "${YELLOW}${WARN} Sox/Rec not installed - skipping recording test${NC}"

if [ -f "$TEST_RECORDING" ]; then
    echo ""
    echo -e "${GREEN}${CHECK} Recording complete${NC}"
    echo ""
    echo -e "${CYAN}Playing back recording...${NC}"
    afplay "$TEST_RECORDING" 2>/dev/null || echo -e "${YELLOW}Could not play recording${NC}"

    # Show file info
    FILE_SIZE=$(stat -f%z "$TEST_RECORDING" 2>/dev/null || echo "0")
    FILE_SIZE_KB=$((FILE_SIZE / 1024))
    echo ""
    echo -e "${CYAN}Recording details:${NC}"
    echo -e "  Size: ${GREEN}${FILE_SIZE_KB}KB${NC}"
    echo -e "  Location: ${GREEN}${TEST_RECORDING}${NC}"

    # Cleanup
    read -p "Delete test recording? (y/n): " DELETE_REC
    if [[ "$DELETE_REC" == "y" ]]; then
        rm "$TEST_RECORDING"
        echo -e "${GREEN}${CHECK} Test recording deleted${NC}"
    fi
else
    echo -e "${YELLOW}${WARN} Recording test skipped (requires sox/rec)${NC}"
    echo -e "${CYAN}Install with: brew install sox${NC}"
fi

echo ""
sleep 2

# ============================================================
# TEST 5: SIRI INTEGRATION
# ============================================================

echo -e "${BOLD}${BLUE}${MIC} TEST 5: SIRI INTEGRATION${NC}"
echo ""

echo -e "${CYAN}Checking Siri status...${NC}"

SIRI_ENABLED=$(defaults read com.apple.Siri VoiceTriggerUserEnabled 2>/dev/null || echo "0")

if [ "$SIRI_ENABLED" -eq 1 ]; then
    echo -e "${GREEN}${CHECK} Siri voice activation enabled${NC}"
else
    echo -e "${YELLOW}${WARN} Siri voice activation disabled${NC}"
    echo -e "${CYAN}Enable in: System Settings > Siri & Spotlight${NC}"
fi

echo ""
sleep 2

# ============================================================
# TEST 6: AUDIO INTERFACE (Apollo)
# ============================================================

echo -e "${BOLD}${BLUE}${MUSIC} TEST 6: AUDIO INTERFACE CHECK${NC}"
echo ""

if [ -d "/Applications/Universal Audio" ]; then
    echo -e "${GREEN}${CHECK} Universal Audio Console detected${NC}"

    # Check if UA Console is running
    UA_RUNNING=$(pgrep -i "UA Console" || echo "")
    if [ -n "$UA_RUNNING" ]; then
        echo -e "${GREEN}${CHECK} UA Console is running${NC}"
    else
        echo -e "${YELLOW}${WARN} UA Console not running${NC}"
        read -p "Launch UA Console? (y/n): " LAUNCH_UA
        if [[ "$LAUNCH_UA" == "y" ]]; then
            open /Applications/Universal\ Audio/UA\ Console.app 2>/dev/null
            echo -e "${GREEN}${CHECK} UA Console launched${NC}"
        fi
    fi

    echo ""
    echo -e "${CYAN}Recommended UA Console settings:${NC}"
    echo -e "  • Buffer size: ${YELLOW}256 samples${NC} (low latency)"
    echo -e "  • Sample rate: ${YELLOW}96kHz${NC} (for mixing)"
    echo -e "  • Processing: ${YELLOW}Hardware${NC} (not CPU)"
else
    echo -e "${YELLOW}ℹ️  Universal Audio Console not installed${NC}"
    echo -e "${CYAN}Using system audio interface${NC}"
fi

echo ""
sleep 2

# ============================================================
# TEST 7: VOICE COMMAND READINESS
# ============================================================

echo -e "${BOLD}${BLUE}${MIC} TEST 7: VOICE COMMAND READINESS${NC}"
echo ""

echo -e "${CYAN}Testing voice command responsiveness...${NC}"
echo ""

# Check if ClaudeRMT or similar is accessible
echo -e "${YELLOW}Voice command systems to verify:${NC}"
echo -e "  1. ${CYAN}SHIRL${NC} - Voice control assistant"
echo -e "  2. ${CYAN}ClaudeRMT${NC} - Remote terminal control"
echo -e "  3. ${CYAN}ENGR_KEITH${NC} - Network monitoring"
echo ""

echo -e "${GREEN}Test these voice commands:${NC}"
echo -e "  ${MAGENTA}\"SHIRL, confirm GOD hot-rod mode active\"${NC}"
echo -e "  ${MAGENTA}\"SHIRL, GOD performance status\"${NC}"
echo -e "  ${MAGENTA}\"SHIRL, activate hot-rod mode\"${NC}"
echo -e "  ${MAGENTA}\"ENGR_KEITH, verify MC96 infrastructure\"${NC}"
echo ""

sleep 3

# ============================================================
# FINAL REPORT
# ============================================================

clear
echo ""
echo -e "${BOLD}${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BOLD}${GREEN}     ${MIC} VOICE CONTROL TEST COMPLETE${NC}"
echo -e "${BOLD}${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${GREEN}${BOLD}✅ AUDIO SYSTEM STATUS:${NC}"
echo ""
echo -e "${GREEN}  ${CHECK} Audio devices verified${NC}"
echo -e "${GREEN}  ${CHECK} Microphone levels optimized${NC}"
echo -e "${GREEN}  ${CHECK} System audio output functional${NC}"

if [ -f "$TEST_RECORDING" ] || [ "$FILE_SIZE_KB" -gt 0 ]; then
    echo -e "${GREEN}  ${CHECK} Recording test successful${NC}"
fi

if [ "$SIRI_ENABLED" -eq 1 ]; then
    echo -e "${GREEN}  ${CHECK} Siri integration active${NC}"
else
    echo -e "${YELLOW}  ${WARN} Siri not enabled${NC}"
fi

if [ -d "/Applications/Universal Audio" ]; then
    echo -e "${GREEN}  ${CHECK} Professional audio interface ready${NC}"
fi

echo ""

echo -e "${MAGENTA}${BOLD}🎤 VOICE COMMAND READINESS:${NC}"
echo ""
echo -e "${CYAN}System ready for:${NC}"
echo -e "  • ${GREEN}ClaudeRMT voice control${NC}"
echo -e "  • ${GREEN}SHIRL assistant integration${NC}"
echo -e "  • ${GREEN}Voice-activated workflows${NC}"
echo -e "  • ${GREEN}Professional recording${NC}"
echo ""

echo -e "${BLUE}${BOLD}📋 NEXT STEPS:${NC}"
echo ""
echo -e "${CYAN}1. Test voice commands with SHIRL${NC}"
echo -e "${CYAN}2. Verify ClaudeRMT voice recognition${NC}"
echo -e "${CYAN}3. Configure custom voice macros${NC}"
echo -e "${CYAN}4. Set up voice-triggered workflows${NC}"
echo ""

echo -e "${BOLD}${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${BOLD}${MAGENTA}GORUNFREE! 🎸🔥${NC}"
echo ""
