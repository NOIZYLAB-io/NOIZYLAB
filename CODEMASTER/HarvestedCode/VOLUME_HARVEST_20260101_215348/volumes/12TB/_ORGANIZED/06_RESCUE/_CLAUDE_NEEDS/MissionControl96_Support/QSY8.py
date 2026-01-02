from collections import deque
import numpy as np
from ..dlink import service
from ..utils.audit import audit_event

class PredictiveSentinel:
    def __init__(self, window=30, cpu_thresh=2.0, mem_thresh=2.0):
        self.cpu_hist = {}
        self.mem_hist = {}
        self.window = window
        self.cpu_thresh = cpu_thresh
        self.mem_thresh = mem_thresh

    def _push(self, hist, key, val):
        dq = hist.get(key) or deque(maxlen=self.window)
        dq.append(val); hist[key] = dq
        arr = np.array(dq); return arr.mean(), arr.std()

    def tick(self):
        for d in service.list_devices():
            s = service.device_status(d.id)
            cpu_mean, cpu_std = self._push(self.cpu_hist, d.id, s.cpu)
            mem_mean, mem_std = self._push(self.mem_hist, d.id, s.mem)
            cpu_z = (s.cpu - cpu_mean) / (cpu_std or 1)
            mem_z = (s.mem - mem_mean) / (mem_std or 1)
            if cpu_z >= self.cpu_thresh or mem_z >= self.mem_thresh or not s.online:
                res = service.apply_config(d.id, {"wifi_power": "medium"}, dry_run=False)
                audit_event("predictive-heal", d.id, res, extra={"cpu_z": float(cpu_z), "mem_z": float(mem_z), "online": s.online})
