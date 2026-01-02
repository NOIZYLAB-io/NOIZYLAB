from fastapi import FastAPI
from pydantic import BaseModel
import subprocess, os

app = FastAPI()

class NarrateRequest(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"narrator": "online", "dupeKiller": "online", "metadataBot": "online", "mcp": "online"}

@app.post("/narrate")
def narrate(req: NarrateRequest):
    # Stub: integrate ElevenLabs here
    return {"status": "ok", "message": f"Narrated: {req.text}"}

@app.get("/scan-wavs")
def scan_wavs():
    # Walk filesystem (stubbed here)
    return {"status": "ok", "files_found": 12}

@app.get("/dupe-killer")
def dupe_killer():
    # Stub duplicate detection
    return {"status": "ok", "duplicates_removed": 27}

@app.get("/run-script")
def run_script():
    # Safe example
    out = subprocess.getoutput("echo 'System script run'")
    return {"status": "ok", "output": out}
