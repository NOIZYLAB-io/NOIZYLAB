"""
NoizyMemory GEN-1 — Layer 2: Device Memory
==========================================
Tracks device specs, OS, performance issues, recurring failures.
Enables predictive diagnostics and pattern recognition.
"""

from datetime import datetime
from typing import Dict, Any, List, Optional

# In-memory store (replace with database in production)
DEVICE_MEMORY: Dict[str, Dict[str, Any]] = {}


def remember_device(email: str, device_info: Dict[str, Any]) -> bool:
    """
    Store device information for a client.
    
    Args:
        email: Client identifier
        device_info: Dict containing device specs (os, cpu, ram, disk, etc.)
    
    Returns:
        True if successful
    """
    if email not in DEVICE_MEMORY:
        DEVICE_MEMORY[email] = {
            "devices": [],
            "primary_device": None,
            "first_seen": datetime.now().isoformat()
        }
    
    # Add timestamp to device info
    device_info["recorded_at"] = datetime.now().isoformat()
    
    # Check if this device already exists (by device name or ID)
    device_id = device_info.get("device_name") or device_info.get("id")
    existing = None
    
    for i, d in enumerate(DEVICE_MEMORY[email]["devices"]):
        if d.get("device_name") == device_id or d.get("id") == device_id:
            existing = i
            break
    
    if existing is not None:
        # Update existing device
        DEVICE_MEMORY[email]["devices"][existing].update(device_info)
    else:
        # Add new device
        DEVICE_MEMORY[email]["devices"].append(device_info)
    
    # Set as primary if first device
    if not DEVICE_MEMORY[email]["primary_device"]:
        DEVICE_MEMORY[email]["primary_device"] = device_id
    
    DEVICE_MEMORY[email]["last_updated"] = datetime.now().isoformat()
    
    return True


def recall_device(email: str) -> Dict[str, Any]:
    """
    Retrieve all device information for a client.
    
    Args:
        email: Client identifier
    
    Returns:
        Dict of device data, or empty dict if not found
    """
    return DEVICE_MEMORY.get(email, {})


def update_device(email: str, device_id: str, updates: Dict[str, Any]) -> bool:
    """Update specific device fields."""
    if email not in DEVICE_MEMORY:
        return False
    
    for d in DEVICE_MEMORY[email]["devices"]:
        if d.get("device_name") == device_id or d.get("id") == device_id:
            d.update(updates)
            d["last_updated"] = datetime.now().isoformat()
            return True
    
    return False


def log_device_issue(email: str, device_id: str, issue: str) -> bool:
    """Log a device-specific issue for pattern tracking."""
    if email not in DEVICE_MEMORY:
        DEVICE_MEMORY[email] = {"devices": [], "issues": []}
    
    if "issues" not in DEVICE_MEMORY[email]:
        DEVICE_MEMORY[email]["issues"] = []
    
    DEVICE_MEMORY[email]["issues"].append({
        "device_id": device_id,
        "issue": issue,
        "timestamp": datetime.now().isoformat()
    })
    
    return True


def get_device_issues(email: str, device_id: Optional[str] = None) -> List[Dict]:
    """Get issues for a specific device or all devices."""
    if email not in DEVICE_MEMORY:
        return []
    
    issues = DEVICE_MEMORY[email].get("issues", [])
    
    if device_id:
        return [i for i in issues if i.get("device_id") == device_id]
    
    return issues


def get_recurring_device_problems(email: str) -> Dict[str, int]:
    """Identify recurring device problems."""
    issues = get_device_issues(email)
    problem_counts = {}
    
    for issue in issues:
        problem = issue.get("issue", "unknown")
        problem_counts[problem] = problem_counts.get(problem, 0) + 1
    
    # Return only problems that occurred more than once
    return {k: v for k, v in problem_counts.items() if v > 1}


def get_primary_device(email: str) -> Optional[Dict]:
    """Get the client's primary device info."""
    if email not in DEVICE_MEMORY:
        return None
    
    primary_id = DEVICE_MEMORY[email].get("primary_device")
    if not primary_id:
        return None
    
    for d in DEVICE_MEMORY[email].get("devices", []):
        if d.get("device_name") == primary_id or d.get("id") == primary_id:
            return d
    
    return None

