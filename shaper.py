"""
NoizyNet Traffic Shaping Engine
===============================
Prioritizes traffic for AI processes, diagnostics,
client sessions, VR, compute jobs, and high-importance tasks.
"""

from typing import Dict, List, Optional
from datetime import datetime


# Traffic class priorities (lower = higher priority)
TRAFFIC_PRIORITIES = {
    # Real-time / Critical
    "vr_stream": 0,
    "audio_lowlatency": 1,
    "voice_call": 1,
    
    # Interactive
    "remote_support": 2,
    "remote_desktop": 2,
    "ssh": 2,
    
    # Important
    "diagnostics": 3,
    "ai_inference": 3,
    "compute_job": 3,
    
    # Normal
    "web_browse": 4,
    "api_request": 4,
    "general": 4,
    
    # Background
    "file_sync": 5,
    "backup": 5,
    "bulk_transfer": 5,
    
    # Low priority
    "update_check": 6,
    "telemetry": 6,
    "bulk_backup": 7,
}

# Bandwidth allocations (percentage of total)
BANDWIDTH_ALLOCATIONS = {
    0: 30,  # VR/audio gets 30%
    1: 20,  # Low latency
    2: 20,  # Interactive
    3: 15,  # Important
    4: 10,  # Normal
    5: 4,   # Background
    6: 1,   # Low priority
}

# Active shaping rules
ACTIVE_RULES: List[Dict] = []


def shape_traffic(packet_type: str) -> int:
    """
    Get priority order for a packet type.
    Lower number = higher priority.
    """
    return TRAFFIC_PRIORITIES.get(packet_type, 4)


def classify_traffic(packet: Dict) -> str:
    """
    Classify traffic type from packet metadata.
    """
    protocol = packet.get("protocol", "tcp").lower()
    port = packet.get("port", 0)
    size = packet.get("size", 0)
    
    # VR streaming (high-frequency UDP)
    if protocol == "udp" and port in range(7000, 8000):
        return "vr_stream"
    
    # Audio streaming
    if protocol == "udp" and port in [5004, 5005, 6000, 6001]:
        return "audio_lowlatency"
    
    # SSH
    if port == 22:
        return "ssh"
    
    # Remote desktop
    if port in [3389, 5900]:
        return "remote_desktop"
    
    # NoizyOS API
    if port == 8080:
        return "api_request"
    
    # Compute/Diagnostics
    if port == 8989:
        return "diagnostics"
    
    # Large transfers
    if size > 1000000:
        return "bulk_transfer"
    
    # Web traffic
    if port in [80, 443]:
        return "web_browse"
    
    return "general"


def get_bandwidth_allocation(priority: int) -> int:
    """
    Get bandwidth allocation percentage for priority level.
    """
    return BANDWIDTH_ALLOCATIONS.get(priority, 5)


def add_shaping_rule(rule: Dict) -> None:
    """
    Add a custom traffic shaping rule.
    
    Rule includes:
    - match: criteria to match (port, protocol, ip, etc.)
    - priority: priority level
    - bandwidth_limit: optional bandwidth cap
    - active: bool
    """
    rule["created"] = datetime.now().isoformat()
    ACTIVE_RULES.append(rule)


def remove_shaping_rule(rule_id: int) -> bool:
    """
    Remove a shaping rule by index.
    """
    if 0 <= rule_id < len(ACTIVE_RULES):
        ACTIVE_RULES.pop(rule_id)
        return True
    return False


def get_active_rules() -> List[Dict]:
    """
    Get all active shaping rules.
    """
    return ACTIVE_RULES


def apply_context_shaping(base_priority: int, context: Dict) -> int:
    """
    Adjust priority based on context.
    """
    adjusted = base_priority
    
    # Emergency mode boosts everything
    if context.get("flowState") == "emergency":
        adjusted = max(0, adjusted - 2)
    
    # VR active - boost real-time traffic
    if context.get("vr_active") and base_priority <= 2:
        adjusted = max(0, adjusted - 1)
    
    # High compute load - deprioritize background
    if context.get("compute_load", 0) > 80 and base_priority >= 5:
        adjusted = min(7, adjusted + 1)
    
    # Client session - boost support traffic
    if context.get("client_session") and base_priority == 2:
        adjusted = 1
    
    return adjusted


def get_qos_config() -> Dict:
    """
    Generate QoS configuration for network devices.
    """
    return {
        "queues": [
            {"id": 0, "name": "realtime", "weight": 50, "types": ["vr_stream", "audio_lowlatency"]},
            {"id": 1, "name": "interactive", "weight": 25, "types": ["remote_support", "ssh", "diagnostics"]},
            {"id": 2, "name": "normal", "weight": 15, "types": ["web_browse", "api_request", "general"]},
            {"id": 3, "name": "background", "weight": 10, "types": ["backup", "bulk_transfer", "update_check"]},
        ],
        "default_queue": 2,
        "strict_priority": [0],  # Queue 0 always first
    }


def estimate_latency(packet_type: str, current_load: int) -> int:
    """
    Estimate latency in ms for a packet type given current load.
    """
    base_latency = {
        "vr_stream": 1,
        "audio_lowlatency": 2,
        "remote_support": 5,
        "diagnostics": 10,
        "general": 20,
        "bulk_transfer": 100,
    }
    
    base = base_latency.get(packet_type, 20)
    
    # Load adds latency
    load_factor = 1 + (current_load / 100)
    
    return int(base * load_factor)

