from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os, time
from pathlib import Path
import openai
import requests

BASE = Path(__file__).resolve().parent
UPLOADS = BASE / "uploads"
UPLOADS.mkdir(exist_ok=True, parents=True)

app = FastAPI(title="NoizyFish Clean & Fix Portal")
templates = Jinja2Templates(directory=str(BASE / "templates"))

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def upload(
    request: Request,
    client_name: str = Form(...),
    description: str = Form(""),
    voice: UploadFile | None = None,
    image: UploadFile | None = None
):
    info = {"client": client_name, "desc": description, "timestamp": time.time()}
    files_saved = []

    if voice:
        vpath = UPLOADS / f"{int(time.time())}_{voice.filename}"
        with open(vpath, "wb") as f:
            f.write(await voice.read())
        files_saved.append(str(vpath))
        info["voice"] = str(vpath)

    if image:
        ipath = UPLOADS / f"{int(time.time())}_{image.filename}"
        with open(ipath, "wb") as f:
            f.write(await image.read())
        files_saved.append(str(ipath))
        info["image"] = str(ipath)

    # Step 1: Transcribe voice (if exists)
    transcript = ""
    if voice:
        try:
            openai.api_key = os.getenv("OPENAI_API_KEY")
            with open(vpath, "rb") as f:
                res = openai.Audio.transcriptions.create(model="whisper-1", file=f)
            transcript = res.get("text", "")
        except Exception as e:
            transcript = f"[Transcription error: {e}]"
    info["transcript"] = transcript

    # Step 2: Generate diagnostic "code"
    summary_prompt = f"Client: {client_name}\\nDescription: {description}\\nTranscript: {transcript}\\nGenerate a one-line issue code:"
    diag_code = ""
    try:
        res = openai.Chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": summary_prompt}]
        )
        diag_code = res.choices[0].message.content.strip()
    except Exception as e:
        diag_code = f"[AI error: {e}]"
    info["diagnostic_code"] = diag_code

    # Step 3: Send to Mission Control (MCP server)
    try:
        requests.post("http://127.0.0.1:8765/publish", json={"topic": "client_intake", "payload": info}, timeout=2)
    except Exception:
        pass

    return templates.TemplateResponse("upload.html", {
        "request": request,
        "message": "✅ Upload received and analyzed!",
        "details": info
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)