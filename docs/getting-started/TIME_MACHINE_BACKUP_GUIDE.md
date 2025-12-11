# ⏰ TIME MACHINE BACKUP GUIDE
**Date:** November 19, 2025  
**Mission:** Complete backup before system reformat

---

## 🎯 BACKUP STRATEGY

### Phase 1: Ultra Deep Scan (RUNNING OVERNIGHT)
✓ **Status:** In Progress  
✓ **Scanning:** All drives for code, scripts, configs  
✓ **Output:** `/Volumes/4TB_02/CODE_MASTER/`

### Phase 2: Time Machine Backup (NOW)
✓ **Destination:** `/Volumes/TM_BackUp/`  
✓ **Purpose:** System-level backup of everything

---

## 📋 TIME MACHINE BACKUP STEPS

### 1. Verify Time Machine Drive
```bash
# Check TM_BackUp is mounted
ls -la /Volumes/TM_BackUp/

# Check available space
df -h /Volumes/TM_BackUp/
```

### 2. Configure Time Machine
**Via System Settings:**
1. Open **System Settings** → **General** → **Time Machine**
2. Click **"+"** to add backup disk
3. Select **TM_BackUp**
4. Click **Use Disk**
5. Enable **Back Up Automatically**

**Or via Terminal:**
```bash
# Set Time Machine destination
sudo tmutil setdestination /Volumes/TM_BackUp/

# Enable Time Machine
sudo tmutil enable

# Start backup immediately
sudo tmutil startbackup --block
```

### 3. Monitor Backup Progress
```bash
# Check backup status
tmutil status

# Watch progress in real-time
while true; do
  clear
  echo "=== TIME MACHINE BACKUP STATUS ==="
  tmutil status
  echo ""
  echo "Press Ctrl+C to stop monitoring"
  sleep 10
done
```

### 4. Verify Backup After Completion
```bash
# List all backups
tmutil listbackups

# Check latest backup
tmutil latestbackup

# Verify backup integrity
tmutil verifychecksums /Volumes/TM_BackUp/
```

---

## 🔍 WHAT TIME MACHINE BACKS UP

✓ **System Files**
- macOS system files
- Applications
- System preferences
- User accounts

✓ **User Data**
- Documents
- Desktop
- Downloads
- Pictures, Music, Movies
- Mail, Contacts, Calendar

✓ **Application Data**
- Application settings
- Preferences
- Caches (selected)
- Saved games/states

✓ **Hidden Files**
- `.zshrc`, `.bashrc`
- SSH keys (`~/.ssh/`)
- GPG keys (`~/.gnupg/`)
- Git config (`~/.gitconfig`)

---

## ⚠️ WHAT TIME MACHINE EXCLUDES

❌ Excluded by default:
- `/Volumes/` (external drives - that's why we need CODE_MASTER!)
- Temporary files
- Trash
- Caches (most)
- Virtual machines (unless specified)
- Time Machine backups themselves

---

## 🎯 YOUR COMPLETE BACKUP STRATEGY

### Backup #1: CODE_MASTER (Ultra Deep Scan)
**Location:** `/Volumes/4TB_02/CODE_MASTER/`  
**Contains:**
- All Python code
- All shell scripts
- All Git repositories
- All configuration files
- All VS Code workspaces
- All documentation

**Why:** External drives not backed up by Time Machine

### Backup #2: Time Machine
**Location:** `/Volumes/TM_BackUp/`  
**Contains:**
- Complete system state
- All internal drive data
- Applications
- System settings
- User files

**Why:** System-level backup for full restore

### Result: COMPLETE COVERAGE ✓
- External code → CODE_MASTER
- System + internal files → Time Machine
- **NOTHING GETS LEFT BEHIND**

---

## 💾 ESTIMATED TIMES

### Time Machine First Backup
- **Small system (< 500GB):** 2-6 hours
- **Medium system (500GB-1TB):** 6-12 hours
- **Large system (1TB+):** 12-24 hours

**Note:** First backup is always the slowest. Incremental backups are much faster!

### Ultra Deep Scan
- **Running overnight:** 4-8 hours (normal for multi-TB drives)

---

## 📊 SPACE REQUIREMENTS

Check your space:
```bash
# System drive size
df -h /

# TM_BackUp available space
df -h /Volumes/TM_BackUp/

# CODE_MASTER usage
du -sh /Volumes/4TB_02/CODE_MASTER/
```

**Rule of Thumb:**
- Time Machine needs 2-3x your system drive size
- CODE_MASTER needs much less (code is small!)

---

## 🚀 RECOMMENDED OVERNIGHT PROCESS

### Tonight:
1. ✓ **Ultra Deep Scan** - RUNNING (let it finish)
2. ✓ **Start Time Machine Backup** - Start now
3. ✓ **Go to bed** - Let both run overnight

### Tomorrow Morning:
1. Check Ultra Deep Scan results
2. Verify Time Machine backup completed
3. Review CODE_MASTER contents
4. Run verification scripts
5. **READY TO REFORMAT** ✓

---

## 📝 QUICK START COMMANDS

### Start Time Machine Backup NOW:
```bash
# One command to start backup
sudo tmutil setdestination /Volumes/TM_BackUp/ && sudo tmutil startbackup --block
```

### Check Both Backups:
```bash
# Ultra Deep Scan status
tail -f /Volumes/4TB_02/CODE_MASTER/logs/ultra_scan_*.log

# Time Machine status
tmutil status
```

---

## ✅ PRE-REFORMAT CHECKLIST

Before reformatting, verify:

### CODE_MASTER
- [ ] Ultra Deep Scan completed
- [ ] Report generated at `/Volumes/4TB_02/CODE_MASTER/ULTRA_DEEP_SCAN_*.md`
- [ ] All critical code locations identified
- [ ] File lists created in `ultra_scan_results/`

### Time Machine
- [ ] First backup completed
- [ ] Backup visible in System Settings → Time Machine
- [ ] Can browse backup contents
- [ ] Latest backup timestamp is recent

### Double-Check
- [ ] Both backups accessible
- [ ] 4TB_02 drive safely disconnected or kept safe
- [ ] TM_BackUp drive safely stored
- [ ] No active work with unsaved changes

---

## 🆘 TROUBLESHOOTING

### Time Machine Won't Start
```bash
# Reset Time Machine
sudo tmutil disable
sudo tmutil enable
sudo tmutil startbackup
```

### Time Machine Running Slow
- Normal for first backup
- Close heavy applications
- Disable other disk-intensive tasks
- Let it run overnight

### Backup Failed
```bash
# Check logs
log show --predicate 'subsystem == "com.apple.TimeMachine"' --last 1h

# Verify disk
diskutil verifyVolume /Volumes/TM_BackUp/

# Try again
sudo tmutil startbackup --block
```

---

## 📱 MONITORING FROM ANOTHER DEVICE

### SSH into your Mac:
```bash
ssh your-username@your-mac-ip

# Check both processes
ps aux | grep ULTRA_DEEP_SCAN
tmutil status
```

---

## 🎊 SUCCESS INDICATORS

### Morning Status:
```
✓ Ultra Deep Scan report exists
✓ Time Machine shows "Latest Backup: [Recent Date]"
✓ No error messages
✓ Both backup drives accessible
✓ CODE_MASTER populated with code
✓ TM_BackUp showing backup snapshots
```

---

## 🚀 AFTER REFORMAT

### Restore from Time Machine:
1. Boot into Recovery Mode (Cmd+R at startup)
2. Select "Restore from Time Machine Backup"
3. Choose TM_BackUp drive
4. Select latest backup
5. Follow prompts

### Restore CODE_MASTER:
1. Connect 4TB_02 drive
2. Copy code back from CODE_MASTER to desired locations
3. Verify Git repos, Python environments, etc.

---

**Status:** Ready to execute  
**Next:** Start Time Machine backup and let both run overnight  
**Tomorrow:** Verify both backups and prepare for reformat ✓
