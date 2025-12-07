#!/usr/bin/env python3
"""
DNS Security Manager - SPF, DKIM, DMARC Management
==================================================
Complete email security record management
"""

import re
import json
from typing import Dict, List
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

class DNSSecurityManager:
    def __init__(self):
        self.records = {
            "spf": [],
            "dkim": [],
            "dmarc": []
        }
    
    def add_spf(self, domain: str, spf_record: str):
        """Add SPF record for domain"""
        self.records["spf"].append({
            "domain": domain,
            "type": "TXT",
            "name": "@",
            "value": spf_record,
            "ttl": 3600
        })
    
    def add_dkim(self, domain: str, selector: str, public_key: str):
        """Add DKIM record for domain"""
        dkim_record = f"v=DKIM1; k=rsa; p={public_key}"
        self.records["dkim"].append({
            "domain": domain,
            "type": "TXT",
            "name": f"{selector}._domainkey",
            "value": dkim_record,
            "ttl": 3600
        })
    
    def add_dmarc(self, domain: str, policy: str = "quarantine", rua: str = None):
        """Add DMARC record for domain"""
        dmarc_parts = [f"v=DMARC1", f"p={policy}"]
        
        if rua:
            dmarc_parts.append(f"rua=mailto:{rua}")
        
        dmarc_record = "; ".join(dmarc_parts)
        
        self.records["dmarc"].append({
            "domain": domain,
            "type": "TXT",
            "name": "_dmarc",
            "value": dmarc_record,
            "ttl": 3600
        })
    
    def generate_outlook_spf(self, domain: str, include_godaddy: bool = False) -> str:
        """Generate Outlook/Microsoft 365 SPF record
        
        Args:
            domain: Domain name (not used but kept for compatibility)
            include_godaddy: If True, include GoDaddy secureserver.net
        """
        if include_godaddy:
            return "v=spf1 include:spf.protection.outlook.com include:secureserver.net -all"
        return "v=spf1 include:spf.protection.outlook.com -all"
    
    def generate_google_spf(self, domain: str) -> str:
        """Generate Google Workspace SPF record"""
        return "v=spf1 include:_spf.google.com ~all"
    
    def generate_combined_spf(self, domain: str, providers: List[str]) -> str:
        """Generate combined SPF for multiple providers"""
        includes = []
        
        if "outlook" in providers or "microsoft" in providers or "office365" in providers:
            includes.append("spf.protection.outlook.com")
        
        if "google" in providers or "gmail" in providers:
            includes.append("_spf.google.com")
        
        if "sendgrid" in providers:
            includes.append("sendgrid.net")
        
        if "mailchimp" in providers:
            includes.append("servers.mcsv.net")
        
        parts = ["v=spf1"]
        for include in includes:
            parts.append(f"include:{include}")
        parts.append("-all")
        
        return " ".join(parts)
    
    def display_records(self, domain: str = None):
        """Display all DNS records"""
        table = Table(title="DNS Security Records", box=box.ROUNDED)
        table.add_column("Type", style="cyan")
        table.add_column("Domain", style="green")
        table.add_column("Name", style="yellow")
        table.add_column("Value", style="white")
        
        for record_type, records in self.records.items():
            for record in records:
                if domain and record["domain"] != domain:
                    continue
                
                value = record["value"]
                if len(value) > 50:
                    value = value[:47] + "..."
                
                table.add_row(
                    record_type.upper(),
                    record["domain"],
                    record["name"],
                    value
                )
        
        console.print(table)
    
    def export_dns(self, format: str = "json") -> str:
        """Export DNS records"""
        if format == "json":
            return json.dumps(self.records, indent=2)
        elif format == "zone":
            # Generate DNS zone file format
            lines = []
            for record_type, records in self.records.items():
                for record in records:
                    name = record["name"]
                    if name == "@":
                        name = record["domain"]
                    else:
                        name = f"{name}.{record['domain']}"
                    
                    lines.append(f"{name}\t{record['ttl']}\tIN\t{record['type']}\t\"{record['value']}\"")
            return "\n".join(lines)
        return ""

def main():
    """Example usage"""
    manager = DNSSecurityManager()
    
    domain = "example.com"
    
    console.print("[bold blue]DNS Security Manager[/bold blue]\n")
    
    # Microsoft 365 Only (Recommended)
    m365_spf = manager.generate_outlook_spf(domain, include_godaddy=False)
    manager.add_spf(domain, m365_spf)
    console.print(f"[green]✅ Added Microsoft 365 SPF (Recommended)[/green]")
    console.print(f"   {m365_spf}")
    
    # Optional: Hybrid version
    console.print("\n[yellow]Optional: Hybrid (Microsoft 365 + GoDaddy)[/yellow]")
    hybrid_spf = manager.generate_outlook_spf(domain, include_godaddy=True)
    console.print(f"   {hybrid_spf}")
    console.print("   ⚠️  Only use if you actually send from GoDaddy")
    
    # Add DMARC
    manager.add_dmarc(domain, policy="quarantine", rua=f"dmarc@{domain}")
    console.print(f"\n[green]✅ Added DMARC for {domain}[/green]")
    
    # Display
    console.print("\n")
    manager.display_records(domain)
    
    # Export
    console.print("\n[bold]JSON Export:[/bold]")
    console.print(Panel(manager.export_dns("json"), style="cyan"))

if __name__ == "__main__":
    main()

