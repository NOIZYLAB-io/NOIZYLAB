#!/bin/bash
# ADVANCED HOTKEY SETUP
# Power user shortcuts for Phase 2 features
# GORUNFREE - Next Level

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${PURPLE}╔═══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║                                                               ║${NC}"
echo -e "${PURPLE}║          🔥 ADVANCED HOTKEY SETUP 🔥                          ║${NC}"
echo -e "${PURPLE}║                                                               ║${NC}"
echo -e "${PURPLE}║              Phase 2 Power User Features                      ║${NC}"
echo -e "${PURPLE}║                                                               ║${NC}"
echo -e "${PURPLE}╚═══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Detect platform
PLATFORM=$(uname -s)

echo -e "${CYAN}Detected platform: $PLATFORM${NC}"
echo ""

# Create advanced scripts directory
mkdir -p ~/ai-genius-pro
cd ~/ai-genius-pro

echo -e "${BLUE}[1/5] Creating Multi-Model Query Script${NC}"
cat > ~/ai-genius-pro/ask-multiple << 'EOFMULTI'
#!/bin/bash
# Query multiple AI models at once
cd ~/ai-genius-pro
python3 multi-model-query.py "$@"
EOFMULTI
chmod +x ~/ai-genius-pro/ask-multiple
echo -e "${GREEN}✓ Multi-model script created${NC}\n"

echo -e "${BLUE}[2/5] Creating Screenshot Analyzer${NC}"
cat > ~/ai-genius-pro/analyze-screenshot << 'EOFSCREEN'
#!/bin/bash
# Analyze screenshot with AI vision
cd ~/ai-genius-pro
bash screenshot-analyzer.sh
EOFSCREEN
chmod +x ~/ai-genius-pro/analyze-screenshot
echo -e "${GREEN}✓ Screenshot analyzer created${NC}\n"

echo -e "${BLUE}[3/5] Creating Context-Aware Scripts${NC}"

# Explain anything
cat > ~/ai-genius-pro/explain << 'EOFEXPLAIN'
#!/bin/bash
# AI explains selected text
SELECTED=$(osascript -e 'tell application "System Events" to get the clipboard' 2>/dev/null || xclip -o -selection clipboard 2>/dev/null)
cd ~/ai-genius
python3 universal-ai-selector.py claude-sonnet-4 <<< "Explain this in simple terms: $SELECTED"
EOFEXPLAIN
chmod +x ~/ai-genius-pro/explain

# Fix anything
cat > ~/ai-genius-pro/fix << 'EOFFIX'
#!/bin/bash
# AI fixes errors, grammar, or bugs
SELECTED=$(osascript -e 'tell application "System Events" to get the clipboard' 2>/dev/null || xclip -o -selection clipboard 2>/dev/null)
cd ~/ai-genius
python3 universal-ai-selector.py claude-sonnet-4 <<< "Fix any errors in this: $SELECTED"
EOFFIX
chmod +x ~/ai-genius-pro/fix

# Improve anything
cat > ~/ai-genius-pro/improve << 'EOFIMPROVE'
#!/bin/bash
# AI improves writing, code, or design
SELECTED=$(osascript -e 'tell application "System Events" to get the clipboard' 2>/dev/null || xclip -o -selection clipboard 2>/dev/null)
cd ~/ai-genius
python3 universal-ai-selector.py claude-sonnet-4 <<< "Improve this: $SELECTED"
EOFIMPROVE
chmod +x ~/ai-genius-pro/improve

# Translate anything
cat > ~/ai-genius-pro/translate << 'EOFTRANS'
#!/bin/bash
# AI translates to any language
SELECTED=$(osascript -e 'tell application "System Events" to get the clipboard' 2>/dev/null || xclip -o -selection clipboard 2>/dev/null)
echo "Translate to which language?"
read LANG
cd ~/ai-genius
python3 universal-ai-selector.py claude-sonnet-4 <<< "Translate this to $LANG: $SELECTED"
EOFTRANS
chmod +x ~/ai-genius-pro/translate

echo -e "${GREEN}✓ Context-aware scripts created${NC}\n"

echo -e "${BLUE}[4/5] Creating Quick Action Scripts${NC}"

# Summarize
cat > ~/ai-genius-pro/summarize << 'EOFSUM'
#!/bin/bash
SELECTED=$(osascript -e 'tell application "System Events" to get the clipboard' 2>/dev/null || xclip -o -selection clipboard 2>/dev/null)
cd ~/ai-genius
python3 universal-ai-selector.py gemini-2-flash <<< "Summarize this in 3 bullet points: $SELECTED"
EOFSUM
chmod +x ~/ai-genius-pro/summarize

# Ask quick
cat > ~/ai-genius-pro/ask-quick << 'EOFQUICK'
#!/bin/bash
osascript -e 'display dialog "Quick AI question:" default answer ""' | sed 's/.*text returned://;s/,.*//' | xargs -I {} bash -c "cd ~/ai-genius && python3 universal-ai-selector.py gemini-2-flash <<< '{}'"
EOFQUICK
chmod +x ~/ai-genius-pro/ask-quick

echo -e "${GREEN}✓ Quick action scripts created${NC}\n"

echo -e "${BLUE}[5/5] Platform-Specific Setup${NC}"

case "$PLATFORM" in
    Darwin)
        echo -e "${CYAN}Setting up Mac hotkeys...${NC}\n"
        
        echo -e "${YELLOW}Recommended Keyboard Shortcuts:${NC}"
        echo ""
        echo "System Settings → Keyboard → Keyboard Shortcuts → App Shortcuts"
        echo ""
        echo "Add these shortcuts:"
        echo "  ⌘⌥M  →  ~/ai-genius-pro/ask-multiple"
        echo "  ⌘⌥S  →  ~/ai-genius-pro/analyze-screenshot"
        echo "  ⌘⌥E  →  ~/ai-genius-pro/explain"
        echo "  ⌘⌥F  →  ~/ai-genius-pro/fix"
        echo "  ⌘⌥I  →  ~/ai-genius-pro/improve"
        echo "  ⌘⌥T  →  ~/ai-genius-pro/translate"
        echo "  ⌘⌥Q  →  ~/ai-genius-pro/ask-quick"
        echo "  ⌘⌥U  →  ~/ai-genius-pro/summarize"
        echo ""
        ;;
    
    Linux)
        echo -e "${CYAN}Setting up Linux hotkeys...${NC}\n"
        
        echo -e "${YELLOW}Recommended Keyboard Shortcuts:${NC}"
        echo ""
        echo "Settings → Keyboard → Custom Shortcuts"
        echo ""
        echo "Add these shortcuts:"
        echo "  Ctrl+Alt+M  →  ~/ai-genius-pro/ask-multiple"
        echo "  Ctrl+Alt+S  →  ~/ai-genius-pro/analyze-screenshot"
        echo "  Ctrl+Alt+E  →  ~/ai-genius-pro/explain"
        echo "  Ctrl+Alt+F  →  ~/ai-genius-pro/fix"
        echo "  Ctrl+Alt+I  →  ~/ai-genius-pro/improve"
        echo "  Ctrl+Alt+T  →  ~/ai-genius-pro/translate"
        echo ""
        ;;
esac

echo -e "${GREEN}✓ Setup instructions displayed${NC}\n"

# Copy multi-model script if it exists
if [ -f "../multi-model-query.py" ]; then
    cp ../multi-model-query.py ~/ai-genius-pro/
    echo -e "${GREEN}✓ Multi-model query script copied${NC}"
fi

if [ -f "../screenshot-analyzer.sh" ]; then
    cp ../screenshot-analyzer.sh ~/ai-genius-pro/
    echo -e "${GREEN}✓ Screenshot analyzer copied${NC}"
fi

# Copy base scripts
if [ -f "../universal-ai-selector.py" ]; then
    cp ../universal-ai-selector.py ~/ai-genius-pro/
    echo -e "${GREEN}✓ Base AI selector copied${NC}"
fi

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${bold}✅ ADVANCED HOTKEYS READY${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${CYAN}📍 Scripts installed to:${NC}"
echo "   ~/ai-genius-pro/"
echo ""

echo -e "${CYAN}🎯 Available Commands:${NC}"
echo "   ask-multiple      - Query multiple AIs at once"
echo "   analyze-screenshot - Capture & analyze with AI vision"
echo "   explain           - Explain selected text"
echo "   fix               - Fix errors/bugs"
echo "   improve           - Improve writing/code"
echo "   translate         - Translate to any language"
echo "   ask-quick         - Quick AI question dialog"
echo "   summarize         - Summarize in 3 bullets"
echo ""

echo -e "${CYAN}💡 Usage Examples:${NC}"
echo "   ~/ai-genius-pro/ask-multiple \"What is quantum computing?\""
echo "   ~/ai-genius-pro/analyze-screenshot"
echo "   # Select text, then run:"
echo "   ~/ai-genius-pro/explain"
echo ""

echo -e "${YELLOW}⚡ Next: Set up keyboard shortcuts in System Settings${NC}"
echo ""

echo -e "${GREEN}${BOLD}🔥 PHASE 2 POWER USER MODE ACTIVATED 🔥${NC}"
echo ""
