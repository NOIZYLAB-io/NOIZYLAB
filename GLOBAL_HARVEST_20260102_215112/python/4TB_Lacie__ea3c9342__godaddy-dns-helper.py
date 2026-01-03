#!/usr/bin/env python3
"""
GoDaddy DNS Helper - SPF Record Setup Assistant
===============================================
Helps you set up SPF records in GoDaddy DNS
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

def show_godaddy_setup():
    """Show GoDaddy-specific setup instructions"""
    
    domain = "noizyfish.com"
    
    console.print(Panel.fit(
        "[bold blue]GoDaddy DNS SPF Setup[/bold blue]\n"
        f"Domain: [green]{domain}[/green]",
        border_style="blue"
    ))
    
    console.print("\n[bold]Step 1: Access GoDaddy DNS[/bold]")
    console.print("   URL: https://dcc.godaddy.com/control/portfolio/noizyfish.com/settings")
    console.print("   Or: GoDaddy → My Products → noizyfish.com → DNS\n")
    
    console.print("[bold]Step 2: Add TXT Record[/bold]")
    
    table = Table(title="SPF Record Details", box=box.ROUNDED)
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Type", "TXT")
    table.add_row("Name/Host", "@ (or leave blank)")
    table.add_row("Value", "v=spf1 include:spf.protection.outlook.com -all")
    table.add_row("TTL", "600 (or default)")
    
    console.print(table)
    
    console.print("\n[bold yellow]⚠️  Important:[/bold yellow]")
    console.print("   • You can only have ONE SPF record")
    console.print("   • If you have an existing SPF, EDIT it (don't add new)")
    console.print("   • Wait 5-15 minutes for DNS propagation")
    
    console.print("\n[bold]Step 3: Verify[/bold]")
    console.print("   Run: [cyan]dig TXT noizyfish.com | grep spf[/cyan]")
    console.print("   Or visit: https://mxtoolbox.com/spf.aspx")
    
    # Show both options
    console.print("\n[bold]SPF Record Options:[/bold]\n")
    
    # Option 1: Microsoft 365 Only
    console.print(Panel(
        "[bold green]✅ Option 1: Microsoft 365 Only (Recommended)[/bold green]\n\n"
        "[white]v=spf1 include:spf.protection.outlook.com -all[/white]\n\n"
        "Use this if you only send from Microsoft 365",
        border_style="green"
    ))
    
    # Option 2: Hybrid
    console.print(Panel(
        "[bold yellow]⚠️  Option 2: Microsoft 365 + GoDaddy (Hybrid)[/bold yellow]\n\n"
        "[white]v=spf1 include:spf.protection.outlook.com include:secureserver.net -all[/white]\n\n"
        "Only use if you actually send from GoDaddy too",
        border_style="yellow"
    ))
    
    console.print("\n[bold cyan]Quick Copy Commands:[/bold cyan]\n")
    console.print("Microsoft 365 Only:")
    console.print(Panel("v=spf1 include:spf.protection.outlook.com -all", style="green"))
    
    console.print("\nHybrid (Microsoft 365 + GoDaddy):")
    console.print(Panel("v=spf1 include:spf.protection.outlook.com include:secureserver.net -all", style="yellow"))
    
    console.print("\n[bold]Verification After Setup:[/bold]")
    console.print("   Wait 5-15 minutes, then run:")
    console.print("   [cyan]dig TXT noizyfish.com | grep spf[/cyan]")
    console.print("\n   Expected output:")
    console.print("   [green]\"v=spf1 include:spf.protection.outlook.com -all\"[/green]")

def generate_dns_export():
    """Generate DNS zone file format for reference"""
    domain = "noizyfish.com"
    
    records = {
        "SPF (Microsoft 365 Only)": {
            "name": "@",
            "type": "TXT",
            "value": "v=spf1 include:spf.protection.outlook.com -all",
            "ttl": 600
        },
        "SPF (Hybrid)": {
            "name": "@",
            "type": "TXT",
            "value": "v=spf1 include:spf.protection.outlook.com include:secureserver.net -all",
            "ttl": 600
        }
    }
    
    console.print("\n[bold]DNS Zone File Format (Reference):[/bold]\n")
    
    for record_name, record in records.items():
        console.print(f"[cyan]{record_name}:[/cyan]")
        console.print(f"  {record['name'] or domain}\t{record['ttl']}\tIN\t{record['type']}\t\"{record['value']}\"")

if __name__ == "__main__":
    show_godaddy_setup()
    generate_dns_export()
    
    console.print("\n[bold green]✅ Ready to add SPF record in GoDaddy![/bold green]")
    console.print("   Follow the steps above to complete setup.\n")

