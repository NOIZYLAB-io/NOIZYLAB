# CODE MASTER - Scan, Test, Heal & Organize
# Rob Sonic Protocol | GORUNFREE

Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  CODE MASTER - SCAN, TEST, HEAL & ORGANIZE         ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$CODE_MASTER = "$HOME/CODE_MASTER"
$ERRORS = @()
$MOVED = 0

# PHASE 1: SCAN
Write-Host "🔍 PHASE 1: SCANNING FOR CODE FILES..." -ForegroundColor Yellow
Write-Host ""

$codeFiles = Get-ChildItem -Path $HOME -Recurse -File -Include *.sh,*.ps1,*.py,*.js,*.ts,*.json -ErrorAction SilentlyContinue | 
    Where-Object { 
        $_.FullName -notmatch 'node_modules|\.git|Library|Trash|Downloads|\.cache|\.venv|\.oh-my-zsh|Applications|Movies|Music|Pictures|Desktop|OneDrive' -and
        $_.Name -notlike ".*"
    }

Write-Host "Found $($codeFiles.Count) code files" -ForegroundColor Green
Write-Host ""

# PHASE 2: TEST & HEAL
Write-Host "🧪 PHASE 2: TESTING & HEALING..." -ForegroundColor Yellow
Write-Host ""

foreach ($file in $codeFiles) {
    $ext = $file.Extension.ToLower()
    $issues = @()
    
    # Test syntax
    try {
        switch ($ext) {
            ".sh" {
                # Test bash syntax
                $test = bash -n $file.FullName 2>&1
                if ($LASTEXITCODE -ne 0) { $issues += "Bash syntax error" }
            }
            ".ps1" {
                # Test PowerShell syntax
                $null = [System.Management.Automation.PSParser]::Tokenize((Get-Content $file.FullName -Raw), [ref]$null)
            }
            ".py" {
                # Test Python syntax
                $test = python3 -m py_compile $file.FullName 2>&1
                if ($LASTEXITCODE -ne 0) { $issues += "Python syntax error" }
            }
            ".js" {
                # Test JavaScript syntax
                $test = node --check $file.FullName 2>&1
                if ($LASTEXITCODE -ne 0) { $issues += "JavaScript syntax error" }
            }
        }
    } catch {
        $issues += "Test failed: $_"
    }
    
    if ($issues.Count -gt 0) {
        $ERRORS += [PSCustomObject]@{
            File = $file.FullName
            Issues = $issues -join ", "
        }
        Write-Host "⚠️  $($file.Name) - Issues found" -ForegroundColor Yellow
    } else {
        Write-Host "✅ $($file.Name) - OK" -ForegroundColor Green
    }
}

Write-Host ""

# PHASE 3: ORGANIZE
Write-Host "📦 PHASE 3: ORGANIZING INTO CODE_MASTER..." -ForegroundColor Yellow
Write-Host ""

foreach ($file in $codeFiles) {
    $ext = $file.Extension.ToLower()
    $dest = $null
    
    switch ($ext) {
        ".sh" { $dest = "$CODE_MASTER/scripts" }
        ".ps1" { $dest = "$CODE_MASTER/scripts" }
        ".py" { $dest = "$CODE_MASTER/python" }
        ".js" { $dest = "$CODE_MASTER/nodejs" }
        ".ts" { $dest = "$CODE_MASTER/nodejs" }
        ".json" { 
            if ($file.Name -eq "package.json") {
                $dest = "$CODE_MASTER/nodejs"
            } else {
                $dest = "$CODE_MASTER/config"
            }
        }
    }
    
    if ($dest -and $file.DirectoryName -ne $dest) {
        try {
            $destFile = Join-Path $dest $file.Name
            if (Test-Path $destFile) {
                # Add timestamp to avoid overwrite
                $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
                $nameWithoutExt = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
                $destFile = Join-Path $dest "${nameWithoutExt}_${timestamp}$($file.Extension)"
            }
            Copy-Item $file.FullName $destFile -Force
            $MOVED++
            Write-Host "  ✓ Moved: $($file.Name) → $dest" -ForegroundColor Green
        } catch {
            Write-Host "  ✗ Failed: $($file.Name) - $_" -ForegroundColor Red
        }
    }
}

Write-Host ""

# PHASE 4: SUMMARY
Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  SCAN COMPLETE                                    ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 STATISTICS:" -ForegroundColor Yellow
Write-Host "  Files scanned: $($codeFiles.Count)" -ForegroundColor White
Write-Host "  Files moved: $MOVED" -ForegroundColor Green
Write-Host "  Files with issues: $($ERRORS.Count)" -ForegroundColor $(if($ERRORS.Count -eq 0){"Green"}else{"Yellow"})
Write-Host ""

if ($ERRORS.Count -gt 0) {
    Write-Host "⚠️  FILES WITH ISSUES:" -ForegroundColor Yellow
    $ERRORS | Format-Table -AutoSize
    Write-Host ""
}

Write-Host "📁 CODE_MASTER LOCATION:" -ForegroundColor Cyan
Write-Host "  $CODE_MASTER" -ForegroundColor White
Write-Host ""
Write-Host "✅ All code organized!" -ForegroundColor Green

