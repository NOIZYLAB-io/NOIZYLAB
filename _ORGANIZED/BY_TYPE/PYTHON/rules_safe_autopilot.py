"""
🟥 SAFE AUTOPILOT RULES
Business = fully automated
Technical repairs = ALWAYS require approval
"""

SAFE_AUTOPILOT_RULES = {
    "name": "Safe Autopilot",
    "description": "AI runs business; YOU approve all technical repairs",
    
    # These run automatically
    "auto_allowed": [
        "intake", "client_intake", "auto_intake",
        "schedule", "booking", "appointment",
        "billing", "invoice", "receipt",
        "marketing", "content", "social",
        "crm", "customer_update", "follow_up",
        "prediagnostics", "device_info",
        "notification", "reminder", "alert",
        "report", "analytics", "metrics",
        "backup", "snapshot", "sync",
        "log", "monitor", "health_check",
    ],
    
    # These require approval
    "requires_approval": [
        "repair", "fix", "patch",
        "install", "uninstall", "remove",
        "update", "upgrade",
        "driver", "firmware",
        "registry", "config",
        "network_change", "firewall",
        "user_settings", "preferences",
        "disk_operation", "partition",
        "malware_removal", "quarantine",
    ],
    
    # These are NEVER allowed
    "forbidden": [
        "kernel_op", "system_file_modify",
        "os_reinstall", "format",
        "remote_access_unsolicited",
        "data_deletion_permanent",
        "unsandboxed_execution",
        "credential_access",
    ],
    
    # Safety guardrails
    "guardrails": {
        "max_auto_actions_per_hour": 100,
        "require_logging": True,
        "require_backup_before_change": True,
        "notify_on_approval_needed": True,
    },
}

