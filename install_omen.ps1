# 🔥 OMEGA SYSTEM - HP-OMEN INSTALLER 🔥
# Fish Music Inc - CB_01
# Run as Administrator on HP-OMEN

Write-Host ""
Write-Host "╔═══════════════════════════════════════════════════════════════╗"
Write-Host "║                                                               ║"
Write-Host "║       🔥 OMEGA BRAIN - HP-OMEN INSTALLER 🔥                   ║"
Write-Host "║                                                               ║"
Write-Host "║              GABRIEL ↔ OMEN SUPER-MESH                       ║"
Write-Host "║                 Fish Music Inc - CB_01                        ║"
Write-Host "║                                                               ║"
Write-Host "╚═══════════════════════════════════════════════════════════════╝"
Write-Host ""

# Check admin
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "❌ This script requires Administrator privileges"
    Write-Host "   Right-click → Run as Administrator"
    pause
    exit
}

Write-Host "✅ Running as Administrator"
Write-Host ""

# ==================== PHASE 1: CORE PACKAGES ====================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
Write-Host "📦 PHASE 1: INSTALLING CORE PACKAGES"
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
Write-Host ""

Write-Host "[1/7] Installing Python..."
winget install -e --id Python.Python.3.11 --silent

Write-Host "[2/7] Installing Node.js..."
winget install -e --id OpenJS.NodeJS --silent

Write-Host "[3/7] Installing Task..."
winget install -e --id Task.Task --silent

Write-Host "[4/7] Installing Redis..."
winget install -e --id Redis.Redis --silent

Write-Host "[5/7] Installing Git..."
winget install -e --id Git.Git --silent

Write-Host "[6/7] Installing Python packages..."
pip install ray chromadb sentence-transformers watchdog scikit-learn paho-mqtt psutil pydantic

Write-Host "[7/7] Installing Syncthing..."
winget install -e --id Syncthing.Syncthing --silent

Write-Host ""
Write-Host "✅ Core packages installed!"
Write-Host ""

# ==================== PHASE 2: NETWORK CONFIGURATION ====================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
Write-Host "🌐 PHASE 2: NETWORK CONFIGURATION"
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
Write-Host ""

Write-Host "⚠️  MANUAL STEP REQUIRED:"
Write-Host ""
Write-Host "Set Jumbo Frames on Network Adapter:"
Write-Host "  1. Control Panel → Network Adapters"
Write-Host "  2. Right-click your Ethernet → Properties"
Write-Host "  3. Configure → Advanced"
Write-Host "  4. Find 'Jumbo Packet' or 'Jumbo Frame'"
Write-Host "  5. Set to: 9014 bytes"
Write-Host "  6. Click OK"
Write-Host "  7. Reboot Windows"
Write-Host ""
pause

# Enable SMB Multichannel
Write-Host "[+] Enabling SMB Multichannel..."
Set-SmbClientConfiguration -EnableMultiChannel $true -Force

Write-Host "✅ SMB optimized!"
Write-Host ""

# ==================== PHASE 3: CREATE SCRIPTS ====================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
Write-Host "📝 PHASE 3: CREATING HELPER SCRIPTS"
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
Write-Host ""

# Mount GABRIEL script
$mountScript = @'
@echo off
REM 📁 Mount GABRIEL as Z: drive
echo Mounting GABRIEL share...
net use Z: /delete /yes 2>nul
net use Z: \\gabriel.local\NoizyShare /persistent:yes

if %ERRORLEVEL% EQU 0 (
    echo ✅ Z: drive mounted!
    echo    GABRIEL files accessible at Z:\
) else (
    echo ❌ Mount failed
    echo    Check: GABRIEL File Sharing enabled
)
pause
'@
$mountScript | Out-File -FilePath "$env:USERPROFILE\Desktop\mount_gabriel.bat" -Encoding ASCII

# Start Ray worker script
$rayScript = @'
@echo off
REM 🧠 Start Ray worker
echo Starting Ray worker...
echo Connecting to GABRIEL...

REM Replace with actual GABRIEL IP
set GABRIEL_IP=192.168.1.100

ray start --address=%GABRIEL_IP%:6379 --num-cpus=14 --num-gpus=1

if %ERRORLEVEL% EQU 0 (
    echo ✅ Ray worker connected!
    echo    Check dashboard: http://%GABRIEL_IP%:8265
) else (
    echo ❌ Connection failed
    echo    Check: GABRIEL Ray cluster running
)
pause
'@
$rayScript | Out-File -FilePath "$env:USERPROFILE\Desktop\start_ray_worker.bat" -Encoding ASCII

# Omega start script (Windows version)
$omegaScript = @'
@echo off
REM 🔥 OMEGA BRAIN - OMEN STARTUP

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║         🔥 OMEGA BRAIN - OMEN SERVICES STARTING 🔥            ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

REM Start Redis
echo [1/3] Starting Redis...
start /B redis-server
timeout /t 2 /nobreak >nul
echo       ✅ Redis online

REM Start Syncthing
echo [2/3] Starting Syncthing...
start /B syncthing -no-browser
timeout /t 2 /nobreak >nul
echo       ✅ Syncthing online

REM Connect to Ray cluster
echo [3/3] Connecting to Ray cluster...
set GABRIEL_IP=192.168.1.100
ray start --address=%GABRIEL_IP%:6379
echo       ✅ Ray worker connected

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║              🚀 OMEN SERVICES ONLINE 🚀                       ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo 🔥 GORUNFREE! 🎸🔥
echo.
pause
'@
$omegaScript | Out-File -FilePath "$env:USERPROFILE\Desktop\omega_start_omen.bat" -Encoding ASCII

Write-Host "✅ Scripts created on Desktop:"
Write-Host "   • mount_gabriel.bat"
Write-Host "   • start_ray_worker.bat"
Write-Host "   • omega_start_omen.bat"
Write-Host ""

# ==================== PHASE 4: OPENSSH SERVER ====================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
Write-Host "🔐 PHASE 4: SSH SERVER"
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
Write-Host ""

Write-Host "[+] Enabling OpenSSH Server..."
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

Write-Host "[+] Starting SSH service..."
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

Write-Host "✅ SSH server enabled and running!"
Write-Host ""

# ==================== COMPLETE ====================
Write-Host ""
Write-Host "╔═══════════════════════════════════════════════════════════════╗"
Write-Host "║                                                               ║"
Write-Host "║              ✅ OMEN INSTALLATION COMPLETE! ✅                 ║"
Write-Host "║                                                               ║"
Write-Host "╠═══════════════════════════════════════════════════════════════╣"
Write-Host "║                                                               ║"
Write-Host "║  Next Steps:                                                  ║"
Write-Host "║  1. REBOOT Windows (for jumbo frames)                         ║"
Write-Host "║  2. Run: mount_gabriel.bat                                    ║"
Write-Host "║  3. Run: omega_start_omen.bat                                 ║"
Write-Host "║  4. Install Tailscale: https://tailscale.com/download         ║"
Write-Host "║                                                               ║"
Write-Host "╚═══════════════════════════════════════════════════════════════╝"
Write-Host ""
Write-Host "🔥 GORUNFREE! 🎸🔥"
Write-Host ""
pause
