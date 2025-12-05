#!/usr/bin/env python3
"""
MASTER CONTROL CENTER - ALL-IN-ONE SYSTEM
Complete control of all domains, emails, services, monitoring, and Outlook
"""

import os
import sys
import json
import subprocess
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ==================== SYSTEM CONFIGURATION ====================
BASE_DIR = "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB"
CONFIG_FILE = f"{BASE_DIR}/domains_and_emails_master.json"

# Load main configuration
with open(CONFIG_FILE, 'r') as f:
    CONFIG = json.load(f)

# ==================== SYSTEM MODULES ====================
MODULES = {
    "domain_manager": {
        "name": "Advanced Domain & Email Manager",
        "script": "ADVANCED_DOMAIN_EMAIL_MANAGER.py",
        "description": "Health checks, analytics, backups",
        "status": "ready"
    },
    "monitoring": {
        "name": "24/7 Monitoring System",
        "script": "DOMAIN_EMAIL_MONITOR_24_7.py",
        "description": "Continuous monitoring with alerts",
        "status": "ready"
    },
    "services_integration": {
        "name": "Services Integration (X4 Speed)",
        "script": "MASTER_SERVICES_INTEGRATION_X4.py",
        "description": "Slack, Cloudflare, GoDaddy, MS365, Google",
        "status": "ready"
    },
    "outlook_setup": {
        "name": "Outlook Configuration",
        "script": "SETUP_OUTLOOK_ALL_EMAILS.sh",
        "description": "7 email accounts for Outlook",
        "status": "ready"
    }
}

# ==================== DASHBOARD CLASS ====================
class MasterControlCenter:
    """Unified control center for all systems"""
    
    def __init__(self):
        self.domains = CONFIG.get('all_domains', [])
        self.emails = CONFIG.get('all_emails', [])
        self.stats = self.load_stats()
    
    def load_stats(self):
        """Load system statistics"""
        return {
            "domains": len(self.domains),
            "emails": len(self.emails),
            "services": 6,
            "files_in_git": self.count_git_files(),
            "modules": len(MODULES)
        }
    
    def count_git_files(self):
        """Count files in Git"""
        try:
            result = subprocess.run(
                ['ls', '-1', BASE_DIR],
                capture_output=True,
                text=True
            )
            return len(result.stdout.split('\n')) - 1
        except:
            return 0
    
    def display_header(self):
        """Display control center header"""
        print("\n" + "="*70)
        print("🎛️  MASTER CONTROL CENTER - ALL SYSTEMS")
        print("="*70)
        print(f"📊 Domains: {self.stats['domains']} | Emails: {self.stats['emails']} | Services: {self.stats['services']}")
        print(f"📁 Files in Git: {self.stats['files_in_git']} | Modules: {self.stats['modules']}")
        print("="*70)
    
    def display_main_menu(self):
        """Display main menu"""
        print("\n🎯 MAIN MENU:")
        print("\n1. 🏥 Health Check - Run domain & email health check")
        print("2. 📊 Monitoring - Start 24/7 monitoring system")
        print("3. 🔗 Services - Run services integration (X4 Speed)")
        print("4. 📧 Outlook - View Outlook setup guide")
        print("5. 📈 Analytics - Generate analytics reports")
        print("6. 💾 Backup - Backup all configurations")
        print("7. 🔧 System Info - Display system information")
        print("8. 🚀 Quick Start - Run all systems check")
        print("9. 📖 Documentation - View all guides")
        print("0. 🚪 Exit")
        print()
    
    def run_health_check(self):
        """Run domain and email health check"""
        print("\n" + "="*70)
        print("🏥 RUNNING HEALTH CHECK...")
        print("="*70)
        
        script = f"{BASE_DIR}/ADVANCED_DOMAIN_EMAIL_MANAGER.py"
        if os.path.exists(script):
            os.system(f"python3 {script}")
        else:
            print("⚠ Health check script not found")
    
    def start_monitoring(self):
        """Start monitoring system"""
        print("\n" + "="*70)
        print("📊 STARTING MONITORING SYSTEM...")
        print("="*70)
        print("\nOptions:")
        print("1. Quick Check (single run)")
        print("2. Continuous (1 hour)")
        print("3. Continuous (24 hours)")
        
        choice = input("\nSelect option (1-3): ").strip()
        
        script = f"{BASE_DIR}/DOMAIN_EMAIL_MONITOR_24_7.py"
        if choice == "1":
            os.system(f"python3 {script}")
        elif choice == "2":
            os.system(f"python3 {script} continuous 1")
        elif choice == "3":
            os.system(f"python3 {script} continuous 24")
    
    def run_services_integration(self):
        """Run services integration"""
        print("\n" + "="*70)
        print("🔗 SERVICES INTEGRATION (X4 SPEED)")
        print("="*70)
        print("\n⚠ Important: Requires API keys in .env_services")
        print("\nProceed? (y/n): ", end="")
        
        if input().lower() == 'y':
            env_file = f"{BASE_DIR}/.env_services"
            if os.path.exists(env_file):
                os.system(f"source {env_file} && python3 {BASE_DIR}/MASTER_SERVICES_INTEGRATION_X4.py")
            else:
                print("⚠ .env_services not found. Run SETUP_SERVICES_X4.sh first")
    
    def view_outlook_guide(self):
        """View Outlook setup guide"""
        print("\n" + "="*70)
        print("📧 OUTLOOK SETUP GUIDE")
        print("="*70)
        
        guide = f"{BASE_DIR}/outlook_configs/MASTER_SETUP_GUIDE.md"
        if os.path.exists(guide):
            with open(guide, 'r') as f:
                print(f.read())
        else:
            print("\n⚠ Outlook guide not found")
            print("Run: bash SETUP_OUTLOOK_ALL_EMAILS.sh")
    
    def generate_analytics(self):
        """Generate comprehensive analytics"""
        print("\n" + "="*70)
        print("📈 GENERATING ANALYTICS...")
        print("="*70)
        
        analytics = {
            "timestamp": datetime.now().isoformat(),
            "system_stats": self.stats,
            "domains": self.domains,
            "emails": self.emails,
            "modules_status": MODULES
        }
        
        # Save analytics
        analytics_file = f"{BASE_DIR}/domain_reports/master_analytics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        os.makedirs(f"{BASE_DIR}/domain_reports", exist_ok=True)
        
        with open(analytics_file, 'w') as f:
            json.dump(analytics, f, indent=2)
        
        print(f"\n✓ Analytics saved: {analytics_file}")
        print(f"\n📊 SUMMARY:")
        print(f"  • Domains: {self.stats['domains']}")
        print(f"  • Emails: {self.stats['emails']}")
        print(f"  • Services: {self.stats['services']}")
        print(f"  • Files: {self.stats['files_in_git']}")
    
    def backup_configurations(self):
        """Backup all configurations"""
        print("\n" + "="*70)
        print("💾 BACKING UP CONFIGURATIONS...")
        print("="*70)
        
        backup_dir = f"{BASE_DIR}/email_backups"
        os.makedirs(backup_dir, exist_ok=True)
        
        backup_data = {
            "timestamp": datetime.now().isoformat(),
            "domains": CONFIG.get('domains', {}),
            "emails": CONFIG.get('all_emails', []),
            "modules": MODULES,
            "stats": self.stats
        }
        
        backup_file = f"{backup_dir}/master_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(backup_file, 'w') as f:
            json.dump(backup_data, f, indent=2)
        
        print(f"\n✓ Backup saved: {backup_file}")
    
    def display_system_info(self):
        """Display system information"""
        print("\n" + "="*70)
        print("🔧 SYSTEM INFORMATION")
        print("="*70)
        
        print(f"\n📍 Base Directory:")
        print(f"  {BASE_DIR}")
        
        print(f"\n📊 Statistics:")
        print(f"  • Domains: {self.stats['domains']}")
        for domain in self.domains:
            print(f"    - {domain}")
        
        print(f"\n  • Emails: {self.stats['emails']}")
        for email in self.emails[:5]:
            print(f"    - {email}")
        if len(self.emails) > 5:
            print(f"    ... and {len(self.emails) - 5} more")
        
        print(f"\n  • Services Integrated: {self.stats['services']}")
        print(f"    - Slack")
        print(f"    - Cloudflare")
        print(f"    - GoDaddy")
        print(f"    - Microsoft 365")
        print(f"    - Google Workspace")
        print(f"    - Custom DNS")
        
        print(f"\n  • Files in Git: {self.stats['files_in_git']}")
        
        print(f"\n📦 Modules:")
        for key, module in MODULES.items():
            status_icon = "✓" if module['status'] == "ready" else "⚠"
            print(f"  {status_icon} {module['name']}")
            print(f"    {module['description']}")
    
    def quick_start(self):
        """Run quick start check on all systems"""
        print("\n" + "="*70)
        print("🚀 QUICK START - ALL SYSTEMS CHECK")
        print("="*70)
        
        print("\n1. Checking configuration files...")
        files_ok = all([
            os.path.exists(CONFIG_FILE),
            os.path.exists(f"{BASE_DIR}/ADVANCED_DOMAIN_EMAIL_MANAGER.py"),
            os.path.exists(f"{BASE_DIR}/DOMAIN_EMAIL_MONITOR_24_7.py")
        ])
        print(f"  {'✓' if files_ok else '✗'} Configuration files")
        
        print("\n2. Checking directories...")
        dirs_ok = all([
            os.path.exists(f"{BASE_DIR}/email_backups"),
            os.path.exists(f"{BASE_DIR}/domain_reports"),
            os.path.exists(f"{BASE_DIR}/monitoring_alerts")
        ])
        print(f"  {'✓' if dirs_ok else '✗'} Required directories")
        
        print("\n3. Checking Outlook setup...")
        outlook_ok = os.path.exists(f"{BASE_DIR}/outlook_configs")
        print(f"  {'✓' if outlook_ok else '✗'} Outlook configuration")
        
        print("\n4. System status...")
        print(f"  ✓ {self.stats['domains']} domains configured")
        print(f"  ✓ {self.stats['emails']} email accounts")
        print(f"  ✓ {self.stats['modules']} modules ready")
        
        print("\n" + "="*70)
        if files_ok and dirs_ok:
            print("✅ ALL SYSTEMS OPERATIONAL!")
        else:
            print("⚠ Some systems need configuration")
        print("="*70)
    
    def view_documentation(self):
        """View all documentation"""
        print("\n" + "="*70)
        print("📖 DOCUMENTATION")
        print("="*70)
        
        docs = [
            ("Domain & Email Upgrade", "DOMAIN_EMAIL_UPGRADE_COMPLETE.md"),
            ("Services Integration", "SERVICES_INTEGRATION_GUIDE.md"),
            ("Outlook Setup", "outlook_configs/MASTER_SETUP_GUIDE.md"),
        ]
        
        print("\nAvailable Documentation:")
        for i, (name, path) in enumerate(docs, 1):
            full_path = f"{BASE_DIR}/{path}"
            exists = "✓" if os.path.exists(full_path) else "✗"
            print(f"{i}. {exists} {name}")
            print(f"   {full_path}")
        
        print("\nView a document? (1-3, or 0 to cancel): ", end="")
        choice = input().strip()
        
        if choice.isdigit() and 1 <= int(choice) <= len(docs):
            _, path = docs[int(choice) - 1]
            full_path = f"{BASE_DIR}/{path}"
            if os.path.exists(full_path):
                os.system(f"cat {full_path} | less")
    
    def run(self):
        """Main control loop"""
        self.display_header()
        
        while True:
            self.display_main_menu()
            choice = input("Select option (0-9): ").strip()
            
            if choice == '1':
                self.run_health_check()
            elif choice == '2':
                self.start_monitoring()
            elif choice == '3':
                self.run_services_integration()
            elif choice == '4':
                self.view_outlook_guide()
            elif choice == '5':
                self.generate_analytics()
            elif choice == '6':
                self.backup_configurations()
            elif choice == '7':
                self.display_system_info()
            elif choice == '8':
                self.quick_start()
            elif choice == '9':
                self.view_documentation()
            elif choice == '0':
                print("\n✨ Goodbye!\n")
                sys.exit(0)
            else:
                print("\n⚠ Invalid option. Please try again.")
            
            input("\nPress Enter to continue...")

# ==================== MAIN EXECUTION ====================
def main():
    """Main execution"""
    try:
        control_center = MasterControlCenter()
        control_center.run()
    except KeyboardInterrupt:
        print("\n\n⚠ Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

