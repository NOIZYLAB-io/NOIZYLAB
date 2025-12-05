# PowerShell: Inspiron Hot-Rod Script
# Cleans, updates, and optimizes Windows for speed and reliability

Write-Host "🚀 Starting Inspiron Hot-Rod Maintenance..." -ForegroundColor Cyan

# 1. Run Windows Update
Write-Host "[+] Running Windows Update..."
if (-not (Get-Module -ListAvailable -Name PSWindowsUpdate)) {
	Install-Module PSWindowsUpdate -Force -Scope CurrentUser
}
Import-Module PSWindowsUpdate -ErrorAction SilentlyContinue
if (Get-Command Get-WindowsUpdate -ErrorAction SilentlyContinue) {
	Get-WindowsUpdate -AcceptAll -Install -AutoReboot
} else {
	Write-Host "PSWindowsUpdate module not available." -ForegroundColor Yellow
}

# 2. Clean up disk
Write-Host "[+] Running Disk Cleanup..."
Cleanmgr /sageset:1
Cleanmgr /sagerun:1

# 3. Remove temp files
Write-Host "[+] Removing temp files..."
Remove-Item -Path $env:TEMP\* -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path C:\Windows\Temp\* -Recurse -Force -ErrorAction SilentlyContinue

# 4. Disable unnecessary startup programs
Write-Host "[+] Disabling unnecessary startup programs..."
Get-CimInstance Win32_StartupCommand | Remove-CimInstance
if (Get-Command Start-MpScan -ErrorAction SilentlyContinue) {
	Start-MpScan -ScanType QuickScan
} else {
	Write-Host "Windows Defender not available. Skipping malware scan." -ForegroundColor Yellow
}

# 7. Defragment drive (if HDD)
Write-Host "[+] Defragmenting drive..."
if ((Get-PhysicalDisk | Where-Object MediaType -eq 'HDD').Count -gt 0) {
	Optimize-Volume -DriveLetter C
} else {
	Write-Host "Drive C: is not an HDD. Skipping defragmentation." -ForegroundColor Yellow
}

Write-Host "✅ Inspiron Hot-Rod Maintenance Complete!" -ForegroundColor Green
Start-MpScan -ScanType QuickScan

# 7. Defragment drive (if HDD)
Write-Host "[+] Defragmenting drive..."
Optimize-Volume -DriveLetter C

Write-Host "✅ Inspiron Hot-Rod Maintenance Complete!" -ForegroundColor Green
