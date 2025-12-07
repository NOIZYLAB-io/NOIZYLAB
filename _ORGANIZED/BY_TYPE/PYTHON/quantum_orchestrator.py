#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quantum Orchestrator — Noizy Fish
Author: R.S Plowman (Fish Music Inc.)

Engines:
1) Identity Lockdown
2) Vault & Recovery
3) VS Code Cockpit
4) Snapshot & Git
5) Audio Scanner
6) Deduplication
7) Library Assembly (with simple project/year tags)
8) Automation Hooks
9) Distribution Staging
10) Legacy Pack

Commands:
  python quantum_orchestrator.py init
  python quantum_orchestrator.py ignition
  python quantum_orchestrator.py identity
  python quantum_orchestrator.py vault
  python quantum_orchestrator.py cockpit
  python quantum_orchestrator.py snapshot
  python quantum_orchestrator.py commit "Message"
  python quantum_orchestrator.py scan --paths <p1> <p2> ...
  python quantum_orchestrator.py assemble --csv audio_library.csv --yaml audio_library.yaml
  python quantum_orchestrator.py distribute --title "Work Title" --folder Release
  python quantum_orchestrator.py legacy --year 2025 --out LegacyPack_2025.zip
"""

import os, sys, csv, yaml, json, hashlib, shutil, tempfile, subprocess, time, re, zipfile
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Tuple, Optional
import click
from rich.console import Console
from rich.table import Table
from cryptography.fernet import Fernet

console = Console()

# Paths
ROOT = Path(__file__).resolve().parent
CFG_FILE = ROOT / "digital_landscape.yaml"
VAULT_FILE = ROOT / "vault.enc"
VAULT_KEY = ROOT / "vault.key"
SCAN_DB = ROOT / "audio_scan.jsonl"
DEDUP_DB = ROOT / "audio_dedupe.json"
CSV_OUT = ROOT / "audio_library.csv"
YAML_OUT = ROOT / "audio_library.yaml"
SNAP_DIR = ROOT / "snapshots"
VS_DIR = ROOT / ".vscode"

# Identity
PRIMARY_EMAIL = "rp@fishmusicinc.com"
ADMIN_EMAIL = "rsplowman@icloud.com"
KNOWN_SECURITY_URLS = {
    "Microsoft 365": "https://account.microsoft.com/security",
    "GoDaddy": "https://account.godaddy.com/security",
    "Facebook": "https://www.facebook.com/settings?tab=security",
    "YouTube": "https://myaccount.google.com/security",
    "SoundCloud": "https://soundcloud.com/settings/password",
}

# Audio
AUDIO_EXTS = {".wav", ".aiff", ".aif", ".flac", ".mp3", ".ogg", ".m4a", ".aac"}
FORMAT_RANK = {"wav": 4, "aiff": 4, "aif": 4, "flac": 3, "m4a": 2, "mp3": 2, "ogg": 2, "aac": 2}

# Optional voice
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY", "")
ELEVEN_VOICE_ID = os.getenv("ELEVEN_VOICE_ID", "")

def speak(text: str):
    if not ELEVEN_API_KEY or not ELEVEN_VOICE_ID:
        return
    try:
        import requests
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}"
        headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
        data = {"text": text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.85}}
        r = requests.post(url, headers=headers, json=data, timeout=20)
        r.raise_for_status()
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tmp.write(r.content); tmp.close()
        subprocess.run(["afplay", tmp.name], check=False)
        os.remove(tmp.name)
    except Exception:
        pass

def ensure_dirs():
    SNAP_DIR.mkdir(exist_ok=True)
    VS_DIR.mkdir(exist_ok=True)

def save_vscode():
    subprocess.run(["osascript","-e",'tell application "Visual Studio Code" to save front document'])

def load_cfg() -> Dict[str, Any]:
    if not CFG_FILE.exists():
        default_cfg = {
            "identity": {"primary_email": PRIMARY_EMAIL, "admin_email": ADMIN_EMAIL, "aliases": ["info@fishmusicinc.com","support@fishmusicinc.com"]},
            "domains": [
                {"name":"fishmusicinc.com","registrar":"GoDaddy","dns_host":"Microsoft 365","status":"active"},
                {"name":"noizy.ai","registrar":"GoDaddy","dns_host":"GoDaddy","status":"active"},
            ],
            "accounts": [
                {"service":"Microsoft 365","login":PRIMARY_EMAIL,"twofa":"pending","recovery_codes":"vault","security_url":KNOWN_SECURITY_URLS["Microsoft 365"]},
                {"service":"GoDaddy","login":PRIMARY_EMAIL,"twofa":"pending","recovery_codes":"vault","security_url":KNOWN_SECURITY_URLS["GoDaddy"]},
                {"service":"Facebook","login":PRIMARY_EMAIL,"twofa":"pending","recovery_codes":"vault","security_url":KNOWN_SECURITY_URLS["Facebook"]},
                {"service":"YouTube","login":PRIMARY_EMAIL,"twofa":"pending","recovery_codes":"vault","security_url":KNOWN_SECURITY_URLS["YouTube"]},
                {"service":"SoundCloud","login":PRIMARY_EMAIL,"twofa":"pending","recovery_codes":"vault","security_url":KNOWN_SECURITY_URLS["SoundCloud"]},
            ],
            "notes": "Single source of truth for Rob's digital landscape."
        }
        CFG_FILE.write_text(yaml.safe_dump(default_cfg, sort_keys=False))
    return yaml.safe_load(CFG_FILE.read_text())

def save_cfg(cfg: Dict[str, Any]):
    CFG_FILE.write_text(yaml.safe_dump(cfg, sort_keys=False))
    save_vscode()

# Vault
def get_fernet() -> Fernet:
    if not VAULT_KEY.exists():
        key = Fernet.generate_key()
        VAULT_KEY.write_bytes(key)
        console.print("[green]Generated vault.key — back it up safely.[/green]")
    return Fernet(VAULT_KEY.read_bytes())

def vault_add(service: str, text: str):
    f = get_fernet()
    existing = b""
    if VAULT_FILE.exists():
        try:
            existing = f.decrypt(VAULT_FILE.read_bytes())
        except Exception:
            existing = b""
    entry = f"[{datetime.utcnow().isoformat()}] {service}: {text}\n".encode()
    VAULT_FILE.write_bytes(f.encrypt(existing + entry))
    save_vscode()

def vault_read() -> str:
    f = get_fernet()
    if not VAULT_FILE.exists(): return ""
    try: return f.decrypt(VAULT_FILE.read_bytes()).decode()
    except Exception: return ""

# Identity engine
def identity_lockdown() -> int:
    cfg = load_cfg()
    changed = 0
    for acc in cfg.get("accounts", []):
        login = acc.get("login","").strip().lower()
        if login not in (PRIMARY_EMAIL.lower(), ADMIN_EMAIL.lower()):
            acc["login"] = PRIMARY_EMAIL
            changed += 1
        if not acc.get("security_url"):
            acc["security_url"] = KNOWN_SECURITY_URLS.get(acc["service"], "")
    save_cfg(cfg)
    console.print(f"[green]Identity enforced; updated {changed} account(s).[/green]")
    speak(f"Identity lockdown complete. {changed} accounts updated.")
    return changed

def identity_audit() -> Table:
    cfg = load_cfg()
    t = Table(title="Identity Audit")
    t.add_column("Service"); t.add_column("Login"); t.add_column("2FA"); t.add_column("Portal"); t.add_column("Note")
    for acc in cfg.get("accounts", []):
        note = ""
        login = acc.get("login","")
        if login.strip().lower() not in (PRIMARY_EMAIL.lower(), ADMIN_EMAIL.lower()):
            note = "Stray login"
        if acc.get("twofa","pending") != "enabled":
            note = (note + " | " if note else "") + "2FA pending"
        if not acc.get("security_url"):
            note = (note + " | " if note else "") + "Missing portal"
        t.add_row(acc["service"], login, acc.get("twofa","pending"), acc.get("security_url",""), note)
    console.print(t)
    return t

# VS Code cockpit engine
def write_vscode_files():
    tasks = {
        "version": "2.0.0",
        "tasks": [
            {"label":"Noizy Fish: Status","type":"shell","command":"python","args":[str(ROOT/"quantum_orchestrator.py"),"status"],"problemMatcher":[]},
            {"label":"Noizy Fish: Ignition","type":"shell","command":"python","args":[str(ROOT/"quantum_orchestrator.py"),"ignition"],"problemMatcher":[]},
            {"label":"Noizy Fish: Scan Audio","type":"shell","command":"python","args":[str(ROOT/"quantum_orchestrator.py"),"scan"],"problemMatcher":[]},
            {"label":"Noizy Fish: Assemble Library","type":"shell","command":"python","args":[str(ROOT/"quantum_orchestrator.py"),"assemble"],"problemMatcher":[]},
        ]
    }
    (VS_DIR/"tasks.json").write_text(json.dumps(tasks, indent=2))
    keybindings = [
        {"key":"shift+cmd+b","command":"workbench.action.tasks.runTask","args":"Noizy Fish: Status","when":"editorTextFocus"}
    ]
    (VS_DIR/"keybindings.json").write_text(json.dumps(keybindings, indent=2))
    console.print(f"[green]VS Code cockpit wired in {VS_DIR}[/green]")
    speak("VS Code cockpit wired.")
    save_vscode()

# Snapshot & Git
def snapshot_cfg(label: str = "digital_landscape"):
    SNAP_DIR.mkdir(exist_ok=True)
    dest = SNAP_DIR / f"{label}_{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}.yaml"
    shutil.copyfile(CFG_FILE, dest)
    console.print(f"[green]Snapshot saved:[/green] {dest}")
    speak("Snapshot saved.")
    save_vscode()

def git_commit(message: str = "Noizy Fish commit"):
    subprocess.run(["git","add","."], check=False)
    subprocess.run(["git","commit","-m",message], check=False)
    console.print(f"[green]Git commit:[/green] {message}")
    speak("Commit complete.")

# Audio scanner
def file_checksum(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def probe_audio(path: Path) -> Dict[str, Any]:
    info = {"path": str(path), "name": path.name, "ext": path.suffix.lower(), "size_bytes": path.stat().st_size, "duration_sec": None}
    if path.suffix.lower() in (".wav",".aiff",".aif"):
        try:
            import wave
            with wave.open(str(path),"rb") as w:
                frames=w.getnframes(); rate=w.getframerate()
                info["duration_sec"]=round(frames/float(rate),3) if rate else None
        except Exception:
            pass
    # Simple project/year tag from folders: /Projects/ProjectName/2021/track.wav
    parts = path.parts
    info["project"] = next((p for p in parts if re.match(r"^[A-Za-z0-9_\-\.]{3,}$", p)), None)
    year_matches = [p for p in parts if re.match(r"^20\d{2}$", p)]
    info["year"] = year_matches[-1] if year_matches else None
    return info

def scan_paths(paths: List[Path]) -> int:
    count = 0
    with SCAN_DB.open("a") as out:
        for root in paths:
            root = root.expanduser().resolve()
            if not root.exists():
                console.print(f"[yellow]Missing path:[/yellow] {root}")
                continue
            for p in root.rglob("*"):
                if p.is_file() and p.suffix.lower() in AUDIO_EXTS:
                    rec = probe_audio(p)
                    rec["checksum"] = file_checksum(p)
                    out.write(json.dumps(rec) + "\n")
                    count += 1
    console.print(f"[green]Scanned {count} audio files[/green]")
    speak(f"Scan complete: {count} files.")
    save_vscode()
    return count

# Deduplication
def dedupe_scan() -> Tuple[int,int]:
    if not SCAN_DB.exists(): return 0,0
    best = {}
    total = 0
    with SCAN_DB.open("r") as f:
        for line in f:
            total += 1
            try: rec=json.loads(line)
            except Exception: continue
            cs = rec.get("checksum"); ext = rec.get("ext","").lstrip(".").lower()
            rank = FORMAT_RANK.get(ext,1)
            prev = best.get(cs)
            if cs and (not prev or rank > prev.get("_rank",0)):
                rec["_rank"] = rank
                best[cs] = rec
    DEDUP_DB.write_text(json.dumps(best, indent=2))
    console.print(f"[green]Deduped to {len(best)} unique files[/green]")
    speak(f"Deduplication complete: {len(best)} unique.")
    save_vscode()
    return total, len(best)

# Library assembly
def export_library(csv_path: Path = CSV_OUT, yaml_path: Path = YAML_OUT):
    if not DEDUP_DB.exists():
        console.print("[yellow]No dedupe DB found. Run assemble first.[/yellow]"); return
    db = json.loads(DEDUP_DB.read_text())
    rows = []
    for cs, rec in db.items():
        rows.append({
            "checksum": cs,
            "path": rec.get("path",""),
            "name": rec.get("name",""),
            "ext": rec.get("ext",""),
            "size_bytes": rec.get("size_bytes",0),
            "duration_sec": rec.get("duration_sec",None),
            "project": rec.get("project",None),
            "year": rec.get("year",None),
        })
    # CSV
    with csv_path.open("w", newline="") as f:
        headers = ["checksum","path","name","ext","size_bytes","duration_sec","project","year"]
        w = csv.DictWriter(f, fieldnames=headers); w.writeheader()
        for r in rows: w.writerow({k:r.get(k,"") for k in headers})
    # YAML
    yaml_path.write_text(yaml.safe_dump({"audio_files": rows}, sort_keys=False))
    console.print(f"[green]Exported library:[/green] {csv_path} / {yaml_path}")
    speak("Library export complete.")
    save_vscode()

# Distribution staging
def stage_release(title: str, out_folder: Path):
    out_folder = out_folder.expanduser().resolve()
    out_folder.mkdir(parents=True, exist_ok=True)
    # Gather likely assets: masters, artwork, metadata
    assets = []
    for cand in ["Masters","Mixdowns","Artwork","Docs"]:
        p = ROOT / cand
        if p.exists(): assets.append(p)
    for a in assets:
        dest = out_folder / a.name
        if a.is_dir():
            # shallow copy
            (dest).mkdir(exist_ok=True)
            for f in a.glob("*"):
                if f.is_file(): shutil.copy2(f, dest / f.name)
        else:
            shutil.copy2(a, dest)
    # Write basic README
    readme = out_folder / "README.md"
    readme.write_text(f"# Release: {title}\n\nAssembled on {datetime.utcnow().isoformat()}.\n")
    console.print(f"[green]Release staged in {out_folder}[/green]")
    speak(f"Release staged: {title}.")
    save_vscode()

# Legacy pack bundling
def build_legacy_pack(year: int, out_zip: Path):
    out_zip = out_zip.expanduser().resolve()
    tmp_dir = ROOT / f"Legacy_{year}"
    tmp_dir.mkdir(exist_ok=True)
    # Include configs, library index, snapshots
    for src in [CFG_FILE, CSV_OUT, YAML_OUT]:
        if Path(src).exists():
            shutil.copy2(src, tmp_dir / Path(src).name)
    if SNAP_DIR.exists():
        (tmp_dir / "snapshots").mkdir(exist_ok=True)
        for s in SNAP_DIR.glob("*.yaml"):
            shutil.copy2(s, tmp_dir / "snapshots" / s.name)
    # Zip it
    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for p in tmp_dir.rglob("*"):
            z.write(p, p.relative_to(tmp_dir))
    console.print(f"[green]Legacy pack written:[/green] {out_zip}")
    speak(f"Legacy pack sealed for {year}.")
    save_vscode()

# CLI
@click.group()
def cli():
    ensure_dirs()

@cli.command()
def init():
    """Initialize config and VS Code cockpit."""
    load_cfg()
    write_vscode_files()
    console.print("[green]Initialized config and cockpit[/green]")
    speak("Initialization complete.")

@cli.command()
def identity():
    """Audit + enforce identity."""
    identity_audit()
    identity_lockdown()

@cli.command()
@click.argument("service")
@click.argument("codes")
def vault(service: str, codes: str):
    """Store 2FA recovery codes in encrypted vault."""
    vault_add(service, codes)
    console.print("[green]Codes stored in vault[/green]")
    speak("Codes stored securely.")

@cli.command()
def cockpit():
    """Write VS Code tasks/keybindings."""
    write_vscode_files()

@cli.command()
def snapshot():
    """Snapshot the digital landscape config."""
    snapshot_cfg()

@cli.command()
@click.argument("message", required=False, default="Noizy Fish commit")
def commit(message: str):
    """Git add/commit."""
    git_commit(message)

@cli.command()
@click.option("--paths", multiple=True, default=["~/Music"], help="Paths to scan")
def scan(paths: Tuple[str,...]):
    """Scan audio files across paths."""
    count = scan_paths([Path(p) for p in paths])
    console.print(f"[green]{count} files scanned[/green]")

@cli.command()
@click.option("--csv", "csv_path", default=str(CSV_OUT))
@click.option("--yaml", "yaml_path", default=str(YAML_OUT))
def assemble(csv_path: str, yaml_path: str):
    """Deduplicate and export library."""
    total, unique = dedupe_scan()
    export_library(Path(csv_path), Path(yaml_path))
    console.print(f"[green]Assembled library: {unique} unique of {total} scanned[/green]")

@cli.command()
@click.option("--title", required=True)
@click.option("--folder", "folder", default="Release")
def distribute(title: str, folder: str):
    """Stage a release folder with assets and README."""
    stage_release(title, ROOT / folder)

@cli.command()
@click.option("--year", type=int, required=True)
@click.option("--out", "out_zip", default="LegacyPack.zip")
def legacy(year: int, out_zip: str):
    """Build a legacy pack zip."""
    build_legacy_pack(year, ROOT / out_zip)

@cli.command()
def status():
    """Show identity audit + library summary."""
    identity_audit()
    if YAML_OUT.exists():
        data = yaml.safe_load(YAML_OUT.read_text()).get("audio_files", [])
        console.print(f"[green]Library entries:[/green] {len(data)}")
    else:
        console.print("[yellow]Library not assembled yet[/yellow]")

@cli.command()
def ignition():
    """Run the full leap sequence end-to-end."""
    console.print("[green]Ignition: starting quantum leap[/green]")
    speak("Ignition. Starting quantum leap.")
    write_vscode_files()
    identity_lockdown()
    snapshot_cfg()
    scan_paths([Path("~/Music"), Path("/Volumes/Archive1"), Path("/Volumes/Archive2")])
    dedupe_scan()
    export_library()
    git_commit("Identity + Library assembled")
    console.print("[green]Ignition complete[/green]")
    speak("Ignition complete. All systems go.")

if __name__ == "__main__":
    cli()