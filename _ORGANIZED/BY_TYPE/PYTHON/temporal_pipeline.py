#!/usr/bin/env python3
"""
🟫 NOIZYLAB - Temporal Pipeline
Past + Present + Future - Use old work to shape future output
Fish Music Inc - CB_01
🔥 GORUNFREE! 🎸🔥
"""

import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional


class TemporalPipeline:
    """Uses history to shape future creative output"""

    LOG = Path("history/actions.json")

    def __init__(self, log_path: str = None):
        if log_path:
            self.LOG = Path(log_path)
        self._ensure_log()

    def _ensure_log(self):
        """Ensure log file exists"""
        if not self.LOG.exists():
            self.LOG.parent.mkdir(parents=True, exist_ok=True)
            self.LOG.write_text("[]")

    def log(self, action: str, metadata: Dict = None):
        """Log an action to temporal history"""
        self._ensure_log()
        data = json.loads(self.LOG.read_text())
        data.append({
            "action": action,
            "metadata": metadata or {},
            "timestamp": datetime.now().isoformat()
        })
        self.LOG.write_text(json.dumps(data, indent=2))

    def replay(self) -> List[Dict]:
        """Replay all logged actions"""
        self._ensure_log()
        return json.loads(self.LOG.read_text())

    def replay_range(self, start: str = None, end: str = None) -> List[Dict]:
        """Replay actions within time range"""
        all_actions = self.replay()
        filtered = []
        for a in all_actions:
            ts = a.get("timestamp", "")
            if start and ts < start:
                continue
            if end and ts > end:
                continue
            filtered.append(a)
        return filtered

    def get_patterns(self) -> Dict:
        """Analyze action patterns"""
        actions = self.replay()
        patterns = {}
        for a in actions:
            action = a.get("action", "unknown")
            patterns[action] = patterns.get(action, 0) + 1
        return dict(sorted(patterns.items(), key=lambda x: x[1], reverse=True))

    def predict_next(self) -> Optional[str]:
        """Predict next action based on history"""
        patterns = self.get_patterns()
        if patterns:
            return list(patterns.keys())[0]
        return None

    def clear(self):
        """Clear history"""
        self.LOG.write_text("[]")

    def export(self, path: str):
        """Export history to file"""
        Path(path).write_text(json.dumps(self.replay(), indent=2))

    def stats(self) -> Dict:
        """Get temporal stats"""
        actions = self.replay()
        return {
            "total_actions": len(actions),
            "unique_actions": len(set(a.get("action") for a in actions)),
            "first_action": actions[0]["timestamp"] if actions else None,
            "last_action": actions[-1]["timestamp"] if actions else None,
            "top_patterns": dict(list(self.get_patterns().items())[:5])
        }


if __name__ == "__main__":
    pipe = TemporalPipeline("history/demo.json")
    pipe.log("created project")
    pipe.log("added drums")
    pipe.log("mixed vocals")
    
    print("⏳ TEMPORAL PIPELINE")
    print(f"   Stats: {pipe.stats()}")
    print(f"   Predict next: {pipe.predict_next()}")
    print("\n🔥 GORUNFREE! 🎸🔥")
