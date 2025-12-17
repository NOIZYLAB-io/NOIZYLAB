# FIX VS CODE TERMINAL CORRUPTION - Remove rob/lucy.sh
# Fixes terminal issues when running scripts in VS Code
# Rob Sonic Protocol | GORUNFREE

Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Red
Write-Host "║  FIXING VS CODE TERMINAL CORRUPTION              ║" -ForegroundColor Red
Write-Host "║  Removing rob/lucy.sh from VS Code                ║" -ForegroundColor Red
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Red
Write-Host ""

$VSCODE_SETTINGS = "$HOME/Library/Application Support/Code/User/settings.json"
$BACKUP_DIR = "$HOME/CODE_MASTER/backups/$(Get-Date -Format 'yyyyMMdd_HHmmss')"
New-Item -ItemType Directory -Force -Path $BACKUP_DIR | Out-Null

Write-Host "📦 Backup location: $BACKUP_DIR" -ForegroundColor Cyan
Write-Host ""

# PHASE 1: BACKUP VS CODE SETTINGS
Write-Host "🔍 PHASE 1: Backing up VS Code settings..." -ForegroundColor Yellow
Write-Host ""

if (Test-Path $VSCODE_SETTINGS) {
    Copy-Item $VSCODE_SETTINGS "$BACKUP_DIR/vscode_settings.json.backup" -Force
    Write-Host "  ✓ Backed up VS Code settings" -ForegroundColor Green
    
    $settings = Get-Content $VSCODE_SETTINGS -Raw | ConvertFrom-Json
    
    # Check for lucy references
    $settingsJson = Get-Content $VSCODE_SETTINGS -Raw
    if ($settingsJson -match "lucy|rob/lucy") {
        Write-Host "  ⚠️  Found lucy references in VS Code settings" -ForegroundColor Yellow
    } else {
        Write-Host "  ✓ No lucy references found" -ForegroundColor Green
    }
} else {
    Write-Host "  ⚠️  VS Code settings not found" -ForegroundColor Yellow
    $settings = @{} | ConvertTo-Json | ConvertFrom-Json
}

Write-Host ""

# PHASE 2: FIX TERMINAL CONFIGURATION
Write-Host "🔍 PHASE 2: Fixing terminal configuration..." -ForegroundColor Yellow
Write-Host ""

# Create clean terminal settings
$cleanSettings = @{
    "terminal.integrated.defaultProfile.osx" = "zsh"
    "terminal.integrated.profiles.osx" = @{
        "zsh" = @{
            "path" = "/bin/zsh"
            "args" = @("-l")
        }
        "bash" = @{
            "path" = "/bin/bash"
        }
    }
    "terminal.integrated.shell.osx" = "/bin/zsh"
    "terminal.integrated.shellArgs.osx" = @("-l")
    "terminal.integrated.env.osx" = @{
        "SHELL" = "/bin/zsh"
    }
    "terminal.integrated.cwd" = "`${workspaceFolder}"
    "terminal.integrated.inheritEnv" = $true
    "terminal.integrated.automationProfile.osx" = @{
        "path" = "/bin/zsh"
    }
}

# Merge with existing settings (if any)
if (Test-Path $VSCODE_SETTINGS) {
    try {
        $existing = Get-Content $VSCODE_SETTINGS -Raw | ConvertFrom-Json
        $merged = $existing | ConvertTo-Json -Depth 10 | ConvertFrom-Json
        
        # Remove any lucy references
        $mergedJson = $merged | ConvertTo-Json -Depth 10
        $mergedJson = $mergedJson -replace '.*lucy.*\n', ''
        $mergedJson = $mergedJson -replace '.*rob/lucy.*\n', ''
        
        # Add/update terminal settings
        foreach ($key in $cleanSettings.Keys) {
            $mergedJsonObj = $mergedJson | ConvertFrom-Json
            $mergedJsonObj | Add-Member -NotePropertyName $key -NotePropertyValue $cleanSettings[$key] -Force
            $mergedJson = $mergedJsonObj | ConvertTo-Json -Depth 10
        }
        
        $mergedJson | Set-Content $VSCODE_SETTINGS -NoNewline
        Write-Host "  ✓ Updated VS Code settings with clean terminal config" -ForegroundColor Green
    } catch {
        Write-Host "  ⚠️  Error updating settings, creating clean version" -ForegroundColor Yellow
        $cleanSettings | ConvertTo-Json -Depth 10 | Set-Content $VSCODE_SETTINGS
        Write-Host "  ✓ Created clean VS Code settings" -ForegroundColor Green
    }
} else {
    # Create new settings file
    $cleanSettings | ConvertTo-Json -Depth 10 | Set-Content $VSCODE_SETTINGS
    Write-Host "  ✓ Created new VS Code settings" -ForegroundColor Green
}

Write-Host ""

# PHASE 3: CHECK VS CODE TASKS
Write-Host "🔍 PHASE 3: Checking VS Code tasks..." -ForegroundColor Yellow
Write-Host ""

$tasksFile = "$HOME/Library/Application Support/Code/User/tasks.json"
if (Test-Path $tasksFile) {
    $tasksContent = Get-Content $tasksFile -Raw
    if ($tasksContent -match "lucy|rob/lucy") {
        Copy-Item $tasksFile "$BACKUP_DIR/tasks.json.backup" -Force
        $tasksContent = $tasksContent -replace '.*lucy.*\n', ''
        $tasksContent = $tasksContent -replace '.*rob/lucy.*\n', ''
        $tasksContent | Set-Content $tasksFile -NoNewline
        Write-Host "  ✓ Cleaned tasks.json" -ForegroundColor Green
    } else {
        Write-Host "  ✓ tasks.json is clean" -ForegroundColor Green
    }
} else {
    Write-Host "  ✓ No tasks.json found" -ForegroundColor Green
}

Write-Host ""

# PHASE 4: CHECK WORKSPACE SETTINGS
Write-Host "🔍 PHASE 4: Checking workspace settings..." -ForegroundColor Yellow
Write-Host ""

$workspaceFiles = Get-ChildItem -Path $HOME -Recurse -File -Filter "*.code-workspace" -ErrorAction SilentlyContinue | 
    Where-Object { $_.FullName -notmatch 'CODE_MASTER|Library|Trash|Downloads' } |
    Select-Object -First 5

foreach ($workspace in $workspaceFiles) {
    $content = Get-Content $workspace.FullName -Raw
    if ($content -match "lucy|rob/lucy") {
        Copy-Item $workspace.FullName "$BACKUP_DIR/$(Split-Path $workspace.Name -Leaf).backup" -Force
        $content = $content -replace '.*lucy.*\n', ''
        $content = $content -replace '.*rob/lucy.*\n', ''
        $content | Set-Content $workspace.FullName -NoNewline
        Write-Host "  ✓ Cleaned: $($workspace.Name)" -ForegroundColor Green
    }
}

Write-Host ""

# PHASE 5: FIX TERMINAL PROFILE
Write-Host "🔍 PHASE 5: Creating clean terminal profile..." -ForegroundColor Yellow
Write-Host ""

# Ensure .zshrc is clean
if (Test-Path "$HOME/.zshrc") {
    $zshrcContent = Get-Content "$HOME/.zshrc" -Raw
    if ($zshrcContent -match "lucy|rob/lucy") {
        Copy-Item "$HOME/.zshrc" "$BACKUP_DIR/.zshrc.backup" -Force
        $zshrcContent = $zshrcContent -replace '.*lucy.*\n', ''
        $zshrcContent = $zshrcContent -replace '.*rob/lucy.*\n', ''
        $zshrcContent | Set-Content "$HOME/.zshrc" -NoNewline
        Write-Host "  ✓ Cleaned .zshrc" -ForegroundColor Green
    }
}

Write-Host ""

# PHASE 6: CREATE CLEAN VS CODE SETTINGS FILE
Write-Host "🔍 PHASE 6: Creating clean VS Code settings..." -ForegroundColor Yellow
Write-Host ""

$cleanVSCodeSettings = @"
{
    "terminal.integrated.defaultProfile.osx": "zsh",
    "terminal.integrated.profiles.osx": {
        "zsh": {
            "path": "/bin/zsh",
            "args": ["-l"],
            "icon": "terminal"
        },
        "bash": {
            "path": "/bin/bash",
            "icon": "terminal-bash"
        }
    },
    "terminal.integrated.shell.osx": "/bin/zsh",
    "terminal.integrated.shellArgs.osx": ["-l"],
    "terminal.integrated.env.osx": {
        "SHELL": "/bin/zsh"
    },
    "terminal.integrated.cwd": "`${workspaceFolder}",
    "terminal.integrated.inheritEnv": true,
    "terminal.integrated.automationProfile.osx": {
        "path": "/bin/zsh"
    },
    "files.exclude": {
        "**/.git": true,
        "**/.DS_Store": true
    }
}
"@

# Save clean settings
$cleanVSCodeSettings | Set-Content "$HOME/vscode_settings_clean.json" -NoNewline
Write-Host "  ✓ Created: vscode_settings_clean.json" -ForegroundColor Green
Write-Host "  Copy this to VS Code settings if needed" -ForegroundColor Cyan

Write-Host ""

# SUMMARY
Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  VS CODE TERMINAL FIX COMPLETE                   ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""
Write-Host "✅ FIXES APPLIED:" -ForegroundColor Green
Write-Host "  • VS Code terminal configuration fixed" -ForegroundColor White
Write-Host "  • Removed lucy references from settings" -ForegroundColor White
Write-Host "  • Clean terminal profile created" -ForegroundColor White
Write-Host "  • All files backed up to: $BACKUP_DIR" -ForegroundColor White
Write-Host ""

Write-Host "✅ NEXT STEPS:" -ForegroundColor Green
Write-Host "  1. Close VS Code completely (Cmd+Q)" -ForegroundColor White
Write-Host "  2. Wait 5 seconds" -ForegroundColor White
Write-Host "  3. Reopen VS Code" -ForegroundColor White
Write-Host "  4. Open a NEW terminal (Ctrl+`)" -ForegroundColor White
Write-Host "  5. Test: whoami (should show: rsp_ms)" -ForegroundColor White
Write-Host "  6. Test: echo `$SHELL (should show: /bin/zsh)" -ForegroundColor White
Write-Host ""

if (Test-Path "$HOME/vscode_settings_fixed.json") {
    Write-Host "💡 TIP: If issues persist, copy:" -ForegroundColor Yellow
    Write-Host "   cp ~/vscode_settings_fixed.json ~/Library/Application\ Support/Code/User/settings.json" -ForegroundColor Cyan
    Write-Host ""
}

Write-Host "🔥 VS Code terminal corruption fixed! 🚀" -ForegroundColor Green

