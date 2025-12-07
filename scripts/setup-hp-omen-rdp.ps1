# HP-OMEN Remote Desktop Quick Setup
# Run as Administrator on the HP-OMEN machine

# Script to enable RDP, SSH, and configure firewall
# Usage: powershell -ExecutionPolicy Bypass -File setup-hp-omen-rdp.ps1

Write-Host "🖥️  HP-OMEN Remote Desktop Configuration" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Check for admin privileges
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "❌ This script must be run as Administrator!" -ForegroundColor Red
    exit 1
}

# Function to enable RDP
function Enable-RDP {
    Write-Host "`n🔧 Enabling Remote Desktop Protocol (RDP)..." -ForegroundColor Yellow
    
    try {
        # Enable RDP
        Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections" -Value 0 -ErrorAction Stop
        
        # Verify
        $status = Get-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections"
        if ($status.fDenyTSConnections -eq 0) {
            Write-Host "✅ RDP Enabled" -ForegroundColor Green
        }
    }
    catch {
        Write-Host "❌ Failed to enable RDP: $_" -ForegroundColor Red
    }
}

# Function to configure firewall
function Configure-Firewall {
    Write-Host "`n🔥 Configuring Windows Firewall..." -ForegroundColor Yellow
    
    try {
        # Remove existing RDP rule if present
        Remove-NetFirewallRule -DisplayName "Allow RDP" -ErrorAction SilentlyContinue
        
        # Add new RDP firewall rule
        New-NetFirewallRule -Name "Allow-RDP-3389" -DisplayName "Allow RDP (3389)" -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 3389 -ErrorAction Stop
        
        Write-Host "✅ Firewall rule added for RDP (port 3389)" -ForegroundColor Green
        
        # Add SSH rule if available
        Remove-NetFirewallRule -DisplayName "SSH Server" -ErrorAction SilentlyContinue
        New-NetFirewallRule -Name "Allow-SSH-22" -DisplayName "Allow SSH (22)" -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22 -ErrorAction SilentlyContinue
        Write-Host "✅ Firewall rule added for SSH (port 22)" -ForegroundColor Green
    }
    catch {
        Write-Host "⚠️  Firewall configuration warning: $_" -ForegroundColor Yellow
    }
}

# Function to enable SSH
function Enable-SSH {
    Write-Host "`n🔐 Setting up SSH Server..." -ForegroundColor Yellow
    
    try {
        # Check if SSH is already installed
        $sshStatus = Get-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0 -ErrorAction SilentlyContinue
        
        if ($sshStatus.State -ne "Installed") {
            Write-Host "📦 Installing OpenSSH Server..." -ForegroundColor Cyan
            Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0 -ErrorAction Stop
        }
        
        # Start SSH service
        Start-Service sshd -ErrorAction Stop
        Set-Service -Name sshd -StartupType Automatic -ErrorAction Stop
        
        Write-Host "✅ SSH Server enabled and running" -ForegroundColor Green
    }
    catch {
        Write-Host "⚠️  SSH setup warning: $_" -ForegroundColor Yellow
    }
}

# Function to display system info
function Display-SystemInfo {
    Write-Host "`n📊 System Information:" -ForegroundColor Cyan
    Write-Host "======================" -ForegroundColor Cyan
    
    try {
        $computerName = $env:COMPUTERNAME
        $ipAddress = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -notlike "127.*"} | Select-Object -First 1).IPAddress
        $osInfo = Get-CimInstance -ClassName Win32_OperatingSystem
        
        Write-Host "Computer Name: $computerName" -ForegroundColor White
        Write-Host "IP Address: $ipAddress" -ForegroundColor White
        Write-Host "OS: $($osInfo.Caption)" -ForegroundColor White
        Write-Host "System: HP-OMEN" -ForegroundColor Cyan
        
        Write-Host "`n🎮 Remote Connection Details:" -ForegroundColor Cyan
        Write-Host "RDP Address: $computerName`:3389 or $ipAddress`:3389" -ForegroundColor Green
        Write-Host "SSH Address: $computerName or $ipAddress" -ForegroundColor Green
        Write-Host "Port 22 (SSH), Port 3389 (RDP)" -ForegroundColor White
    }
    catch {
        Write-Host "⚠️  Error retrieving system info: $_" -ForegroundColor Yellow
    }
}

# Function to verify configuration
function Verify-Configuration {
    Write-Host "`n✔️  Verification Results:" -ForegroundColor Cyan
    Write-Host "========================" -ForegroundColor Cyan
    
    # Check RDP
    $rdpStatus = Get-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections" -ErrorAction SilentlyContinue
    if ($rdpStatus.fDenyTSConnections -eq 0) {
        Write-Host "✅ RDP: ENABLED" -ForegroundColor Green
    } else {
        Write-Host "❌ RDP: DISABLED" -ForegroundColor Red
    }
    
    # Check SSH
    $sshService = Get-Service sshd -ErrorAction SilentlyContinue
    if ($sshService -and $sshService.Status -eq "Running") {
        Write-Host "✅ SSH: RUNNING" -ForegroundColor Green
    } else {
        Write-Host "⚠️  SSH: NOT RUNNING" -ForegroundColor Yellow
    }
    
    # Check firewall rules
    $rdpRule = Get-NetFirewallRule -DisplayName "Allow RDP*" -ErrorAction SilentlyContinue
    if ($rdpRule) {
        Write-Host "✅ Firewall RDP Rule: EXISTS" -ForegroundColor Green
    } else {
        Write-Host "❌ Firewall RDP Rule: MISSING" -ForegroundColor Red
    }
}

# Main execution
Clear-Host
Enable-RDP
Configure-Firewall
Enable-SSH
Display-SystemInfo
Verify-Configuration

Write-Host "`n✨ Setup Complete!" -ForegroundColor Green
Write-Host "You can now connect to your HP-OMEN from remote machines." -ForegroundColor White
Write-Host "`n📝 Next Steps:" -ForegroundColor Cyan
Write-Host "1. Share the IP address and computer name above" -ForegroundColor White
Write-Host "2. Use Remote Desktop app or SSH to connect" -ForegroundColor White
Write-Host "3. Consider changing the RDP port for security" -ForegroundColor White
Write-Host "4. Set a strong password if you haven't already" -ForegroundColor White

Write-Host "`n🔒 Security Tips:" -ForegroundColor Yellow
Write-Host "- Change RDP port from 3389 to something custom (e.g., 3390)" -ForegroundColor White
Write-Host "- Enable Network Level Authentication (NLA)" -ForegroundColor White
Write-Host "- Use strong passwords (20+ characters)" -ForegroundColor White
Write-Host "- Consider using VPN for external access" -ForegroundColor White

Write-Host "`n" -ForegroundColor Cyan
