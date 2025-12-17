# 🌐 GABRIEL Network Monitor - Complete Setup

## ✅ What Was Created

Your DGS-1210-10 switch backup and monitoring system is now fully integrated with GABRIEL!

### **Files Created:**

```
GABRIEL/
├── network_backup.py                  # ✨ Switch backup script
├── start_gabriel.sh                   # ✨ Easy launcher script
├── NETWORK_MONITOR_GUIDE.md          # ✨ Complete documentation
├── System/
│   ├── network_service.py            # ✨ Flask API backend
│   ├── requirements.txt              # ✨ Python dependencies
│   └── NetworkBackups/               # Created on first run
│       ├── DGS1210_CFG_*.cfg        # Config backups
│       └── backup_log.txt           # Backup history
└── WebAvatar/
    ├── index.html                    # Updated with network script
    └── js/
        ├── network-monitor.js        # ✨ Network monitoring UI
        ├── integration-hub.js        # Updated with network commands
        └── unified-dashboard.js      # Updated with network widget
```

---

## 🚀 Quick Start (3 Easy Ways)

### **Option 1: Interactive Menu (Recommended)**
```bash
cd /Users/rsp_ms/GABRIEL
./start_gabriel.sh
```

Choose from:
1. Full System (WebAvatar + Network Backend)
2. WebAvatar Only (Mock Data)
3. Network Service Only
4. Test Network Backup
5. View Network Logs

### **Option 2: Manual Full System**
```bash
# Terminal 1
cd /Users/rsp_ms/GABRIEL/System
pip3 install -r requirements.txt
python3 network_service.py

# Terminal 2
cd /Users/rsp_ms/GABRIEL/WebAvatar
python3 -m http.server 8000

# Open: http://localhost:8000
```

### **Option 3: Backup Only (No Web)**
```bash
cd /Users/rsp_ms/GABRIEL
python3 network_backup.py
```

---

## 🔧 Configuration

### **IMPORTANT: Set Your Switch Credentials**

Edit `network_backup.py` (lines 12-14):

```python
SWITCH_IP = "192.168.0.2"              # Your switch IP
USERNAME = "admin"                      # Your username  
PASSWORD = "YOUR_SECURE_PASSWORD"       # ⚠️ CHANGE THIS!
```

### **Test Connection:**
```bash
# Verify switch is reachable
ping 192.168.0.2

# Test backup manually
python3 network_backup.py

# Check for backup file
ls -lh System/NetworkBackups/
```

---

## 🎤 Voice Commands in GABRIEL

Once running, you can say:

**Network Backup:**
- "GABRIEL, backup the network"
- "Backup the switch configuration"
- "Save network config"

**Status Checks:**
- "Check network status"
- "Show switch status"
- "What's the network doing?"

**Port Information:**
- "Show port status"
- "What ports are active?"
- "Network port information"

**Backup History:**
- "Show backup history"
- "When was last backup?"
- "Network backup log"

---

## 📊 Dashboard Features

### **Network Monitor Widget (Top-Left Dashboard)**

Shows:
- 🌐 **Status** - Switch online/offline
- 🔌 **Ports Active** - e.g., "8/10"
- 💾 **Last Backup** - Timestamp

**Widget Buttons:**
- **View** - Detailed switch information
- **Control** - Backup now, view logs, configure

### **System Console Commands**

Type directly in dashboard console:
```
network:backup          # Trigger backup
network:status          # Get switch status
network:ports           # Show all ports
network:history         # View backup history
```

---

## 🤖 Integration with Other Systems

Network monitor works with all GABRIEL systems:

**Example Multi-System Commands:**

```
"Backup network and notify family"
→ Backs up switch, then sends MyFamily AI notification

"Check network status and log to NOIZYLAB"
→ Gets switch status, logs to NOIZYLAB operations

"Backup network then upload to Drive"
→ Backs up config, uploads to Google Drive

"Run health check on everything including network"
→ Checks all systems + network switch
```

**From Dashboard Console:**
```javascript
system:orchestrate {
    name: "Network Maintenance",
    steps: [
        { system: 'network', action: 'backup' },
        { system: 'family', action: 'notify', params: { message: 'Network backup complete' } }
    ]
}
```

---

## 📈 Automation Options

### **Automated Daily Backups**

**Option 1: Crontab (macOS/Linux)**
```bash
# Edit crontab
crontab -e

# Add line for daily 3 AM backup
0 3 * * * /usr/bin/python3 /Users/rsp_ms/GABRIEL/network_backup.py
```

**Option 2: LaunchAgent (macOS)**
Create `~/Library/LaunchAgents/com.gabriel.network-backup.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.gabriel.network-backup</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/rsp_ms/GABRIEL/network_backup.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>3</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
</dict>
</plist>
```

Load with: `launchctl load ~/Library/LaunchAgents/com.gabriel.network-backup.plist`

---

## 🔐 Security Best Practices

1. **Change Default Password**
   - Update `PASSWORD` in `network_backup.py`
   - Use strong password (12+ characters)

2. **Keep Switch Private**
   - Don't expose switch to internet
   - Use only on private network

3. **Secure Backup Files**
   - Backups contain sensitive config
   - Set proper file permissions:
     ```bash
     chmod 700 System/NetworkBackups
     chmod 600 System/NetworkBackups/*.cfg
     ```

4. **Regular Security Updates**
   - Keep switch firmware updated
   - Update Python packages:
     ```bash
     pip3 install --upgrade -r System/requirements.txt
     ```

---

## 🐛 Troubleshooting

### **Problem: "Connection refused" when backing up**

**Solutions:**
1. Check switch IP: `ping 192.168.0.2`
2. Verify switch web interface accessible in browser
3. Check credentials in `network_backup.py`
4. Ensure switch firmware 6.10+ installed

### **Problem: Dashboard shows "Disconnected"**

**This is normal!**
- Dashboard works with mock data if backend not running
- Start `network_service.py` for real data
- Widget still functional in mock mode

### **Problem: Permission denied when running script**

**Solution:**
```bash
chmod +x start_gabriel.sh
chmod +x network_backup.py
```

### **Problem: Module not found errors**

**Solution:**
```bash
cd /Users/rsp_ms/GABRIEL/System
pip3 install -r requirements.txt
```

### **Problem: Backup file not created**

**Check:**
1. Look for errors in console output
2. View log: `cat System/NetworkBackups/backup_log.txt`
3. Verify credentials are correct
4. Test API manually:
   ```bash
   curl -u admin:password http://192.168.0.2/cgi-bin/DownloadCfg.cgi -o test.cfg
   ```

---

## 📂 Backup Management

### **View Backups:**
```bash
ls -lh System/NetworkBackups/DGS1210_CFG_*.cfg
```

### **View Backup Log:**
```bash
tail -20 System/NetworkBackups/backup_log.txt
```

### **Restore a Backup:**
1. Log into switch web interface
2. Go to Management → Restore Configuration
3. Upload `.cfg` file
4. Reboot switch

### **Clean Old Backups:**
Script auto-keeps last 10 backups. To change:

Edit `network_backup.py` line 63:
```python
prune_old_backups(keep_last=20)  # Keep more backups
```

---

## 🎯 Real-World Scenarios

### **Scenario 1: Pre-Update Backup**
```
Voice: "GABRIEL, backup network"
Action: Saves config before making changes
Result: Safe rollback point if needed
```

### **Scenario 2: Daily Health Check**
```
Voice: "What's network status?"
Action: Shows switch health, port status
Result: Catch issues early
```

### **Scenario 3: Automated Maintenance**
```
Cron: Runs backup at 3 AM daily
Script: Auto-prunes old backups
Log: Records all actions
```

### **Scenario 4: Integrated Workflow**
```
Voice: "Backup network and notify team"
Action: Multi-system orchestration
1. Backs up switch config
2. Uploads to Google Drive
3. Sends MyFamily AI notification
Result: Complete automated workflow
```

---

## 📊 Monitoring Tips

1. **Weekly Reviews**
   - Check backup logs weekly
   - Verify backups are completing
   - Review port status changes

2. **Monthly Tests**
   - Test a backup restore (lab switch)
   - Verify all credentials still work
   - Update firmware if available

3. **Alert Setup**
   - Set up email notifications (future enhancement)
   - Monitor backup failure patterns
   - Track port up/down events

4. **Documentation**
   - Document what's on each port
   - Note any special VLAN configs
   - Keep firmware version records

---

## 🔄 System Architecture

```
┌─────────────────────────────────────────────┐
│        GABRIEL WebAvatar Interface          │
│     (Voice, Dashboard, 3D Avatar)           │
└────────────────┬────────────────────────────┘
                 │
         Voice: "Backup network"
                 │
┌────────────────▼────────────────────────────┐
│         Integration Hub                     │
│   Routes "network:backup" command           │
└────────────────┬────────────────────────────┘
                 │
          HTTP POST Request
                 │
┌────────────────▼────────────────────────────┐
│      Network Service (Flask API)            │
│         localhost:5010                      │
└────────────────┬────────────────────────────┘
                 │
      Executes network_backup.py
                 │
┌────────────────▼────────────────────────────┐
│      network_backup.py Script               │
│   Connects to switch via HTTP API           │
└────────────────┬────────────────────────────┘
                 │
       HTTP GET with auth
                 │
┌────────────────▼────────────────────────────┐
│       DGS-1210-10 Switch                    │
│    192.168.0.2:80/cgi-bin/DownloadCfg.cgi  │
└────────────────┬────────────────────────────┘
                 │
      Returns .cfg file
                 │
┌────────────────▼────────────────────────────┐
│   System/NetworkBackups/                    │
│   DGS1210_CFG_2025-11-11_14-30-00.cfg      │
└─────────────────────────────────────────────┘
```

---

## 📚 Additional Resources

### **DGS-1210-10 Documentation**
- [D-Link Support Site](https://support.dlink.com)
- Firmware updates
- CLI reference guide

### **GABRIEL Documentation**
- `INTEGRATION_GUIDE.md` - Full system integration
- `QUICK_REFERENCE.md` - Command reference
- `MASTER_INTEGRATION.md` - System overview

### **Python Libraries**
- [Requests Documentation](https://requests.readthedocs.io)
- [Flask Documentation](https://flask.palletsprojects.com)

---

## ✅ Verification Checklist

Before production use:

- [ ] Updated switch credentials in `network_backup.py`
- [ ] Tested manual backup: `python3 network_backup.py`
- [ ] Verified backup file created in `System/NetworkBackups/`
- [ ] Checked backup log for errors
- [ ] Started network service successfully
- [ ] Confirmed dashboard shows network widget
- [ ] Tested voice command: "backup network"
- [ ] Set up automated daily backups (optional)
- [ ] Secured backup directory permissions
- [ ] Documented network port assignments

---

## 🎉 You're All Set!

Your DGS-1210-10 switch is now monitored and backed up by GABRIEL!

**Start now:**
```bash
cd /Users/rsp_ms/GABRIEL
./start_gabriel.sh
```

**Try saying:**
- "GABRIEL, backup the network"
- "Check network status"
- "Show port status"

**Your network is now part of your AI command center! 🌐🚀**
