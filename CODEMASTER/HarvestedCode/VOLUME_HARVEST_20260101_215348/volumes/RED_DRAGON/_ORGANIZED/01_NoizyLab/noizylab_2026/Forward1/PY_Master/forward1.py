import os
import sys
import yaml
import click
import webbrowser
import logging
from datetime import datetime
from rich.console import Console
from rich.table import Table
from cryptography.fernet import Fernet

console = Console()

CONFIG_FILE = "config.yaml"
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "forward1.log")
VAULT_KEY_FILE = "vault.key"
VAULT_FILE = "vault.enc"

# ---------- Utilities ----------

def ensure_paths():
    os.makedirs(LOG_DIR, exist_ok=True)
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "a").close()

def setup_logging():
    ensure_paths()
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

def log_action(msg):
    logging.info(msg)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        console.print("[red]Missing config.yaml[/red]")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)

def get_fernet():
    if not os.path.exists(VAULT_KEY_FILE):
        key = Fernet.generate_key()
        with open(VAULT_KEY_FILE, "wb") as fk:
            fk.write(key)
        console.print("[green]Generated new vault key (vault.key). Keep it safe.[/green]")
    with open(VAULT_KEY_FILE, "rb") as fk:
        key = fk.read()
    return Fernet(key)

def vault_append(text):
    f = get_fernet()
    existing_plain = b""
    if os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, "rb") as vf:
            existing = vf.read()
        try:
            existing_plain = f.decrypt(existing)
        except Exception:
            existing_plain = b""
    new_plain = existing_plain + (f"[{datetime.utcnow().isoformat()}] {text}\n").encode()
    new_enc = f.encrypt(new_plain)
    with open(VAULT_FILE, "wb") as vf:
        vf.write(new_enc)

def vault_read():
    if not os.path.exists(VAULT_FILE):
        console.print("[yellow]Vault is empty.[/yellow]")
        return
    f = get_fernet()
    with open(VAULT_FILE, "rb") as vf:
        data = vf.read()
    try:
        plain = f.decrypt(data).decode()
        console.print(plain)
    except Exception:
        console.print("[red]Vault decryption failed. Ensure vault.key is correct.[/red]")

# ---------- CLI ----------

@click.group()
def cli():
    """Forward1: Account & Domain Consolidation Toolkit"""
    setup_logging()

@cli.command()
def status():
    """Show current configuration summary."""
    cfg = load_config()

    table = Table(title="Identity")
    table.add_column("Key")
    table.add_column("Value")
    table.add_row("Admin Email", cfg["identity"]["admin_email"])
    table.add_row("Business Email", cfg["identity"]["business_email"])
    table.add_row("Brand", cfg["identity"]["brand"])
    table.add_row("Alias", cfg["identity"]["alias"])
    console.print(table)

    dt = Table(title="Domains")
    dt.add_column("Domain")
    dt.add_column("Registrar")
    dt.add_column("Status")
    for d in cfg["domains"]:
        dt.add_row(d["name"], d["registrar"], d["status"])
    console.print(dt)

    mt = Table(title="Mailboxes")
    mt.add_column("Address")
    mt.add_column("Platform")
    mt.add_column("Status")
    for m in cfg["mailboxes"]:
        mt.add_row(m["address"], m["platform"], m["status"])
    console.print(mt)

    at = Table(title="Accounts")
    at.add_column("Name")
    at.add_column("Email")
    at.add_column("2FA")
    for a in cfg["accounts"]:
        at.add_row(a["name"], a["email"], a.get("twofa", "unknown"))
    console.print(at)

    log_action("Status viewed")

@cli.command()
def checklist():
    """Show prioritized action checklist."""
    cfg = load_config()
    console.print("[bold green]Forward1 Checklist[/bold green]\n")

    console.print("[bold]Domains:[/bold]")
    for d in cfg["domains"]:
        console.print(f"- {d['name']} [{d['status']}]")
        for act in d.get("actions", []):
            console.print(f"  • {act}")

    console.print("\n[bold]Mailboxes:[/bold]")
    for m in cfg["mailboxes"]:
        console.print(f"- {m['address']} [{m['status']}]")

    console.print("\n[bold]2FA Targets:[/bold]")
    for a in cfg["accounts"]:
        console.print(f"- {a['name']} ({a['email']}) → {a.get('twofa','unknown')}")

    log_action("Checklist viewed")

@cli.command()
@click.argument("target", type=click.Choice(["godaddy","microsoft","social","webador","all"]))
def open(target):
    """Open admin/security portals in your browser."""
    cfg = load_config()

    def _open(url, label):
        webbrowser.open(url)
        console.print(f"[green]Opened:[/green] {label} → {url}")
        log_action(f"Opened {label}: {url}")

    if target in ("godaddy","all"):
        gd = next((a for a in cfg["accounts"] if a["name"].lower()=="godaddy"), None)
        if gd:
            if gd.get("url_products"):
                _open(gd["url_products"], "GoDaddy Products")
            if gd.get("url_security"):
                _open(gd["url_security"], "GoDaddy Security")

    if target in ("microsoft","all"):
        ms = next((a for a in cfg["accounts"] if a["name"].lower()=="microsoft 365"), None)
        if ms:
            if ms.get("url_admin"):
                _open(ms["url_admin"], "Microsoft 365 Admin")
            if ms.get("url_security"):
                _open(ms["url_security"], "Microsoft Account Security")

    if target in ("webador","all"):
        _open("https://www.webador.com/v2/dashboard", "Webador Dashboard")

    if target in ("social","all"):
        for name in ["Facebook","Instagram","LinkedIn","YouTube","SoundCloud"]:
            acc = next((a for a in cfg["accounts"] if a["name"].lower()==name.lower()), None)
            if acc and acc.get("url_security"):
                _open(acc["url_security"], f"{name} Security")

@cli.group()
def vault():
    """Manage encrypted vault for recovery codes and notes."""
    pass

@vault.command("add")
@click.argument("text", nargs=-1)
def vault_add(text):
    """Add an encrypted note (e.g., recovery codes)."""
    payload = " ".join(text).strip()
    if not payload:
        console.print("[red]Provide text to store.[/red]")
        return
    vault_append(payload)
    console.print("[green]Stored in encrypted vault.[/green]")
    log_action("Vault note added")

@vault.command("read")
def vault_read_cmd():
    """Read encrypted notes."""
    vault_read()
    log_action("Vault read")

# ---------- Stubs for future API integrations ----------

@cli.group()
def integrate():
    """Future integrations (Microsoft Graph, GoDaddy API, etc.)."""
    pass

@integrate.command("microsoft-graph")
def integrate_ms_graph():
    """Stub: integrate with Microsoft Graph to automate mailbox creation."""
    console.print("[yellow]Stub: Microsoft Graph integration placeholder.[/yellow]")
    console.print("- Would create mailboxes (rp, info, rsp, admin) under your tenant.")
    console.print("- Requires Azure app registration + delegated permissions.")
    log_action("Microsoft Graph stub invoked")

@integrate.command("godaddy-api")
def integrate_godaddy():
    """Stub: integrate with GoDaddy API to manage DNS and auto-renew."""
    console.print("[yellow]Stub: GoDaddy API integration placeholder.[/yellow]")
    console.print("- Would set auto-renew, update DNS, and validate transfers.")
    console.print("- Requires GoDaddy API key/secret.")
    log_action("GoDaddy API stub invoked")

if __name__ == "__main__":
    cli()