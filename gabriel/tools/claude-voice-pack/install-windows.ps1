#═══════════════════════════════════════════════════════════════════════════════
# M2G Claude Voice Pack - Windows Installer
# 
# Run: powershell -ExecutionPolicy Bypass -File install-windows.ps1
#
# Installs:
#   • m2g-say    - Windows SAPI voice wrapper
#   • claudev    - Claude CLI wrapper with spoken status
#
# Usage after install (in new terminal):
#   m2g-say "hello world"
#   claudev "explain quantum computing"
#   $env:SAY=0; claudev "silent mode"
#═══════════════════════════════════════════════════════════════════════════════
$ErrorActionPreference = "Stop"

$Root = Join-Path $env:USERPROFILE "m2g\claude-voice"

Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  M2G Claude Voice Pack - Windows Installer" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""
Write-Host "Installing to: $Root"
Write-Host ""

# Create directory
New-Item -ItemType Directory -Force -Path $Root | Out-Null

#───────────────────────────────────────────────────────────────────────────────
# say.ps1 - PowerShell voice script (using System.Speech)
#───────────────────────────────────────────────────────────────────────────────
@'
#═══════════════════════════════════════════════════════════════════════════════
# m2g-say - Windows text-to-speech (System.Speech.Synthesis)
#═══════════════════════════════════════════════════════════════════════════════
param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$TextParts
)

$text = ($TextParts -join " ").Trim()
if ($text.Length -eq 0) { exit 0 }

Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer

# Preferred voices (high-quality first)
$preferred = @(
    "Microsoft David Desktop",
    "Microsoft Zira Desktop", 
    "Microsoft Mark Desktop",
    "David",
    "Zira",
    "Mark"
)

$installedVoices = $synth.GetInstalledVoices() | ForEach-Object { $_.VoiceInfo.Name }

$selectedVoice = $null
foreach ($v in $preferred) {
    foreach ($installed in $installedVoices) {
        if ($installed -like "*$v*") {
            $selectedVoice = $installed
            break
        }
    }
    if ($selectedVoice) { break }
}

if ($selectedVoice) {
    try {
        $synth.SelectVoice($selectedVoice)
    } catch {
        # Fallback to default
    }
}

# Set rate (slightly faster than default)
$synth.Rate = 1

# Speak
$synth.Speak($text)
'@ | Out-File (Join-Path $Root "say.ps1") -Encoding utf8
Write-Host "✓ Created say.ps1" -ForegroundColor Green

#───────────────────────────────────────────────────────────────────────────────
# m2g-say.cmd - Batch wrapper for say.ps1
#───────────────────────────────────────────────────────────────────────────────
@"
@echo off
powershell -NoProfile -ExecutionPolicy Bypass -File "%USERPROFILE%\m2g\claude-voice\say.ps1" %*
"@ | Out-File (Join-Path $Root "m2g-say.cmd") -Encoding ascii
Write-Host "✓ Created m2g-say.cmd" -ForegroundColor Green

#───────────────────────────────────────────────────────────────────────────────
# claudev.cmd - Claude wrapper with voice status
#───────────────────────────────────────────────────────────────────────────────
@'
@echo off
setlocal enabledelayedexpansion

rem ═══════════════════════════════════════════════════════════════════════════
rem claudev - Claude CLI wrapper with spoken status
rem
rem Environment:
rem   SAY=0        Disable voice (default: 1)
rem   CLAUDE_BIN   Force specific CLI
rem ═══════════════════════════════════════════════════════════════════════════

rem Default SAY=1
if "%SAY%"=="" set "SAY=1"

rem Check for help flags (skip voice)
for %%a in (%*) do (
    if "%%a"=="-h" goto :runsilent
    if "%%a"=="--help" goto :runsilent
    if "%%a"=="-v" goto :runsilent
    if "%%a"=="--version" goto :runsilent
)

rem Auto-detect Claude CLI
set "BIN=%CLAUDE_BIN%"
if not "%BIN%"=="" goto :run

where m2g-claude >nul 2>nul && set "BIN=m2g-claude" && goto :run
where claude >nul 2>nul && set "BIN=claude" && goto :run
where claude-code >nul 2>nul && set "BIN=claude-code" && goto :run

echo claudev: no Claude CLI found 1>&2
echo Install one of: m2g-claude, claude, claude-code 1>&2
exit /b 127

:runsilent
%BIN% %*
exit /b %ERRORLEVEL%

:run
rem Speak start
if "%SAY%"=="1" start /b cmd /c m2g-say Claude starting

rem Run Claude
%BIN% %*
set "RC=%ERRORLEVEL%"

rem Speak result
if "%SAY%"=="1" (
    if "%RC%"=="0" (
        call m2g-say Claude done
    ) else (
        call m2g-say Claude error, code %RC%
    )
)

exit /b %RC%
'@ | Out-File (Join-Path $Root "claudev.cmd") -Encoding ascii
Write-Host "✓ Created claudev.cmd" -ForegroundColor Green

#───────────────────────────────────────────────────────────────────────────────
# m2g-ask.cmd - Quick Claude question
#───────────────────────────────────────────────────────────────────────────────
@'
@echo off
setlocal enabledelayedexpansion

rem ═══════════════════════════════════════════════════════════════════════════
rem m2g-ask - Quick Claude question (clipboard or argument)
rem ═══════════════════════════════════════════════════════════════════════════

set "PROMPT=%*"

rem If no argument, try clipboard
if "%PROMPT%"=="" (
    for /f "usebackq delims=" %%i in (`powershell -command "Get-Clipboard"`) do set "PROMPT=%%i"
)

if "%PROMPT%"=="" (
    echo Usage: m2g-ask "your question" 1>&2
    echo        Or copy text to clipboard first 1>&2
    exit /b 1
)

claudev %PROMPT%
'@ | Out-File (Join-Path $Root "m2g-ask.cmd") -Encoding ascii
Write-Host "✓ Created m2g-ask.cmd" -ForegroundColor Green

#───────────────────────────────────────────────────────────────────────────────
# Add to User PATH
#───────────────────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "Updating PATH..."

$CurrentUserPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($CurrentUserPath -notlike "*$Root*") {
    [Environment]::SetEnvironmentVariable("Path", "$CurrentUserPath;$Root", "User")
    Write-Host "✓ Added to User PATH" -ForegroundColor Green
} else {
    Write-Host "✓ Already in PATH" -ForegroundColor Green
}

#───────────────────────────────────────────────────────────────────────────────
# Create uninstaller
#───────────────────────────────────────────────────────────────────────────────
@'
# M2G Claude Voice Pack - Uninstaller
$ErrorActionPreference = "Stop"

Write-Host "Removing M2G Claude Voice Pack..."

$Root = Join-Path $env:USERPROFILE "m2g\claude-voice"

# Remove from PATH
$CurrentPath = [Environment]::GetEnvironmentVariable("Path", "User")
$NewPath = ($CurrentPath -split ";" | Where-Object { $_ -ne $Root }) -join ";"
[Environment]::SetEnvironmentVariable("Path", $NewPath, "User")

# Remove folder
if (Test-Path $Root) {
    Remove-Item -Recurse -Force $Root
}

Write-Host "✓ Uninstalled" -ForegroundColor Green
'@ | Out-File (Join-Path $Root "uninstall.ps1") -Encoding utf8

#───────────────────────────────────────────────────────────────────────────────
# Done
#───────────────────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  ✓ M2G Claude Voice Pack Installed" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""
Write-Host "Commands available (open NEW terminal):"
Write-Host "  m2g-say `"text`"     - Speak text" -ForegroundColor Yellow
Write-Host "  claudev `"prompt`"   - Claude with voice status" -ForegroundColor Yellow
Write-Host "  m2g-ask `"question`" - Quick question (or use clipboard)" -ForegroundColor Yellow
Write-Host ""
Write-Host "Options:"
Write-Host '  $env:SAY=0; claudev ...  - Disable voice'
Write-Host '  $env:CLAUDE_BIN="xxx"    - Force specific CLI'
Write-Host ""
Write-Host "Uninstall:"
Write-Host "  powershell -File `"$Root\uninstall.ps1`""
Write-Host ""

# Test voice
try {
    & (Join-Path $Root "m2g-say.cmd") "Claude voice pack installed"
} catch {
    Write-Host "(Voice test skipped)" -ForegroundColor Gray
}
