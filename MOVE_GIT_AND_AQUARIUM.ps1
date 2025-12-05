# MOVE GIT REPOS & THE_AQUARIUM TO CODE_MASTER
# Rob Sonic Protocol | GORUNFREE

Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  MOVING GIT REPOS & THE_AQUARIUM                    ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$CODE_MASTER = "$HOME/CODE_MASTER"
$GIT_REPOS_DIR = "$CODE_MASTER/git-repos"
$AQUARIUM_DIR = "$CODE_MASTER/THE_AQUARIUM"

$MOVED_REPOS = 0
$MOVED_AQUARIUM = 0

# PHASE 1: FIND & MOVE GIT REPOSITORIES
Write-Host "🔍 PHASE 1: Finding Git Repositories..." -ForegroundColor Yellow
Write-Host ""

$gitRepos = Get-ChildItem -Path $HOME -Recurse -Directory -Filter ".git" -ErrorAction SilentlyContinue | 
    Where-Object { 
        $_.FullName -notmatch 'node_modules|\.cache|Library|Trash|Downloads|Applications|Movies|Music|Pictures|OneDrive|Desktop|CODE_MASTER' -and
        $_.Parent.FullName -ne $HOME
    } | 
    Select-Object -ExpandProperty Parent -Unique

Write-Host "Found $($gitRepos.Count) Git repositories" -ForegroundColor Green
Write-Host ""

foreach ($repo in $gitRepos) {
    $repoName = $repo.Name
    $destPath = Join-Path $GIT_REPOS_DIR $repoName
    
    try {
        if (Test-Path $destPath) {
            $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
            $destPath = Join-Path $GIT_REPOS_DIR "${repoName}_${timestamp}"
        }
        
        Write-Host "  Moving: $repoName" -ForegroundColor Cyan
        Copy-Item -Path $repo.FullName -Destination $destPath -Recurse -Force -ErrorAction Stop
        $MOVED_REPOS++
        Write-Host "    ✓ Moved to: $destPath" -ForegroundColor Green
    } catch {
        Write-Host "    ✗ Failed: $_" -ForegroundColor Red
    }
}

Write-Host ""

# PHASE 2: FIND & MOVE THE_AQUARIUM
Write-Host "🔍 PHASE 2: Finding THE_AQUARIUM..." -ForegroundColor Yellow
Write-Host ""

# Check home directory
$aquariumPaths = @()
if (Test-Path "$HOME/THE_AQUARIUM") {
    $aquariumPaths += "$HOME/THE_AQUARIUM"
}
if (Test-Path "$HOME/THE_AQUARIUM") {
    $aquariumPaths += "$HOME/THE_AQUARIUM"
}

# Search for any AQUARIUM directories
Get-ChildItem -Path $HOME -Directory -ErrorAction SilentlyContinue | 
    Where-Object { $_.Name -like "*AQUARIUM*" -or $_.Name -like "*aquarium*" } | 
    ForEach-Object { $aquariumPaths += $_.FullName }

# Remove duplicates
$aquariumPaths = $aquariumPaths | Select-Object -Unique

Write-Host "Found $($aquariumPaths.Count) AQUARIUM location(s)" -ForegroundColor Green
Write-Host ""

foreach ($aquariumPath in $aquariumPaths) {
    if (Test-Path $aquariumPath) {
        try {
            Write-Host "  Moving: $aquariumPath" -ForegroundColor Cyan
            
            # Get folder name
            $folderName = Split-Path $aquariumPath -Leaf
            
            if ($folderName -eq "THE_AQUARIUM") {
                $destPath = $AQUARIUM_DIR
            } else {
                $destPath = Join-Path $AQUARIUM_DIR $folderName
            }
            
            # If destination exists, merge or rename
            if (Test-Path $destPath) {
                $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
                $destPath = Join-Path $AQUARIUM_DIR "${folderName}_${timestamp}"
            }
            
            Copy-Item -Path $aquariumPath -Destination $destPath -Recurse -Force -ErrorAction Stop
            $MOVED_AQUARIUM++
            Write-Host "    ✓ Moved to: $destPath" -ForegroundColor Green
        } catch {
            Write-Host "    ✗ Failed: $_" -ForegroundColor Red
        }
    }
}

Write-Host ""

# PHASE 3: SUMMARY
Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  MOVE COMPLETE                                    ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 STATISTICS:" -ForegroundColor Yellow
Write-Host "  Git repositories moved: $MOVED_REPOS" -ForegroundColor Green
Write-Host "  THE_AQUARIUM locations moved: $MOVED_AQUARIUM" -ForegroundColor Green
Write-Host ""

Write-Host "📁 LOCATIONS:" -ForegroundColor Cyan
Write-Host "  Git repos: $GIT_REPOS_DIR" -ForegroundColor White
Write-Host "  THE_AQUARIUM: $AQUARIUM_DIR" -ForegroundColor White
Write-Host ""

Write-Host "✅ All Git repos and THE_AQUARIUM organized!" -ForegroundColor Green

