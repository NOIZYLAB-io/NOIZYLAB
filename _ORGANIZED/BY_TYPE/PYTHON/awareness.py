#!/usr/bin/env python3
import subprocess
class OmnipresentAwareness:
    NODES = ["192.168.0.20", "192.168.0.10", "127.0.0.1"]
    def probe(self):
        results = {}
        for n in self.NODES:
            try:
                r = subprocess.run(["ping", "-c", "1", "-W", "1", n], capture_output=True, timeout=2)
                results[n] = "online" if r.returncode == 0 else "offline"
            except:
                results[n] = "timeout"
        return results
