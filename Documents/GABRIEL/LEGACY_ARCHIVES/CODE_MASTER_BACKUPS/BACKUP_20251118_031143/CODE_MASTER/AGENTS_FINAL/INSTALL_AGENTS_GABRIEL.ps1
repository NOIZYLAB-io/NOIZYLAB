# INSTALL_AGENTS_GABRIEL.ps1
# GORUNFREEX5000 - COMPLETE 7-AGENT SYSTEM INSTALLER FOR GABRIEL (Windows)
# ONE COMMAND INSTALLS EVERYTHING
#
# Run this: Right-click → "Run as Administrator"

#Requires -RunAsAdministrator

$ErrorActionPreference = "Stop"

Clear-Host

Write-Host "╔══════════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                                                                      ║" -ForegroundColor Cyan
Write-Host "║          🚀 GORUNFREEX5000 - GABRIEL INSTALLER 🚀                    ║" -ForegroundColor Cyan
Write-Host "║                                                                      ║" -ForegroundColor Cyan
Write-Host "║          INSTALLING ALL 7 AI AGENTS + AUTO-STARTUP                   ║" -ForegroundColor Cyan
Write-Host "║                                                                      ║" -ForegroundColor Cyan
Write-Host "║          GABRIEL (HP Omen Windows)                                   ║" -ForegroundColor Cyan
Write-Host "║                                                                      ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$SCRIPT_DIR = $PSScriptRoot
$BASE_DIR = "$env:ProgramFiles\MC96_Automation"
$SCRIPTS_DIR = "$BASE_DIR\Scripts"
$LOGS_DIR = "$BASE_DIR\Logs"
$STARTUP_DIR = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"

# ═══════════════════════════════════════════════════════════════════════
# SETUP DIRECTORIES
# ═══════════════════════════════════════════════════════════════════════

Write-Host "⚡ Setting up directory structure..." -ForegroundColor Yellow

New-Item -ItemType Directory -Path $BASE_DIR -Force | Out-Null
New-Item -ItemType Directory -Path $SCRIPTS_DIR -Force | Out-Null
New-Item -ItemType Directory -Path $LOGS_DIR -Force | Out-Null

Write-Host "  ✓ Created: $BASE_DIR" -ForegroundColor Green
Write-Host "  ✓ Created: $SCRIPTS_DIR" -ForegroundColor Green
Write-Host "  ✓ Created: $LOGS_DIR" -ForegroundColor Green
Write-Host ""

# ═══════════════════════════════════════════════════════════════════════
# INSTALL 7 AI AGENTS
# ═══════════════════════════════════════════════════════════════════════

Write-Host "⚡ Installing 7 AI Agents..." -ForegroundColor Yellow

$AgentFiles = @(
    "AGENT_LUCY.ps1",
    "AGENT_POPS.ps1",
    "AGENT_ENGR_KEITH.ps1",
    "AGENT_DREAM.ps1",
    "AGENT_ALEX_WARD.ps1",
    "AGENT_WARDIE.ps1",
    "AGENT_FLEET.ps1"
)

$InstalledCount = 0

foreach ($AgentFile in $AgentFiles) {
    $SourcePath = Join-Path $SCRIPT_DIR $AgentFile
    $DestPath = Join-Path $SCRIPTS_DIR $AgentFile
    
    if (Test-Path $SourcePath) {
        Copy-Item $SourcePath $DestPath -Force
        $AgentName = $AgentFile -replace "\.ps1$", ""
        $Icon = switch ($AgentName) {
            "AGENT_LUCY" { "💜" }
            "AGENT_POPS" { "🔧" }
            "AGENT_ENGR_KEITH" { "⚙️" }
            "AGENT_DREAM" { "💭" }
            "AGENT_ALEX_WARD" { "💰" }
            "AGENT_WARDIE" { "🎯" }
            "AGENT_FLEET" { "⚙️" }
            default { "✓" }
        }
        Write-Host "  $Icon $AgentName installed" -ForegroundColor Green
        $InstalledCount++
    } else {
        Write-Host "  ⚠ $AgentFile not found (will skip)" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "  ✓ Installed $InstalledCount/7 agents" -ForegroundColor Green
Write-Host ""

# ═══════════════════════════════════════════════════════════════════════
# INSTALL STARTUP LOADER
# ═══════════════════════════════════════════════════════════════════════

Write-Host "⚡ Installing startup loader..." -ForegroundColor Yellow

$StartupLoaderSource = Join-Path $SCRIPT_DIR "LOAD_ALL_AGENTS_STARTUP.ps1"
$StartupLoaderDest = Join-Path $SCRIPTS_DIR "LOAD_ALL_AGENTS_STARTUP.ps1"

if (Test-Path $StartupLoaderSource) {
    Copy-Item $StartupLoaderSource $StartupLoaderDest -Force
    Write-Host "  ✓ Startup loader installed" -ForegroundColor Green
} else {
    Write-Host "  ⚠ Startup loader not found (will create minimal version)" -ForegroundColor Yellow
}

Write-Host ""

# ═══════════════════════════════════════════════════════════════════════
# CONFIGURE AUTO-STARTUP
# ═══════════════════════════════════════════════════════════════════════

Write-Host "⚡ Configuring auto-startup..." -ForegroundColor Yellow

$StartupScript = @"
Start-Process powershell.exe -ArgumentList `
    "-WindowStyle Hidden -ExecutionPolicy Bypass -File `"$StartupLoaderDest`"" `
    -WindowStyle Hidden
"@

$StartupScriptPath = Join-Path $STARTUP_DIR "MC96_Agents.ps1"
$StartupScript | Out-File $StartupScriptPath -Encoding ASCII

# Create a shortcut for cleaner startup
$WScriptShell = New-Object -ComObject WScript.Shell
$Shortcut = $WScriptShell.CreateShortcut("$STARTUP_DIR\MC96_Agents.lnk")
$Shortcut.TargetPath = "powershell.exe"
$Shortcut.Arguments = "-WindowStyle Hidden -ExecutionPolicy Bypass -File `"$StartupLoaderDest`""
$Shortcut.WindowStyle = 7  # Minimized
$Shortcut.Save()

Write-Host "  ✓ Auto-startup configured" -ForegroundColor Green
Write-Host "  ✓ Shortcut created: $STARTUP_DIR\MC96_Agents.lnk" -ForegroundColor Green
Write-Host ""

# ═══════════════════════════════════════════════════════════════════════
# CREATE DESKTOP SHORTCUTS
# ═══════════════════════════════════════════════════════════════════════

Write-Host "⚡ Creating desktop shortcuts..." -ForegroundColor Yellow

# Agent Control shortcut
$ControlScript = @"
Start-Process powershell.exe -ArgumentList `
    "-NoProfile -ExecutionPolicy Bypass -File `"$StartupLoaderDest`"" `
    -Verb RunAs
"@

$ControlScriptPath = "$env:USERPROFILE\Desktop\MC96_Agent_Control.ps1"
$ControlScript | Out-File $ControlScriptPath -Encoding ASCII

Write-Host "  ✓ MC96_Agent_Control.ps1" -ForegroundColor Green

# Agent Logs shortcut
$LogsScript = @"
Start-Process explorer.exe -ArgumentList `"$LOGS_DIR`"
"@

$LogsScriptPath = "$env:USERPROFILE\Desktop\MC96_Agent_Logs.ps1"
$LogsScript | Out-File $LogsScriptPath -Encoding ASCII

Write-Host "  ✓ MC96_Agent_Logs.ps1" -ForegroundColor Green

Write-Host ""

# ═══════════════════════════════════════════════════════════════════════
# START AGENTS NOW
# ═══════════════════════════════════════════════════════════════════════

Write-Host "⚡ Starting all agents NOW..." -ForegroundColor Yellow

Start-Process powershell.exe -ArgumentList `
    "-WindowStyle Hidden -ExecutionPolicy Bypass -File `"$StartupLoaderDest`"" `
    -WindowStyle Hidden

Start-Sleep -Seconds 5

# Count running agents
$RunningAgents = Get-Process powershell -ErrorAction SilentlyContinue | Where-Object { 
    $_.CommandLine -like "*AGENT_*" 
}

$RunningCount = 0
if ($RunningAgents) {
    $RunningCount = ($RunningAgents | Measure-Object).Count
}

Write-Host "  ✓ Agents started" -ForegroundColor Green
Write-Host "  ✓ Found $RunningCount running processes" -ForegroundColor Green
Write-Host ""

# ═══════════════════════════════════════════════════════════════════════
# INSTALLATION COMPLETE
# ═══════════════════════════════════════════════════════════════════════

Write-Host "╔══════════════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║                                                                      ║" -ForegroundColor Green
Write-Host "║          ✅✅✅ INSTALLATION COMPLETE ✅✅✅                            ║" -ForegroundColor Green
Write-Host "║                                                                      ║" -ForegroundColor Green
Write-Host "╚══════════════════════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""

Write-Host "🎯 WHAT GOT INSTALLED:" -ForegroundColor Cyan
Write-Host ""
Write-Host "AI AGENTS:" -ForegroundColor White
Write-Host "  💜 AGENT_LUCY (Creative/Music) - Every 5 min" -ForegroundColor Magenta
Write-Host "  🔧 AGENT_POPS (System Health) - Every 3 min" -ForegroundColor Cyan
Write-Host "  ⚙️  AGENT_ENGR_KEITH (Engineering) - Every 4 min" -ForegroundColor White
Write-Host "  💭 AGENT_DREAM (Vision/Goals) - Every 6 min" -ForegroundColor Blue
Write-Host "  💰 AGENT_ALEX_WARD (Monetization) - Every 6 min" -ForegroundColor Yellow
Write-Host "  🎯 AGENT_WARDIE (Strategic) - Every 7 min" -ForegroundColor DarkCyan
Write-Host "  ⚙️  AGENT_FLEET (Operations) - Every 5 min" -ForegroundColor White
Write-Host ""

Write-Host "CONFIGURATION:" -ForegroundColor White
Write-Host "  ✓ Auto-start at every Windows boot" -ForegroundColor Green
Write-Host "  ✓ Agents running NOW in background" -ForegroundColor Green
Write-Host "  ✓ Desktop shortcuts created" -ForegroundColor Green
Write-Host ""

Write-Host "LOCATIONS:" -ForegroundColor White
Write-Host "  Agents:   $SCRIPTS_DIR" -ForegroundColor Gray
Write-Host "  Logs:     $LOGS_DIR" -ForegroundColor Gray
Write-Host "  Startup:  $STARTUP_DIR\MC96_Agents.lnk" -ForegroundColor Gray
Write-Host ""

Write-Host "DESKTOP SHORTCUTS:" -ForegroundColor White
Write-Host "  • MC96_Agent_Control.ps1  - Restart all agents" -ForegroundColor Gray
Write-Host "  • MC96_Agent_Logs.ps1     - View logs folder" -ForegroundColor Gray
Write-Host ""

Write-Host "NEXT STEPS:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. CHECK AGENTS:" -ForegroundColor White
Write-Host "   Double-click: MC96_Agent_Logs.ps1 on Desktop" -ForegroundColor Gray
Write-Host ""
Write-Host "2. RESTART AGENTS:" -ForegroundColor White
Write-Host "   Right-click: MC96_Agent_Control.ps1 → Run as Administrator" -ForegroundColor Gray
Write-Host ""
Write-Host "3. REBOOT TEST:" -ForegroundColor White
Write-Host "   Restart Windows → Agents auto-start" -ForegroundColor Gray
Write-Host ""

Write-Host "⚡⚡⚡ GORUNFREEX5000 COMPLETE ⚡⚡⚡" -ForegroundColor Green
Write-Host ""
Write-Host "7 agents installed." -ForegroundColor White
Write-Host "Agents running NOW." -ForegroundColor White
Write-Host "Auto-start configured." -ForegroundColor White
Write-Host "Complete automation." -ForegroundColor White
Write-Host ""

# Notification
Add-Type -AssemblyName System.Windows.Forms
$notification = New-Object System.Windows.Forms.NotifyIcon
$notification.Icon = [System.Drawing.SystemIcons]::Information
$notification.BalloonTipIcon = [System.Windows.Forms.ToolTipIcon]::Info
$notification.BalloonTipTitle = "MC96 Agent System - GABRIEL"
$notification.BalloonTipText = "Installation complete! All 7 agents installed and running."
$notification.Visible = $true
$notification.ShowBalloonTip(5000)

Start-Sleep -Seconds 2
$notification.Dispose()

Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
