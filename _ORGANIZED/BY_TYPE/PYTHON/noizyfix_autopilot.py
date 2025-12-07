from .system_exec import run_cmd, detect_os


def autopilot_run():
    os_name = detect_os()

    if os_name == "darwin":
        return run_noizyfix_macos()

    if os_name == "windows":
        return run_noizyfix_windows()

    return {"status": "unsupported-os"}


# -------------------
# macOS FIX ENGINE
# -------------------
def run_noizyfix_macos():
    log = []

    log.append(run_cmd("sudo dscacheutil -flushcache"))
    log.append(run_cmd("sudo killall -HUP mDNSResponder"))
    log.append(run_cmd("rm -rf ~/Library/Caches/*"))
    log.append(run_cmd("sudo softwareupdate -ia"))

    return {
        "status": "completed",
        "os": "macOS",
        "actions": [
            "dns_flush",
            "mdns_respawn",
            "cache_cleanup",
            "system_update",
        ],
        "log": log,
    }


# -------------------
# WINDOWS FIX ENGINE
# -------------------
def run_noizyfix_windows():
    cmds = [
        "ipconfig /flushdns",
        "netsh winsock reset",
        "del /q/f/s %TEMP%\\*",
        "wuauclt /detectnow"
    ]

    results = [run_cmd(cmd) for cmd in cmds]

    return {
        "status": "completed",
        "os": "windows",
        "actions": [
            "dns_flush",
            "winsock_reset",
            "temp_cleanup",
            "windows_update_check",
        ],
        "log": results,
    }

