import subprocess, time, json, os
def autosave_commit(label="Ritual"):
    try:
        ts=time.strftime("%Y-%m-%d %H:%M:%S"); subprocess.check_call(["git","add","."])
        subprocess.check_call(["git","commit","-m",f"{label} autosave at {ts}"])
        return True
    except:
        return False
