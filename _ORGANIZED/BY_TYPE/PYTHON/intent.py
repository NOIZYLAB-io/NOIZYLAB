"""
NoizyDrive Intent Engine
========================
Learns why files exist and their purpose.
Semantic understanding of file context.
"""

from typing import Dict, Optional, List
from datetime import datetime
import re


# Intent patterns
INTENT_PATTERNS = {
    "session_log": [r"session", r"recording", r"capture"],
    "project_asset": [r"asset", r"resource", r"material"],
    "client_deliverable": [r"final", r"delivery", r"export", r"master"],
    "work_in_progress": [r"wip", r"draft", r"v\d+", r"revision"],
    "reference": [r"ref", r"reference", r"inspiration"],
    "backup": [r"backup", r"bak", r"archive"],
    "temp": [r"temp", r"tmp", r"scratch"],
    "config": [r"config", r"settings", r"pref"],
}


def infer_intent(filename: str, context: Dict = None) -> str:
    """
    Infer the intent/purpose of a file.
    
    Context can include:
    - session: current session ID
    - project: project name
    - client: client name
    - compute_job: job ID
    - source_app: originating application
    - user_action: what user was doing
    """
    if context is None:
        context = {}
    
    # Context-based intent (highest priority)
    if context.get("session"):
        return f"session:{context['session']}"
    
    if context.get("project"):
        return f"project:{context['project']}"
    
    if context.get("client"):
        return f"client:{context['client']}"
    
    if context.get("compute_job"):
        return f"compute_output:{context['compute_job']}"
    
    if context.get("source_app"):
        return f"app_output:{context['source_app']}"
    
    # Pattern-based intent
    name_lower = filename.lower()
    for intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, name_lower, re.IGNORECASE):
                return intent
    
    # Time-based inference
    hour = datetime.now().hour
    if context.get("user_action") == "save":
        if 9 <= hour <= 17:
            return "work_output"
        else:
            return "personal_output"
    
    return "unknown"


def infer_detailed_intent(filename: str, context: Dict = None) -> Dict:
    """
    Get detailed intent analysis.
    """
    primary = infer_intent(filename, context)
    
    result = {
        "primary_intent": primary,
        "confidence": 0.5,
        "context_used": [],
        "inferred_relationships": [],
    }
    
    if context:
        # Track what context was used
        for key in ["session", "project", "client", "compute_job"]:
            if context.get(key):
                result["context_used"].append(key)
                result["confidence"] = 0.9
    
    # Infer relationships
    if primary.startswith("project:"):
        project = primary.split(":")[1]
        result["inferred_relationships"].append({
            "type": "belongs_to",
            "target": f"project/{project}",
        })
    
    if primary.startswith("client:"):
        client = primary.split(":")[1]
        result["inferred_relationships"].append({
            "type": "owned_by",
            "target": f"client/{client}",
        })
    
    # Pattern matches increase confidence
    name_lower = filename.lower()
    for intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, name_lower):
                if intent == primary or primary == "unknown":
                    result["confidence"] = min(0.95, result["confidence"] + 0.1)
    
    return result


def extract_version(filename: str) -> Optional[str]:
    """
    Extract version number from filename.
    """
    patterns = [
        r"v(\d+(?:\.\d+)*)",  # v1, v1.2, v1.2.3
        r"_(\d+)$",           # _1, _2
        r"revision[_\s]?(\d+)",
        r"r(\d+)",            # r1, r2
    ]
    
    name = filename.lower()
    for pattern in patterns:
        match = re.search(pattern, name)
        if match:
            return match.group(1)
    
    return None


def is_final_version(filename: str) -> bool:
    """
    Check if file appears to be a final version.
    """
    final_indicators = ["final", "master", "approved", "release", "gold"]
    name_lower = filename.lower()
    
    return any(ind in name_lower for ind in final_indicators)


def get_intent_priority(intent: str) -> int:
    """
    Get priority for intent (for processing order).
    """
    priorities = {
        "client_deliverable": 10,
        "work_in_progress": 8,
        "project_asset": 7,
        "session_log": 6,
        "reference": 4,
        "backup": 2,
        "temp": 1,
        "unknown": 0,
    }
    
    # Handle prefixed intents
    if ":" in intent:
        base = intent.split(":")[0]
        if base in ["client", "project"]:
            return 9
        if base == "compute_output":
            return 5
    
    return priorities.get(intent, 3)


def suggest_retention(intent: str) -> Dict:
    """
    Suggest retention policy based on intent.
    """
    policies = {
        "client_deliverable": {"keep": "forever", "backup": True},
        "project_asset": {"keep": "forever", "backup": True},
        "work_in_progress": {"keep": "1_year", "backup": False},
        "session_log": {"keep": "6_months", "backup": False},
        "reference": {"keep": "1_year", "backup": False},
        "backup": {"keep": "90_days", "backup": False},
        "temp": {"keep": "7_days", "backup": False},
        "compute_output": {"keep": "30_days", "backup": False},
    }
    
    # Handle prefixed intents
    if ":" in intent:
        base = intent.split(":")[0]
        if base in ["client", "project"]:
            return {"keep": "forever", "backup": True}
    
    return policies.get(intent, {"keep": "1_year", "backup": False})

