# SCAN GHOST DRIVE - Find and Analyze Hidden GHOST Drive
# Rob Sonic Protocol | GORUNFREE

Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  SCANNING GHOST DRIVE (2.8TB)                     ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$REPORT_FILE = "$HOME/CODE_MASTER/GHOST_DRIVE_SCAN_REPORT.txt"
$report = @()

# PHASE 1: FIND GHOST DRIVE
Write-Host "🔍 PHASE 1: Finding GHOST Drive..." -ForegroundColor Yellow
Write-Host ""

$ghostDrive = $null
$allDisks = diskutil list 2>&1 | Out-String

# Look for 2.8TB drives
$diskList = diskutil list
$report += "=== DISK LIST ==="
$report += $diskList
$report += ""

# Check for GHOST in disk names
$diskInfo = diskutil info /dev/disk* 2>&1 | Out-String
if ($diskInfo -match "GHOST|2\.8.*TB|2800.*GB") {
    Write-Host "✓ Found potential GHOST drive" -ForegroundColor Green
} else {
    Write-Host "⚠️  GHOST drive not found by name" -ForegroundColor Yellow
}

# Check mounted volumes
Write-Host ""
Write-Host "📦 Checking mounted volumes..." -ForegroundColor Cyan
$volumes = Get-Volume | Where-Object { $_.Size -gt 2TB -or $_.FileSystemLabel -like "*GHOST*" }
foreach ($vol in $volumes) {
    Write-Host "  Found: $($vol.FileSystemLabel) ($([math]::Round($vol.Size/1GB,2)) GB)" -ForegroundColor Green
    $report += "Volume: $($vol.FileSystemLabel) - $([math]::Round($vol.Size/1GB,2)) GB"
}

Write-Host ""

# PHASE 2: CHECK DESKTOP FOR HIDDEN GHOST
Write-Host "🔍 PHASE 2: Checking Desktop for hidden GHOST..." -ForegroundColor Yellow
Write-Host ""

$desktopItems = Get-ChildItem "$HOME/Desktop" -Force -ErrorAction SilentlyContinue
$ghostItems = $desktopItems | Where-Object { 
    $_.Name -like "*GHOST*" -or 
    $_.Name -like "*ghost*" -or
    $_.Attributes -match "Hidden"
}

if ($ghostItems.Count -gt 0) {
    Write-Host "Found $($ghostItems.Count) GHOST-related item(s) on Desktop:" -ForegroundColor Green
    foreach ($item in $ghostItems) {
        Write-Host "  • $($item.Name) ($($item.Attributes))" -ForegroundColor Cyan
        $report += "Desktop Item: $($item.Name) - $($item.Attributes)"
        
        if ($item.PSIsContainer) {
            $itemCount = (Get-ChildItem $item.FullName -Recurse -ErrorAction SilentlyContinue | Measure-Object).Count
            $itemSize = (Get-ChildItem $item.FullName -Recurse -File -ErrorAction SilentlyContinue | 
                Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum / 1GB
            Write-Host "    Files: $itemCount | Size: $([math]::Round($itemSize,2)) GB" -ForegroundColor White
            $report += "  Files: $itemCount | Size: $([math]::Round($itemSize,2)) GB"
        }
    }
} else {
    Write-Host "⚠️  No GHOST items found on Desktop" -ForegroundColor Yellow
}

Write-Host ""

# PHASE 3: SCAN ALL EXTERNAL DRIVES
Write-Host "🔍 PHASE 3: Scanning all external drives..." -ForegroundColor Yellow
Write-Host ""

$externalDisks = diskutil list | Select-String -Pattern "external" -Context 5
$report += "=== EXTERNAL DISKS ==="
$report += $externalDisks
$report += ""

Write-Host "External drives found:" -ForegroundColor Cyan
$externalDisks | ForEach-Object { Write-Host "  $_" -ForegroundColor White }

Write-Host ""

# PHASE 4: CHECK FOR 2.8TB DRIVES
Write-Host "🔍 PHASE 4: Looking for 2.8TB drives..." -ForegroundColor Yellow
Write-Host ""

$largeDisks = @()
foreach ($disk in Get-Disk -ErrorAction SilentlyContinue) {
    $sizeGB = [math]::Round($disk.Size / 1GB, 2)
    if ($sizeGB -gt 2500 -and $sizeGB -lt 3000) {
        $largeDisks += $disk
        Write-Host "  Found: $($disk.FriendlyName) - $sizeGB GB" -ForegroundColor Green
        $report += "2.8TB Drive: $($disk.FriendlyName) - $sizeGB GB"
    }
}

if ($largeDisks.Count -eq 0) {
    Write-Host "⚠️  No 2.8TB drives found" -ForegroundColor Yellow
}

Write-Host ""

# PHASE 5: SCAN MOUNTED VOLUMES
Write-Host "🔍 PHASE 5: Scanning mounted volumes..." -ForegroundColor Yellow
Write-Host ""

$mountedVolumes = Get-Volume | Where-Object { $_.DriveType -eq "Fixed" -or $_.DriveType -eq "Removable" }
foreach ($vol in $mountedVolumes) {
    if ($vol.Size -gt 2TB) {
        $mountPoint = (Get-PSDrive | Where-Object { $_.Name -eq $vol.DriveLetter }).Root
        Write-Host "  Volume: $($vol.FileSystemLabel)" -ForegroundColor Cyan
        Write-Host "    Size: $([math]::Round($vol.Size/1GB,2)) GB" -ForegroundColor White
        Write-Host "    Free: $([math]::Round($vol.SizeRemaining/1GB,2)) GB" -ForegroundColor White
        Write-Host "    Mount: $mountPoint" -ForegroundColor White
        
        $report += "Mounted Volume: $($vol.FileSystemLabel)"
        $report += "  Size: $([math]::Round($vol.Size/1GB,2)) GB"
        $report += "  Free: $([math]::Round($vol.SizeRemaining/1GB,2)) GB"
        $report += "  Mount: $mountPoint"
        
        # Scan contents if accessible
        if ($mountPoint -and (Test-Path $mountPoint)) {
            Write-Host "    Scanning contents..." -ForegroundColor Yellow
            $topLevel = Get-ChildItem $mountPoint -ErrorAction SilentlyContinue | Select-Object -First 20
            Write-Host "    Top-level items: $($topLevel.Count)" -ForegroundColor White
            $report += "  Top-level items: $($topLevel.Count)"
            
            foreach ($item in $topLevel) {
                Write-Host "      • $($item.Name)" -ForegroundColor Gray
                $report += "    - $($item.Name)"
            }
        }
        Write-Host ""
    }
}

# PHASE 6: CHECK /Volumes
Write-Host "🔍 PHASE 6: Checking /Volumes directory..." -ForegroundColor Yellow
Write-Host ""

if (Test-Path "/Volumes") {
    $volumes = Get-ChildItem "/Volumes" -ErrorAction SilentlyContinue
    $ghostVolumes = $volumes | Where-Object { $_.Name -like "*GHOST*" -or $_.Name -like "*ghost*" }
    
    if ($ghostVolumes.Count -gt 0) {
        Write-Host "Found GHOST volume(s) in /Volumes:" -ForegroundColor Green
        foreach ($vol in $ghostVolumes) {
            Write-Host "  • $($vol.Name)" -ForegroundColor Cyan
            $report += "GHOST Volume: $($vol.Name)"
            
            # Scan contents
            $contents = Get-ChildItem $vol.FullName -ErrorAction SilentlyContinue | Select-Object -First 50
            Write-Host "    Items: $($contents.Count)" -ForegroundColor White
            $report += "  Items: $($contents.Count)"
            
            foreach ($item in $contents | Select-Object -First 10) {
                Write-Host "      - $($item.Name)" -ForegroundColor Gray
                $report += "    - $($item.Name)"
            }
        }
    } else {
        Write-Host "⚠️  No GHOST volumes found in /Volumes" -ForegroundColor Yellow
    }
}

Write-Host ""

# SUMMARY
Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  SCAN COMPLETE                                    ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Save report
$report | Out-File $REPORT_FILE -Encoding utf8
Write-Host "📄 Report saved to: $REPORT_FILE" -ForegroundColor Cyan
Write-Host ""

Write-Host "✅ GHOST Drive scan complete!" -ForegroundColor Green

