#!/bin/bash
# UNIVERSAL AI GENIUS SETUP
# Sets up global hotkeys that work via Cloudflare Workers
# Works on: Mac, Windows (WSL/Git Bash), Linux
# GORUNFREEX1000 - Cross-platform edition

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${PURPLE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║        🌐  UNIVERSAL AI GENIUS SETUP  🌐                  ║"
echo "║                                                           ║"
echo "║         Cloudflare Workers > Automator                    ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Detect platform
if [[ "$OSTYPE" == "darwin"* ]]; then
    PLATFORM="mac"
    echo -e "${GREEN}✓ Detected: macOS${NC}"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    PLATFORM="linux"
    echo -e "${GREEN}✓ Detected: Linux${NC}"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    PLATFORM="windows"
    echo -e "${GREEN}✓ Detected: Windows${NC}"
else
    PLATFORM="unknown"
    echo -e "${YELLOW}⚠ Unknown platform: $OSTYPE${NC}"
fi

echo ""
echo -e "${BLUE}[1/5] Configuration${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Get worker URL
echo -e "${CYAN}Enter your Cloudflare Worker URL:${NC}"
echo -e "${YELLOW}Example: https://ai-genius-cloud.your-subdomain.workers.dev${NC}"
read -p "URL: " WORKER_URL

if [ -z "$WORKER_URL" ]; then
    echo -e "${YELLOW}⚠ No URL provided. Please deploy first:${NC}"
    echo "  ./deploy-ai-genius-cloud.sh"
    exit 1
fi

# Update Python script with URL
sed -i.bak "s|WORKER_URL = .*|WORKER_URL = \"$WORKER_URL\"|" universal-ai-selector.py
rm universal-ai-selector.py.bak 2>/dev/null || true

echo -e "${GREEN}✓ Configuration saved${NC}"
echo ""

echo -e "${BLUE}[2/5] Installing Dependencies${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}⚠ Python 3 not found${NC}"
    if [ "$PLATFORM" = "mac" ]; then
        echo "Install: brew install python3"
    elif [ "$PLATFORM" = "linux" ]; then
        echo "Install: sudo apt install python3"
    fi
    exit 1
else
    echo -e "${GREEN}✓ Python 3 found${NC}"
fi

# Make script executable
chmod +x universal-ai-selector.py

echo -e "${GREEN}✓ Dependencies ready${NC}"
echo ""

echo -e "${BLUE}[3/5] Setting Up Hotkeys${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ "$PLATFORM" = "mac" ]; then
    echo -e "${CYAN}Creating macOS shortcuts...${NC}"
    
    # Create helper scripts in user bin
    mkdir -p ~/bin
    
    # Create wrapper scripts for each model
    cat > ~/bin/ask-claude << 'EOF'
#!/bin/bash
cd "$(dirname "$0")/../ai-genius"
python3 universal-ai-selector.py claude-sonnet-4
EOF
    
    cat > ~/bin/ask-gemini << 'EOF'
#!/bin/bash
cd "$(dirname "$0")/../ai-genius"
python3 universal-ai-selector.py gemini-2-flash
EOF
    
    cat > ~/bin/ask-gpt << 'EOF'
#!/bin/bash
cd "$(dirname "$0")/../ai-genius"
python3 universal-ai-selector.py gpt-4o
EOF
    
    chmod +x ~/bin/ask-*
    
    # Copy Python script to accessible location
    mkdir -p ~/ai-genius
    cp universal-ai-selector.py ~/ai-genius/
    
    echo -e "${GREEN}✓ Scripts installed to ~/bin/${NC}"
    echo ""
    echo -e "${YELLOW}To complete setup:${NC}"
    echo "1. Open System Settings → Keyboard → Shortcuts"
    echo "2. Click 'App Shortcuts' → '+'"
    echo "3. Add these shortcuts:"
    echo ""
    echo "   Command: ~/bin/ask-claude"
    echo "   Shortcut: ⌘⌥C"
    echo ""
    echo "   Command: ~/bin/ask-gemini"
    echo "   Shortcut: ⌘⌥G"
    echo ""
    echo "   Command: ~/bin/ask-gpt"
    echo "   Shortcut: ⌘⌥T"
    echo ""

elif [ "$PLATFORM" = "linux" ]; then
    echo -e "${CYAN}Creating Linux shortcuts...${NC}"
    
    # Install xdotool if needed
    if ! command -v xdotool &> /dev/null; then
        echo -e "${YELLOW}Installing xdotool...${NC}"
        sudo apt install -y xdotool || true
    fi
    
    # Create desktop entries
    mkdir -p ~/.local/share/applications
    
    cat > ~/.local/share/applications/ask-claude.desktop << EOF
[Desktop Entry]
Name=Ask Claude
Exec=python3 $(pwd)/universal-ai-selector.py claude-sonnet-4
Type=Application
NoDisplay=true
EOF
    
    cat > ~/.local/share/applications/ask-gemini.desktop << EOF
[Desktop Entry]
Name=Ask Gemini
Exec=python3 $(pwd)/universal-ai-selector.py gemini-2-flash
Type=Application
NoDisplay=true
EOF
    
    echo -e "${GREEN}✓ Desktop entries created${NC}"
    echo ""
    echo -e "${YELLOW}To complete setup:${NC}"
    echo "1. Open Settings → Keyboard → Shortcuts"
    echo "2. Add custom shortcuts:"
    echo ""
    echo "   Name: Ask Claude"
    echo "   Command: python3 $(pwd)/universal-ai-selector.py claude-sonnet-4"
    echo "   Shortcut: Ctrl+Alt+C"
    echo ""
    echo "   Name: Ask Gemini"
    echo "   Command: python3 $(pwd)/universal-ai-selector.py gemini-2-flash"
    echo "   Shortcut: Ctrl+Alt+G"
    echo ""

elif [ "$PLATFORM" = "windows" ]; then
    echo -e "${CYAN}Creating Windows shortcuts...${NC}"
    
    # Create batch files
    cat > ask-claude.bat << 'EOF'
@echo off
python universal-ai-selector.py claude-sonnet-4
EOF
    
    cat > ask-gemini.bat << 'EOF'
@echo off
python universal-ai-selector.py gemini-2-flash
EOF
    
    echo -e "${GREEN}✓ Batch files created${NC}"
    echo ""
    echo -e "${YELLOW}To complete setup:${NC}"
    echo "1. Install AutoHotkey: https://www.autohotkey.com/"
    echo "2. Create hotkey script (see WINDOWS-SETUP.md)"
    echo ""
fi

echo ""
echo -e "${BLUE}[4/5] Browser Extension (Optional)${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

echo -e "${CYAN}Creating browser extension...${NC}"

# Create extension directory
mkdir -p ai-genius-extension

# Create manifest
cat > ai-genius-extension/manifest.json << EOF
{
  "manifest_version": 3,
  "name": "AI GENIUS Universal",
  "version": "1.0.0",
  "description": "Access all your AI models via right-click",
  "permissions": ["contextMenus", "clipboardWrite"],
  "host_permissions": ["$WORKER_URL/*"],
  "background": {
    "service_worker": "background.js"
  },
  "icons": {
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  }
}
EOF

# Create background script
cat > ai-genius-extension/background.js << EOF
chrome.runtime.onInstalled.addListener(() => {
  // Create context menu items
  chrome.contextMenus.create({
    id: "ask-claude",
    title: "Ask Claude",
    contexts: ["selection"]
  });
  
  chrome.contextMenus.create({
    id: "ask-gemini",
    title: "Ask Gemini",
    contexts: ["selection"]
  });
  
  chrome.contextMenus.create({
    id: "ask-gpt",
    title: "Ask GPT-4",
    contexts: ["selection"]
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  const text = info.selectionText;
  let modelId = "";
  
  if (info.menuItemId === "ask-claude") modelId = "claude-sonnet-4";
  else if (info.menuItemId === "ask-gemini") modelId = "gemini-2-flash";
  else if (info.menuItemId === "ask-gpt") modelId = "gpt-4o";
  
  // Send to worker
  fetch("$WORKER_URL/api/ask", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({model_id: modelId, message: text})
  })
  .then(r => r.json())
  .then(data => {
    // Copy to clipboard
    navigator.clipboard.writeText(data.response);
    // Show notification
    chrome.notifications.create({
      type: "basic",
      iconUrl: "icon48.png",
      title: "AI GENIUS",
      message: "Response copied to clipboard!"
    });
  });
});
EOF

echo -e "${GREEN}✓ Extension created in ai-genius-extension/${NC}"
echo ""
echo -e "${YELLOW}To install:${NC}"
echo "Chrome/Edge:"
echo "1. Go to chrome://extensions"
echo "2. Enable 'Developer mode'"
echo "3. Click 'Load unpacked'"
echo "4. Select ai-genius-extension folder"
echo ""
echo "Firefox:"
echo "1. Go to about:debugging"
echo "2. Click 'This Firefox'"
echo "3. Click 'Load Temporary Add-on'"
echo "4. Select manifest.json"
echo ""

echo -e "${BLUE}[5/5] Bookmarklet (Quick Option)${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

BOOKMARKLET="javascript:(function(){const t=window.getSelection().toString();if(!t)return alert('No text selected');fetch('$WORKER_URL/api/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({model_id:'claude-sonnet-4',message:t})}).then(r=>r.json()).then(d=>{navigator.clipboard.writeText(d.response);alert('Response copied to clipboard!');});})();"

echo -e "${CYAN}Bookmarklet created!${NC}"
echo ""
echo -e "${YELLOW}To use:${NC}"
echo "1. Create a new bookmark"
echo "2. Name it: 'Ask Claude'"
echo "3. Paste this as URL:"
echo ""
echo -e "${CYAN}$BOOKMARKLET${NC}"
echo ""
echo "4. Select text on any page"
echo "5. Click the bookmark"
echo "6. Response copied to clipboard!"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}✅ SETUP COMPLETE${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo -e "${PURPLE}🎯 YOU NOW HAVE:${NC}"
echo ""
echo "1. ✅ Universal Python script (works everywhere)"
echo "2. ✅ Platform-specific setup (Mac/Linux/Windows)"
echo "3. ✅ Browser extension (Chrome/Firefox/Edge)"
echo "4. ✅ Bookmarklet (instant access)"
echo ""

echo -e "${PURPLE}💡 ADVANTAGES OVER AUTOMATOR:${NC}"
echo ""
echo "✅ Works on Mac, Windows, Linux"
echo "✅ Works on GABRIEL (HP Omen)"
echo "✅ No macOS-specific dependencies"
echo "✅ Cloudflare = always available"
echo "✅ Browser extension = works in browser"
echo "✅ Bookmarklet = zero installation"
echo "✅ More powerful than Automator"
echo "✅ Global access via Cloudflare"
echo ""

echo -e "${PURPLE}🚀 NEXT STEPS:${NC}"
echo ""
echo "1. Deploy Cloudflare Worker (if not done):"
echo "   ${CYAN}./deploy-ai-genius-cloud.sh${NC}"
echo ""
echo "2. Test the Python script:"
echo "   ${CYAN}python3 universal-ai-selector.py claude-sonnet-4${NC}"
echo ""
echo "3. Set up hotkeys (see instructions above)"
echo ""
echo "4. Install browser extension (optional)"
echo ""
echo "5. Create bookmarklet (instant access)"
echo ""

echo -e "${GREEN}✨ GORUNFREEX1000 - UNIVERSAL EDITION ✨${NC}"
echo ""
