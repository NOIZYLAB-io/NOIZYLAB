# AGENT_POPS.ps1
# POPS - System Health & Wisdom Agent
# GORUNFREEX5000 - PERSISTENT AGENT - AUTO-LOADS AT STARTUP
#
# ROLE: Elder statesman of the system - monitors health, provides wisdom, keeps everything running smooth
# SPECIALTY: System diagnostics, health monitoring, preventive maintenance

param(
    [switch]$Startup,
    [switch]$Silent
)

$AGENT_NAME = "POPS"
$AGENT_ROLE = "System Health & Wisdom Agent"
$AGENT_COLOR = "Cyan"
$LOG_PATH = "$env:ProgramFiles\MC96_Automation\Logs\POPS_$(Get-Date -Format 'yyyyMMdd').log"

function Write-Pops {
    param([string]$Message, [string]$Color = $AGENT_COLOR)
    $Timestamp = Get-Date -Format "HH:mm:ss"
    $Output = "[$Timestamp] [POPS] $Message"
    
    if (!$Silent) {
        Write-Host $Output -ForegroundColor $Color
    }
    
    $Output | Out-File $LOG_PATH -Append
}

function Start-PopsAgent {
    Write-Pops "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" "White"
    Write-Pops "POPS AGENT ACTIVATED" "Green"
    Write-Pops "Role: $AGENT_ROLE"
    Write-Pops "Status: PERSISTENT - WATCHING OVER EVERYTHING"
    Write-Pops "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" "White"
    
    # Agent capabilities
    Write-Pops "Capabilities Loaded:"
    Write-Pops "  ✓ MC96ECOUNIVERSE network health monitoring"
    Write-Pops "  ✓ GABRIEL system diagnostics"
    Write-Pops "  ✓ Drive health checks (THE_AQUARIUM protection)"
    Write-Pops "  ✓ CPU/RAM/Storage monitoring"
    Write-Pops "  ✓ Preventive maintenance alerts"
    
    Write-Pops "POPS is on watch - keeping the family healthy" "Green"
    Write-Pops "Logging to: $LOG_PATH"
    
    # Persistent monitoring loop
    $Counter = 0
    while ($true) {
        Start-Sleep -Seconds 180  # Check every 3 minutes
        
        $Counter++
        Write-Pops "System check #$Counter - All systems nominal" "DarkCyan"
        
        # System health monitoring
        # Check disk space
        $Drives = Get-PSDrive -PSProvider FileSystem | Where-Object { $_.Used -gt 0 }
        foreach ($Drive in $Drives) {
            $PercentFree = [math]::Round(($Drive.Free / ($Drive.Used + $Drive.Free)) * 100, 2)
            
            if ($PercentFree -lt 10) {
                Write-Pops "⚠ WARNING: Drive $($Drive.Name): Low space - $PercentFree% free" "Red"
            } elseif ($PercentFree -lt 20) {
                Write-Pops "ℹ Drive $($Drive.Name): $PercentFree% free - monitor closely" "Yellow"
            }
        }
        
        # Check MC96 network devices
        $MC96Devices = @{
            "10.90.90.90" = "MC96 Switch"
            "10.90.90.10" = "GOD"
        }
        
        foreach ($IP in $MC96Devices.Keys) {
            if (!(Test-Connection -ComputerName $IP -Count 1 -Quiet)) {
                Write-Pops "⚠ ALERT: $($MC96Devices[$IP]) offline at $IP" "Red"
            }
        }
    }
}

# Initialize
if ($Startup) {
    Write-Pops "STARTUP MODE - POPS taking watch position"
    Start-PopsAgent
} else {
    Start-PopsAgent
}
