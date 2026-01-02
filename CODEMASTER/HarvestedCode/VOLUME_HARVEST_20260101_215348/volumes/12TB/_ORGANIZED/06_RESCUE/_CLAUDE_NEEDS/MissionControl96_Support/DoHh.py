#!/usr/bin/env python3
import subprocess, sys, os
buf = sys.argv[1] if len(sys.argv) > 1 else "256"
print(f"Setting CoreAudio buffer (placeholder) to {buf}")
subprocess.run(["killall","-9","coreaudiod"], check=False)
print("CoreAudio restarted")