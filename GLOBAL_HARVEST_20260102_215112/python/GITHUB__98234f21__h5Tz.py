# ──────────────────────────────────────────────────────────────────────────────
# FILE: rock_mode.py  (One‑File, Sweet & Amazing, Ready to Rock)
# ──────────────────────────────────────────────────────────────────────────────
"""
NoizyFish ROCK MODE — a single, glorious Python file that:
- Self-checks keys and optional deps (OpenAI, ElevenLabs)
- Spins up a FastAPI micro-portal with HTML UI
- Accepts image + audio uploads, transcribes voice, generates a diagnostic code
- Can synthesize a short spoken reply via ElevenLabs (if key present)
- Publishes everything to your MCP server so Mission Control sees it instantly
- Tries to auto-launch MCP if it's not running yet

Run:
  python rock_mode.py
Then visit:
  http://127.0.0.1:9090
"""
from __future__ import annotations
import os, sys, time, subprocess, json
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# ── Paths & folders ─────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent
PORTAL = ROOT / "portal"
UPLOADS = PORTAL / "uploads"
TEMPLATES = PORTAL / "templates"
UPLOADS.mkdir(parents=True, exist_ok=True)
TEMPLATES.mkdir(parents=True, exist_ok=True)

# Minimal inline template (in case real template is missing)
INDEX_HTML = (TEMPLATES/"rock.html")
if not INDEX_HTML.exists():
    INDEX_HTML.write_text(
        """
<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>NoizyFish — ROCK MODE</title>
  <style>
    body{font-family:system-ui;background:#0b0e12;color:#e6edf3;margin:0;padding:24px}
    .wrap{max-width:980px;margin:0 auto}
    .card{background:#11161c;border:1px solid #1f2630;border-radius:16px;padding:18px;margin-bottom:16px}
    input,textarea,button{width:100%;padding:10px;border-radius:10px;border:1px solid #2b3440;background:#0b0e12;color:#e6edf3}
    button{cursor:pointer}
    small{opacity:0.7}
    pre{white-space:pre-wrap;word-break:break-word;background:#0b0e12;border:1px solid #1f2630;border-radius:8px;padding:8px}
  </style>
</head>
<body>
  <div class="wrap">
    <h1>🐟 NoizyFish — ROCK MODE</h1>
    <div class="card">
      <form action="/upload" method="post" enctype="multipart/form-data">
        <label>Client Name</label>
        <input name="client_name" placeholder="Your client's name" required>
        <label>Short Description</label>
        <textarea name="description" rows="3" placeholder="Describe the issue…"></textarea>
        <label>Upload Screenshot / Image (optional)</label>
        <input type="file" name="image" accept="image/*" />
        <label>Upload Voice Note (optional)</label>
        <input type="file" name="voice" accept="audio/*" />
        <button type="submit">Submit to Mission Control</button>
        <small>Transcribes voice (OpenAI) and may reply (ElevenLabs) if keys present.</small>
      </form>
    </div>
    <div class="card">
      <h3>Health</h3>
      <div id="health">Loading…</div>
      <script>
        async function tick(){
          try{const r=await fetch('/health');const j=await r.json();document.getElementById('health').innerHTML='<pre>'+JSON.stringify(j,null,2)+'</pre>'}catch(e){}
        }
        tick(); setInterval(tick, 1500);
      </script>
    </div>
  </div>
</body>
</html>
        """,
        encoding="utf-8",
    )

# ── Utilities ────────────────────────────────────────────────────────────────
MCP_URL = os.getenv("MCP_URL", "http://127.0.0.1:8765")


def _post_mcp(topic: str, payload: dict) -> None:
    try:
        import requests
        requests.post(f"{MCP_URL}/publish", json={"topic": topic, "payload": payload}, timeout=2)
    except Exception:
        pass


def _ensure_mcp_running() -> None:
    try:
        import requests
        r = requests.get(f"{MCP_URL}/", timeout=0.6)
        if r.status_code == 200:
            return
    except Exception:
        pass
    # Try to launch mcp_server.py in background if present
    mcp = ROOT / "mcp_server.py"
    if mcp.exists():
        subprocess.Popen([sys.executable, str(mcp)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# ── AI helpers (optional) ────────────────────────────────────────────────────

def transcribe_audio(path: Path) -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return "(no OPENAI_API_KEY — skipping transcription)"
    try:
        import openai
        client = openai.OpenAI(api_key=key)
        with open(path, "rb") as f:
            res = client.audio.transcriptions.create(model="whisper-1", file=f)
        return getattr(res, "text", "") or res.get("text", "")
    except Exception as e:
        return f"(stt_error) {e}"


def llm_issue_code(client: str, desc: str, transcript: str) -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        # Fallback cheap code
        base = (desc or transcript or "unknown").lower()[:32].replace(" ", "-")
        return f"NF-{int(time.time())}-{base or 'na'}"
    try:
        import openai
        client_oai = openai.OpenAI(api_key=key)
        prompt = (
            "You generate a compact issue code (UPPER_SNAKE) + short rationale.\n"
            f"Client: {client}\nDescription: {desc}\nTranscript: {transcript}\n"
            "Return format: CODE: <CODE> | WHY: <one-liner>\n"
        )
        res = client_oai.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        text = res.choices[0].message.content.strip()
        return text
    except Exception as e:
        return f"NF-{int(time.time())}-ERR | WHY: {e}"


def tts_reply(text: str) -> Optional[str]:
    key = os.getenv("ELEVENLABS_API_KEY")
    if not key:
        return None
    try:
        from elevenlabs import ElevenLabs
        voice = os.getenv("ELEVENLABS_VOICE", "Sarah")
        model = os.getenv("ELEVENLABS_MODEL", "eleven_turbo_v2")
        out = ROOT/"output_audio"; out.mkdir(exist_ok=True)
        cli = ElevenLabs(api_key=key)
        audio = cli.generate(text=text, voice=voice, model=model, output_format="mp3_44100_128")
        fp = out/f"reply_{int(time.time())}.mp3"
        fp.write_bytes(audio)
        return str(fp)
    except Exception:
        return None


# ── FastAPI app ──────────────────────────────────────────────────────────────
app = FastAPI(title="NoizyFish — ROCK MODE", version="1.0")
templates = Jinja2Templates(directory=str(TEMPLATES))

@app.on_event("startup")
async def _startup():
    _ensure_mcp_running()

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("rock.html", {"request": request})

@app.get("/health")
def health():
    return {
        "mcp": MCP_URL,
        "openai_key": bool(os.getenv("OPENAI_API_KEY")),
        "elevenlabs_key": bool(os.getenv("ELEVENLABS_API_KEY")),
        "time": int(time.time()),
    }

@app.post("/upload", response_class=HTMLResponse)
async def upload(
    request: Request,
    client_name: str = Form(...),
    description: str = Form(""),
    voice: UploadFile | None = None,
    image: UploadFile | None = None,
):
    info = {"client": client_name, "desc": description, "ts": int(time.time())}
    if image:
        ip = UPLOADS/f"{int(time.time())}_{image.filename}"
        ip.write_bytes(await image.read())
        info["image"] = str(ip)
    if voice:
        vp = UPLOADS/f"{int(time.time())}_{voice.filename}"
        vp.write_bytes(await voice.read())
        info["voice"] = str(vp)
        info["transcript"] = transcribe_audio(vp)
    info["diagnostic_code"] = llm_issue_code(client_name, description, info.get("transcript", ""))
    reply_path = tts_reply(f"Thanks {client_name}. We logged your case. Code: {info['diagnostic_code']}")
    if reply_path:
        info["reply_path"] = reply_path
    # ship to Mission Control
    _post_mcp("client_intake", info)
    return templates.TemplateResponse("rock.html", {"request": request, "message": "Uploaded & analyzed!", "details": info})


# ── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    print("\n🎸 NoizyFish ROCK MODE on http://127.0.0.1:9090  (MCP will auto-launch if needed)\n")
    uvicorn.run("rock_mode:app", host="127.0.0.1", port=9090, reload=True)