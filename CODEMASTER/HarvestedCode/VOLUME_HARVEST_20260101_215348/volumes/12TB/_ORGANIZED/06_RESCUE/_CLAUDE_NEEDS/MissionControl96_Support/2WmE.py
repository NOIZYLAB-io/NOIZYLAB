
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI(title="Noizy Vista Demo")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/")
def index():
    return FileResponse("index.html")

@app.get("/handshake")
def handshake():
    return JSONResponse({"status": "ok", "message": "Handshake successful", "machine": "OMEN or Inspiron"})
