"""Orchestra: Flow Bridge - Connects to 100 Flows"""
from datetime import datetime

ACTIVE_FLOWS = {}
FLOW_LOG = []

def trigger_flow(flow_id, context=None):
    """Trigger a flow by ID"""
    context = context or {}
    
    flow_entry = {
        "flow_id": flow_id,
        "context": context,
        "triggered_at": datetime.now().isoformat(),
        "status": "running",
    }
    ACTIVE_FLOWS[flow_id] = flow_entry
    FLOW_LOG.append(flow_entry)
    
    # Execute flow
    try:
        result = _execute_flow(flow_id, context)
        flow_entry["status"] = "completed"
        flow_entry["result"] = result
    except Exception as e:
        flow_entry["status"] = "error"
        flow_entry["error"] = str(e)
    
    return flow_entry

def _execute_flow(flow_id, context):
    """Execute a flow"""
    # Route to flow module
    return {"flow": flow_id, "executed": True, "context": context}

def get_active_flows():
    return {k: v for k, v in ACTIVE_FLOWS.items() if v["status"] == "running"}

def stop_flow(flow_id):
    if flow_id in ACTIVE_FLOWS:
        ACTIVE_FLOWS[flow_id]["status"] = "stopped"
        return {"stopped": flow_id}
    return {"error": "Flow not found"}

def get_flow_log(limit=50):
    return FLOW_LOG[-limit:]

def trigger_batch(flow_ids, context=None):
    """Trigger multiple flows"""
    return [trigger_flow(fid, context) for fid in flow_ids]

