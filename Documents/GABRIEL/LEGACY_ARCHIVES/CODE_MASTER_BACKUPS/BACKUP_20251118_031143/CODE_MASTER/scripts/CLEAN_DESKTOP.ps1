# CLEAN & ORGANIZE DESKTOP - MC96
# Rob Sonic Protocol | GORUNFREE

Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  CLEANING & ORGANIZING DESKTOP                     ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$DESKTOP = "$HOME/Desktop"
$ORGANIZED_DIR = "$DESKTOP/ORGANIZED_$(Get-Date -Format 'yyyyMMdd')"
$LOG_FILE = "$HOME/CODE_MASTER/logs/desktop_clean_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"

New-Item -ItemType Directory -Force -Path $ORGANIZED_DIR | Out-Null
New-Item -ItemType Directory -Force -Path "$HOME/CODE_MASTER/logs" | Out-Null

function Write-Log {
    param($Message, $Color = "White")
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logMessage = "[$timestamp] $Message"
    Write-Host $logMessage -ForegroundColor $Color
    Add-Content -Path $LOG_FILE -Value $logMessage
}

Write-Log "=== DESKTOP CLEANUP STARTED ===" "Cyan"

# PHASE 1: CREATE ORGANIZATION FOLDERS
Write-Log "PHASE 1: Creating organization folders..." "Yellow"

$folders = @{
    "Documents" = @(".pdf", ".doc", ".docx", ".txt", ".rtf", ".pages")
    "Images" = @(".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".heic", ".psd")
    "Videos" = @(".mp4", ".mov", ".avi", ".mkv", ".m4v", ".wmv")
    "Audio" = @(".mp3", ".wav", ".aac", ".m4a", ".flac", ".ogg")
    "Archives" = @(".zip", ".rar", ".7z", ".tar", ".gz", ".dmg")
    "Code" = @(".py", ".js", ".sh", ".ps1", ".json", ".html", ".css", ".md")
    "Spreadsheets" = @(".xls", ".xlsx", ".csv", ".numbers")
    "Presentations" = @(".ppt", ".pptx", ".key")
    "Downloads" = @()  # For misc downloads
    "Projects" = @()   # For project folders
}

foreach ($folderName in $folders.Keys) {
    $folderPath = Join-Path $ORGANIZED_DIR $folderName
    New-Item -ItemType Directory -Force -Path $folderPath | Out-Null
    Write-Log "  ✓ Created: $folderName" "Green"
}

Write-Host ""

# PHASE 2: ORGANIZE FILES BY TYPE
Write-Log "PHASE 2: Organizing files by type..." "Yellow"

$items = Get-ChildItem $DESKTOP -File -ErrorAction SilentlyContinue | 
    Where-Object { $_.Name -notlike ".*" -and $_.Name -ne "Desktop.ini" }

$movedCount = 0
foreach ($item in $items) {
    $ext = $item.Extension.ToLower()
    $moved = $false
    
    foreach ($folderName in $folders.Keys) {
        $extensions = $folders[$folderName]
        if ($extensions -contains $ext -or ($extensions.Count -eq 0 -and $folderName -eq "Downloads")) {
            $destPath = Join-Path $ORGANIZED_DIR $folderName $item.Name
            if (Test-Path $destPath) {
                $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
                $nameWithoutExt = [System.IO.Path]::GetFileNameWithoutExtension($item.Name)
                $destPath = Join-Path $ORGANIZED_DIR $folderName "${nameWithoutExt}_${timestamp}$ext"
            }
            Move-Item $item.FullName $destPath -Force -ErrorAction SilentlyContinue
            Write-Log "  Moved: $($item.Name) → $folderName" "Cyan"
            $moved = $true
            $movedCount++
            break
        }
    }
    
    if (-not $moved) {
        # Move to Downloads folder
        $destPath = Join-Path $ORGANIZED_DIR "Downloads" $item.Name
        if (Test-Path $destPath) {
            $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
            $nameWithoutExt = [System.IO.Path]::GetFileNameWithoutExtension($item.Name)
            $destPath = Join-Path $ORGANIZED_DIR "Downloads" "${nameWithoutExt}_${timestamp}$ext"
        }
        Move-Item $item.FullName $destPath -Force -ErrorAction SilentlyContinue
        Write-Log "  Moved: $($item.Name) → Downloads" "Cyan"
        $movedCount++
    }
}

Write-Host ""

# PHASE 3: ORGANIZE FOLDERS
Write-Log "PHASE 3: Organizing folders..." "Yellow"

$foldersOnDesktop = Get-ChildItem $DESKTOP -Directory -ErrorAction SilentlyContinue | 
    Where-Object { $_.Name -notlike ".*" -and $_.Name -ne "ORGANIZED_*" }

foreach ($folder in $foldersOnDesktop) {
    $destPath = Join-Path $ORGANIZED_DIR "Projects" $folder.Name
    if (Test-Path $destPath) {
        $destPath = Join-Path $ORGANIZED_DIR "Projects" "${folder.Name}_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
    }
    Move-Item $folder.FullName $destPath -Force -ErrorAction SilentlyContinue
    Write-Log "  Moved folder: $($folder.Name) → Projects" "Cyan"
    $movedCount++
}

Write-Host ""

# PHASE 4: CREATE DESKTOP SHORTCUTS
Write-Log "PHASE 4: Creating desktop shortcuts..." "Yellow"

# Keep important shortcuts
$importantItems = @(
    "GHOST_DRIVE",
    "MissionControl96"
)

foreach ($itemName in $importantItems) {
    $itemPath = Join-Path $DESKTOP $itemName
    if (Test-Path $itemPath) {
        Write-Log "  ✓ Kept: $itemName" "Green"
    }
}

Write-Host ""

# PHASE 5: SUMMARY
Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  CLEANUP COMPLETE                                 ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

Write-Log "=== CLEANUP SUMMARY ===" "Cyan"
Write-Log "Items organized: $movedCount" "Green"
Write-Log "Organization folder: $ORGANIZED_DIR" "Green"
Write-Host ""

Write-Host "✅ DESKTOP CLEANED & ORGANIZED!" -ForegroundColor Green
Write-Host "📁 All items moved to: $ORGANIZED_DIR" -ForegroundColor Cyan
Write-Host "📄 Log saved to: $LOG_FILE" -ForegroundColor Cyan
Write-Host ""

