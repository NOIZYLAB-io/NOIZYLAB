# AUTOMATOR AI - QUICK REFERENCE CARD
## Keep This Handy

---

## ⚡ INSTANT SETUP

```bash
./setup-automator-ai.sh
~/setup-ai-keys.sh
node dreamchamber.js &
```

---

## 🎯 RIGHT-CLICK MENU

**Select text → Right-click → Services →**

- **Ask Claude Opus** 🧠 - Most intelligent
- **Ask Claude Sonnet** ⚡ - Best value (recommended)
- **Ask GPT-4o** 🔮 - Fast multimodal
- **Ask Gemini Pro** ✨ - Huge context (1M tokens)
- **Ask Gemini Flash** 💎 - Cheapest ($0.075/M)
- **Ask Llama** 🦙 - Open source
- **Ask Perplexity** 🔍 - Search-augmented

---

## ⌨️ KEYBOARD SHORTCUTS

**Assign in:** System Settings → Keyboard → Shortcuts → Services

Recommended:
- **⌘⌥C** - Ask Claude Sonnet
- **⌘⌥G** - Ask GPT-4o
- **⌘⌥E** - Ask Gemini
- **⌘⌥P** - Pick Model (dynamic)
- **⌘⌥M** - Compare Models

---

## 🎤 VOICE COMMANDS

**Setup Siri Shortcuts, then say:**

- "Ask Claude" → Claude Sonnet
- "Ask GPT" → GPT-4o
- "Ask AI" → Pick model dynamically
- "Compare models" → Multi-model comparison

---

## 💰 WHICH MODEL WHEN

| Task | Model | Why |
|------|-------|-----|
| Code review | Claude Sonnet | Best understanding |
| Quick question | Gemini Flash | Fastest + cheapest |
| Research | Perplexity | Includes web search |
| Long document | Gemini Pro | 1M token context |
| Complex analysis | Claude Opus | Most intelligent |
| Creative writing | Claude Opus | Best creativity |
| General use | Claude Sonnet | Best value |

---

## 🛠️ TOOLS

**~/ai-model-picker.sh** - Choose model on-the-fly  
**~/ai-compare.sh** - Compare multiple models  
**~/setup-ai-keys.sh** - Manage API keys  

---

## 🚨 QUICK FIXES

**Service not showing?**
```bash
/System/Library/CoreServices/pbs -flush
killall Finder
```

**DREAMCHAMBER not running?**
```bash
node dreamchamber.js &
```

**Check API keys:**
```bash
security find-generic-password -a $USER -s 'anthropic_api_key' -w
```

---

## 💡 PRO TIPS

1. **Use ⌘⌥C for everything** - Claude Sonnet is 90% good enough
2. **Perplexity for research** - It searches the web automatically
3. **Gemini Flash for speed** - When you need fast answers
4. **Compare on important stuff** - Get multiple perspectives
5. **Voice control rocks** - Set it up, you'll love it

---

## 📊 COST REFERENCE

**Per 1M input tokens:**
- Gemini Flash: $0.075 (cheapest)
- Gemini Pro: $0.125
- Llama: $0.88
- GPT-4o: $2.50
- Claude Sonnet: $3.00 ⭐ (best value)
- Claude Opus: $15.00 (premium)
- Perplexity: FREE (with search)

---

## ✅ DAILY WORKFLOW

1. Start DREAMCHAMBER once: `node dreamchamber.js &`
2. Select text anywhere
3. Press **⌘⌥C** (or right-click → Ask Claude Sonnet)
4. Response in: Notification + Clipboard + TextEdit
5. Paste where needed

**Zero friction. GORUNFREE X1000.**

---

**Print this. Pin it. Use it daily. 📌**
