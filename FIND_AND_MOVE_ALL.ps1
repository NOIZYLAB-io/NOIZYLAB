# FIND & MOVE ALL GIT REPOS & THE_AQUARIUM
# Comprehensive search and move script

Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  FINDING ALL GIT REPOS & THE_AQUARIUM              ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$CODE_MASTER = "$HOME/CODE_MASTER"
$GIT_REPOS_DIR = "$CODE_MASTER/git-repos"
$AQUARIUM_DIR = "$CODE_MASTER/THE_AQUARIUM"

# Ensure directories exist
New-Item -ItemType Directory -Force -Path $GIT_REPOS_DIR, $AQUARIUM_DIR | Out-Null

$foundRepos = @()
$foundAquarium = @()

# Search for Git repos in common locations
Write-Host "🔍 Searching for Git repositories..." -ForegroundColor Yellow

$searchPaths = @(
    $HOME,
    "$HOME/Documents",
    "$HOME/NOIZYLAB",
    "$HOME/GABRIEL",
    "$HOME/Desktop",
    "$HOME/Projects"
)

foreach ($searchPath in $searchPaths) {
    if (Test-Path $searchPath) {
        Write-Host "  Searching: $searchPath" -ForegroundColor Cyan
        $repos = Get-ChildItem -Path $searchPath -Recurse -Directory -Filter ".git" -Depth 5 -ErrorAction SilentlyContinue |
            Where-Object { 
                $_.FullName -notmatch 'node_modules|\.cache|Library|Trash|Downloads|Applications|Movies|Music|Pictures|OneDrive|CODE_MASTER' 
            }
        
        foreach ($repo in $repos) {
            $repoPath = Split-Path $repo.FullName -Parent
            if ($repoPath -notin $foundRepos) {
                $foundRepos += $repoPath
                Write-Host "    ✓ Found: $repoPath" -ForegroundColor Green
            }
        }
    }
}

Write-Host ""
Write-Host "Found $($foundRepos.Count) Git repositories" -ForegroundColor Green
Write-Host ""

# Search for THE_AQUARIUM
Write-Host "🔍 Searching for THE_AQUARIUM..." -ForegroundColor Yellow

foreach ($searchPath in $searchPaths) {
    if (Test-Path $searchPath) {
        $aquarium = Get-ChildItem -Path $searchPath -Recurse -Directory -ErrorAction SilentlyContinue |
            Where-Object { 
                $_.Name -like "*AQUARIUM*" -or $_.Name -like "*aquarium*" 
            } |
            Select-Object -First 10
        
        foreach ($aq in $aquarium) {
            if ($aq.FullName -notin $foundAquarium) {
                $foundAquarium += $aq.FullName
                Write-Host "    ✓ Found: $($aq.FullName)" -ForegroundColor Green
            }
        }
    }
}

Write-Host ""
Write-Host "Found $($foundAquarium.Count) AQUARIUM location(s)" -ForegroundColor Green
Write-Host ""

# Move Git repos
$MOVED_REPOS = 0
if ($foundRepos.Count -gt 0) {
    Write-Host "📦 Moving Git repositories..." -ForegroundColor Yellow
    foreach ($repoPath in $foundRepos) {
        $repoName = Split-Path $repoPath -Leaf
        $destPath = Join-Path $GIT_REPOS_DIR $repoName
        
        if (Test-Path $destPath) {
            $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
            $destPath = Join-Path $GIT_REPOS_DIR "${repoName}_${timestamp}"
        }
        
        try {
            Write-Host "  Moving: $repoName" -ForegroundColor Cyan
            Copy-Item -Path $repoPath -Destination $destPath -Recurse -Force -ErrorAction Stop
            $MOVED_REPOS++
            Write-Host "    ✓ Moved to: $destPath" -ForegroundColor Green
        } catch {
            Write-Host "    ✗ Failed: $_" -ForegroundColor Red
        }
    }
}

# Move THE_AQUARIUM
$MOVED_AQUARIUM = 0
if ($foundAquarium.Count -gt 0) {
    Write-Host ""
    Write-Host "📦 Moving THE_AQUARIUM..." -ForegroundColor Yellow
    foreach ($aqPath in $foundAquarium) {
        $aqName = Split-Path $aqPath -Leaf
        
        if ($aqName -eq "THE_AQUARIUM") {
            $destPath = $AQUARIUM_DIR
        } else {
            $destPath = Join-Path $AQUARIUM_DIR $aqName
        }
        
        if (Test-Path $destPath) {
            $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
            $destPath = Join-Path $AQUARIUM_DIR "${aqName}_${timestamp}"
        }
        
        try {
            Write-Host "  Moving: $aqName" -ForegroundColor Cyan
            Copy-Item -Path $aqPath -Destination $destPath -Recurse -Force -ErrorAction Stop
            $MOVED_AQUARIUM++
            Write-Host "    ✓ Moved to: $destPath" -ForegroundColor Green
        } catch {
            Write-Host "    ✗ Failed: $_" -ForegroundColor Red
        }
    }
}

# Summary
Write-Host ""
Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  COMPLETE                                         ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 RESULTS:" -ForegroundColor Yellow
Write-Host "  Git repositories found: $($foundRepos.Count)" -ForegroundColor White
Write-Host "  Git repositories moved: $MOVED_REPOS" -ForegroundColor Green
Write-Host "  THE_AQUARIUM found: $($foundAquarium.Count)" -ForegroundColor White
Write-Host "  THE_AQUARIUM moved: $MOVED_AQUARIUM" -ForegroundColor Green
Write-Host ""
Write-Host "📁 LOCATIONS:" -ForegroundColor Cyan
Write-Host "  Git repos: $GIT_REPOS_DIR" -ForegroundColor White
Write-Host "  THE_AQUARIUM: $AQUARIUM_DIR" -ForegroundColor White
Write-Host ""

if ($foundRepos.Count -eq 0 -and $foundAquarium.Count -eq 0) {
    Write-Host "⚠️  No Git repos or THE_AQUARIUM found in common locations" -ForegroundColor Yellow
    Write-Host "   They may be in a different location or not exist yet" -ForegroundColor Yellow
}

