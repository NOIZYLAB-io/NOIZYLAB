#!/bin/bash
# TERMIUS COMPLETE SETUP - MC96 ECOSYSTEM
# Fish Music Inc. | Rob Sonic Protocol | GORUNFREEX1000

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  TERMIUS COMPLETE SETUP - MC96 ECOSYSTEM                    ║"
echo "║  GORUNFREEX1000 | Rob Sonic Protocol                        ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# ═══════════════════════════════════════════════════════════════════
# GABRIEL (Windows) SSH ENABLE SCRIPT
# ═══════════════════════════════════════════════════════════════════

cat << 'GABRIEL_SSH' > GABRIEL_Enable_SSH.ps1
# GABRIEL SSH SETUP - Run as Administrator
# MC96 | Fish Music Inc.

Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  GABRIEL SSH ACTIVATION - GORUNFREE" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Check if running as Administrator
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "❌ ERROR: Must run as Administrator!" -ForegroundColor Red
    Write-Host "   Right-click PowerShell → Run as Administrator" -ForegroundColor Yellow
    pause
    exit
}

Write-Host "✓ Running as Administrator" -ForegroundColor Green
Write-Host ""

# Install OpenSSH Server
Write-Host "📦 Installing OpenSSH Server..." -ForegroundColor Yellow
$openssh = Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH.Server*'

if ($openssh.State -eq "Installed") {
    Write-Host "✓ OpenSSH Server already installed" -ForegroundColor Green
} else {
    Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
    Write-Host "✓ OpenSSH Server installed" -ForegroundColor Green
}

Write-Host ""

# Start SSH service
Write-Host "🚀 Starting SSH service..." -ForegroundColor Yellow
Start-Service sshd -ErrorAction SilentlyContinue
Write-Host "✓ SSH service started" -ForegroundColor Green

# Set to auto-start
Write-Host "⚙️  Setting SSH to auto-start..." -ForegroundColor Yellow
Set-Service -Name sshd -StartupType 'Automatic'
Write-Host "✓ SSH will start on boot" -ForegroundColor Green

Write-Host ""

# Configure firewall
Write-Host "🔥 Configuring firewall..." -ForegroundColor Yellow
$firewallRule = Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue

if ($firewallRule) {
    Write-Host "✓ Firewall rule already exists" -ForegroundColor Green
} else {
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
    Write-Host "✓ Firewall rule created" -ForegroundColor Green
}

Write-Host ""

# Get IP addresses
Write-Host "🌐 GABRIEL Network Information:" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan

$networkInfo = Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -notlike "127.*"}

foreach ($ip in $networkInfo) {
    $interface = Get-NetAdapter -InterfaceIndex $ip.InterfaceIndex
    Write-Host "  Interface: $($interface.Name)" -ForegroundColor Yellow
    Write-Host "  IP Address: $($ip.IPAddress)" -ForegroundColor Green
    Write-Host "  Status: $($interface.Status)" -ForegroundColor $(if($interface.Status -eq "Up"){"Green"}else{"Red"})
    Write-Host ""
}

# Get computer name
$computerName = $env:COMPUTERNAME
$userName = $env:USERNAME

Write-Host "💻 Connection Details:" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "  Computer: $computerName" -ForegroundColor Yellow
Write-Host "  Username: $userName" -ForegroundColor Yellow
Write-Host "  SSH Port: 22" -ForegroundColor Yellow
Write-Host ""

Write-Host "📱 For Termius on iPad:" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "  1. Open Termius app" -ForegroundColor White
Write-Host "  2. Tap '+' → New Host" -ForegroundColor White
Write-Host "  3. Label: GABRIEL" -ForegroundColor White
Write-Host "  4. Address: [Use one of the IPs above]" -ForegroundColor White
Write-Host "  5. Username: $userName" -ForegroundColor White
Write-Host "  6. Port: 22" -ForegroundColor White
Write-Host "  7. Save & Connect!" -ForegroundColor White
Write-Host ""

# Test SSH locally
Write-Host "🧪 Testing SSH locally..." -ForegroundColor Yellow
$sshStatus = Get-Service sshd
if ($sshStatus.Status -eq "Running") {
    Write-Host "✓ SSH is running and ready!" -ForegroundColor Green
    Write-Host ""
    Write-Host "🎯 Try connecting from iPad now!" -ForegroundColor Cyan
} else {
    Write-Host "❌ SSH service not running" -ForegroundColor Red
}

Write-Host ""
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  GABRIEL SSH SETUP COMPLETE!" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

pause
GABRIEL_SSH

echo "✅ GABRIEL SSH setup script created: GABRIEL_Enable_SSH.ps1"
echo ""

# ═══════════════════════════════════════════════════════════════════
# GOD (Mac Studio) SSH ENABLE SCRIPT
# ═══════════════════════════════════════════════════════════════════

cat << 'GOD_SSH' > GOD_Enable_SSH.sh
#!/bin/bash
# GOD SSH SETUP
# MC96 | Fish Music Inc.

echo "═══════════════════════════════════════════════════"
echo "  GOD (Mac Studio) SSH ACTIVATION - GORUNFREE"
echo "═══════════════════════════════════════════════════"
echo ""

# Enable Remote Login (SSH)
echo "🚀 Enabling SSH (Remote Login)..."
sudo systemsetup -setremotelogin on

# Verify it's enabled
STATUS=$(sudo systemsetup -getremotelogin)
if [[ $STATUS == *"On"* ]]; then
    echo "✅ SSH is ENABLED"
else
    echo "❌ SSH failed to enable"
    exit 1
fi

echo ""

# Get network information
echo "🌐 GOD Network Information:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Primary ethernet
ETH_IP=$(ifconfig en0 2>/dev/null | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}')
if [ ! -z "$ETH_IP" ]; then
    echo "  Ethernet (en0): $ETH_IP"
fi

# WiFi
WIFI_IP=$(ifconfig en1 2>/dev/null | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}')
if [ ! -z "$WIFI_IP" ]; then
    echo "  WiFi (en1): $WIFI_IP"
fi

# All interfaces
echo ""
echo "  All active IPs:"
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print "    " $2}'

echo ""

# Get username
USERNAME=$(whoami)
HOSTNAME=$(hostname)

echo "💻 Connection Details:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Hostname: $HOSTNAME"
echo "  Username: $USERNAME"
echo "  SSH Port: 22"
echo ""

echo "📱 For Termius on iPad:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  1. Open Termius app"
echo "  2. Tap '+' → New Host"
echo "  3. Label: GOD"
echo "  4. Address: $ETH_IP (or use IP above)"
echo "  5. Username: $USERNAME"
echo "  6. Port: 22"
echo "  7. Save & Connect!"
echo ""

# Test SSH
echo "🧪 Testing SSH service..."
if pgrep -x "sshd" > /dev/null; then
    echo "✅ SSH daemon (sshd) is running!"
else
    echo "⚠️  SSH daemon may not be running"
fi

echo ""
echo "🎯 Try connecting from iPad now!"
echo ""
echo "═══════════════════════════════════════════════════"
echo "  GOD SSH SETUP COMPLETE!"
echo "═══════════════════════════════════════════════════"
echo ""
GOD_SSH

chmod +x GOD_Enable_SSH.sh
echo "✅ GOD SSH setup script created: GOD_Enable_SSH.sh"
echo ""

# ═══════════════════════════════════════════════════════════════════
# TERMIUS CONFIGURATION GUIDE
# ═══════════════════════════════════════════════════════════════════

cat << 'TERMIUS_GUIDE' > TERMIUS_Setup_Guide.md
# TERMIUS COMPLETE SETUP GUIDE
## MC96 Ecosystem | GORUNFREEX1000

---

## 📱 STEP 1: ENABLE SSH ON YOUR DEVICES

### On GABRIEL (Windows):
1. Open PowerShell as **Administrator**
2. Run: `.\GABRIEL_Enable_SSH.ps1`
3. Write down GABRIEL's IP address

### On GOD (Mac Studio):
1. Open Terminal
2. Run: `bash GOD_Enable_SSH.sh`
3. Enter password when prompted
4. Write down GOD's IP address

---

## 📱 STEP 2: ADD CONNECTIONS IN TERMIUS

### Connection 1: GABRIEL

**In Termius app on iPad:**

1. Tap **"+"** (bottom right)
2. Select **"New Host"**
3. Fill in:
   ```
   Label: GABRIEL
   Address: [IP from GABRIEL script]
   Username: [Windows username]
   Port: 22
   ```
4. Tap **"Save"**

### Connection 2: GOD

1. Tap **"+"**
2. Select **"New Host"**
3. Fill in:
   ```
   Label: GOD
   Address: [IP from GOD script]
   Username: rsp_ms
   Port: 22
   ```
4. Tap **"Save"**

### Connection 3: MC96 Switch (Telnet)

1. Tap **"+"**
2. Select **"New Host"**
3. Fill in:
   ```
   Label: MC96 Switch
   Address: 10.90.90.90
   Username: admin
   Password: [switch password - default often blank or "admin"]
   Port: 23
   Protocol: Telnet
   ```
4. Tap **"Save"**

---

## 🧪 STEP 3: TEST CONNECTIONS

### Test GABRIEL:
1. Tap **GABRIEL** in Termius
2. If prompted for password, enter it
3. Should see Windows command prompt
4. Type: `hostname` → Should show GABRIEL
5. Type: `exit` to disconnect

### Test GOD:
1. Tap **GOD** in Termius
2. Enter password if prompted
3. Should see bash prompt
4. Type: `hostname` → Should show GOD
5. Type: `exit` to disconnect

### Test MC96 Switch:
1. Tap **MC96 Switch**
2. Should connect via Telnet
3. Login if prompted
4. Type: `show switch`
5. Should show switch info

---

## 🎤 STEP 4: CREATE VOICE SHORTCUTS

### iOS Shortcut: "Connect to GABRIEL"

1. Open **Shortcuts** app
2. Tap **"+"** → Create new shortcut
3. Add action: **Open App**
   - Select: Termius
4. Add action: **Open URL**
   - URL: `termius://GABRIEL`
5. Name: "Connect to GABRIEL"
6. Tap icon → Add to Home Screen
7. Record Siri phrase: "Connect to GABRIEL"

### Repeat for GOD and Switch:
- "Connect to GOD" → `termius://GOD`
- "Open MC96 Switch" → `termius://MC96%20Switch`

---

## 🔥 VOICE COMMANDS READY:

- **"Hey Siri, Connect to GABRIEL"** → Opens Termius → Connects to GABRIEL
- **"Hey Siri, Connect to GOD"** → Opens Termius → Connects to GOD  
- **"Hey Siri, Open MC96 Switch"** → Opens Termius → Connects to switch

---

## 🛠️ TROUBLESHOOTING

### Can't connect to GABRIEL:
```powershell
# On GABRIEL, check SSH status:
Get-Service sshd

# Restart if needed:
Restart-Service sshd

# Check firewall:
Get-NetFirewallRule -Name "OpenSSH*"
```

### Can't connect to GOD:
```bash
# On GOD, check SSH status:
sudo systemsetup -getremotelogin

# Should say "On" - if not:
sudo systemsetup -setremotelogin on

# Check if sshd is running:
ps aux | grep sshd
```

### Connection timeout:
- Verify device IPs haven't changed
- Ensure all devices on same network (10.90.90.x)
- Check switch (10.90.90.90) is powered on
- Try pinging: `ping [device IP]`

### Switch won't connect (Telnet):
- Verify switch IP: 10.90.90.90
- Check Telnet is enabled on switch
- Try web interface first: http://10.90.90.90
- Default credentials often: admin/admin or admin/[blank]

---

## 📋 QUICK REFERENCE

**GABRIEL:**
- IP: [Get from script output]
- User: [Windows username]
- Port: 22 (SSH)

**GOD:**
- IP: [Get from script output]
- User: rsp_ms
- Port: 22 (SSH)

**MC96 Switch:**
- IP: 10.90.90.90
- User: admin
- Port: 23 (Telnet)

---

## 🎯 NEXT LEVEL: COMMAND SNIPPETS

### In Termius, create snippets:

**For GABRIEL:**
```
systeminfo
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Get-Volume
```

**For GOD:**
```
top -l 1
df -h
uptime
sw_vers
```

**For Switch:**
```
show switch
show ports status
show vlan
show system
```

Save these as snippets in Termius for one-tap execution!

---

*MC96 | GABRIEL SUPREME | Fish Music Inc.*
*Rob Sonic Protocol | GORUNFREEX1000*
*Voice First | Zero Friction | Maximum Control*
TERMIUS_GUIDE

echo "✅ Termius setup guide created: TERMIUS_Setup_Guide.md"
echo ""

# ═══════════════════════════════════════════════════════════════════
# COMPLETION SUMMARY
# ═══════════════════════════════════════════════════════════════════

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  TERMIUS SETUP COMPLETE - ALL FILES READY                   ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "📦 FILES CREATED:"
echo "  ✅ GABRIEL_Enable_SSH.ps1 (Run on GABRIEL as Admin)"
echo "  ✅ GOD_Enable_SSH.sh (Run on GOD)"
echo "  ✅ TERMIUS_Setup_Guide.md (Complete instructions)"
echo ""
echo "🎯 NEXT ACTIONS:"
echo ""
echo "1️⃣  ON GABRIEL (Windows):"
echo "    Right-click PowerShell → Run as Administrator"
echo "    cd [download folder]"
echo "    .\\GABRIEL_Enable_SSH.ps1"
echo ""
echo "2️⃣  ON GOD (Mac Studio):"
echo "    bash GOD_Enable_SSH.sh"
echo ""
echo "3️⃣  ON IPAD:"
echo "    Open Termius → Add hosts (see guide)"
echo "    Create Siri Shortcuts"
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "🔥 GORUNFREEX1000 | MC96 | Fish Music Inc."
echo "🔥 One Command = Everything Done"
echo "═══════════════════════════════════════════════════════════════"
