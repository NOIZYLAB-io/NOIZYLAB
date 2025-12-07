# Persistent Boot Startup Installation Guide

## M2Ultra (macOS) - LaunchAgent Setup

### Automatic Installation:
```bash
# Copy startup script
mkdir -p ~/.local/bin
cp scripts/m2ultra-boot-startup.sh ~/.local/bin/
chmod +x ~/.local/bin/m2ultra-boot-startup.sh

# Install LaunchAgent
mkdir -p ~/Library/LaunchAgents
cp Library/LaunchAgents/com.noizylab.m2ultra.boot.plist ~/Library/LaunchAgents/

# Enable the LaunchAgent
launchctl load ~/Library/LaunchAgents/com.noizylab.m2ultra.boot.plist

# Verify installation
launchctl list | grep m2ultra
```

### Manual Setup:
1. Create `~/.local/bin/m2ultra-boot-startup.sh`
2. Create `~/Library/LaunchAgents/com.noizylab.m2ultra.boot.plist`
3. Run: `launchctl load ~/Library/LaunchAgents/com.noizylab.m2ultra.boot.plist`

### Verify It's Running:
```bash
# Check log
tail -f ~/.m2ultra-boot.log

# List active agents
launchctl list | grep noisy

# Test manually
~/.local/bin/m2ultra-boot-startup.sh
```

### Troubleshooting M2Ultra:
```bash
# Reload the agent
launchctl unload ~/Library/LaunchAgents/com.noizylab.m2ultra.boot.plist
launchctl load ~/Library/LaunchAgents/com.noizylab.m2ultra.boot.plist

# Check for errors
log stream --predicate 'eventMessage contains[c] "m2ultra"' --level debug

# Manually test
zsh ~/.local/bin/m2ultra-boot-startup.sh
```

---

## HP-OMEN (Windows) - Task Scheduler Setup

### Option 1: Automatic via PowerShell (Recommended):
```powershell
# Run as Administrator
cd C:\Users\Gabriel\NOIZYLAB\scripts

# Import the task
Register-ScheduledTask -Xml (Get-Content HP-OMEN-Task-Scheduler.xml | Out-String) -TaskName "HP-OMEN Boot Startup" -Force

# Enable the task
Enable-ScheduledTask -TaskName "HP-OMEN Boot Startup"

# Verify
Get-ScheduledTask -TaskName "HP-OMEN Boot Startup"
```

### Option 2: Manual via Task Scheduler UI:
1. Open **Task Scheduler**
2. Click **Create Basic Task** → Name: "HP-OMEN Boot Startup"
3. **Trigger**: "At startup"
4. **Action**: 
   - Program: `powershell.exe`
   - Arguments: `-NoProfile -ExecutionPolicy Bypass -File "C:\path\to\HP-OMEN-boot-startup.ps1"`
5. **Conditions**: Check "Wake the computer to run this task"
6. Click **OK**

### Option 3: Startup Folder (Simplest):
```powershell
# Copy startup script to Startup folder
Copy-Item HP-OMEN-boot-startup.ps1 -Destination "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\"

# Rename to .cmd wrapper
@"
@echo off
powershell -NoProfile -ExecutionPolicy Bypass -File "%APPDATA%\NOIZYLAB\HP-OMEN-boot-startup.ps1"
"@ | Out-File "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\OMEN-Boot.cmd"
```

### Verify It's Running (Windows):
```powershell
# Check Task Scheduler history
Get-ScheduledTaskInfo -TaskName "HP-OMEN Boot Startup"

# View last run status
Get-ScheduledTask -TaskName "HP-OMEN Boot Startup" | Select-Object @{Name="Status";Expression={$_.State}}

# Test manually
powershell -ExecutionPolicy Bypass -File "C:\path\to\HP-OMEN-boot-startup.ps1"
```

### Troubleshooting HP-OMEN:
```powershell
# Disable and re-enable task
Disable-ScheduledTask -TaskName "HP-OMEN Boot Startup"
Enable-ScheduledTask -TaskName "HP-OMEN Boot Startup"

# Check event logs
Get-WinEvent -LogName System | Where-Object {$_.ProviderName -eq "Task Scheduler"} | Select-Object TimeCreated, Message | Head -20

# Run task manually
Start-ScheduledTask -TaskName "HP-OMEN Boot Startup"

# Check execution policy
Get-ExecutionPolicy -Scope CurrentUser
```

---

## What Runs on Boot

### M2Ultra:
✅ SSH server enabled  
✅ Screen Sharing (VNC) activated  
✅ Environment variables set  
✅ Aliases loaded  
✅ Network drives mount attempts  
✅ System info logged  

### HP-OMEN:
✅ RDP service verified/started  
✅ SSH service verified/started  
✅ Network drives mounted  
✅ Desktop shortcut created  
✅ System info displayed  
✅ Ready for M2Ultra connection  

---

## Connection After Boot

### From M2Ultra to HP-OMEN:
```bash
# SSH
ssh username@omen-ip

# VNC (if configured on OMEN)
open vnc://omen-ip
```

### From HP-OMEN to M2Ultra:
```powershell
# SSH from OMEN PowerShell
ssh m2ultra@m2ultra-ip

# Or use the desktop shortcut created by boot script
```

---

## Disable Boot Startup (If Needed)

### M2Ultra:
```bash
launchctl unload ~/Library/LaunchAgents/com.noizylab.m2ultra.boot.plist
```

### HP-OMEN:
```powershell
Disable-ScheduledTask -TaskName "HP-OMEN Boot Startup"
```

---

**Status**: ✅ Ready for persistent boot configuration  
**Last Updated**: December 7, 2025
