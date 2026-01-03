#!/usr/bin/env python3
"""
IT Genius - Comprehensive IT Setup Assistant
A tool to help with all types of computer and system configurations
"""

import json
import os
import sys
import platform
import subprocess
from typing import Dict, List, Optional
from pathlib import Path

class ITGenius:
    """Main IT Genius class for system setup and configuration"""
    
    def __init__(self):
        self.config_dir = Path.home() / ".it_genius"
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.load_config()
        self.system_info = self.get_system_info()
    
    def load_config(self):
        """Load or create configuration file"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "saved_emails": {},
                "network_profiles": {},
                "system_settings": {}
            }
            self.save_config()
    
    def save_config(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def get_system_info(self) -> Dict:
        """Get system information"""
        return {
            "os": platform.system(),
            "os_version": platform.version(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "hostname": platform.node()
        }
    
    def display_banner(self):
        """Display welcome banner"""
        print("\n" + "="*70)
        print(" " * 20 + "IT GENIUS - Setup Assistant")
        print("="*70)
        print(f"\nSystem: {self.system_info['os']} {self.system_info['os_version']}")
        print(f"Architecture: {self.system_info['architecture']}")
        print(f"Hostname: {self.system_info['hostname']}\n")
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "-"*70)
        print("MAIN MENU")
        print("-"*70)
        print("1. Email Account Setup")
        print("2. Network Configuration")
        print("3. System Diagnostics")
        print("4. Software Installation Guides")
        print("5. Security & Privacy Settings")
        print("6. Backup & Recovery")
        print("7. Performance Optimization")
        print("8. View Saved Configurations")
        print("9. Export Configuration")
        print("0. Exit")
        print("-"*70)
    
    def email_setup(self):
        """Email account setup wizard"""
        from email_setup import EmailSetup
        email_wizard = EmailSetup(self.config)
        email_wizard.run()
        self.save_config()
    
    def network_setup(self):
        """Network configuration wizard"""
        from network_setup import NetworkSetup
        network_wizard = NetworkSetup(self.config)
        network_wizard.run()
        self.save_config()
    
    def system_diagnostics(self):
        """Run system diagnostics"""
        from system_diagnostics import SystemDiagnostics
        diagnostics = SystemDiagnostics(self.system_info)
        diagnostics.run()
    
    def software_guides(self):
        """Software installation guides"""
        from software_guides import SoftwareGuides
        guides = SoftwareGuides()
        guides.show_menu()
    
    def security_settings(self):
        """Security and privacy settings"""
        from security_settings import SecuritySettings
        security = SecuritySettings(self.system_info)
        security.show_menu()
    
    def backup_recovery(self):
        """Backup and recovery tools"""
        from backup_recovery import BackupRecovery
        backup = BackupRecovery(self.config)
        backup.show_menu()
    
    def performance_optimization(self):
        """Performance optimization tools"""
        from performance_optimization import PerformanceOptimization
        perf = PerformanceOptimization(self.system_info)
        perf.show_menu()
    
    def view_saved_configs(self):
        """View all saved configurations"""
        print("\n" + "="*70)
        print("SAVED CONFIGURATIONS")
        print("="*70)
        
        if self.config.get("saved_emails"):
            print("\n📧 Email Accounts:")
            for email, settings in self.config["saved_emails"].items():
                print(f"  • {email}")
                print(f"    Provider: {settings.get('provider', 'Unknown')}")
                print(f"    IMAP: {settings.get('imap_server', 'N/A')}")
                print(f"    SMTP: {settings.get('smtp_server', 'N/A')}")
        
        if self.config.get("network_profiles"):
            print("\n🌐 Network Profiles:")
            for profile_name, profile in self.config["network_profiles"].items():
                print(f"  • {profile_name}")
                print(f"    Type: {profile.get('type', 'Unknown')}")
        
        if not self.config.get("saved_emails") and not self.config.get("network_profiles"):
            print("\nNo saved configurations yet.")
        
        print("\n" + "="*70)
        input("\nPress Enter to continue...")
    
    def export_config(self):
        """Export configuration to file"""
        export_file = input("\nEnter filename to export (default: it_genius_export.json): ").strip()
        if not export_file:
            export_file = "it_genius_export.json"
        
        if not export_file.endswith('.json'):
            export_file += '.json'
        
        try:
            with open(export_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            print(f"✅ Configuration exported to: {export_file}")
        except Exception as e:
            print(f"❌ Error exporting: {e}")
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Main run loop"""
        self.display_banner()
        
        while True:
            self.display_menu()
            choice = input("\nSelect an option: ").strip()
            
            try:
                if choice == "1":
                    self.email_setup()
                elif choice == "2":
                    self.network_setup()
                elif choice == "3":
                    self.system_diagnostics()
                elif choice == "4":
                    self.software_guides()
                elif choice == "5":
                    self.security_settings()
                elif choice == "6":
                    self.backup_recovery()
                elif choice == "7":
                    self.performance_optimization()
                elif choice == "8":
                    self.view_saved_configs()
                elif choice == "9":
                    self.export_config()
                elif choice == "0":
                    print("\n👋 Thank you for using IT Genius!")
                    sys.exit(0)
                else:
                    print("\n❌ Invalid option. Please try again.")
            except KeyboardInterrupt:
                print("\n\n👋 Exiting...")
                sys.exit(0)
            except Exception as e:
                print(f"\n❌ Error: {e}")
                input("Press Enter to continue...")


if __name__ == "__main__":
    try:
        genius = ITGenius()
        genius.run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)

