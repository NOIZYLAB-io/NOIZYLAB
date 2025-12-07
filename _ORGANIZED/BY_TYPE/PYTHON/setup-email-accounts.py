#!/usr/bin/env python3
"""
Email Account Setup Wizard - Multi-Provider
============================================
Setup iCloud, Exchange, Google, Yahoo, AOL, or Custom accounts
"""

import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

from src.email_providers import EmailProviderSetup

console = Console()

def main():
    """Main setup wizard"""
    console.clear()
    console.print(Panel.fit(
        "[bold cyan]Email Account Setup Wizard[/bold cyan]\n"
        "[dim]Configure email accounts for NoizyLab[/dim]",
        border_style="cyan"
    ))
    console.print()
    
    # Display providers
    providers = EmailProviderSetup.display_providers()
    console.print()
    
    # Select provider
    try:
        choice = int(Prompt.ask("[bold]Select Provider (1-6)[/bold]", choices=["1", "2", "3", "4", "5", "6"]))
        provider_key = list(EmailProviderSetup.PROVIDERS.keys())[choice - 1]
    except (ValueError, IndexError):
        console.print("[red]❌ Invalid selection[/red]")
        return
    
    # Setup provider
    config = EmailProviderSetup.setup_provider(provider_key)
    if not config:
        return
    
    # Test connection
    test = Confirm.ask("\n[bold]Test connection?[/bold]", default=True)
    if test:
        success = EmailProviderSetup.test_connection(config)
        if not success:
            save_anyway = Confirm.ask("[bold]Save anyway?[/bold]", default=False)
            if not save_anyway:
                console.print("[yellow]Setup cancelled[/yellow]")
                return
    
    # Save to identities
    save = Confirm.ask("\n[bold]Save as email identity?[/bold]", default=True)
    if save:
        identity_key = Prompt.ask("[bold]Identity key[/bold]", default="")
        if not identity_key:
            identity_key = None
        
        EmailProviderSetup.save_to_identities(config, identity_key)
        console.print()
        console.print(Panel.fit(
            "[bold green]✅ Account configured successfully![/bold green]\n\n"
            f"Provider: {config['provider_name']}\n"
            f"Email: {config['email']}\n"
            f"Identity: {identity_key or 'auto-generated'}",
            border_style="green"
        ))
    
    console.print()
    console.print("[dim]You can now use this account in NoizyLab CORE[/dim]")
    console.print("[dim]Launch with: nz[/dim]")

if __name__ == "__main__":
    main()

