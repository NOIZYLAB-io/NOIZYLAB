"""
FMOD Audio Programming Template (Python)
----------------------------------------
This template demonstrates basic FMOD audio scripting concepts using the FMOD Python API.
"""

import fmod

# Initialize FMOD system
system = fmod.System()
system.init()

# Load and play a sound
sound = system.create_sound('path/to/audio.wav')
channel = system.play_sound(sound)

# Set volume and effects
channel.set_volume(0.8)
# channel.add_dsp(fmod.DSP_TYPE_ECHO)

# Stop playback
channel.stop()

# Release resources
sound.release()
system.close()

# For more advanced usage, see FMOD API docs: https://www.fmod.com/resources/documentation-api
