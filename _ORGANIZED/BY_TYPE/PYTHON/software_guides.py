#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Software Installation Guides Module for IT Genius
Comprehensive guides for installing and managing software on macOS and Windows
"""

import platform
import subprocess
import os
from typing import Dict, List

class SoftwareGuides:
    """Software installation and management guides"""
    
    def __init__(self):
        self.os_type = platform.system()
        self.is_macos = self.os_type == "Darwin"
        self.is_windows = self.os_type == "Windows"
        self.is_linux = self.os_type == "Linux"
    
    def show_menu(self):
        """Display software guides menu"""
        while True:
            print("\n" + "="*70)
            print("SOFTWARE INSTALLATION GUIDES")
            print("="*70)
            print("1. Package Manager Setup")
            print("2. Essential Development Tools")
            print("3. Productivity Software")
            print("4. Security & Privacy Tools")
            print("5. Media & Creative Tools")
            print("6. System Utilities")
            print("7. Cloud Services Setup")
            print("8. Virtualization Tools")
            print("9. Command Line Tools")
            print("10. Automated Installation Scripts")
            print("0. Back to Main Menu")
            print("="*70)
            
            choice = input("\nSelect an option: ").strip()
            
            if choice == "1":
                self.package_manager_setup()
            elif choice == "2":
                self.development_tools()
            elif choice == "3":
                self.productivity_software()
            elif choice == "4":
                self.security_tools()
            elif choice == "5":
                self.media_tools()
            elif choice == "6":
                self.system_utilities()
            elif choice == "7":
                self.cloud_services()
            elif choice == "8":
                self.virtualization_tools()
            elif choice == "9":
                self.command_line_tools()
            elif choice == "10":
                self.installation_scripts()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")
            
            if choice != "0":
                input("\nPress Enter to continue...")
    
    def package_manager_setup(self):
        """Package manager installation and setup"""
        print("\n" + "="*70)
        print("PACKAGE MANAGER SETUP")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Package Managers:")
            print("\n1. Homebrew (Recommended):")
            print("   Install: /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
            print("   Usage: brew install <package>")
            print("   Update: brew update && brew upgrade")
            
            print("\n2. MacPorts:")
            print("   Download from: https://www.macports.org/install.php")
            print("   Usage: sudo port install <package>")
            
            print("\n3. Conda (Python):")
            print("   Install: Download Miniconda from https://docs.conda.io/en/latest/miniconda.html")
            print("   Usage: conda install <package>")
            
        elif self.is_windows:
            print("\n🪟 Windows Package Managers:")
            print("\n1. Chocolatey (Recommended):")
            print("   Install: Run PowerShell as Admin, then:")
            print("   Set-ExecutionPolicy Bypass -Scope Process -Force;")
            print("   [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;")
            print("   iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")
            print("   Usage: choco install <package>")
            
            print("\n2. Winget (Built-in):")
            print("   Usage: winget install <package>")
            print("   Search: winget search <package>")
            
            print("\n3. Scoop:")
            print("   Install: iwr -useb get.scoop.sh | iex")
            print("   Usage: scoop install <package>")
            
        elif self.is_linux:
            print("\n🐧 Linux Package Managers:")
            print("\n1. APT (Debian/Ubuntu):")
            print("   Update: sudo apt update")
            print("   Install: sudo apt install <package>")
            
            print("\n2. YUM/DNF (Red Hat/CentOS/Fedora):")
            print("   Install: sudo dnf install <package>")
            
            print("\n3. Pacman (Arch Linux):")
            print("   Install: sudo pacman -S <package>")
        
        print("\n" + "="*70)
    
    def development_tools(self):
        """Development tools installation guides"""
        print("\n" + "="*70)
        print("ESSENTIAL DEVELOPMENT TOOLS")
        print("="*70)
        
        tools = {
            "Git": {
                "macos": "brew install git",
                "windows": "choco install git",
                "description": "Version control system"
            },
            "Python": {
                "macos": "brew install python@3.11",
                "windows": "choco install python",
                "description": "Programming language"
            },
            "Node.js": {
                "macos": "brew install node",
                "windows": "choco install nodejs",
                "description": "JavaScript runtime"
            },
            "Docker": {
                "macos": "brew install --cask docker",
                "windows": "choco install docker-desktop",
                "description": "Containerization platform"
            },
            "VS Code": {
                "macos": "brew install --cask visual-studio-code",
                "windows": "choco install vscode",
                "description": "Code editor"
            },
            "Postman": {
                "macos": "brew install --cask postman",
                "windows": "choco install postman",
                "description": "API testing tool"
            }
        }
        
        print("\n📦 Recommended Development Tools:\n")
        for tool, info in tools.items():
            print(f"🔧 {tool} - {info['description']}")
            if self.is_macos:
                print(f"   Install: {info['macos']}")
            elif self.is_windows:
                print(f"   Install: {info['windows']}")
            print()
        
        print("\n💡 Pro Tips:")
        print("   • Use version managers (nvm, pyenv, rbenv) for multiple versions")
        print("   • Set up SSH keys for Git: ssh-keygen -t ed25519 -C 'your_email@example.com'")
        print("   • Configure Git: git config --global user.name 'Your Name'")
        print("   • Install useful VS Code extensions: Python, ESLint, Prettier")
        
        print("\n" + "="*70)
    
    def productivity_software(self):
        """Productivity software recommendations"""
        print("\n" + "="*70)
        print("PRODUCTIVITY SOFTWARE")
        print("="*70)
        
        software = {
            "Office Suites": ["Microsoft 365", "Google Workspace", "LibreOffice"],
            "Note Taking": ["Notion", "Obsidian", "Evernote", "OneNote"],
            "Task Management": ["Todoist", "Asana", "Trello", "Microsoft To Do"],
            "Communication": ["Slack", "Microsoft Teams", "Discord", "Zoom"],
            "Password Managers": ["1Password", "LastPass", "Bitwarden", "KeePass"],
            "File Sync": ["Dropbox", "Google Drive", "OneDrive", "iCloud Drive"],
            "PDF Tools": ["Adobe Acrobat", "PDF Expert", "Preview (macOS)"],
            "Screen Recording": ["OBS Studio", "QuickTime (macOS)", "ScreenRecorder"]
        }
        
        for category, apps in software.items():
            print(f"\n📱 {category}:")
            for app in apps:
                print(f"   • {app}")
        
        print("\n💡 Installation Tips:")
        if self.is_macos:
            print("   • Use App Store for official apps")
            print("   • Use Homebrew Cask: brew install --cask <app>")
        elif self.is_windows:
            print("   • Use Microsoft Store for official apps")
            print("   • Use Chocolatey: choco install <app>")
        
        print("\n" + "="*70)
    
    def security_tools(self):
        """Security and privacy tools"""
        print("\n" + "="*70)
        print("SECURITY & PRIVACY TOOLS")
        print("="*70)
        
        tools = {
            "Antivirus": {
                "macos": ["Sophos", "Malwarebytes", "ClamXav"],
                "windows": ["Windows Defender", "Malwarebytes", "Bitdefender"]
            },
            "VPN": ["NordVPN", "ExpressVPN", "ProtonVPN", "Mullvad"],
            "Firewall": {
                "macos": "Built-in Firewall (System Settings → Network → Firewall)",
                "windows": "Windows Firewall (Settings → Privacy & Security → Windows Security)"
            },
            "Encryption": ["VeraCrypt", "FileVault (macOS)", "BitLocker (Windows)"],
            "Privacy": ["Privacy Badger", "uBlock Origin", "DuckDuckGo"]
        }
        
        print("\n🔒 Security Tools:\n")
        for category, items in tools.items():
            print(f"🛡️  {category}:")
            if isinstance(items, dict):
                if self.is_macos and "macos" in items:
                    for tool in items["macos"]:
                        print(f"   • {tool}")
                elif self.is_windows and "windows" in items:
                    for tool in items["windows"]:
                        print(f"   • {tool}")
                else:
                    print(f"   {items}")
            elif isinstance(items, list):
                for tool in items:
                    print(f"   • {tool}")
            else:
                print(f"   {items}")
            print()
        
        print("\n💡 Security Best Practices:")
        print("   • Enable two-factor authentication everywhere")
        print("   • Use strong, unique passwords (password manager)")
        print("   • Keep software updated")
        print("   • Use VPN on public networks")
        print("   • Enable full disk encryption")
        print("   • Regular backups")
        print("   • Be cautious with email attachments")
        
        print("\n" + "="*70)
    
    def media_tools(self):
        """Media and creative tools"""
        print("\n" + "="*70)
        print("MEDIA & CREATIVE TOOLS")
        print("="*70)
        
        categories = {
            "Image Editing": ["Adobe Photoshop", "GIMP", "Affinity Photo", "Pixelmator"],
            "Video Editing": ["Adobe Premiere Pro", "Final Cut Pro (macOS)", "DaVinci Resolve", "iMovie"],
            "Audio": ["Audacity", "GarageBand (macOS)", "Logic Pro (macOS)", "Reaper"],
            "3D Modeling": ["Blender", "Maya", "Cinema 4D"],
            "Design": ["Adobe Illustrator", "Figma", "Sketch (macOS)", "Canva"],
            "Streaming": ["OBS Studio", "Streamlabs", "XSplit"]
        }
        
        for category, tools in categories.items():
            print(f"\n🎨 {category}:")
            for tool in tools:
                print(f"   • {tool}")
        
        print("\n💡 Free Alternatives:")
        print("   • GIMP (Photoshop alternative)")
        print("   • DaVinci Resolve (Professional video editing)")
        print("   • Blender (3D modeling and animation)")
        print("   • Audacity (Audio editing)")
        print("   • Inkscape (Vector graphics)")
        
        print("\n" + "="*70)
    
    def system_utilities(self):
        """System utility tools"""
        print("\n" + "="*70)
        print("SYSTEM UTILITIES")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Utilities:")
            print("   • CleanMyMac X - System cleanup")
            print("   • Disk Utility - Built-in disk management")
            print("   • Activity Monitor - Process management")
            print("   • Console - System logs")
            print("   • Terminal - Command line")
            print("   • Time Machine - Backup solution")
            print("   • OnyX - System maintenance")
            print("   • AppCleaner - App uninstaller")
            
        elif self.is_windows:
            print("\n🪟 Windows Utilities:")
            print("   • CCleaner - System cleanup")
            print("   • Task Manager - Process management")
            print("   • Event Viewer - System logs")
            print("   • PowerShell - Command line")
            print("   • Disk Management - Disk utilities")
            print("   • System Restore - Recovery")
            print("   • Revo Uninstaller - App uninstaller")
            print("   • Process Explorer - Advanced task manager")
        
        print("\n💡 Built-in System Tools:")
        if self.is_macos:
            print("   • Disk Utility: Applications → Utilities")
            print("   • Activity Monitor: Applications → Utilities")
            print("   • Console: Applications → Utilities")
        elif self.is_windows:
            print("   • Task Manager: Ctrl+Shift+Esc")
            print("   • Event Viewer: eventvwr.msc")
            print("   • Disk Management: diskmgmt.msc")
        
        print("\n" + "="*70)
    
    def cloud_services(self):
        """Cloud services setup"""
        print("\n" + "="*70)
        print("CLOUD SERVICES SETUP")
        print("="*70)
        
        services = {
            "File Storage": {
                "iCloud Drive": "Built-in on macOS/iOS",
                "Google Drive": "drive.google.com",
                "Dropbox": "dropbox.com",
                "OneDrive": "onedrive.live.com",
                "Box": "box.com"
            },
            "Backup": {
                "Time Machine": "Built-in on macOS",
                "Backblaze": "backblaze.com",
                "Carbonite": "carbonite.com",
                "Acronis": "acronis.com"
            },
            "Development": {
                "GitHub": "github.com",
                "GitLab": "gitlab.com",
                "Bitbucket": "bitbucket.org"
            },
            "Productivity": {
                "Google Workspace": "workspace.google.com",
                "Microsoft 365": "microsoft.com/microsoft-365",
                "Notion": "notion.so"
            }
        }
        
        for category, items in services.items():
            print(f"\n☁️  {category}:")
            for service, info in items.items():
                print(f"   • {service}: {info}")
        
        print("\n💡 Setup Tips:")
        print("   • Enable automatic syncing for important folders")
        print("   • Use version control for code (Git)")
        print("   • Set up automated backups")
        print("   • Enable two-factor authentication")
        print("   • Review sharing permissions regularly")
        
        print("\n" + "="*70)
    
    def virtualization_tools(self):
        """Virtualization and container tools"""
        print("\n" + "="*70)
        print("VIRTUALIZATION TOOLS")
        print("="*70)
        
        tools = {
            "Virtual Machines": {
                "macos": ["VMware Fusion", "Parallels Desktop", "VirtualBox"],
                "windows": ["VMware Workstation", "Hyper-V", "VirtualBox"]
            },
            "Containers": ["Docker", "Podman", "Kubernetes"],
            "Cloud VMs": ["AWS EC2", "Google Cloud Compute", "Azure VMs"]
        }
        
        for category, items in tools.items():
            print(f"\n🖥️  {category}:")
            if isinstance(items, dict):
                if self.is_macos and "macos" in items:
                    for tool in items["macos"]:
                        print(f"   • {tool}")
                elif self.is_windows and "windows" in items:
                    for tool in items["windows"]:
                        print(f"   • {tool}")
            elif isinstance(items, list):
                for tool in items:
                    print(f"   • {tool}")
        
        print("\n💡 Installation:")
        if self.is_macos:
            print("   • Docker: brew install --cask docker")
            print("   • VirtualBox: brew install --cask virtualbox")
        elif self.is_windows:
            print("   • Docker Desktop: choco install docker-desktop")
            print("   • VirtualBox: choco install virtualbox")
        
        print("\n" + "="*70)
    
    def command_line_tools(self):
        """Command line tools and utilities"""
        print("\n" + "="*70)
        print("COMMAND LINE TOOLS")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Terminal Tools:")
            print("   • Homebrew: Package manager")
            print("   • zsh/oh-my-zsh: Enhanced shell")
            print("   • iTerm2: Terminal emulator")
            print("   • tmux: Terminal multiplexer")
            print("   • htop: Process monitor")
            print("   • tree: Directory tree")
            print("   • jq: JSON processor")
            print("   • wget/curl: File downloaders")
            print("   • grep/awk/sed: Text processing")
            
            print("\n📦 Install Essential Tools:")
            print("   brew install htop tree jq wget")
            print("   brew install --cask iterm2")
            
        elif self.is_windows:
            print("\n🪟 Windows PowerShell/CMD Tools:")
            print("   • PowerShell: Modern command line")
            print("   • Windows Terminal: Enhanced terminal")
            print("   • Git Bash: Unix-like environment")
            print("   • WSL: Windows Subsystem for Linux")
            print("   • Chocolatey: Package manager")
            print("   • Scoop: Alternative package manager")
            
            print("\n📦 Install Essential Tools:")
            print("   choco install git curl wget")
            print("   choco install microsoft-windows-terminal")
        
        print("\n💡 Useful Commands:")
        print("   • Find files: find . -name '*.txt'")
        print("   • Search text: grep -r 'pattern' .")
        print("   • Process info: ps aux | grep <process>")
        print("   • Disk usage: du -sh *")
        print("   • Network: netstat -an | grep LISTEN")
        
        print("\n" + "="*70)
    
    def installation_scripts(self):
        """Generate installation scripts"""
        print("\n" + "="*70)
        print("AUTOMATED INSTALLATION SCRIPTS")
        print("="*70)
        
        print("\n💡 Create installation scripts for:")
        print("   • Development environment setup")
        print("   • Essential software bundle")
        print("   • System configuration")
        print("   • Backup automation")
        
        if self.is_macos:
            print("\n📝 Example macOS Script (save as setup.sh):")
            print("""
#!/bin/bash
# macOS Development Setup Script

# Install Homebrew if not installed
if ! command -v brew &> /dev/null; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Update Homebrew
brew update

# Install essential tools
brew install git python node
brew install --cask visual-studio-code docker

# Install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

echo "✅ Setup complete!"
            """)
            
        elif self.is_windows:
            print("\n📝 Example Windows Script (save as setup.ps1):")
            print("""
# Windows Development Setup Script

# Install Chocolatey if not installed
if (!(Get-Command choco -ErrorAction SilentlyContinue)) {
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
}

# Install essential tools
choco install git python nodejs vscode docker-desktop -y

Write-Host "✅ Setup complete!" -ForegroundColor Green
            """)
        
        print("\n💡 Usage:")
        if self.is_macos:
            print("   chmod +x setup.sh")
            print("   ./setup.sh")
        elif self.is_windows:
            print("   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser")
            print("   .\\setup.ps1")
        
        print("\n" + "="*70)

