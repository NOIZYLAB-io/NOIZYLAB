#!/usr/bin/env python3
"""
Authenticator Orchestrator: Streamlined 2FA rollout and tracking
- Opens target security portals
- Guides flows for Microsoft 365, GoDaddy, Facebook
- Encrypts backup codes in a vault
- Tracks 2FA status in config.yaml
- Optional: ElevenLabs TTS confirmations (Sarah)
- Optional: TOTP generation from stored secrets (pyotp)
"""

import os, sys, yaml, click, webbrowser, logging, subprocess, tempfile, requests
from datetime import datetime
from typing import Dict, Any
from rich.console import Console
from rich.table import Table
from cryptography.fernet import Fernet

console = Console()

# Files
CONFIG_FILE = "config.yaml"
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "auth_orchestrator.log")
VAULT_KEY_FILE = "vault.key"
VAULT_FILE = "vault.enc"

# Optional TTS (ElevenLabs)
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
ELEVEN_VOICE_ID = os.getenv("ELEVEN_VOICE_ID")  # Sarah's voice ID

DEFAULT_CONFIG = {
    "identity": {
        "admin_email": "rsplowman@icloud.com",
        "business_email": "rp@fishmusicinc.com"
    },
    "accounts": [
        {"name": "Microsoft 365", "email": "rsplowman@icloud.com", "security_url": "https://account.microsoft.com/security", "twofa": "pending"},
        {"name": "GoDaddy", "email": "rp@fishmusicinc.com", "security_url": "https://account.godaddy.com/security", "twofa": "pending"},
        {"name": "Facebook", "email": "rp@fishmusicinc.com", "security_url": "https://www.facebook.com/settings?tab=security", "twofa": "pending"}
    ],
    "settings": {"tts": True, "log_actions": True}
}

# Setup
def ensure_setup():
    os.makedirs(LOG_DIR, exist_ok=True)
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            yaml.safe_dump(DEFAULT_CONFIG, f, sort_keys=False)
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def log(msg: str):
    logging.info(msg)

def load_cfg() -> Dict[str, Any]:
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)

def save_cfg(cfg: Dict[str, Any]):
    with open(CONFIG_FILE, "w") as f:
        yaml.safe_dump(cfg, f, sort_keys=False)

# Vault
def get_fernet() -> Fernet:
    if not os.path.exists(VAULT_KEY_FILE):
        key = Fernet.generate_key()
        with open(VAULT_KEY_FILE, "wb") as fk: fk.write(key)
        console.print("[green]Generated vault.key — back it up safely.[/green]")
    with open(VAULT_KEY_FILE, "rb") as fk: key = fk.read()
    return Fernet(key)

def vault_add(text: str):
    f = get_fernet()
    existing = b""
    if os.path.exists(VAULT_FILE):
        try:
            existing = f.decrypt(open(VAULT_FILE, "rb").read())
        except Exception:
            existing = b""
    new_plain = existing + f"[{datetime.utcnow().isoformat()}] {text}\n".encode()
    enc = f.encrypt(new_plain)
    with open(VAULT_FILE, "wb") as vf: vf.write(enc)

def vault_read() -> str:
    f = get_fernet()
    if not os.path.exists(VAULT_FILE): return ""
    try:
        return f.decrypt(open(VAULT_FILE, "rb").read()).decode()
    except Exception:
        return ""

# TTS with ElevenLabs
def speak(text: str):
    cfg = load_cfg()
    if not cfg["settings"].get("tts"): return
    if not ELEVEN_API_KEY or not ELEVEN_VOICE_ID:
        return
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}"
    headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
    data = {"text": text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}}
    try:
        r = requests.post(url, headers=headers, json=data, timeout=20)
        r.raise_for_status()
    except Exception as e:
        console.print(f"[red]TTS error:[/red] {e}")
        return
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp.write(r.content); tmp.close()
    # macOS playback
    subprocess.run(["afplay", tmp.name])
    try: os.remove(tmp.name)
    except: pass

def open_url(name: str, url: str):
    webbrowser.open(url)
    console.print(f"[green]Opened:[/green] {name} → {url}")
    log(f"Opened {name}: {url}")

# Optional TOTP fallback (requires stored shared secret)
try:
    import pyotp
except ImportError:
    pyotp = None

def totp_code(secret: str) -> str:
    if not pyotp:
        return "Install pyotp to compute TOTP (pip install pyotp)."
    return pyotp.TOTP(secret).now()

# CLI
@click.group()
def cli():
    ensure_setup()

@cli.command()
def status():
    """Show account status."""
    cfg = load_cfg()
    table = Table(title="Accounts")
    table.add_column("Name"); table.add_column("Email"); table.add_column("2FA")
    for a in cfg["accounts"]:
        table.add_row(a["name"], a["email"], a.get("twofa", "unknown"))
    console.print(table)

@cli.command()
@click.argument("name")
@click.argument("status")
def set2fa(name: str, status: str):
    """Mark 2FA status for an account."""
    cfg = load_cfg()
    for a in cfg["accounts"]:
        if a["name"].lower() == name.lower():
            a["twofa"] = status
            save_cfg(cfg)
            console.print(f"[green]Updated:[/green] {name} → {status}")
            speak(f"{name} two-factor authentication is now {status}.")
            return
    console.print(f"[red]Account not found:[/red] {name}")

@cli.group()
def flow():
    """Guided flows for enabling 2FA."""
    pass

@flow.command("m365")
def flow_m365():
    """Enable 2FA for Microsoft 365 (guided)."""
    cfg = load_cfg()
    acc = next((a for a in cfg["accounts"] if a["name"] == "Microsoft 365"), None)
    if acc: open_url("Microsoft Security", acc["security_url"])
    speak("Open Microsoft Security. Choose Two-step verification, then Authenticator app.")
    console.print("- Turn on Two-step verification.")
    console.print("- Choose 'Authenticator App' and scan QR with iPhone, then iPad.")
    console.print("- Copy backup codes below and paste into vault when prompted.")
    if click.confirm("Mark Microsoft 365 2FA as enabled?"):
        acc["twofa"] = "enabled"; save_cfg(cfg)
        console.print("[green]Microsoft 365 2FA → enabled[/green]"); speak("Microsoft two-factor enabled.")
        codes = click.prompt("Paste backup codes (or a note)", default="", show_default=False)
        if codes.strip():
            vault_add(f"Microsoft 365 backup codes: {codes.strip()}")
            console.print("[green]Stored backup codes in encrypted vault[/green]"); speak("Backup codes stored securely.")

@flow.command("godaddy")
def flow_godaddy():
    """Enable 2FA for GoDaddy (guided)."""
    cfg = load_cfg()
    acc = next((a for a in cfg["accounts"] if a["name"] == "GoDaddy"), None)
    if acc: open_url("GoDaddy Security", acc["security_url"])
    speak("Open GoDaddy Security. Enable authenticator app two factor.")
    console.print("- Enable Authenticator app 2FA.")
    console.print("- Scan QR on iPhone, then iPad.")
    if click.confirm("Mark GoDaddy 2FA as enabled?"):
        acc["twofa"] = "enabled"; save_cfg(cfg)
        console.print("[green]GoDaddy 2FA → enabled[/green]"); speak("GoDaddy two-factor enabled.")
        codes = click.prompt("Paste backup codes (or a note)", default="", show_default=False)
        if codes.strip():
            vault_add(f"GoDaddy backup codes: {codes.strip()}")
            console.print("[green]Stored backup codes in encrypted vault[/green]")

@flow.command("facebook")
def flow_facebook():
    """Enable 2FA for Facebook (guided)."""
    cfg = load_cfg()
    acc = next((a for a in cfg["accounts"] if a["name"] == "Facebook"), None)
    if acc: open_url("Facebook Security", acc["security_url"])
    speak("Open Facebook Security and choose authentication app.")
    console.print("- Two-Factor Authentication → Authentication App.")
    console.print("- Scan QR with iPhone and iPad.")
    if click.confirm("Mark Facebook 2FA as enabled?"):
        acc["twofa"] = "enabled"; save_cfg(cfg)
        console.print("[green]Facebook 2FA → enabled[/green]"); speak("Facebook two-factor enabled.")
        codes = click.prompt("Paste backup codes (or a note)", default="", show_default=False)
        if codes.strip():
            vault_add(f"Facebook backup codes: {codes.strip()}")
            console.print("[green]Stored backup codes in encrypted vault[/green]")

@cli.group()
def vault():
    """Encrypted vault operations."""
    pass

@vault.command("add")
@click.argument("text", nargs=-1)
def vault_add_cmd(text):
    payload = " ".join(text).strip()
    if not payload:
        console.print("[red]Provide text to store[/red]"); return
    vault_add(payload); speak("Stored in encrypted vault.")
    console.print("[green]Stored in encrypted vault[/green]")

@vault.command("read")
def vault_read_cmd():
    out = vault_read()
    if not out:
        console.print("[yellow]Vault is empty or unreadable[/yellow]")
    else:
        console.print(out)

@cli.command()
@click.argument("service")
@click.argument("secret")
def totp(service: str, secret: str):
    """Compute a TOTP code (backup) given a shared secret."""
    code = totp_code(secret)
    console.print(f"{service} TOTP: {code}")

@cli.command()
def save_all():
    """Ask VS Code to save the front document (macOS AppleScript)."""
    subprocess.run(["osascript", "-e", 'tell application "Visual Studio Code" to save front document'])
    speak("File saved."); console.print("[green]VS Code save triggered[/green]")

@cli.command()
def helpme():
    """List common commands."""
    console.print("""
Commands:
- python authenticator_orchestrator.py status
- python authenticator_orchestrator.py flow m365
- python authenticator_orchestrator.py flow godaddy
- python authenticator_orchestrator.py flow facebook
- python authenticator_orchestrator.py vault add "Service backup codes: XXXXX"
- python authenticator_orchestrator.py vault read
- python authenticator_orchestrator.py set2fa "Microsoft 365" enabled
- python authenticator_orchestrator.py save_all
- python authenticator_orchestrator.py totp Service SECRET
""")

if __name__ == "__main__":
    cli()