"""MirrorMind - Version Control for AI State"""
import json
import hashlib
from datetime import datetime
from .backup import list_backups, restore_backup

VERSION_HISTORY = []

def create_version(state, message="Auto-save"):
    """Create a new version"""
    state_str = json.dumps(state, sort_keys=True, default=str)
    version_hash = hashlib.sha256(state_str.encode()).hexdigest()[:12]
    
    version = {
        "hash": version_hash,
        "message": message,
        "created_at": datetime.now().isoformat(),
        "parent": VERSION_HISTORY[-1]["hash"] if VERSION_HISTORY else None,
        "size": len(state_str),
    }
    
    VERSION_HISTORY.append(version)
    
    return version

def get_versions(limit=20):
    """Get version history"""
    return VERSION_HISTORY[-limit:][::-1]

def compare_versions(version_a, version_b):
    """Compare two versions"""
    backups = list_backups()
    
    state_a = None
    state_b = None
    
    for backup in backups:
        result = restore_backup(backup["id"])
        if "error" not in result:
            state_hash = hashlib.sha256(
                json.dumps(result["state"], sort_keys=True, default=str).encode()
            ).hexdigest()[:12]
            
            if state_hash == version_a:
                state_a = result["state"]
            if state_hash == version_b:
                state_b = result["state"]
    
    if not state_a or not state_b:
        return {"error": "Version not found"}
    
    return diff_states(state_a, state_b)

def diff_states(state_a, state_b):
    """Calculate difference between two states"""
    diff = {
        "added": [],
        "removed": [],
        "changed": [],
    }
    
    keys_a = set(state_a.keys()) if isinstance(state_a, dict) else set()
    keys_b = set(state_b.keys()) if isinstance(state_b, dict) else set()
    
    diff["added"] = list(keys_b - keys_a)
    diff["removed"] = list(keys_a - keys_b)
    
    for key in keys_a & keys_b:
        if state_a[key] != state_b[key]:
            diff["changed"].append(key)
    
    return diff

def get_version_by_hash(version_hash):
    """Get a specific version by hash"""
    for version in VERSION_HISTORY:
        if version["hash"] == version_hash:
            return version
    return None

def tag_version(version_hash, tag_name):
    """Tag a version for easy reference"""
    version = get_version_by_hash(version_hash)
    if version:
        version["tag"] = tag_name
        return {"tagged": True, "hash": version_hash, "tag": tag_name}
    return {"error": "Version not found"}

def get_tagged_versions():
    """Get all tagged versions"""
    return [v for v in VERSION_HISTORY if v.get("tag")]

