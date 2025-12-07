"""NoizyGrid: Jumbo Frame Engine - MC96 Network Optimization"""
from datetime import datetime

JUMBO_STATUS = {"enabled": True, "mtu": 9000, "interface": "en0"}
PACKET_LOG = []

def enable_jumbo(interface="en0", mtu=9000):
    """Enable jumbo frames"""
    JUMBO_STATUS["enabled"] = True
    JUMBO_STATUS["mtu"] = mtu
    JUMBO_STATUS["interface"] = interface
    return {"status": "enabled", "mtu": mtu, "interface": interface}

def disable_jumbo():
    JUMBO_STATUS["enabled"] = False
    JUMBO_STATUS["mtu"] = 1500
    return {"status": "disabled", "mtu": 1500}

def send_jumbo(data, target_node):
    """Send data using jumbo frames"""
    packet = {"target": target_node, "size": len(str(data)), "mtu": JUMBO_STATUS["mtu"], 
              "jumbo": JUMBO_STATUS["enabled"], "timestamp": datetime.now().isoformat()}
    PACKET_LOG.append(packet)
    return packet

def get_jumbo_status():
    return JUMBO_STATUS

def get_packet_stats():
    if not PACKET_LOG: return {"total": 0, "avg_size": 0}
    return {"total": len(PACKET_LOG), "avg_size": sum(p["size"] for p in PACKET_LOG) / len(PACKET_LOG)}

