#!/bin/zsh
# HP-OMEN Remote Desktop Setup Script
# Enables RDP, SSH, and VNC for remote access

set -e

echo "🖥️  HP-OMEN Remote Desktop Setup"
echo "=================================="

# Detect OS
OS_TYPE=$(uname)

if [[ "$OS_TYPE" == "Darwin" ]]; then
    echo "❌ macOS detected. Remote Desktop setup is Windows-specific."
    echo "For macOS remote access, consider: Screen Sharing, VNC, or SSH tunneling"
    exit 1
fi

# Windows-specific setup
if [[ "$OS_TYPE" == "MINGW64_NT"* ]] || [[ "$OS_TYPE" == "MSYS_NT"* ]]; then
    echo "✅ Windows detected - setting up Remote Desktop"
    
    # Enable RDP
    echo "🔧 Enabling Remote Desktop Protocol (RDP)..."
    
    # Registry key to enable RDP
    reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
    
    # Allow through Windows Firewall
    echo "🔥 Configuring Windows Firewall..."
    netsh advfirewall firewall add rule name="Allow RDP" dir=in action=allow protocol=tcp localport=3389
    
    echo "✅ RDP enabled on port 3389"
    
    # Optional: Enable SSH if available
    if command -v ssh &> /dev/null; then
        echo "🔐 SSH already available"
    else
        echo "⚠️  SSH not found. Consider installing OpenSSH Server"
    fi
    
    # Get system info
    echo ""
    echo "📊 System Information:"
    echo "Computer Name: $(hostname)"
    echo "IP Address: $(ipconfig getifaddr en0 2>/dev/null || ipconfig | grep -A 5 "Ethernet adapter" | grep "IPv4" | head -1)"
    
    exit 0
fi

# Linux RDP setup (if applicable)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "✅ Linux detected - setting up RDP server"
    
    # Check for xrdp
    if ! command -v xrdp &> /dev/null; then
        echo "📦 Installing xrdp..."
        sudo apt-get update
        sudo apt-get install -y xrdp xserver-xorg-core
    fi
    
    # Start xrdp service
    echo "🚀 Starting xrdp service..."
    sudo systemctl start xrdp
    sudo systemctl enable xrdp
    
    # Configure firewall
    echo "🔥 Configuring firewall..."
    sudo ufw allow 3389/tcp
    
    echo "✅ RDP enabled on port 3389"
    
    exit 0
fi

echo "❌ Unsupported OS"
exit 1
