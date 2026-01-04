#!/usr/bin/env python3
"""
Supersonic preprocessor for Claude: compress forensic/log data to high-signal JSON.
"""
import json
from typing import Any, Dict


def prepare_claude_manifest(forensic_log, jitter_data) -> str:
    """
    Compresses the forensic audit into a 'Supersonic' summary for Claude.
    Expects forensic_log to expose .score and .get_drift_points(); jitter_data with .mean().
    """
    summary: Dict[str, Any] = {
        "integrity_score": getattr(forensic_log, "score", None),
        "critical_drift": getattr(forensic_log, "get_drift_points", lambda: [])(),
        "jitter_baseline": getattr(jitter_data, "mean", lambda: None)(),
        "registry_hash": "SOVEREIGN_LOCKED",
    }
    return json.dumps(summary, indent=2)


if __name__ == "__main__":
    # Stub demo
    class _Log:
        score = 0.991

        def get_drift_points(self):
            return ["U8900-rail"]

    class _Jitter:
        def mean(self):
            return 0.037

    print(prepare_claude_manifest(_Log(), _Jitter()))
