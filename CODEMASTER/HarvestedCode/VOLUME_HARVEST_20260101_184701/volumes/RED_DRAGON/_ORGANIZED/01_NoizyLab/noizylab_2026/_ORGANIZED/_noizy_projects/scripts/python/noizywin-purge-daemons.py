import subprocess

VM_NAME = "NOIZYWIN"
DAEMONS = ["SpeechRuntime.exe", "Cortana.exe"]

def purge_voice_daemons():
    for daemon in DAEMONS:
        cmd = ["prlctl", "exec", VM_NAME, f"taskkill /F /IM {daemon}"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"🔇 Purged {daemon}:\n{result.stdout}")

if __name__ == "__main__":
    purge_voice_daemons()
