from flask import Flask, request, send_file, jsonify

import requests
import os
import tempfile
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Lucy's voice ID

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text_input = data.get("text", "")
    if not text_input:
        return jsonify({"error": "No text provided"}), 400

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "Accept": "audio/wav",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }
    payload = {
        "text": text_input,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp:
            tmp.write(response.content)
            tmp.flush()
            return send_file(tmp.name, mimetype='audio/wav', as_attachment=True, download_name='narration.wav')
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == '__main__':
    app.run(port=8765)
