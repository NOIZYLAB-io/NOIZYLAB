import time, threading
from dlink_dashboard.dlink import service
from ..utils.audit import audit_event

class Sentinel:
    def __init__(self, interval=15):
        self.interval = interval
        self._running = False
        self._backoff = {}  # device_id -> attempt count

    def start(self, app):
        if self._running: return
        self._running = True
        t = threading.Thread(target=self._loop, args=(app,), daemon=True)
        t.start()

    def _loop(self, app):
        from dlink_dashboard.intel.predictive import PredictiveSentinel
        predictive = PredictiveSentinel()
        with app.app_context():
            while self._running:
                try:
                    for d in service.list_devices():
                        s = service.device_status(d.id)
                        if self._is_unhealthy(s):
                            self._handle_unhealthy_device(d, s)
                        else:
                            self._backoff[d.id] = 0
                    # Lightweight anomaly detection
                    predictive.tick()
                except Exception as e:
                    audit_event("sentinel-error", "grid", {"ok": False, "error": str(e)})
                time.sleep(self.interval)

    def _is_unhealthy(self, status):
        return (not status.online) or (status.cpu >= 90) or (status.mem >= 90)

    def _handle_unhealthy_device(self, device, status):
        n = self._backoff.get(device.id, 0)
        delay = min(300, int(2 ** n))  # capped exponential
        action = "observe"
        result = {"ok": True, "reason": "within backoff window", "delay": delay}
        if delay == 1:  # first hit -> attempt light heal
            action = "heal-config"
            result = service.apply_config(device.id, {"wifi_power": "medium"}, dry_run=False)
        elif delay >= 4 and n < 5:  # escalating -> reboot
            action = "reboot"
            result = service.reboot(device.id, dry_run=False)
        self._backoff[device.id] = n + 1
        audit_event(
            f"sentinel-{action}",
            device.id,
            result,
            extra={"cpu": status.cpu, "mem": status.mem, "online": status.online}
        )
