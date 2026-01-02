import subprocess

def scan_pcie():
    result = subprocess.check_output([
        "system_profiler", "SPPCIDataType"
    ]).decode()
    with open("/Users/rsp_ms/NoizyFish/Logs/pcie_status.log", "w") as log:
        log.write(result)

scan_pcie()
