"""Orchestra: Sync Link - Cross-Device Synchronization"""
from datetime import datetime

SYNC_STATE = {
    "last_sync": None,
    "sync_count": 0,
    "devices": {},
    "status": "idle",
}

SYNC_LOG = []

def sync_all():
    """Sync state across all devices"""
    SYNC_STATE["status"] = "syncing"
    
    # Gather state from all layers
    from .state_router import get_global_state
    state = get_global_state()
    
    sync_record = {
        "timestamp": datetime.now().isoformat(),
        "state_snapshot": state,
        "devices_synced": list(SYNC_STATE["devices"].keys()),
    }
    
    SYNC_STATE["last_sync"] = sync_record["timestamp"]
    SYNC_STATE["sync_count"] += 1
    SYNC_STATE["status"] = "idle"
    SYNC_LOG.append(sync_record)
    
    return sync_record

def get_sync_status():
    return SYNC_STATE.copy()

def register_device(device_id, device_info):
    """Register a device for sync"""
    SYNC_STATE["devices"][device_id] = {
        **device_info,
        "registered_at": datetime.now().isoformat(),
        "last_seen": datetime.now().isoformat(),
    }
    return {"registered": device_id}

def unregister_device(device_id):
    if device_id in SYNC_STATE["devices"]:
        del SYNC_STATE["devices"][device_id]
        return {"unregistered": device_id}
    return {"error": "Device not found"}

def heartbeat_device(device_id):
    if device_id in SYNC_STATE["devices"]:
        SYNC_STATE["devices"][device_id]["last_seen"] = datetime.now().isoformat()
        return {"heartbeat": device_id}
    return {"error": "Device not found"}

def get_sync_log(limit=20):
    return SYNC_LOG[-limit:]

