import subprocess
import os
from slab_mood import get_slab_mood

mood = get_slab_mood(temp=62, pcie_health="Optimal")
soundscape = os.path.expanduser(f"~/NoizyFish/Soundscapes/{mood.lower()}_loop.wav")
subprocess.run(["ffplay", "-nodisp", "-autoexit", soundscape])
