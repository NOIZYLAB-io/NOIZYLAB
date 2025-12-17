# 🌐 Network Monitor Integration - Quick Start

## What You Have

GABRIEL can now monitor and backup your DGS-1210-10 network switch!

## 📦 Files Created

1. **`network_backup.py`** - Python script to backup switch configuration
2. **`System/network_service.py`** - Flask API backend for web integration
3. **`WebAvatar/js/network-monitor.js`** - Frontend network monitoring
4. **Updated Integration Hub** - Added network commands
5. **Updated Dashboard** - Added network widget

## 🚀 Quick Start

### Option 1: Use Without Backend (Mock Mode)
Just start GABRIEL - network widget shows mock data:
```bash
cd /Users/rsp_ms/GABRIEL/WebAvatar
python3 -m http.server 8000
# Open: http://localhost:8000
```

### Option 2: Full Integration (Real Data)

**Terminal 1 - Start Network Service:**
```bash
cd /Users/rsp_ms/GABRIEL/System
pip3 install flask flask-cors requests
python3 network_service.py
# Runs on http://localhost:5010
```

**Terminal 2 - Start GABRIEL:**
```bash
cd /Users/rsp_ms/GABRIEL/WebAvatar
python3 -m http.server 8000
# Open: http://localhost:8000
```

## 🔧 Configuration

### 1. Update Switch Credentials

Edit `network_backup.py`:
```python
SWITCH_IP = "192.168.0.2"              # Your switch IP
USERNAME = "admin"                      # Your username
PASSWORD = "YOUR_SECURE_PASSWORD"       # Your password
```

### 2. Test Backup Manually

```bash
cd /Users/rsp_ms/GABRIEL
python3 network_backup.py
```

Check: `/Users/rsp_ms/GABRIEL/System/NetworkBackups/`

## 🎤 Voice Commands

Once configured, you can say:

```
"GABRIEL, backup the network"
"Check network status"
"Show me switch status"
"What's the port status?"
"Backup switch configuration"
```

## 📊 Dashboard Widget

The Network Monitor widget shows:
- ✅ **Status** - Switch online/offline
- 🔌 **Ports Active** - Active ports (e.g., 8/10)
- 💾 **Last Backup** - Time of last backup

**Widget Controls:**
- **View** - Detailed switch analysis
- **Control** - Backup now, view logs, configure

## 🔐 Security Notes

1. **Change default password** in `network_backup.py`
2. **Switch should be on private network** (not exposed to internet)
3. **Backups stored locally** at `/Users/rsp_ms/GABRIEL/System/NetworkBackups/`
4. **Keeps last 10 backups** (auto-prunes older ones)

## 🐛 Troubleshooting

### Switch Not Responding
- Verify switch IP: `ping 192.168.0.2`
- Check switch web interface accessible
- Ensure firmware 6.10+ installed

### Backup Script Fails
- Check credentials in `network_backup.py`
- Verify `requests` library installed: `pip3 install requests`
- Check backup log: `System/NetworkBackups/backup_log.txt`

### Dashboard Shows "Disconnected"
- Normal if backend not running (uses mock data)
- Start `network_service.py` for real integration
- Check console (F12) for connection errors

## 📂 File Structure

```
GABRIEL/
├── network_backup.py              # Main backup script
├── System/
│   ├── network_service.py         # Flask API backend
│   └── NetworkBackups/            # Backup storage
│       ├── DGS1210_CFG_*.cfg     # Config backups
│       └── backup_log.txt         # Backup history
└── WebAvatar/
    └── js/
        └── network-monitor.js     # Frontend integration
```

## 🎯 Usage Examples

### Automated Daily Backup

Add to crontab:
```bash
# Run backup daily at 3 AM
0 3 * * * /usr/bin/python3 /Users/rsp_ms/GABRIEL/network_backup.py
```

### Manual Backup via GABRIEL

**Voice:** "Backup the network"
**Dashboard Console:** `network:backup`
**Direct:** `python3 network_backup.py`

### Check Switch Health

**Voice:** "What's the network status?"
**Dashboard:** Click "View" on Network widget
**Console:** `network:status`

## 💡 Pro Tips

1. **Test backup weekly** - Ensure configs are current
2. **Monitor port status** - Catch unexpected disconnections
3. **Review backup logs** - Check for any failures
4. **Keep firmware updated** - For best compatibility
5. **Document your network** - Note what's on each port

## 🔗 Integration with Other Systems

Network monitor integrates with:
- **NOIZYLAB** - Can trigger network ops from workflows
- **MyFamily AI** - Notify family of network changes
- **TechTool** - Run network diagnostics
- **Chief Architect** - Include in system health reports

Example multi-system command:
```
"GABRIEL, backup network and notify family when complete"
```

## 📖 API Reference

### Backend Endpoints (localhost:5010)

```
GET  /api/network/status              # Service health
POST /api/network/backup              # Trigger backup
GET  /api/network/switch/{ip}         # Switch status
GET  /api/network/switch/{ip}/ports   # Port status
GET  /api/network/history             # Backup history
```

### Frontend Commands

```javascript
// Execute from browser console (F12)
app.integrationHub.executeCommand('network:backup')
app.integrationHub.executeCommand('network:status')
app.integrationHub.executeCommand('network:ports')
app.integrationHub.executeCommand('network:history')
```

## ✅ You're Ready!

Your network is now monitored by GABRIEL! 

**Test it:** Say "GABRIEL, check network status" 🌐
