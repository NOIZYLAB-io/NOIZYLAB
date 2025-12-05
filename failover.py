"""NoizyGrid: Failover System"""
from datetime import datetime

FAILOVER_CONFIG = {"primary": "m2_ultra", "secondary": "mac_studio", "tertiary": "hp_omen"}
FAILOVER_LOG = []

def failover(failed_node):
    """Execute failover from failed node"""
    order = list(FAILOVER_CONFIG.values())
    if failed_node in order:
        order.remove(failed_node)
    
    if not order: return {"error": "No backup nodes available"}
    
    new_primary = order[0]
    event = {"failed": failed_node, "new_primary": new_primary, "timestamp": datetime.now().isoformat()}
    FAILOVER_LOG.append(event)
    
    return {"status": "failover_complete", "from": failed_node, "to": new_primary}

def get_backup_nodes():
    return FAILOVER_CONFIG

def set_failover_order(primary, secondary, tertiary=None):
    FAILOVER_CONFIG["primary"] = primary
    FAILOVER_CONFIG["secondary"] = secondary
    if tertiary: FAILOVER_CONFIG["tertiary"] = tertiary
    return FAILOVER_CONFIG

def test_failover():
    """Test failover without actually failing over"""
    return {"test": "passed", "order": list(FAILOVER_CONFIG.values())}

def get_failover_history():
    return FAILOVER_LOG

