# AUTOMATOR AI CONTROL - COMPLETE GUIDE
## Use ANY AI Model from Anywhere on Mac

**Select text → Right-click → Ask AI**

---

## 🚀 ONE-COMMAND SETUP

```bash
cd /mnt/user-data/outputs/noizylab-perfect
./setup-automator-ai.sh
```

**Done. All AI models now in right-click menu.**

---

## 🎯 WHAT YOU GET

### Right-Click Menu (Services):
- **Ask Claude Opus** (🧠 most intelligent)
- **Ask Claude Sonnet** (⚡ best value)
- **Ask GPT-4o** (🔮 fast multimodal)
- **Ask Gemini Pro** (✨ huge context)
- **Ask Gemini Flash** (💎 cheapest)
- **Ask Llama** (🦙 open source)
- **Ask Perplexity** (🔍 search-augmented)

### Dynamic Tools:
- **AI Model Picker** - Choose model on-the-fly
- **AI Comparison** - Send to multiple models
- **API Key Manager** - Secure storage

---

## 📝 USAGE EXAMPLES

### Example 1: Code Review
```
1. In Cursor/VSCode, select your code
2. Right-click → Services → Ask Claude Sonnet
3. Wait 2-5 seconds
4. Response appears in TextEdit
5. Response also copied to clipboard
```

### Example 2: Explain Text
```
1. In Safari, select article paragraph
2. Right-click → Services → Ask GPT-4o
3. "Explain this in simple terms"
4. Response displayed
```

### Example 3: Research Query
```
1. Type your question in Notes
2. Select it
3. Right-click → Services → Ask Perplexity
4. Get search-augmented answer
```

### Example 4: Compare Models
```
1. Select your question
2. Run: ~/ai-compare.sh
3. Choose: Claude Sonnet, GPT-4o, Gemini
4. See all 3 responses side-by-side
```

### Example 5: Dynamic Model Pick
```
1. Select text
2. Run: ~/ai-model-picker.sh
3. Dialog shows all models
4. Pick the one you want
5. Get response
```

---

## ⌨️ KEYBOARD SHORTCUTS

### Setup Shortcuts:
1. **System Settings** → **Keyboard** → **Shortcuts** → **Services**
2. Find your "Ask [Model]" services
3. Assign hotkeys

### Recommended:
- **⌘⌥C** - Ask Claude Sonnet (most used)
- **⌘⌥G** - Ask GPT-4o (fast)
- **⌘⌥E** - Ask Gemini (cheap)
- **⌘⌥O** - Ask Claude Opus (complex)
- **⌘⌥P** - AI Model Picker (choose dynamically)
- **⌘⌥M** - AI Comparison (multiple models)

### Usage with Shortcuts:
```
1. Select text anywhere
2. Press ⌘⌥C
3. Claude Sonnet analyzes
4. Response in notification + clipboard + TextEdit
```

---

## 🎤 VOICE CONTROL INTEGRATION

### With Siri Shortcuts:

**Create Shortcut: "Ask AI"**
1. Open Shortcuts app
2. New Shortcut
3. Add actions:
   - Get Clipboard
   - Run Shell Script: `~/ai-model-picker.sh "[clipboard]"`
   - Show Result
4. Add to Siri: "Ask AI"

**Usage:**
```
1. Copy your question
2. Say: "Hey Siri, ask AI"
3. Pick model from dialog
4. Get response
```

**Create Shortcut: "Ask Claude"**
1. New Shortcut
2. Actions:
   - Get Clipboard
   - Run Shell Script with Clipboard
   - Speak Text (response)
3. Add to Siri: "Ask Claude"

**Usage:**
```
1. Copy code/text
2. Say: "Hey Siri, ask Claude"
3. Hear response
```

---

## 🔑 API KEYS SETUP

**One-time setup:**

```bash
~/setup-ai-keys.sh
```

**Enter your keys:**
- Anthropic: `sk-ant-api03-...` (you have this)
- OpenAI: `sk-...` (optional)
- Google: `AIza...` (optional)

**Keys stored securely in macOS Keychain.**

**Update a key:**
```bash
security add-generic-password -a $USER -s 'anthropic_api_key' -w "NEW-KEY" -U
```

**View stored key:**
```bash
security find-generic-password -a $USER -s 'anthropic_api_key' -w
```

---

## 🛠️ CUSTOMIZATION

### Add Custom Prompts

Edit the workflow to add a prefix:

```bash
# In the workflow script, change:
MESSAGE="$SELECTED_TEXT"

# To:
MESSAGE="Explain this code:\n\n$SELECTED_TEXT"
```

### Create Specialized Services

**"Improve This Code":**
```bash
MESSAGE="Improve this code for readability and performance:\n\n$SELECTED_TEXT"
MODEL_ID="claude-sonnet-4"
```

**"Find Bugs":**
```bash
MESSAGE="Find potential bugs or issues:\n\n$SELECTED_TEXT"
MODEL_ID="gpt-4o"
```

**"Simplify This":**
```bash
MESSAGE="Explain this in simple terms:\n\n$SELECTED_TEXT"
MODEL_ID="claude-sonnet-4"
```

---

## 📱 iOS SHORTCUTS INTEGRATION

### iPad/iPhone Shortcuts:

**Shortcut: "Send to Claude"**
```
1. Shortcut receives: Text
2. URL: http://GOD.local:7777/api/chat
3. Method: POST
4. Body:
   {
     "model": "claude-sonnet-4",
     "message": "[Input]",
     "conversation_id": "[timestamp]",
     "api_keys": {
       "anthropic": "sk-ant-..."
     }
   }
5. Get Dictionary Value: response
6. Show Result / Speak Text
```

**Usage:**
- Share text from any app → Send to Claude
- Or: Select text → Share → Send to Claude
- Or: Say "Hey Siri, send to Claude"

---

## 🔄 WORKFLOWS EXAMPLES

### Workflow 1: Code Explainer
```
Input: Selected code
Action: Send to Claude Sonnet
Output: Explanation in plain English
```

### Workflow 2: Multi-Model Comparison
```
Input: Question
Action: Send to Claude, GPT, Gemini
Output: 3 responses in table format
```

### Workflow 3: Smart Router
```
Input: Text
Logic: 
  - If code → Claude Sonnet
  - If question → Perplexity
  - If creative → Claude Opus
  - If technical doc → Gemini Pro
Output: Routed to best model
```

### Workflow 4: Continuous Improvement
```
Input: Code
Action 1: Ask Claude to improve
Action 2: Ask GPT to review improvements
Action 3: Ask Gemini for final check
Output: Best version from all 3
```

---

## 🎨 ADVANCED AUTOMATOR TECHNIQUES

### Chain Multiple AIs

**First pass - Claude:**
```applescript
tell application "System Events"
    keystroke "c" using command down
    delay 0.5
end tell

set selectedText to the clipboard
set response1 to do shell script "curl -X POST http://localhost:7777/api/chat ..."
```

**Second pass - GPT reviews Claude:**
```applescript
set response2 to do shell script "curl -X POST http://localhost:7777/api/chat -d '{\"message\":\"Review this response: " & response1 & "\"}'"
```

**Show both:**
```applescript
display dialog "Claude: " & response1 & "

GPT-4o: " & response2
```

### Context-Aware Routing

```applescript
set selectedText to the clipboard

if selectedText contains "function" or selectedText contains "def" then
    set modelToUse to "claude-sonnet-4"
else if selectedText contains "?" then
    set modelToUse to "perplexity-online"
else
    set modelToUse to "gpt-4o"
end if

-- Send to chosen model
```

### Batch Processing

```applescript
-- Get multiple selections
set textList to every paragraph of selectedText

repeat with currentText in textList
    -- Send each to AI
    set response to do shell script "curl ..."
    
    -- Collect responses
end repeat

-- Combine all responses
```

---

## 🚨 TROUBLESHOOTING

### "Service not appearing in menu"
```bash
# Refresh Services
/System/Library/CoreServices/pbs -flush
killall Finder
```

### "No response from AI"
1. Check DREAMCHAMBER is running: `ps aux | grep dreamchamber`
2. Test API: `curl http://localhost:7777/api/models`
3. Check API keys: `~/setup-ai-keys.sh`

### "API key error"
```bash
# Re-save key
security add-generic-password -a $USER -s 'anthropic_api_key' -w "YOUR-KEY" -U
```

### "Slow responses"
- Use faster model (Gemini Flash, GPT-4o)
- Check internet connection
- Try different model

---

## 💡 PRO TIPS

### Tip 1: Model Selection Strategy
- **Quick tasks:** Gemini Flash (fastest + cheapest)
- **Code review:** Claude Sonnet (best understanding)
- **Research:** Perplexity (includes search)
- **Complex reasoning:** Claude Opus (most intelligent)

### Tip 2: Keyboard Shortcuts
- Assign ⌘⌥C to your most-used model
- Use ⌘⌥P for dynamic picker
- ⌘⌥M for comparison mode

### Tip 3: Batch Operations
- Select multiple items
- Run comparison
- See which model performs best
- Use that model going forward

### Tip 4: Voice Control
- Create Siri shortcuts for each model
- "Ask Claude", "Ask GPT", etc.
- Hands-free operation
- Perfect for accessibility

### Tip 5: Context Matters
- Long documents → Gemini Pro (1M context)
- Code → Claude or GPT
- Research → Perplexity
- Creative → Claude Opus

---

## 📊 MODEL COMPARISON

| Model | Speed | Cost | Best For |
|-------|-------|------|----------|
| Gemini Flash | ⚡⚡⚡ | $ | Quick tasks |
| GPT-4o | ⚡⚡ | $$ | Balanced |
| Claude Sonnet | ⚡ | $$ | **Best overall** |
| Gemini Pro | ⚡⚡ | $ | Long docs |
| Perplexity | ⚡ | FREE | Research |
| Claude Opus | ⚡ | $$$$ | Complex |

---

## 🎯 RECOMMENDED WORKFLOW

### For Rob (Accessibility + GORUNFREE):

**Setup once:**
```bash
cd /mnt/user-data/outputs/noizylab-perfect
./setup-automator-ai.sh
~/setup-ai-keys.sh
node dreamchamber.js &
```

**Daily use:**
1. Select text anywhere
2. Press ⌘⌥C (or say "Ask Claude")
3. Get response instantly
4. Response in clipboard + notification + TextEdit

**Zero friction. Perfect accessibility.**

---

## ✅ SUMMARY

**What you got:**
- ✅ 7 AI models in right-click menu
- ✅ Keyboard shortcuts for each
- ✅ Voice control ready
- ✅ Model comparison tool
- ✅ Dynamic model picker
- ✅ Secure API key storage
- ✅ iOS Shortcuts compatible
- ✅ Works system-wide

**One setup command. Works everywhere.**

**GORUNFREE X1000 ✨**

---

## 📚 FILES CREATED

- **setup-automator-ai.sh** - Main setup script
- **~/Library/Services/Ask*.workflow** - Quick Actions (7 models)
- **~/ai-model-picker.sh** - Dynamic model selection
- **~/ai-compare.sh** - Multi-model comparison
- **~/setup-ai-keys.sh** - Secure key storage

---

**Select text. Right-click. Ask AI. Get answer.**

**That's it. GORUNFREE X1000. ✨**
