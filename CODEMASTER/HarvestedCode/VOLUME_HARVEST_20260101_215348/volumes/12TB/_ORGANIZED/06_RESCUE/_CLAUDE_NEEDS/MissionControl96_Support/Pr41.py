from flask import Flask, request, send_file, jsonify
from __future__ import annotations
import os, asyncio, json, subprocess, hashlib, httpx
from pathlib import Path
from collections import defaultdict

import requests
import tempfile
from flask_cors import CORS
from .utils import walk_files, file_hash, expand

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("ELEVENLABS_API_KEY", "put_your_real_key_here")
VOICE_ID = os.getenv("VOICE_ID", "EXAVITQu4vr4xnSDxMaL")  # Lucy's voice ID

AUDIO_EXTS = ('.wav', '.wave', '.aiff', '.aif', '.mp3', '.flac')

ELEVEN_TTS_URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

async def narrate(api_key: str, voice_id: str, text: str, out_path: str) -> str:
    headers = {
        "Accept": "audio/wav",
        "Content-Type": "application/json",
        "xi-api-key": api_key,
    }
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.7},
    }
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    url = ELEVEN_TTS_URL.format(voice_id=voice_id)
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(url, headers=headers, json=payload)
        r.raise_for_status()
        out.write_bytes(r.content)
    return str(out)

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

def find_dupes(root: str) -> dict:
    files = walk_files(root, AUDIO_EXTS)
    by_size: dict[int, list[Path]] = defaultdict(list)
    for p in files:
        by_size[p.stat().st_size].append(p)
    # Only hash size collisions
    candidates = [grp for grp in by_size.values() if len(grp) > 1]
    hashes: dict[str, list[Path]] = defaultdict(list)
    for grp in candidates:
        for p in grp:
            hashes[file_hash(p)].append(p)
    dupes = {h: ps for h, ps in hashes.items() if len(ps) > 1}
    total = sum(len(ps) - 1 for ps in dupes.values())
    return {"groups": {k: [str(p) for p in v] for k, v in dupes.items()}, "duplicates": total}

def quarantine(dupes: dict, quarantine_dir: str) -> dict:
    q = Path(expand(quarantine_dir))
    q.mkdir(parents=True, exist_ok=True)
    moved = []
    for _, paths in dupes.get("groups", {}).items():
        # keep first, move the rest
        for p in list(map(Path, paths))[1:]:
            dest = q / p.name
            try:
                p.rename(dest)
                moved.append(str(dest))
            except Exception as e:
                moved.append(f"ERROR:{p}:{e}")
    return {"moved": moved}

def expand(path: str) -> str:
    return os.path.expanduser(os.path.expandvars(path))

def scan(root: str) -> dict:
    files: list[Path] = walk_files(root, AUDIO_EXTS)
    total_bytes = sum(p.stat().st_size for p in files)
    return {
        "count": len(files),
        "bytes": total_bytes,
        "files": [str(p) for p in files[:200]],  # cap payload
    }

def walk_files(root: str, exts: tuple[str, ...]) -> list[Path]:
    root = expand(root)
    paths: list[Path] = []
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() in exts:
                paths.append(p)
    return paths

def file_hash(p: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            h.update(chunk)
    return h.hexdigest()

if __name__ == '__main__':
    app.run(host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", 8765)))
