# GABRIEL_MASTER_TUNNEL.ps1
# MC96 Tunnel System v2.0 - Windows (Gabriel) Deployment
# Run as Administrator

$LogFile = "$HOME\.mc96\tunnel.log"
$WorkDir = "$HOME\.mc96"
New-Item -ItemType Directory -Force -Path $WorkDir | Out-Null

Write-Host "=== MC96 TUNNEL SYSTEM v2.0 (GABRIEL) ===" -ForegroundColor Cyan
Add-Content $LogFile "=== MC96 TUNNEL SYSTEM v2.0 (GABRIEL) ==="
Add-Content $LogFile (Get-Date)

# 1. Health Monitor Script (Python)
$MonitorScript = @"
import http.server
import json
import socketserver
import subprocess

PORT = 9999

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            tunnel_status = "down"
            # Simple check for cloudflared process
            output = subprocess.getoutput("tasklist /FI \"IMAGENAME eq cloudflared.exe\"")
            if "cloudflared.exe" in output:
                tunnel_status = "up"
                
            response = {
                "system": "GABRIEL",
                "status": "ok",
                "tunnel": tunnel_status,
                "version": "2.0"
            }
            self.wfile.write(json.dumps(response).encode())

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Health Monitor serving on {PORT}")
    httpd.serve_forever()
"@
Set-Content -Path "$WorkDir\health_monitor.py" -Value $MonitorScript

# 2. Watchdog Script (PowerShell)
$WatchdogScript = @"
while (`$true) {
    # Check Health Monitor
    `$monitor = Get-Process python -ErrorAction SilentlyContinue | Where-Object { `$_.MainWindowTitle -like "*health_monitor*" }
    if (!`$monitor) {
        Start-Process python -ArgumentList "$WorkDir\health_monitor.py" -WindowStyle Hidden
    }

    # Check Tunnel
    `$tunnel = Get-Process cloudflared -ErrorAction SilentlyContinue
    if (!`$tunnel) {
        Write-Host "Starting Tunnel..."
        Start-Process cloudflared -ArgumentList "tunnel run GABRIEL" -WindowStyle Hidden
    }
    
    Start-Sleep -Seconds 300 # 5 Minute Check
}
"@
Set-Content -Path "$WorkDir\run_watchdog.ps1" -Value $WatchdogScript

# 3. Create Scheduled Task for Auto-Start
$TaskName = "MC96_Tunnel_Watchdog"
$Action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-ExecutionPolicy Bypass -File $WorkDir\run_watchdog.ps1"
$Trigger = New-ScheduledTaskTrigger -AtLogon
$Principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Principal $Principal

Write-Host "[SUCCESS] Scheduled Task '$TaskName' created." -ForegroundColor Green
Write-Host "Please ensure cloudflared is authenticated and 'GABRIEL' tunnel is configured."
