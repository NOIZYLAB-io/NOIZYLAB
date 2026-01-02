import subprocess
import os

def strategist_offer(service, price=None):
    if service == "overlay_rendering":
        subprocess.run([os.path.expanduser("~/NoizyFish/Triggers/launch_overlay.sh")])
        if price == "ambient loop":
            subprocess.run([os.path.expanduser("~/NoizyFish/Triggers/play_mood_loop.sh"), "focused"])


def healer_accept(task, reward=None):
    if task == "capsule curation":
        subprocess.run([os.path.expanduser("~/NoizyFish/Triggers/build_capsule.sh")])
        if reward == "voice feedback":
            subprocess.run(["say", "Capsule curation complete."])
