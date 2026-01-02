@app.post("/check-code")
async def check_code(code: str, language: str):
    if language == "python":
        with open("temp.py", "w") as f:
            f.write(code)
        lint = subprocess.run(["flake8", "temp.py"], capture_output=True, text=True)
        compile_check = subprocess.run(["python3", "-m", "py_compile", "temp.py"], capture_output=True, text=True)
        return {"lint": lint.stdout or lint.stderr, "compile": compile_check.stderr}
    elif language in ["sh", "bash", "zsh"]:
        with open("temp.sh", "w") as f:
            f.write(code)
        lint = subprocess.run(["shellcheck", "temp.sh"], capture_output=True, text=True)
        return {"lint": lint.stdout or lint.stderr}
    return {"error": "Unsupported language"}
# Health endpoint: status and services
@app.get("/health")
def health():
    return {"status": "green", "services": ["narrator", "dupe-killer", "metadata"]}
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import StreamingResponse
import subprocess, os, hashlib, glob, asyncio

app = FastAPI()

# Narrate text (placeholder until ElevenLabs wired in)
@app.post("/narrate")
async def narrate_text(text: str):
    # This will later call ElevenLabs
    return {"status": "ok", "message": f"Narrating: {text}"}

# Scan WAVs
@app.post("/scan-wavs")
async def scan_wavs():
    files = glob.glob("**/*.wav", recursive=True)
    return {"count": len(files), "files": files[:20]}  # sample list

# Big Dupe Killer
@app.post("/dupe-killer")
async def dupe_killer():
    seen, dupes = {}, []
    for filepath in glob.glob("**/*.wav", recursive=True):
        h = hashlib.md5(open(filepath, "rb").read()).hexdigest()
        if h in seen:
            dupes.append(filepath)
        else:
            seen[h] = filepath
    return {"dupes": dupes, "count": len(dupes)}

# Run a system script
@app.post("/run-script")
async def run_script():
    proc = subprocess.run(["echo", "Hello from Bobby!"], capture_output=True, text=True)
    return {"stdout": proc.stdout.strip(), "stderr": proc.stderr.strip()}
