# HP-OMEN Remote Desktop Setup Guide

## Overview
This guide enables remote access to your HP-OMEN machine via RDP, SSH, and alternative methods.

## Method 1: Windows Remote Desktop Protocol (RDP)

### Quick Setup (Windows 10/11 Pro, Enterprise, Education)

#### Enable RDP:
1. **Right-click "This PC"** or **"My Computer"** → **Properties**
2. Click **"Advanced system settings"**
3. Go to **"Remote" tab**
4. Check **"Allow remote connections to this computer"**
5. Click **Apply** → **OK**

#### Via Settings (Windows 10/11):
1. Open **Settings** → **System** → **Remote Desktop**
2. Toggle **"Enable Remote Desktop"** to ON
3. Note your computer name and IP address

#### Via PowerShell (Admin):
```powershell
# Enable RDP
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections" -Value 0

# Add firewall rule
netsh advfirewall firewall add rule name="Allow RDP" dir=in action=allow protocol=tcp localport=3389

# Verify RDP status
Get-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections"
```

### Finding Your Connection Details

```powershell
# Get hostname
$env:COMPUTERNAME

# Get IP address
ipconfig | findstr "IPv4"

# Get network info
Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -notlike "127.*"}
```

## Method 2: SSH Remote Access

### Prerequisites
- Windows 10+ build 1809 or later
- Or: Install OpenSSH from Microsoft Store / GitHub

### Enable SSH Server (Windows):
```powershell
# As Administrator
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Start SSH service
Start-Service sshd
Set-Service -Name sshd -StartupType Automatic

# Allow through firewall
New-NetFirewallRule -Name sshd -DisplayName 'SSH Server' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```

### Connect via SSH:
```bash
# From macOS/Linux
ssh username@hp-omen-ip-address

# Specify custom port (if changed)
ssh -p 2222 username@hp-omen-ip-address
```

## Method 3: Wake-on-LAN (WOL) + Remote Access

### Enable Wake-on-LAN:
1. **Device Manager** → **Network adapters**
2. Right-click your network adapter → **Properties**
3. Go to **Power Management** tab
4. Check **"Allow this device to wake the computer"**
5. Also check **"Only allow a magic packet to wake the computer"** (optional)

### Find MAC Address:
```powershell
# Get MAC address
Get-NetAdapter | Select-Object Name, MacAddress
```

### Wake Machine from macOS:
```bash
# Using wakeonlan tool (install via brew)
brew install wakeonlan
wakeonlan AA:BB:CC:DD:EE:FF  # Replace with MAC address
```

## Method 4: Third-Party Solutions

### Option A: TeamViewer
- Download: https://www.teamviewer.com
- Benefits: Works through NAT/firewalls, cross-platform
- Setup: Install and create account

### Option B: Chrome Remote Desktop
- Extension: https://chrome.google.com/webstore
- Benefits: Browser-based, Google account required
- Setup: Install extension and enable remote connections

### Option C: AnyDesk
- Download: https://anydesk.com
- Benefits: Low latency, simple setup
- Setup: Install and follow prompts

## HP-OMEN Specific Settings

### Optimize for Remote Desktop:
```powershell
# Enable hardware acceleration for better performance
Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Services\TermService' -name "fUseHardwarePerformance" -Value 1

# Allow multiple connections (Pro/Enterprise)
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v MaxConnectionsPerUser /t REG_DWORD /d 2 /f
```

### Adjust Graphics for Remote Session:
When connecting via RDP, in the connection dialog:
- Display tab → Color depth: 32-bit
- Experience tab → Disable: Wallpaper, Animations, Themes
- Enable: Persistent Bitmap Caching

## Network Configuration

### Port Forwarding (If accessing externally):
1. **Router Admin Panel** (usually 192.168.1.1 or 192.168.0.1)
2. Find **Port Forwarding** settings
3. Forward external port 3389 → HP-OMEN internal IP:3389
4. ⚠️ **Security**: Change default port or use VPN

### Static IP Setup:
```powershell
# Get network info
Get-NetAdapter | Select-Object InterfaceIndex, Name

# Set static IP
New-NetIPAddress -InterfaceIndex 4 -IPAddress 192.168.1.100 -PrefixLength 24 -DefaultGateway 192.168.1.1
```

## Security Best Practices

### 🔒 Critical:
1. **Change default RDP port** from 3389
2. **Use strong password** (20+ characters)
3. **Enable Network Level Authentication (NLA)**
4. **Keep Windows updated**
5. **Use VPN** for external access

### Enable NLA:
```powershell
# Verify NLA is enabled
Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name "SecurityLayer"
# Should return: 2 (SSL/TLS) or 1 (RDP)
```

### Change RDP Port:
```powershell
# Change to port 3390
Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name "PortNumber" -Value 3390

# Restart service
Restart-Service TermService

# Update firewall
Remove-NetFirewallRule -Name "Allow RDP" -ErrorAction SilentlyContinue
New-NetFirewallRule -Name "Allow RDP Custom" -DisplayName 'RDP Port 3390' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 3390
```

## Troubleshooting

### RDP Connection Refused:
```powershell
# Verify RDP is enabled
Get-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections"
# Should return: 0 (enabled)

# Restart service
Restart-Service TermService

# Check firewall
Get-NetFirewallRule -DisplayName "*RDP*"
```

### SSH Not Working:
```powershell
# Check service status
Get-Service sshd | Select-Object Status, StartType

# Start service
Start-Service sshd

# Check firewall rule
Get-NetFirewallRule -Name "sshd"
```

### Slow Connection:
1. Reduce color depth in RDP client
2. Disable visual themes and wallpaper
3. Check network bandwidth
4. Move closer to router (if using WiFi)
5. Use wired Ethernet for better performance

## Remote Connection Commands

### From macOS (RDP):
```bash
# Using Microsoft Remote Desktop app
open "rdp://username@hp-omen-ip:3389"

# Or use mstsc equivalent on Mac
/Applications/Microsoft\ Remote\ Desktop.app/Contents/MacOS/Microsoft\ Remote\ Desktop
```

### From Linux (RDP):
```bash
# Using rdesktop
rdesktop -u username -p password hp-omen-ip:3389

# Using freerdp
xfreerdp /v:hp-omen-ip:3389 /u:username
```

### SSH Tunnel for RDP:
```bash
# Create secure tunnel
ssh -L 3389:localhost:3389 username@hp-omen-ip

# Then connect RDP client to localhost:3389
```

## Aliases & Shortcuts

Add to your `~/.zsh_aliases`:
```bash
# HP-OMEN Remote Access
alias omen-rdp="open 'rdp://username@192.168.1.100:3389'"
alias omen-ssh="ssh username@192.168.1.100"
alias omen-wake="wakeonlan AA:BB:CC:DD:EE:FF"
alias omen-info="ssh username@192.168.1.100 'ipconfig | grep IPv4'"
```

## Verification Checklist

- [ ] RDP enabled on HP-OMEN
- [ ] SSH service running (if using SSH)
- [ ] Firewall rules added
- [ ] Static IP configured
- [ ] Strong password set
- [ ] Network Level Authentication enabled
- [ ] Tested connection from remote machine
- [ ] Port forwarding configured (if external access needed)
- [ ] VPN ready for external connections

---

**Last Updated**: December 7, 2025
**Repository**: https://github.com/Noizyfish/NOIZYLAB
