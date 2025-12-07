"""
NoizyMesh Role Classifier
=========================
AI-based device role assignment based on vendor fingerprinting.

Roles:
- primary: Main workstations (M2 Ultra, Mac Pro)
- work: Work nodes (Omen, laptops)
- portal: Control surfaces (iPads, iPhones)
- fun: Entertainment (consoles)
- utility: Printers, NAS
- security: Cameras, access points
- ghost: Unknown devices (potential threats)
"""

from typing import Dict


# Known device patterns for role classification
ROLE_PATTERNS = {
    "primary": [
        "apple inc", "apple computer", "mac pro", "mac studio", "mac mini"
    ],
    "portal": [
        "ipad", "iphone", "ipod", "apple mobile"
    ],
    "work": [
        "hp", "hewlett", "lenovo", "dell", "asus", "acer", "microsoft",
        "intel corporate", "gigabyte", "msi"
    ],
    "fun": [
        "xbox", "sony", "playstation", "nintendo", "valve", "steam"
    ],
    "security": [
        "camera", "arlo", "ring", "nest", "wyze", "hikvision", "dahua",
        "ubiquiti", "unifi", "reolink"
    ],
    "utility": [
        "brother", "epson", "canon", "hp inc", "synology", "qnap",
        "western digital", "seagate", "netgear", "tp-link", "linksys"
    ],
    "network": [
        "cisco", "d-link", "netgear", "asus router", "ubiquiti", "aruba"
    ]
}


def assign_role(device: Dict) -> str:
    """
    Assign a role to a device based on its vendor fingerprint.
    Returns role string.
    """
    vendor = device.get("vendor", "").lower()
    
    # Check each role pattern
    for role, patterns in ROLE_PATTERNS.items():
        for pattern in patterns:
            if pattern in vendor:
                # Special case: Apple devices need further classification
                if role == "primary" and any(p in vendor for p in ["ipad", "iphone", "ipod"]):
                    return "portal"
                return role
    
    # Unknown device = ghost (potential security concern)
    return "ghost"


def get_role_priority(role: str) -> str:
    """
    Get network priority based on role.
    Used for MC96 path optimization.
    """
    priorities = {
        "primary": "critical",
        "work": "high",
        "portal": "high",
        "security": "medium",
        "network": "medium",
        "utility": "low",
        "fun": "low",
        "ghost": "isolate"
    }
    return priorities.get(role, "normal")


def get_role_color(role: str) -> str:
    """
    Get UI color for role display.
    """
    colors = {
        "primary": "#F5C542",   # Gold
        "work": "#00E5FF",      # Cyan
        "portal": "#9B59B6",    # Purple
        "security": "#FF3747",  # Red
        "network": "#3498DB",   # Blue
        "utility": "#95A5A6",   # Gray
        "fun": "#2ECC71",       # Green
        "ghost": "#E74C3C"      # Danger Red
    }
    return colors.get(role, "#FFFFFF")


def should_auto_provision(role: str) -> bool:
    """
    Determine if device should be auto-provisioned.
    """
    return role in ["work", "portal", "primary"]


def get_provision_action(role: str) -> str:
    """
    Get provisioning action for role.
    """
    actions = {
        "work": "install_noizylab_agent",
        "portal": "install_noizyportal",
        "primary": "install_noizyos_full",
        "security": "add_to_noizyshield",
        "fun": "monitor_only",
        "ghost": "alert_and_isolate"
    }
    return actions.get(role, "monitor_only")

