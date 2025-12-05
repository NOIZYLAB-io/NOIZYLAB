#!/usr/bin/env python3
"""
SPF Record Manager - Email Security Tool
=========================================
Manages SPF, DKIM, DMARC records for email authentication
"""

import re
from typing import Dict, List, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class SPFManager:
    def __init__(self):
        self.spf_pattern = re.compile(r'v=spf1\s+([^\s]+(?:\s+[^\s]+)*)\s+(-|~|\?)?all')
    
    def parse_spf(self, spf_record: str) -> Dict:
        """Parse SPF record into components"""
        spf_record = spf_record.strip()
        
        if not spf_record.startswith('v=spf1'):
            return {"valid": False, "error": "Invalid SPF record format"}
        
        # Extract mechanism
        match = self.spf_pattern.match(spf_record)
        if not match:
            return {"valid": False, "error": "Could not parse SPF record"}
        
        mechanisms = match.group(1).split()
        qualifier = match.group(2) if match.group(2) else "-"
        
        parsed = {
            "valid": True,
            "version": "spf1",
            "mechanisms": [],
            "includes": [],
            "ips": [],
            "all_qualifier": qualifier,
            "raw": spf_record
        }
        
        for mechanism in mechanisms:
            if mechanism.startswith("include:"):
                parsed["includes"].append(mechanism.replace("include:", ""))
            elif mechanism.startswith("ip4:") or mechanism.startswith("ip6:"):
                parsed["ips"].append(mechanism)
            elif mechanism in ["a", "mx", "ptr"]:
                parsed["mechanisms"].append(mechanism)
            elif mechanism.startswith("a:") or mechanism.startswith("mx:"):
                parsed["mechanisms"].append(mechanism)
        
        return parsed
    
    def validate_spf(self, spf_record: str) -> Dict:
        """Validate SPF record"""
        parsed = self.parse_spf(spf_record)
        
        if not parsed["valid"]:
            return parsed
        
        issues = []
        
        # Check length (SPF records should be < 255 chars)
        if len(spf_record) > 255:
            issues.append("SPF record exceeds 255 characters (DNS TXT limit)")
        
        # Check for common issues
        if parsed["all_qualifier"] == "?":
            issues.append("Warning: '?all' allows all (neutral policy)")
        
        if not parsed["includes"] and not parsed["ips"]:
            issues.append("Warning: No includes or IPs specified")
        
        return {
            **parsed,
            "issues": issues,
            "validated": len(issues) == 0
        }
    
    def generate_spf(self, includes: List[str] = None, ips: List[str] = None, 
                    qualifier: str = "-") -> str:
        """Generate SPF record"""
        parts = ["v=spf1"]
        
        if includes:
            for include in includes:
                parts.append(f"include:{include}")
        
        if ips:
            for ip in ips:
                if ":" in ip:
                    parts.append(f"ip6:{ip}")
                else:
                    parts.append(f"ip4:{ip}")
        
        parts.append(f"{qualifier}all")
        
        spf = " ".join(parts)
        
        if len(spf) > 255:
            console.print("[red]Warning: Generated SPF exceeds 255 characters[/red]")
        
        return spf
    
    def display_spf(self, spf_record: str):
        """Display SPF record in formatted table"""
        parsed = self.validate_spf(spf_record)
        
        if not parsed["valid"]:
            console.print(f"[red]Error: {parsed.get('error', 'Invalid SPF')}[/red]")
            return
        
        table = Table(title="SPF Record Analysis")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Version", parsed["version"])
        table.add_row("All Qualifier", parsed["all_qualifier"] + 
                     (" (Strict - Reject all)" if parsed["all_qualifier"] == "-" else
                      " (Soft - Neutral)" if parsed["all_qualifier"] == "~" else
                      " (Neutral)"))
        
        if parsed["includes"]:
            table.add_row("Includes", ", ".join(parsed["includes"]))
        
        if parsed["ips"]:
            table.add_row("IPs", ", ".join(parsed["ips"]))
        
        if parsed["mechanisms"]:
            table.add_row("Mechanisms", ", ".join(parsed["mechanisms"]))
        
        table.add_row("Length", f"{len(spf_record)} chars")
        table.add_row("Valid", "✅ Yes" if parsed["validated"] else "⚠️  Issues found")
        
        console.print(table)
        
        if parsed.get("issues"):
            console.print("\n[yellow]Issues:[/yellow]")
            for issue in parsed["issues"]:
                console.print(f"  ⚠️  {issue}")
        
        console.print(f"\n[bold]Raw SPF Record:[/bold]")
        console.print(Panel(spf_record, style="green"))

def main():
    """Main CLI"""
    manager = SPFManager()
    
    console.print("[bold blue]SPF Record Manager[/bold blue]\n")
    
    # Microsoft 365 (Primary - Recommended)
    spf_m365 = "v=spf1 include:spf.protection.outlook.com -all"
    console.print("[bold green]✅ Microsoft 365 (Primary - Recommended)[/bold green]")
    manager.display_spf(spf_m365)
    
    # Microsoft 365 + GoDaddy (Hybrid - Only if sending from GoDaddy too)
    spf_hybrid = "v=spf1 include:spf.protection.outlook.com include:secureserver.net -all"
    console.print("\n[bold yellow]⚠️  Microsoft 365 + GoDaddy (Hybrid - Only if needed)[/bold yellow]")
    manager.display_spf(spf_hybrid)
    
    # Recommendations
    console.print("\n[bold cyan]Recommendations:[/bold cyan]")
    console.print("  ✅ Use Microsoft 365 only if you only send from Microsoft 365")
    console.print("  ⚠️  Use hybrid version ONLY if you actually send emails from GoDaddy")
    console.print("  📝 Keep it simple - one provider is better than multiple")

if __name__ == "__main__":
    main()

