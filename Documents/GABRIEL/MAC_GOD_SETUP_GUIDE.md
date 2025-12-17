# 🖥️ GOD Mac Studio Setup Guide

## Overview

Complete setup script for Mac Studio (GOD) with:
- ☁️ **OneDrive** installation & configuration
- 🌐 **SMB Server** for network file sharing
- 🔄 **Auto-Sync** from Projects → OneDriveSync
- ⚙️ **System Optimization** for server use

---

## Quick Start

```bash
cd /Users/rsp_ms/GABRIEL
bash setup_mac_god.sh

# Select option 1 (Full Setup)
```

---

## Features

### 1. OneDrive Installation
- Installs OneDrive via Homebrew
- Creates `~/OneDriveSync` folder
- Checks if OneDrive is running
- Provides sign-in instructions

### 2. SMB Network Sharing
- Sets NetBIOS name to "MacStudio"
- Enables SMB server
- Configures file sharing
- Access via: `smb://MacStudio` or `smb://[IP]`

### 3. Automated Sync
- **Method**: LaunchAgent (better than Folder Actions)
- **Source**: `~/Projects`
- **Destination**: `~/OneDriveSync`
- **Frequency**: Every 5 minutes
- **Features**: 
  - Incremental sync (only changed files)
  - Excludes: `.DS_Store`, `node_modules`, `.git`, `*.pyc`, `__pycache__`
  - Preserves timestamps
  - Deletes removed files

### 4. System Optimization
- Sets computer name: "MacStudio"
- Disables sleep (always-on server)
- Display sleep: 10 minutes
- Optional SSH access

---

## Menu Options

```
1. Full Setup (All features)           ← Recommended first time
2. Install OneDrive only
3. Configure SMB only
4. Setup Auto-Sync only
5. System Preferences only
6. Show Status                         ← Check everything
7. Test Sync Now                       ← Manual sync
8. View Logs                           ← Troubleshooting
9. Exit
```

---

## File Structure

```
Mac Studio (GOD)
├── ~/Projects/                         ← Your working files
│   └── [syncs to OneDriveSync]
│
├── ~/OneDriveSync/                     ← Sync staging
│   └── [syncs to OneDrive]
│
├── ~/OneDrive/                         ← OneDrive cloud folder
│   └── [Microsoft manages]
│
└── ~/Library/
    ├── Scripts/
    │   └── sync_to_onedrive.sh        ← Sync script
    │
    ├── LaunchAgents/
    │   └── com.macstudio.onedrive.sync.plist
    │
    └── Logs/
        ├── mac_god_setup.log          ← Setup log
        ├── onedrive_sync.log          ← Sync log
        ├── onedrive_sync_out.log      ← Stdout
        └── onedrive_sync_error.log    ← Stderr
```

---

## Sync Flow

```
┌─────────────┐     Every 5 min     ┌────────────────┐
│  ~/Projects │ ──────rsync──────▶  │ ~/OneDriveSync │
└─────────────┘                      └────────────────┘
                                            │
                                            │ OneDrive App
                                            │ (automatic)
                                            ▼
                                     ┌──────────────┐
                                     │ ☁️ OneDrive  │
                                     │   Cloud      │
                                     └──────────────┘
```

**Why two steps?**
- OneDrive monitors `~/OneDrive` folder only
- Your `~/Projects` can be anywhere
- `~/OneDriveSync` bridges the gap
- Keeps your workspace clean

---

## Usage Examples

### First Time Setup

```bash
# 1. Run full setup
bash setup_mac_god.sh
# Select: 1 (Full Setup)

# 2. Sign in to OneDrive
# Open: /Applications/OneDrive.app
# Sign in with Microsoft account

# 3. Configure OneDrive sync
# In OneDrive settings:
# - Choose folders to sync
# - Select ~/OneDriveSync folder

# 4. Create Projects folder
mkdir -p ~/Projects

# 5. Test sync
# Add file to ~/Projects
echo "test" > ~/Projects/test.txt
# Wait 5 minutes or use option 7 (Test Sync Now)
# Check ~/OneDriveSync/test.txt
```

### Daily Usage

```bash
# Check status
bash setup_mac_god.sh
# Select: 6 (Show Status)

# Manual sync
bash setup_mac_god.sh
# Select: 7 (Test Sync Now)

# View recent syncs
bash setup_mac_god.sh
# Select: 8 (View Logs)

# Or directly:
tail -f ~/Library/Logs/onedrive_sync.log
```

### Network Access (from other machines)

```bash
# macOS/Linux
open smb://MacStudio

# Windows
\\MacStudio

# Or by IP
smb://192.168.0.X  # (check status for IP)
```

---

## Sync Script Details

**Location**: `~/Library/Scripts/sync_to_onedrive.sh`

**What it does**:
```bash
rsync -av --delete \
    --exclude='.DS_Store' \
    --exclude='node_modules' \
    --exclude='.git' \
    --exclude='*.pyc' \
    --exclude='__pycache__' \
    ~/Projects/ ~/OneDriveSync/
```

**Options**:
- `-a`: Archive mode (preserves permissions, timestamps)
- `-v`: Verbose (logs details)
- `--delete`: Remove files deleted from source
- `--exclude`: Skip unnecessary files

**Run manually**:
```bash
bash ~/Library/Scripts/sync_to_onedrive.sh
```

---

## LaunchAgent Details

**Location**: `~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist`

**Schedule**: Every 5 minutes (300 seconds)

**Control commands**:
```bash
# Check status
launchctl list | grep onedrive

# Stop service
launchctl unload ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist

# Start service
launchctl load ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist

# Restart service
launchctl unload ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist
launchctl load ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist

# View service info
launchctl list com.macstudio.onedrive.sync
```

**Change sync interval**:
```bash
# Edit plist
nano ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist

# Find:
<key>StartInterval</key>
<integer>300</integer>

# Change 300 to desired seconds:
# 60 = 1 minute
# 300 = 5 minutes (default)
# 600 = 10 minutes
# 1800 = 30 minutes

# Reload
launchctl unload ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist
launchctl load ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist
```

---

## SMB Sharing Details

**NetBIOS Name**: MacStudio

**Access from**:
- macOS: `smb://MacStudio` (Finder → Go → Connect to Server)
- Windows: `\\MacStudio` (File Explorer address bar)
- Linux: `smb://MacStudio` (Files → Other Locations)

**Shared folders** (configured in System Preferences):
```bash
# Open Sharing preferences
open "x-apple.systempreferences:com.apple.preferences.sharing"

# Or manually:
System Preferences → Sharing → File Sharing
```

**Add shared folder**:
1. System Preferences → Sharing
2. Enable "File Sharing"
3. Click "+" under Shared Folders
4. Select folder (e.g., ~/OneDriveSync)
5. Set permissions for users

---

## Troubleshooting

### OneDrive not syncing

```bash
# Check if OneDrive is running
pgrep -x "OneDrive"

# Launch if not running
open /Applications/OneDrive.app

# Check OneDrive status
# Click OneDrive icon in menu bar → Preferences
```

### Auto-sync not working

```bash
# Check if service is running
launchctl list | grep onedrive

# Check logs
tail -50 ~/Library/Logs/onedrive_sync.log
tail -50 ~/Library/Logs/onedrive_sync_error.log

# Test sync manually
bash ~/Library/Scripts/sync_to_onedrive.sh

# Restart service
launchctl unload ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist
launchctl load ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist
```

### SMB not accessible

```bash
# Check if SMB is running
sudo launchctl list | grep smb

# Restart SMB
sudo launchctl kickstart -k system/com.apple.smbd

# Check firewall
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate

# Get IP address
ipconfig getifaddr en0
# Try: smb://[IP_ADDRESS]

# Check computer name
scutil --get ComputerName
scutil --get LocalHostName
```

### Projects not syncing

```bash
# Check if folders exist
ls -la ~/Projects
ls -la ~/OneDriveSync

# Check permissions
ls -ld ~/Projects ~/OneDriveSync

# Test sync manually
bash ~/Library/Scripts/sync_to_onedrive.sh

# Watch sync in real-time
tail -f ~/Library/Logs/onedrive_sync.log
```

### Homebrew issues

```bash
# Update Homebrew
brew update

# Check Homebrew doctor
brew doctor

# Reinstall OneDrive
brew uninstall --cask onedrive
brew install --cask onedrive
```

---

## Advanced Configuration

### Exclude additional files from sync

Edit: `~/Library/Scripts/sync_to_onedrive.sh`

Add more `--exclude` lines:
```bash
rsync -av --delete \
    --exclude='.DS_Store' \
    --exclude='node_modules' \
    --exclude='.git' \
    --exclude='*.pyc' \
    --exclude='__pycache__' \
    --exclude='*.tmp' \          # Add this
    --exclude='*.log' \          # Add this
    --exclude='build/' \         # Add this
    ~/Projects/ ~/OneDriveSync/
```

### Sync multiple folders

Create additional LaunchAgents with different sources:

```bash
# Copy existing plist
cp ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist \
   ~/Library/LaunchAgents/com.macstudio.documents.sync.plist

# Edit new plist
nano ~/Library/LaunchAgents/com.macstudio.documents.sync.plist

# Change Label and script path
# Then create corresponding sync script

# Load new service
launchctl load ~/Library/LaunchAgents/com.macstudio.documents.sync.plist
```

### Email notifications on sync errors

Install `msmtp` or use built-in `mail`:

```bash
# Add to sync script
if [ $? -ne 0 ]; then
    echo "Sync failed at $(date)" | mail -s "OneDrive Sync Failed" your@email.com
fi
```

### Webhook notifications

Add to sync script:
```bash
# On success
curl -X POST https://your-webhook.com/sync-success \
    -d "status=success&time=$(date)"

# On failure
curl -X POST https://your-webhook.com/sync-failed \
    -d "status=failed&time=$(date)"
```

---

## Monitoring & Maintenance

### Check sync activity

```bash
# Real-time log
tail -f ~/Library/Logs/onedrive_sync.log

# Recent syncs
tail -20 ~/Library/Logs/onedrive_sync.log

# Error logs
tail -20 ~/Library/Logs/onedrive_sync_error.log

# Count syncs today
grep "$(date +%Y-%m-%d)" ~/Library/Logs/onedrive_sync.log | wc -l
```

### Disk space monitoring

```bash
# Check folder sizes
du -sh ~/Projects
du -sh ~/OneDriveSync
du -sh ~/OneDrive

# Detailed breakdown
du -h ~/Projects | sort -h | tail -20
```

### Network statistics

```bash
# Check network connections
netstat -an | grep ESTABLISHED

# Monitor network usage (requires sudo)
sudo nettop

# Check SMB connections
sudo lsof -i :445
```

### System health

```bash
# CPU usage
top -l 1 | grep "CPU usage"

# Memory usage
top -l 1 | grep PhysMem

# Disk usage
df -h

# Uptime
uptime
```

---

## Uninstall / Cleanup

```bash
# Stop sync service
launchctl unload ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist

# Remove LaunchAgent
rm ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist

# Remove sync script
rm ~/Library/Scripts/sync_to_onedrive.sh

# Uninstall OneDrive
brew uninstall --cask onedrive

# Remove folders (optional)
rm -rf ~/OneDriveSync

# Disable SMB
sudo launchctl unload /System/Library/LaunchDaemons/com.apple.smbd.plist

# Reset computer name (optional)
sudo scutil --set ComputerName "Mac-Studio"
sudo scutil --set HostName "Mac-Studio"
sudo scutil --set LocalHostName "Mac-Studio"
```

---

## Security Notes

### File Permissions
- Sync script preserves original permissions
- OneDrive may modify permissions for cloud storage
- Test with sensitive files before production use

### Network Security
- SMB traffic is not encrypted by default
- Use VPN for remote access
- Configure firewall rules appropriately
- Consider enabling SMB signing:
  ```bash
  sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server SigningRequired -bool true
  ```

### Password Protection
- Script does not store OneDrive credentials
- OneDrive uses system keychain
- SMB shares require user authentication

---

## Backup Strategy

**Recommended 3-2-1 approach**:
1. **Original**: ~/Projects (working files)
2. **Sync copy**: ~/OneDriveSync (staging)
3. **Cloud backup**: OneDrive (offsite)

**Additional backups**:
- Time Machine: Local backup disk
- Carbon Copy Cloner: Bootable backup
- Backblaze: Additional cloud backup

---

## Integration with GABRIEL

```bash
# Add to gabriel_ultimate.py
>>> sync onedrive    # Trigger manual sync
>>> sync status      # Check sync status
>>> sync logs        # View recent syncs

# Add to WebAvatar dashboard
# - OneDrive sync status widget
# - Last sync timestamp
# - Sync error alerts
```

---

## Performance Optimization

### Reduce sync frequency (lower CPU usage)
```bash
# Change from 5 minutes to 15 minutes
nano ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist
# Set StartInterval to 900 (15 minutes)
```

### Exclude large files
```bash
# Add to sync script
--exclude='*.iso' \
--exclude='*.dmg' \
--exclude='*.zip' \
--exclude='videos/' \
```

### Sync only during work hours
Replace `StartInterval` with `StartCalendarInterval`:
```xml
<key>StartCalendarInterval</key>
<dict>
    <key>Hour</key>
    <integer>9</integer>  <!-- 9 AM -->
    <key>Minute</key>
    <integer>0</integer>
</dict>
```

---

## FAQ

**Q: Do I need OneDriveSync folder if I use OneDrive directly?**
A: Yes, if you want to sync from ~/Projects. OneDrive only monitors ~/OneDrive by default.

**Q: Can I sync to Dropbox or Google Drive instead?**
A: Yes, modify the sync script destination to ~/Dropbox or ~/Google Drive.

**Q: What if I have multiple Macs?**
A: Each Mac can sync to same OneDrive folder. Use different NetBIOS names.

**Q: Does this work with OneDrive Business?**
A: Yes, same process. Sign in with work account.

**Q: Can I pause sync temporarily?**
A: Yes: `launchctl unload ~/Library/LaunchAgents/com.macstudio.onedrive.sync.plist`

**Q: How do I sync faster?**
A: Reduce StartInterval or run manual sync.

---

## Summary

✅ **Installed**: OneDrive via Homebrew
✅ **Configured**: SMB sharing as "MacStudio"  
✅ **Created**: Auto-sync every 5 minutes
✅ **Optimized**: System for server use
✅ **Monitored**: Logs and status tracking

**Access Mac remotely**: `smb://MacStudio`
**Check sync status**: `bash setup_mac_god.sh` → Option 6
**Manual sync**: `bash setup_mac_god.sh` → Option 7

---

**Created**: November 11, 2025
**Version**: 1.0
**Status**: Production Ready 🚀
