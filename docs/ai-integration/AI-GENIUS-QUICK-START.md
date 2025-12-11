# AI GENIUS - QUICK START CARD
## Print This | Pin It | Use It Daily

---

## ⚡ INSTANT START

```bash
cd /mnt/user-data/outputs/noizylab-perfect
./setup-ai-genius.sh      # Run once (2 min)
./start-ai-genius.sh      # Start server
open http://localhost:8888
```

---

## 🆓 10 FREE AI MODELS

| Model | Icon | Best For | How to Access |
|-------|------|----------|---------------|
| **Gemini Flash** | 💎 | Everything (FREE!) | Right-click → Ask Gemini |
| **Cursor AI** | 💻 | Coding | Right-click → Ask Cursor |
| **Perplexity** | 🔍 | Research | Right-click → Ask Perplexity |
| **Llama 3.3** | 🦙 | Privacy | Right-click → Ask Llama |
| **ChatGPT Free** | 🔮 | General | Web: chat.openai.com |
| **Phind** | 🔬 | Dev Help | Web: phind.com |
| **Ollama** | 🏠 | Local/Offline | Right-click → Ask Ollama |
| **Codeium** | 🚀 | Code Complete | IDE plugin |
| **HuggingFace** | 🤗 | Experiments | Web: huggingface.co/chat |
| **LM Studio** | 🎬 | Local GUI | App: lmstudio.ai |

**PLUS: You.com, Blackbox, Tabnine, Poe AI**

---

## ⌨️ KEYBOARD SHORTCUTS

**Assign in:** System Settings → Keyboard → Shortcuts → Services

| Hotkey | AI | Use For |
|--------|-----|---------|
| **⌘⌥G** | Gemini | Quick questions (FREE, fast) |
| **⌘⌥C** | Claude | Complex tasks |
| **⌘⌥K** | Cursor | Code review |
| **⌘⌥P** | Perplexity | Research (FREE) |
| **⌘⌥L** | Ollama | Offline/privacy (FREE) |

---

## 🎯 DAILY WORKFLOW

### 1. Start Once (Morning):
```bash
./start-ai-genius.sh &
```

### 2. Use All Day:
- **Select text anywhere**
- **Press hotkey** (or right-click)
- **Get answer**
- **Paste result**

### 3. Which AI?
- Quick → **Gemini** (FREE, fastest)
- Code → **Cursor** (FREE, best)
- Research → **Perplexity** (FREE, search)
- Complex → **Claude** ($3/M, smartest)
- Offline → **Ollama** (FREE, private)

---

## 📝 EDIT YOUR LIST

```bash
nano ai-models-list.json
```

**Add model:**
```json
"new-ai": {
  "name": "New AI",
  "free": true,
  "enabled": true
}
```

**Disable model:**
```json
"some-ai": {
  "enabled": false
}
```

**Save → Reload → Done!**

---

## 🔑 FREE API KEYS

**Google (Gemini):**
https://aistudio.google.com/app/apikey

**Together (Llama):**
https://api.together.xyz (free $25)

**HuggingFace:**
https://huggingface.co/settings/tokens

**Store key:**
```bash
security add-generic-password -a $USER -s 'google_api_key' -w "YOUR-KEY"
```

---

## 🚨 QUICK FIXES

**Server not starting?**
```bash
lsof -i :8888          # Check port
kill -9 <PID>          # Kill if needed
./start-ai-genius.sh   # Restart
```

**Right-click not showing?**
```bash
/System/Library/CoreServices/pbs -flush
killall Finder
```

**Ollama not running?**
```bash
brew install ollama
ollama serve &
ollama pull llama3.3
```

---

## 💡 PRO TIPS

1. **Start with Gemini** - FREE & excellent
2. **Use Perplexity for research** - Auto web search
3. **Ollama for privacy** - 100% local
4. **Cursor for coding** - Best AI editor
5. **Compare when unsure** - Multiple perspectives
6. **Hotkeys are king** - Set them up!
7. **Edit the list** - Add new AIs as you find them

---

## 📊 COST COMPARISON

| Model | Cost | Speed | Quality |
|-------|------|-------|---------|
| Gemini Flash | FREE | ⚡⚡⚡ | ⭐⭐⭐⭐ |
| Ollama | FREE | ⚡⚡ | ⭐⭐⭐⭐ |
| Perplexity | FREE | ⚡⚡ | ⭐⭐⭐⭐ |
| ChatGPT Free | FREE | ⚡⚡ | ⭐⭐⭐ |
| Claude | $3/M | ⚡ | ⭐⭐⭐⭐⭐ |

**Best FREE: Gemini Flash** ⭐  
**Best Paid: Claude Sonnet** ⭐

---

## ✅ CHECKLIST

- [ ] Run setup: `./setup-ai-genius.sh`
- [ ] Start server: `./start-ai-genius.sh`
- [ ] Open dashboard: http://localhost:8888
- [ ] Assign hotkeys: System Settings → Keyboard
- [ ] Get Google API key (free)
- [ ] Install Ollama: `brew install ollama`
- [ ] Download Cursor: https://cursor.sh
- [ ] Test: Select text → Press ⌘⌥G

---

## 📁 KEY FILES

- **ai-models-list.json** - Edit this!
- **AI-GENIUS-GUIDE.md** - Full docs
- **setup-ai-genius.sh** - Installer
- **start-ai-genius.sh** - Launcher

---

## 🎯 REMEMBER

**ONE SYSTEM = ALL AI**

**Select text. Press hotkey. Get answer.**

**GORUNFREE X1000 ✨**

---

**📌 Pin this card to your monitor**
