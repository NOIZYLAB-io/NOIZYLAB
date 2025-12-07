#!/usr/bin/env python3
"""
HotRod Cloudflare - Advanced Cloudflare Integration for NoizyLab
================================================================
Complete Cloudflare automation, monitoring, and optimization
"""

import requests
import json
import os
from typing import Dict, List, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from datetime import datetime

console = Console()

class HotRodCloudflare:
    def __init__(self):
        self.api_token = os.getenv("CLOUDFLARE_API_TOKEN", "")
        self.account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID", "")
        self.zone_id = os.getenv("CLOUDFLARE_ZONE_ID", "")
        self.base_url = "https://api.cloudflare.com/client/v4"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
    
    def get_zones(self) -> List[Dict]:
        """Get all zones"""
        try:
            response = requests.get(
                f"{self.base_url}/zones",
                headers=self.headers,
                timeout=10
            )
            if response.status_code == 200:
                return response.json().get("result", [])
            return []
        except Exception as e:
            console.print(f"[red]Error getting zones: {e}[/red]")
            return []
    
    def get_workers(self) -> List[Dict]:
        """Get all Workers"""
        if not self.account_id:
            return []
        
        try:
            response = requests.get(
                f"{self.base_url}/accounts/{self.account_id}/workers/scripts",
                headers=self.headers,
                timeout=10
            )
            if response.status_code == 200:
                return response.json().get("result", [])
            return []
        except Exception as e:
            console.print(f"[red]Error getting workers: {e}[/red]")
            return []
    
    def get_d1_databases(self) -> List[Dict]:
        """Get all D1 databases"""
        if not self.account_id:
            return []
        
        try:
            response = requests.get(
                f"{self.base_url}/accounts/{self.account_id}/d1/database",
                headers=self.headers,
                timeout=10
            )
            if response.status_code == 200:
                return response.json().get("result", [])
            return []
        except Exception as e:
            console.print(f"[red]Error getting D1 databases: {e}[/red]")
            return []
    
    def deploy_worker(self, name: str, script: str, bindings: Dict = None) -> Dict:
        """Deploy a Cloudflare Worker"""
        if not self.account_id:
            return {"error": "Account ID not set"}
        
        try:
            # Upload worker
            files = {
                'script': (None, script),
                'metadata': (None, json.dumps({"main_module": "index.js"}))
            }
            
            response = requests.put(
                f"{self.base_url}/accounts/{self.account_id}/workers/scripts/{name}",
                headers={"Authorization": f"Bearer {self.api_token}"},
                files=files,
                timeout=30
            )
            
            if response.status_code == 200:
                return {"status": "success", "worker": name}
            else:
                return {"status": "error", "message": response.text}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def create_d1_database(self, name: str) -> Dict:
        """Create a D1 database"""
        if not self.account_id:
            return {"error": "Account ID not set"}
        
        try:
            response = requests.post(
                f"{self.base_url}/accounts/{self.account_id}/d1/database",
                headers=self.headers,
                json={"name": name},
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json().get("result", {})
            return {"error": response.text}
        except Exception as e:
            return {"error": str(e)}
    
    def setup_email_routing(self, zone_id: str, catch_all: str = None) -> Dict:
        """Setup Cloudflare Email Routing"""
        try:
            # Enable Email Routing
            response = requests.post(
                f"{self.base_url}/zones/{zone_id}/email/routing/enable",
                headers=self.headers,
                timeout=10
            )
            
            if catch_all:
                # Set catch-all address
                response = requests.post(
                    f"{self.base_url}/zones/{zone_id}/email/routing/addresses/catch_all",
                    headers=self.headers,
                    json={"email": catch_all},
                    timeout=10
                )
            
            return {"status": "success"}
        except Exception as e:
            return {"error": str(e)}
    
    def get_analytics(self, zone_id: str, days: int = 7) -> Dict:
        """Get zone analytics"""
        try:
            since = datetime.now().timestamp() - (days * 24 * 60 * 60)
            
            response = requests.get(
                f"{self.base_url}/zones/{zone_id}/analytics/dashboard",
                headers=self.headers,
                params={"since": int(since)},
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json().get("result", {})
            return {}
        except Exception as e:
            return {"error": str(e)}
    
    def optimize_zone(self, zone_id: str) -> Dict:
        """Optimize zone settings"""
        optimizations = {
            "auto_minify": {"html": True, "css": True, "js": True},
            "browser_cache_ttl": 14400,
            "cache_level": "aggressive",
            "development_mode": 0
        }
        
        results = {}
        for setting, value in optimizations.items():
            try:
                response = requests.patch(
                    f"{self.base_url}/zones/{zone_id}/settings/{setting}",
                    headers=self.headers,
                    json={"value": value},
                    timeout=10
                )
                results[setting] = "success" if response.status_code == 200 else "error"
            except:
                results[setting] = "error"
        
        return results
    
    def display_status(self):
        """Display Cloudflare status"""
        console.print(Panel.fit(
            "[bold blue]HotRod Cloudflare - Status[/bold blue]",
            border_style="blue"
        ))
        
        # Zones
        zones = self.get_zones()
        if zones:
            table = Table(title="Cloudflare Zones", box=box.ROUNDED)
            table.add_column("Zone", style="cyan")
            table.add_column("Status", style="green")
            table.add_column("Plan", style="yellow")
            
            for zone in zones[:10]:  # Show first 10
                table.add_row(
                    zone.get("name", ""),
                    zone.get("status", ""),
                    zone.get("plan", {}).get("name", "")
                )
            
            console.print(table)
        
        # Workers
        workers = self.get_workers()
        if workers:
            console.print(f"\n[green]✅ Workers: {len(workers)} deployed[/green]")
        
        # D1 Databases
        d1_dbs = self.get_d1_databases()
        if d1_dbs:
            console.print(f"[green]✅ D1 Databases: {len(d1_dbs)} created[/green]")
        
        # Configuration status
        console.print("\n[bold]Configuration:[/bold]")
        console.print(f"  API Token: {'✅ Set' if self.api_token else '❌ Not set'}")
        console.print(f"  Account ID: {'✅ Set' if self.account_id else '❌ Not set'}")
        console.print(f"  Zone ID: {'✅ Set' if self.zone_id else '❌ Not set'}")

if __name__ == "__main__":
    cf = HotRodCloudflare()
    cf.display_status()

