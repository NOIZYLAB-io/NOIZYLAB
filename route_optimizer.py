"""
NoizyNet Adaptive Route Optimizer
=================================
Predictive packet routing based on device roles,
compute load, system mood, threat level, and session type.
"""

from typing import Dict, Optional, List
from datetime import datetime


# Route priority levels
PRIORITY_LEVELS = {
    "critical": 0,    # Emergency, security
    "priority": 1,    # VR, real-time audio
    "high": 2,        # Primary devices, compute
    "shield": 3,      # Security traffic
    "support": 4,     # Client support
    "normal": 5,      # Regular traffic
    "low": 6,         # Bulk, backup
    "throttle": 7,    # Rate-limited
}

# Route history for learning
ROUTE_HISTORY: List[Dict] = []


def optimize_route(packet: Dict, context: Dict) -> str:
    """
    Determine optimal routing priority for a packet.
    
    Packet includes:
    - src_ip, dst_ip
    - src_role, dst_role (from NoizyMesh)
    - protocol, port
    - size
    
    Context includes:
    - flowState: calm/normal/emergency
    - threat_level: low/medium/high
    - compute_load: 0-100
    - vr_active: bool
    - client_session: bool
    """
    # Emergency mode - everything critical
    if context.get("flowState") == "emergency":
        return "critical"
    
    # VR traffic gets top priority
    if context.get("vr_active") and packet.get("protocol") == "udp":
        return "priority"
    
    # Threat detected - security traffic prioritized
    if context.get("threat_level") == "high":
        if packet.get("dst_role") == "security":
            return "shield"
        # Throttle unknown traffic during threats
        if packet.get("src_role") == "ghost":
            return "throttle"
    
    # Primary devices always get high priority
    if packet.get("dst_role") == "primary":
        return "high"
    
    # Security devices
    if packet.get("dst_role") == "security":
        return "shield"
    
    # Client support sessions
    if context.get("client_session") or packet.get("dst_role") == "client":
        return "support"
    
    # Compute traffic during heavy load
    if context.get("compute_load", 0) > 70:
        if packet.get("protocol") == "tcp" and packet.get("port") in [8080, 8989]:
            return "high"
    
    # Bulk transfers get lower priority
    if packet.get("size", 0) > 1000000:  # > 1MB
        return "low"
    
    return "normal"


def get_route_weight(priority: str) -> int:
    """
    Get numeric weight for priority (lower = higher priority).
    """
    return PRIORITY_LEVELS.get(priority, 5)


def should_use_jumbo_frames(packet: Dict, context: Dict) -> bool:
    """
    Determine if jumbo frames should be used for this packet.
    Always prefer jumbo frames for local traffic.
    """
    # Large transfers benefit most
    if packet.get("size", 0) > 10000:
        return True
    
    # Local mesh traffic
    if packet.get("dst_role") in ["primary", "work", "compute"]:
        return True
    
    # Compute jobs
    if context.get("compute_active"):
        return True
    
    return True  # Default to jumbo [[memory:11717841]]


def calculate_optimal_path(src: str, dst: str, mesh: List[Dict]) -> List[str]:
    """
    Calculate optimal network path between two nodes.
    """
    # Simple direct path for now
    # Could be enhanced with multi-hop routing
    return [src, "mc96.local", dst]


def log_route_decision(packet: Dict, priority: str, context: Dict) -> None:
    """
    Log routing decision for learning.
    """
    entry = {
        "timestamp": datetime.now().isoformat(),
        "src": packet.get("src_ip"),
        "dst": packet.get("dst_ip"),
        "priority": priority,
        "context_state": context.get("flowState"),
    }
    
    ROUTE_HISTORY.append(entry)
    
    # Trim history
    if len(ROUTE_HISTORY) > 1000:
        ROUTE_HISTORY[:] = ROUTE_HISTORY[-500:]


def get_route_stats() -> Dict:
    """
    Get routing statistics.
    """
    if not ROUTE_HISTORY:
        return {"total": 0}
    
    priority_counts = {}
    for entry in ROUTE_HISTORY[-100:]:
        p = entry.get("priority", "unknown")
        priority_counts[p] = priority_counts.get(p, 0) + 1
    
    return {
        "total": len(ROUTE_HISTORY),
        "recent_100": priority_counts,
    }


def predict_congestion(current_load: Dict) -> Dict:
    """
    Predict network congestion based on current state.
    """
    cpu = current_load.get("cpu", 0)
    network = current_load.get("network_io", 0)
    active_sessions = current_load.get("sessions", 0)
    
    risk = 0
    if cpu > 80:
        risk += 30
    if network > 80:
        risk += 40
    if active_sessions > 10:
        risk += 20
    
    return {
        "congestion_risk": min(100, risk),
        "recommendation": "throttle_bulk" if risk > 60 else "normal",
    }

