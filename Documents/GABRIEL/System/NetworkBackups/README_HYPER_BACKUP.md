# 🌐 DGS-1210-10 HYPER BACKUP UTILITY v3.0

## 🚀 Enterprise-Grade Network Infrastructure Protection

### **What's New in v3.0**

This is the **ULTIMATE** version of the DGS-1210-10 backup utility with advanced enterprise features!

---

## ✨ Features

### **Core Backup**
- ✅ **HTTP API Integration** - Direct download from switch
- ✅ **Automatic Scheduling** - Run via cron/systemd
- ✅ **Multi-Format Export** - CFG, JSON metadata
- ✅ **Intelligent Pruning** - Keep last N backups

### **Advanced Features (v3.0)**
- ✨ **Change Detection** - Skip backup if no changes
- ✨ **Diff Generation** - See exactly what changed
- ✨ **SHA256 Hashing** - Verify backup integrity
- ✨ **Gzip Compression** - Automatic archiving
- ✨ **Health Monitoring** - Pre-backup switch checks
- ✨ **Webhook Notifications** - Alert on success/failure
- ✨ **State Tracking** - Remember last backup hash
- ✨ **Rollback Support** - Keep archives for recovery

---

## 📦 Installation

### **1. Create Directory Structure**
```bash
mkdir -p /Users/rsp_ms/GABRIEL/System/NetworkBackups/{archives,diffs}
cd /Users/rsp_ms/GABRIEL/System/NetworkBackups
```

### **2. Download Script**
```bash
# Script already created at:
# /Users/rsp_ms/GABRIEL/System/NetworkBackups/dgs1210_backup.py
chmod +x dgs1210_backup.py
```

### **3. Configure Credentials**

**Option A: Edit script directly** (lines 39-41)
```python
SWITCH_IP = "192.168.0.2"           # Your switch IP
USERNAME = "admin"                   # Your username
PASSWORD = "YOUR_SECURE_PASSWORD"    # Change this!
```

**Option B: Use environment variables** (recommended)
```bash
export SWITCH_IP="192.168.0.2"
export SWITCH_USER="admin"
export SWITCH_PASS="your_password"
```

### **4. Test Run**
```bash
python3 dgs1210_backup.py
```

---

## 🎯 Usage

### **Basic Usage**
```bash
# Run backup manually
python3 dgs1210_backup.py

# Run with custom switch IP
SWITCH_IP="192.168.1.100" python3 dgs1210_backup.py

# Run with webhook notification
WEBHOOK_URL="https://hooks.example.com/notify" python3 dgs1210_backup.py
```

### **Expected Output**
```
================================================================================
🌐 DGS-1210-10 HYPER BACKUP UTILITY v3.0
================================================================================

ℹ️  Backup routine started
ℹ️  Target: 192.168.0.2
🏥  Running health check...
🏥  Health check passed
💾  Connecting to 192.168.0.2...
✅  Backup complete → DGS1210_CFG_2025-11-11_15-30-00.cfg (45821 bytes)
ℹ️  Metadata exported → DGS1210_CFG_2025-11-11_15-30-00.json
🔄  Configuration changes detected!
🔄  Diff generated → diff_20251111_153000.txt
ℹ️  Compressed → DGS1210_CFG_2025-11-11_15-30-00.cfg.gz
✅  Backup routine completed in 3.42s
ℹ️  Backups: 10 | Archives: 25

================================================================================
✅ Backup Complete!
================================================================================
```

---

## 📁 Directory Structure

```
NetworkBackups/
├── dgs1210_backup.py           # Main backup script (v3.0)
├── backup_log.txt              # All backup operations logged
├── .backup_state.json          # Last backup hash & metadata
│
├── DGS1210_CFG_*.cfg          # Recent backups (last 10)
├── DGS1210_CFG_*.json         # Backup metadata files
│
├── archives/
│   └── DGS1210_CFG_*.cfg.gz   # Compressed archives (last 30)
│
└── diffs/
    └── diff_*.txt              # Configuration change diffs
```

---

## ⚙️ Configuration

### **Environment Variables**

| Variable | Default | Description |
|----------|---------|-------------|
| `SWITCH_IP` | 192.168.0.2 | Switch IP address |
| `SWITCH_USER` | admin | Switch username |
| `SWITCH_PASS` | (required) | Switch password |
| `WEBHOOK_URL` | (none) | Notification webhook URL |

### **Script Constants**

Edit these in `dgs1210_backup.py`:

```python
# Retention
KEEP_BACKUPS = 10          # Keep last 10 uncompressed
KEEP_ARCHIVES = 30         # Keep last 30 compressed

# Timeouts
TIMEOUT = 30               # HTTP request timeout (seconds)

# Features
CHANGE_DETECTION = True    # Skip if no changes
DIFF_GENERATION = True     # Generate change diffs
HEALTH_CHECK = True        # Pre-backup health check
COMPRESSION_ENABLED = True # Compress archives
NOTIFICATIONS_ENABLED = False  # Webhook alerts
```

---

## 🔄 Change Detection

### **How It Works**

1. **First Run:**
   - Downloads config
   - Calculates SHA256 hash
   - Saves hash to `.backup_state.json`
   - Creates archive

2. **Subsequent Runs:**
   - Downloads new config
   - Calculates new hash
   - Compares with last hash
   - If **identical**: Skips archive, logs "no changes"
   - If **different**: Creates archive, generates diff

### **Benefits**
- 💾 Saves storage space
- ⚡ Faster backups
- 📊 Clear change history
- 🔍 Easy troubleshooting

### **Diff Example**
```diff
--- old/DGS1210_CFG_2025-11-10_12-00-00.cfg
+++ new/DGS1210_CFG_2025-11-11_15-30-00.cfg
@@ -45,7 +45,7 @@
 config ports 1 speed auto flow_control disable
-config ports 2 speed 100_full flow_control disable
+config ports 2 speed 1000_full flow_control disable
 config ports 3 speed auto flow_control disable
```

---

## 🏥 Health Monitoring

### **Pre-Backup Checks**

The script verifies:

1. **✅ Network Reachability**
   - Pings switch (ICMP)
   - Timeout: 2 seconds

2. **✅ Web Interface**
   - Checks HTTP access
   - Validates credentials

3. **✅ Backup Ready**
   - Both checks must pass

### **Health Check Output**
```
🏥  Running health check...
🏥  Health check passed
```

**If Failed:**
```
❌  Switch not ready for backup!
🏥  Reachable: ✅
🏥  Web Interface: ❌
```

---

## 📊 Metadata Export

Each backup generates a JSON metadata file:

**DGS1210_CFG_2025-11-11_15-30-00.json:**
```json
{
  "filename": "DGS1210_CFG_2025-11-11_15-30-00.cfg",
  "timestamp": "2025-11-11T15:30:00.123456",
  "size_bytes": 45821,
  "hash_sha256": "a1b2c3d4e5f6...",
  "switch_ip": "192.168.0.2",
  "version": "3.0"
}
```

**Use Cases:**
- Verify backup integrity
- Track backup history
- Automate restore scripts
- Audit compliance

---

## 🔔 Webhook Notifications

### **Enable Notifications**

```python
# In script
NOTIFICATIONS_ENABLED = True
WEBHOOK_URL = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
```

Or via environment:
```bash
WEBHOOK_URL="https://hooks.example.com/notify" python3 dgs1210_backup.py
```

### **Notification Payload**

**Success:**
```json
{
  "status": "success",
  "timestamp": "2025-11-11T15:30:00",
  "switch_ip": "192.168.0.2",
  "details": {
    "duration": 3.42,
    "backups": 10,
    "archives": 25,
    "changes_detected": true,
    "diff_file": "diff_20251111_153000.txt"
  }
}
```

**Failure:**
```json
{
  "status": "failed",
  "timestamp": "2025-11-11T15:30:00",
  "switch_ip": "192.168.0.2",
  "details": {
    "reason": "Switch not ready",
    "health": {
      "reachable": true,
      "web_interface": false,
      "backup_ready": false
    }
  }
}
```

---

## ⏰ Automated Scheduling

### **Cron (macOS/Linux)**

```bash
# Edit crontab
crontab -e

# Add daily backup at 3 AM
0 3 * * * cd /Users/rsp_ms/GABRIEL/System/NetworkBackups && /usr/bin/python3 dgs1210_backup.py >> /tmp/dgs1210_backup.log 2>&1

# With environment variables
0 3 * * * SWITCH_IP="192.168.0.2" SWITCH_USER="admin" SWITCH_PASS="password" /usr/bin/python3 /Users/rsp_ms/GABRIEL/System/NetworkBackups/dgs1210_backup.py
```

### **LaunchAgent (macOS)**

**~/Library/LaunchAgents/com.gabriel.dgs1210-backup.plist:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.gabriel.dgs1210-backup</string>
    
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/rsp_ms/GABRIEL/System/NetworkBackups/dgs1210_backup.py</string>
    </array>
    
    <key>EnvironmentVariables</key>
    <dict>
        <key>SWITCH_IP</key>
        <string>192.168.0.2</string>
        <key>SWITCH_USER</key>
        <string>admin</string>
        <key>SWITCH_PASS</key>
        <string>your_password</string>
    </dict>
    
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>3</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    
    <key>StandardOutPath</key>
    <string>/tmp/dgs1210_backup.log</string>
    
    <key>StandardErrorPath</key>
    <string>/tmp/dgs1210_backup.error.log</string>
</dict>
</plist>
```

**Load:**
```bash
launchctl load ~/Library/LaunchAgents/com.gabriel.dgs1210-backup.plist
launchctl start com.gabriel.dgs1210-backup
```

---

## 🔐 Security Best Practices

1. **Secure Credentials**
   ```bash
   # Use environment variables
   export SWITCH_PASS="$(security find-generic-password -a $USER -s switch_pass -w)"
   ```

2. **Restrict File Permissions**
   ```bash
   chmod 700 /Users/rsp_ms/GABRIEL/System/NetworkBackups
   chmod 600 /Users/rsp_ms/GABRIEL/System/NetworkBackups/*.cfg
   chmod 600 /Users/rsp_ms/GABRIEL/System/NetworkBackups/.backup_state.json
   ```

3. **Secure Switch Access**
   - Use HTTPS if available (modify URL in script)
   - Change default admin password
   - Restrict switch management to private network

4. **Log Security**
   ```bash
   chmod 600 backup_log.txt
   ```

---

## 🔄 Rollback / Restore

### **List Available Backups**
```bash
ls -lh DGS1210_CFG_*.cfg
```

### **Extract Archived Backup**
```bash
gunzip -c archives/DGS1210_CFG_2025-11-10_12-00-00.cfg.gz > restore.cfg
```

### **Restore to Switch**

**Via Web Interface:**
1. Log into switch web UI
2. Go to **Management → Restore Configuration**
3. Upload `.cfg` file
4. Reboot switch

**Via CLI (if available):**
```bash
# Upload via SCP
scp restore.cfg admin@192.168.0.2:/runtime/config.cfg

# Reboot switch
ssh admin@192.168.0.2 "reboot"
```

---

## 📊 Monitoring & Analytics

### **View Recent Backups**
```bash
ls -lht DGS1210_CFG_*.cfg | head -10
```

### **Check Backup Frequency**
```bash
grep "Backup complete" backup_log.txt | tail -20
```

### **Detect Configuration Changes**
```bash
ls -lht diffs/diff_*.txt | head -10
cat diffs/diff_20251111_153000.txt
```

### **Verify Backup Integrity**
```bash
# Check hash
python3 -c "import hashlib; print(hashlib.sha256(open('DGS1210_CFG_2025-11-11_15-30-00.cfg','rb').read()).hexdigest())"

# Compare with metadata
cat DGS1210_CFG_2025-11-11_15-30-00.json | grep hash_sha256
```

---

## 🐛 Troubleshooting

### **Problem: "Connection timeout"**

**Causes:**
- Switch offline
- Wrong IP address
- Network issue

**Solutions:**
```bash
# Test connectivity
ping -c 3 192.168.0.2

# Check switch web interface
curl -v http://192.168.0.2

# Increase timeout
# Edit script: TIMEOUT = 60
```

### **Problem: "HTTP 401 Unauthorized"**

**Causes:**
- Wrong username/password
- Credentials changed

**Solutions:**
```bash
# Test credentials manually
curl -u admin:password http://192.168.0.2/cgi-bin/DownloadCfg.cgi -o test.cfg

# Update credentials in script or env vars
```

### **Problem: "No configuration changes detected" every time**

**Causes:**
- `.backup_state.json` corrupted
- Hash calculation issue

**Solutions:**
```bash
# Reset state
rm .backup_state.json

# Force new backup
python3 dgs1210_backup.py
```

### **Problem: "Health check failed"**

**Causes:**
- ICMP blocked (firewall)
- Switch rebooting

**Solutions:**
```bash
# Disable health check temporarily
# Edit script: HEALTH_CHECK = False

# Or wait for switch to come online
```

---

## 📈 Performance & Limits

- **Backup Duration:** 2-5 seconds (typical)
- **File Size:** 40-50 KB (uncompressed)
- **Compressed Size:** 8-12 KB (75% reduction)
- **Network Impact:** Minimal (single HTTP request)
- **Storage:** ~500 KB for 10 backups + 30 archives

---

## 🔮 Future Enhancements

- [ ] HTTPS support
- [ ] Multi-switch support
- [ ] Email notifications
- [ ] Grafana integration
- [ ] Configuration validation
- [ ] Auto-rollback on errors
- [ ] Backup encryption
- [ ] Cloud storage sync (S3, Drive)

---

## 📚 Integration with GABRIEL

### **Network Service API**
```python
# In network_service.py
@app.route('/api/network/backup/hyper', methods=['POST'])
def trigger_hyper_backup():
    result = subprocess.run(['python3', 'NetworkBackups/dgs1210_backup.py'])
    return jsonify({'success': result.returncode == 0})
```

### **GABRIEL Ultimate Python**
```python
# In gabriel_ultimate.py
async def backup_network_hyper():
    subprocess.run(['python3', 'System/NetworkBackups/dgs1210_backup.py'])
```

---

## 🏆 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-10 | Initial release (basic backup) |
| 2.0 | 2025-11-11 | Added metadata, compression |
| 3.0 | 2025-11-11 | **Change detection, diffs, health checks, webhooks** |

---

## 📄 License

MIT License - Feel free to modify and distribute!

---

## 🤝 Support

**Issues?** Check:
1. Switch is powered on and accessible
2. Credentials are correct
3. Firewall allows HTTP access
4. Python 3.7+ installed
5. `requests` module installed: `pip3 install requests`

**Questions?** Check `backup_log.txt` for detailed error messages.

---

**🌟 GABRIEL DGS-1210-10 HYPER BACKUP v3.0 - Enterprise Network Protection! 🌟**
