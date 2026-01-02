from elevenlabs import ElevenLabs
import os

# grab your API key from environment variable
client = ElevenLabs(api_key=os.environ.get("ELEVENLABS_API_KEY"))

# pick a voice (can be "Rachel", "Adam", etc. or your custom voice ID)
voice = "Rachel"

# text to narrate
text = "Welcome back! This is your AI narrator, ready to tell your story."

# synthesize
audio = client.text_to_speech.convert(
    voice_id=voice,
    model_id="eleven_multilingual_v2",
    text=text
)

# save to file
with open("narration.wav", "wb") as f:
    for chunk in audio:
        f.write(chunk)

const handleNarrate = async () => {
  if (!textToNarrate.trim()) return;
  logActivity(`🎙 Narrating text: "${textToNarrate}"`);
  try {
    const res = await fetch("http://localhost:8765/tts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: textToNarrate }),
    });
    if (res.ok) {
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const audio = new Audio(url);
      audio.play();
      logActivity("✅ Narration played.");
    } else {
      logActivity("❌ Narration failed.");
    }
  } catch (e) {
    logActivity("❌ Narration error: " + e);
  }
  setTextToNarrate("");
};
