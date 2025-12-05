"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         MODE MANAGER                                         ║
║              The Three-Mode Autonomy System                                  ║
║                                                                              ║
║  MODE 1: SAFE AUTOPILOT - AI runs business, YOU approve repairs             ║
║  MODE 2: TECHNICIAN ASSIST - AI does safe repairs, you approve major        ║
║  MODE 3: FULL AUTOOPS - Everything automatic except dangerous ops           ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from datetime import datetime

MODES = {
    "safe_autopilot": {
        "id": 1,
        "name": "Safe Autopilot",
        "description": "AI runs business; YOU approve technical repairs",
        "auto_intake": True,
        "auto_schedule": True,
        "auto_billing": True,
        "auto_marketing": True,
        "auto_crm": True,
        "auto_prediagnostics": True,
        "auto_safe_repairs": False,
        "auto_major_repairs": False,
        "auto_system_changes": False,
        "requires_approval": ["all_repairs", "system_changes", "software_removal"],
    },
    "technician_assist": {
        "id": 2,
        "name": "Technician Assist",
        "description": "AI does safe repairs automatically; you approve major ones",
        "auto_intake": True,
        "auto_schedule": True,
        "auto_billing": True,
        "auto_marketing": True,
        "auto_crm": True,
        "auto_prediagnostics": True,
        "auto_safe_repairs": True,
        "auto_major_repairs": False,
        "auto_system_changes": False,
        "requires_approval": ["major_repairs", "system_changes", "kernel_ops", "software_removal"],
        "safe_repairs": [
            "clear_logs", "repair_permissions", "fix_startup_items", "reset_preferences",
            "run_sfc_dism", "optimize_ram", "reset_network_stack", "remove_bloatware",
            "tune_up", "update_drivers_noncritical", "repair_caches", "identify_malware"
        ],
    },
    "full_autoops": {
        "id": 3,
        "name": "Full AutoOps",
        "description": "Everything automatic except dangerous OS-level operations",
        "auto_intake": True,
        "auto_schedule": True,
        "auto_billing": True,
        "auto_marketing": True,
        "auto_crm": True,
        "auto_prediagnostics": True,
        "auto_safe_repairs": True,
        "auto_major_repairs": True,
        "auto_system_changes": False,
        "requires_approval": ["kernel_ops", "os_modification", "data_deletion", "remote_access"],
        "forbidden": ["modify_system_files", "kernel_level_ops", "unsandboxed_ops", "remote_without_permission"],
    },
}

CURRENT_MODE = "technician_assist"
MODE_LOG = []

def get_mode():
    """Get current operating mode"""
    return {"current": CURRENT_MODE, "config": MODES[CURRENT_MODE]}

def set_mode(mode_name):
    """Set operating mode"""
    global CURRENT_MODE
    if mode_name not in MODES:
        return {"error": f"Unknown mode: {mode_name}", "available": list(MODES.keys())}
    
    old_mode = CURRENT_MODE
    CURRENT_MODE = mode_name
    
    event = {"from": old_mode, "to": mode_name, "timestamp": datetime.now().isoformat()}
    MODE_LOG.append(event)
    
    return {"status": "mode_changed", "from": old_mode, "to": mode_name, "config": MODES[mode_name]}

def can_auto_execute(action_type):
    """Check if action can be auto-executed in current mode"""
    mode = MODES[CURRENT_MODE]
    
    # Check forbidden actions
    if action_type in mode.get("forbidden", []):
        return {"allowed": False, "reason": "forbidden_action"}
    
    # Check if requires approval
    if action_type in mode.get("requires_approval", []):
        return {"allowed": False, "reason": "requires_approval"}
    
    # Check specific permissions
    if action_type == "repair" and not mode.get("auto_safe_repairs"):
        return {"allowed": False, "reason": "repairs_require_approval"}
    
    if action_type == "major_repair" and not mode.get("auto_major_repairs"):
        return {"allowed": False, "reason": "major_repairs_require_approval"}
    
    return {"allowed": True, "mode": CURRENT_MODE}

def is_safe_repair(repair_type):
    """Check if repair is classified as safe"""
    mode = MODES.get("technician_assist", {})
    return repair_type in mode.get("safe_repairs", [])

def get_mode_log():
    return MODE_LOG

def get_all_modes():
    return MODES

def get_permissions():
    """Get current mode permissions"""
    mode = MODES[CURRENT_MODE]
    return {
        "auto_business": all([mode.get("auto_intake"), mode.get("auto_schedule"), mode.get("auto_billing")]),
        "auto_safe_repairs": mode.get("auto_safe_repairs", False),
        "auto_major_repairs": mode.get("auto_major_repairs", False),
        "requires_approval": mode.get("requires_approval", []),
    }

