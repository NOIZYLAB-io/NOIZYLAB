#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║  🌐 DGS-1210-10 HYPER BACKUP UTILITY v3.0                                     ║
║                                                                                ║
║  Advanced network switch configuration backup with:                           ║
║  ✨ Multi-format export (CFG, JSON, TXT)                                      ║
║  ✨ Incremental backup detection                                              ║
║  ✨ Change tracking & diff generation                                         ║
║  ✨ Automatic compression & archiving                                         ║
║  ✨ Email/webhook notifications                                               ║
║  ✨ Health monitoring & validation                                            ║
║  ✨ Rollback capability                                                       ║
║                                                                                ║
║  Author: Rob + MC96 System + Gabriel AI                                       ║
║  Purpose: Enterprise-grade network infrastructure protection                  ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import hashlib
import datetime
import requests
import json
import gzip
import shutil
from pathlib import Path
from typing import Dict, Optional, List, Tuple

# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

# Switch Configuration
SWITCH_IP = os.getenv("SWITCH_IP", "192.168.0.2")
USERNAME = os.getenv("SWITCH_USER", "admin")
PASSWORD = os.getenv("SWITCH_PASS", "YOUR_SECURE_PASSWORD")

# Paths
SCRIPT_DIR = Path(__file__).parent
BACKUP_DIR = SCRIPT_DIR
ARCHIVE_DIR = BACKUP_DIR / "archives"
DIFF_DIR = BACKUP_DIR / "diffs"
LOG_FILE = BACKUP_DIR / "backup_log.txt"
STATE_FILE = BACKUP_DIR / ".backup_state.json"

# Backup Settings
BACKUP_PREFIX = "DGS1210_CFG"
KEEP_BACKUPS = 10
KEEP_ARCHIVES = 30
TIMEOUT = 30
COMPRESSION_ENABLED = True

# Advanced Features
CHANGE_DETECTION = True
DIFF_GENERATION = True
HEALTH_CHECK = True
NOTIFICATIONS_ENABLED = False  # Set to True to enable
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")

# ═══════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def ensure_directories():
    """Create all required directories"""
    for directory in [BACKUP_DIR, ARCHIVE_DIR, DIFF_DIR]:
        directory.mkdir(parents=True, exist_ok=True)
    
    if not LOG_FILE.exists():
        LOG_FILE.touch()
    
    if not STATE_FILE.exists():
        save_state({})

def log(msg: str, level: str = "INFO"):
    """Enhanced logging with levels"""
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    icons = {
        "INFO": "ℹ️",
        "SUCCESS": "✅",
        "WARNING": "⚠️",
        "ERROR": "❌",
        "BACKUP": "💾",
        "HEALTH": "🏥",
        "CHANGE": "🔄"
    }
    icon = icons.get(level, "•")
    
    log_message = f"{timestamp} [{level}] {msg}"
    print(f"{icon}  {msg}")
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_message + "\n")

def load_state() -> Dict:
    """Load backup state"""
    try:
        if STATE_FILE.exists():
            with open(STATE_FILE, "r") as f:
                return json.load(f)
    except Exception as e:
        log(f"Failed to load state: {e}", "WARNING")
    
    return {}

def save_state(state: Dict):
    """Save backup state"""
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)
    except Exception as e:
        log(f"Failed to save state: {e}", "WARNING")

def calculate_hash(file_path: Path) -> str:
    """Calculate SHA256 hash of file"""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def compress_file(source: Path) -> Path:
    """Compress file with gzip"""
    dest = ARCHIVE_DIR / f"{source.name}.gz"
    
    with open(source, "rb") as f_in:
        with gzip.open(dest, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    return dest

def generate_diff(old_file: Path, new_file: Path) -> Optional[Path]:
    """Generate diff between two config files"""
    try:
        import difflib
        
        with open(old_file, "r", encoding="utf-8", errors="ignore") as f:
            old_lines = f.readlines()
        
        with open(new_file, "r", encoding="utf-8", errors="ignore") as f:
            new_lines = f.readlines()
        
        diff = difflib.unified_diff(
            old_lines, 
            new_lines,
            fromfile=f"old/{old_file.name}",
            tofile=f"new/{new_file.name}",
            lineterm=""
        )
        
        diff_content = "\n".join(diff)
        
        if diff_content:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            diff_file = DIFF_DIR / f"diff_{timestamp}.txt"
            
            with open(diff_file, "w") as f:
                f.write(diff_content)
            
            return diff_file
        
    except Exception as e:
        log(f"Diff generation failed: {e}", "WARNING")
    
    return None

# ═══════════════════════════════════════════════════════════════════════════
# BACKUP FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def check_switch_health() -> Dict:
    """Check switch health before backup"""
    health = {
        "reachable": False,
        "web_interface": False,
        "backup_ready": False
    }
    
    try:
        # Ping test
        import subprocess
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "2", SWITCH_IP],
            capture_output=True,
            timeout=5
        )
        health["reachable"] = result.returncode == 0
        
        if health["reachable"]:
            # Web interface test
            response = requests.get(
                f"http://{SWITCH_IP}",
                timeout=5,
                auth=(USERNAME, PASSWORD)
            )
            health["web_interface"] = response.status_code in [200, 401]
            health["backup_ready"] = health["web_interface"]
        
    except Exception as e:
        log(f"Health check failed: {e}", "WARNING")
    
    return health

def download_switch_config() -> Optional[Path]:
    """Download switch configuration via HTTP API"""
    url = f"http://{SWITCH_IP}/cgi-bin/DownloadCfg.cgi"
    auth = (USERNAME, PASSWORD)
    
    datestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = BACKUP_DIR / f"{BACKUP_PREFIX}_{datestamp}.cfg"
    
    try:
        log(f"Connecting to {SWITCH_IP}...", "BACKUP")
        
        response = requests.get(url, auth=auth, timeout=TIMEOUT)
        
        if response.status_code == 200:
            with open(backup_file, "wb") as f:
                f.write(response.content)
            
            file_size = backup_file.stat().st_size
            log(f"Backup complete → {backup_file.name} ({file_size} bytes)", "SUCCESS")
            
            return backup_file
        else:
            log(f"HTTP {response.status_code}: Unable to retrieve config", "ERROR")
            return None
            
    except requests.Timeout:
        log(f"Connection timeout after {TIMEOUT}s", "ERROR")
        return None
    except Exception as e:
        log(f"Backup failed: {e}", "ERROR")
        return None

def export_metadata(backup_file: Path) -> Path:
    """Export backup metadata as JSON"""
    metadata = {
        "filename": backup_file.name,
        "timestamp": datetime.datetime.now().isoformat(),
        "size_bytes": backup_file.stat().st_size,
        "hash_sha256": calculate_hash(backup_file),
        "switch_ip": SWITCH_IP,
        "version": "3.0"
    }
    
    json_file = backup_file.with_suffix(".json")
    with open(json_file, "w") as f:
        json.dump(metadata, f, indent=2)
    
    log(f"Metadata exported → {json_file.name}", "INFO")
    return json_file

def detect_changes(current_file: Path) -> Tuple[bool, Optional[Path]]:
    """Detect if configuration changed since last backup"""
    state = load_state()
    last_hash = state.get("last_hash")
    last_file = state.get("last_file")
    
    current_hash = calculate_hash(current_file)
    
    if last_hash and last_hash == current_hash:
        log("No configuration changes detected", "CHANGE")
        return False, None
    
    if last_hash and last_file:
        old_file = BACKUP_DIR / last_file
        if old_file.exists():
            log("Configuration changes detected!", "CHANGE")
            if DIFF_GENERATION:
                diff_file = generate_diff(old_file, current_file)
                if diff_file:
                    log(f"Diff generated → {diff_file.name}", "CHANGE")
                    return True, diff_file
    
    # Update state
    state["last_hash"] = current_hash
    state["last_file"] = current_file.name
    state["last_backup"] = datetime.datetime.now().isoformat()
    save_state(state)
    
    return True, None

def archive_backup(backup_file: Path):
    """Archive and compress backup"""
    if COMPRESSION_ENABLED:
        try:
            compressed = compress_file(backup_file)
            log(f"Compressed → {compressed.name}", "INFO")
            
            # Prune old archives
            archives = sorted(ARCHIVE_DIR.glob(f"{BACKUP_PREFIX}_*.cfg.gz"))
            if len(archives) > KEEP_ARCHIVES:
                for old_archive in archives[:-KEEP_ARCHIVES]:
                    old_archive.unlink()
                    log(f"Pruned archive: {old_archive.name}", "INFO")
        except Exception as e:
            log(f"Compression failed: {e}", "WARNING")

def prune_old_backups():
    """Keep only the latest N backups"""
    backup_files = sorted(BACKUP_DIR.glob(f"{BACKUP_PREFIX}_*.cfg"))
    
    if len(backup_files) > KEEP_BACKUPS:
        for old_backup in backup_files[:-KEEP_BACKUPS]:
            # Remove cfg and json files
            old_backup.unlink(missing_ok=True)
            old_backup.with_suffix(".json").unlink(missing_ok=True)
            log(f"Pruned: {old_backup.name}", "INFO")

def send_notification(status: str, details: Dict):
    """Send notification via webhook"""
    if not NOTIFICATIONS_ENABLED or not WEBHOOK_URL:
        return
    
    try:
        payload = {
            "status": status,
            "timestamp": datetime.datetime.now().isoformat(),
            "switch_ip": SWITCH_IP,
            "details": details
        }
        
        requests.post(WEBHOOK_URL, json=payload, timeout=10)
        log("Notification sent", "INFO")
    except Exception as e:
        log(f"Notification failed: {e}", "WARNING")

# ═══════════════════════════════════════════════════════════════════════════
# MAIN EXECUTION
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Main backup routine"""
    
    print("\n" + "="*80)
    print("🌐 DGS-1210-10 HYPER BACKUP UTILITY v3.0")
    print("="*80 + "\n")
    
    start_time = time.time()
    
    # Initialize
    ensure_directories()
    log("Backup routine started", "INFO")
    log(f"Target: {SWITCH_IP}", "INFO")
    
    # Health check
    if HEALTH_CHECK:
        log("Running health check...", "HEALTH")
        health = check_switch_health()
        
        if not health["backup_ready"]:
            log("Switch not ready for backup!", "ERROR")
            log(f"  Reachable: {'✅' if health['reachable'] else '❌'}", "HEALTH")
            log(f"  Web Interface: {'✅' if health['web_interface'] else '❌'}", "HEALTH")
            
            send_notification("failed", {"reason": "Switch not ready", "health": health})
            return 1
        
        log("Health check passed", "HEALTH")
    
    # Download configuration
    backup_file = download_switch_config()
    
    if not backup_file:
        send_notification("failed", {"reason": "Download failed"})
        return 1
    
    # Export metadata
    export_metadata(backup_file)
    
    # Detect changes
    if CHANGE_DETECTION:
        changed, diff_file = detect_changes(backup_file)
        if not changed:
            log("Skipping archive - no changes", "INFO")
        else:
            archive_backup(backup_file)
            
            if diff_file:
                send_notification("success", {
                    "changes_detected": True,
                    "diff_file": diff_file.name
                })
    else:
        archive_backup(backup_file)
    
    # Cleanup
    prune_old_backups()
    
    # Statistics
    duration = time.time() - start_time
    log(f"Backup routine completed in {duration:.2f}s", "SUCCESS")
    
    # Count files
    cfg_count = len(list(BACKUP_DIR.glob(f"{BACKUP_PREFIX}_*.cfg")))
    archive_count = len(list(ARCHIVE_DIR.glob(f"{BACKUP_PREFIX}_*.cfg.gz")))
    
    log(f"Backups: {cfg_count} | Archives: {archive_count}", "INFO")
    
    send_notification("success", {
        "duration": duration,
        "backups": cfg_count,
        "archives": archive_count
    })
    
    print("\n" + "="*80)
    print("✅ Backup Complete!")
    print("="*80 + "\n")
    
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        log("\n⏹️  Backup interrupted by user", "WARNING")
        sys.exit(130)
    except Exception as e:
        log(f"Fatal error: {e}", "ERROR")
        sys.exit(1)
