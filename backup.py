"""MirrorMind - Backup System"""
import os
import json
import hashlib
from datetime import datetime

BACKUP_DIR = "/Users/m2ultra/NOIZYLAB/noizyOS_v2/backups/mirrormind"
BACKUP_INDEX = {}

def ensure_backup_dir():
    os.makedirs(BACKUP_DIR, exist_ok=True)

def create_backup(state_data, backup_type="full"):
    """Create a backup of AI state"""
    ensure_backup_dir()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_id = f"backup_{timestamp}_{backup_type}"
    
    # Calculate checksum
    data_str = json.dumps(state_data, sort_keys=True, default=str)
    checksum = hashlib.sha256(data_str.encode()).hexdigest()
    
    backup = {
        "id": backup_id,
        "type": backup_type,
        "created_at": datetime.now().isoformat(),
        "checksum": checksum,
        "size_bytes": len(data_str),
        "state": state_data,
    }
    
    # Save to file
    backup_path = os.path.join(BACKUP_DIR, f"{backup_id}.json")
    with open(backup_path, "w") as f:
        json.dump(backup, f, indent=2, default=str)
    
    BACKUP_INDEX[backup_id] = {
        "path": backup_path,
        "type": backup_type,
        "created_at": backup["created_at"],
        "checksum": checksum,
    }
    
    return {"backup_id": backup_id, "checksum": checksum, "path": backup_path}

def restore_backup(backup_id):
    """Restore from a backup"""
    if backup_id not in BACKUP_INDEX:
        # Try to find on disk
        backup_path = os.path.join(BACKUP_DIR, f"{backup_id}.json")
        if not os.path.exists(backup_path):
            return {"error": "Backup not found"}
    else:
        backup_path = BACKUP_INDEX[backup_id]["path"]
    
    with open(backup_path, "r") as f:
        backup = json.load(f)
    
    # Verify checksum
    data_str = json.dumps(backup["state"], sort_keys=True, default=str)
    checksum = hashlib.sha256(data_str.encode()).hexdigest()
    
    if checksum != backup["checksum"]:
        return {"error": "Backup corrupted - checksum mismatch"}
    
    return {
        "restored": True,
        "backup_id": backup_id,
        "state": backup["state"],
        "original_date": backup["created_at"],
    }

def get_latest_backup(backup_type=None):
    """Get the most recent backup"""
    ensure_backup_dir()
    
    backups = []
    for filename in os.listdir(BACKUP_DIR):
        if filename.endswith(".json"):
            if backup_type and backup_type not in filename:
                continue
            path = os.path.join(BACKUP_DIR, filename)
            with open(path, "r") as f:
                backup = json.load(f)
                backups.append(backup)
    
    if not backups:
        return None
    
    return max(backups, key=lambda x: x["created_at"])

def list_backups():
    """List all available backups"""
    ensure_backup_dir()
    
    backups = []
    for filename in os.listdir(BACKUP_DIR):
        if filename.endswith(".json"):
            path = os.path.join(BACKUP_DIR, filename)
            stat = os.stat(path)
            backups.append({
                "id": filename.replace(".json", ""),
                "path": path,
                "size_bytes": stat.st_size,
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            })
    
    return sorted(backups, key=lambda x: x["modified"], reverse=True)

def delete_old_backups(keep_count=10):
    """Delete old backups, keeping the most recent ones"""
    backups = list_backups()
    
    if len(backups) <= keep_count:
        return {"deleted": 0}
    
    to_delete = backups[keep_count:]
    deleted = 0
    
    for backup in to_delete:
        try:
            os.remove(backup["path"])
            deleted += 1
        except:
            pass
    
    return {"deleted": deleted, "remaining": keep_count}

