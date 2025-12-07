#!/bin/zsh
# Quick deployment script for permanent boot startup
# Run this on M2Ultra to complete setup

echo "🚀 NOIZYLAB Persistent Boot Setup"
echo "=================================="
echo ""

# M2Ultra Setup
echo "📱 M2Ultra (macOS) Configuration:"
echo "================================"

# Check if LaunchAgent is loaded
if launchctl list | grep -q "com.noizylab.m2ultra.boot"; then
    echo "✅ LaunchAgent is ACTIVE and running"
    echo "✅ Boot startup is ENABLED"
    echo ""
    echo "Last boot startup log:"
    tail -5 ~/.m2ultra-boot.log
else
    echo "❌ LaunchAgent not loaded. Installing..."
    mkdir -p ~/.local/bin
    chmod +x ~/.local/bin/m2ultra-boot-startup.sh
    mkdir -p ~/Library/LaunchAgents
    launchctl load ~/Library/LaunchAgents/com.noizylab.m2ultra.boot.plist
    echo "✅ LaunchAgent installed and loaded"
fi

echo ""
echo "HP-OMEN Setup Instructions:"
echo "==========================="
echo ""
echo "On HP-OMEN (Gabriel's Machine), run this in PowerShell (as Administrator):"
echo ""
echo "# Option 1: Using Task Scheduler (Recommended)"
echo "cd C:\Users\Gabriel\NOIZYLAB\scripts"
echo 'Register-ScheduledTask -Xml (Get-Content HP-OMEN-Task-Scheduler.xml | Out-String) -TaskName "HP-OMEN Boot Startup" -Force'
echo ""
echo "# Option 2: Simple Startup Folder"
echo 'Copy-Item HP-OMEN-boot-startup.ps1 "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\"'
echo ""

echo ""
echo "🔗 Connection Testing:"
echo "====================="
echo ""

# Test SSH
echo "🔐 SSH Status:"
if sudo systemsetup -getremotelogin | grep -q "On"; then
    echo "✅ SSH is ENABLED"
else
    echo "❌ SSH is DISABLED"
    echo "   Run: sudo systemsetup -setremotelogin on"
fi

# Test Screen Sharing
echo ""
echo "📺 Screen Sharing Status:"
if pgrep -q "ARDAgent"; then
    echo "✅ Screen Sharing is RUNNING"
else
    echo "⚠️  Screen Sharing is not running"
    echo "   Will be started on next boot"
fi

# Get connection info
echo ""
echo "📍 M2Ultra Connection Details:"
echo "=============================="
echo "Computer Name: $(scutil --get ComputerName)"
echo "IP Address: $(ipconfig getifaddr en0)"
echo ""
echo "SSH: ssh m2ultra@$(ipconfig getifaddr en0)"
echo "VNC: vnc://$(ipconfig getifaddr en0)"
echo ""

echo "✨ Setup Complete!"
echo ""
echo "📝 What's Running on Boot:"
echo "- SSH Server"
echo "- Screen Sharing (VNC)"
echo "- Environment aliases"
echo "- Network drive mounting"
echo "- Automatic reconnection hourly"
echo ""
echo "🎮 Next Steps:"
echo "1. Configure HP-OMEN boot startup (see instructions above)"
echo "2. Share M2Ultra IP with Gabriel"
echo "3. Test connection with: ssh m2ultra@[IP]"
echo "4. System will auto-initialize on each boot"
