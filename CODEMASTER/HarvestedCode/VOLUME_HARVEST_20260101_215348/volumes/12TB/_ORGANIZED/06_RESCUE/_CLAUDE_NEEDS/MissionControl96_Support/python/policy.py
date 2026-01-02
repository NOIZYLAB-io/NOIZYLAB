import time, yaml
from ..dlink import service
from ..utils.audit import audit_event

class PolicyEngine:
    def __init__(self, path="policies/rules.yaml"):
        with open(path,"r") as f: self.rules = yaml.safe_load(f)
        self.state = {}  # device_id -> {rule_id: first_seen_ts}

    def evaluate(self):
        now = int(time.time())
        for d in service.list_devices():
            s = service.device_status(d.id)
            for r in self.rules:
                rid = r["id"]; st = self.state.setdefault(d.id, {}).get(rid)
                match = False
                m = r["match"]
                if "online" in m: match |= (s.online == m["online"])
                if "cpu_gt" in m: match |= (s.cpu >= m["cpu_gt"])
                if match:
                    if not st: self.state[d.id][rid] = now
                    elif now - st >= m.get("duration_sec", 0):
                        action = r["action"]
                        if action == "reboot":
                            res = service.reboot(d.id, dry_run=False)
                        elif action == "heal-config":
                            res = service.apply_config(d.id, r.get("params", {}), dry_run=False)
                        else: res = {"ok": False, "message":"unknown action"}
                        audit_event(f"policy-{rid}", d.id, res, extra={"rule": r})
                        self.state[d.id][rid] = None  # reset
                else:
                    self.state[d.id][rid] = None
