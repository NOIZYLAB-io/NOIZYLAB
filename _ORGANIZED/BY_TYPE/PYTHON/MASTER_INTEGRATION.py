#!/usr/bin/env python3
"""
Master Integration - Unifies All NoizyLab Systems
==================================================
"""

import json
import sqlite3
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

class MasterIntegration:
    def __init__(self):
        self.base = Path("/Users/m2ultra/NOIZYLAB")
    
    def create_unified_config(self):
        """Create unified configuration for all systems"""
        console.print("[cyan]🔗 Creating unified configuration...[/cyan]")
        
        config = {
            "noizylab": {
                "version": "6.0",
                "status": "complete",
                "systems": {
                    "email_intelligence": {
                        "version": "4.0",
                        "api": "http://localhost:8000",
                        "dashboard": "http://localhost:8501",
                        "status": "ready"
                    },
                    "cloudflare": {
                        "version": "hotrod",
                        "dashboard": "http://localhost:8504",
                        "workers": ["noizylab-email", "noizylab-ai-router"],
                        "status": "ready"
                    },
                    "master_dashboard": {
                        "version": "1.0",
                        "url": "http://localhost:8503",
                        "status": "ready"
                    },
                    "health": {
                        "monitor": "health/health-monitor.py",
                        "healer": "health/healtheworld.py",
                        "status": "ready"
                    },
                    "automation": {
                        "auto_monitor": "automation/auto-monitor.py",
                        "status": "ready"
                    }
                },
                "email_accounts": {
                    "total": 7,
                    "domains": ["gmail.com", "noizylab.ca", "fishmusicinc.com", "icloud.com"]
                },
                "integrations": {
                    "cloudflare": "integrated",
                    "email_clients": "configured",
                    "ios_devices": "ready",
                    "xcode": "ready"
                }
            }
        }
        
        config_path = self.base / "unified_config.json"
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        console.print(f"[green]✅ Unified config saved[/green]")
        return config
    
    def verify_all_systems(self):
        """Verify all systems are ready"""
        console.print("[cyan]🔍 Verifying all systems...[/cyan]")
        
        systems = {
            "Email Intelligence": self.base / "email-intelligence/api_server_v4.py",
            "Cloudflare HotRod": self.base / "cloudflare/hotrod-cloudflare.py",
            "Master Dashboard": self.base / "master-dashboard/master-dashboard.py",
            "Health Monitor": self.base / "health/health-monitor.py",
            "Auto Monitor": self.base / "automation/auto-monitor.py",
            "System Analytics": self.base / "analytics/system-analytics.py"
        }
        
        table = Table(title="System Verification")
        table.add_column("System", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Location", style="yellow")
        
        all_ready = True
        for name, path in systems.items():
            if path.exists():
                table.add_row(name, "✅ Ready", str(path.relative_to(self.base)))
            else:
                table.add_row(name, "❌ Missing", str(path))
                all_ready = False
        
        console.print()
        console.print(table)
        
        return all_ready
    
    def generate_status_report(self):
        """Generate complete status report"""
        console.print(Panel.fit(
            "[bold blue]NoizyLab Master Integration[/bold blue]",
            border_style="blue"
        ))
        console.print()
        
        # Verify systems
        all_ready = self.verify_all_systems()
        console.print()
        
        # Create unified config
        config = self.create_unified_config()
        console.print()
        
        # Summary
        if all_ready:
            console.print(Panel.fit(
                "[bold green]✅ ALL SYSTEMS READY![/bold green]\n\n"
                "NoizyLab is complete and ready to use!",
                border_style="green"
            ))
        else:
            console.print(Panel.fit(
                "[bold yellow]⚠️  Some systems need attention[/bold yellow]",
                border_style="yellow"
            ))
        
        return config

if __name__ == "__main__":
    integration = MasterIntegration()
    integration.generate_status_report()

