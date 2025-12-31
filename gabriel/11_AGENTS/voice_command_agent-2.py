# Voice Command Agent Plugin
# Handles wake word, speech-to-text, and TTS for Bobby

def register(orchestrator):
    orchestrator.register_agent('voice_command', VoiceCommandAgent())

class VoiceCommandAgent:
    def handle_event(self, event):
        # Placeholder: handle voice input/output events
        return {'status': 'ok', 'message': 'Voice Command agent active.'}
