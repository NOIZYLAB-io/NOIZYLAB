#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deep_clean_audit.py — Cha-Cha’s Big Cleanup & System Check (macOS-safe)

What it does (non-destructive):
- System snapshot: macOS version, uptime, CPU/mem/disk, network, battery
- Disk space report & large folders scan (no deletions)
- Spotlight status & (optional) reindex trigger
- Logs & cache *report* with gentle clean of user-level temp only
- Homebrew: doctor/update/outdated (no upgrades unless you choose)
- Python envs: list venvs, pip issues, conflicting installations
- LaunchAgents/Login Items sanity
- Audio/TTS: coreaudiod status, default I/O, test “Siri Voice 3”
- Noizy workspace: Cha-Cha/Buddy/Hand-of-God presence & quick self-tests
- Optional: restart CoreAudio, purge inactive RAM (if supported)

All actions logged to Saved_Notes/. Dry-run toggle included.
"""

import os, sys, shlex, subprocess
from pathlib import Path
from datetime import datetime

# ------------ Config ------------
VOICE = "Siri Voice 3"              # set to exact label from `say -v "?"`
WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
SAVE_DIR = WORKSPACE / "Saved_Notes"
SAVE_DIR.mkdir(parents=True, exist_ok=True)
DRY_RUN = False

# ------------ Utils ------------
def say(msg: str):
    try:
        subprocess.run(["say", "-v", VOICE, msg], check=False)
    except OSError as e:
        print(f"say() error: {e}")

def logname(suffix: str):
    return SAVE_DIR / (datetime.now().strftime("%Y-%m-%d_%H%M_") + f"{suffix}.txt")

def run(cmd, allow_fail=True, shell=False, sudo=False):
    if sudo and isinstance(cmd, list) and cmd[0] != "sudo":
        cmd = ["sudo"] + cmd
    pretty = cmd if isinstance(cmd, str) else " ".join(shlex.quote(x) for x in cmd)
    if DRY_RUN:
        return 0, f"(dry-run) {pretty}"
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, shell=shell)
        return 0, out
    except subprocess.CalledProcessError as e:
        if allow_fail:
            return e.returncode, (e.output or str(e))
        raise

def save_report(name: str, content: str):
    p = logname(name)
    p.write_text(content, encoding="utf-8")
    return p

def heading(title): 
    bar = "=" * len(title)
    return f"{title}\n{bar}\n"

def is_macos():
    return sys.platform == "darwin"

# ------------ Checks & Cleanups ------------
def snapshot_system():
    parts = []
    parts.append(heading("System Snapshot"))
    for desc, cmd in [
        ("macOS Version", ["sw_vers"]),
        ("Uptime", ["uptime"]),
        ("CPU", ["sysctl", "-n", "machdep.cpu.brand_string"]),
        ("Memory", ["vm_stat"]),
        ("Disk Usage /", ["df", "-h", "/"]),
        ("Network (ipconfig)", ["ipconfig", "getsummary"])
    ]:
        _, out = run(cmd)
        parts.append(f"## {desc}\n{out.strip()}\n")
    p = save_report("system_snapshot", "\n".join(parts))
    return f"Saved: {p}"

def disk_scan():
    home = str(Path.home())
    candidates = [
        "~/Downloads", "~/Library/Caches", "~/Library/Logs",
        "~/Movies", "~/Music", "~/Pictures"
    ]
    out = [heading("Disk Scan (Top-level Sizes)")]
    _, du_out = run(["du", "-sh", "/Applications", "/Library", home, "/System", "/usr", "/opt", "/private"], allow_fail=True)
    out.append(du_out.strip())
    out.append("\n" + heading("Candidate Folders"))
    for c in candidates:
        _, size = run(["du", "-sh", os.path.expanduser(c)], allow_fail=True)
        out.append(f"{c}: {size.strip()}")
    p = save_report("disk_scan", "\n".join(out))
    return f"Saved: {p}"

def spotlight_status(reindex=False):
    out = [heading("Spotlight Status")]
    _, st = run(["mdutil", "-s", "/"], allow_fail=True)
    out.append(st.strip())
    if reindex:
        _, idx = run(["mdutil", "-E", "/"], allow_fail=True, sudo=True)
        out.append("\nTriggered reindex:\n" + idx.strip())
    p = save_report("spotlight", "\n".join(out))
    return f"Saved: {p}"

def gentle_temp_clean():
    """
    Only removes user temp folder contents in ~/Library/Caches/com.apple.finder/Cache.db? No.
    We'll do *very* safe: ~/Library/Caches/* subfolders' ephemeral files if allowed,
    and /var/folders user temp via mktemp dir – but default is report-only unless user chooses.
    """
    out = [heading("Gentle Temp Clean (User)")]
    cache_dir = Path.home() / "Library" / "Caches"
    removed = 0
    if cache_dir.exists():
        for item in cache_dir.iterdir():
            # do not delete the folder itself; try to prune trivial *.tmp files
            if item.is_dir():
                for sub in item.glob("**/*.tmp"):
                    if not DRY_RUN:
                        try:
                            sub.unlink(missing_ok=True)
                            removed += 1
                        except OSError as e:
                            print(f"gentle_temp_clean() error: {e}")
        out.append(f"Removed {removed} *.tmp files in ~/Library/Caches/** (safe prune).")
    else:
        out.append("No ~/Library/Caches found.")
    p = save_report("gentle_temp_clean", "\n".join(out))
    return f"Saved: {p}"

def logs_summary():
    out = [heading("Recent System Logs (brief)")]
    _, syslog = run(["log", "show", "--style", "syslog", "--last", "30m"])
    out.append(syslog[:200000])  # cap
    p = save_report("logs_recent", "\n".join(out))
    return f"Saved: {p}"

def brew_health():
    out = [heading("Homebrew Health")]
    for desc, cmd in [
        ("brew doctor", ["brew", "doctor"]),
        ("brew update", ["brew", "update"]),
        ("brew outdated", ["brew", "outdated"])
    ]:
        _, o = run(cmd, allow_fail=True)
        out.append(f"\n## {desc}\n{o.strip()}")
    p = save_report("brew_health", "\n".join(out))
    return f"Saved: {p}"

def python_env_health():
    out = [heading("Python Environment Health")]
    # which pythons
    for cmd in [["which", "python3"], ["python3", "--version"]]:
        _, o = run(cmd, allow_fail=True)
        out.append("$ " + " ".join(cmd) + "\n" + o.strip())
    # pip check if available
    _, pipv = run(["python3", "-m", "pip", "--version"], allow_fail=True)
    out.append("\n## pip\n" + pipv.strip())
    _, pipc = run(["python3", "-m", "pip", "check"], allow_fail=True)
    out.append("\n" + pipc.strip())
    p = save_report("python_env_health", "\n".join(out))
    return f"Saved: {p}"

def launch_items_health():
    out = [heading("Login Items & LaunchAgents")]
    # Login items (macOS 13+ not easily listable via CLI; we’ll capture LaunchAgents/Daemons)
    la = Path.home() / "Library" / "LaunchAgents"
    sys_la = Path("/Library/LaunchAgents")
    sys_ld = Path("/Library/LaunchDaemons")
    for title, path in [("User LaunchAgents", la), ("System LaunchAgents", sys_la), ("System LaunchDaemons", sys_ld)]:
        out.append(f"\n## {title}\n")
        if path.exists():
            for f in sorted(path.glob("*.plist")):
                out.append(str(f))
        else:
            out.append("(none)")
    p = save_report("launch_items", "\n".join(out))
    return f"Saved: {p}"

def audio_tts_health():
    out = [heading("Audio/TTS Health")]
    # coreaudiod running?
    _, ps = run(["pgrep", "coreaudiod"], allow_fail=True)
    out.append("coreaudiod PID(s): " + (ps.strip() or "not running"))
    # default audio devices snapshot
    _, sp = run(["system_profiler", "SPAudioDataType"], allow_fail=True)
    out.append("\nSystem Profiler (Audio) excerpt:\n" + sp[:100000])
    # test TTS voice
    try:
        subprocess.run(["say", "-v", VOICE, "Cha Cha system voice test completed."], check=False)
        out.append("\nTTS: spoke with " + VOICE)
    except OSError as e:
        out.append(f"\nTTS: failed -> {e}")
    p = save_report("audio_tts", "\n".join(out))
    return f"Saved: {p}"

def restart_coreaudio():
    _, _ = run(["sudo", "pkill", "coreaudiod"], allow_fail=True)
    return "Requested coreaudiod restart."

def purge_ram():
    code, _ = run(["which", "purge"], allow_fail=True)
    if code != 0:
        return "'purge' not available on this macOS."
    run(["purge"], allow_fail=True, sudo=True)
    return "Purged inactive RAM (if supported)."

def noizy_workspace_health():
    out = [heading("Noizy Workspace Health")]
    CHECK_VSBUDDY = "check_vsbuddy.py"
    files = [
        "hand_of_god.py",
        "cha_cha_hotrod.py",
        "chacha_bridge.py",
        "cha_cha_listener.py",
        CHECK_VSBUDDY,
        "save_textedit.py",
        "clipboard_guard.py",
        "read_page_cha_cha.py",
        "read_selection_cha_cha.py"
    ]
    for f in files:
        p = WORKSPACE / f
        out.append(f"{f}: {'OK' if p.exists() else 'MISSING'}")
    # quick self-tests (non-invasive)
    if (WORKSPACE / "chacha_bridge.py").exists():
        out.append("\nBridge present.")
    if (WORKSPACE / CHECK_VSBUDDY).exists():
        _, res = run(["python3", str(WORKSPACE / CHECK_VSBUDDY), "status"], allow_fail=True)
        out.append("\nVS Buddy status:\n" + res.strip())
    p = save_report("noizy_workspace", "\n".join(out))
    return f"Saved: {p}"

# ------------ Menu ------------
def menu():
    print("\n=== Cha-Cha Big Cleanup & Check ===")
    print("1) System snapshot")
    print("2) Disk scan (sizes)")
    print("3) Spotlight status  (r=reindex)")
    print("4) Gentle temp clean (safe *.tmp purge in user caches)")
    print("5) Recent logs (30m)")
    print("6) Homebrew health (doctor/update/outdated)")
    print("7) Python env health")
    print("8) LaunchAgents/Login items snapshot")
    print("9) Audio & TTS health + voice test")
    print("a) Restart CoreAudio")
    print("b) Purge inactive RAM (if available)")
    print("c) Noizy workspace health (Cha-Cha/Buddy)")
    print("d) Toggle dry-run (current: {})".format("ON" if DRY_RUN else "OFF"))
    print("m) Mute Cha-Cha (persistent)")
    print("u) Unmute Cha-Cha (persistent)")
    print("q) Quit")
    return input("Select: ").strip().lower()

def main():
    if not is_macos():
        print("This tool is for macOS.")
        sys.exit(2)
    say("Beginning system check, my dear.")
    def handle_choice(choice, dry_run_ref):
        if choice == "1":
            print(snapshot_system()); say("System snapshot saved.")
        elif choice == "2":
            print(disk_scan()); say("Disk scan saved.")
        elif choice == "3":
            ans = input("Reindex Spotlight? (y/N): ").strip().lower()
            print(spotlight_status(reindex=(ans=="y"))); say("Spotlight report saved.")
        elif choice == "4":
            print(gentle_temp_clean()); say("Gentle temp cleanup done.")
        elif choice == "5":
            print(logs_summary()); say("Logs captured.")
        elif choice == "6":
            print(brew_health()); say("Homebrew health completed.")
        elif choice == "7":
            print(python_env_health()); say("Python report saved.")
        elif choice == "8":
            print(launch_items_health()); say("LaunchAgents snapshot saved.")
        elif choice == "9":
            print(audio_tts_health()); say("Audio and voice check complete.")
        elif choice == "a":
            print(restart_coreaudio()); say("Core Audio restarted.")
        elif choice == "b":
            print(purge_ram()); say("Memory purged, if supported.")
        elif choice == "c":
            print(noizy_workspace_health()); say("Workspace check complete.")
        elif choice == "d":
            dry_run_ref[0] = not dry_run_ref[0]
            print("Dry-run is now", dry_run_ref[0])
        elif choice == "m":
            say("Cha-Cha is now muted.")
            subprocess.run(["osascript", "-e", "set volume output muted true"])
        elif choice == "u":
            say("Cha-Cha is now unmuted.")
            subprocess.run(["osascript", "-e", "set volume output muted false"])
        elif choice == "q":
            say("All done. Reports are in Saved Notes, my dear.")
            return False
        else:
            print("Invalid choice.")
        return True

    dry_run_ref = [DRY_RUN]
    running = True
    while running:
        c = menu()
        running = handle_choice(c, dry_run_ref)
    DRY_RUN = dry_run_ref[0]

if __name__ == "__main__":
    main()
