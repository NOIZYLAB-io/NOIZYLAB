#!/usr/bin/env python3
"""
Cloudflare Email Routing Setup - Automate Email Routing Configuration
=====================================================================
Sets up email routing for noizylab.ca and other domains
"""

import requests
import json
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class CloudflareEmailRouting:
    def __init__(self):
        self.api_token = os.getenv("CLOUDFLARE_API_TOKEN", "")
        self.zone_id = os.getenv("CLOUDFLARE_ZONE_ID", "")
        self.account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID", "")
        self.base_url = "https://api.cloudflare.com/client/v4"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
    
    def enable_email_routing(self, zone_id: str = None) -> dict:
        """Enable Email Routing for a zone"""
        zone = zone_id or self.zone_id
        if not zone:
            return {"error": "Zone ID required"}
        
        try:
            response = requests.post(
                f"{self.base_url}/zones/{zone}/email/routing/enable",
                headers=self.headers,
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json().get("result", {})
            return {"error": response.text}
        except Exception as e:
            return {"error": str(e)}
    
    def get_email_routing_status(self, zone_id: str = None) -> dict:
        """Get Email Routing status"""
        zone = zone_id or self.zone_id
        if not zone:
            return {"error": "Zone ID required"}
        
        try:
            response = requests.get(
                f"{self.base_url}/zones/{zone}/email/routing",
                headers=self.headers,
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json().get("result", {})
            return {}
        except Exception as e:
            return {"error": str(e)}
    
    def create_destination_address(self, zone_id: str, email: str) -> dict:
        """Create destination address"""
        zone = zone_id or self.zone_id
        if not zone:
            return {"error": "Zone ID required"}
        
        try:
            response = requests.post(
                f"{self.base_url}/zones/{zone}/email/routing/addresses",
                headers=self.headers,
                json={"email": email},
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json().get("result", {})
            return {"error": response.text}
        except Exception as e:
            return {"error": str(e)}
    
    def create_routing_rule(self, zone_id: str, rule_name: str, 
                           match: str, action: str) -> dict:
        """Create email routing rule"""
        zone = zone_id or self.zone_id
        if not zone:
            return {"error": "Zone ID required"}
        
        try:
            response = requests.post(
                f"{self.base_url}/zones/{zone}/email/routing/rules",
                headers=self.headers,
                json={
                    "name": rule_name,
                    "enabled": True,
                    "matchers": [{"type": "literal", "field": "to", "value": match}],
                    "actions": [{"type": "forward", "value": [action]}]
                },
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json().get("result", {})
            return {"error": response.text}
        except Exception as e:
            return {"error": str(e)}
    
    def setup_noizylab_routing(self):
        """Setup email routing for noizylab.ca"""
        console.print(Panel.fit(
            "[bold blue]Setting Up Email Routing for noizylab.ca[/bold blue]",
            border_style="blue"
        ))
        console.print()
        
        if not self.zone_id:
            console.print("[red]❌ Zone ID not set. Set CLOUDFLARE_ZONE_ID[/red]")
            return
        
        # Enable Email Routing
        console.print("[cyan]📧 Enabling Email Routing...[/cyan]")
        result = self.enable_email_routing()
        if "error" in result:
            console.print(f"[yellow]⚠️  {result['error']}[/yellow]")
        else:
            console.print("[green]✅ Email Routing enabled[/green]")
        console.print()
        
        # Create destination addresses
        destinations = [
            "rspplowman@gmail.com",  # Primary destination
            "rsp@noizylab.ca",
            "help@noizylab.ca",
            "hello@noizylab.ca"
        ]
        
        console.print("[cyan]📬 Creating destination addresses...[/cyan]")
        for dest in destinations:
            result = self.create_destination_address(self.zone_id, dest)
            if "error" in result:
                console.print(f"  ⚠️  {dest}: {result.get('error', 'Error')}")
            else:
                console.print(f"  ✅ {dest}")
        console.print()
        
        # Create routing rules
        console.print("[cyan]📋 Creating routing rules...[/cyan]")
        
        rules = [
            {
                "name": "rsp@noizylab.ca → rspplowman@gmail.com",
                "match": "rsp@noizylab.ca",
                "action": "rspplowman@gmail.com"
            },
            {
                "name": "help@noizylab.ca → rspplowman@gmail.com",
                "match": "help@noizylab.ca",
                "action": "rspplowman@gmail.com"
            },
            {
                "name": "hello@noizylab.ca → rspplowman@gmail.com",
                "match": "hello@noizylab.ca",
                "action": "rspplowman@gmail.com"
            }
        ]
        
        for rule in rules:
            result = self.create_routing_rule(
                self.zone_id,
                rule["name"],
                rule["match"],
                rule["action"]
            )
            if "error" in result:
                console.print(f"  ⚠️  {rule['name']}: {result.get('error', 'Error')}")
            else:
                console.print(f"  ✅ {rule['name']}")
        console.print()
        
        # Get status
        status = self.get_email_routing_status()
        if status:
            console.print("[green]✅ Email Routing configured![/green]")
            console.print(f"   Status: {status.get('status', 'active')}")
        
        console.print()
        console.print(Panel.fit(
            "[bold green]✅ Email Routing Setup Complete![/bold green]\n\n"
            "View in Cloudflare Dashboard:\n"
            "https://dash.cloudflare.com/1323e14ace0c8d7362612d5b5c0d41bb/noizylab.ca/email/routing/overview",
            border_style="green"
        ))

if __name__ == "__main__":
    routing = CloudflareEmailRouting()
    routing.setup_noizylab_routing()

