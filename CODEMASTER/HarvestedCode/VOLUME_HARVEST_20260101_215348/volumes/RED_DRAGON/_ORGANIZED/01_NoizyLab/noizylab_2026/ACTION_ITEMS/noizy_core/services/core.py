from __future__ import annotations
import uvicorn, threading, time
from fastapi import FastAPI
from .util import mission_api, node_name

app = FastAPI(title="NoizyCore Control")

@app.get("/health")
def health():
    return {"status":"ok","node": node_name()}

# Minimal control plane placeholder
@app.get("/control/info")
def info():
    return {
        "message":"NoizyCore Control Plane",
        "api": mission_api()
    }

if __name__ == "__main__":
    # binds to 8010 to match earlier Mission Control unless you proxy differently
    uvicorn.run(app, host="0.0.0.0", port=8010, log_level="warning")
