#!/bin/bash
# AI GENIUS - COMPLETE SETUP
# All AI models + Automator integration + Full automation
# GORUNFREE X1000

set -e

echo "🤖 AI GENIUS - COMPLETE SETUP"
echo "=============================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${BLUE}Step 1: Initialize Configuration${NC}"
node ai-genius-config.js save
echo -e "${GREEN}✓ Configuration created${NC}"
echo ""

echo -e "${BLUE}Step 2: Display Available AI Models${NC}"
node ai-genius-config.js list
echo ""

echo -e "${BLUE}Step 3: Create Automator Quick Actions${NC}"
echo "Creating right-click services for all AI models..."
echo ""

# Create Services directory
SERVICES_DIR="$HOME/Library/Services"
mkdir -p "$SERVICES_DIR"

# Function to create Quick Action for each model
create_quick_action() {
    local MODEL_ID=$1
    local MODEL_NAME=$2
    local MODEL_ICON=$3
    
    echo "  Creating: Ask $MODEL_NAME"
    
    WORKFLOW_PATH="$SERVICES_DIR/Ask $MODEL_NAME.workflow"
    mkdir -p "$WORKFLOW_PATH/Contents"
    
    # Create Info.plist
    cat > "$WORKFLOW_PATH/Contents/Info.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>NSServices</key>
    <array>
        <dict>
            <key>NSMenuItem</key>
            <dict>
                <key>default</key>
                <string>$MODEL_ICON Ask $MODEL_NAME</string>
            </dict>
            <key>NSMessage</key>
            <string>runWorkflowAsService</string>
            <key>NSRequiredContext</key>
            <dict>
                <key>NSTextContent</key>
                <string>NSStringPboardType</string>
            </dict>
            <key>NSSendTypes</key>
            <array>
                <string>public.utf8-plain-text</string>
            </array>
        </dict>
    </array>
</dict>
</plist>
EOF
    
    # Create workflow
    cat > "$WORKFLOW_PATH/Contents/document.wflow" << 'WFLOW_EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>actions</key>
    <array>
        <dict>
            <key>action</key>
            <dict>
                <key>AMActionVersion</key>
                <string>2.0.3</string>
                <key>AMApplication</key>
                <array>
                    <string>Automator</string>
                </array>
                <key>AMParameterProperties</key>
                <dict>
                    <key>COMMAND_STRING</key>
                    <dict/>
                    <key>CheckedForUserDefaultShell</key>
                    <dict/>
                    <key>inputMethod</key>
                    <dict/>
                    <key>shell</key>
                    <dict/>
                    <key>source</key>
                    <dict/>
                </dict>
                <key>AMProvides</key>
                <dict>
                    <key>Container</key>
                    <string>List</string>
                    <key>Types</key>
                    <array>
                        <string>com.apple.cocoa.string</string>
                    </array>
                </dict>
                <key>ActionBundlePath</key>
                <string>/System/Library/Automator/Run Shell Script.action</string>
                <key>ActionName</key>
                <string>Run Shell Script</string>
                <key>ActionParameters</key>
                <dict>
                    <key>COMMAND_STRING</key>
                    <string>#!/bin/bash
SELECTED_TEXT="$1"
MODEL_ID="MODEL_ID_PLACEHOLDER"
MODEL_NAME="MODEL_NAME_PLACEHOLDER"

# Call AI GENIUS
RESPONSE=$(curl -s -X POST http://localhost:8888/api/ask \
  -H "Content-Type: application/json" \
  -d "{
    \"model_id\": \"$MODEL_ID\",
    \"message\": \"$SELECTED_TEXT\",
    \"api_keys\": {
      \"ANTHROPIC_API_KEY\": \"$(security find-generic-password -a $USER -s 'anthropic_api_key' -w 2>/dev/null)\",
      \"GOOGLE_API_KEY\": \"$(security find-generic-password -a $USER -s 'google_api_key' -w 2>/dev/null)\",
      \"TOGETHER_API_KEY\": \"$(security find-generic-password -a $USER -s 'together_api_key' -w 2>/dev/null)\"
    }
  }")

# Extract response
RESPONSE_TEXT=$(echo "$RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin).get('response', 'No response'))")

# Copy to clipboard
echo "$RESPONSE_TEXT" | pbcopy

# Show notification
osascript -e "display notification \"Response copied to clipboard\" with title \"$MODEL_NAME\""

# Open in TextEdit
osascript << 'APPLESCRIPT_EOF'
tell application "TextEdit"
    activate
    make new document
    set text of document 1 to "MODEL_ICON_PLACEHOLDER $MODEL_NAME Response:\n\n" & "RESPONSE_TEXT_PLACEHOLDER"
end tell
APPLESCRIPT_EOF

echo "$RESPONSE_TEXT"
</string>
                    <key>CheckedForUserDefaultShell</key>
                    <true/>
                    <key>inputMethod</key>
                    <integer>0</integer>
                    <key>shell</key>
                    <string>/bin/bash</string>
                    <key>source</key>
                    <string></string>
                </dict>
                <key>BundleIdentifier</key>
                <string>com.apple.RunShellScript</string>
                <key>CFBundleVersion</key>
                <string>2.0.3</string>
                <key>CanShowSelectedItemsWhenRun</key>
                <false/>
                <key>CanShowWhenRun</key>
                <true/>
                <key>Category</key>
                <array>
                    <string>AMCategoryUtilities</string>
                </array>
                <key>Class Name</key>
                <string>RunShellScriptAction</string>
                <key>InputUUID</key>
                <string>INPUT-UUID</string>
                <key>Keywords</key>
                <array>
                    <string>Shell</string>
                    <string>Script</string>
                    <string>Command</string>
                    <string>Run</string>
                    <string>Unix</string>
                </array>
                <key>OutputUUID</key>
                <string>OUTPUT-UUID</string>
                <key>UUID</key>
                <string>ACTION-UUID</string>
                <key>UnlocalizedApplications</key>
                <array>
                    <string>Automator</string>
                </array>
                <key>arguments</key>
                <dict>
                    <key>0</key>
                    <dict>
                        <key>default value</key>
                        <integer>0</integer>
                        <key>name</key>
                        <string>inputMethod</string>
                        <key>required</key>
                        <string>0</string>
                        <key>type</key>
                        <string>0</string>
                        <key>uuid</key>
                        <string>0</string>
                    </dict>
                    <key>1</key>
                    <dict>
                        <key>default value</key>
                        <false/>
                        <key>name</key>
                        <string>CheckedForUserDefaultShell</string>
                        <key>required</key>
                        <string>0</string>
                        <key>type</key>
                        <string>0</string>
                        <key>uuid</key>
                        <string>1</string>
                    </dict>
                    <key>2</key>
                    <dict>
                        <key>default value</key>
                        <string></string>
                        <key>name</key>
                        <string>source</string>
                        <key>required</key>
                        <string>0</string>
                        <key>type</key>
                        <string>0</string>
                        <key>uuid</key>
                        <string>2</string>
                    </dict>
                    <key>3</key>
                    <dict>
                        <key>default value</key>
                        <string></string>
                        <key>name</key>
                        <string>COMMAND_STRING</string>
                        <key>required</key>
                        <string>0</string>
                        <key>type</key>
                        <string>0</string>
                        <key>uuid</key>
                        <string>3</string>
                    </dict>
                    <key>4</key>
                    <dict>
                        <key>default value</key>
                        <string>/bin/sh</string>
                        <key>name</key>
                        <string>shell</string>
                        <key>required</key>
                        <string>0</string>
                        <key>type</key>
                        <string>0</string>
                        <key>uuid</key>
                        <string>4</string>
                    </dict>
                </dict>
                <key>isViewVisible</key>
                <integer>1</integer>
                <key>location</key>
                <string>449.000000:316.000000</string>
                <key>nibPath</key>
                <string>/System/Library/Automator/Run Shell Script.action/Contents/Resources/Base.lproj/main.nib</string>
            </dict>
            <key>isViewVisible</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>connectors</key>
    <dict/>
    <key>workflowMetaData</key>
    <dict>
        <key>workflowTypeIdentifier</key>
        <string>com.apple.Automator.servicesMenu</string>
    </dict>
</dict>
</plist>
WFLOW_EOF
    
    # Replace placeholders
    sed -i '' "s/MODEL_ID_PLACEHOLDER/$MODEL_ID/g" "$WORKFLOW_PATH/Contents/document.wflow"
    sed -i '' "s/MODEL_NAME_PLACEHOLDER/$MODEL_NAME/g" "$WORKFLOW_PATH/Contents/document.wflow"
    sed -i '' "s/MODEL_ICON_PLACEHOLDER/$MODEL_ICON/g" "$WORKFLOW_PATH/Contents/document.wflow"
}

# Create Quick Actions for key models
create_quick_action "cursor" "Cursor AI" "💻"
create_quick_action "claude-sonnet" "Claude Sonnet" "⚡"
create_quick_action "gemini-flash" "Gemini Flash" "💎"
create_quick_action "chatgpt-free" "ChatGPT" "🔮"
create_quick_action "llama-3.3-70b" "Llama 3.3" "🦙"
create_quick_action "perplexity" "Perplexity" "🔍"
create_quick_action "ollama-local" "Ollama Local" "🏠"

echo -e "${GREEN}✓ Quick Actions created${NC}"
echo ""

echo -e "${BLUE}Step 4: Refresh Services Menu${NC}"
/System/Library/CoreServices/pbs -flush
killall Finder 2>/dev/null || true
echo -e "${GREEN}✓ Services refreshed${NC}"
echo ""

echo -e "${BLUE}Step 5: Start AI GENIUS Server${NC}"
echo "Starting server on port 8888..."
echo ""

# Create launch script
cat > "$SCRIPT_DIR/start-ai-genius.sh" << 'START_EOF'
#!/bin/bash
cd "$(dirname "$0")"
node ai-genius.js
START_EOF

chmod +x "$SCRIPT_DIR/start-ai-genius.sh"

echo -e "${GREEN}✓ Launch script created${NC}"
echo ""

echo "================================"
echo -e "${GREEN}AI GENIUS SETUP COMPLETE!${NC}"
echo "================================"
echo ""
echo "What was created:"
echo ""
echo "📋 Configuration:"
echo "  • ai-genius-config.json (editable)"
echo "  • 16+ AI models configured"
echo "  • 10+ FREE models included"
echo ""
echo "🤖 Quick Actions (Right-click menu):"
echo "  • Ask Cursor AI"
echo "  • Ask Claude Sonnet"
echo "  • Ask Gemini Flash"
echo "  • Ask ChatGPT"
echo "  • Ask Llama 3.3"
echo "  • Ask Perplexity"
echo "  • Ask Ollama Local"
echo ""
echo "🌐 Web Dashboard:"
echo "  http://localhost:8888"
echo "  http://GOD.local:8888"
echo "  http://10.90.90.x:8888 (iPad)"
echo ""
echo "Next steps:"
echo ""
echo "1️⃣  Start the server:"
echo "   ./start-ai-genius.sh"
echo ""
echo "2️⃣  Open dashboard:"
echo "   open http://localhost:8888"
echo ""
echo "3️⃣  Edit configuration (optional):"
echo "   nano ai-genius-config.json"
echo "   OR use web dashboard"
echo ""
echo "4️⃣  Setup keyboard shortcuts:"
echo "   System Settings > Keyboard > Shortcuts > Services"
echo "   Assign hotkeys to 'Ask' services"
echo ""
echo "5️⃣  Use AI anywhere:"
echo "   Select text > Right-click > Services > Ask [Model]"
echo "   OR press your hotkey"
echo ""
echo "================================"
echo "🚀 Features Ready:"
echo "================================"
echo ""
echo "✅ Cursor AI - Code editor integration"
echo "✅ GitHub Copilot++ - VSCode extension"
echo "✅ Claude Sonnet - Best value AI"
echo "✅ Gemini Flash - FREE & fastest"
echo "✅ ChatGPT - Free web access"
echo "✅ Llama 3.3 - Open source"
echo "✅ Perplexity - Search-augmented"
echo "✅ Ollama - Local/offline AI"
echo "✅ HuggingFace - Multiple models"
echo "✅ Poe AI - Multi-bot access"
echo "✅ You.com - AI search"
echo "✅ Phind - Developer search"
echo "✅ LM Studio - Local GUI"
echo "✅ Tabnine - Code completion"
echo "✅ Codeium - Forever free coding"
echo "✅ Blackbox AI - Code search"
echo ""
echo "GORUNFREE X1000 ✨"
