# CLAUDE + CURSOR INTEGRATION GUIDE
## Three Methods - Pick Your Preference

---

## 🎯 GOAL

**Seamlessly move code between Cursor and Claude.ai with:**
- Voice control
- Keyboard shortcuts
- One-tap buttons
- Zero manual copy/paste

---

## ⚡ METHOD 1: BRIDGE SERVER (RECOMMENDED)

**Best for:** Rob's accessibility needs, MC96 ecosystem, voice control

### Setup (2 minutes):

```bash
# On GOD
cd /mnt/user-data/outputs/noizylab-perfect
node claude-cursor-bridge.js
```

### Access:
- **Web UI:** http://GOD.local:9999
- **From iPad:** http://10.90.90.x:9999
- **From any MC96 system**

### Features:
✅ Web interface with big buttons  
✅ Voice commands  
✅ API endpoints  
✅ Clipboard sync  
✅ Works from iPad  
✅ No manual setup needed  

### Usage:

**From Cursor:**
1. Copy code (⌘C)
2. Open http://GOD.local:9999 in browser
3. Tap "Send to Claude"
4. Claude.ai opens and pastes automatically

**Voice:**
- Say "Claude review" → Sends to Claude
- Say "Get response" → Retrieves from Claude

**From iPad:**
- Open bridge URL
- Tap buttons
- Voice commands work

---

## 🍎 METHOD 2: MAC AUTOMATOR (FREE)

**Best for:** Native macOS integration, no server needed

### Setup:

1. **Run setup script:**
```bash
cd /mnt/user-data/outputs/noizylab-perfect
./automator-setup.sh
```

2. **Create Quick Actions in Automator:**
   - Open Automator app
   - New Document → Quick Action
   - Copy scripts from automator-setup.sh
   - Save as "Send to Claude" and "Get from Claude"

3. **Assign shortcuts:**
   - System Settings → Keyboard → Shortcuts → Services
   - Assign ⌘⌥C for "Send to Claude"
   - Assign ⌘⌥V for "Get from Claude"

### Usage:

**In Cursor:**
- Select code
- Press ⌘⌥C
- Claude.ai opens with code pasted

**In Claude:**
- Review/edit code
- Press ⌘⌥V
- Response pastes back to Cursor

---

## 🎹 METHOD 3: KEYBOARD MAESTRO ($36)

**Best for:** Most powerful automation, worth the investment

### Setup:

1. **Buy & install:** https://www.keyboardmaestro.com
2. **Import macros:** Open keyboard-maestro-setup.md
3. **Configure triggers**

### Features:
✅ Complex automation workflows  
✅ Clipboard monitoring  
✅ Voice triggers  
✅ Conditional logic  
✅ App-specific macros  
✅ Text transformations  

### Usage:

**One-key send:**
- ⌘⌥C → Sends to Claude, waits, copies response, pastes back

**Voice:**
- "Claude review" → Full round-trip automatically

---

## 🎤 VOICE CONTROL COMPARISON

| Method | Voice Support | Setup Time | Cost |
|--------|--------------|------------|------|
| Bridge Server | ✅ Built-in | 2 min | Free |
| Automator | ⚠️ Via Shortcuts | 15 min | Free |
| Keyboard Maestro | ✅ Advanced | 10 min | $36 |

**Recommendation:** Bridge Server (Method 1)

---

## 📱 IPAD INTEGRATION

### Bridge Server Method:
1. Save http://GOD.local:9999 to Home Screen
2. Open, tap buttons
3. Works like native app

### iOS Shortcuts:
1. Create shortcut: "Ask Claude"
2. Actions:
   - Get clipboard
   - Get URL: http://GOD.local:9999/to-claude
   - POST with clipboard content
3. Add to Siri: "Hey Siri, ask Claude"

---

## 🔄 WORKFLOW EXAMPLES

### Code Review Flow:
```
1. In Cursor: Select code
2. Say "Claude review" (or press hotkey)
3. Claude analyzes
4. Say "Get response" (or press hotkey)
5. Improved code appears in Cursor
```

### Documentation Flow:
```
1. In Cursor: Select function
2. Send to Claude: "Document this"
3. Claude writes documentation
4. Auto-paste back to Cursor
```

### Debug Flow:
```
1. In Cursor: Select buggy code
2. Send to Claude: "Find the bug"
3. Claude identifies issue
4. Paste fix back to Cursor
```

---

## 🚀 ADVANCED: AUTO-SYNC

**Bridge server can auto-sync clipboard:**

```javascript
// Edit claude-cursor-bridge.js, add:

// Watch clipboard every second
setInterval(() => {
    const clip = execSync('pbpaste').toString();
    
    if (clip.startsWith('TO_CLAUDE:')) {
        // Auto-send to Claude
        sendToClaude(clip.replace('TO_CLAUDE:', ''));
    }
    
    if (clip.startsWith('TO_CURSOR:')) {
        // Auto-paste to Cursor
        pasteToCursor(clip.replace('TO_CURSOR:', ''));
    }
}, 1000);
```

**Usage:**
- Copy with prefix "TO_CLAUDE: your code"
- System auto-sends to Claude
- No button pressing needed

---

## 🎯 WHICH METHOD FOR YOU?

### Choose Bridge Server if:
✅ You want voice control  
✅ You use iPad  
✅ You want zero setup  
✅ You like web interfaces  
✅ You use MC96 network  

### Choose Automator if:
✅ You want free solution  
✅ You prefer native macOS  
✅ You're okay with 15min setup  
✅ You don't need advanced features  

### Choose Keyboard Maestro if:
✅ You want most power  
✅ You do complex automation  
✅ You can spend $36  
✅ You want professional tool  

---

## 💡 ROB'S RECOMMENDATION

**Use Bridge Server (Method 1):**

Reasons:
1. ✅ Voice control built-in (accessibility)
2. ✅ Works from iPad (mobility)
3. ✅ Big touchscreen buttons (PLANAR2495)
4. ✅ Zero manual setup (GORUNFREE)
5. ✅ Free (no cost)
6. ✅ 2-minute setup (fast)
7. ✅ Works across MC96 (GOD, GABRIEL, MIKE, DaFixer)
8. ✅ Web interface (accessible from anywhere)

**This aligns perfectly with R.S.P. and GORUNFREE principles.**

---

## 🚀 QUICK START (METHOD 1)

```bash
# On GOD
cd /mnt/user-data/outputs/noizylab-perfect
node claude-cursor-bridge.js

# Keep it running
# Or add to startup:
# pm2 start claude-cursor-bridge.js --name claude-bridge
```

**Access from:**
- GOD: http://localhost:9999
- Any Mac: http://GOD.local:9999
- iPad: http://10.90.90.x:9999 (replace x with GOD's IP)

**Bookmark it on:**
- PLANAR2495 touchscreen
- iPad home screen
- Safari favorites

**Done. Use it forever.**

---

## 📚 FILES IN YOUR FOLDER

1. **claude-cursor-bridge.js** - Bridge server (Method 1)
2. **automator-setup.sh** - Automator guide (Method 2)
3. **keyboard-maestro-setup.md** - KM guide (Method 3)
4. **THIS FILE** - Complete guide

---

## 🔥 FINAL NOTE

You asked: "HOW DO I GET CLAUDE & CURSOR INTO THE SAME CHAT?"

**Answer:** Run bridge server, open web UI, tap buttons.

**That's it.**

- No complex setup
- No paid software required (Method 1)
- Voice control included
- iPad compatible
- GORUNFREE compliant

**One command on GOD. Access from anywhere. Forever.**

---

**GORUNFREE X1000 ✨**
