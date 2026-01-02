from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Serve a simple dashboard page
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return """
    <html>
    <head><title>Mission Control Dashboard</title></head>
    <body>
      <h1>Mission Control Dashboard</h1>
      <p>Agents Online: Diagnostics, Repair, Performance, AudioOps, MemoryKeeper</p>
      <p><a href='/fetch/diagnostics'>View Diagnostics</a></p>
      <p><a href='/generate_playlist'>Generate Playlist</a></p>
      <p><a href='/health'>Health Check</a></p>
    </body>
    </html>
    """

# Mount static files for future expansion
app.mount("/static", StaticFiles(directory="static"), name="static")
