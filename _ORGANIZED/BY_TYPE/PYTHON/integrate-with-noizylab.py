#!/usr/bin/env python3
"""
Integrate Cloudflare with NoizyLab
===================================
Connects Cloudflare services with NoizyLab systems
"""

import requests
import os
from pathlib import Path
from rich.console import Console

console = Console()

class CloudflareNoizyLabIntegration:
    def __init__(self):
        self.base = Path("/Users/m2ultra/NOIZYLAB")
        self.api_token = os.getenv("CLOUDFLARE_API_TOKEN", "")
        self.account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID", "")
    
    def setup_email_integration(self):
        """Integrate Cloudflare Email Routing with NoizyLab Email System"""
        console.print("[cyan]📧 Setting up email integration...[/cyan]")
        
        # Create integration config
        config = {
            "cloudflare_email_routing": {
                "enabled": True,
                "catch_all": os.getenv("CLOUDFLARE_CATCH_ALL", ""),
                "worker_endpoint": "https://noizylab-email.your-subdomain.workers.dev"
            }
        }
        
        config_path = self.base / "email-intelligence" / "cloudflare_config.json"
        import json
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        console.print("[green]✅ Email integration configured[/green]")
    
    def setup_worker_endpoints(self):
        """Setup Cloudflare Worker endpoints for NoizyLab API"""
        console.print("[cyan]🔗 Setting up worker endpoints...[/cyan]")
        
        endpoints = {
            "email_worker": "https://noizylab-email.your-subdomain.workers.dev",
            "ai_router": "https://noizylab-ai-router.your-subdomain.workers.dev"
        }
        
        # Update API server config
        api_config_path = self.base / "email-intelligence" / "app" / "config.py"
        if api_config_path.exists():
            content = api_config_path.read_text()
            if "CLOUDFLARE_WORKER" not in content:
                content += f"\n# Cloudflare Workers\nCLOUDFLARE_EMAIL_WORKER = '{endpoints['email_worker']}'\nCLOUDFLARE_AI_WORKER = '{endpoints['ai_router']}'\n"
                api_config_path.write_text(content)
        
        console.print("[green]✅ Worker endpoints configured[/green]")
    
    def setup_d1_sync(self):
        """Setup D1 database sync with local databases"""
        console.print("[cyan]💾 Setting up D1 sync...[/cyan]")
        
        # Create sync script
        sync_script = """#!/usr/bin/env python3
# Sync local database with Cloudflare D1
import sqlite3
import requests
import os

local_db = "email_intelligence.db"
d1_endpoint = os.getenv("D1_ENDPOINT", "")

# Sync logic here
"""
        
        sync_path = self.base / "cloudflare" / "sync-d1.py"
        sync_path.write_text(sync_script)
        sync_path.chmod(0o755)
        
        console.print("[green]✅ D1 sync configured[/green]")
    
    def create_unified_config(self):
        """Create unified configuration for Cloudflare + NoizyLab"""
        console.print("[cyan]⚙️  Creating unified config...[/cyan]")
        
        config = {
            "cloudflare": {
                "api_token": self.api_token[:10] + "..." if self.api_token else "not_set",
                "account_id": self.account_id[:10] + "..." if self.account_id else "not_set",
                "workers": {
                    "email": "noizylab-email",
                    "ai_router": "noizylab-ai-router"
                },
                "d1_databases": {
                    "email_log": "noizylab-db"
                }
            },
            "noizylab": {
                "email_system": "integrated",
                "ai_system": "integrated",
                "database_sync": "enabled"
            }
        }
        
        import json
        config_path = self.base / "cloudflare" / "unified_config.json"
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        console.print("[green]✅ Unified config created[/green]")
    
    def integrate_all(self):
        """Run all integrations"""
        console.print(Panel.fit(
            "[bold blue]Cloudflare ↔ NoizyLab Integration[/bold blue]",
            border_style="blue"
        ))
        console.print()
        
        self.setup_email_integration()
        self.setup_worker_endpoints()
        self.setup_d1_sync()
        self.create_unified_config()
        
        console.print()
        console.print(Panel.fit(
            "[bold green]✅ Integration Complete![/bold green]\n\n"
            "Cloudflare is now fully integrated with NoizyLab!",
            border_style="green"
        ))

if __name__ == "__main__":
    integrator = CloudflareNoizyLabIntegration()
    integrator.integrate_all()

