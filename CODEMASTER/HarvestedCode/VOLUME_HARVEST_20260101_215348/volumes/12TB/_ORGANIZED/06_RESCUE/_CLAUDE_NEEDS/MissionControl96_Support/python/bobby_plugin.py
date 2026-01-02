# Bobby plugin for NoizyFish Orchestrator
class BobbyAgent:
    def on_message(self, msg):
        print(f"[BobbyAgent] Received: {msg}")
        # Here you could call speak_with_say, send to ElevenLabs, etc.
        # For demo, just print
        if "hello" in msg.lower():
            print("[BobbyAgent] Hi there! How can I help you today?")
        elif "debug" in msg.lower():
            print("[BobbyAgent] Starting debug routine...")
        else:
            print(f"[BobbyAgent] You said: {msg}")

def register_agent():
    return BobbyAgent()
