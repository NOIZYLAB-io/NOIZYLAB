from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key="YOUR_API_KEY"  # Replace with your actual API key
)

# Fetch Sarah's voice_id
voices = client.voices.get_all()
sarah_voice_id = None
for v in voices['voices']:
    if v['name'].lower() == 'sarah':
        sarah_voice_id = v['voice_id']
        break
if not sarah_voice_id:
    raise Exception("Sarah voice not found. Make sure your API key has voices_read permission.")

response = client.conversational_ai.agents.create(
    name="Mission Control",
    conversation_config={
        "agent": {
            "prompt": {
                "prompt": "You are Mission Control, using Sarah's voice for all responses.",
            },
            "voice_id": sarah_voice_id
        }
    }
)
print(response)
