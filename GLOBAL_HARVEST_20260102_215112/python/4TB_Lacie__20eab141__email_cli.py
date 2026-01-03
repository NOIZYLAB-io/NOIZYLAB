#!/usr/bin/env python3
"""
Email CLI - Complete Email Management Interface
==============================================
"""

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from email_sender import EmailSender
import json

console = Console()
sender = EmailSender()

@click.group()
def cli():
    """NoizyLab Email Management CLI"""
    pass

@cli.command()
@click.option('--smtp-server', prompt='SMTP Server', default='smtp.office365.com')
@click.option('--smtp-port', prompt='SMTP Port', default=587, type=int)
@click.option('--username', prompt='Email Username')
@click.option('--password', prompt='Email Password', hide_input=True)
@click.option('--from-email', prompt='From Email')
@click.option('--from-name', prompt='From Name', default='NoizyLab')
def configure(smtp_server, smtp_port, username, password, from_email, from_name):
    """Configure email settings"""
    sender.configure(smtp_server, smtp_port, username, password, from_email, from_name)
    console.print("[green]✅ Email configuration saved![/green]")

@cli.command()
@click.option('--to', prompt='To Email')
@click.option('--subject', prompt='Subject')
@click.option('--body', prompt='Body')
@click.option('--html', help='HTML body (optional)')
@click.option('--attachment', multiple=True, help='Attachment file paths')
def send(to, subject, body, html, attachment):
    """Send email"""
    result = sender.send_email(to, subject, body, html, list(attachment) if attachment else None)
    
    if result['status'] == 'success':
        console.print(f"[green]✅ Email sent to {to}[/green]")
    else:
        console.print(f"[red]❌ Error: {result['message']}[/red]")

@cli.command()
@click.option('--limit', default=20, help='Number of emails to show')
def history(limit):
    """Show email history"""
    emails = sender.get_email_history(limit)
    
    if not emails:
        console.print("[yellow]No email history[/yellow]")
        return
    
    table = Table(title="Email History")
    table.add_column("ID", style="cyan")
    table.add_column("To", style="green")
    table.add_column("Subject", style="yellow")
    table.add_column("Status", style="magenta")
    table.add_column("Sent At", style="blue")
    
    for email in emails:
        status_icon = "✅" if email['status'] == 'sent' else "❌"
        table.add_row(
            str(email['id']),
            email['to'],
            email['subject'][:50],
            f"{status_icon} {email['status']}",
            email['sent_at']
        )
    
    console.print(table)

@cli.command()
@click.option('--email', prompt='Email Address')
@click.option('--name', prompt='Name', default='')
@click.option('--company', prompt='Company', default='')
@click.option('--tags', help='Tags (comma-separated)')
@click.option('--notes', prompt='Notes', default='')
def add_contact(email, name, company, tags, notes):
    """Add email contact"""
    tag_list = tags.split(',') if tags else None
    sender.add_contact(email, name, company, tag_list, notes)

@cli.command()
def contacts():
    """List all contacts"""
    contacts_list = sender.get_contacts()
    
    if not contacts_list:
        console.print("[yellow]No contacts found[/yellow]")
        return
    
    table = Table(title="Email Contacts")
    table.add_column("ID", style="cyan")
    table.add_column("Email", style="green")
    table.add_column("Name", style="yellow")
    table.add_column("Company", style="blue")
    table.add_column("Tags", style="magenta")
    
    for contact in contacts_list:
        tags_str = ', '.join(contact['tags']) if contact['tags'] else '-'
        table.add_row(
            str(contact['id']),
            contact['email'],
            contact['name'] or '-',
            contact['company'] or '-',
            tags_str
        )
    
    console.print(table)

@cli.command()
def status():
    """Show email system status"""
    config = sender.config
    
    console.print(Panel.fit(
        "[bold blue]Email System Status[/bold blue]\n\n"
        f"SMTP Server: {config.get('smtp_server', 'Not configured')}\n"
        f"From Email: {config.get('from_email', 'Not configured')}\n"
        f"Configured: {'✅ Yes' if config.get('username') else '❌ No'}",
        border_style="blue"
    ))

if __name__ == '__main__':
    cli()

