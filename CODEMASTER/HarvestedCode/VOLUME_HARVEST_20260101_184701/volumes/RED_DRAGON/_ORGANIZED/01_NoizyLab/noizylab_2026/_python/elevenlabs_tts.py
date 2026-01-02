import httpx
import os

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "your_api_key_here")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "your_voice_id_here")


def synthesize_speech(text, output_path="output.wav"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {"xi-api-key": ELEVENLABS_API_KEY, "Content-Type": "application/json"}
    data = {"text": text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}}
    with httpx.stream("POST", url, headers=headers, json=data) as response:
        response.raise_for_status()
        with open(output_path, "wb") as f:
            for chunk in response.iter_bytes():
                f.write(chunk)
    return output_path

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 elevenlabs_tts.py 'Text to speak'")
        exit(1)
    text = sys.argv[1]
    out = synthesize_speech(text)
    print(f"Audio saved to {out}")
