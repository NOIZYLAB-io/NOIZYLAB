"""NoizyFlow Trigger Engine"""
def check_trigger(trigger, event):
    if trigger.get("type") != event.get("type"):
        return False
    for k, v in trigger.items():
        if k == "type":
            continue
        if event.get(k) != v:
            return False
    return True

