#!/usr/bin/env python3
"""
NoizyLab CORE v3.0 - Ultimate Intelligence Aggregator
=====================================================
CSV Logging, AI Composer, Inbox Scanner, Data Vault
"""

import json
import os
import csv
import base64
import time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.progress import track
from rich.layout import Layout
from rich.markdown import Markdown
from rich.align import Align
from rich.live import Live

try:
    from googleapiclient.errors import HttpError
    from googleapiclient.discovery import build
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    GMAIL_AVAILABLE = True
except ImportError:
    GMAIL_AVAILABLE = False
    Request = None

# Update imports to work from core/ directory
import sys
from pathlib import Path
_parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(_parent_dir))

from src.mailer import NoizyMailer
try:
    from src.email_scheduler import EmailScheduler
    from src.bulk_operations import BulkEmailSender
    from src.enhanced_ui import EnhancedUI
    UPGRADE_FEATURES_AVAILABLE = True
except ImportError:
    UPGRADE_FEATURES_AVAILABLE = False
    EmailScheduler = None
    BulkEmailSender = None
    EnhancedUI = None

# --- INITIALIZATION ---
console = Console()
mailer = NoizyMailer()

# Gmail API Setup (optional)
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
GMAIL_SERVICE = None

def init_gmail_service():
    """Initialize Gmail API service"""
    global GMAIL_SERVICE
    
    if not GMAIL_AVAILABLE:
        return None
    
    try:
        # Get parent directory path
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        creds_file = os.path.join(parent_dir, 'config', 'security', 'gmail_credentials.json')
        token_file = os.path.join(parent_dir, 'config', 'security', 'gmail_token.json')
        
        creds = None
        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(creds_file):
                    return None
                flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
                creds = flow.run_local_server(port=0)
            
            with open(token_file, 'w') as token:
                token.write(creds.to_json())
        
        GMAIL_SERVICE = build('gmail', 'v1', credentials=creds)
        return GMAIL_SERVICE
    except Exception as e:
        console.print(f"[yellow]⚠️  Gmail API not configured: {e}[/yellow]")
        return None

# --- MODULE 1: THE DATA VAULT (CSV LOGGING) ---
# Get parent directory path for data files
_parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(_parent_dir, 'data', 'email_database.csv')

def log_to_vault(identity, recipient, subject, status):
    """Log email to CSV database"""
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, 'a', newline='') as csvfile:
        fieldnames = ['Timestamp', 'Identity', 'Recipient', 'Subject', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'Identity': identity,
            'Recipient': recipient,
            'Subject': subject,
            'Status': status
        })

def view_vault():
    """View all entries in the vault"""
    if not os.path.isfile(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as f:
        return list(csv.DictReader(f))

# --- MODULE 2: THE AI COMPOSER (Logic Engine) ---
def ai_generate_draft(keywords, tone):
    """
    Simulates an LLM by expanding keywords into professional text.
    Future upgrade: Connect this function to OpenAI API.
    """
    # Simple logic expansion for now
    intro = "I hope you are having a productive week."
    if tone == "Urgent":
        intro = "I am writing to you with some urgency regarding the following."
    elif tone == "Casual":
        intro = "Hope you're doing well!"

    body = f"{intro}\n\nRegarding: {keywords}."
    
    closer = "I look forward to your thoughts."
    if "invoice" in keywords.lower():
        closer = "Please process this at your earliest convenience."
    elif "meeting" in keywords.lower():
        closer = "Let me know what time works for you."
    elif "follow" in keywords.lower() or "follow-up" in keywords.lower():
        closer = "Looking forward to hearing from you soon."

    return body + "\n\n" + closer

# --- MODULE 3: THE INBOX INTELLIGENCE ---
def fetch_recent_emails(service, limit=5):
    """Fetch recent emails from Gmail"""
    if not service:
        return []
    
    try:
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=limit).execute()
        messages = results.get('messages', [])
        email_data = []
        
        if not messages:
            return []

        for msg in track(messages, description="[cyan]Scanning Inbox...[/cyan]"):
            txt = service.users().messages().get(userId='me', id=msg['id']).execute()
            payload = txt['payload']
            headers = payload['headers']
            
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "(No Subject)")
            sender = next((h['value'] for h in headers if h['name'] == 'From'), "(Unknown)")
            snippet = txt.get('snippet', '')
            
            email_data.append({"from": sender, "subject": subject, "snippet": snippet})
            
        return email_data
    except Exception as e:
        console.print(f"[yellow]⚠️  Error fetching emails: {e}[/yellow]")
        return []

# --- MODULE 4: UI SCREENS ---
def header():
    """Display header"""
    console.clear()
    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    grid.add_row("[bold color(39)]NOIZYLAB[/bold color(39)] [bold white]CORE v3.0[/bold white]")
    grid.add_row("[dim]Intelligence Aggregator | Connected via Google Workspace[/dim]")
    console.print(Panel(grid, style="bold color(39)"))

def dashboard_home():
    """Display main dashboard"""
    header()
    
    # Stats Panel
    vault = view_vault()
    sent_count = len(vault)
    last_sent = vault[-1]['Timestamp'] if vault else "Never"
    
    stats = Table.grid(expand=True)
    stats.add_column(justify="center", ratio=1)
    stats.add_column(justify="center", ratio=1)
    stats.add_row(f"[bold green]{sent_count}[/bold green]", f"[bold yellow]{last_sent}[/bold yellow]")
    stats.add_row("Total Sent", "Last Activity")
    
    console.print(Panel(stats, title="System Status", border_style="green"))
    
    console.print("\n[bold white]SELECT MODULE:[/bold white]")
    console.print("[1] 📤 [bold cyan]Smart Composer[/bold cyan] (Send Mail)")
    console.print("[2] 📥 [bold magenta]Inbox Scanner[/bold magenta] (Read Mail)")
    console.print("[3] 💾 [bold yellow]Data Vault[/bold yellow] (View History)")
    console.print("[4] 👤 [bold white]Identity Config[/bold white]")
    console.print("[5] 📅 [bold green]Email Scheduler[/bold green] (Schedule Emails)")
    console.print("[6] 📨 [bold blue]Bulk Operations[/bold blue] (Send to Many)")
    console.print("[Q] 🛑 Shutdown")

# --- MAIN LOGIC ---
def run_composer():
    """Run Smart Composer"""
    header()
    console.print("[bold cyan]--- SMART COMPOSER ---[/bold cyan]")
    
    # Identity
    ids = list(mailer.config['identities'].keys())
    if not ids:
        console.print("[red]❌ No identities configured. Run Configuration Wizard first![/red]")
        Prompt.ask("\n[dim]Press Enter to return[/dim]")
        return
    
    for i, key in enumerate(ids):
        identity = mailer.config['identities'][key]
        console.print(f"[{i+1}] {key} ({identity.get('email', '')})")
    
    try:
        id_idx = IntPrompt.ask("\n[bold]Select Sender Identity[/bold]", choices=[str(i+1) for i in range(len(ids))])
        sender_key = ids[id_idx-1]
    except:
        return
    
    # Recipient
    to_email = Prompt.ask("\n[bold]Recipient Email[/bold]")
    
    # Mode
    console.print("\n[bold]Drafting Mode:[/bold]")
    console.print("[1] Manual Write")
    console.print("[2] AI Auto-Draft (Keyword Expansion)")
    mode = Prompt.ask("Select Mode", choices=["1", "2"], default="1")
    
    subj = ""
    body = ""
    
    if mode == "1":
        subj = Prompt.ask("\n[bold]Subject[/bold]")
        body = Prompt.ask("[bold]Body[/bold]", multiline=True)
    else:
        subj = Prompt.ask("\n[bold]Subject[/bold]")
        keywords = Prompt.ask("[bold]Enter Keywords[/bold] (e.g. 'meeting, tuesday, starbucks')")
        tone = Prompt.ask("[bold]Tone[/bold]", choices=["Professional", "Casual", "Urgent"], default="Professional")
        with console.status("[bold green]Generating text...[/bold green]"):
            time.sleep(1.5)  # Simulate thinking
            body = ai_generate_draft(keywords, tone)
            console.print(f"[green]✅ Draft generated![/green]")
    
    # Review
    identity = mailer.config['identities'][sender_key]
    console.print()
    console.print(Panel(
        f"[dim]From: {identity.get('email', sender_key)}[/dim]\n\n[bold]Subject:[/bold] {subj}\n\n{body}",
        title="📧 DRAFT PREVIEW",
        border_style="yellow"
    ))
    
    if Prompt.ask("\n[bold]🚀 Execute Send?[/bold]", choices=["y", "n"]) == "y":
        with console.status("[bold green]Sending email...[/bold green]"):
            success = mailer.send_email(sender_key, to_email, subj, body)
        
        if success:
            log_to_vault(sender_key, to_email, subj, "SENT")
            console.print("[bold green]✅ Transmission Complete.[/bold green]")
        else:
            log_to_vault(sender_key, to_email, subj, "FAILED")
            console.print("[bold red]❌ Transmission Failed.[/bold red]")
        
        time.sleep(2)

def run_inbox():
    """Run Inbox Scanner"""
    header()
    
    if not GMAIL_AVAILABLE:
        console.print("[yellow]⚠️  Gmail API not available. Install: pip install google-api-python-client[/yellow]")
        Prompt.ask("\n[dim]Press Enter to return[/dim]")
        return
    
    service = init_gmail_service()
    if not service:
        console.print("[yellow]⚠️  Gmail API not configured.[/yellow]")
        console.print()
        console.print("[bold]To enable Inbox Scanner:[/bold]")
        console.print("1. Run setup helper: [cyan]bash setup-gmail-api.sh[/cyan]")
        console.print("2. Or see: [cyan]GMAIL_API_SETUP.md[/cyan]")
        console.print()
        console.print("[dim]Quick steps:[/dim]")
        console.print("  • Get credentials from Google Cloud Console")
        console.print("  • Save as: config/gmail_credentials.json")
        console.print("  • Run Inbox Scanner again to authenticate")
        console.print()
        console.print("[dim]Note: Smart Composer and Data Vault work without Gmail API[/dim]")
        Prompt.ask("\n[dim]Press Enter to return[/dim]")
        return
    
    emails = fetch_recent_emails(service, limit=5)
    
    if not emails:
        console.print("[yellow]No emails found or inbox is empty.[/yellow]")
    else:
        table = Table(title="📥 Recent Incoming Intelligence", show_lines=True, header_style="bold magenta")
        table.add_column("Sender", style="cyan", no_wrap=True)
        table.add_column("Subject", style="white")
        table.add_column("Snippet", style="dim white")
        
        for e in emails:
            # Clean up sender name
            sender_clean = e['from'].split('<')[0].strip().replace('"', '')
            table.add_row(sender_clean, e['subject'], e['snippet'][:50]+"...")
        
        console.print(table)
    
    Prompt.ask("\n[dim]Press Enter to return to Dashboard[/dim]")

def run_vault():
    """Run Data Vault"""
    header()
    data = view_vault()
    if not data:
        console.print("[yellow]Vault Empty. No emails sent yet.[/yellow]")
    else:
        table = Table(title="💾 Encrypted Transmission Logs", header_style="bold magenta")
        table.add_column("Time", style="dim", width=16)
        table.add_column("Identity", style="cyan")
        table.add_column("To", style="magenta")
        table.add_column("Subject", style="white")
        table.add_column("Status", style="green")
        
        for row in data[-20:]:  # Show last 20
            status_style = "green" if row['Status'] == "SENT" else "red"
            table.add_row(
                row['Timestamp'],
                row['Identity'],
                row['Recipient'],
                row['Subject'][:40],
                f"[{status_style}]{row['Status']}[/{status_style}]"
            )
        console.print(table)
    
    Prompt.ask("\n[dim]Press Enter to return[/dim]")

# --- APP LOOP ---
if __name__ == "__main__":
    # Initialize upgrade features
    scheduler = None
    bulk_sender = None
    ui = None
    
    if UPGRADE_FEATURES_AVAILABLE:
        try:
            scheduler = EmailScheduler()
            bulk_sender = BulkEmailSender(mailer)
            ui = EnhancedUI()
        except Exception as e:
            console.print(f"[yellow]⚠️  Some upgrade features unavailable: {e}[/yellow]")
    
    # Initialize Gmail service on startup (optional)
    if GMAIL_AVAILABLE:
        init_gmail_service()
    
    while True:
        dashboard_home()
        cmd = Prompt.ask("\n[bold]Command[/bold]", choices=["1", "2", "3", "4", "5", "6", "q", "Q"], default="1")
        
        if cmd.lower() == 'q':
            console.clear()
            console.print("[bold red]CORE OFFLINE.[/bold red]")
            break
        elif cmd == '1':
            run_composer()
        elif cmd == '2':
            run_inbox()
        elif cmd == '3':
            run_vault()
        elif cmd == '4':
            header()
            console.print("[bold]Identity Configuration[/bold]")
            console.print()
            console.print("[1] Setup New Email Account")
            console.print("[2] View Current Identities")
            console.print("[3] Back to Dashboard")
            console.print()
            
            sub_cmd = Prompt.ask("[bold]Select[/bold]", choices=["1", "2", "3"], default="3")
            
            if sub_cmd == "1":
                console.print()
                console.print("[dim]Launching Email Account Setup...[/dim]")
                time.sleep(1)
                import subprocess
                import sys
                import os
                script_path = os.path.join(_parent_dir, "scripts", "setup-email-accounts.py")
                subprocess.run([sys.executable, script_path])
            elif sub_cmd == "2":
                console.print()
                ids = list(mailer.config.get('identities', {}).keys())
                if ids:
                    table = Table(title="Configured Identities", show_header=True, header_style="bold magenta")
                    table.add_column("Key", style="cyan")
                    table.add_column("Name", style="green")
                    table.add_column("Email", style="yellow")
                    table.add_column("Provider", style="dim")
                    
                    for key in ids:
                        identity = mailer.config['identities'][key]
                        provider = identity.get('provider_name', 'N/A')
                        table.add_row(key, identity.get('name', ''), identity.get('email', ''), provider)
                    
                    console.print(table)
                else:
                    console.print("[yellow]No identities configured yet.[/yellow]")
                    console.print("[dim]Run option 1 to set up an account.[/dim]")
                
                Prompt.ask("\n[dim]Press Enter to return[/dim]")
        
        elif cmd == '5':  # Email Scheduler
            if scheduler is None:
                console.print("[red]❌ Email Scheduler not available[/red]")
                Prompt.ask("\n[dim]Press Enter to return[/dim]")
                continue
            header()
            console.print("[bold green]--- EMAIL SCHEDULER ---[/bold green]")
            console.print()
            console.print("[1] Schedule Email")
            console.print("[2] View Scheduled")
            console.print("[3] Cancel Scheduled")
            console.print("[4] Back to Dashboard")
            
            sub_cmd = Prompt.ask("\n[bold]Select[/bold]", choices=["1", "2", "3", "4"], default="4")
            
            if sub_cmd == "1":
                # Schedule email
                ids = list(bot.config['identities'].keys())
                if not ids:
                    console.print("[red]❌ No identities configured[/red]")
                    Prompt.ask("\n[dim]Press Enter to return[/dim]")
                    continue
                
                for i, key in enumerate(ids, 1):
                    identity = bot.config['identities'][key]
                    console.print(f"[{i}] {key} ({identity.get('email', '')})")
                
                try:
                    id_idx = int(Prompt.ask("\n[bold]Select Identity[/bold]")) - 1
                    identity_key = ids[id_idx]
                except:
                    continue
                
                to_email = Prompt.ask("[bold]Recipient[/bold]")
                subject = Prompt.ask("[bold]Subject[/bold]")
                body = Prompt.ask("[bold]Body[/bold]", multiline=True)
                
                # Get schedule time
                date_str = Prompt.ask("[bold]Send Date (YYYY-MM-DD)[/bold]", default=datetime.now().strftime("%Y-%m-%d"))
                time_str = Prompt.ask("[bold]Send Time (HH:MM)[/bold]", default="12:00")
                
                try:
                    send_at = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
                    scheduler.schedule_email(identity_key, to_email, subject, body, send_at)
                except Exception as e:
                    console.print(f"[red]❌ Error: {e}[/red]")
                
                Prompt.ask("\n[dim]Press Enter to return[/dim]")
            
            elif sub_cmd == "2":
                scheduler.display_scheduled()
                Prompt.ask("\n[dim]Press Enter to return[/dim]")
            
            elif sub_cmd == "3":
                scheduled = scheduler.list_scheduled()
                if scheduled:
                    scheduler.display_scheduled()
                    schedule_id = Prompt.ask("\n[bold]Schedule ID to cancel[/bold]")
                    scheduler.cancel_scheduled(schedule_id)
                else:
                    console.print("[yellow]No scheduled emails[/yellow]")
                Prompt.ask("\n[dim]Press Enter to return[/dim]")
        
        elif cmd == '6':  # Bulk Operations
            if bulk_sender is None:
                console.print("[red]❌ Bulk Operations not available[/red]")
                Prompt.ask("\n[dim]Press Enter to return[/dim]")
                continue
            header()
            console.print("[bold blue]--- BULK EMAIL OPERATIONS ---[/bold blue]")
            console.print()
            
            ids = list(bot.config['identities'].keys())
            if not ids:
                console.print("[red]❌ No identities configured[/red]")
                Prompt.ask("\n[dim]Press Enter to return[/dim]")
                continue
            
            for i, key in enumerate(ids, 1):
                identity = bot.config['identities'][key]
                console.print(f"[{i}] {key} ({identity.get('email', '')})")
            
            try:
                id_idx = int(Prompt.ask("\n[bold]Select Identity[/bold]")) - 1
                identity_key = ids[id_idx]
            except:
                continue
            
            console.print("\n[bold]Enter recipient emails (one per line, empty line to finish):[/bold]")
            recipients = []
            while True:
                email = Prompt.ask("[bold]Email[/bold]", default="")
                if not email:
                    break
                recipients.append(email)
            
            if not recipients:
                console.print("[yellow]No recipients entered[/yellow]")
                Prompt.ask("\n[dim]Press Enter to return[/dim]")
                continue
            
            subject = Prompt.ask("[bold]Subject[/bold]")
            body = Prompt.ask("[bold]Body[/bold]", multiline=True)
            personalize = Confirm.ask("[bold]Personalize emails?[/bold] (use {name} and {email} in body)", default=False)
            delay = float(Prompt.ask("[bold]Delay between sends (seconds)[/bold]", default="1.0"))
            
            confirm = Confirm.ask(f"\n[bold]Send to {len(recipients)} recipients?[/bold]", default=False)
            if confirm:
                results = bulk_sender.send_bulk(identity_key, recipients, subject, body, personalize, delay)
                console.print()
                bulk_sender.display_results(results)
            
            Prompt.ask("\n[dim]Press Enter to return[/dim]")
