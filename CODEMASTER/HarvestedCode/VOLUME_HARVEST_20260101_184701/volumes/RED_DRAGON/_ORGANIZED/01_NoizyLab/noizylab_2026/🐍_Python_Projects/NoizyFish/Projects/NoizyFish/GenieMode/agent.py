import subprocess
import os

class Agent:
    def trigger(self, name):
        mapping = {
            "capsule_builder": os.path.expanduser("~/NoizyFish/Triggers/build_capsule.sh"),
            "slab_resurrector": os.path.expanduser("~/NoizyFish/Triggers/restart_noizywind.sh"),
        }
        script = mapping.get(name)
        if script and os.path.exists(script):
            subprocess.run([script])
        else:
            print(f"No trigger found for: {name}")

    def offer(self, service, price=None):
        if service == "overlay_rendering":
            subprocess.run([os.path.expanduser("~/NoizyFish/Triggers/launch_overlay.sh")])
            if price == "ambient loop":
                subprocess.run([os.path.expanduser("~/NoizyFish/Triggers/play_mood_loop.sh"), "focused"])

    def accept(self, task, reward=None):
        if task == "capsule curation":
            subprocess.run([os.path.expanduser("~/NoizyFish/Triggers/build_capsule.sh")])
            if reward == "voice feedback":
                subprocess.run(["say", "Capsule curation complete."])
