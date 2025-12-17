# SCAN MissionControl96 - Hidden GHOST Drive Folder
# Rob Sonic Protocol | GORUNFREE

Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  SCANNING MissionControl96 (GHOST Drive)          ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$MISSION_CONTROL = "/Users/rsp_ms/Desktop/MissionControl96"
$REPORT_FILE = "$HOME/CODE_MASTER/MISSIONCONTROL96_SCAN_REPORT.txt"
$report = @()

# PHASE 1: LOCATE MissionControl96
Write-Host "🔍 PHASE 1: Locating MissionControl96..." -ForegroundColor Yellow
Write-Host ""

if (Test-Path $MISSION_CONTROL) {
    Write-Host "✓ Found: $MISSION_CONTROL" -ForegroundColor Green
    $report += "Location: $MISSION_CONTROL"
    $report += "Status: Found"
    $report += ""
} else {
    Write-Host "⚠️  MissionControl96 not found at: $MISSION_CONTROL" -ForegroundColor Yellow
    
    # Search for it
    $found = Get-ChildItem "$HOME/Desktop" -Force -ErrorAction SilentlyContinue | 
        Where-Object { $_.Name -like "*Mission*" -or $_.Name -like "*MC96*" }
    
    if ($found) {
        Write-Host "Found similar folder(s):" -ForegroundColor Cyan
        foreach ($item in $found) {
            Write-Host "  • $($item.FullName)" -ForegroundColor White
            $MISSION_CONTROL = $item.FullName
        }
    } else {
        Write-Host "❌ MissionControl96 not found on Desktop" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""

# PHASE 2: SCAN STRUCTURE
Write-Host "🔍 PHASE 2: Scanning folder structure..." -ForegroundColor Yellow
Write-Host ""

$totalItems = (Get-ChildItem $MISSION_CONTROL -Recurse -ErrorAction SilentlyContinue | Measure-Object).Count
$totalFiles = (Get-ChildItem $MISSION_CONTROL -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count
$totalDirs = (Get-ChildItem $MISSION_CONTROL -Recurse -Directory -ErrorAction SilentlyContinue | Measure-Object).Count

$totalSize = (Get-ChildItem $MISSION_CONTROL -Recurse -File -ErrorAction SilentlyContinue | 
    Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum

Write-Host "📊 STATISTICS:" -ForegroundColor Cyan
Write-Host "  Total items: $totalItems" -ForegroundColor White
Write-Host "  Files: $totalFiles" -ForegroundColor White
Write-Host "  Directories: $totalDirs" -ForegroundColor White
Write-Host "  Total size: $([math]::Round($totalSize/1GB,2)) GB" -ForegroundColor White
Write-Host ""

$report += "=== STATISTICS ==="
$report += "Total items: $totalItems"
$report += "Files: $totalFiles"
$report += "Directories: $totalDirs"
$report += "Total size: $([math]::Round($totalSize/1GB,2)) GB"
$report += ""

# PHASE 3: TOP-LEVEL CONTENTS
Write-Host "🔍 PHASE 3: Top-level contents..." -ForegroundColor Yellow
Write-Host ""

$topLevel = Get-ChildItem $MISSION_CONTROL -ErrorAction SilentlyContinue
Write-Host "Found $($topLevel.Count) top-level item(s):" -ForegroundColor Green
Write-Host ""

$report += "=== TOP-LEVEL CONTENTS ==="

foreach ($item in $topLevel) {
    $itemCount = (Get-ChildItem $item.FullName -Recurse -ErrorAction SilentlyContinue | Measure-Object).Count
    $itemSize = (Get-ChildItem $item.FullName -Recurse -File -ErrorAction SilentlyContinue | 
        Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum / 1GB
    
    $type = if ($item.PSIsContainer) { "DIR" } else { "FILE" }
    $sizeStr = if ($item.PSIsContainer) { "$([math]::Round($itemSize,2)) GB" } else { "$([math]::Round($item.Length/1MB,2)) MB" }
    
    Write-Host "  • $($item.Name) [$type]" -ForegroundColor Cyan
    Write-Host "    Items: $itemCount | Size: $sizeStr" -ForegroundColor White
    Write-Host ""
    
    $report += "$($item.Name) [$type] - Items: $itemCount | Size: $sizeStr"
}

$report += ""

# PHASE 4: FILE TYPES
Write-Host "🔍 PHASE 4: Analyzing file types..." -ForegroundColor Yellow
Write-Host ""

$fileTypes = Get-ChildItem $MISSION_CONTROL -Recurse -File -ErrorAction SilentlyContinue | 
    Group-Object Extension | 
    Sort-Object Count -Descending | 
    Select-Object -First 20

Write-Host "Most common file types:" -ForegroundColor Green
foreach ($type in $fileTypes) {
    $typeName = if ($type.Name) { $type.Name } else { "(no extension)" }
    Write-Host "  $typeName : $($type.Count) files" -ForegroundColor White
    $report += "File type: $typeName - $($type.Count) files"
}

Write-Host ""

# PHASE 5: LARGEST FILES
Write-Host "🔍 PHASE 5: Largest files..." -ForegroundColor Yellow
Write-Host ""

$largestFiles = Get-ChildItem $MISSION_CONTROL -Recurse -File -ErrorAction SilentlyContinue | 
    Sort-Object Length -Descending | 
    Select-Object -First 10

Write-Host "Top 10 largest files:" -ForegroundColor Green
foreach ($file in $largestFiles) {
    $sizeGB = [math]::Round($file.Length / 1GB, 2)
    $relPath = $file.FullName.Replace($MISSION_CONTROL, ".")
    Write-Host "  $relPath" -ForegroundColor Cyan
    Write-Host "    $sizeGB GB" -ForegroundColor White
    $report += "Large file: $relPath - $sizeGB GB"
}

Write-Host ""

# PHASE 6: CHECK FOR SPECIFIC CONTENT
Write-Host "🔍 PHASE 6: Checking for specific content..." -ForegroundColor Yellow
Write-Host ""

$keywords = @("GHOST", "backup", "Time Machine", "TM_BackUp", "MC_RESCUE", "code", "scripts", "projects")
foreach ($keyword in $keywords) {
    $matches = Get-ChildItem $MISSION_CONTROL -Recurse -ErrorAction SilentlyContinue | 
        Where-Object { $_.Name -like "*$keyword*" } | 
        Select-Object -First 5
    
    if ($matches) {
        Write-Host "  Found '$keyword':" -ForegroundColor Cyan
        foreach ($match in $matches) {
            $relPath = $match.FullName.Replace($MISSION_CONTROL, ".")
            Write-Host "    • $relPath" -ForegroundColor White
            $report += "Keyword '$keyword': $relPath"
        }
    }
}

Write-Host ""

# PHASE 7: CHECK DISK SPACE
Write-Host "🔍 PHASE 7: Checking disk space..." -ForegroundColor Yellow
Write-Host ""

$drive = (Get-Item $MISSION_CONTROL).PSDrive
if ($drive) {
    $freeSpace = $drive.Free / 1GB
    $usedSpace = ($drive.Used) / 1GB
    Write-Host "  Drive: $($drive.Name)" -ForegroundColor Cyan
    Write-Host "  Free space: $([math]::Round($freeSpace,2)) GB" -ForegroundColor White
    Write-Host "  Used space: $([math]::Round($usedSpace,2)) GB" -ForegroundColor White
    $report += "Drive: $($drive.Name) - Free: $([math]::Round($freeSpace,2)) GB"
}

Write-Host ""

# SUMMARY
Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  SCAN COMPLETE                                    ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Save report
$report | Out-File $REPORT_FILE -Encoding utf8
Write-Host "📄 Full report saved to: $REPORT_FILE" -ForegroundColor Cyan
Write-Host ""

Write-Host "✅ MissionControl96 scan complete!" -ForegroundColor Green
Write-Host ""
Write-Host "📁 Location: $MISSION_CONTROL" -ForegroundColor White
Write-Host "📊 Size: $([math]::Round($totalSize/1GB,2)) GB" -ForegroundColor White
Write-Host "📄 Files: $totalFiles" -ForegroundColor White

