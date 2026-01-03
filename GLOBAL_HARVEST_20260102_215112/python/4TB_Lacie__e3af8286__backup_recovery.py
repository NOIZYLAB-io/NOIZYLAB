#!/usr/bin/env python3
"""
Backup & Recovery Module for IT Genius
Comprehensive backup strategies and recovery procedures for macOS and Windows
"""

import platform
import subprocess
import os
import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime

class BackupRecovery:
    """Backup and recovery management"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.os_type = platform.system()
        self.is_macos = self.os_type == "Darwin"
        self.is_windows = self.os_type == "Windows"
        if "backup_profiles" not in self.config:
            self.config["backup_profiles"] = {}
    
    def show_menu(self):
        """Display backup and recovery menu"""
        while True:
            print("\n" + "="*70)
            print("BACKUP & RECOVERY")
            print("="*70)
            print("1. Backup Strategy Guide")
            print("2. macOS Backup (Time Machine)")
            print("3. Windows Backup")
            print("4. Cloud Backup Setup")
            print("5. File-Level Backup")
            print("6. System Image Creation")
            print("7. Recovery Procedures")
            print("8. Backup Automation")
            print("9. Backup Verification")
            print("10. Manage Backup Profiles")
            print("0. Back to Main Menu")
            print("="*70)
            
            choice = input("\nSelect an option: ").strip()
            
            if choice == "1":
                self.backup_strategy()
            elif choice == "2":
                self.time_machine_setup()
            elif choice == "3":
                self.windows_backup()
            elif choice == "4":
                self.cloud_backup()
            elif choice == "5":
                self.file_backup()
            elif choice == "6":
                self.system_image()
            elif choice == "7":
                self.recovery_procedures()
            elif choice == "8":
                self.backup_automation()
            elif choice == "9":
                self.verify_backup()
            elif choice == "10":
                self.manage_profiles()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")
            
            if choice != "0":
                input("\nPress Enter to continue...")
    
    def backup_strategy(self):
        """Backup strategy guide"""
        print("\n" + "="*70)
        print("BACKUP STRATEGY GUIDE")
        print("="*70)
        
        print("\n📋 The 3-2-1 Backup Rule:")
        print("   • 3 copies of your data")
        print("   • 2 different storage media")
        print("   • 1 copy off-site")
        
        print("\n💾 Backup Types:")
        print("\n1. Full Backup:")
        print("   • Complete system backup")
        print("   • Includes all files and system state")
        print("   • Takes longest, uses most space")
        print("   • Recommended: Weekly or monthly")
        
        print("\n2. Incremental Backup:")
        print("   • Only backs up changed files since last backup")
        print("   • Faster, uses less space")
        print("   • Requires full backup + all incrementals to restore")
        print("   • Recommended: Daily")
        
        print("\n3. Differential Backup:")
        print("   • Backs up all changes since last full backup")
        print("   • Faster than full, slower than incremental")
        print("   • Requires full backup + latest differential")
        print("   • Recommended: Every few days")
        
        print("\n4. Continuous/Sync Backup:")
        print("   • Real-time file synchronization")
        print("   • Cloud-based (Dropbox, iCloud, OneDrive)")
        print("   • Good for important files")
        print("   • Not a replacement for full backup")
        
        print("\n📦 What to Backup:")
        print("   ✓ User files (Documents, Photos, Videos)")
        print("   ✓ Application data")
        print("   ✓ System settings")
        print("   ✓ Email and contacts")
        print("   ✓ Browser bookmarks")
        print("   ✓ Software licenses")
        
        print("\n❌ What NOT to Backup:")
        print("   ✗ System cache files")
        print("   ✗ Temporary files")
        print("   ✗ Application caches")
        print("   ✗ Trash/Recycle Bin")
        
        print("\n💡 Best Practices:")
        print("   • Automate backups")
        print("   • Test restore procedures regularly")
        print("   • Encrypt backups")
        print("   • Store off-site copy")
        print("   • Version your backups")
        print("   • Document backup procedures")
        
        print("\n" + "="*70)
    
    def time_machine_setup(self):
        """Time Machine setup for macOS"""
        if not self.is_macos:
            print("\n⚠️  Time Machine is only available on macOS")
            return
        
        print("\n" + "="*70)
        print("TIME MACHINE SETUP (macOS)")
        print("="*70)
        
        print("\n🍎 Setting Up Time Machine:")
        print("\n1. Connect External Drive:")
        print("   • Use external drive or network drive")
        print("   • Format as APFS or Mac OS Extended")
        print("   • Minimum size: 2x your data size")
        
        print("\n2. Enable Time Machine:")
        print("   System Settings → General → Time Machine")
        print("   Click 'Add Backup Disk'")
        print("   Select your drive")
        print("   Enable 'Back Up Automatically'")
        
        print("\n3. Configure Options:")
        print("   Click 'Options' to:")
        print("   • Exclude specific folders")
        print("   • Set backup frequency")
        print("   • Enable encryption")
        
        print("\n4. Manual Backup:")
        print("   Time Machine menu → Back Up Now")
        
        print("\n5. Terminal Commands:")
        print("   # Check Time Machine status")
        print("   tmutil status")
        print("   # List backup destinations")
        print("   tmutil listdestinations")
        print("   # Start backup")
        print("   tmutil startbackup")
        print("   # Exclude folder")
        print("   tmutil addexclusion /path/to/folder")
        
        print("\n💡 Time Machine Tips:")
        print("   • First backup takes longest")
        print("   • Keep drive connected for automatic backups")
        print("   • Use network drive for multiple Macs")
        print("   • Encrypt backups for security")
        print("   • Clean up old backups periodically")
        
        print("\n" + "="*70)
    
    def windows_backup(self):
        """Windows backup setup"""
        if not self.is_windows:
            print("\n⚠️  Windows Backup is only available on Windows")
            return
        
        print("\n" + "="*70)
        print("WINDOWS BACKUP")
        print("="*70)
        
        print("\n🪟 Windows Backup Options:")
        print("\n1. File History:")
        print("   Settings → Privacy & Security → Windows Backup")
        print("   Turn on 'Remember my apps'")
        print("   Add drive for File History")
        print("   Automatically backs up user files")
        
        print("\n2. System Image Backup:")
        print("   Control Panel → System and Security → Backup and Restore")
        print("   Create a system image")
        print("   Full system backup to external drive")
        
        print("\n3. OneDrive Sync:")
        print("   Settings → Accounts → Microsoft account")
        print("   Enable OneDrive sync")
        print("   Automatic cloud backup")
        
        print("\n4. PowerShell Commands:")
        print("   # Check backup status")
        print("   Get-WBSummary")
        print("   # Start backup")
        print("   Start-WBBackup -Policy $policy")
        
        print("\n💡 Windows Backup Tips:")
        print("   • Use File History for user files")
        print("   • Create system image monthly")
        print("   • Use OneDrive for cloud sync")
        print("   • Keep external drive connected")
        print("   • Test restore procedures")
        
        print("\n" + "="*70)
    
    def cloud_backup(self):
        """Cloud backup services setup"""
        print("\n" + "="*70)
        print("CLOUD BACKUP SETUP")
        print("="*70)
        
        services = {
            "iCloud Drive": {
                "platform": "macOS/iOS",
                "setup": "System Settings → Apple ID → iCloud → iCloud Drive",
                "features": "Automatic sync, 5GB free, paid plans available"
            },
            "OneDrive": {
                "platform": "Windows/macOS",
                "setup": "Settings → Accounts → Microsoft account → OneDrive",
                "features": "5GB free, Office 365 includes 1TB"
            },
            "Google Drive": {
                "platform": "All platforms",
                "setup": "drive.google.com → Install desktop app",
                "features": "15GB free, paid plans available"
            },
            "Dropbox": {
                "platform": "All platforms",
                "setup": "dropbox.com → Download desktop app",
                "features": "2GB free, paid plans available"
            },
            "Backblaze": {
                "platform": "macOS/Windows",
                "setup": "backblaze.com → Download and install",
                "features": "Unlimited backup, $7/month"
            },
            "Carbonite": {
                "platform": "macOS/Windows",
                "setup": "carbonite.com → Download and install",
                "features": "Unlimited backup, various plans"
            }
        }
        
        print("\n☁️  Cloud Backup Services:\n")
        for service, info in services.items():
            print(f"📦 {service}:")
            print(f"   Platform: {info['platform']}")
            print(f"   Setup: {info['setup']}")
            print(f"   Features: {info['features']}")
            print()
        
        print("\n💡 Cloud Backup Best Practices:")
        print("   • Encrypt sensitive data before uploading")
        print("   • Use two-factor authentication")
        print("   • Review sharing permissions")
        print("   • Keep local backup as well")
        print("   • Test restore procedures")
        print("   • Monitor storage usage")
        
        print("\n" + "="*70)
    
    def file_backup(self):
        """File-level backup procedures"""
        print("\n" + "="*70)
        print("FILE-LEVEL BACKUP")
        print("="*70)
        
        print("\n📁 Manual File Backup:")
        print("\n1. Identify Important Files:")
        print("   • Documents folder")
        print("   • Desktop files")
        print("   • Downloads (important items)")
        print("   • Pictures/Videos")
        print("   • Application data")
        
        print("\n2. Copy to External Drive:")
        if self.is_macos:
            print("   • Connect external drive")
            print("   • Drag folders to external drive")
            print("   • Or use Terminal: cp -R ~/Documents /Volumes/Backup/")
        elif self.is_windows:
            print("   • Connect external drive")
            print("   • Copy folders to external drive")
            print("   • Or use PowerShell: Copy-Item -Path C:\\Users\\... -Destination D:\\Backup\\ -Recurse")
        
        print("\n3. Automated Scripts:")
        if self.is_macos:
            print("\n   # macOS Backup Script (backup.sh):")
            print("   #!/bin/bash")
            print("   BACKUP_DIR=\"/Volumes/Backup/$(date +%Y%m%d)\"")
            print("   mkdir -p \"$BACKUP_DIR\"")
            print("   rsync -av ~/Documents \"$BACKUP_DIR/\"")
            print("   rsync -av ~/Pictures \"$BACKUP_DIR/\"")
            print("   echo \"Backup complete!\"")
        elif self.is_windows:
            print("\n   # Windows Backup Script (backup.ps1):")
            print("   $BackupDir = \"D:\\Backup\\$(Get-Date -Format 'yyyyMMdd')\"")
            print("   New-Item -ItemType Directory -Path $BackupDir")
            print("   Copy-Item -Path $env:USERPROFILE\\Documents -Destination $BackupDir -Recurse")
            print("   Copy-Item -Path $env:USERPROFILE\\Pictures -Destination $BackupDir -Recurse")
            print("   Write-Host \"Backup complete!\"")
        
        print("\n💡 File Backup Tips:")
        print("   • Organize files before backing up")
        print("   • Use date-based folder names")
        print("   • Verify files after copying")
        print("   • Compress large backups")
        print("   • Keep multiple versions")
        
        print("\n" + "="*70)
    
    def system_image(self):
        """System image creation"""
        print("\n" + "="*70)
        print("SYSTEM IMAGE CREATION")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS System Image:")
            print("\n1. Using Disk Utility:")
            print("   Applications → Utilities → Disk Utility")
            print("   File → New Image → Image from Folder")
            print("   Select system drive or folder")
            print("   Choose compression and encryption")
            
            print("\n2. Using Terminal (dd):")
            print("   # WARNING: Advanced users only!")
            print("   sudo dd if=/dev/diskX of=/path/to/image.dmg bs=1m")
            
            print("\n3. Using Carbon Copy Cloner:")
            print("   Third-party tool for full disk cloning")
            print("   bombich.com")
            
        elif self.is_windows:
            print("\n🪟 Windows System Image:")
            print("\n1. Using Built-in Tool:")
            print("   Control Panel → System and Security")
            print("   Backup and Restore → Create a system image")
            print("   Select destination (external drive)")
            print("   Include system drive and other drives")
            
            print("\n2. Using PowerShell:")
            print("   # Create system image")
            print("   $policy = New-WBPolicy")
            print("   Add-WBSystemState -Policy $policy")
            print("   Add-WBBareMetalRecovery -Policy $policy")
            print("   $backupTarget = New-WBBackupTarget -VolumePath E:")
            print("   Add-WBBackupTarget -Policy $policy -Target $backupTarget")
            print("   Start-WBBackup -Policy $policy")
            
            print("\n3. Using Third-party Tools:")
            print("   • Macrium Reflect")
            print("   • Acronis True Image")
            print("   • Clonezilla (free)")
        
        print("\n💡 System Image Tips:")
        print("   • Create image when system is clean")
        print("   • Store on external drive")
        print("   • Test restore procedure")
        print("   • Update image periodically")
        print("   • Keep multiple versions")
        
        print("\n" + "="*70)
    
    def recovery_procedures(self):
        """Recovery procedures guide"""
        print("\n" + "="*70)
        print("RECOVERY PROCEDURES")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Recovery:")
            print("\n1. Recovery Mode:")
            print("   • Intel Mac: Hold Cmd+R during startup")
            print("   • Apple Silicon: Hold power button until 'Loading startup options'")
            print("   • Options: Restore from Time Machine, Reinstall macOS, Disk Utility")
            
            print("\n2. Restore from Time Machine:")
            print("   • Boot to Recovery Mode")
            print("   • Select 'Restore from Time Machine Backup'")
            print("   • Choose backup and follow prompts")
            
            print("\n3. Internet Recovery:")
            print("   • Hold Option+Cmd+R during startup")
            print("   • Downloads recovery system from internet")
            
            print("\n4. Target Disk Mode:")
            print("   • Hold T during startup")
            print("   • Connect to another Mac via Thunderbolt/USB")
            print("   • Access files from other Mac")
            
        elif self.is_windows:
            print("\n🪟 Windows Recovery:")
            print("\n1. Recovery Environment:")
            print("   • Settings → Update & Security → Recovery")
            print("   • Advanced startup → Restart now")
            print("   • Or: Hold Shift while clicking Restart")
            
            print("\n2. System Restore:")
            print("   • Recovery Environment → Troubleshoot")
            print("   • Advanced options → System Restore")
            print("   • Choose restore point")
            
            print("\n3. System Image Recovery:")
            print("   • Recovery Environment → Troubleshoot")
            print("   • Advanced options → System Image Recovery")
            print("   • Select system image")
            
            print("\n4. Reset This PC:")
            print("   • Recovery Environment → Troubleshoot")
            print("   • Reset this PC")
            print("   • Keep files or remove everything")
        
        print("\n💡 Recovery Best Practices:")
        print("   • Test recovery procedures before you need them")
        print("   • Keep recovery media accessible")
        print("   • Document recovery steps")
        print("   • Have multiple backup methods")
        print("   • Know your recovery key locations")
        
        print("\n" + "="*70)
    
    def backup_automation(self):
        """Backup automation setup"""
        print("\n" + "="*70)
        print("BACKUP AUTOMATION")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Automation:")
            print("\n1. Time Machine (Automatic):")
            print("   • Enable in System Settings")
            print("   • Backs up automatically when drive connected")
            
            print("\n2. Launchd (Scheduled Tasks):")
            print("   • Create plist file in ~/Library/LaunchAgents/")
            print("   • Schedule using launchctl")
            
            print("\n3. Automator:")
            print("   • Create backup workflow")
            print("   • Schedule with Calendar app")
            
        elif self.is_windows:
            print("\n🪟 Windows Automation:")
            print("\n1. Task Scheduler:")
            print("   • Windows + R → taskschd.msc")
            print("   • Create Basic Task")
            print("   • Schedule backup script")
            
            print("\n2. PowerShell Scheduled Job:")
            print("   $trigger = New-JobTrigger -Daily -At 2am")
            print("   Register-ScheduledJob -Name Backup -ScriptBlock {...} -Trigger $trigger")
        
        print("\n💡 Automation Tips:")
        print("   • Schedule during off-hours")
        print("   • Send email notifications")
        print("   • Log backup activities")
        print("   • Monitor backup success")
        print("   • Test automation regularly")
        
        print("\n" + "="*70)
    
    def verify_backup(self):
        """Backup verification procedures"""
        print("\n" + "="*70)
        print("BACKUP VERIFICATION")
        print("="*70)
        
        print("\n✅ Verification Checklist:")
        print("\n1. File Integrity:")
        print("   • Compare file sizes")
        print("   • Check file counts")
        print("   • Verify checksums (md5, sha256)")
        
        print("\n2. Restore Test:")
        print("   • Restore sample files")
        print("   • Verify files open correctly")
        print("   • Test on different system if possible")
        
        print("\n3. Backup Logs:")
        print("   • Review backup logs for errors")
        print("   • Check completion status")
        print("   • Verify backup dates")
        
        print("\n4. Storage Verification:")
        print("   • Check backup drive health")
        print("   • Verify available space")
        print("   • Test drive read/write")
        
        if self.is_macos:
            print("\n🍎 macOS Verification:")
            print("   # Check Time Machine status")
            print("   tmutil verifychecksums")
            print("   # List backups")
            print("   tmutil listbackups")
        elif self.is_windows:
            print("\n🪟 Windows Verification:")
            print("   # Check backup status")
            print("   Get-WBSummary")
            print("   # Verify backup")
            print("   Get-WBBackupSet")
        
        print("\n💡 Regular Verification:")
        print("   • Weekly: Check backup logs")
        print("   • Monthly: Test restore")
        print("   • Quarterly: Full verification")
        
        print("\n" + "="*70)
    
    def manage_profiles(self):
        """Manage backup profiles"""
        print("\n" + "="*70)
        print("MANAGE BACKUP PROFILES")
        print("="*70)
        
        if self.config["backup_profiles"]:
            print("\n📋 Saved Backup Profiles:")
            for name, profile in self.config["backup_profiles"].items():
                print(f"\n   {name}:")
                print(f"      Type: {profile.get('type', 'Unknown')}")
                print(f"      Destination: {profile.get('destination', 'N/A')}")
                print(f"      Schedule: {profile.get('schedule', 'N/A')}")
        else:
            print("\nNo backup profiles saved yet.")
        
        print("\n💡 Create Backup Profile:")
        name = input("\nProfile name (or 'skip'): ").strip()
        if name and name.lower() != 'skip':
            profile = {
                "type": input("Backup type (full/incremental/cloud): ").strip(),
                "destination": input("Destination path: ").strip(),
                "schedule": input("Schedule (daily/weekly/monthly): ").strip(),
                "created": datetime.now().isoformat()
            }
            self.config["backup_profiles"][name] = profile
            print(f"✅ Profile '{name}' saved!")
        
        print("\n" + "="*70)

