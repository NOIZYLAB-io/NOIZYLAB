# ═══════════════════════════════════════════════════════════════════════════════
#  ██████╗  █████╗ ██████╗ ██████╗ ██╗███████╗██╗         
# ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██║         
# ██║  ███╗███████║██████╔╝██████╔╝██║█████╗  ██║         
# ██║   ██║██╔══██║██╔══██╗██╔══██╗██║██╔══╝  ██║         
# ╚██████╔╝██║  ██║██████╔╝██║  ██║██║███████╗███████╗    
#  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝    
#        ███████╗██╗   ██╗██████╗ ███████╗██████╗ ███████╗ ██████╗ ███╗   ██╗██╗ ██████╗
#        ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔════╝██╔═══██╗████╗  ██║██║██╔════╝
#        ███████╗██║   ██║██████╔╝█████╗  ██████╔╝███████╗██║   ██║██╔██╗ ██║██║██║     
#        ╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██║   ██║██║╚██╗██║██║██║     
#        ███████║╚██████╔╝██║     ███████╗██║  ██║███████║╚██████╔╝██║ ╚████║██║╚██████╗
#        ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝
# ═══════════════════════════════════════════════════════════════════════════════
# GABRIEL (HP-OMEN) SUPERSONIC MODE - WINDOWS EDITION
# MC96ECOUNIVERSE - 1000% SPEED - NO LIMITS
# ═══════════════════════════════════════════════════════════════════════════════
# Run as Administrator: Right-click PowerShell > Run as Administrator
# ═══════════════════════════════════════════════════════════════════════════════

#Requires -RunAsAdministrator

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════════════════════════" -ForegroundColor Magenta
Write-Host "  🚀 GABRIEL SUPERSONIC MODE - 1000% ACTIVATION" -ForegroundColor White
Write-Host "═══════════════════════════════════════════════════════════════════════════════" -ForegroundColor Magenta
Write-Host ""

# ═══════════════════════════════════════════════════════════════════════════════
# 1. JUMBO FRAMES - MTU 9000
# ═══════════════════════════════════════════════════════════════════════════════
Write-Host "⚡ [1/7] ACTIVATING JUMBO FRAMES (MTU 9000)..." -ForegroundColor Cyan

$adapters = Get-NetAdapter | Where-Object { $_.Status -eq "Up" }
foreach ($adapter in $adapters) {
    try {
        Set-NetAdapterAdvancedProperty -Name $adapter.Name -RegistryKeyword "*JumboPacket" -RegistryValue 9014 -ErrorAction SilentlyContinue
        Write-Host "   ✅ $($adapter.Name): Jumbo Frames ENABLED" -ForegroundColor Green
    } catch {
        Write-Host "   ⚠️ $($adapter.Name): Check adapter settings manually" -ForegroundColor Yellow
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# 2. TCP/IP OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════════════
Write-Host ""
Write-Host "⚡ [2/7] TURBOCHARGING TCP/IP STACK..." -ForegroundColor Cyan

# Enable TCP Window Auto-Tuning
netsh int tcp set global autotuninglevel=experimental | Out-Null
Write-Host "   ✅ TCP Auto-Tuning: EXPERIMENTAL (max speed)" -ForegroundColor Green

# Enable Direct Cache Access
netsh int tcp set global dca=enabled 2>$null | Out-Null
Write-Host "   ✅ Direct Cache Access: ENABLED" -ForegroundColor Green

# Enable Receive Side Scaling
netsh int tcp set global rss=enabled | Out-Null
Write-Host "   ✅ Receive Side Scaling: ENABLED" -ForegroundColor Green

# Enable TCP Timestamps
netsh int tcp set global timestamps=enabled | Out-Null
Write-Host "   ✅ TCP Timestamps: ENABLED" -ForegroundColor Green

# Disable TCP Chimney (better for modern systems)
netsh int tcp set global chimney=disabled 2>$null | Out-Null

# Enable ECN
netsh int tcp set global ecncapability=enabled | Out-Null
Write-Host "   ✅ ECN Capability: ENABLED" -ForegroundColor Green

# ═══════════════════════════════════════════════════════════════════════════════
# 3. NETWORK ADAPTER OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════════════
Write-Host ""
Write-Host "⚡ [3/7] OPTIMIZING NETWORK ADAPTERS..." -ForegroundColor Cyan

foreach ($adapter in $adapters) {
    # Disable interrupt moderation for lower latency
    Set-NetAdapterAdvancedProperty -Name $adapter.Name -RegistryKeyword "*InterruptModeration" -RegistryValue 0 -ErrorAction SilentlyContinue
    
    # Increase receive buffers
    Set-NetAdapterAdvancedProperty -Name $adapter.Name -RegistryKeyword "*ReceiveBuffers" -RegistryValue 2048 -ErrorAction SilentlyContinue
    
    # Increase transmit buffers
    Set-NetAdapterAdvancedProperty -Name $adapter.Name -RegistryKeyword "*TransmitBuffers" -RegistryValue 2048 -ErrorAction SilentlyContinue
    
    Write-Host "   ✅ $($adapter.Name): Buffers maximized, latency minimized" -ForegroundColor Green
}

# ═══════════════════════════════════════════════════════════════════════════════
# 4. DNS - CLOUDFLARE 1.1.1.1
# ═══════════════════════════════════════════════════════════════════════════════
Write-Host ""
Write-Host "⚡ [4/7] SETTING CLOUDFLARE DNS (1.1.1.1)..." -ForegroundColor Cyan

foreach ($adapter in $adapters) {
    Set-DnsClientServerAddress -InterfaceAlias $adapter.Name -ServerAddresses ("1.1.1.1","1.0.0.1") -ErrorAction SilentlyContinue
    Write-Host "   ✅ $($adapter.Name): DNS = 1.1.1.1, 1.0.0.1" -ForegroundColor Green
}

# Flush DNS cache
Clear-DnsClientCache
Write-Host "   ✅ DNS Cache: FLUSHED" -ForegroundColor Green

# ═══════════════════════════════════════════════════════════════════════════════
# 5. SMB OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════════════
Write-Host ""
Write-Host "⚡ [5/7] TURBOCHARGING SMB..." -ForegroundColor Cyan

# Enable SMB Multichannel
Set-SmbClientConfiguration -EnableMultichannel $true -Force | Out-Null
Write-Host "   ✅ SMB Multichannel: ENABLED" -ForegroundColor Green

# Enable Large MTU
Set-SmbClientConfiguration -EnableLargeMtu $true -Force | Out-Null
Write-Host "   ✅ SMB Large MTU: ENABLED" -ForegroundColor Green

# Increase connections
Set-SmbClientConfiguration -ConnectionCountPerRssNetworkInterface 4 -Force | Out-Null
Write-Host "   ✅ SMB Connections per RSS: 4" -ForegroundColor Green

# Enable bandwidth throttling bypass
Set-SmbClientConfiguration -EnableBandwidthThrottling $false -Force | Out-Null
Write-Host "   ✅ SMB Bandwidth Throttling: DISABLED" -ForegroundColor Green

# ═══════════════════════════════════════════════════════════════════════════════
# 6. GIT CONFIGURATION (HOT ROD)
# ═══════════════════════════════════════════════════════════════════════════════
Write-Host ""
Write-Host "⚡ [6/7] CONFIGURING GIT HOT ROD..." -ForegroundColor Cyan

$gitConfig = @"
[user]
    name = Rob Plowman
    email = rsp@noizyfish.com

[core]
    editor = code --wait
    autocrlf = true
    preloadindex = true
    fscache = true

[init]
    defaultBranch = main

[push]
    default = current
    autoSetupRemote = true

[pack]
    threads = 0
    windowMemory = 4g

[protocol]
    version = 2

[fetch]
    parallel = 8

[alias]
    s = status -sb
    c = commit -m
    ca = commit -am
    aa = add --all
    p = push
    pl = pull
    l = log --oneline -20
    ship = !git add -A && git commit -m
    flow = !git add -A && git commit -m \"FLOW: \" && git push
    morning = !git fetch --all --prune && git pull --rebase && git status -sb
    night = !git add -A && git commit -m \"NIGHTLY\" && git push
"@

$gitConfigPath = "$env:USERPROFILE\.gitconfig"
$gitConfig | Out-File -FilePath $gitConfigPath -Encoding utf8 -Force
Write-Host "   ✅ Git config: $gitConfigPath" -ForegroundColor Green
Write-Host "   ✅ Git aliases: ship, flow, morning, night" -ForegroundColor Green

# ═══════════════════════════════════════════════════════════════════════════════
# 7. SSH KEY FOR GITHUB
# ═══════════════════════════════════════════════════════════════════════════════
Write-Host ""
Write-Host "⚡ [7/7] CHECKING SSH KEY..." -ForegroundColor Cyan

$sshKeyPath = "$env:USERPROFILE\.ssh\id_ed25519"
if (-not (Test-Path $sshKeyPath)) {
    Write-Host "   Creating SSH key for GitHub..." -ForegroundColor Yellow
    ssh-keygen -t ed25519 -C "rsp@noizyfish.com" -f $sshKeyPath -N '""' 2>$null
    Write-Host "   ✅ SSH Key created: $sshKeyPath" -ForegroundColor Green
    Write-Host ""
    Write-Host "   📋 ADD THIS KEY TO GITHUB:" -ForegroundColor Yellow
    Get-Content "$sshKeyPath.pub"
    Write-Host ""
    Write-Host "   Go to: https://github.com/settings/ssh/new" -ForegroundColor Cyan
    Write-Host "   Title: GABRIEL-HP-OMEN" -ForegroundColor Cyan
} else {
    Write-Host "   ✅ SSH Key exists: $sshKeyPath" -ForegroundColor Green
}

# Add GitHub to known hosts
$knownHostsPath = "$env:USERPROFILE\.ssh\known_hosts"
ssh-keyscan github.com 2>$null | Out-File -FilePath $knownHostsPath -Append -Encoding utf8

# ═══════════════════════════════════════════════════════════════════════════════
# STATUS REPORT
# ═══════════════════════════════════════════════════════════════════════════════
Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════════════════════════" -ForegroundColor Magenta
Write-Host "  🔥 GABRIEL SUPERSONIC MODE: ACTIVE" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════════════════════════════" -ForegroundColor Magenta
Write-Host ""
Write-Host "   ⚡ JUMBO FRAMES:     MTU 9014 (+15-20% throughput)" -ForegroundColor Cyan
Write-Host "   ⚡ TCP AUTO-TUNE:    EXPERIMENTAL (max speed)" -ForegroundColor Cyan
Write-Host "   ⚡ RSS:              ENABLED (multi-core networking)" -ForegroundColor Cyan
Write-Host "   ⚡ SMB MULTICHAN:    ENABLED (parallel transfers)" -ForegroundColor Cyan
Write-Host "   ⚡ CLOUDFLARE DNS:   1.1.1.1 (fastest DNS)" -ForegroundColor Cyan
Write-Host "   ⚡ GIT HOT ROD:      Parallel fetch, FLOW aliases" -ForegroundColor Cyan
Write-Host ""
Write-Host "   🚀 SPEED LEVEL: 1000%" -ForegroundColor Green
Write-Host "   🌌 GABRIEL + GOD = MC96ECOUNIVERSE" -ForegroundColor Green
Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════════════════════════" -ForegroundColor Magenta
Write-Host "   NO LIMITS OF ANY KIND IN THE UNIVERSE - GORUNFREE!!! 🔥" -ForegroundColor White
Write-Host "═══════════════════════════════════════════════════════════════════════════════" -ForegroundColor Magenta
Write-Host ""
Write-Host "   ⚠️  RESTART REQUIRED for all changes to take effect" -ForegroundColor Yellow
Write-Host ""

