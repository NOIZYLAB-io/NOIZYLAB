#!/usr/bin/env python3
"""
LUCY - Real-Time Voice Transcription
Listens to your UAD Apollo and transcribes speech to text instantly
"""

import whisper
import sounddevice as sd
import numpy as np
import queue
import tempfile
import wave
import os
from datetime import datetime

class LucyListener:
    def __init__(self, model_size="base"):
        print("🎤 LUCY - Real-Time Voice Transcription")
        print("Loading Whisper model...")
        self.model = whisper.load_model(model_size)
        self.audio_queue = queue.Queue()
        self.sample_rate = 16000
        self.chunk_duration = 3  # Process every 3 seconds

    def audio_callback(self, indata, frames, time, status):
        """Callback for audio stream"""
        if status:
            print(f"Status: {status}")
        self.audio_queue.put(indata.copy())

    def save_chunk(self, audio_data):
        """Save audio chunk to temporary WAV file"""
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        with wave.open(temp_file.name, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(self.sample_rate)
            wf.writeframes((audio_data * 32767).astype(np.int16).tobytes())
        return temp_file.name

    def listen(self):
        """Start listening and transcribing"""
        print(f"\n✅ Listening on UAD Apollo (sample rate: {self.sample_rate}Hz)")
        print("Speak now - transcription appears below:\n")
        print("=" * 60)

        with sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            callback=self.audio_callback,
            blocksize=int(self.sample_rate * self.chunk_duration)
        ):
            audio_buffer = []

            while True:
                try:
                    # Collect audio chunks
                    while not self.audio_queue.empty():
                        audio_buffer.append(self.audio_queue.get())

                    # Process when we have enough audio
                    if len(audio_buffer) >= 1:
                        audio_data = np.concatenate(audio_buffer, axis=0)
                        audio_buffer = []

                        # Save to temp file
                        temp_file = self.save_chunk(audio_data)

                        # Transcribe
                        result = self.model.transcribe(
                            temp_file,
                            language="en",
                            fp16=False
                        )

                        # Clean up temp file
                        os.remove(temp_file)

                        # Display transcription
                        text = result["text"].strip()
                        if text:
                            timestamp = datetime.now().strftime("%H:%M:%S")
                            print(f"[{timestamp}] {text}")

                except KeyboardInterrupt:
                    print("\n\n🔴 Stopped listening")
                    break
                except Exception as e:
                    print(f"Error: {e}")


if __name__ == "__main__":
    # Use "tiny" for fastest speed, "base" for better accuracy
    # "small", "medium", "large" for even better accuracy but slower
    lucy = LucyListener(model_size="tiny")  # Fast real-time
    lucy.listen()
