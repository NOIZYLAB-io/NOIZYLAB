#!/usr/bin/env python3
"""
Forward1: All-in-one Consolidation Toolkit
- Central config
- CLI control panel
- Encrypted vault for recovery codes
- Browser openers for admin/security portals
- Optional stubs for API automation (GoDaddy, Microsoft Graph)

Usage:
  pip install click rich pyyaml cryptography
  python forward1_all_in_one.py help
"""

import os
import sys
import json
import yaml
import click
import webbrowser
import logging
import getpass
from datetime import datetime
from typing import List, Dict, Any, Optional

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from cryptography.fernet import Fernet

console = Console()

# -----------------------------
# Embedded default configuration
# -----------------------------
DEFAULT_CONFIG_YAML = """
identity:
  admin_email: "rsplowman@icloud.com"
  business_email: "rp@fishmusicinc.com"
  brand: "Fish Music Inc."
  alias: "R.S Plowman"

domains:
  - name: "fishmusicinc.com"
    registrar: "GoDaddy"
    status: "live"
    actions:
      - "Activate Microsoft 365 mailbox rp@fishmusicinc.com"
      - "Enable auto-renew"
  - name: "noizy.ai"
    registrar: "GoDaddy"
    status: "to_register"
    actions:
      - "Register for 2 years + domain privacy + auto-renew"
      - "Create admin@noizy.ai mailbox after registration"
  - name: "noizyfish.com"
    registrar: "Webador"
    status: "transfer_pending"
    actions:
      - "Unlock at Webador + request EPP/Auth code"
      - "Initiate transfer to GoDaddy"

mailboxes:
  - address: "rp@fishmusicinc.com"
    platform: "Microsoft 365"
    status: "pending_activation"
  - address: "info@fishmusicinc.com"
    platform: "Microsoft 365"
    status: "to_create"
  - address: "rsp@noizyfish.com"
    platform: "Microsoft 365"
    status: "to_create_after_transfer"
  - address: "admin@noizy.ai"
    platform: "Microsoft 365"
    status: "to_create_after_registration"

accounts:
  - name: "GoDaddy"
    email: "rp@fishmusicinc.com"
    url_products: "https://account.godaddy.com/products"
    url_security: "https://account.godaddy.com/security"
    twofa: "pending"
  - name: "Microsoft 365"
    email: "rsplowman@icloud.com"
    url_admin: "https://admin.microsoft.com/"
    url_security: "https://account.microsoft.com/security"
    twofa: "enabled"
  - name: "Facebook"
    email: "rp@fishmusicinc.com"
    url_security: "https://www.facebook.com/settings?tab=security"
    twofa: "pending"
  - name: "Instagram"
    email: "rp@fishmusicinc.com"
    url_security: "https://help.instagram.com/566810106808145"
    twofa: "pending"
  - name: "LinkedIn"
    email: "rsplowman@icloud.com"
    url_security: "https://www.linkedin.com/psettings/security"
    twofa: "pending"
  - name: "YouTube"
    email: "rp@fishmusicinc.com"
    url_security: "https://myaccount.google.com/security"
    twofa: "pending"
  - name: "SoundCloud"
    email: "rp@fishmusicinc.com"
    url_security: "https://soundcloud.com/settings/password"
    twofa: "pending"

settings:
  backup_vault: true
  open_in_browser: true
  log_actions: true
"""

# -----------------------------
# File paths
# -----------------------------
CONFIG_FILE = "config.yaml"
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "forward1.log")
VAULT_KEY_FILE = "vault.key"
VAULT_FILE = "vault.enc"

# -----------------------------
# Setup + utilities
# -----------------------------
def ensure_paths():
    os.makedirs(LOG_DIR, exist_ok=True)
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "a").close()
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            f.write(DEFAULT_CONFIG_YAML)
        console.print("[green]Wrote default config.yaml[/green]")

def setup_logging():
    ensure_paths()
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

def log_action(msg: str):
    logging.info(msg)

def load_config() -> Dict[str, Any]:
    ensure_paths()
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)

def save_config(cfg: Dict[str, Any]):
    with open(CONFIG_FILE, "w") as f:
        yaml.safe_dump(cfg, f, sort_keys=False)

def get_fernet() -> Fernet:
    if not os.path.exists(VAULT_KEY_FILE):
        key = Fernet.generate_key()
        with open(VAULT_KEY_FILE, "wb") as fk:
            fk.write(key)
        console.print("[green]Generated new vault key (vault.key). Keep it safe and backed up.[/green]")
    with open(VAULT_KEY_FILE, "rb") as fk:
        key = fk.read()
    return Fernet(key)

def vault_append(text: str):
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

def vault_read_text() -> Optional[str]:
    if not os.path.exists(VAULT_FILE):
        return None
    f = get_fernet()
    with open(VAULT_FILE, "rb") as vf:
        data = vf.read()
    try:
        return f.decrypt(data).decode()
    except Exception:
        return None

def open_url(label: str, url: str):
    webbrowser.open(url)
    console.print(f"[green]Opened:[/green] {label} → {url}")
    log_action(f"Opened {label}: {url}")

# -----------------------------
# CLI
# -----------------------------
@click.group()
def cli():
    """Forward1: All-in-one Consolidation Toolkit"""
    setup_logging()

# -------- Status & Checklist --------
@cli.command()
def status():
    """Show current configuration summary."""
    cfg = load_config()

    console.print(Panel.fit("Identity", style="bold cyan"))
    table = Table()
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

# -------- Open Admin/Security Portals --------
@cli.command()
@click.argument("target", type=click.Choice(["godaddy","microsoft","social","webador","all"]))
def open(target):
    """Open admin/security portals in your browser."""
    cfg = load_config()

    if target in ("godaddy","all"):
        gd = next((a for a in cfg["accounts"] if a["name"].lower()=="godaddy"), None)
        if gd:
            if gd.get("url_products"): open_url("GoDaddy Products", gd["url_products"])
            if gd.get("url_security"): open_url("GoDaddy Security", gd["url_security"])

    if target in ("microsoft","all"):
        ms = next((a for a in cfg["accounts"] if a["name"].lower()=="microsoft 365"), None)
        if ms:
            if ms.get("url_admin"): open_url("Microsoft 365 Admin", ms["url_admin"])
            if ms.get("url_security"): open_url("Microsoft Account Security", ms["url_security"])

    if target in ("webador","all"):
        open_url("Webador Dashboard", "https://www.webador.com/v2/dashboard")

    if target in ("social","all"):
        for name in ["Facebook","Instagram","LinkedIn","YouTube","SoundCloud"]:
            acc = next((a for a in cfg["accounts"] if a["name"].lower()==name.lower()), None)
            if acc and acc.get("url_security"):
                open_url(f"{name} Security", acc["url_security"])

# -------- Vault management --------
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
    txt = vault_read_text()
    if txt is None:
        console.print("[yellow]Vault is empty or key mismatch.[/yellow]")
    else:
        console.print(Panel.fit(txt, title="Vault contents", subtitle="Keep vault.key safe", border_style="green"))
    log_action("Vault read")

# -------- Config updates (quick toggles) --------
@cli.group()
def cfg():
    """Quick config updates."""
    pass

@cfg.command("set-domain-status")
@click.argument("domain")
@click.argument("status")
def cfg_set_domain_status(domain: str, status: str):
    """Set domain status (e.g., noizy.ai registered)."""
    cfg = load_config()
    found = False
    for d in cfg["domains"]:
        if d["name"].lower() == domain.lower():
            d["status"] = status
            found = True
    if found:
        save_config(cfg)
        console.print(f"[green]Updated {domain} → {status}[/green]")
        log_action(f"Domain status updated: {domain} -> {status}")
    else:
        console.print(f"[red]Domain not found: {domain}[/red]")

@cfg.command("set-mailbox-status")
@click.argument("address")
@click.argument("status")
def cfg_set_mailbox_status(address: str, status: str):
    """Set mailbox status (e.g., rp@fishmusicinc.com active)."""
    cfg = load_config()
    found = False
    for m in cfg["mailboxes"]:
        if m["address"].lower() == address.lower():
            m["status"] = status
            found = True
    if found:
        save_config(cfg)
        console.print(f"[green]Updated {address} → {status}[/green]")
        log_action(f"Mailbox status updated: {address} -> {status}")
    else:
        console.print(f"[red]Mailbox not found: {address}[/red]")

@cfg.command("set-2fa")
@click.argument("name")
@click.argument("status")
def cfg_set_2fa(name: str, status: str):
    """Set 2FA status (e.g., GoDaddy enabled)."""
    cfg = load_config()
    found = False
    for a in cfg["accounts"]:
        if a["name"].lower() == name.lower():
            a["twofa"] = status
            found = True
    if found:
        save_config(cfg)
        console.print(f"[green]Updated 2FA {name} → {status}[/green]")
        log_action(f"2FA status updated: {name} -> {status}")
    else:
        console.print(f"[red]Account not found: {name}[/red]")

# -------- Guided flows --------
@cli.group()
def flow():
    """Guided flows to move you forward quickly."""
    pass

@flow.command("register-noizy-ai")
def flow_register_noizy_ai():
    """Guide: register noizy.ai and lock it down."""
    cfg = load_config()
    open_url("GoDaddy Products", "https://account.godaddy.com/products")
    console.print("- Search for 'noizy.ai' → add to cart")
    console.print("- Choose 2-year term, enable auto-renew + domain privacy")
    console.print("- Complete checkout")
    if Confirm.ask("After completing purchase, mark noizy.ai as registered?"):
        # Update config
        for d in cfg["domains"]:
            if d["name"] == "noizy.ai":
                d["status"] = "registered"
        save_config(cfg)
        console.print("[green]Marked noizy.ai as registered[/green]")
        log_action("noizy.ai registered (marked)")
        if Confirm.ask("Open Microsoft 365 Admin to set up admin@noizy.ai mailbox?"):
            open_url("Microsoft 365 Admin", "https://admin.microsoft.com/")
            console.print("- Create mailbox admin@noizy.ai when domain is verified.")
    else:
        console.print("[yellow]Left status unchanged.[/yellow]")

@flow.command("transfer-noizyfish")
def flow_transfer_noizyfish():
    """Guide: transfer noizyfish.com from Webador to GoDaddy."""
    open_url("Webador Dashboard", "https://www.webador.com/v2/dashboard")
    console.print("- Unlock noizyfish.com and request EPP/Auth code.")
    console.print("- Copy the EPP code to your clipboard.")
    open_url("GoDaddy Domain Transfers", "https://account.godaddy.com/domains/transfer")
    console.print("- Paste EPP code at GoDaddy → complete transfer checkout.")
    if Confirm.ask("Mark noizyfish.com as 'transfer_in_progress'?"):
        cfg = load_config()
        for d in cfg["domains"]:
            if d["name"] == "noizyfish.com":
                d["status"] = "transfer_in_progress"
        save_config(cfg)
        console.print("[green]Status updated: transfer_in_progress[/green]")
        log_action("noizyfish.com transfer_in_progress")

@flow.command("activate-m365")
def flow_activate_m365():
    """Guide: activate Microsoft 365 mailboxes (rp, info, rsp, admin)."""
    open_url("Microsoft 365 Admin", "https://admin.microsoft.com/")
    console.print("- Verify domains (fishmusicinc.com, noizy.ai once registered).")
    console.print("- Create mailboxes: rp@, info@, rsp@ (after transfer), admin@ (after registration).")
    if Confirm.ask("Mark rp@fishmusicinc.com as active?"):
        cfg = load_config()
        for m in cfg["mailboxes"]:
            if m["address"] == "rp@fishmusicinc.com":
                m["status"] = "active"
        save_config(cfg)
        console.print("[green]rp@fishmusicinc.com → active[/green]")
        log_action("rp@fishmusicinc.com active")

@flow.command("enable-2fa")
def flow_enable_2fa():
    """Guide: enable 2FA across all accounts with Microsoft Authenticator."""
    cfg = load_config()
    console.print(Panel.fit("Use Microsoft Authenticator on your phone. Sign in with rsplowman@icloud.com and enable cloud backup.", border_style="cyan"))
    # Microsoft
    open_url("Microsoft Account Security", "https://account.microsoft.com/security")
    console.print("- Enable 2FA → scan with Microsoft Authenticator.")
    # GoDaddy
    open_url("GoDaddy Security", "https://account.godaddy.com/security")
    console.print("- Enable 2FA → scan with Authenticator.")
    # Socials
    for acc in cfg["accounts"]:
        nm = acc["name"].lower()
        if nm in ["facebook","instagram","linkedin","youtube","soundcloud"] and acc.get("url_security"):
            open_url(f"{acc['name']} Security", acc["url_security"])
            console.print(f"- Enable 2FA in {acc['name']} → scan with Authenticator.")
    if Confirm.ask("Mark 2FA as enabled for Microsoft 365 and GoDaddy?"):
        for a in cfg["accounts"]:
            if a["name"] in ["Microsoft 365", "GoDaddy"]:
                a["twofa"] = "enabled"
        save_config(cfg)
        console.print("[green]Updated 2FA status for Microsoft 365 & GoDaddy[/green]")
        log_action("2FA enabled for Microsoft 365 & GoDaddy")
    # Vault tip
    if Confirm.ask("Store backup codes in encrypted vault now?"):
        code = Prompt.ask("Paste backup codes or a note")
        vault_append(f"Backup codes: {code}")
        console.print("[green]Stored in encrypted vault[/green]")

# -------- Optional API stubs (disabled by default) --------
@cli.group()
def integrate():
    """Optional API integrations (placeholders)."""
    pass

@integrate.command("godaddy")
def integrate_godaddy():
    """Stub: manage DNS + auto-renew via GoDaddy API (requires API key/secret)."""
    console.print(Panel.fit(
        "GoDaddy API stub:\n- Would set auto-renew and manage DNS.\n- Requires GODADDY_API_KEY and GODADDY_API_SECRET in environment.\n- This is a placeholder to keep things safe.",
        border_style="yellow"
    ))
    log_action("GoDaddy API stub invoked")

@integrate.command("microsoft-graph")
def integrate_ms_graph():
    """Stub: create mailboxes via Microsoft Graph (requires Azure app)."""
    console.print(Panel.fit(
        "Microsoft Graph stub:\n- Would create mailboxes (rp, info, rsp, admin) and set policies.\n- Requires Azure App registration and delegated permissions.\n- Placeholder for future automation.",
        border_style="yellow"
    ))
    log_action("Microsoft Graph API stub invoked")

# -------- Help --------
@cli.command()
def help():
    """Show common commands."""
    console.print("""
[bold]Common commands:[/bold]
- python forward1_all_in_one.py help
- python forward1_all_in_one.py status
- python forward1_all_in_one.py checklist
- python forward1_all_in_one.py open godaddy
- python forward1_all_in_one.py vault add "Test recovery code"
- python forward1_all_in_one.py vault read
    """)
    log_action("Help viewed")

if __name__ == "__main__":
    cli()