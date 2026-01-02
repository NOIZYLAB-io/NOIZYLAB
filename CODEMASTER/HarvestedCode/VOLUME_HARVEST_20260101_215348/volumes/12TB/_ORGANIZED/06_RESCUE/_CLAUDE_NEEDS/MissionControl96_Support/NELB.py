import subprocess
from slab_mood_engine import get_slab_mood

mood = get_slab_mood(temp=62, pcie_health="Optimal")
soundscape = f"~/NoizyFish/Soundscapes/{mood.lower()}_loop.wav"
subprocess.run(["ffplay", "-nodisp", "-autoexit", soundscape])
