import subprocess, os
from datetime import datetime

filename = f"memory_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
path = os.path.expanduser(f"~/NoizyFish/Legacy/{filename}")
subprocess.run(["say", "Tell me something you want remembered."])
subprocess.run(["rec", path])
subprocess.run(["say", "Memory captured and preserved."])
