"""
🟧 TECHNICIAN ASSIST RULES
Safe repairs auto-run
Major repairs require approval
Dangerous repairs blocked
"""

TECHNICIAN_ASSIST_RULES = {
    "name": "Technician Assist",
    "description": "AI does safe repairs automatically; you approve major ones",
    
    # These run automatically
    "auto_allowed": [
        # Business operations
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
    
    # Safe repairs that auto-run
    "safe_repairs": [
        "clear_logs", "clear_cache", "clear_temp",
        "repair_permissions", "fix_permissions",
        "fix_startup_items", "disable_startup",
        "reset_preferences", "reset_defaults",
        "run_sfc", "run_dism", "sfc_dism",
        "optimize_ram", "free_memory",
        "reset_network_stack", "flush_dns",
        "remove_bloatware", "disable_bloatware",
        "tune_up", "optimization",
        "update_drivers_noncritical",
        "repair_caches", "rebuild_cache",
        "identify_malware", "scan_malware",
        "disk_cleanup", "defrag",
        "browser_cleanup", "cookie_clear",
    ],
    
    # These require approval
    "requires_approval": [
        "major_repair", "system_repair",
        "driver_critical", "driver_gpu", "driver_chipset",
        "registry_edit", "registry_clean",
        "software_install", "software_remove",
        "malware_remove", "quarantine_delete",
        "partition_resize", "disk_format",
        "network_config", "firewall_rule",
        "user_account_change",
        "bios_update", "firmware_update",
    ],
    
    # These are NEVER allowed
    "forbidden": [
        "kernel_op", "system_file_modify",
        "os_reinstall", "format_system",
        "remote_access_unsolicited",
        "data_deletion_permanent",
        "unsandboxed_execution",
        "credential_access",
        "bootloader_modify",
    ],
    
    # Safety guardrails
    "guardrails": {
        "max_auto_actions_per_hour": 200,
        "require_logging": True,
        "require_backup_before_major": True,
        "notify_on_approval_needed": True,
        "auto_rollback_on_failure": True,
    },
}

