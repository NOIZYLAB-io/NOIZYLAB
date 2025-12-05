"""
NoizyMemory GEN-1 — Layer 3: Issue Memory
==========================================
Tracks all reported problems, identifies patterns, enables predictive diagnostics.
"""

from datetime import datetime
from typing import Dict, List, Any, Optional

# In-memory store (replace with database in production)
ISSUE_HISTORY: Dict[str, List[Dict[str, Any]]] = {}


def log_issue(email: str, issue: str, details: Optional[Dict] = None) -> bool:
    """
    Log an issue reported by a client.
    
    Args:
        email: Client identifier
        issue: Issue description
        details: Optional additional details (device, severity, etc.)
    
    Returns:
        True if successful
    """
    if email not in ISSUE_HISTORY:
        ISSUE_HISTORY[email] = []
    
    issue_entry = {
        "issue": issue,
        "timestamp": datetime.now().isoformat(),
        "resolved": False
    }
    
    if details:
        issue_entry.update(details)
    
    ISSUE_HISTORY[email].append(issue_entry)
    return True


def recall_issues(email: str, limit: Optional[int] = None) -> List[Dict]:
    """
    Retrieve all issues for a client.
    
    Args:
        email: Client identifier
        limit: Optional limit on number of issues to return
    
    Returns:
        List of issue records
    """
    issues = ISSUE_HISTORY.get(email, [])
    
    if limit:
        return issues[-limit:]
    
    return issues


def repeated_issues(email: str) -> Dict[str, int]:
    """
    Identify repeated issues for pattern recognition.
    
    Args:
        email: Client identifier
    
    Returns:
        Dict mapping issue descriptions to occurrence counts
    """
    issues = ISSUE_HISTORY.get(email, [])
    issue_counts = {}
    
    for entry in issues:
        issue = entry.get("issue", "unknown")
        # Normalize issue text for matching
        normalized = issue.lower().strip()
        issue_counts[normalized] = issue_counts.get(normalized, 0) + 1
    
    return issue_counts


def get_unresolved_issues(email: str) -> List[Dict]:
    """Get all unresolved issues for a client."""
    issues = ISSUE_HISTORY.get(email, [])
    return [i for i in issues if not i.get("resolved", False)]


def resolve_issue(email: str, issue_index: int) -> bool:
    """Mark an issue as resolved."""
    if email not in ISSUE_HISTORY:
        return False
    
    if 0 <= issue_index < len(ISSUE_HISTORY[email]):
        ISSUE_HISTORY[email][issue_index]["resolved"] = True
        ISSUE_HISTORY[email][issue_index]["resolved_at"] = datetime.now().isoformat()
        return True
    
    return False


def get_issue_patterns(email: str) -> Dict[str, Any]:
    """
    Analyze issue patterns for predictive diagnostics.
    
    Returns:
        Dict with pattern analysis
    """
    issues = ISSUE_HISTORY.get(email, [])
    
    if not issues:
        return {"total": 0, "patterns": {}, "recurring": []}
    
    counts = repeated_issues(email)
    recurring = [k for k, v in counts.items() if v > 1]
    
    # Find most common issue
    most_common = max(counts.items(), key=lambda x: x[1]) if counts else (None, 0)
    
    return {
        "total": len(issues),
        "patterns": counts,
        "recurring": recurring,
        "most_common": most_common[0],
        "most_common_count": most_common[1]
    }


def get_recent_issues(email: str, days: int = 30) -> List[Dict]:
    """Get issues from the last N days."""
    from datetime import timedelta
    
    issues = ISSUE_HISTORY.get(email, [])
    cutoff = datetime.now() - timedelta(days=days)
    
    recent = []
    for issue in issues:
        try:
            ts = datetime.fromisoformat(issue.get("timestamp", ""))
            if ts > cutoff:
                recent.append(issue)
        except:
            continue
    
    return recent

