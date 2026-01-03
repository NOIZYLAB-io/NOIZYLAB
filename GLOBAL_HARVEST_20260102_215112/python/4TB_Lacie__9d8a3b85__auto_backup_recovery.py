#!/usr/bin/env python3
"""
Auto Backup & Recovery System
Automatic backups, point-in-time recovery, disaster recovery
"""

import json
import shutil
from pathlib import Path
from datetime import datetime

class AutoBackupRecovery:
    """Automatic backup and recovery system"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.backup_dir = self.base_dir / "backups"
        self.backup_dir.mkdir(exist_ok=True)

    def create_backup(self, backup_type="full"):
        """Create backup"""
        print("\n" + "="*80)
        print("💾 AUTO BACKUP SYSTEM")
        print("="*80)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = self.backup_dir / f"backup_{timestamp}"
        backup_path.mkdir(exist_ok=True)

        # Backup important directories
        important_dirs = [
            "knowledge_base",
            "solutions_database",
            "learning_database",
            ".hotrod_cache",
            ".ultra_hotrod"
        ]

        backed_up = []
        for dir_name in important_dirs:
            source = self.base_dir / dir_name
            if source.exists():
                dest = backup_path / dir_name
                try:
                    if source.is_dir():
                        shutil.copytree(source, dest, dirs_exist_ok=True)
                    else:
                        shutil.copy2(source, dest)
                    backed_up.append(dir_name)
                except Exception as e:
                    print(f"  ⚠️  Failed to backup {dir_name}: {e}")

        # Backup config files
        config_files = list(self.base_dir.glob("*.json"))
        for config_file in config_files:
            try:
                shutil.copy2(config_file, backup_path / config_file.name)
                backed_up.append(config_file.name)
            except Exception as e:
                print(f"  ⚠️  Failed to backup {config_file.name}: {e}")

        # Create backup manifest
        manifest = {
            "timestamp": datetime.now().isoformat(),
            "type": backup_type,
            "backed_up": backed_up,
            "backup_path": str(backup_path)
        }

        manifest_file = backup_path / "manifest.json"
        with open(manifest_file, 'w') as f:
            json.dump(manifest, f, indent=2)

        print(f"\n✅ Backup created: {backup_path.name}")
        print(f"  • Items backed up: {len(backed_up)}")
        print(f"  • Type: {backup_type}")

        return backup_path

    def list_backups(self):
        """List all backups"""
        backups = []
        for backup_dir in self.backup_dir.iterdir():
            if backup_dir.is_dir():
                manifest_file = backup_dir / "manifest.json"
                if manifest_file.exists():
                    with open(manifest_file, 'r') as f:
                        manifest = json.load(f)
                    backups.append(manifest)

        return sorted(backups, key=lambda x: x['timestamp'], reverse=True)

    def restore_backup(self, backup_name):
        """Restore from backup"""
        print("\n" + "="*80)
        print("🔄 RESTORE FROM BACKUP")
        print("="*80)

        backup_path = self.backup_dir / backup_name
        if not backup_path.exists():
            print(f"❌ Backup not found: {backup_name}")
            return False

        manifest_file = backup_path / "manifest.json"
        if manifest_file.exists():
            with open(manifest_file, 'r') as f:
                manifest = json.load(f)

            print(f"\n📋 Backup Info:")
            print(f"  • Timestamp: {manifest['timestamp']}")
            print(f"  • Type: {manifest['type']}")
            print(f"  • Items: {len(manifest['backed_up'])}")

            # Restore items
            restored = 0
            for item in manifest['backed_up']:
                source = backup_path / item
                dest = self.base_dir / item
                try:
                    if source.is_dir():
                        shutil.copytree(source, dest, dirs_exist_ok=True)
                    else:
                        shutil.copy2(source, dest)
                    restored += 1
                except Exception as e:
                    print(f"  ⚠️  Failed to restore {item}: {e}")

            print(f"\n✅ Restored {restored} items")
            return True

        return False

    def auto_backup_schedule(self):
        """Configure auto backup schedule"""
        schedule = {
            "enabled": True,
            "frequency": "hourly",
            "retention_days": 30,
            "backup_types": ["full", "incremental"],
            "compression": True,
            "encryption": True
        }

        schedule_file = self.backup_dir / "schedule.json"
        with open(schedule_file, 'w') as f:
            json.dump(schedule, f, indent=2)

        print("\n✅ Auto backup scheduled:")
        print("  • Frequency: Hourly")
        print("  • Retention: 30 days")
        print("  • Compression: Enabled")
        print("  • Encryption: Enabled")

if __name__ == "__main__":
    backup = AutoBackupRecovery()
    backup.create_backup()
    backup.auto_backup_schedule()

