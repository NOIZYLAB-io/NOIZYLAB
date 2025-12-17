# 🎯 GABRIEL COMMAND CENTER - Quick Reference

## 🚀 Start System
```bash
cd /Users/rsp_ms/GABRIEL/WebAvatar
python3 -m http.server 8000
# Open: http://localhost:8000
```

## 🎤 Voice Commands

### **System Status**
- "Check all systems"
- "Run health check"
- "System status"

### **NOIZYLAB**
- "NOIZYLAB status"
- "Create banner [description]"
- "Query knowledge portal about [topic]"
- "Execute NOIZYLAB operation [name]"

### **MyFamily AI**
- "Check family status"
- "Show family schedule"
- "Notify family [message]"
- "Check [member name]"

### **Google Drive**
- "List Drive files"
- "Stream file [file-id]"
- "Upload to Drive"
- "Share file with [email]"

### **TechTool**
- "Execute command [command]"
- "Show command history"
- "Terminal status"

### **System Management**
- "Optimize all systems"
- "Generate architect report"
- "Analyze [system] architecture"

## 📊 Dashboard Shortcuts

| Button | Action |
|--------|--------|
| 🔄 Refresh | Update all widgets |
| ❤️ Health Check | Run diagnostics |
| 📊 Toggle | Minimize/maximize |

## 🎮 Dashboard Console Commands

```javascript
// Direct command execution
system:status:all
system:health:check
noizylab:status
family:schedule
gdrive:list root
techtool:execute ls -la
architect:report
```

## 🔌 System Status Indicators

- 🟢 **Connected** - System online and responding
- 🟡 **Discovered** - System found but not connected
- ⚪ **Disconnected** - System offline
- 🔴 **Error** - System has errors

## 🏗️ Widget Controls

Each widget has:
- **View** - Detailed system analysis
- **Control** - Restart, optimize, logs, configure

## 📟 Console Log Types

- **Info** (Blue) - General information
- **Success** (Green) - Command succeeded
- **Error** (Red) - Command failed
- **Command** (Yellow) - User input

## 🔧 Quick Configuration

### **Add Backend System**

Edit `js/integration-hub.js`:
```javascript
const endpoints = [
    { name: 'your_system', url: 'http://localhost:PORT/api', check: '/health' }
];
```

### **Add Voice Pattern**

Edit `parseIntent()` in `integration-hub.js`:
```javascript
if (lower.includes('your keyword')) {
    return { system: 'your_system', action: 'your_action', params: {} };
}
```

### **Add Dashboard Widget**

Edit `createSystemWidgets()` in `unified-dashboard.js`:
```javascript
{
    id: 'your_system',
    name: 'Your System',
    icon: '⭐',
    color: '#your_color',
    metrics: ['Metric1', 'Metric2', 'Metric3']
}
```

## 🎯 Common Workflows

### **Morning Check**
```
Voice: "GABRIEL, check all systems"
       "Show family schedule"
       "NOIZYLAB status"
```

### **Project Setup**
```
Voice: "Create banner for new project"
       "Upload to Drive"
       "Notify family about new project"
```

### **System Maintenance**
```
Voice: "Run health check"
       "Optimize all systems"
       "Generate architect report"
```

## 🐛 Quick Fixes

| Problem | Solution |
|---------|----------|
| Dashboard not visible | Clear cache, refresh (Cmd+Shift+R) |
| Systems disconnected | Check backend services running |
| Voice not working | Check microphone permissions |
| Commands fail | Use dashboard console for testing |

## 📚 Key Files

```
WebAvatar/
├── index.html                    # Main interface
├── INTEGRATION_GUIDE.md          # Full documentation
├── js/
│   ├── integration-hub.js        # Command routing
│   ├── unified-dashboard.js      # Dashboard UI
│   └── main.js                   # Application controller
```

## 🔗 Your Systems

Connected to:
- **NOIZYLAB** - Operations, agents, banners
- **MyFamily AI** - Family monitoring
- **GDrive** - File streaming
- **Flow** - Browser extension
- **TechTool** - Terminal automation
- **Architect** - System optimization

## 💡 Pro Tips

1. **Dashboard stays on top** - Always visible during work
2. **Console = Command Line** - Faster than voice sometimes
3. **Mock data OK** - Works without backends for testing
4. **Voice patterns flexible** - Try natural language
5. **Widgets auto-update** - Every 5 seconds
6. **Multi-system tasks** - Chain commands together
7. **Event-driven** - Systems notify on changes

## 🎓 Learning Resources

- Full guide: `INTEGRATION_GUIDE.md`
- Web avatar: `README.md`
- Your docs: `/DOCUMENTATION/` folder
- Console (F12): Real-time logs

## ⚡ Power User Commands

```javascript
// Access from browser console (F12)

// Get all systems
app.integrationHub.getAllSystemsStatus()

// Execute any command
app.integrationHub.executeCommand('system:health:check')

// Process voice command
app.integrationHub.processVoiceCommand("your command")

// Multi-system orchestration
app.integrationHub.orchestrateMultiSystemTask({...workflow})

// Dashboard controls
dashboard.logToConsole("message", "info")
dashboard.updateAllWidgets()
```

## 🎉 Ready to Rock!

GABRIEL is your **unified command center** for everything!

**Start talking to your systems! 🚀**
