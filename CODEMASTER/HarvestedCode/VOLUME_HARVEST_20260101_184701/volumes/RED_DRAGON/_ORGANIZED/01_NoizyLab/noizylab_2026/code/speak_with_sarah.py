import requests

# ElevenLabs Text-to-Speech for NoizyFish profile

def speak_with_sarah(text, voice_id="Sarah", api_key="your-elevenlabs-api-key"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.85
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    with open("/Users/rsp_ms/Desktop/NoizyFish/sarah_output.mp3", "wb") as f:
        f.write(response.content)
    print("Sarah has spoken. 🎙️")

# Example usage
if __name__ == "__main__":
    speak_with_sarah("Welcome back, Rob. Your system is humming and your legacy is alive.")
