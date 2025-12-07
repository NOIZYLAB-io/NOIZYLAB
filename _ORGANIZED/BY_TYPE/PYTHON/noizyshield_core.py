"""
NoizyOS Ultra — NoizyShield Core
================================
Central security controller for threat detection and system hardening.
Analyzes system behavior, detects anomalies, raises alerts.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from collections import defaultdict

# Threat log
THREATS: List[Dict[str, Any]] = []

# Failed login tracking (IP -> count)
FAILED_LOGINS: Dict[str, Dict] = defaultdict(lambda: {"count": 0, "first": None, "last": None})

# Blocked IPs
BLOCKED_IPS: set = set()

# Rate limiting
REQUEST_COUNTS: Dict[str, List[datetime]] = defaultdict(list)

# Thresholds
MAX_FAILED_LOGINS = 5
FAILED_LOGIN_WINDOW = 300  # 5 minutes
RATE_LIMIT_WINDOW = 60  # 1 minute
RATE_LIMIT_MAX = 100  # requests per minute


def log_failed_login(ip: str) -> Dict[str, Any]:
    """
    Log a failed login attempt from an IP.
    Returns block status if threshold exceeded.
    """
    now = datetime.now()
    
    entry = FAILED_LOGINS[ip]
    entry["count"] += 1
    entry["last"] = now.isoformat()
    
    if not entry["first"]:
        entry["first"] = now.isoformat()
    
    # Check if should block
    if entry["count"] >= MAX_FAILED_LOGINS:
        first_attempt = datetime.fromisoformat(entry["first"])
        if (now - first_attempt).seconds <= FAILED_LOGIN_WINDOW:
            BLOCKED_IPS.add(ip)
            log_threat("brute_force", f"IP {ip} blocked after {entry['count']} failed logins", ip)
            return {"blocked": True, "ip": ip}
    
    return {"blocked": False, "attempts": entry["count"]}


def check_brute_force(ip: str) -> bool:
    """Check if an IP is blocked for brute force."""
    return ip in BLOCKED_IPS


def unblock_ip(ip: str) -> bool:
    """Unblock an IP address."""
    if ip in BLOCKED_IPS:
        BLOCKED_IPS.remove(ip)
        FAILED_LOGINS[ip] = {"count": 0, "first": None, "last": None}
        return True
    return False


def log_threat(threat_type: str, description: str, source: str = "unknown") -> None:
    """Log a security threat."""
    THREATS.append({
        "type": threat_type,
        "description": description,
        "source": source,
        "timestamp": datetime.now().isoformat(),
        "severity": get_severity(threat_type)
    })
    
    # Keep only last 1000 threats
    if len(THREATS) > 1000:
        THREATS.pop(0)


def get_severity(threat_type: str) -> str:
    """Get severity level for a threat type."""
    high_severity = ["brute_force", "malware", "data_exfil", "crypto_miner"]
    medium_severity = ["unusual_traffic", "memory_exhaustion", "suspicious_process"]
    
    if threat_type in high_severity:
        return "high"
    elif threat_type in medium_severity:
        return "medium"
    return "low"


def evaluate_threats(stats: Dict[str, Any]) -> List[str]:
    """
    Analyze system stats for security threats.
    
    Args:
        stats: Dict with cpu_usage, ram_usage, network_out, user_active, etc.
    
    Returns:
        List of threat descriptions
    """
    alerts = []
    
    cpu = stats.get("cpu_usage", 0) or 0
    ram = stats.get("ram_usage", 0) or 0
    network_out = stats.get("network_out", 0) or 0
    network_in = stats.get("network_in", 0) or 0
    user_active = stats.get("user_active", True)
    processes = stats.get("processes", [])
    
    # ========================================
    # HIGH CPU WITH NO USER ACTIVITY
    # ========================================
    if cpu > 90 and not user_active:
        alert = "🔴 Possible crypto miner or malicious background process (high CPU, no user)"
        alerts.append(alert)
        log_threat("crypto_miner", alert, "system_stats")
    
    # ========================================
    # UNUSUAL OUTBOUND TRAFFIC
    # ========================================
    if network_out > 10_000_000:  # > 10 MB/s
        alert = "🟠 Unusual outbound traffic detected (possible data exfiltration)"
        alerts.append(alert)
        log_threat("data_exfil", alert, "network")
    
    # ========================================
    # UNUSUAL INBOUND TRAFFIC
    # ========================================
    if network_in > 50_000_000:  # > 50 MB/s
        alert = "🟠 High inbound traffic (possible attack or unauthorized download)"
        alerts.append(alert)
        log_threat("unusual_traffic", alert, "network")
    
    # ========================================
    # MEMORY EXHAUSTION
    # ========================================
    if ram > 95:
        alert = "🟡 Memory exhaustion risk (RAM > 95%)"
        alerts.append(alert)
        log_threat("memory_exhaustion", alert, "system_stats")
    
    # ========================================
    # SUSPICIOUS PROCESSES (if provided)
    # ========================================
    suspicious_names = ["miner", "cryptonight", "xmrig", "coinhive", "backdoor"]
    for proc in processes:
        proc_name = proc.get("name", "").lower()
        if any(sus in proc_name for sus in suspicious_names):
            alert = f"🔴 Suspicious process detected: {proc.get('name')}"
            alerts.append(alert)
            log_threat("malware", alert, "process_scan")
    
    # ========================================
    # RAPID CPU SPIKES
    # ========================================
    if cpu > 85 and stats.get("cpu_spike", False):
        alert = "🟡 Rapid CPU spike detected"
        alerts.append(alert)
        log_threat("suspicious_process", alert, "system_stats")
    
    return alerts


def get_threat_level() -> str:
    """
    Get current overall threat level.
    Based on recent threats.
    """
    if not THREATS:
        return "safe"
    
    # Check last hour
    one_hour_ago = datetime.now() - timedelta(hours=1)
    recent = [
        t for t in THREATS 
        if datetime.fromisoformat(t["timestamp"]) > one_hour_ago
    ]
    
    high_count = sum(1 for t in recent if t["severity"] == "high")
    medium_count = sum(1 for t in recent if t["severity"] == "medium")
    
    if high_count > 0:
        return "critical"
    elif medium_count >= 3:
        return "elevated"
    elif medium_count > 0 or len(recent) > 5:
        return "guarded"
    
    return "safe"


def get_recent_threats(limit: int = 20) -> List[Dict]:
    """Get recent threats."""
    return THREATS[-limit:][::-1]  # Most recent first


def get_blocked_ips() -> List[str]:
    """Get list of blocked IPs."""
    return list(BLOCKED_IPS)


def check_rate_limit(ip: str) -> bool:
    """
    Check if an IP has exceeded rate limit.
    Returns True if blocked, False if allowed.
    """
    now = datetime.now()
    cutoff = now - timedelta(seconds=RATE_LIMIT_WINDOW)
    
    # Clean old entries
    REQUEST_COUNTS[ip] = [t for t in REQUEST_COUNTS[ip] if t > cutoff]
    
    # Check limit
    if len(REQUEST_COUNTS[ip]) >= RATE_LIMIT_MAX:
        return True
    
    # Log this request
    REQUEST_COUNTS[ip].append(now)
    return False

