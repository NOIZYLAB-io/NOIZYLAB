#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Noizy Fish All-In-One Cockpit
Author: R.S Plowman (Fish Music Inc.)

Unifies:
- Digital landscape (accounts/domains) with audit + enforcement
- Encrypted vault for 2FA recovery codes
- VS Code unanimity (front-document save + tasks/keybindings writer)
- Audio library scanner + dedupe + CSV/YAML export
- Snapshots + Git commit
- Optional Sarah voice via ElevenLabs (env: ELEVEN_API_KEY, ELEVEN_VOICE_ID)

Commands:
  python noizyfish_all_in_one.py init
  python noizyfish_all_in_one.py audit
  python noizyfish_all_in_one.py enforce
  python noizyfish_all_in_one.py status
  python noizyfish_all_in_one.py open "Microsoft 365"
  python noizyfish_all_in_one.py set2fa "YouTube" enabled
  python noizyfish_all_in_one.py store "YouTube" "code1,code2,..."
  python noizyfish_all_in_one.py read_vault
  python noizyfish_all_in_one.py write_vscode
  python noizyfish_all_in_one.py save_vscode
  python noizyfish_all_in_one.py git_commit "Message"
  python noizyfish_all_in_one.py scan_audio <paths...>
  python noizyfish_all_in_one.py assemble_audio --csv audio_library.csv --yaml audio_library.yaml
  python noizyfish_all_in_one.py snapshot
"""

import os
import sys
import csv
import yaml
import json
import time
import click
import shutil
import hashlib
import tempfile
import requests
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Tuple, Iterable
from rich.table import Table
from rich.console import Console
from cryptography.fernet import Fernet

console = Console()

# --- Constants ---
ROOT = Path(__file__).resolve().parent
CFG_FILE = ROOT / "digital_landscape.yaml"
LOG_DIR = ROOT / "logs"
SNAP_DIR = ROOT / "snapshots"
VAULT_FILE = ROOT / "vault.enc"
VAULT_KEY = ROOT / "vault.key"
AUDIO_SCAN_DB = ROOT / "audio_scan.jsonl"     # raw scan records
AUDIO_DEDUPE_DB = ROOT / "audio_dedupe.json"  # checksum -> best record
DEFAULT_CSV = ROOT / "audio_library.csv"
DEFAULT_YAML = ROOT / "audio_library.yaml"

PRIMARY_EMAIL = "rp@fishmusicinc.com"
ADMIN_EMAIL = "rsplowman@icloud.com"

ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY", "")
ELEVEN_VOICE_ID = os.getenv("ELEVEN_VOICE_ID", "")

KNOWN_SECURITY_URLS = {
    "Microsoft 365": "https://account.microsoft.com/security",
    "GoDaddy": "https://account.godaddy.com/security",
    "Facebook": "https://www.facebook.com/settings?tab=security",
    "YouTube": "https://myaccount.google.com/security",
    "SoundCloud": "https://soundcloud.com/settings/password",
}

DEFAULT_CFG = {
    "identity": {
        "primary_email": PRIMARY_EMAIL,
        "admin_email": ADMIN_EMAIL,
        "aliases": ["info@fishmusicinc.com", "support@fishmusicinc.com"]
    },
    "domains": [
        {"name": "fishmusicinc.com", "registrar": "GoDaddy", "dns_host": "Microsoft 365", "status": "active"},
        {"name": "noizy.ai", "registrar": "GoDaddy", "dns_host": "GoDaddy", "status": "active"}
    ],
    "accounts": [
        {"service": "Microsoft 365", "login": PRIMARY_EMAIL, "twofa": "pending", "recovery_codes": "vault", "security_url": KNOWN_SECURITY_URLS["Microsoft 365"]},
        {"service": "GoDaddy", "login": PRIMARY_EMAIL, "twofa": "pending", "recovery_codes": "vault", "security_url": KNOWN_SECURITY_URLS["GoDaddy"]},
        {"service": "Facebook", "login": PRIMARY_EMAIL, "twofa": "pending", "recovery_codes": "vault", "security_url": KNOWN_SECURITY_URLS["Facebook"]},
        {"service": "YouTube", "login": PRIMARY_EMAIL, "twofa": "pending", "recovery_codes": "vault", "security_url": KNOWN_SECURITY_URLS["YouTube"]},
        {"service": "SoundCloud", "login": PRIMARY_EMAIL, "twofa": "pending", "recovery_codes": "vault", "security_url": KNOWN_SECURITY_URLS["SoundCloud"]},
    ],
    "notes": "Single source of truth for the digital landscape."
}

AUDIO_EXTS = {".wav", ".aiff", ".aif", ".flac", ".mp3", ".ogg", ".m4a", ".aac"}


# --- Setup ---
def ensure_dirs():
    LOG_DIR.mkdir(exist_ok=True)
    SNAP_DIR.mkdir(exist_ok=True)


def load_cfg() -> Dict[str, Any]:
    if not CFG_FILE.exists():
        with CFG_FILE.open("w") as f:
            yaml.safe_dump(DEFAULT_CFG, f, sort_keys=False)
    with CFG_FILE.open("r") as f:
        return yaml.safe_load(f)


def save_cfg(cfg: Dict[str, Any]):
    with CFG_FILE.open("w") as f:
        yaml.safe_dump(cfg, f, sort_keys=False)


# --- Voice (optional) ---
def speak(text: str):
    if not ELEVEN_API_KEY or not ELEVEN_VOICE_ID:
        return
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}"
        headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
        data = {"text": text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.85}}
        r = requests.post(url, headers=headers, json=data, timeout=20)
        r.raise_for_status()
    except Exception:
        return
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp.write(r.content); tmp.close()
    subprocess.run(["afplay", tmp.name], check=False)
    try: os.remove(tmp.name)
    except Exception: pass


# --- Vault ---
def get_fernet() -> Fernet:
    if not VAULT_KEY.exists():
        key = Fernet.generate_key()
        with VAULT_KEY.open("wb") as fk:
            fk.write(key)
        console.print("[green]Generated vault.key — back it up safely.[/green]")
    with VAULT_KEY.open("rb") as fk:
        key = fk.read()
    return Fernet(key)


def vault_add(service: str, text: str):
    f = get_fernet()
    existing = b""
    if VAULT_FILE.exists():
        try:
            existing = f.decrypt(VAULT_FILE.read_bytes())
        except Exception:
            existing = b""
    entry = f"[{datetime.utcnow().isoformat()}] {service}: {text}\n".encode()
    enc = f.encrypt(existing + entry)
    VAULT_FILE.write_bytes(enc)


def vault_read() -> str:
    f = get_fernet()
    if not VAULT_FILE.exists():
        return ""
    try:
        return f.decrypt(VAULT_FILE.read_bytes()).decode()
    except Exception:
        return ""


# --- Audit & Enforcement ---
def audit(cfg: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    issues = {"stray_logins": [], "missing_twofa": [], "missing_security_url": []}
    for acc in cfg.get("accounts", []):
        login = acc.get("login", "").strip().lower()
        if login not in (PRIMARY_EMAIL.lower(), ADMIN_EMAIL.lower()):
            issues["stray_logins"].append(acc)
        if acc.get("twofa", "pending") != "enabled":
            issues["missing_twofa"].append(acc)
        if not acc.get("security_url"):
            issues["missing_security_url"].append(acc)
    return issues


def print_audit(issues: Dict[str, List[Dict[str, Any]]]):
    table = Table(title="Digital Landscape Audit")
    table.add_column("Issue", style="bold")
    table.add_column("Service")
    table.add_column("Login")
    table.add_column("Note")
    for acc in issues["stray_logins"]:
        table.add_row("Stray login", acc["service"], acc.get("login",""), "Migrate to rp@fishmusicinc.com")
    for acc in issues["missing_twofa"]:
        table.add_row("2FA not enabled", acc["service"], acc.get("login",""), "Enable and store recovery codes")
    for acc in issues["missing_security_url"]:
        table.add_row("Missing security URL", acc["service"], acc.get("login",""), "Add portal URL")
    console.print(table)


def enforce_primary(cfg: Dict[str, Any]) -> int:
    changed = 0
    for acc in cfg.get("accounts", []):
        login = acc.get("login", "")
        if login.strip().lower() not in (PRIMARY_EMAIL.lower(), ADMIN_EMAIL.lower()):
            acc["login"] = PRIMARY_EMAIL
            changed += 1
    if changed:
        save_cfg(cfg)
    return changed


# --- Portals ---
def open_portal(service: str, cfg: Dict[str, Any]):
    url = None
    for acc in cfg.get("accounts", []):
        if acc["service"].lower() == service.lower():
            url = acc.get("security_url")
            break
    if not url:
        url = KNOWN_SECURITY_URLS.get(service)
    if not url:
        console.print(f"[yellow]No security URL known for {service}[/yellow]")
        return
    subprocess.run(["open", url])
    speak(f"Opening {service} security portal.")


# --- VS Code unanimity ---
def vscode_save_front():
    subprocess.run(["osascript", "-e", 'tell application "Visual Studio Code" to save front document'])
    console.print("[green]VS Code: front document saved[/green]")
    speak("VS Code save complete.")


def git_commit(message: str = "Noizy Fish commit"):
    try:
        subprocess.run(["git", "add", "."], check=False)
        subprocess.run(["git", "commit", "-m", message], check=False)
        console.print(f"[green]Git commit:[/green] {message}")
        speak("Commit complete.")
    except Exception as e:
        console.print(f"[yellow]Git commit skipped:[/yellow] {e}")


TASKS_JSON = {
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Noizy Fish: Status",
            "type": "shell",
            "command": "python",
            "args": ["noizyfish_all_in_one.py", "status"],
            "problemMatcher": []
        },
        {
            "label": "Noizy Fish: Audit Landscape",
            "type": "shell",
            "command": "python",
            "args": ["noizyfish_all_in_one.py", "audit"],
            "problemMatcher": []
        },
        {
            "label": "Noizy Fish: Enforce Primary",
            "type": "shell",
            "command": "python",
            "args": ["noizyfish_all_in_one.py", "enforce"],
            "problemMatcher": []
        },
        {
            "label": "Noizy Fish: Scan Audio",
            "type": "shell",
            "command": "python",
            "args": ["noizyfish_all_in_one.py", "scan_audio"],
            "problemMatcher": []
        },
        {
            "label": "Noizy Fish: Assemble Audio Library",
            "type": "shell",
            "command": "python",
            "args": ["noizyfish_all_in_one.py", "assemble_audio"],
            "problemMatcher": []
        }
    ]
}

KEYBINDINGS_JSON = [
    {
        "key": "shift+cmd+b",
        "command": "workbench.action.tasks.runTask",
        "args": "Noizy Fish: Status",
        "when": "editorTextFocus"
    }
]

def write_vscode_files():
    vscode_dir = ROOT / ".vscode"
    vscode_dir.mkdir(exist_ok=True)
    (vscode_dir / "tasks.json").write_text(json.dumps(TASKS_JSON, indent=2))
    (vscode_dir / "keybindings.json").write_text(json.dumps(KEYBINDINGS_JSON, indent=2))
    console.print(f"[green]Wrote VS Code tasks/keybindings in {vscode_dir}[/green]")
    speak("VS Code template files written.")


# --- Audio scanning & assembly ---
def file_checksum(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def probe_basic_audio(path: Path) -> Dict[str, Any]:
    info = {"path": str(path), "name": path.name, "ext": path.suffix.lower(), "size_bytes": path.stat().st_size, "duration_sec": None}
    if path.suffix.lower() in (".wav", ".aiff", ".aif"):
        try:
            import wave
            with wave.open(str(path), "rb") as w:
                frames = w.getnframes()
                rate = w.getframerate()
                info["duration_sec"] = round(frames / float(rate), 3) if rate else None
        except Exception:
            pass
    return info


def scan_paths(paths: Iterable[Path]) -> int:
    count = 0
    with AUDIO_SCAN_DB.open("a") as out:
        for p in paths:
            root = p.expanduser().resolve()
            if not root.exists():
                console.print(f"[yellow]Missing path:[/yellow] {root}")
                continue
            for path in root.rglob("*"):
                if path.is_file() and path.suffix.lower() in AUDIO_EXTS:
                    info = probe_basic_audio(path)
                    info["checksum"] = file_checksum(path)
                    out.write(json.dumps(info) + "\n")
                    count += 1
    return count


def dedupe_scan() -> Tuple[int, int]:
    if not AUDIO_SCAN_DB.exists():
        return 0, 0
    best: Dict[str, Dict[str, Any]] = {}
    with AUDIO_SCAN_DB.open("r") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except Exception:
                continue
            checksum = rec.get("checksum")
            if not checksum:
                continue
            rank = {"wav": 4, "aiff": 4, "aif": 4, "flac": 3, "m4a": 2, "mp3": 2, "ogg": 2, "aac": 2}.get(rec.get("ext", "").lstrip("."), 1)
            prev = best.get(checksum)
            if not prev or rank > prev.get("_rank", 0):
                rec["_rank"] = rank
                best[checksum] = rec
    AUDIO_DEDUPE_DB.write_text(json.dumps(best, indent=2))
    total = sum(1 for _ in AUDIO_SCAN_DB.open("r"))
    return total, len(best)


def export_audio_library(csv_path: Path, yaml_path: Path):
    if not AUDIO_DEDUPE_DB.exists():
        console.print("[yellow]No dedupe database found. Run assemble_audio first.[/yellow]")
        return
    db = json.loads(AUDIO_DEDUPE_DB.read_text())
    rows = []
    for checksum, rec in db.items():
        rows.append({
            "checksum": checksum,
            "path": rec.get("path", ""),
            "name": rec.get("name", ""),
            "ext": rec.get("ext", ""),
            "size_bytes": rec.get("size_bytes", 0),
            "duration_sec": rec.get("duration_sec", None),
        })
    # CSV
    with csv_path.open("w", newline="") as f:
        headers = ["checksum","path","name","ext","size_bytes","duration_sec"]
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in headers})
    console.print(f"[green]Exported CSV:[/green] {csv_path}")
    # YAML
    with yaml_path.open("w") as f:
        yaml.safe_dump({"audio_files": rows}, f, sort_keys=False)
    console.print(f"[green]Exported YAML:[/green] {yaml_path}")


# --- Snapshots & status ---
def snapshot_cfg():
    ensure_dirs()
    stamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    dest = SNAP_DIR / f"digital_landscape_{stamp}.yaml"
    shutil.copyfile(CFG_FILE, dest)
    console.print(f"[green]Snapshot saved:[/green] {dest}")
    speak("Digital landscape snapshot saved.")


def show_status():
    cfg = load_cfg()
    table = Table(title="Accounts")
    table.add_column("Service", style="bold")
    table.add_column("Login")
    table.add_column("2FA")
    table.add_column("Portal")
    for acc in cfg.get("accounts", []):
        table.add_row(acc["service"], acc.get("login",""), acc.get("twofa","pending"), acc.get("security_url",""))
    console.print(table)


# --- CLI ---
@click.group()
def cli():
    ensure_dirs()


@cli.command()
def init():
    """Create default digital_landscape.yaml if missing."""
    if CFG_FILE.exists():
        console.print("[yellow]Config already exists.[/yellow]")
        return
    save_cfg(DEFAULT_CFG)
    console.print("[green]Initialized digital_landscape.yaml[/green]")
    speak("Digital landscape initialized.")


@cli.command(name="audit")
def audit_cmd():
    """Audit accounts for redundancy and missing 2FA/URLs."""
    cfg = load_cfg()
    issues = audit(cfg)
    print_audit(issues)
    total = sum(len(v) for v in issues.values())
    speak(f"Audit complete. {total} issues found.") if total else speak("Audit complete. No issues found.")


@cli.command()
def enforce():
    """Enforce rp@fishmusicinc.com as primary login across accounts."""
    cfg = load_cfg()
    changed = enforce_primary(cfg)
    console.print(f"[green]Updated {changed} account(s) to {PRIMARY_EMAIL}[/green]")
    speak(f"Primary login enforced on {changed} accounts.")
    vscode_save_front()


@cli.command()
def status():
    """Show accounts table."""
    show_status()


@cli.command()
@click.argument("service")
def open(service: str):
    """Open the security/admin portal for a service."""
    cfg = load_cfg()
    open_portal(service, cfg)


@cli.command()
@click.argument("service")
@click.argument("status")
def set2fa(service: str, status: str):
    """Set 2FA status for a service (enabled/pending)."""
    cfg = load_cfg()
    for acc in cfg.get("accounts", []):
        if acc["service"].lower() == service.lower():
            acc["twofa"] = status
            save_cfg(cfg)
            console.print(f"[green]{service} 2FA → {status}[/green]")
            speak(f"{service} two-factor is now {status}.")
            vscode_save_front()
            return
    console.print(f"[red]Service not found: {service}[/red]")


@cli.command()
@click.argument("service")
@click.argument("codes")
def store(service: str, codes: str):
    """Store recovery codes for a service in encrypted vault."""
    vault_add(service, codes)
    console.print("[green]Stored codes in encrypted vault[/green]")
    speak(f"Stored {service} codes in the vault.")
    vscode_save_front()


@cli.command()
def read_vault():
    """Print vault contents."""
    out = vault_read()
    console.print(out if out else "[yellow]Vault empty[/yellow]")


@cli.command()
def write_vscode():
    """Write .vscode/tasks.json and keybindings.json (permanent wiring)."""
    write_vscode_files()


@cli.command()
def save_vscode():
    """Ask VS Code to save the front document (unanimity)."""
    vscode_save_front()


@cli.command()
@click.argument("message", required=False, default="Noizy Fish commit")
def git_commit(message: str):
    """Git add/commit with a message."""
    git_commit(message)


@cli.command()
@click.argument("paths", nargs=-1)
def scan_audio(paths: Tuple[str, ...]):
    """Scan paths for audio files and record raw entries."""
    if not paths:
        console.print("[yellow]Provide one or more paths to scan.[/yellow]")
        return
    count = scan_paths([Path(p) for p in paths])
    console.print(f"[green]Scanned audio files:[/green] {count}")
    speak(f"Audio scan complete. {count} files recorded.")
    vscode_save_front()


@cli.command()
@click.option("--csv", "csv_path", default=str(DEFAULT_CSV), help="Output CSV path")
@click.option("--yaml", "yaml_path", default=str(DEFAULT_YAML), help="Output YAML path")
def assemble_audio(csv_path: str, yaml_path: str):
    """Deduplicate scanned audio and export the library index."""
    total, unique = dedupe_scan()
    console.print(f"[green]Scan records:[/green] {total}  [green]Unique files:[/green] {unique}")
    export_audio_library(Path(csv_path), Path(yaml_path))
    speak(f"Audio assembly complete. {unique} unique files indexed.")
    vscode_save_front()


@cli.command()
def snapshot():
    """Save timestamped snapshot of digital_landscape.yaml."""
    snapshot_cfg()
    vscode_save_front()


if __name__ == "__main__":
    cli()