# LOAD_ALL_AGENTS_STARTUP.ps1
# MASTER AGENT LOADER - AUTO-LOADS AT WINDOWS STARTUP
# GORUNFREEX5000 - LOAD ALL 7 AGENTS IN EVERY STARTUP SESSION
#
# Loads: LUCY, POPS, ENGR_KEITH, DREAM, ALEX_WARD, WARDIE, FLEET
# Keeps them running persistently in background
# Optimizes GABRIEL system performance
#
# USAGE: This runs automatically at Windows startup after installation

#Requires -RunAsAdministrator

$ErrorActionPreference = "Continue"

$AGENT_SCRIPTS = @{
    "LUCY" = "$env:ProgramFiles\MC96_Automation\Scripts\AGENT_LUCY.ps1"
    "POPS" = "$env:ProgramFiles\MC96_Automation\Scripts\AGENT_POPS.ps1"
    "ENGR_KEITH" = "$env:ProgramFiles\MC96_Automation\Scripts\AGENT_ENGR_KEITH.ps1"
    "DREAM" = "$env:ProgramFiles\MC96_Automation\Scripts\AGENT_DREAM.ps1"
    "ALEX_WARD" = "$env:ProgramFiles\MC96_Automation\Scripts\AGENT_ALEX_WARD.ps1"
    "WARDIE" = "$env:ProgramFiles\MC96_Automation\Scripts\AGENT_WARDIE.ps1"
    "FLEET" = "$env:ProgramFiles\MC96_Automation\Scripts\AGENT_FLEET.ps1"
}

$LOG_PATH = "$env:ProgramFiles\MC96_Automation\Logs\AGENT_STARTUP_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"

function Write-Log {
    param([string]$Message, [string]$Color = "White")
    $Timestamp = Get-Date -Format "HH:mm:ss"
    $Output = "[$Timestamp] $Message"
    Write-Host $Output -ForegroundColor $Color
    $Output | Out-File $LOG_PATH -Append
}

Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                                                                      ║" -ForegroundColor Cyan
Write-Host "║              MC96 AGENT SYSTEM - STARTUP LOADER                      ║" -ForegroundColor Cyan
Write-Host "║                    GORUNFREEX5000                                    ║" -ForegroundColor Cyan
Write-Host "║                                                                      ║" -ForegroundColor Cyan
Write-Host "║          LOADING ALL 7 AGENTS - PERSISTENT BACKGROUND MODE           ║" -ForegroundColor Cyan
Write-Host "║                                                                      ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

Write-Log "═══════════════════════════════════════════════════════════════" "White"
Write-Log "AGENT SYSTEM INITIALIZATION - 7 AGENTS" "Yellow"
Write-Log "═══════════════════════════════════════════════════════════════" "White"

# ═══════════════════════════════════════════════════════════════════════
# PHASE 1: GABRIEL SYSTEM OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════

Write-Log ""
Write-Log "PHASE 1: GABRIEL System Optimization" "Cyan"
Write-Log "───────────────────────────────────────────────────────────────" "White"

# Set power plan to High Performance
try {
    powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
    Write-Log "✓ Power plan set to High Performance" "Green"
} catch {
    Write-Log "⚠ Could not set power plan" "Yellow"
}

# Optimize network settings
try {
    netsh int tcp set global autotuninglevel=normal
    Write-Log "✓ Network auto-tuning optimized" "Green"
} catch {
    Write-Log "⚠ Could not optimize network settings" "Yellow"
}

Write-Log "✓ GABRIEL optimization complete" "Green"

# ═══════════════════════════════════════════════════════════════════════
# PHASE 2: STOP ANY EXISTING AGENT PROCESSES
# ═══════════════════════════════════════════════════════════════════════

Write-Log ""
Write-Log "PHASE 2: Stopping existing agent processes" "Cyan"
Write-Log "───────────────────────────────────────────────────────────────" "White"

$ExistingAgents = Get-Process powershell -ErrorAction SilentlyContinue | Where-Object { 
    $_.CommandLine -like "*AGENT_*" 
}

if ($ExistingAgents) {
    foreach ($Process in $ExistingAgents) {
        try {
            Stop-Process -Id $Process.Id -Force
            Write-Log "  ✓ Stopped existing agent (PID: $($Process.Id))" "Yellow"
        } catch {
            Write-Log "  ⚠ Could not stop PID $($Process.Id)" "Yellow"
        }
    }
} else {
    Write-Log "  No existing agents to stop" "White"
}

Start-Sleep -Seconds 2

# ═══════════════════════════════════════════════════════════════════════
# PHASE 3: START ALL 7 AGENTS
# ═══════════════════════════════════════════════════════════════════════

Write-Log ""
Write-Log "PHASE 3: Starting all 7 AI agents" "Cyan"
Write-Log "───────────────────────────────────────────────────────────────" "White"

$StartedAgents = @()
$FailedAgents = @()

foreach ($AgentName in $AGENT_SCRIPTS.Keys | Sort-Object) {
    $ScriptPath = $AGENT_SCRIPTS[$AgentName]
    
    if (Test-Path $ScriptPath) {
        try {
            $Process = Start-Process powershell.exe -ArgumentList `
                "-WindowStyle Hidden -ExecutionPolicy Bypass -File `"$ScriptPath`"" `
                -WindowStyle Hidden -PassThru
            
            Start-Sleep -Milliseconds 500
            
            if ($Process -and !$Process.HasExited) {
                $StartedAgents += $AgentName
                $Icon = switch ($AgentName) {
                    "LUCY" { "💜" }
                    "POPS" { "🔧" }
                    "ENGR_KEITH" { "⚙️" }
                    "DREAM" { "💭" }
                    "ALEX_WARD" { "💰" }
                    "WARDIE" { "🎯" }
                    "FLEET" { "⚙️" }
                    default { "✓" }
                }
                Write-Log "  $Icon AGENT_$AgentName started (PID: $($Process.Id))" "Green"
            } else {
                $FailedAgents += $AgentName
                Write-Log "  ✗ AGENT_$AgentName failed to start" "Red"
            }
        } catch {
            $FailedAgents += $AgentName
            Write-Log "  ✗ AGENT_$AgentName error: $($_.Exception.Message)" "Red"
        }
    } else {
        $FailedAgents += $AgentName
        Write-Log "  ✗ AGENT_$AgentName script not found at $ScriptPath" "Red"
    }
}

# ═══════════════════════════════════════════════════════════════════════
# PHASE 4: VERIFICATION
# ═══════════════════════════════════════════════════════════════════════

Write-Log ""
Write-Log "PHASE 4: Agent verification" "Cyan"
Write-Log "───────────────────────────────────────────────────────────────" "White"

Start-Sleep -Seconds 3

$RunningCount = 0
foreach ($AgentName in $AGENT_SCRIPTS.Keys) {
    $Process = Get-Process powershell -ErrorAction SilentlyContinue | Where-Object { 
        $_.CommandLine -like "*AGENT_$AgentName*" 
    }
    
    if ($Process) {
        $RunningCount++
        Write-Log "  ✓ AGENT_$AgentName verified (PID: $($Process.Id))" "Green"
    } else {
        Write-Log "  ✗ AGENT_$AgentName not running" "Red"
    }
}

# ═══════════════════════════════════════════════════════════════════════
# FINAL STATUS
# ═══════════════════════════════════════════════════════════════════════

Write-Log ""
Write-Log "═══════════════════════════════════════════════════════════════" "White"
Write-Log "STARTUP COMPLETE" "Green"
Write-Log "═══════════════════════════════════════════════════════════════" "White"
Write-Log ""
Write-Log "Agents Started: $($StartedAgents.Count)/7" "Green"
Write-Log "Running Now: $RunningCount/7" "Green"

if ($StartedAgents.Count -eq 7) {
    Write-Log "✓✓✓ ALL 7 AGENTS OPERATIONAL ✓✓✓" "Green"
} elseif ($StartedAgents.Count -ge 5) {
    Write-Log "⚠ PARTIAL SUCCESS - Some agents operational" "Yellow"
} else {
    Write-Log "✗ STARTUP ISSUES - Check logs" "Red"
}

Write-Log ""
Write-Log "Agent Details:" "White"
Write-Log "  💜 LUCY - Creative/Music monitoring" "Magenta"
Write-Log "  🔧 POPS - System Health & Network" "Cyan"
Write-Log "  ⚙️  ENGR_KEITH - Engineering optimization" "White"
Write-Log "  💭 DREAM - Vision & Goal tracking" "Blue"
Write-Log "  💰 ALEX_WARD - Monetization Genius" "Yellow"
Write-Log "  🎯 WARDIE - Strategic Foresight" "DarkCyan"
Write-Log "  ⚙️  FLEET - Operations Commander" "White"
Write-Log ""
Write-Log "Logs: $env:ProgramFiles\MC96_Automation\Logs\" "Gray"
Write-Log "GORUNFREEX5000 - Complete automation active" "Green"
Write-Log ""

# Notification
Add-Type -AssemblyName System.Windows.Forms
$notification = New-Object System.Windows.Forms.NotifyIcon
$notification.Icon = [System.Drawing.SystemIcons]::Information
$notification.BalloonTipIcon = [System.Windows.Forms.ToolTipIcon]::Info
$notification.BalloonTipTitle = "MC96 Agent System"
$notification.BalloonTipText = "All 7 agents running on GABRIEL`n$RunningCount/7 operational"
$notification.Visible = $true
$notification.ShowBalloonTip(5000)

Start-Sleep -Seconds 2
$notification.Dispose()

Write-Host ""
Write-Host "Press any key to close this window..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
