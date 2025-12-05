#!/usr/bin/env python3
"""
Email Routing Setup - Configure Email Routing for All Addresses
================================================================
Sets up email routing for Google Account emails via Cloudflare
"""

import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

class EmailRoutingSetup:
    def __init__(self):
        self.base = Path("/Users/m2ultra/NOIZYLAB/email-intelligence")
        self.config_path = self.base / "google_accounts.json"
        self.cloudflare_config = self.base / "cloudflare_config.json"
    
    def setup_routing_rules(self):
        """Setup email routing rules for all addresses"""
        console.print("[cyan]📧 Setting up email routing rules...[/cyan]")
        
        if not self.config_path.exists():
            console.print("[red]❌ Google accounts config not found. Run google-account-manager.py first.[/red]")
            return
        
        with open(self.config_path) as f:
            config = json.load(f)
        
        routing_rules = {
            "noizylab_domain": {
                "domain": "noizylab.ca",
                "addresses": config.get("noizylab_emails", []),
                "catch_all": "help@noizylab.ca",
                "purpose": "NoizyLab business emails"
            },
            "fishmusic_domain": {
                "domain": "fishmusicinc.com",
                "addresses": config.get("fishmusic_emails", []),
                "catch_all": "info@fishmusicinc.com",
                "purpose": "Fish Music Inc business emails"
            },
            "personal": {
                "addresses": [
                    config.get("google_account", {}).get("primary", ""),
                    config.get("google_account", {}).get("recovery", "")
                ],
                "purpose": "Personal email addresses"
            }
        }
        
        # Save routing rules
        routing_path = self.base / "email_routing_rules.json"
        with open(routing_path, 'w') as f:
            json.dump(routing_rules, f, indent=2)
        
        console.print(f"[green]✅ Routing rules saved to {routing_path}[/green]")
        
        # Display routing table
        table = Table(title="Email Routing Configuration")
        table.add_column("Domain/Type", style="cyan")
        table.add_column("Addresses", style="green")
        table.add_column("Catch-All", style="yellow")
        
        for key, rule in routing_rules.items():
            addresses_str = ", ".join(rule.get("addresses", []))[:50]
            catch_all = rule.get("catch_all", "N/A")
            table.add_row(key, addresses_str, catch_all)
        
        console.print()
        console.print(table)
        
        return routing_rules
    
    def generate_cloudflare_routing(self):
        """Generate Cloudflare email routing configuration"""
        console.print("[cyan]☁️  Generating Cloudflare routing config...[/cyan]")
        
        routing_rules = self.setup_routing_rules()
        
        if not routing_rules:
            console.print("[red]❌ Could not generate routing rules[/red]")
            return
        
        cloudflare_config = {
            "email_routing": {
                "enabled": True,
                "domains": [
                    {
                        "domain": "noizylab.ca",
                        "catch_all": "help@noizylab.ca",
                        "addresses": routing_rules["noizylab_domain"]["addresses"]
                    },
                    {
                        "domain": "fishmusicinc.com",
                        "catch_all": "info@fishmusicinc.com",
                        "addresses": routing_rules["fishmusic_domain"]["addresses"]
                    }
                ],
                "worker_endpoint": "https://noizylab-email.your-subdomain.workers.dev"
            }
        }
        
        with open(self.cloudflare_config, 'w') as f:
            json.dump(cloudflare_config, f, indent=2)
        
        console.print(f"[green]✅ Cloudflare config saved[/green]")

if __name__ == "__main__":
    setup = EmailRoutingSetup()
    setup.setup_routing_rules()
    setup.generate_cloudflare_routing()
    console.print()
    console.print("[bold green]✅ Email routing setup complete![/bold green]")

