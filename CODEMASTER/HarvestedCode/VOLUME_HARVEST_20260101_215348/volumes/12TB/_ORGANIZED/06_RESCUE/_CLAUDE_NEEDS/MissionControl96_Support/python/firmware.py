import time, requests
from ..dlink import service
from ..utils.audit import audit_event

def check_and_stage():
    for d in service.list_devices():
        try:
            # Placeholder: query vendor endpoint by model
            latest = "1.21"
            if service.device_status(d.id).firmware != latest:
                res = service.apply_config(d.id, {"stage_firmware": latest}, dry_run=False)
                audit_event("firmware-stage", d.id, res, extra={"latest": latest})
        except Exception as e:
            audit_event("firmware-error", d.id, {"ok": False, "error": str(e)})
