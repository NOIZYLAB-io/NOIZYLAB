# M2Ultra Remote Desktop Setup Guide

## Quick Enable (Manual)

### Screen Sharing (Remote Desktop for macOS)
1. **System Settings** → **General** → **Sharing**
2. Enable **"Screen Sharing"**
3. Note the address shown (e.g., `vnc://192.168.1.x`)

### SSH Access
```bash
# Enable SSH via Terminal
sudo systemsetup -setremotelogin on

# Verify SSH is running
sudo systemsetup -getremotelogin
```

## Automated Setup

Run the setup script:
```bash
chmod +x scripts/setup-m2ultra-remote.sh
./scripts/setup-m2ultra-remote.sh
```

## Connection Methods

### From another Mac (Screen Sharing - VNC):
```bash
# Use command line
open vnc://192.168.1.100

# Or use Finder → Go → Connect to Server
cmd+k then vnc://hostname
```

### From Windows (RDP-style):
Install one of:
- **Microsoft Remote Desktop** (App Store)
- **VNC Viewer** (RealVNC)
- **Chrome Remote Desktop**

### SSH Connection (Any Platform):
```bash
ssh m2ultra@192.168.1.100
# or
ssh m2ultra@m2ultra.local
```

## Find M2Ultra Details

```bash
# Computer name
scutil --get ComputerName

# IP Address
ipconfig getifaddr en0

# Full network info
ifconfig
```

## Security Setup

### Change SSH Port (Optional):
```bash
# Edit SSH config
sudo nano /etc/ssh/sshd_config

# Find line: #Port 22
# Change to: Port 2222

# Restart SSH
sudo launchctl stop com.openssh.sshd
sudo launchctl start com.openssh.sshd
```

### Restrict Screen Sharing Access:
1. System Settings → Sharing → Screen Sharing
2. Click **Options**
3. Select **"Only these users:"**
4. Add specific users

### VNC Password:
1. System Settings → Sharing → Screen Sharing
2. Set VNC password for remote users

## Quick Aliases

Add to `~/.zsh_aliases`:
```bash
# M2Ultra Remote Access
alias m2-info="echo 'M2Ultra @ ' && ipconfig getifaddr en0 && echo 'SSH: ssh m2ultra@$(ipconfig getifaddr en0)'"
alias m2-vnc="open 'vnc://$(ipconfig getifaddr en0)'"
alias m2-stop-sharing="sudo systemsetup -setremotelogin off"
alias m2-start-sharing="sudo systemsetup -setremotelogin on"
```

## Access from Gabriel's HP-OMEN

From HP-OMEN to M2Ultra:
```powershell
# PowerShell - If using VNC Viewer or Chrome Remote Desktop
# Otherwise use SSH:
ssh m2ultra@[M2ULTRA_IP]
```

## Troubleshooting

### Screen Sharing not available:
```bash
# Re-enable via Terminal
sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart -activate -configure -access -on -users admin -privs -all -restart -agent -console
```

### SSH Not Working:
```bash
# Verify SSH is enabled
sudo systemsetup -getremotelogin

# Enable if needed
sudo systemsetup -setremotelogin on

# Check SSH daemon status
sudo launchctl list | grep ssh

# Restart SSH
sudo launchctl stop com.openssh.sshd
sudo launchctl start com.openssh.sshd
```

### Find M2Ultra on Network:
```bash
# Using Bonjour
dns-sd -B _ssh._tcp local

# Or ping
ping m2ultra.local
```

---

**Status**: ✅ Ready for remote access
**Last Updated**: December 7, 2025
