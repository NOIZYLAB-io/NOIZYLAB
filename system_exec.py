import subprocess
import platform


def run_cmd(cmd: str):
    try:
        result = subprocess.check_output(
            cmd, stderr=subprocess.STDOUT, shell=True
        ).decode()
        return {"ok": True, "output": result}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def detect_os():
    return platform.system().lower()

