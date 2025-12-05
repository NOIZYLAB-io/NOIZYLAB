import { ElevenLabsClient, play } from '@elevenlabs/elevenlabs-js';

const elevenlabs = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY || "YOUR_API_KEY",
});

async function speakWithModel() {
  const audio = await elevenlabs.textToSpeech.convert(
    'JBFqnCBsd6RMkjVDRZzb', // voice_id
    {
      text: 'This is a test using a specific ElevenLabs model.',
      modelId: 'eleven_multilingual_v2', // See docs for available models
      outputFormat: 'mp3_44100_128',
    }
  );
  await play(audio);
}

speakWithModel();