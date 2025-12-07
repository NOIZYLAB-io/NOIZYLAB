# HP-OMEN Windows Boot Startup Script
# Place in: C:\Users\Gabriel\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
# Or use Task Scheduler for more control

# Initialize environment on boot
Write-Host "🚀 HP-OMEN Boot Startup - $(Get-Date)" -ForegroundColor Cyan

# ============================================================================
# ENVIRONMENT VARIABLES
# ============================================================================

$env:NOIZYLAB_HOME = "C:\NOIZYLAB"
$env:OMEN_DRIVES = @(
    "Z:",  # M2Ultra
    "Y:"   # Network shares
)

# ============================================================================
# START ESSENTIAL SERVICES
# ============================================================================

Write-Host "🔧 Starting essential services..." -ForegroundColor Yellow

# Verify RDP is running
$rdpService = Get-Service TermService -ErrorAction SilentlyContinue
if ($rdpService.Status -ne "Running") {
    Write-Host "Starting Remote Desktop Service..." -ForegroundColor Cyan
    Start-Service TermService
}

# Verify SSH is running
$sshService = Get-Service sshd -ErrorAction SilentlyContinue
if ($sshService -and $sshService.Status -ne "Running") {
    Write-Host "Starting SSH Service..." -ForegroundColor Cyan
    Start-Service sshd
}

# ============================================================================
# MOUNT NETWORK DRIVES
# ============================================================================

Write-Host "📁 Mounting network drives..." -ForegroundColor Yellow

# Mount M2Ultra (via SMB)
try {
    $m2Ultra_IP = "192.168.1.100"  # Update with actual M2Ultra IP
    $m2Ultra_User = "m2ultra"
    New-PSDrive -Name "M2Ultra" -PSProvider FileSystem -Root "\\$m2Ultra_IP\Users\m2ultra\Shares" -Credential (Get-Credential -UserName $m2Ultra_User -Message "Enter M2Ultra credentials") -ErrorAction SilentlyContinue
    Write-Host "✅ M2Ultra mounted" -ForegroundColor Green
}
catch {
    Write-Host "⚠️  M2Ultra mount warning: $_" -ForegroundColor Yellow
}

# ============================================================================
# DISPLAY SYSTEM INFO
# ============================================================================

Write-Host "`n📊 HP-OMEN System Information:" -ForegroundColor Cyan
Write-Host "=============================" -ForegroundColor Cyan
Write-Host "Computer: $env:COMPUTERNAME" -ForegroundColor White
Write-Host "User: $env:USERNAME" -ForegroundColor White
Write-Host "Time: $(Get-Date)" -ForegroundColor White

# Get IP address
$ipAddress = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -notlike "127.*"} | Select-Object -First 1).IPAddress
Write-Host "IP Address: $ipAddress" -ForegroundColor Cyan

# ============================================================================
# VERIFY SERVICES
# ============================================================================

Write-Host "`n✔️  Service Status:" -ForegroundColor Cyan
Write-Host "=================" -ForegroundColor Cyan

$rdpStatus = Get-Service TermService | Select-Object Status
Write-Host "RDP Service: $($rdpStatus.Status)" -ForegroundColor $(if ($rdpStatus.Status -eq "Running") { "Green" } else { "Red" })

$sshStatus = Get-Service sshd -ErrorAction SilentlyContinue | Select-Object Status
if ($sshStatus) {
    Write-Host "SSH Service: $($sshStatus.Status)" -ForegroundColor $(if ($sshStatus.Status -eq "Running") { "Green" } else { "Red" })
}

# ============================================================================
# CREATE DESKTOP SHORTCUT FOR QUICK LAUNCH
# ============================================================================

$desktopPath = [System.IO.Path]::Combine([System.Environment]::GetFolderPath('Desktop'))
$linkPath = "$desktopPath\Connect_to_M2Ultra.lnk"

# Create shortcut to SSH M2Ultra
$shell = New-Object -ComObject WScript.Shell
$link = $shell.CreateShortcut($linkPath)
$link.TargetPath = "powershell.exe"
$link.Arguments = "-NoExit -Command 'ssh m2ultra@192.168.1.100'"  # Update IP
$link.Description = "SSH to M2Ultra"
$link.Save()

Write-Host "`n✨ Boot startup complete!" -ForegroundColor Green
Write-Host "HP-OMEN is ready for remote access from M2Ultra" -ForegroundColor White
Write-Host "`n🎮 Quick Commands:" -ForegroundColor Cyan
Write-Host "ssh m2ultra@$(Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -notlike '127.*'} | Select-Object -First 1).IPAddress" -ForegroundColor Green
