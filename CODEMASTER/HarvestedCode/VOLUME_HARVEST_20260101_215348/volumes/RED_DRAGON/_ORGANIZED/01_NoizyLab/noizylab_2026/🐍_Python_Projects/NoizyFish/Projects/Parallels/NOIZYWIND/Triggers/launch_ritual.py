import subprocess

def launch_ritual(name):
    rituals = {
        "scan": "~/NoizyFish/Triggers/slablink_scanner.py",
        "activate": "~/NoizyFish/Triggers/Noizy_Genie_SlabLink.py",
        "dashboard": "open http://localhost:5050"
    }
    path = rituals.get(name)
    if path:
        if path.endswith(".py"):
            subprocess.run(["python3", path])
        else:
            subprocess.run(["bash", "-c", path])
    else:
        print("❌ Unknown ritual.")

# Example usage
# launch_ritual("scan")
# launch_ritual("activate")
# launch_ritual("dashboard")
