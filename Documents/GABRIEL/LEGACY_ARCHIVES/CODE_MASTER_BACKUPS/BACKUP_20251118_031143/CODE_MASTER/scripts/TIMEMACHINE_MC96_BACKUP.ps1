# TIME MACHINE BACKUP SETUP - MC96 MISSION CONTROL
# 2 Users + 2.8TB GHOST Drive Backup
# Rob Sonic Protocol | GORUNFREE

Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  TIME MACHINE BACKUP - MC96 MISSION CONTROL       ║" -ForegroundColor Cyan
Write-Host "║  2 Users + 2.8TB GHOST Drive                     ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Check if running as root or with sudo
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "⚠️  Some operations require administrator privileges" -ForegroundColor Yellow
    Write-Host "   Run with: sudo powershell -ExecutionPolicy Bypass -File TIMEMACHINE_MC96_BACKUP.ps1" -ForegroundColor Yellow
    Write-Host ""
}

# PHASE 1: DETECT GHOST DRIVE
Write-Host "🔍 PHASE 1: Detecting GHOST Drive (2.8TB)..." -ForegroundColor Yellow
Write-Host ""

$ghostDrive = $null
$allDisks = diskutil list 2>&1 | Out-String

# Look for 2.8TB drive
$diskInfo = diskutil info /dev/disk* 2>&1 | Out-String
if ($diskInfo -match "2\.8.*TB|GHOST|2800.*GB") {
    Write-Host "✓ Found potential GHOST drive" -ForegroundColor Green
} else {
    Write-Host "⚠️  GHOST drive not automatically detected" -ForegroundColor Yellow
    Write-Host "   Please identify the drive manually:" -ForegroundColor Yellow
    Write-Host ""
    diskutil list | Format-Table -AutoSize
    Write-Host ""
    $ghostDrive = Read-Host "Enter disk identifier (e.g., disk2s1)"
}

# PHASE 2: DETECT USERS
Write-Host ""
Write-Host "🔍 PHASE 2: Detecting Users..." -ForegroundColor Yellow
Write-Host ""

$users = dscl . list /Users | Where-Object { 
    $_ -notmatch '^_' -and 
    $_ -ne 'daemon' -and 
    $_ -ne 'nobody' -and 
    $_ -ne 'root' 
} | Where-Object { Test-Path "/Users/$_" }

Write-Host "Found $($users.Count) user(s):" -ForegroundColor Green
foreach ($user in $users) {
    $homeSize = (Get-ChildItem "/Users/$user" -Recurse -ErrorAction SilentlyContinue | 
        Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum / 1GB
    Write-Host "  • $user ($([math]::Round($homeSize, 2)) GB)" -ForegroundColor Cyan
}

Write-Host ""

# PHASE 3: CHECK TIME MACHINE STATUS
Write-Host "🔍 PHASE 3: Checking Time Machine Status..." -ForegroundColor Yellow
Write-Host ""

$tmStatus = tmutil status 2>&1 | Out-String
if ($tmStatus -match "Running") {
    Write-Host "✓ Time Machine is currently running" -ForegroundColor Green
} elseif ($tmStatus -match "Stopped") {
    Write-Host "⚠️  Time Machine is stopped" -ForegroundColor Yellow
} else {
    Write-Host "ℹ️  Time Machine status unknown" -ForegroundColor Cyan
}

$currentDestination = tmutil destinationinfo 2>&1 | Out-String
if ($currentDestination) {
    Write-Host "Current backup destination:" -ForegroundColor Cyan
    Write-Host $currentDestination
} else {
    Write-Host "⚠️  No backup destination configured" -ForegroundColor Yellow
}

Write-Host ""

# PHASE 4: PREPARE GHOST DRIVE
Write-Host "🔍 PHASE 4: Preparing GHOST Drive for Time Machine..." -ForegroundColor Yellow
Write-Host ""

if ($ghostDrive) {
    Write-Host "Checking drive: $ghostDrive" -ForegroundColor Cyan
    
    # Check if drive is formatted
    $driveInfo = diskutil info $ghostDrive 2>&1 | Out-String
    if ($driveInfo -match "APFS|HFS") {
        Write-Host "✓ Drive is formatted" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Drive may need formatting" -ForegroundColor Yellow
        Write-Host "   Format as APFS for best Time Machine compatibility" -ForegroundColor Yellow
    }
    
    # Check available space
    $availableSpace = (Get-PSDrive | Where-Object { $_.Name -eq $ghostDrive }).Free / 1GB
    Write-Host "Available space: $([math]::Round($availableSpace, 2)) GB" -ForegroundColor Cyan
}

Write-Host ""

# PHASE 5: SETUP INSTRUCTIONS
Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  TIME MACHINE SETUP INSTRUCTIONS                   ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

Write-Host "📋 MANUAL SETUP STEPS:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Open System Settings → General → Time Machine" -ForegroundColor White
Write-Host ""
Write-Host "2. Click 'Add Backup Disk' or 'Select Disk'" -ForegroundColor White
Write-Host ""
Write-Host "3. Select your GHOST drive (2.8TB)" -ForegroundColor White
Write-Host ""
Write-Host "4. If prompted, enter password to encrypt backup (recommended)" -ForegroundColor White
Write-Host ""
Write-Host "5. Time Machine will format the drive if needed" -ForegroundColor White
Write-Host ""
Write-Host "6. Both users will be backed up automatically" -ForegroundColor White
Write-Host ""

# PHASE 6: EXCLUSIONS (OPTIONAL)
Write-Host "📋 RECOMMENDED EXCLUSIONS:" -ForegroundColor Yellow
Write-Host ""
Write-Host "To save space, you may want to exclude:" -ForegroundColor White
Write-Host "  • /System/Library/Caches" -ForegroundColor Cyan
Write-Host "  • /Library/Caches" -ForegroundColor Cyan
Write-Host "  • ~/Library/Caches" -ForegroundColor Cyan
Write-Host "  • node_modules folders" -ForegroundColor Cyan
Write-Host "  • .git folders (if you have separate Git backup)" -ForegroundColor Cyan
Write-Host ""

# PHASE 7: VERIFICATION SCRIPT
Write-Host "📋 VERIFICATION COMMANDS:" -ForegroundColor Yellow
Write-Host ""
Write-Host "Check Time Machine status:" -ForegroundColor White
Write-Host "  tmutil status" -ForegroundColor Cyan
Write-Host ""
Write-Host "List backup destinations:" -ForegroundColor White
Write-Host "  tmutil destinationinfo" -ForegroundColor Cyan
Write-Host ""
Write-Host "List recent backups:" -ForegroundColor White
Write-Host "  tmutil listbackups" -ForegroundColor Cyan
Write-Host ""
Write-Host "Start backup manually:" -ForegroundColor White
Write-Host "  tmutil startbackup" -ForegroundColor Cyan
Write-Host ""
Write-Host "Stop backup:" -ForegroundColor White
Write-Host "  tmutil stopbackup" -ForegroundColor Cyan
Write-Host ""

# PHASE 8: ESTIMATED BACKUP TIME
Write-Host "📊 ESTIMATED BACKUP TIME:" -ForegroundColor Yellow
Write-Host ""

$totalSize = 0
foreach ($user in $users) {
    $userSize = (Get-ChildItem "/Users/$user" -Recurse -ErrorAction SilentlyContinue | 
        Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum / 1GB
    $totalSize += $userSize
}

$systemSize = 50  # Estimate for system files
$totalSize += $systemSize

Write-Host "Estimated total backup size: $([math]::Round($totalSize, 2)) GB" -ForegroundColor Cyan
Write-Host "First backup time: ~$([math]::Round($totalSize / 10, 1)) hours (at ~100 MB/s)" -ForegroundColor Cyan
Write-Host "Incremental backups: ~5-30 minutes" -ForegroundColor Cyan
Write-Host ""

# PHASE 9: AUTOMATION SCRIPT
Write-Host "📋 AUTOMATION SCRIPT CREATED:" -ForegroundColor Yellow
Write-Host ""

$autoScript = @"
#!/bin/bash
# Time Machine Backup Automation - MC96
# Auto-start backup and monitor progress

echo "🕐 Starting Time Machine backup..."
tmutil startbackup

echo "📊 Monitoring backup progress..."
while true; do
    STATUS=`tmutil status | grep -i "Running\|Stopped\|Idle" | head -1`
    echo "Status: `$STATUS"
    
    if [[ `$STATUS == *"Stopped"* ]] || [[ `$STATUS == *"Idle"* ]]; then
        echo "✅ Backup complete or idle"
        break
    fi
    
    sleep 30
done

echo "📋 Backup summary:"
tmutil listbackups | tail -5
"@

$autoScriptPath = "$HOME/CODE_MASTER/scripts/tm_backup_auto.sh"
$autoScript | Out-File -FilePath $autoScriptPath -Encoding utf8
chmod +x $autoScriptPath 2>/dev/null

Write-Host "  ✓ Created: $autoScriptPath" -ForegroundColor Green
Write-Host "  Run with: bash $autoScriptPath" -ForegroundColor Cyan
Write-Host ""

# COMPLETION
Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  SETUP COMPLETE                                   ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""
Write-Host "✅ Next Steps:" -ForegroundColor Green
Write-Host "  1. Open System Settings → Time Machine" -ForegroundColor White
Write-Host "  2. Select GHOST drive (2.8TB)" -ForegroundColor White
Write-Host "  3. Let Time Machine format and start first backup" -ForegroundColor White
Write-Host "  4. Both users will be backed up automatically" -ForegroundColor White
Write-Host ""
Write-Host "📁 Scripts saved to: $HOME/CODE_MASTER/scripts/" -ForegroundColor Cyan
Write-Host ""
Write-Host "🔥 MC96 Mission Control Backup Ready! 🚀" -ForegroundColor Green

