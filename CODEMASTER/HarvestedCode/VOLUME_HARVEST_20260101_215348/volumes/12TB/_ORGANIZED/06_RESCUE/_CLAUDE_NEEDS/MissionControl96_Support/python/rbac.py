POLICY = {
  "viewer": {"devices": ["DL-001"], "actions": []},
  "operator": {"devices": ["DL-001","DL-002"], "actions": ["status","clients"]},
  "admin": {"devices": ["*"], "actions": ["reboot","config","signed-config"]}
}
def can(role, device_id, action):
    p = POLICY.get(role, {})
    devs = p.get("devices", [])
    acts = p.get("actions", [])
    return ("*" in devs or device_id in devs) and (action in acts or "*" in acts)
