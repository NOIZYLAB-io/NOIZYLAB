"""
Wwise Audio Integration Template (Python)
-----------------------------------------
This template demonstrates basic Wwise audio integration concepts using the Wwise Authoring API (WAAPI).
"""

import waapi

# Connect to Wwise Authoring API
client = waapi.WAAPIClient()

# Play an event
event_name = 'Play_MySound'
client.call('ak.soundengine.postEvent', {'event': event_name})

# Set RTPC value
client.call('ak.soundengine.setRTPCValue', {'rtpc': 'Volume', 'value': 80})

# Stop all sounds
client.call('ak.soundengine.stopAll')

# For more advanced usage, see Wwise WAAPI docs: https://www.audiokinetic.com/library/edge/?source=SDK&id=waapi.html
