# Tailscale Setup Script for Windows - NOIZYLAB
# This script automates the installation and initial configuration of Tailscale on Windows
# Run this script in PowerShell as Administrator

param(
    [switch]$Force
)

Write-Host "=== NOIZYLAB Tailscale Setup for Windows ===" -ForegroundColor Cyan
Write-Host ""

# Check if running as Administrator
function Test-Administrator {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

if (-not (Test-Administrator)) {
    Write-Host "Error: This script must be run as Administrator" -ForegroundColor Red
    Write-Host "Please right-click PowerShell and select 'Run as Administrator'" -ForegroundColor Yellow
    exit 1
}

# Check if Tailscale is already installed
function Test-TailscaleInstalled {
    $tailscalePath = "$env:ProgramFiles\Tailscale\tailscale.exe"
    return Test-Path $tailscalePath
}

# Install Tailscale using winget
function Install-TailscaleWinget {
    Write-Host "Installing Tailscale using winget..." -ForegroundColor Yellow
    
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        winget install --id tailscale.tailscale -e --silent
        Write-Host "✓ Tailscale installed successfully via winget" -ForegroundColor Green
        return $true
    }
    return $false
}

# Install Tailscale using Chocolatey
function Install-TailscaleChoco {
    Write-Host "Checking for Chocolatey..." -ForegroundColor Yellow
    
    if (Get-Command choco -ErrorAction SilentlyContinue) {
        Write-Host "Installing Tailscale using Chocolatey..." -ForegroundColor Yellow
        choco install tailscale -y
        Write-Host "✓ Tailscale installed successfully via Chocolatey" -ForegroundColor Green
        return $true
    }
    return $false
}

# Download and install Tailscale manually
function Install-TailscaleManual {
    Write-Host "Downloading Tailscale installer..." -ForegroundColor Yellow
    
    $installerPath = "$env:TEMP\tailscale-setup.exe"
    $downloadUrl = "https://pkgs.tailscale.com/stable/tailscale-setup-latest.exe"
    
    try {
        Invoke-WebRequest -Uri $downloadUrl -OutFile $installerPath
        Write-Host "✓ Download complete" -ForegroundColor Green
        
        Write-Host "Running installer..." -ForegroundColor Yellow
        Start-Process -FilePath $installerPath -ArgumentList "/quiet" -Wait
        
        Write-Host "✓ Tailscale installed successfully" -ForegroundColor Green
        
        # Clean up
        Remove-Item $installerPath -Force -ErrorAction SilentlyContinue
        
        return $true
    }
    catch {
        Write-Host "Error downloading or installing Tailscale: $_" -ForegroundColor Red
        return $false
    }
}

# Start Tailscale service
function Start-TailscaleService {
    Write-Host ""
    Write-Host "Starting Tailscale service..." -ForegroundColor Yellow
    
    $service = Get-Service -Name "Tailscale" -ErrorAction SilentlyContinue
    
    if ($service) {
        if ($service.Status -ne "Running") {
            Start-Service -Name "Tailscale"
            Write-Host "✓ Tailscale service started" -ForegroundColor Green
        }
        else {
            Write-Host "✓ Tailscale service is already running" -ForegroundColor Green
        }
    }
    else {
        Write-Host "Warning: Tailscale service not found" -ForegroundColor Yellow
    }
}

# Launch Tailscale GUI
function Start-TailscaleGUI {
    Write-Host ""
    Write-Host "Launching Tailscale..." -ForegroundColor Yellow
    
    $tailscaleExe = "$env:ProgramFiles\Tailscale\tailscale-ipn.exe"
    
    if (Test-Path $tailscaleExe) {
        Start-Process $tailscaleExe
        Write-Host "✓ Tailscale GUI launched" -ForegroundColor Green
    }
}

# Show next steps
function Show-NextSteps {
    Write-Host ""
    Write-Host "=== Next Steps ===" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "1. Look for the Tailscale icon in your system tray (bottom-right)" -ForegroundColor White
    Write-Host "2. Click the icon and sign in with your account:" -ForegroundColor White
    Write-Host "   - Google, Microsoft, GitHub, or Email" -ForegroundColor Gray
    Write-Host "3. Your device will automatically join your Tailscale network" -ForegroundColor White
    Write-Host ""
    Write-Host "To check status, run: tailscale status" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "For detailed configuration, see: CODE_MASTER\TAILSCALE_SETUP.md" -ForegroundColor Gray
}

# Main execution
function Main {
    # Check if already installed
    if (Test-TailscaleInstalled) {
        Write-Host "✓ Tailscale is already installed" -ForegroundColor Green
        
        if (-not $Force) {
            Write-Host ""
            Write-Host "To reinstall, run with -Force parameter" -ForegroundColor Yellow
            Start-TailscaleService
            Start-TailscaleGUI
            exit 0
        }
    }
    
    Write-Host "Starting Tailscale installation..." -ForegroundColor Yellow
    Write-Host ""
    
    # Try installation methods in order of preference
    $installed = $false
    
    # Method 1: winget
    if (-not $installed) {
        $installed = Install-TailscaleWinget
    }
    
    # Method 2: Chocolatey
    if (-not $installed) {
        $installed = Install-TailscaleChoco
    }
    
    # Method 3: Manual download
    if (-not $installed) {
        $installed = Install-TailscaleManual
    }
    
    if (-not $installed) {
        Write-Host ""
        Write-Host "Error: Failed to install Tailscale" -ForegroundColor Red
        Write-Host "Please download manually from: https://tailscale.com/download/windows" -ForegroundColor Yellow
        exit 1
    }
    
    # Start service and launch GUI
    Start-TailscaleService
    Start-TailscaleGUI
    
    # Show next steps
    Show-NextSteps
    
    Write-Host ""
    Write-Host "=== Setup Complete ===" -ForegroundColor Green
}

# Run main function
Main
