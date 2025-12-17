# 🕒 GABRIEL Network Backup - Cron Schedule Reference

## 📅 Your Cron Expression

```bash
0 3 * * 1 /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py
```

---

## 📖 What This Means

**Schedule:** Every Monday at 3:00 AM

**Breakdown:**
```
0       - Minute (0 = top of the hour)
3       - Hour (3 = 3 AM)
*       - Day of month (any day)
*       - Month (any month)
1       - Day of week (1 = Monday)
```

---

## 🚀 Quick Setup

### **Method 1: Interactive Setup (Recommended)**
```bash
cd /Users/rsp_ms/GABRIEL
chmod +x setup_cron.sh
./setup_cron.sh
# Select option 2 (Weekly - Monday at 3 AM)
```

### **Method 2: Manual Setup**
```bash
# Edit crontab
crontab -e

# Add this line:
0 3 * * 1 /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py >> /tmp/gabriel_network_backup.log 2>&1

# Save and exit (ESC, :wq, Enter)
```

### **Method 3: One-Line Install**
```bash
(crontab -l 2>/dev/null | grep -v "dgs1210_backup.py"; echo "0 3 * * 1 /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py >> /tmp/gabriel_network_backup.log 2>&1") | crontab -
```

---

## ✅ Verify Installation

### **Check if installed:**
```bash
crontab -l | grep dgs1210_backup
```

**Expected output:**
```
0 3 * * 1 /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py >> /tmp/gabriel_network_backup.log 2>&1
```

### **Test manually:**
```bash
python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py
```

---

## 📊 Schedule Variations

### **Daily at 3 AM:**
```bash
0 3 * * * /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py
```

### **Twice Weekly (Monday & Thursday at 3 AM):**
```bash
0 3 * * 1,4 /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py
```

### **Every 12 hours:**
```bash
0 */12 * * * /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py
```

### **Monthly (1st of month at 3 AM):**
```bash
0 3 1 * * /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py
```

### **Every Sunday at 2 AM:**
```bash
0 2 * * 0 /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py
```

---

## 🔍 Monitoring

### **View Logs:**
```bash
# Cron execution logs
tail -f /tmp/gabriel_network_backup.log

# Backup operation logs
tail -f /GABRIEL/System/NetworkBackups/backup_log.txt

# System cron logs (macOS)
grep CRON /var/log/system.log | tail -20

# System cron logs (Linux)
grep CRON /var/log/syslog | tail -20
```

### **Check Last Backup:**
```bash
ls -lht /GABRIEL/System/NetworkBackups/DGS1210_CFG_*.cfg | head -1
```

### **View Recent Backups:**
```bash
ls -lht /GABRIEL/System/NetworkBackups/DGS1210_CFG_*.cfg | head -10
```

---

## 🛠️ Management Commands

### **List all cron jobs:**
```bash
crontab -l
```

### **Edit crontab:**
```bash
crontab -e
```

### **Remove specific job:**
```bash
crontab -l | grep -v "dgs1210_backup.py" | crontab -
```

### **Remove all cron jobs (careful!):**
```bash
crontab -r
```

### **Backup crontab:**
```bash
crontab -l > ~/crontab_backup_$(date +%Y%m%d).txt
```

### **Restore crontab:**
```bash
crontab ~/crontab_backup_20251111.txt
```

---

## 🐛 Troubleshooting

### **Problem: Cron job not running**

**1. Check if cron service is running:**
```bash
# macOS - should always be running
ps aux | grep cron

# Linux
sudo service cron status
```

**2. Verify Python path:**
```bash
which python3
# Should output: /usr/bin/python3
# If different, update cron command
```

**3. Test script manually:**
```bash
/usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py
```

**4. Check permissions:**
```bash
ls -l /GABRIEL/System/NetworkBackups/dgs1210_backup.py
# Should be readable/executable
```

**5. Verify log directory is writable:**
```bash
touch /tmp/test.log && rm /tmp/test.log
```

### **Problem: No output in logs**

**Check if log file exists:**
```bash
ls -l /tmp/gabriel_network_backup.log
```

**Ensure redirect is in cron command:**
```bash
# Good:
0 3 * * 1 /usr/bin/python3 /path/to/script.py >> /tmp/backup.log 2>&1

# Bad (no logs):
0 3 * * 1 /usr/bin/python3 /path/to/script.py
```

### **Problem: Backup fails in cron but works manually**

**Reasons:**
- Environment variables not set (SWITCH_IP, SWITCH_PASS)
- PATH differences
- Working directory issues

**Solution:**
Create a wrapper script:

```bash
cat > /GABRIEL/System/NetworkBackups/cron_wrapper.sh << 'EOF'
#!/bin/bash
export SWITCH_IP="192.168.0.2"
export SWITCH_USER="admin"
export SWITCH_PASS="your_password"
cd /GABRIEL/System/NetworkBackups
/usr/bin/python3 dgs1210_backup.py
EOF

chmod +x /GABRIEL/System/NetworkBackups/cron_wrapper.sh
```

Then use in cron:
```bash
0 3 * * 1 /GABRIEL/System/NetworkBackups/cron_wrapper.sh >> /tmp/gabriel_network_backup.log 2>&1
```

---

## 🔐 Security Notes

### **Protect credentials:**

**Option 1: Environment variables in wrapper script**
```bash
#!/bin/bash
export SWITCH_PASS="$(security find-generic-password -a $USER -s gabriel_switch -w)"
python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py
```

**Option 2: Secure file with restricted permissions**
```bash
echo "SWITCH_PASS=your_password" > /GABRIEL/.env
chmod 600 /GABRIEL/.env

# In script, load from .env
```

### **Restrict log access:**
```bash
chmod 600 /tmp/gabriel_network_backup.log
```

---

## 📈 Advanced Features

### **Email on failure:**
```bash
0 3 * * 1 /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py || echo "Backup failed!" | mail -s "GABRIEL Backup Alert" admin@example.com
```

### **Success notification:**
```bash
0 3 * * 1 /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py && echo "Backup successful" | mail -s "GABRIEL Backup Success" admin@example.com
```

### **Run with timeout:**
```bash
0 3 * * 1 timeout 300 /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py
```
(Kills after 5 minutes if hung)

### **Lock to prevent overlapping runs:**
```bash
0 3 * * 1 flock -n /tmp/backup.lock /usr/bin/python3 /GABRIEL/System/NetworkBackups/dgs1210_backup.py
```

---

## 🎯 Cron Cheat Sheet

```
*     *     *     *     *
│     │     │     │     │
│     │     │     │     └─── Day of week (0-7, Sun=0 or 7)
│     │     │     └─────---- Month (1-12)
│     │     └───────────---- Day of month (1-31)
│     └─────────────────---- Hour (0-23)
└───────────────────────---- Minute (0-59)
```

**Special Characters:**
- `*` = Any value
- `,` = Multiple values (e.g., `1,3,5`)
- `-` = Range (e.g., `1-5`)
- `/` = Step (e.g., `*/2` = every 2)

**Examples:**
```bash
0 0 * * *       # Daily at midnight
0 */6 * * *     # Every 6 hours
30 14 * * 1-5   # Weekdays at 2:30 PM
0 0 1 * *       # Monthly on 1st at midnight
0 0 * * 0       # Weekly on Sunday at midnight
```

---

## 📞 Quick Help

**Use interactive setup:**
```bash
cd /Users/rsp_ms/GABRIEL
./setup_cron.sh
```

**Commands in setup script:**
- Options 1-5: Add scheduled backup
- Option 6: Remove scheduled backup
- Type `test`: Run manual test
- Type `logs`: View recent logs
- Type `next`: Show next run time

---

## ✅ Success Checklist

After setting up cron:

- [ ] Cron job shows in `crontab -l`
- [ ] Script is executable: `chmod +x dgs1210_backup.py`
- [ ] Switch credentials configured in script
- [ ] Manual test succeeds: `python3 dgs1210_backup.py`
- [ ] Log file created: `/tmp/gabriel_network_backup.log`
- [ ] Backup directory exists and writable
- [ ] Wait for scheduled time and verify backup runs
- [ ] Check logs after first automated run

---

## 🎉 You're All Set!

Your GABRIEL network backup will now run automatically:

```
📅 Every Monday at 3:00 AM
🌐 Backs up DGS-1210-10 switch configuration
💾 Saves to: /GABRIEL/System/NetworkBackups/
📝 Logs to: /tmp/gabriel_network_backup.log
```

**Monitor it:**
```bash
# Watch for next Monday 3 AM backup
tail -f /tmp/gabriel_network_backup.log
```

**Need help?** Use: `./setup_cron.sh`

---

**Last Updated:** November 11, 2025
**Your Schedule:** Every Monday at 3:00 AM ✅
