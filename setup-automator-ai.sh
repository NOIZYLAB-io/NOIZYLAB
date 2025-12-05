#!/bin/bash
# AUTOMATOR AI CONTROL - COMPLETE SETUP
# Creates Quick Actions for every AI model
# GORUNFREE X1000

echo "🤖 AUTOMATOR AI CONTROL SETUP"
echo "=============================="
echo ""

# Create Automator workflows directory
WORKFLOWS_DIR="$HOME/Library/Services"
mkdir -p "$WORKFLOWS_DIR"

echo "Creating Quick Actions for AI models..."
echo ""

# Function to create an Automator Quick Action
create_ai_workflow() {
    local MODEL_NAME=$1
    local MODEL_ID=$2
    local ICON=$3
    
    echo "  📝 Creating: Ask $MODEL_NAME"
    
    # Create the workflow bundle
    WORKFLOW_PATH="$WORKFLOWS_DIR/Ask $MODEL_NAME.workflow"
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
                <string>Ask $MODEL_NAME</string>
            </dict>
            <key>NSMessage</key>
            <string>runWorkflowAsService</string>
            <key>NSRequiredContext</key>
            <dict>
                <key>NSApplicationIdentifier</key>
                <string>*</string>
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
    
    # Create the AppleScript that calls DREAMCHAMBER
    cat > "$WORKFLOW_PATH/Contents/document.wflow" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>actions</key>
    <array>
        <dict>
            <key>action</key>
            <dict>
                <key>ActionName</key>
                <string>Run Shell Script</string>
                <key>ActionParameters</key>
                <dict>
                    <key>COMMAND_STRING</key>
                    <string>#!/bin/bash
# Send selected text to $MODEL_NAME via DREAMCHAMBER

SELECTED_TEXT="\$1"
MODEL_ID="$MODEL_ID"

# Call DREAMCHAMBER API
RESPONSE=\$(curl -s -X POST http://localhost:7777/api/chat \\
  -H "Content-Type: application/json" \\
  -d "{
    \\"model\\": \\"\$MODEL_ID\\",
    \\"message\\": \\"\$SELECTED_TEXT\\",
    \\"conversation_id\\": \\"\$(date +%s)\\",
    \\"api_keys\\": {
      \\"anthropic\\": \\"\$(security find-generic-password -a \$USER -s 'anthropic_api_key' -w 2>/dev/null)\\",
      \\"openai\\": \\"\$(security find-generic-password -a \$USER -s 'openai_api_key' -w 2>/dev/null)\\",
      \\"google\\": \\"\$(security find-generic-password -a \$USER -s 'google_api_key' -w 2>/dev/null)\\"
    }
  }")

# Extract response text
RESPONSE_TEXT=\$(echo "\$RESPONSE" | jq -r '.response // .error // "No response"')

# Show notification
osascript -e "display notification \\"\$RESPONSE_TEXT\\" with title \\"$MODEL_NAME Response\\""

# Copy to clipboard
echo "\$RESPONSE_TEXT" | pbcopy

# Open in new window (optional)
osascript -e 'tell application "TextEdit"
    activate
    make new document
    set text of document 1 to "'"$ICON $MODEL_NAME Response:"'\\n\\n" & "'\$RESPONSE_TEXT'"
end tell'

echo "\$RESPONSE_TEXT"
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
            </dict>
        </dict>
    </array>
</dict>
</plist>
EOF
    
}

# Create workflows for all major models
echo "Creating Quick Actions..."
echo ""

create_ai_workflow "Claude Opus" "claude-opus-4" "🧠"
create_ai_workflow "Claude Sonnet" "claude-sonnet-4" "⚡"
create_ai_workflow "GPT-4o" "gpt-4o" "🔮"
create_ai_workflow "Gemini Pro" "gemini-pro" "✨"
create_ai_workflow "Gemini Flash" "gemini-2.0-flash" "💎"
create_ai_workflow "Llama" "llama-3.3-70b" "🦙"
create_ai_workflow "Perplexity" "perplexity-online" "🔍"

echo ""
echo "✅ Quick Actions created!"
echo ""

# Create model picker workflow
echo "Creating AI Model Picker..."

cat > "$HOME/ai-model-picker.sh" << 'PICKER_EOF'
#!/bin/bash
# AI MODEL PICKER - Choose which AI to use

SELECTED_TEXT="$1"

# Show model picker dialog
MODEL=$(osascript << EOF
set modelList to {"🧠 Claude Opus (Most Intelligent)", "⚡ Claude Sonnet (Best Value)", "🔮 GPT-4o (Fast Multimodal)", "✨ Gemini Pro (Huge Context)", "💎 Gemini Flash (Cheapest)", "🦙 Llama 3.3 (Open Source)", "🔍 Perplexity (Search)"}
set chosenModel to choose from list modelList with prompt "Select AI Model:" default items {"⚡ Claude Sonnet (Best Value)"}
return chosenModel
EOF
)

# Map display name to model ID
case "$MODEL" in
    *"Claude Opus"*)
        MODEL_ID="claude-opus-4"
        ;;
    *"Claude Sonnet"*)
        MODEL_ID="claude-sonnet-4"
        ;;
    *"GPT-4o"*)
        MODEL_ID="gpt-4o"
        ;;
    *"Gemini Pro"*)
        MODEL_ID="gemini-pro"
        ;;
    *"Gemini Flash"*)
        MODEL_ID="gemini-2.0-flash"
        ;;
    *"Llama"*)
        MODEL_ID="llama-3.3-70b"
        ;;
    *"Perplexity"*)
        MODEL_ID="perplexity-online"
        ;;
    *)
        echo "No model selected"
        exit 1
        ;;
esac

# Send to DREAMCHAMBER
RESPONSE=$(curl -s -X POST http://localhost:7777/api/chat \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"$MODEL_ID\",
    \"message\": \"$SELECTED_TEXT\",
    \"conversation_id\": \"$(date +%s)\",
    \"api_keys\": {
      \"anthropic\": \"$(security find-generic-password -a $USER -s 'anthropic_api_key' -w 2>/dev/null)\",
      \"openai\": \"$(security find-generic-password -a $USER -s 'openai_api_key' -w 2>/dev/null)\",
      \"google\": \"$(security find-generic-password -a $USER -s 'google_api_key' -w 2>/dev/null)\"
    }
  }")

# Extract and display response
RESPONSE_TEXT=$(echo "$RESPONSE" | jq -r '.response // .error // "No response"')

osascript -e "display dialog \"$RESPONSE_TEXT\" buttons {\"Copy\", \"OK\"} default button \"Copy\""

if [ $? -eq 0 ]; then
    echo "$RESPONSE_TEXT" | pbcopy
fi

echo "$RESPONSE_TEXT"
PICKER_EOF

chmod +x "$HOME/ai-model-picker.sh"

echo "✅ AI Model Picker created at ~/ai-model-picker.sh"
echo ""

# Create comparison workflow
echo "Creating AI Comparison workflow..."

cat > "$HOME/ai-compare.sh" << 'COMPARE_EOF'
#!/bin/bash
# AI MODEL COMPARISON - Send to multiple models at once

SELECTED_TEXT="$1"

# Show model selection dialog (multiple)
MODELS=$(osascript << EOF
set modelList to {"Claude Sonnet", "GPT-4o", "Gemini Pro", "Claude Opus", "Perplexity"}
set chosenModels to choose from list modelList with prompt "Select models to compare:" with multiple selections allowed
return chosenModels
EOF
)

if [ "$MODELS" = "false" ]; then
    echo "No models selected"
    exit 1
fi

# Convert to model IDs
MODEL_IDS=""
echo "$MODELS" | tr ',' '\n' | while read MODEL; do
    case "$MODEL" in
        *"Claude Opus"*) echo "claude-opus-4" ;;
        *"Claude Sonnet"*) echo "claude-sonnet-4" ;;
        *"GPT-4o"*) echo "gpt-4o" ;;
        *"Gemini Pro"*) echo "gemini-pro" ;;
        *"Perplexity"*) echo "perplexity-online" ;;
    esac
done > /tmp/model_ids.txt

# Send to comparison API
MODELS_JSON=$(cat /tmp/model_ids.txt | jq -R . | jq -s .)

RESPONSE=$(curl -s -X POST http://localhost:7777/api/compare \
  -H "Content-Type: application/json" \
  -d "{
    \"models\": $MODELS_JSON,
    \"message\": \"$SELECTED_TEXT\",
    \"api_keys\": {
      \"anthropic\": \"$(security find-generic-password -a $USER -s 'anthropic_api_key' -w 2>/dev/null)\",
      \"openai\": \"$(security find-generic-password -a $USER -s 'openai_api_key' -w 2>/dev/null)\",
      \"google\": \"$(security find-generic-password -a $USER -s 'google_api_key' -w 2>/dev/null)\"
    }
  }")

# Format and display results
echo "$RESPONSE" | jq -r '.results[] | "## \(.model)\n\n\(.response)\n\n---\n"' > /tmp/comparison.txt

open -e /tmp/comparison.txt

echo "Comparison complete - opened in TextEdit"
COMPARE_EOF

chmod +x "$HOME/ai-compare.sh"

echo "✅ AI Comparison tool created at ~/ai-compare.sh"
echo ""

# Store API keys in Keychain
echo "Setting up secure API key storage..."
echo ""

cat > "$HOME/setup-ai-keys.sh" << 'KEYS_EOF'
#!/bin/bash
# SETUP AI API KEYS - Secure storage in macOS Keychain

echo "🔑 AI API Keys Setup"
echo "==================="
echo ""

# Anthropic
read -p "Enter Anthropic API key (or press Enter to skip): " ANTHROPIC_KEY
if [ ! -z "$ANTHROPIC_KEY" ]; then
    security add-generic-password -a $USER -s 'anthropic_api_key' -w "$ANTHROPIC_KEY" -U
    echo "✅ Anthropic key saved"
fi

# OpenAI
read -p "Enter OpenAI API key (or press Enter to skip): " OPENAI_KEY
if [ ! -z "$OPENAI_KEY" ]; then
    security add-generic-password -a $USER -s 'openai_api_key' -w "$OPENAI_KEY" -U
    echo "✅ OpenAI key saved"
fi

# Google
read -p "Enter Google API key (or press Enter to skip): " GOOGLE_KEY
if [ ! -z "$GOOGLE_KEY" ]; then
    security add-generic-password -a $USER -s 'google_api_key' -w "$GOOGLE_KEY" -U
    echo "✅ Google key saved"
fi

echo ""
echo "✅ API keys saved securely in Keychain"
KEYS_EOF

chmod +x "$HOME/setup-ai-keys.sh"

echo "✅ API key setup tool created at ~/setup-ai-keys.sh"
echo ""

# Refresh Services menu
echo "Refreshing Services menu..."
/System/Library/CoreServices/pbs -flush
killall Finder

echo ""
echo "================================"
echo "✅ AUTOMATOR AI CONTROL READY!"
echo "================================"
echo ""
echo "What was created:"
echo ""
echo "Quick Actions (Right-click menu):"
echo "  • Ask Claude Opus"
echo "  • Ask Claude Sonnet"
echo "  • Ask GPT-4o"
echo "  • Ask Gemini Pro"
echo "  • Ask Gemini Flash"
echo "  • Ask Llama"
echo "  • Ask Perplexity"
echo ""
echo "Scripts:"
echo "  • ~/ai-model-picker.sh - Choose model dynamically"
echo "  • ~/ai-compare.sh - Compare multiple models"
echo "  • ~/setup-ai-keys.sh - Store API keys securely"
echo ""
echo "Next steps:"
echo "  1. Run: ~/setup-ai-keys.sh (store your API keys)"
echo "  2. Start DREAMCHAMBER: node dreamchamber.js"
echo "  3. Select text anywhere"
echo "  4. Right-click > Services > Ask [Model]"
echo ""
echo "Keyboard shortcuts:"
echo "  System Settings > Keyboard > Shortcuts > Services"
echo "  Assign hotkeys to each 'Ask' service"
echo ""
echo "Suggested hotkeys:"
echo "  ⌘⌥C - Ask Claude Sonnet"
echo "  ⌘⌥G - Ask GPT-4o"
echo "  ⌘⌥E - Ask Gemini"
echo "  ⌘⌥P - Pick Model"
echo ""
