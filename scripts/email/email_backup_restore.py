#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
import json
import shutil
import zipfile

#!/usr/bin/env python3
"""
Email Backup & Restore System
Backup and restore email configurations
"""


class EmailBackupRestore:
    """Email backup and restore system"""

    def __init__(self):
        self.config_dir = Path.home() / ".it_genius"
        self.backup_dir = self.config_dir / "backups"
        self.backup_dir.mkdir(exist_ok=True, parents=True)

    def create_backup(self):
        """Create complete backup"""
        print("\n" + "="*80)
        print("💾 CREATING EMAIL CONFIGURATION BACKUP")
        print("="*80)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"email_backup_{timestamp}"
        backup_path = self.backup_dir / backup_name
        backup_path.mkdir(exist_ok=True)

        # Backup all config files
        config_files = [
            "email_config.json",
            "gmail_hotrod_config.json",
            "email_master_config.json",
            "email_automation.json"
        ]

        backed_up = []
        for config_file in config_files:
            src = self.config_dir / config_file
            if src.exists():
                dst = backup_path / config_file
                shutil.copy2(src, dst)
                backed_up.append(config_file)

        # Create backup manifest
        manifest = {
            "backup_date": datetime.now().isoformat(),
            "backup_name": backup_name,
            "files_backed_up": backed_up,
            "domains": {
                "fishmusicinc.com": ["rp@fishmusicinc.com", "info@fishmusicinc.com"],
                "noizylab.ca": ["rsp@noizylab.ca", "help@noizylab.ca", "hello@noizylab.ca"],
                "icloud.com": ["rsplowman@icloud.com"]
            },
            "gmail": "rsplowman@gmail.com"
        }

        manifest_path = backup_path / "backup_manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)

        # Create ZIP archive
        zip_path = self.backup_dir / f"{backup_name}.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in backup_path.rglob('*'):
                if file.is_file():
                    zipf.write(file, file.relative_to(backup_path))

        print(f"\n✅ Backup created successfully!")
        print(f"   Location: {backup_path}")
        print(f"   ZIP Archive: {zip_path}")
        print(f"   Files backed up: {len(backed_up)}")

        return backup_path, zip_path

    def list_backups(self):
        """List all backups"""
        print("\n" + "="*80)
        print("📋 AVAILABLE BACKUPS")
        print("="*80)

        backups = sorted(self.backup_dir.glob("email_backup_*"), reverse=True)

        if not backups:
            print("\n⏳ No backups found.")
            return []

        print(f"\nFound {len(backups)} backup(s):\n")
        for i, backup in enumerate(backups, 1):
            if backup.is_dir():
                manifest = backup / "backup_manifest.json"
                if manifest.exists():
                    with open(manifest, 'r') as f:
                        data = json.load(f)
                    date = data.get("backup_date", "Unknown")
                    print(f"  {i}. {backup.name}")
                    print(f"     Date: {date}")
                    print(f"     Files: {len(data.get('files_backed_up', []))}")
                else:
                    print(f"  {i}. {backup.name}")

        return backups

    def restore_backup(self, backup_path=None):
        """Restore from backup"""
        print("\n" + "="*80)
        print("🔄 RESTORING FROM BACKUP")
        print("="*80)

        if backup_path is None:
            backups = self.list_backups()
            if not backups:
                return

            choice = input("\nSelect backup to restore (number): ").strip()
            try:
                backup_path = backups[int(choice) - 1]
            except (ValueError, IndexError):
                print("❌ Invalid selection")
                return

        manifest = backup_path / "backup_manifest.json"
        if not manifest.exists():
            print("❌ Backup manifest not found")
            return

        with open(manifest, 'r') as f:
            data = json.load(f)

        print(f"\n📋 Backup Info:")
        print(f"   Date: {data.get('backup_date')}")
        print(f"   Files: {len(data.get('files_backed_up', []))}")

        confirm = input("\n⚠️  This will overwrite current configurations. Continue? (y/n): ").strip().lower()
        if confirm != 'y':
            print("❌ Restore cancelled")
            return

        # Restore files
        restored = []
        for config_file in data.get("files_backed_up", []):
            src = backup_path / config_file
            if src.exists():
                dst = self.config_dir / config_file
                shutil.copy2(src, dst)
                restored.append(config_file)

        print(f"\n✅ Restore complete!")
        print(f"   Files restored: {len(restored)}")

    def export_configuration(self):
        """Export configuration for sharing"""
        print("\n" + "="*80)
        print("📤 EXPORT CONFIGURATION")
        print("="*80)

        export_data = {
            "export_date": datetime.now().isoformat(),
            "gmail": "rsplowman@gmail.com",
            "domains": {
                "fishmusicinc.com": {
                    "emails": ["rp@fishmusicinc.com", "info@fishmusicinc.com"],
                    "pop_server": "mail.fishmusicinc.com",
                    "smtp_server": "mail.fishmusicinc.com"
                },
                "noizylab.ca": {
                    "emails": ["rsp@noizylab.ca", "help@noizylab.ca", "hello@noizylab.ca"],
                    "pop_server": "mail.noizylab.ca",
                    "smtp_server": "mail.noizylab.ca"
                },
                "icloud.com": {
                    "emails": ["rsplowman@icloud.com"],
                    "pop_server": "pop.mail.me.com",
                    "smtp_server": "smtp.mail.me.com"
                }
            },
            "server_settings": {
                "pop_port": 995,
                "smtp_port": 587,
                "security": "SSL/TLS"
            }
        }

        export_file = self.config_dir / "email_configuration_export.json"
        with open(export_file, 'w') as f:
            json.dump(export_data, f, indent=2)

        print(f"\n✅ Configuration exported to: {export_file}")
        print(f"   This file can be shared or imported on another system.")

    def main_menu(self):
        """Main menu"""
        while True:
            print("\n" + "="*80)
            print("💾 EMAIL BACKUP & RESTORE SYSTEM")
            print("="*80)
            print("\nOptions:")
            print("  1. 💾 Create Backup")
            print("  2. 📋 List Backups")
            print("  3. 🔄 Restore Backup")
            print("  4. 📤 Export Configuration")
            print("  5. 🗑️  Delete Backup")
            print("  0. Exit")
            print("="*80)

            choice = input("\nSelect option: ").strip()

            if choice == "1":
                self.create_backup()
            elif choice == "2":
                self.list_backups()
            elif choice == "3":
                self.restore_backup()
            elif choice == "4":
                self.export_configuration()
            elif choice == "5":
                self.delete_backup()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option")

            if choice != "0":
                input("\nPress Enter to continue...")

    def delete_backup(self):
        """Delete a backup"""
        backups = self.list_backups()
        if not backups:
            return

        choice = input("\nSelect backup to delete (number): ").strip()
        try:
            backup = backups[int(choice) - 1]
            confirm = input(f"\n⚠️  Delete {backup.name}? (y/n): ").strip().lower()
            if confirm == 'y':
                if backup.is_dir():
                    shutil.rmtree(backup)
                else:
                    backup.unlink()
                print("✅ Backup deleted!")
        except (ValueError, IndexError):
            print("❌ Invalid selection")

if __name__ == "__main__":
    backup = EmailBackupRestore()
    backup.main_menu()

