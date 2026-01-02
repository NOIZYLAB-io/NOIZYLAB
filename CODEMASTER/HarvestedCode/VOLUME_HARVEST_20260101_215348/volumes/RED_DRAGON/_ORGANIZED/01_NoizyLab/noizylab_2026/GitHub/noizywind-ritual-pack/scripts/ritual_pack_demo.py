import subprocess
import os

def trigger_ritual(name):
    script = os.path.expanduser(f"~/GitHub/noizywind-ritual-pack/scripts/{name}.bat")
    if os.path.exists(script):
        subprocess.run([script])
    else:
        print(f"Ritual script {script} not found.")

def overlay_launch(name):
    overlay = os.path.expanduser(f"~/GitHub/noizywind-ritual-pack/overlays/{name}.html")
    if os.path.exists(overlay):
        subprocess.run(["open", overlay])
    else:
        print(f"Overlay {overlay} not found.")

def voice_say(message):
    subprocess.run(["say", message])

# Example usage
if __name__ == "__main__":
    trigger_ritual("build_capsule")
    overlay_launch("planar_eyelevel")
    voice_say("Capsule preserved. Slab is glowing.")
