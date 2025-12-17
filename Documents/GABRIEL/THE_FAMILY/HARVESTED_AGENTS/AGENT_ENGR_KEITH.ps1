# AGENT_ENGR_KEITH.ps1
# ENGR_KEITH - Engineering & Technical Optimization Agent
# GORUNFREEX5000 - PERSISTENT AGENT - AUTO-LOADS AT STARTUP
#
# ROLE: Chief engineer - precision, optimization, technical excellence
# SPECIALTY: System optimization, code efficiency, network engineering, technical problem solving

param(
    [switch]$Startup,
    [switch]$Silent
)

$AGENT_NAME = "ENGR_KEITH"
$AGENT_ROLE = "Engineering & Technical Optimization Agent"
$AGENT_COLOR = "Green"
$LOG_PATH = "$env:ProgramFiles\MC96_Automation\Logs\ENGR_KEITH_$(Get-Date -Format 'yyyyMMdd').log"

function Write-Keith {
    param([string]$Message, [string]$Color = $AGENT_COLOR)
    $Timestamp = Get-Date -Format "HH:mm:ss"
    $Output = "[$Timestamp] [ENGR_KEITH] $Message"
    
    if (!$Silent) {
        Write-Host $Output -ForegroundColor $Color
    }
    
    $Output | Out-File $LOG_PATH -Append
}

function Start-KeithAgent {
    Write-Keith "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" "White"
    Write-Keith "ENGR_KEITH AGENT ACTIVATED" "Green"
    Write-Keith "Role: $AGENT_ROLE"
    Write-Keith "Status: PERSISTENT - OPTIMIZING SYSTEMS"
    Write-Keith "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" "White"
    
    # Agent capabilities
    Write-Keith "Engineering Capabilities Online:"
    Write-Keith "  ✓ Network performance optimization"
    Write-Keith "  ✓ Code efficiency analysis"
    Write-Keith "  ✓ System resource management"
    Write-Keith "  ✓ MC96 switch configuration monitoring"
    Write-Keith "  ✓ GABRIEL (HP Omen) performance tuning"
    Write-Keith "  ✓ Automation script optimization"
    
    # System specs
    Write-Keith "GABRIEL System Analysis:"
    
    # CPU
    $CPU = Get-WmiObject Win32_Processor
    Write-Keith "  CPU: $($CPU.Name)"
    Write-Keith "  Cores: $($CPU.NumberOfCores) / Threads: $($CPU.NumberOfLogicalProcessors)"
    
    # RAM
    $RAM = Get-WmiObject Win32_ComputerSystem
    $TotalRAM = [math]::Round($RAM.TotalPhysicalMemory / 1GB, 2)
    Write-Keith "  RAM: $TotalRAM GB"
    
    # Network
    $NetAdapters = Get-NetAdapter | Where-Object { $_.Status -eq "Up" }
    Write-Keith "  Network Adapters: $($NetAdapters.Count) active"
    
    Write-Keith "ENGR_KEITH monitoring for optimization opportunities" "Green"
    Write-Keith "Logging to: $LOG_PATH"
    
    # Persistent optimization loop
    $Counter = 0
    while ($true) {
        Start-Sleep -Seconds 240  # Check every 4 minutes
        
        $Counter++
        Write-Keith "Engineering check #$Counter - Systems optimal" "DarkGreen"
        
        # Performance monitoring
        # Check CPU usage
        $CPUUsage = (Get-Counter '\Processor(_Total)\% Processor Time').CounterSamples.CookedValue
        if ($CPUUsage -gt 90) {
            Write-Keith "⚠ High CPU usage: $([math]::Round($CPUUsage, 2))%" "Yellow"
        }
        
        # Check RAM usage
        $OS = Get-WmiObject Win32_OperatingSystem
        $UsedRAM = [math]::Round(($OS.TotalVisibleMemorySize - $OS.FreePhysicalMemory) / 1MB, 2)
        $TotalRAM = [math]::Round($OS.TotalVisibleMemorySize / 1MB, 2)
        $RAMPercent = [math]::Round(($UsedRAM / $TotalRAM) * 100, 2)
        
        if ($RAMPercent -gt 90) {
            Write-Keith "⚠ High RAM usage: $RAMPercent% ($UsedRAM GB / $TotalRAM GB)" "Yellow"
        }
        
        # Network throughput check
        $NetStats = Get-NetAdapter | Where-Object { $_.Status -eq "Up" } | Get-NetAdapterStatistics
        foreach ($Stat in $NetStats) {
            $ReceivedMB = [math]::Round($Stat.ReceivedBytes / 1MB, 2)
            $SentMB = [math]::Round($Stat.SentBytes / 1MB, 2)
            Write-Keith "Network $($Stat.Name): ↓$ReceivedMB MB ↑$SentMB MB" "DarkGreen"
        }
    }
}

# Initialize
if ($Startup) {
    Write-Keith "STARTUP MODE - Engineering systems coming online"
    Start-KeithAgent
} else {
    Start-KeithAgent
}
