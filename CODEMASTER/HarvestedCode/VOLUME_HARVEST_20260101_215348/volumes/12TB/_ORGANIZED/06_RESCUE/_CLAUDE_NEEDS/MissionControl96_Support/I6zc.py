import datetime
import subprocess

def capture_memory():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"/Users/rsp_ms/NoizyFish/Legacy/memory_{timestamp}.aiff"
    subprocess.run(["say", "Tell me something you want remembered."])
    subprocess.run(["rec", path])  # Requires SoX installed
    print(f"🧠 Memory captured: {path}")

capture_memory()
