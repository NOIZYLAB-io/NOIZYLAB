"""
NoizyShield+ Behavioral Anomaly Detector
========================================
Watches system like a hawk for unusual patterns.
ML-driven anomaly detection integrated with NoizyMind.
"""

from typing import Dict, List, Optional
from datetime import datetime
import statistics


# Baseline metrics (learned over time)
BASELINES: Dict[str, Dict] = {}

# Anomaly history
ANOMALY_LOG: List[Dict] = []


def detect_anomaly(state: Dict) -> List[Dict]:
    """
    Detect behavioral anomalies in system state.
    
    State includes:
    - cpu: CPU usage %
    - ram: RAM usage %
    - gpu: GPU usage %
    - disk_io: disk I/O rate
    - network_io: network I/O rate
    - user_active: bool
    - ai_job_active: bool
    - processes: number of processes
    """
    cpu = state.get("cpu", 0)
    ram = state.get("ram", 0)
    gpu = state.get("gpu", 0)
    disk_io = state.get("disk_io", 0)
    network_io = state.get("network_io", 0)
    user_active = state.get("user_active", True)
    ai_job_active = state.get("ai_job_active", False)
    processes = state.get("processes", 0)
    
    anomalies = []
    
    # High CPU while idle
    if cpu > 85 and not user_active:
        anomalies.append({
            "type": "cpu_idle_spike",
            "severity": "high",
            "detail": f"CPU at {cpu}% while user idle",
            "metric": "cpu",
            "value": cpu,
        })
    
    # RAM exhaustion
    if ram > 95:
        anomalies.append({
            "type": "ram_exhaustion",
            "severity": "critical",
            "detail": f"RAM at {ram}% - system may become unstable",
            "metric": "ram",
            "value": ram,
        })
    
    # GPU without known job
    if gpu > 80 and not ai_job_active:
        anomalies.append({
            "type": "gpu_unknown_load",
            "severity": "medium",
            "detail": f"GPU at {gpu}% without active AI job",
            "metric": "gpu",
            "value": gpu,
        })
    
    # Unusual disk activity
    baseline_disk = BASELINES.get("disk_io", {}).get("avg", 1000)
    if disk_io > baseline_disk * 5:
        anomalies.append({
            "type": "disk_spike",
            "severity": "medium",
            "detail": f"Disk I/O {disk_io} is 5x above baseline",
            "metric": "disk_io",
            "value": disk_io,
        })
    
    # Unusual network activity
    baseline_net = BASELINES.get("network_io", {}).get("avg", 1000)
    if network_io > baseline_net * 10:
        anomalies.append({
            "type": "network_spike",
            "severity": "high",
            "detail": f"Network I/O {network_io} is 10x above baseline",
            "metric": "network_io",
            "value": network_io,
        })
    
    # Process explosion
    baseline_procs = BASELINES.get("processes", {}).get("avg", 200)
    if processes > baseline_procs * 2:
        anomalies.append({
            "type": "process_explosion",
            "severity": "medium",
            "detail": f"{processes} processes running (2x baseline)",
            "metric": "processes",
            "value": processes,
        })
    
    # Log anomalies
    for a in anomalies:
        log_anomaly(a)
    
    return anomalies


def detect_behavior_pattern(actions: List[str]) -> Optional[Dict]:
    """
    Detect suspicious behavior patterns from action sequences.
    """
    suspicious_patterns = [
        # Ransomware-like behavior
        (["file_enumerate", "file_read", "file_encrypt"], "ransomware_pattern"),
        # Data exfiltration
        (["file_read", "file_read", "network_upload"], "data_exfil"),
        # Privilege escalation attempt
        (["auth_fail", "auth_fail", "auth_fail"], "brute_force"),
        # Reconnaissance
        (["port_scan", "service_probe"], "recon_activity"),
    ]
    
    for pattern, name in suspicious_patterns:
        if all(p in actions for p in pattern):
            return {
                "type": name,
                "severity": "critical",
                "detail": f"Detected {name} behavior pattern",
                "matched": pattern,
            }
    
    return None


def update_baseline(metric: str, value: float) -> None:
    """
    Update baseline statistics for a metric.
    """
    if metric not in BASELINES:
        BASELINES[metric] = {"values": [], "avg": value, "std": 0}
    
    baseline = BASELINES[metric]
    baseline["values"].append(value)
    
    # Keep last 1000 values
    if len(baseline["values"]) > 1000:
        baseline["values"] = baseline["values"][-500:]
    
    # Recalculate stats
    if len(baseline["values"]) >= 10:
        baseline["avg"] = statistics.mean(baseline["values"])
        baseline["std"] = statistics.stdev(baseline["values"])


def log_anomaly(anomaly: Dict) -> Dict:
    """
    Log an anomaly detection.
    """
    entry = {
        **anomaly,
        "timestamp": datetime.now().isoformat(),
        "id": len(ANOMALY_LOG),
    }
    ANOMALY_LOG.append(entry)
    
    # Trim log
    if len(ANOMALY_LOG) > 1000:
        ANOMALY_LOG[:] = ANOMALY_LOG[-500:]
    
    return entry


def get_anomaly_log(limit: int = 50) -> List[Dict]:
    """
    Get recent anomaly log.
    """
    return ANOMALY_LOG[-limit:]


def get_anomaly_summary() -> Dict:
    """
    Get summary of recent anomalies.
    """
    recent = ANOMALY_LOG[-100:]
    
    by_type = {}
    by_severity = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    
    for a in recent:
        t = a.get("type", "unknown")
        s = a.get("severity", "low")
        by_type[t] = by_type.get(t, 0) + 1
        by_severity[s] = by_severity.get(s, 0) + 1
    
    return {
        "total": len(recent),
        "by_type": by_type,
        "by_severity": by_severity,
    }


def is_anomalous(metric: str, value: float, threshold: float = 3.0) -> bool:
    """
    Check if a value is anomalous based on baseline.
    Uses standard deviation threshold.
    """
    baseline = BASELINES.get(metric)
    if not baseline or baseline["std"] == 0:
        return False
    
    z_score = abs(value - baseline["avg"]) / baseline["std"]
    return z_score > threshold

