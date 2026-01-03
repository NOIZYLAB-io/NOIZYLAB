#!/usr/bin/env python3
"""
Security Settings Module for IT Genius
Advanced security and privacy configuration for macOS and Windows
"""

import platform
import subprocess
from typing import Dict

class SecuritySettings:
    """Security and privacy settings manager"""
    
    def __init__(self, system_info: Dict):
        self.system_info = system_info
        self.os_type = system_info.get("os", platform.system())
        self.is_macos = self.os_type == "Darwin"
        self.is_windows = self.os_type == "Windows"
    
    def show_menu(self):
        """Display security settings menu"""
        while True:
            print("\n" + "="*70)
            print("SECURITY & PRIVACY SETTINGS")
            print("="*70)
            print("1. System Security Overview")
            print("2. Firewall Configuration")
            print("3. Encryption Settings")
            print("4. Privacy Controls")
            print("5. Password & Authentication")
            print("6. Network Security")
            print("7. Application Permissions")
            print("8. Security Audit Checklist")
            print("9. Advanced Security Hardening")
            print("0. Back to Main Menu")
            print("="*70)
            
            choice = input("\nSelect an option: ").strip()
            
            if choice == "1":
                self.security_overview()
            elif choice == "2":
                self.firewall_config()
            elif choice == "3":
                self.encryption_settings()
            elif choice == "4":
                self.privacy_controls()
            elif choice == "5":
                self.authentication_settings()
            elif choice == "6":
                self.network_security()
            elif choice == "7":
                self.app_permissions()
            elif choice == "8":
                self.security_checklist()
            elif choice == "9":
                self.advanced_hardening()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")
            
            if choice != "0":
                input("\nPress Enter to continue...")
    
    def security_overview(self):
        """Display security overview"""
        print("\n" + "="*70)
        print("SYSTEM SECURITY OVERVIEW")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Security Features:")
            print("   ✅ Gatekeeper - Prevents unauthorized apps")
            print("   ✅ XProtect - Built-in malware protection")
            print("   ✅ System Integrity Protection (SIP)")
            print("   ✅ FileVault - Full disk encryption")
            print("   ✅ Firewall - Network protection")
            print("   ✅ Touch ID / Face ID - Biometric auth")
            print("   ✅ Secure Enclave - Hardware security")
            
            print("\n📊 Check Security Status:")
            print("   • System Settings → Privacy & Security")
            print("   • System Settings → General → Software Update")
            print("   • System Settings → Network → Firewall")
            
        elif self.is_windows:
            print("\n🪟 Windows Security Features:")
            print("   ✅ Windows Defender - Built-in antivirus")
            print("   ✅ Windows Firewall - Network protection")
            print("   ✅ BitLocker - Full disk encryption")
            print("   ✅ Windows Hello - Biometric auth")
            print("   ✅ SmartScreen - Phishing protection")
            print("   ✅ Secure Boot - Boot protection")
            print("   ✅ TPM - Hardware security")
            
            print("\n📊 Check Security Status:")
            print("   • Settings → Privacy & Security → Windows Security")
            print("   • Windows Security → Virus & threat protection")
            print("   • Windows Security → Firewall & network protection")
        
        print("\n💡 Security Best Practices:")
        print("   • Keep system and apps updated")
        print("   • Use strong, unique passwords")
        print("   • Enable two-factor authentication")
        print("   • Enable full disk encryption")
        print("   • Use firewall")
        print("   • Be cautious with downloads")
        print("   • Regular backups")
        
        print("\n" + "="*70)
    
    def firewall_config(self):
        """Firewall configuration guide"""
        print("\n" + "="*70)
        print("FIREWALL CONFIGURATION")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Firewall Setup:")
            print("\n1. Enable Firewall:")
            print("   System Settings → Network → Firewall")
            print("   Click 'Turn On Firewall'")
            
            print("\n2. Firewall Options:")
            print("   • Block all incoming connections")
            print("   • Automatically allow built-in software")
            print("   • Automatically allow downloaded software")
            
            print("\n3. Advanced Settings (via Terminal):")
            print("   sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on")
            print("   sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on")
            
            print("\n4. Check Firewall Status:")
            print("   /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate")
            
        elif self.is_windows:
            print("\n🪟 Windows Firewall Setup:")
            print("\n1. Enable Firewall:")
            print("   Settings → Privacy & Security → Windows Security")
            print("   Firewall & network protection → Domain/Private/Public network")
            print("   Turn Windows Defender Firewall on")
            
            print("\n2. Advanced Firewall Rules:")
            print("   Windows Security → Firewall & network protection")
            print("   Advanced settings → Inbound/Outbound rules")
            
            print("\n3. PowerShell Commands:")
            print("   Get-NetFirewallProfile")
            print("   Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True")
        
        print("\n💡 Firewall Best Practices:")
        print("   • Always enable firewall")
        print("   • Block unnecessary ports")
        print("   • Review firewall logs regularly")
        print("   • Use application-specific rules when possible")
        
        print("\n" + "="*70)
    
    def encryption_settings(self):
        """Encryption configuration"""
        print("\n" + "="*70)
        print("ENCRYPTION SETTINGS")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Encryption:")
            print("\n1. FileVault (Full Disk Encryption):")
            print("   System Settings → Privacy & Security → FileVault")
            print("   Click 'Turn On' and follow prompts")
            print("   Save recovery key securely!")
            
            print("\n2. Encrypted Disk Images:")
            print("   Disk Utility → File → New Image → Blank Image")
            print("   Encryption: 128-bit or 256-bit AES")
            
            print("\n3. Encrypt External Drives:")
            print("   Format drive with APFS (Encrypted) or Mac OS Extended (Encrypted)")
            
            print("\n4. Terminal Commands:")
            print("   # Check FileVault status")
            print("   fdesetup status")
            print("   # Encrypt external drive")
            print("   diskutil coreStorage convert <disk> -passphrase")
            
        elif self.is_windows:
            print("\n🪟 Windows Encryption:")
            print("\n1. BitLocker (Full Disk Encryption):")
            print("   Settings → Privacy & Security → Device encryption")
            print("   Or: Control Panel → System and Security → BitLocker Drive Encryption")
            print("   Turn on BitLocker for system drive")
            print("   Save recovery key securely!")
            
            print("\n2. Encrypting File System (EFS):")
            print("   Right-click file/folder → Properties → Advanced")
            print("   Check 'Encrypt contents to secure data'")
            
            print("\n3. Encrypted Virtual Hard Disks:")
            print("   Disk Management → Create VHD → Format with BitLocker")
            
            print("\n4. PowerShell Commands:")
            print("   # Check BitLocker status")
            print("   Get-BitLockerVolume")
            print("   # Enable BitLocker")
            print("   Enable-BitLocker -MountPoint 'C:' -EncryptionMethod XtsAes256")
        
        print("\n💡 Encryption Best Practices:")
        print("   • Always encrypt system drive")
        print("   • Encrypt external drives with sensitive data")
        print("   • Store recovery keys securely (password manager)")
        print("   • Use strong encryption (AES-256)")
        print("   • Regular backups of encrypted data")
        
        print("\n" + "="*70)
    
    def privacy_controls(self):
        """Privacy settings and controls"""
        print("\n" + "="*70)
        print("PRIVACY CONTROLS")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Privacy Settings:")
            print("\n1. Location Services:")
            print("   System Settings → Privacy & Security → Location Services")
            print("   Control which apps can access location")
            
            print("\n2. Camera & Microphone:")
            print("   System Settings → Privacy & Security → Camera/Microphone")
            print("   Review and disable unnecessary access")
            
            print("\n3. Analytics & Improvements:")
            print("   System Settings → Privacy & Security → Analytics & Improvements")
            print("   Disable sharing if desired")
            
            print("\n4. Advertising:")
            print("   System Settings → Privacy & Security → Apple Advertising")
            print("   Turn off Personalized Ads")
            
            print("\n5. Screen Recording:")
            print("   System Settings → Privacy & Security → Screen Recording")
            print("   Only allow trusted apps")
            
        elif self.is_windows:
            print("\n🪟 Windows Privacy Settings:")
            print("\n1. Location Services:")
            print("   Settings → Privacy & Security → Location")
            print("   Control location access")
            
            print("\n2. Camera & Microphone:")
            print("   Settings → Privacy & Security → Camera/Microphone")
            print("   Review app permissions")
            
            print("\n3. Diagnostic Data:")
            print("   Settings → Privacy & Security → Diagnostics & feedback")
            print("   Choose 'Required diagnostic data' only")
            
            print("\n4. Advertising ID:")
            print("   Settings → Privacy & Security → General")
            print("   Turn off 'Let apps use advertising ID'")
            
            print("\n5. Activity History:")
            print("   Settings → Privacy & Security → Activity history")
            print("   Disable if not needed")
        
        print("\n💡 Privacy Best Practices:")
        print("   • Review app permissions regularly")
        print("   • Disable unnecessary location tracking")
        print("   • Limit camera/microphone access")
        print("   • Use private browsing when possible")
        print("   • Review privacy policies")
        print("   • Use VPN for sensitive activities")
        
        print("\n" + "="*70)
    
    def authentication_settings(self):
        """Password and authentication settings"""
        print("\n" + "="*70)
        print("PASSWORD & AUTHENTICATION")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS Authentication:")
            print("\n1. Password Settings:")
            print("   System Settings → Users & Groups → Change Password")
            print("   Use strong password (12+ characters, mixed case, numbers, symbols)")
            
            print("\n2. Touch ID / Face ID:")
            print("   System Settings → Touch ID & Password")
            print("   Enable for login and purchases")
            
            print("\n3. Two-Factor Authentication:")
            print("   System Settings → Apple ID → Password & Security")
            print("   Enable Two-Factor Authentication")
            
            print("\n4. Keychain Access:")
            print("   Applications → Utilities → Keychain Access")
            print("   Manage saved passwords securely")
            
        elif self.is_windows:
            print("\n🪟 Windows Authentication:")
            print("\n1. Password Settings:")
            print("   Settings → Accounts → Sign-in options")
            print("   Change password or set PIN")
            print("   Use strong password (12+ characters)")
            
            print("\n2. Windows Hello:")
            print("   Settings → Accounts → Sign-in options")
            print("   Set up Face, Fingerprint, or PIN")
            
            print("\n3. Microsoft Account 2FA:")
            print("   account.microsoft.com → Security")
            print("   Enable two-step verification")
            
            print("\n4. Password Manager:")
            print("   Use Windows Credential Manager or third-party manager")
        
        print("\n💡 Authentication Best Practices:")
        print("   • Use unique, strong passwords (password manager)")
        print("   • Enable two-factor authentication everywhere")
        print("   • Use biometric authentication when available")
        print("   • Never share passwords")
        print("   • Change default passwords immediately")
        print("   • Use passphrases for important accounts")
        print("   • Regular password audits")
        
        print("\n🔐 Recommended Password Managers:")
        print("   • 1Password")
        print("   • LastPass")
        print("   • Bitwarden (free)")
        print("   • KeePass (open source)")
        
        print("\n" + "="*70)
    
    def network_security(self):
        """Network security settings"""
        print("\n" + "="*70)
        print("NETWORK SECURITY")
        print("="*70)
        
        print("\n🌐 Network Security Best Practices:")
        print("\n1. WiFi Security:")
        print("   • Use WPA3 or WPA2 encryption")
        print("   • Change default router password")
        print("   • Use strong WiFi password (20+ characters)")
        print("   • Disable WPS")
        print("   • Hide SSID if desired")
        print("   • Enable MAC address filtering")
        
        print("\n2. VPN Usage:")
        print("   • Use VPN on public WiFi")
        print("   • Choose reputable VPN provider")
        print("   • Enable kill switch")
        print("   • Use DNS leak protection")
        
        print("\n3. DNS Security:")
        print("   • Use secure DNS (1.1.1.1, 8.8.8.8)")
        print("   • Enable DNS over HTTPS (DoH)")
        print("   • Use DNS over TLS (DoT)")
        
        print("\n4. Network Monitoring:")
        print("   • Monitor network traffic")
        print("   • Check for unknown devices")
        print("   • Review firewall logs")
        print("   • Use network scanning tools")
        
        if self.is_macos:
            print("\n🍎 macOS Network Security:")
            print("   • System Settings → Network → Firewall")
            print("   • Use built-in VPN client")
            print("   • Enable Stealth Mode in firewall")
            
        elif self.is_windows:
            print("\n🪟 Windows Network Security:")
            print("   • Windows Security → Firewall & network protection")
            print("   • Use built-in VPN client")
            print("   • Enable network discovery only on trusted networks")
        
        print("\n" + "="*70)
    
    def app_permissions(self):
        """Application permissions management"""
        print("\n" + "="*70)
        print("APPLICATION PERMISSIONS")
        print("="*70)
        
        if self.is_macos:
            print("\n🍎 macOS App Permissions:")
            print("\n1. Review Permissions:")
            print("   System Settings → Privacy & Security")
            print("   Review: Camera, Microphone, Location, Contacts, etc.")
            
            print("\n2. Full Disk Access:")
            print("   System Settings → Privacy & Security → Full Disk Access")
            print("   Only grant to trusted apps")
            
            print("\n3. Screen Recording:")
            print("   System Settings → Privacy & Security → Screen Recording")
            print("   Control which apps can record screen")
            
            print("\n4. Files and Folders:")
            print("   System Settings → Privacy & Security → Files and Folders")
            print("   Granular control over file access")
            
        elif self.is_windows:
            print("\n🪟 Windows App Permissions:")
            print("\n1. Review Permissions:")
            print("   Settings → Privacy & Security")
            print("   Review: Camera, Microphone, Location, etc.")
            
            print("\n2. App Permissions:")
            print("   Settings → Privacy & Security → App permissions")
            print("   Control access for each app")
            
            print("\n3. Background Apps:")
            print("   Settings → Privacy & Security → Background apps")
            print("   Disable unnecessary background apps")
        
        print("\n💡 Permission Best Practices:")
        print("   • Grant minimum necessary permissions")
        print("   • Review permissions regularly")
        print("   • Revoke unused permissions")
        print("   • Be cautious with full disk access")
        print("   • Check app privacy policies")
        
        print("\n" + "="*70)
    
    def security_checklist(self):
        """Security audit checklist"""
        print("\n" + "="*70)
        print("SECURITY AUDIT CHECKLIST")
        print("="*70)
        
        checklist = {
            "System Security": [
                "✓ System and apps are up to date",
                "✓ Firewall is enabled",
                "✓ Antivirus/anti-malware is active",
                "✓ Full disk encryption is enabled",
                "✓ Automatic updates are enabled",
                "✓ Screen lock is configured",
                "✓ Strong login password is set"
            ],
            "Authentication": [
                "✓ Two-factor authentication enabled on all accounts",
                "✓ Password manager is in use",
                "✓ All passwords are unique and strong",
                "✓ Biometric authentication is enabled",
                "✓ Recovery keys are stored securely"
            ],
            "Network Security": [
                "✓ WiFi uses WPA2/WPA3 encryption",
                "✓ Router password is changed from default",
                "✓ VPN is used on public networks",
                "✓ Firewall rules are configured",
                "✓ Unknown devices are not on network"
            ],
            "Privacy": [
                "✓ Location services reviewed",
                "✓ Camera/microphone permissions reviewed",
                "✓ App permissions are minimal",
                "✓ Analytics sharing is limited",
                "✓ Advertising tracking is disabled"
            ],
            "Backup & Recovery": [
                "✓ Regular backups are configured",
                "✓ Backup encryption is enabled",
                "✓ Recovery process is tested",
                "✓ Backup storage is secure"
            ],
            "Software": [
                "✓ Only trusted software is installed",
                "✓ Unused software is removed",
                "✓ Software sources are verified",
                "✓ Browser extensions are reviewed"
            ]
        }
        
        for category, items in checklist.items():
            print(f"\n📋 {category}:")
            for item in items:
                print(f"   {item}")
        
        print("\n💡 Regular Security Maintenance:")
        print("   • Weekly: Review recent app installations")
        print("   • Monthly: Update all software")
        print("   • Quarterly: Full security audit")
        print("   • Annually: Review and update security policies")
        
        print("\n" + "="*70)
    
    def advanced_hardening(self):
        """Advanced security hardening techniques"""
        print("\n" + "="*70)
        print("ADVANCED SECURITY HARDENING")
        print("="*70)
        
        print("\n⚠️  WARNING: Advanced settings may affect system functionality.")
        print("   Only apply if you understand the implications.\n")
        
        if self.is_macos:
            print("🍎 macOS Advanced Hardening:")
            print("\n1. System Integrity Protection (SIP):")
            print("   # Check SIP status")
            print("   csrutil status")
            print("   # Enable SIP (if disabled)")
            print("   # Boot to Recovery Mode, then:")
            print("   csrutil enable")
            
            print("\n2. Disable Remote Management:")
            print("   System Settings → General → Sharing")
            print("   Disable Remote Management")
            
            print("\n3. Secure Boot:")
            print("   System Settings → Privacy & Security")
            print("   Enable 'Require password after sleep'")
            
            print("\n4. Disable Guest Account:")
            print("   System Settings → Users & Groups")
            print("   Disable Guest User")
            
            print("\n5. Terminal Hardening:")
            print("   # Disable root login")
            print("   sudo dscl . -create /Users/root UserShell /usr/bin/false")
            
        elif self.is_windows:
            print("🪟 Windows Advanced Hardening:")
            print("\n1. Group Policy (Pro/Enterprise):")
            print("   gpedit.msc → Computer Configuration")
            print("   Configure security policies")
            
            print("\n2. Disable Unnecessary Services:")
            print("   services.msc")
            print("   Review and disable unused services")
            
            print("\n3. Windows Defender Advanced:")
            print("   Windows Security → Virus & threat protection")
            print("   Advanced settings → Enable all protections")
            
            print("\n4. User Account Control (UAC):")
            print("   Control Panel → User Accounts")
            print("   Set UAC to 'Always notify'")
            
            print("\n5. Disable SMBv1:")
            print("   # PowerShell (Admin)")
            print("   Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol")
        
        print("\n💡 Additional Hardening:")
        print("   • Enable audit logging")
        print("   • Configure intrusion detection")
        print("   • Use application whitelisting")
        print("   • Implement least privilege access")
        print("   • Regular security scans")
        print("   • Monitor system logs")
        
        print("\n📚 Resources:")
        print("   • CIS Benchmarks (Center for Internet Security)")
        print("   • NIST Cybersecurity Framework")
        print("   • OWASP Security Guidelines")
        
        print("\n" + "="*70)

