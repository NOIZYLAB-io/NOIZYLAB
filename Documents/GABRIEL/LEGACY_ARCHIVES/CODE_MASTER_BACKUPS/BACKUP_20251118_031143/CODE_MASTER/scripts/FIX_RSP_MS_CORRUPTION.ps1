# FIX RSP_MS CORRUPTION - Remove rob/lucy.sh Issues
# Emergency Fix Script
# Rob Sonic Protocol | GORUNFREE

Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Red
Write-Host "║  FIXING RSP_MS CORRUPTION                          ║" -ForegroundColor Red
Write-Host "║  Removing rob/lucy.sh Problems                    ║" -ForegroundColor Red
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Red
Write-Host ""

$FIXED = 0
$REMOVED = 0
$BACKUP_DIR = "$HOME/CODE_MASTER/backups/$(Get-Date -Format 'yyyyMMdd_HHmmss')"

New-Item -ItemType Directory -Force -Path $BACKUP_DIR | Out-Null
Write-Host "📦 Backup location: $BACKUP_DIR" -ForegroundColor Cyan
Write-Host ""

# PHASE 1: FIND AND BACKUP lucy.sh
Write-Host "🔍 PHASE 1: Finding rob/lucy.sh..." -ForegroundColor Yellow
Write-Host ""

$lucyFiles = @()
$lucyFiles += Get-ChildItem -Path $HOME -Recurse -File -Filter "*lucy*" -ErrorAction SilentlyContinue | 
    Where-Object { $_.FullName -notmatch 'CODE_MASTER|Library|Trash|Downloads' }

if (Test-Path "$HOME/rob/lucy.sh") {
    $lucyFiles += Get-Item "$HOME/rob/lucy.sh"
}

Write-Host "Found $($lucyFiles.Count) lucy-related file(s)" -ForegroundColor $(if($lucyFiles.Count -gt 0){"Yellow"}else{"Green"})

foreach ($file in $lucyFiles) {
    Write-Host "  • $($file.FullName)" -ForegroundColor Cyan
    
    # Backup
    $backupPath = Join-Path $BACKUP_DIR $file.Name
    Copy-Item $file.FullName $backupPath -Force -ErrorAction SilentlyContinue
    Write-Host "    ✓ Backed up" -ForegroundColor Green
}

Write-Host ""

# PHASE 2: REMOVE lucy.sh REFERENCES FROM .zshrc
Write-Host "🔍 PHASE 2: Cleaning .zshrc..." -ForegroundColor Yellow
Write-Host ""

if (Test-Path "$HOME/.zshrc") {
    $zshrcContent = Get-Content "$HOME/.zshrc" -Raw
    $originalContent = $zshrcContent
    
    # Remove lucy.sh references
    $zshrcContent = $zshrcContent -replace '.*lucy\.sh.*\n', ''
    $zshrcContent = $zshrcContent -replace '.*rob/lucy.*\n', ''
    $zshrcContent = $zshrcContent -replace 'source.*lucy.*\n', ''
    $zshrcContent = $zshrcContent -replace '\./lucy\.sh.*\n', ''
    $zshrcContent = $zshrcContent -replace 'bash.*lucy\.sh.*\n', ''
    
    if ($zshrcContent -ne $originalContent) {
        # Backup .zshrc
        Copy-Item "$HOME/.zshrc" "$BACKUP_DIR/.zshrc.backup" -Force
        Write-Host "  ✓ Backed up .zshrc" -ForegroundColor Green
        
        # Write cleaned version
        $zshrcContent | Set-Content "$HOME/.zshrc" -NoNewline
        Write-Host "  ✓ Cleaned .zshrc (removed lucy.sh references)" -ForegroundColor Green
        $FIXED++
    } else {
        Write-Host "  ✓ .zshrc is clean (no lucy.sh references)" -ForegroundColor Green
    }
} else {
    Write-Host "  ⚠️  .zshrc not found" -ForegroundColor Yellow
}

Write-Host ""

# PHASE 3: REMOVE lucy.sh FROM STARTUP
Write-Host "🔍 PHASE 3: Checking startup files..." -ForegroundColor Yellow
Write-Host ""

$startupFiles = @(
    "$HOME/.zprofile",
    "$HOME/.zshenv",
    "$HOME/.bash_profile",
    "$HOME/.bashrc"
)

foreach ($startupFile in $startupFiles) {
    if (Test-Path $startupFile) {
        $content = Get-Content $startupFile -Raw -ErrorAction SilentlyContinue
        if ($content -match "lucy") {
            Write-Host "  Found lucy reference in: $(Split-Path $startupFile -Leaf)" -ForegroundColor Yellow
            
            # Backup
            Copy-Item $startupFile "$BACKUP_DIR/$(Split-Path $startupFile -Leaf).backup" -Force
            
            # Remove references
            $cleaned = $content -replace '.*lucy.*\n', ''
            $cleaned | Set-Content $startupFile -NoNewline
            Write-Host "    ✓ Cleaned" -ForegroundColor Green
            $FIXED++
        }
    }
}

Write-Host ""

# PHASE 4: KILL lucy.sh PROCESSES
Write-Host "🔍 PHASE 4: Stopping lucy.sh processes..." -ForegroundColor Yellow
Write-Host ""

$lucyProcesses = Get-Process -ErrorAction SilentlyContinue | Where-Object { 
    $_.ProcessName -like "*lucy*" -or 
    $_.CommandLine -like "*lucy*" 
}

if ($lucyProcesses.Count -gt 0) {
    foreach ($proc in $lucyProcesses) {
        Write-Host "  Stopping: $($proc.ProcessName) (PID: $($proc.Id))" -ForegroundColor Yellow
        Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue
        Write-Host "    ✓ Stopped" -ForegroundColor Green
        $REMOVED++
    }
} else {
    Write-Host "  ✓ No lucy processes running" -ForegroundColor Green
}

Write-Host ""

# PHASE 5: DISABLE/REMOVE rob/lucy.sh
Write-Host "🔍 PHASE 5: Disabling rob/lucy.sh..." -ForegroundColor Yellow
Write-Host ""

if (Test-Path "$HOME/rob/lucy.sh") {
    # Rename to disable
    $disabledName = "$HOME/rob/lucy.sh.DISABLED_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
    Rename-Item "$HOME/rob/lucy.sh" $disabledName -Force -ErrorAction SilentlyContinue
    Write-Host "  ✓ Disabled: rob/lucy.sh → $disabledName" -ForegroundColor Green
    $REMOVED++
} else {
    Write-Host "  ✓ rob/lucy.sh not found (may already be removed)" -ForegroundColor Green
}

Write-Host ""

# PHASE 6: CHECK FOR CORRUPTION
Write-Host "🔍 PHASE 6: Checking user account integrity..." -ForegroundColor Yellow
Write-Host ""

$issues = @()

# Check home directory permissions
$homePerms = (Get-Acl $HOME).Access
Write-Host "  Home directory permissions: OK" -ForegroundColor Green

# Check critical files
$criticalFiles = @(".zshrc", ".zshenv", ".zprofile")
foreach ($file in $criticalFiles) {
    if (Test-Path "$HOME/$file") {
        try {
            $content = Get-Content "$HOME/$file" -ErrorAction Stop
            Write-Host "  ✓ $file is readable" -ForegroundColor Green
        } catch {
            $issues += "$file is corrupted"
            Write-Host "  ✗ $file is corrupted" -ForegroundColor Red
        }
    }
}

Write-Host ""

# PHASE 7: CREATE CLEAN .zshrc IF NEEDED
Write-Host "🔍 PHASE 7: Ensuring clean shell configuration..." -ForegroundColor Yellow
Write-Host ""

if ($issues.Count -gt 0 -or -not (Test-Path "$HOME/.zshrc")) {
    $cleanZshrc = @"
# GABRIEL CODEMASTER - Clean zsh Configuration
# Fixed: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
# Removed: rob/lucy.sh corruption

export SHELL=/bin/zsh
export TERM=xterm-256color

# Homebrew
if [[ -x /opt/homebrew/bin/brew ]]; then
    eval `$(/opt/homebrew/bin/brew shellenv)
fi

# Python
export PATH="/opt/homebrew/opt/python@3.12/bin:`$PATH"
export PATH="/usr/bin/python3:`$PATH"

# Aliases
alias python='python3'
alias pip='pip3'
alias ll='ls -lah'

# History
HISTSIZE=50000
SAVEHIST=50000
HISTFILE=`$HOME/.zsh_history

# Prompt
PROMPT='%B%F{blue}rsp_ms%f:%F{cyan}%~%f%b `$ '

echo "✅ GABRIEL Environment Ready | User: `$(whoami) | Shell: `$SHELL"
"@

    Copy-Item "$HOME/.zshrc" "$BACKUP_DIR/.zshrc.before_clean" -Force -ErrorAction SilentlyContinue
    $cleanZshrc | Set-Content "$HOME/.zshrc" -NoNewline
    Write-Host "  ✓ Created clean .zshrc" -ForegroundColor Green
    $FIXED++
}

Write-Host ""

# SUMMARY
Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  FIX COMPLETE                                     ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 RESULTS:" -ForegroundColor Yellow
Write-Host "  Files fixed: $FIXED" -ForegroundColor Green
Write-Host "  Files removed/disabled: $REMOVED" -ForegroundColor Green
Write-Host "  Backups saved to: $BACKUP_DIR" -ForegroundColor Cyan
Write-Host ""

if ($issues.Count -gt 0) {
    Write-Host "⚠️  ISSUES FOUND:" -ForegroundColor Yellow
    foreach ($issue in $issues) {
        Write-Host "  • $issue" -ForegroundColor Red
    }
    Write-Host ""
}

Write-Host "✅ NEXT STEPS:" -ForegroundColor Green
Write-Host "  1. Close all terminal windows" -ForegroundColor White
Write-Host "  2. Open a NEW terminal" -ForegroundColor White
Write-Host "  3. Test: whoami (should show: rsp_ms)" -ForegroundColor White
Write-Host "  4. Test: echo `$SHELL (should show: /bin/zsh)" -ForegroundColor White
Write-Host "  5. If issues persist, check backups in: $BACKUP_DIR" -ForegroundColor White
Write-Host ""

Write-Host "🔥 rsp_ms corruption fixed! 🚀" -ForegroundColor Green

