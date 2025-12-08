#!/usr/bin/env python3
"""
Backup & Restore - Data Protection
==================================
"""

import json
import shutil
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

console = Console()

class BackupRestore:
    def __init__(self, backup_dir: str = "backups"):
        """Initialize Backup & Restore"""
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)
    
    def create_backup(self) -> str:
        """Create a backup of all data"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{timestamp}"
        backup_path = self.backup_dir / backup_name
        backup_path.mkdir(exist_ok=True)
        
        # Files to backup
        files_to_backup = [
            "config/email_config.json",
            "config/contacts.json",
            "config/templates.json",
            "config/drafts.json",
            "email_history.log"
        ]
        
        backed_up = []
        for file_path in files_to_backup:
            src = Path(file_path)
            if src.exists():
                dst = backup_path / src.name
                shutil.copy2(src, dst)
                backed_up.append(file_path)
        
        # Create manifest
        manifest = {
            "timestamp": timestamp,
            "backup_name": backup_name,
            "files": backed_up
        }
        
        with open(backup_path / "manifest.json", 'w') as f:
            json.dump(manifest, f, indent=2)
        
        console.print(f"[green]✅ Backup created: {backup_name}[/green]")
        console.print(f"[dim]Files backed up: {len(backed_up)}[/dim]")
        
        return backup_name
    
    def list_backups(self) -> list:
        """List all available backups"""
        backups = []
        for backup_dir in self.backup_dir.iterdir():
            if backup_dir.is_dir():
                manifest_path = backup_dir / "manifest.json"
                if manifest_path.exists():
                    try:
                        with open(manifest_path, 'r') as f:
                            manifest = json.load(f)
                            backups.append({
                                "name": backup_dir.name,
                                "timestamp": manifest.get("timestamp", ""),
                                "files": manifest.get("files", [])
                            })
                    except:
                        pass
        
        return sorted(backups, key=lambda x: x['timestamp'], reverse=True)
    
    def restore_backup(self, backup_name: str) -> bool:
        """Restore from backup"""
        backup_path = self.backup_dir / backup_name
        
        if not backup_path.exists():
            console.print(f"[red]❌ Backup not found: {backup_name}[/red]")
            return False
        
        manifest_path = backup_path / "manifest.json"
        if not manifest_path.exists():
            console.print(f"[red]❌ Invalid backup: {backup_name}[/red]")
            return False
        
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        console.print(f"[yellow]⚠️  This will overwrite existing files![/yellow]")
        confirm = Confirm.ask(f"[bold]Restore backup {backup_name}?[/bold]", default=False)
        
        if not confirm:
            return False
        
        # Restore files
        restored = []
        for file_name in manifest.get("files", []):
            src = backup_path / Path(file_name).name
            dst = Path(file_name)
            
            if src.exists():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                restored.append(file_name)
        
        console.print(f"[green]✅ Restored {len(restored)} files[/green]")
        return True
    
    def display_backups(self):
        """Display available backups"""
        backups = self.list_backups()
        
        if not backups:
            console.print("[yellow]No backups found[/yellow]")
            return
        
        from rich.table import Table
        table = Table(title="📦 Available Backups", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Date", style="green")
        table.add_column("Files", style="yellow", justify="right")
        
        for backup in backups:
            date_str = backup['timestamp'][:8] if len(backup['timestamp']) >= 8 else backup['timestamp']
            table.add_row(
                backup['name'],
                date_str,
                str(len(backup.get('files', [])))
            )
        
        console.print(table)

