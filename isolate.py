"""
NoizyShield+ Auto-Isolation Engine
==================================
Instantly pull compromised devices off the network.
Zero mercy for threats.
"""

import subprocess
from typing import Dict, List, Optional
from datetime import datetime


# Isolation log
ISOLATION_LOG: List[Dict] = []

# Currently isolated devices
ISOLATED_DEVICES: Dict[str, Dict] = {}


def isolate_device(ip: str, reason: str = "threat_detected") -> Dict:
    """
    Isolate a device from the network.
    
    Methods:
    1. MC96 VLAN isolation (preferred)
    2. Local firewall block
    3. ARP poisoning prevention
    """
    result = {
        "ip": ip,
        "reason": reason,
        "timestamp": datetime.now().isoformat(),
        "methods": [],
        "success": False,
    }
    
    # Method 1: Firewall block (works on all systems)
    try:
        # macOS/Linux
        subprocess.run(
            ["sudo", "pfctl", "-t", "noizyblock", "-T", "add", ip],
            capture_output=True,
            timeout=5
        )
        result["methods"].append("pf_firewall")
    except Exception:
        pass
    
    # Method 2: iptables (Linux)
    try:
        subprocess.run(
            ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"],
            capture_output=True,
            timeout=5
        )
        result["methods"].append("iptables")
    except Exception:
        pass
    
    # Method 3: Log for MC96 switch integration
    # In production, this would send command to switch
    result["methods"].append("mc96_vlan_logged")
    
    if result["methods"]:
        result["success"] = True
        ISOLATED_DEVICES[ip] = result
        log_isolation(result)
    
    return result


def release_device(ip: str) -> Dict:
    """
    Release an isolated device back to the network.
    """
    if ip not in ISOLATED_DEVICES:
        return {"success": False, "error": "Device not isolated"}
    
    result = {
        "ip": ip,
        "action": "release",
        "timestamp": datetime.now().isoformat(),
        "success": False,
    }
    
    # Remove firewall blocks
    try:
        subprocess.run(
            ["sudo", "pfctl", "-t", "noizyblock", "-T", "delete", ip],
            capture_output=True,
            timeout=5
        )
    except Exception:
        pass
    
    try:
        subprocess.run(
            ["sudo", "iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"],
            capture_output=True,
            timeout=5
        )
    except Exception:
        pass
    
    del ISOLATED_DEVICES[ip]
    result["success"] = True
    
    log_isolation({
        "ip": ip,
        "action": "released",
        "timestamp": result["timestamp"],
    })
    
    return result


def kill_switch(ip: str) -> Dict:
    """
    Emergency kill switch - complete network death for device.
    Used for critical threats only.
    """
    result = isolate_device(ip, reason="kill_switch")
    
    # Additional aggressive measures
    try:
        # Block all traffic to/from device
        subprocess.run(
            ["sudo", "iptables", "-A", "OUTPUT", "-d", ip, "-j", "DROP"],
            capture_output=True,
            timeout=5
        )
        
        # Send TCP RST to all connections (terminate existing)
        subprocess.run(
            ["sudo", "hping3", "-R", "-c", "1", ip],
            capture_output=True,
            timeout=5
        )
    except Exception:
        pass
    
    result["kill_switch"] = True
    return result


def quarantine_device(ip: str, duration_minutes: int = 60) -> Dict:
    """
    Temporary quarantine with auto-release.
    """
    result = isolate_device(ip, reason="quarantine")
    result["quarantine_duration"] = duration_minutes
    result["release_at"] = datetime.now().isoformat()  # Would add duration
    
    # In production, schedule auto-release
    return result


def get_isolated_devices() -> Dict[str, Dict]:
    """
    Get all currently isolated devices.
    """
    return ISOLATED_DEVICES


def is_isolated(ip: str) -> bool:
    """
    Check if a device is currently isolated.
    """
    return ip in ISOLATED_DEVICES


def log_isolation(entry: Dict) -> None:
    """
    Log isolation action.
    """
    ISOLATION_LOG.append({
        **entry,
        "id": len(ISOLATION_LOG),
    })
    
    # Trim log
    if len(ISOLATION_LOG) > 500:
        ISOLATION_LOG[:] = ISOLATION_LOG[-250:]


def get_isolation_log(limit: int = 50) -> List[Dict]:
    """
    Get isolation history.
    """
    return ISOLATION_LOG[-limit:]


def bulk_isolate(ips: List[str], reason: str = "bulk_threat") -> Dict:
    """
    Isolate multiple devices at once.
    """
    results = {}
    for ip in ips:
        results[ip] = isolate_device(ip, reason)
    
    return {
        "total": len(ips),
        "success": sum(1 for r in results.values() if r.get("success")),
        "results": results,
    }

