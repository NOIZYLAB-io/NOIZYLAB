"""
🟩 FULL AUTOOPS RULES
Everything safe runs automatically
Everything risky gets queued
Nothing illegal/dangerous ever runs
"""

FULL_AUTOOPS_RULES = {
    "name": "Full AutoOps",
    "description": "Everything automatic except dangerous OS-level operations",
    
    # These run automatically (everything safe)
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
        
        # Safe repairs
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
        
        # Major repairs (auto in this mode)
        "major_repair", "system_repair",
        "driver_update", "driver_install",
        "registry_clean",
        "software_install_approved",
        "malware_remove", "quarantine_delete",
        "network_optimize",
    ],
    
    # These get queued for approval
    "requires_approval": [
        "software_install_new",
        "software_remove_major",
        "partition_resize",
        "network_config_major",
        "firewall_rule_add",
        "user_account_create",
        "bios_update", "firmware_update",
        "remote_access_request",
    ],
    
    # These are ABSOLUTELY NEVER allowed
    "forbidden": [
        "kernel_op", "kernel_modify",
        "system_file_modify", "system_file_delete",
        "os_reinstall", "os_modify",
        "format_system", "format_boot",
        "remote_access_unsolicited",
        "data_deletion_permanent",
        "unsandboxed_execution",
        "credential_access", "credential_steal",
        "bootloader_modify",
        "encryption_key_access",
        "network_intercept",
        "privacy_violation",
    ],
    
    # Safety guardrails
    "guardrails": {
        "max_auto_actions_per_hour": 500,
        "require_logging": True,
        "require_backup_before_major": True,
        "notify_on_approval_needed": True,
        "auto_rollback_on_failure": True,
        "snapshot_before_batch": True,
        "rate_limit_repairs": 10,  # per minute
    },
}

