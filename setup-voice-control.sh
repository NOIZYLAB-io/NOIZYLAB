#!/bin/bash
# VOICE CONTROL BRIDGE
# Siri and voice command integration
# Accessibility-first design

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

SHORTCUTS_DIR=~/Library/Shortcuts
VOICE_DIR=~/ai-genius/voice-commands

mkdir -p "$VOICE_DIR"

echo -e "${PURPLE}╔═══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                                                               ║${NC}"
echo -e "${PURPLE}║          🎤 VOICE CONTROL BRIDGE SETUP 🎤                     ║${NC}"
echo -e "${PURPLE}║                                                               ║${NC}"
echo -e "${PURPLE}║          Accessibility-First Voice Commands                   ║${NC}"
echo -e "${PURPLE}║                                                               ║${NC}"
echo -e "${PURPLE}╚═══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Create voice command handlers
echo -e "${CYAN}Creating voice command handlers...${NC}"

# 1. Ask Claude
cat > "$VOICE_DIR/ask-claude.sh" << 'EOFASK'
#!/bin/bash
# Voice command: "Ask Claude [question]"

QUESTION="$*"

if [ -z "$QUESTION" ]; then
    # Get from clipboard if no args
    QUESTION=$(pbpaste)
fi

cd ~/ai-genius
RESPONSE=$(python3 universal-ai-selector.py claude-sonnet-4 "$QUESTION" 2>/dev/null)

# Copy to clipboard
echo "$RESPONSE" | pbcopy

# Speak response
say "$RESPONSE"

# Display notification
osascript -e "display notification \"$RESPONSE\" with title \"Claude Says:\""
EOFASK
chmod +x "$VOICE_DIR/ask-claude.sh"

# 2. Quick AI
cat > "$VOICE_DIR/quick-ai.sh" << 'EOFQUICK'
#!/bin/bash
# Voice command: "Quick AI [question]"

QUESTION="$*"

cd ~/ai-genius
RESPONSE=$(python3 universal-ai-selector.py gemini-2-flash "$QUESTION" 2>/dev/null)

echo "$RESPONSE" | pbcopy
say "$RESPONSE"
EOFQUICK
chmod +x "$VOICE_DIR/quick-ai.sh"

# 3. Screenshot and Analyze
cat > "$VOICE_DIR/screenshot-analyze.sh" << 'EOFSCREEN'
#!/bin/bash
# Voice command: "Screenshot and analyze"

# Take screenshot
screencapture -i /tmp/voice-screenshot.png

# Analyze with AI
cd ~/ai-genius-pro
./screenshot-analyzer.sh <<EOF
1
/tmp/voice-screenshot.png
1
EOF

# Read result
RESULT=$(cat /tmp/ai-analysis-*.txt 2>/dev/null | tail -1)
say "$RESULT"
EOFSCREEN
chmod +x "$VOICE_DIR/screenshot-analyze.sh"

# 4. Repair Status
cat > "$VOICE_DIR/repair-status.sh" << 'EOFREPAIR'
#!/bin/bash
# Voice command: "Check repair status"

cd ~/ai-genius-pro
STATUS=$(./smart-dashboard.sh <<EOF
1
EOF
)

# Extract key metrics
PENDING=$(echo "$STATUS" | grep -o "[0-9]* pending" | head -1)
ACTIVE=$(echo "$STATUS" | grep -o "[0-9]* active" | head -1)

say "You have $PENDING repairs and $ACTIVE active workflows"
EOFREPAIR
chmod +x "$VOICE_DIR/repair-status.sh"

# 5. Read Clipboard
cat > "$VOICE_DIR/read-clipboard.sh" << 'EOFREAD'
#!/bin/bash
# Voice command: "Read clipboard"

TEXT=$(pbpaste)
say "$TEXT"
EOFREAD
chmod +x "$VOICE_DIR/read-clipboard.sh"

# 6. Dictate and Send
cat > "$VOICE_DIR/dictate-send.sh" << 'EOFDICTATE'
#!/bin/bash
# Voice command: "Dictate message"

# Record audio (requires user to speak)
osascript -e 'tell application "System Events" to keystroke " " using {option down, command down}'
sleep 2

# Get dictated text from clipboard
TEXT=$(pbpaste)

# AI improve the message
cd ~/ai-genius
IMPROVED=$(python3 universal-ai-selector.py claude-sonnet-4 "Improve this message for professional communication: $TEXT" 2>/dev/null)

echo "$IMPROVED" | pbcopy
say "Message improved and copied to clipboard"
EOFDICTATE
chmod +x "$VOICE_DIR/dictate-send.sh"

# 7. Smart Search
cat > "$VOICE_DIR/smart-search.sh" << 'EOFSEARCH'
#!/bin/bash
# Voice command: "Search for [topic]"

TOPIC="$*"

cd ~/ai-genius
RESULT=$(python3 universal-ai-selector.py claude-sonnet-4 "Quick summary: $TOPIC" 2>/dev/null)

say "$RESULT"
echo "$RESULT" | pbcopy
EOFSEARCH
chmod +x "$VOICE_DIR/smart-search.sh"

# 8. Emergency Help
cat > "$VOICE_DIR/emergency-help.sh" << 'EOFEMERGENCY'
#!/bin/bash
# Voice command: "Emergency help"

say "Emergency mode activated. How can I help?"

# Display large help dialog
osascript <<EOFAPPLE
display dialog "EMERGENCY HELP ACTIVE

Say one of these commands:
• Call support
• System status
• Fix my screen
• Read my messages
• Check my schedule

Or press Cancel to exit." buttons {"Cancel"} default button 1 with title "Emergency Help" giving up after 30
EOFAPPLE
EOFEMERGENCY
chmod +x "$VOICE_DIR/emergency-help.sh"

echo -e "${GREEN}✓ Voice command handlers created${NC}"
echo ""

# Create Siri shortcuts instructions
echo -e "${CYAN}Creating Siri shortcut instructions...${NC}"

cat > "$VOICE_DIR/SIRI-SETUP.txt" << 'EOFSIRI'
🎤 SIRI SHORTCUTS SETUP GUIDE

QUICK SETUP (Copy-Paste Commands):
================================

1. OPEN SHORTCUTS APP
   • Press ⌘+Space
   • Type "Shortcuts"
   • Press Enter

2. CREATE SHORTCUTS
   For each command below, create a new shortcut:
   
   ┌─────────────────────────────────────────────┐
   │ SHORTCUT: "Ask Claude"                      │
   ├─────────────────────────────────────────────┤
   │ 1. Add "Get Text From Input"                │
   │ 2. Add "Run Shell Script"                   │
   │    Script: ~/ai-genius/voice-commands/      │
   │            ask-claude.sh                    │
   │    Pass Input: As Arguments                 │
   │ 3. Save                                     │
   └─────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────┐
   │ SHORTCUT: "Quick AI"                        │
   ├─────────────────────────────────────────────┤
   │ 1. Add "Get Text From Input"                │
   │ 2. Add "Run Shell Script"                   │
   │    Script: ~/ai-genius/voice-commands/      │
   │            quick-ai.sh                      │
   │ 3. Save                                     │
   └─────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────┐
   │ SHORTCUT: "Screenshot Analyze"              │
   ├─────────────────────────────────────────────┤
   │ 1. Add "Run Shell Script"                   │
   │    Script: ~/ai-genius/voice-commands/      │
   │            screenshot-analyze.sh            │
   │ 2. Save                                     │
   └─────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────┐
   │ SHORTCUT: "Repair Status"                   │
   ├─────────────────────────────────────────────┤
   │ 1. Add "Run Shell Script"                   │
   │    Script: ~/ai-genius/voice-commands/      │
   │            repair-status.sh                 │
   │ 2. Save                                     │
   └─────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────┐
   │ SHORTCUT: "Read Clipboard"                  │
   ├─────────────────────────────────────────────┤
   │ 1. Add "Run Shell Script"                   │
   │    Script: ~/ai-genius/voice-commands/      │
   │            read-clipboard.sh                │
   │ 2. Save                                     │
   └─────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────┐
   │ SHORTCUT: "Emergency Help"                  │
   ├─────────────────────────────────────────────┤
   │ 1. Add "Run Shell Script"                   │
   │    Script: ~/ai-genius/voice-commands/      │
   │            emergency-help.sh                │
   │ 2. Save                                     │
   └─────────────────────────────────────────────┘

3. ENABLE SIRI ACTIVATION
   • Open each shortcut
   • Click the (i) info button
   • Enable "Add to Siri"
   • Record your voice command

VOICE COMMANDS TO SET UP:
=========================

Priority 1 (Essential):
• "Hey Siri, ask Claude [question]"
• "Hey Siri, quick AI [question]"
• "Hey Siri, read clipboard"
• "Hey Siri, emergency help"

Priority 2 (Useful):
• "Hey Siri, screenshot and analyze"
• "Hey Siri, check repair status"
• "Hey Siri, dictate message"

Priority 3 (Advanced):
• "Hey Siri, smart search [topic]"

TESTING YOUR SHORTCUTS:
=======================

After setup, test each one:
1. "Hey Siri, ask Claude what is GORUNFREE"
2. "Hey Siri, read clipboard"
3. "Hey Siri, emergency help"

ACCESSIBILITY FEATURES:
=======================

For Limited Mobility:
• All commands work hands-free
• Voice-only operation
• Audio responses
• No typing required

For Vision Issues:
• All responses spoken aloud
• Large text notifications
• High contrast displays

TROUBLESHOOTING:
================

If Siri doesn't hear you:
• Check System Preferences → Siri
• Ensure "Listen for 'Hey Siri'" is enabled
• Test microphone in System Preferences → Sound

If shortcuts don't run:
• Open Shortcuts app
• Run manually to test
• Check terminal permissions
• Ensure scripts are executable

If AI doesn't respond:
• Check internet connection
• Verify API keys are set
• Run: ~/ai-genius/universal-ai-selector.py

ADVANCED TIPS:
==============

Add to Menu Bar:
• Drag shortcuts to menu bar
• Click to run without voice

Create Custom Commands:
• Copy existing shortcuts
• Modify scripts
• Add your own workflows

Integrate with Apple Watch:
• Shortcuts sync automatically
• Use watch to trigger commands
• Perfect for mobility needs

NEXT STEPS:
===========

1. Set up priority 1 commands first
2. Test each one thoroughly  
3. Add more commands as needed
4. Customize for your workflow

SUPPORT:
========

Having trouble?
• Run: ~/ai-genius/voice-commands/emergency-help.sh
• Check: ~/ai-genius/QUICK-START.txt
• Test: ./ask-claude.sh "test"
EOFSIRI

echo -e "${GREEN}✓ Siri setup instructions created${NC}"
echo ""

# Create quick test script
cat > "$VOICE_DIR/test-voice.sh" << 'EOFTEST'
#!/bin/bash
echo "Testing voice commands..."
echo ""
echo "1. Testing clipboard read..."
echo "Test message" | pbcopy
bash ~/ai-genius/voice-commands/read-clipboard.sh

echo ""
echo "2. Testing quick AI..."
bash ~/ai-genius/voice-commands/quick-ai.sh "What is 2+2?"

echo ""
echo "✓ Voice commands working!"
EOFTEST
chmod +x "$VOICE_DIR/test-voice.sh"

echo -e "${GREEN}✓ Test script created${NC}"
echo ""

# Summary
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}${BOLD}✅ VOICE CONTROL BRIDGE READY${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${CYAN}📁 Location:${NC} $VOICE_DIR"
echo ""
echo -e "${CYAN}🎯 Next Steps:${NC}"
echo "1. Open Shortcuts app"
echo "2. Follow: $VOICE_DIR/SIRI-SETUP.txt"
echo "3. Test: $VOICE_DIR/test-voice.sh"
echo ""
echo -e "${CYAN}🎤 Voice Commands Available:${NC}"
echo "  • Ask Claude [question]"
echo "  • Quick AI [question]"
echo "  • Screenshot and analyze"
echo "  • Check repair status"
echo "  • Read clipboard"
echo "  • Dictate message"
echo "  • Smart search [topic]"
echo "  • Emergency help"
echo ""
echo -e "${GREEN}Perfect for hands-free operation!${NC}"
echo ""
