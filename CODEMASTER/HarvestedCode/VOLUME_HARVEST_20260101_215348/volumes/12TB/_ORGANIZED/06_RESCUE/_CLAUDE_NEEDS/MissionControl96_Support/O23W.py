from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Noizy Vista Demo")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/")
def index():
    return FileResponse("index.html")
