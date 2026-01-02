import json, time, threading
from pathlib import Path

AUDIT_LOG = Path(__file__).parent.parent / ".." / "audit.log"
AUDIT_LOCK = threading.Lock()

def audit_event(event, subject, result, extra=None):
    entry = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "event": event,
        "subject": subject,
        "result": result,
        "extra": extra or {}
    }
    with AUDIT_LOCK:
        with open(AUDIT_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")

# Story mode: render audit log as mythic prose

def story_mode():
    if not AUDIT_LOG.exists(): return "No rituals yet."
    lines = AUDIT_LOG.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines[-100:]:  # last 100 events
        try:
            e = json.loads(line)
            ts = e["ts"]
            event = e["event"]
            subj = e["subject"]
            result = e["result"]
            # extra = e.get("extra", {})
            # Mythic narration
            if event.startswith("sentinel-"):
                out.append(f"[{ts}] Sentinel invoked {event.replace('sentinel-', '')} on {subj}: {result}")
            else:
                out.append(f"[{ts}] Ritual {event} for {subj}: {result}")
        except Exception:
            continue
    return "\n".join(out)
