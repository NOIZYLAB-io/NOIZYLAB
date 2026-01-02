#!/usr/bin/env python3
"""
ElevenLabs TTS helper
- Prefers voice by name (default: Sarah)
- Reads text from a file or stdin
- Writes MP3 output to a path

Requirements:
- Environment variable ELEVENLABS_API_KEY must be set

Usage:
  python3 elevenlabs_tts.py --text-file INPUT.txt --out OUTPUT.mp3 --voice Sarah
  echo "Hello" | python3 elevenlabs_tts.py --out hello.mp3 --voice Sarah
"""
import argparse
import os
import sys
import json
import urllib.request
import urllib.error
import ssl
try:
    import certifi
except Exception:
    certifi = None

VOICES_URL = "https://api.elevenlabs.io/v1/voices"
TTS_URL_TMPL = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
DEFAULT_MODEL = "eleven_multilingual_v2"
CACHE_DIR = ".eleven_cache"


def http_request(url, method="GET", headers=None, data=None):
    req = urllib.request.Request(url, data=data, method=method)
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    # Create SSL context using certifi if available (fixes CERTIFICATE_VERIFY_FAILED on macOS)
    context = None
    try:
        if certifi is not None:
            context = ssl.create_default_context(cafile=certifi.where())
        else:
            context = ssl.create_default_context()
    except Exception:
        context = None
    try:
        if context is not None:
            with urllib.request.urlopen(req, context=context) as resp:
                return resp.read(), resp.getcode(), resp.info()
        else:
            with urllib.request.urlopen(req) as resp:
                return resp.read(), resp.getcode(), resp.info()
    except urllib.error.HTTPError as e:
        return e.read(), e.code, e.headers
    except Exception as e:
        raise


def cache_path_for_voice(voice_name: str) -> str:
    safe = voice_name.strip().lower().replace(" ", "_")
    return os.path.join(CACHE_DIR, f"voice_id_{safe}.txt")


def get_voice_id_by_name(api_key: str, voice_name: str) -> str:
    # Try cache first
    try:
        cp = cache_path_for_voice(voice_name)
        if os.path.exists(cp):
            with open(cp, "r", encoding="utf-8") as f:
                vid = f.read().strip()
                if vid:
                    return vid
    except Exception:
        pass

    body, code, headers = http_request(
        VOICES_URL,
        headers={
            "xi-api-key": api_key,
            "accept": "application/json",
        },
    )
    if code != 200:
        msg = body.decode('utf-8', 'ignore')
        if code == 401:
            raise RuntimeError(
                "Failed to list voices (HTTP 401 Unauthorized). Invalid API key. "
                "Ensure you are using an ElevenLabs API Key (not a project token). "
                "You can generate one from Profile -> API Keys."
            )
        raise RuntimeError(f"Failed to list voices (HTTP {code}): {msg}")
    data = json.loads(body.decode("utf-8"))
    voices = data.get("voices", [])
    # Case-insensitive match by name
    for v in voices:
        if v.get("name", "").lower() == voice_name.lower():
            vid = v.get("voice_id")
            # Save cache
            try:
                os.makedirs(CACHE_DIR, exist_ok=True)
                with open(cache_path_for_voice(voice_name), "w", encoding="utf-8") as f:
                    f.write(vid or "")
            except Exception:
                pass
            return vid
    raise RuntimeError(f"Voice '{voice_name}' not found in your ElevenLabs account.")


def synthesize(api_key: str, voice_id: str, text: str) -> bytes:
    payload = {
        "text": text,
        "model_id": DEFAULT_MODEL,
        "voice_settings": {
            "stability": 0.41,
            "similarity_boost": 0.8,
            "style": 0.2,
            "use_speaker_boost": True,
        },
    }
    body_bytes = json.dumps(payload).encode("utf-8")
    url = TTS_URL_TMPL.format(voice_id=voice_id)
    resp_body, code, headers = http_request(
        url,
        method="POST",
        headers={
            "xi-api-key": api_key,
            "accept": "audio/mpeg",
            "content-type": "application/json",
        },
        data=body_bytes,
    )
    if code != 200:
        msg = resp_body.decode('utf-8', 'ignore')
        if code == 401:
            raise RuntimeError(
                "TTS failed (HTTP 401 Unauthorized). Invalid API key. "
                "Confirm ELEVENLABS_API_KEY is set correctly (Keychain/launchctl/tts.env)."
            )
        raise RuntimeError(f"TTS failed (HTTP {code}): {msg}")
    return resp_body


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text-file", help="Path to input text file (optional)")
    parser.add_argument("--out", required=True, help="Output audio file path (mp3)")
    parser.add_argument("--voice", default="Sarah", help="Preferred ElevenLabs voice name")
    args = parser.parse_args()

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("ELEVENLABS_API_KEY not set", file=sys.stderr)
        sys.exit(2)

    # Read text
    text = None
    if args.text_file:
        with open(args.text_file, "r", encoding="utf-8") as f:
            text = f.read().strip()
    else:
        data = sys.stdin.read()
        text = data.strip()
    if not text:
        print("No text provided", file=sys.stderr)
        sys.exit(2)

    # Prefer explicit VOICE_ID if provided
    voice_id_env = os.environ.get("ELEVEN_VOICE_ID")
    try:
        if voice_id_env:
            voice_id = voice_id_env
        else:
            voice_id = get_voice_id_by_name(api_key, args.voice)
    except Exception as e:
        print(f"Error resolving voice '{args.voice}': {e}", file=sys.stderr)
        sys.exit(1)

    try:
        audio_bytes = synthesize(api_key, voice_id, text)
        # Ensure output dir exists
        out_dir = os.path.dirname(args.out)
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)
        with open(args.out, "wb") as f:
            f.write(audio_bytes)
        print(f"Saved: {args.out}")
    except Exception as e:
        print(f"TTS error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
