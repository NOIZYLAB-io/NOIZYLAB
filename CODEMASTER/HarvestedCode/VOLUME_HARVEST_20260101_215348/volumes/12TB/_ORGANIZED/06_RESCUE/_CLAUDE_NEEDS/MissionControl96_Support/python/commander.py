# Python: GridCommander
# Add orchestration logic here

import requests

requests.post("http://macstudio.local:5000/pxe_progress", json={"slab":"OMEN_Sentinel","status":"Installing"})
