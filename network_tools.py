import subprocess


def ping_target(ip: str):
    try:
        out = subprocess.check_output(
            ["ping", "-c", "4", ip], stderr=subprocess.STDOUT
        ).decode()
        return {"status": "ok", "output": out}
    except Exception as e:
        return {"status": "error", "error": str(e)}
