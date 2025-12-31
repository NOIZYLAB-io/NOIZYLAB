# ──────────────────────────────────────────────────────────────────────────────
# FILE: mcp_server.py (Self-Locating, Auto-Launcher, VS-Ready)
# ──────────────────────────────────────────────────────────────────────────────
"""
MCP Server — FastAPI Bridge for Mission Control 96 (Universal Launcher)

Features:
- Works from any directory; automatically locates itself.
- POST /publish — agents post events.
- GET /fetch/{topic} — agents retrieve events.
- Optional WebSocket /stream endpoint (for future live streaming).
- Drop-in MCPClient class replaces EventBus in Mission Control.
- Built-in launcher; just run `python mcp_server.py` from anywhere.

Run:
  pip install fastapi uvicorn pydantic requests
  python mcp_server.py

This will automatically start Uvicorn on port 8765.
"""

# --- Self-locating bootstrap -----------------------------------------------
import os, sys, json, time, threading
from typing import Any, Dict, List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)
os.chdir(CURRENT_DIR)

# ----------------------------------------------------------------------------
# Event schema
# ----------------------------------------------------------------------------
class Event(BaseModel):
    topic: str
    payload: Dict[str, Any]

class BatchEvent(BaseModel):
    events: List[Dict[str, Any]]

# ----------------------------------------------------------------------------
# In-memory event store (thread-safe ring buffer)
# ----------------------------------------------------------------------------
class MemoryStore:
    def __init__(self, limit: int = 4000):
        self.lock = threading.Lock()
        self.events: List[Dict[str, Any]] = []
        self.limit = limit

    def add(self, topic: str, payload: Dict[str, Any]):
        with self.lock:
            event = {"ts": time.time(), "topic": topic, "payload": payload}
            self.events.append(event)
            if len(self.events) > self.limit:
                self.events.pop(0)

    def add_batch(self, events: List[Dict[str, Any]]):
        with self.lock:
            for event_data in events:
                event = {
                    "ts": time.time(), 
                    "topic": event_data["topic"], 
                    "payload": event_data["payload"]
                }
                self.events.append(event)
            while len(self.events) > self.limit:
                self.events.pop(0)

    def fetch(self, topic: str) -> List[Dict[str, Any]]:
        with self.lock:
            return [e for e in self.events if e["topic"] == topic]

    def fetch_since(self, topic: str, since_ts: float) -> List[Dict[str, Any]]:
        with self.lock:
            return [e for e in self.events if e["topic"] == topic and e["ts"] >= since_ts]

store = MemoryStore(limit=4000)

# ----------------------------------------------------------------------------
# FastAPI app setup
# ----------------------------------------------------------------------------
app = FastAPI(title="Mission Control MCP Server", version="1.1")

@app.get("/")
def root():
    return {"status": "running", "events_stored": len(store.events)}

@app.post("/publish")
def publish(event: Event):
    store.add(event.topic, event.payload)
    # best-effort broadcast to websocket listeners
    try:
        import asyncio, json as _json, time as _time
        msg = _json.dumps({"topic": event.topic, "payload": event.payload, "ts": _time.time()})
        for ws in list(clients):
            try:
                asyncio.create_task(ws.send_text(msg))
            except Exception:
                pass
    except Exception:
        pass
    return {"status": "ok", "topic": event.topic, "count": len(store.events)}

@app.post("/publish_batch")
def publish_batch(batch: BatchEvent):
    store.add_batch(batch.events)
    return {"status": "ok", "batch_size": len(batch.events), "count": len(store.events)}

@app.get("/fetch/{topic}")
def fetch(topic: str):
    return store.fetch(topic)

@app.get("/events")
def events(limit: int = 200, topic: str | None = None):
    data = store.events[-limit:]
    if topic:
        data = [e for e in data if e.get("topic") == topic]
    return data

@app.get("/dashboard")
def dashboard():
    html = """
    <!doctype html><html><head><meta charset='utf-8'/><title>Mission Control 96 — Dashboard</title>
    <style>
      body{font-family:system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell; margin:24px;background:#0b0e12;color:#e6edf3}
      .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px}
      .card{background:#11161c;border:1px solid #1f2630;border-radius:14px;padding:16px}
      .title{font-weight:700;margin-bottom:8px}
      pre{white-space:pre-wrap;word-break:break-word;background:#0b0e12;border:1px solid #1f2630;border-radius:8px;padding:8px}
      .status-ok{color:#4caf50} .status-degraded{color:#ff9800} .status-critical{color:#f44336}
    </style></head><body>
    <h1>Mission Control 96 — Live Telemetry</h1>
    <div class='grid'>
      <div class='card'><div class='title'>Diagnostics</div><pre id='diagnostics'>…</pre></div>
      <div class='card'><div class='title'>Repairs</div><pre id='repairs'>…</pre></div>
      <div class='card'><div class='title'>Audio Ops</div><pre id='audio_ops'>…</pre></div>
      <div class='card'><div class='title'>Voice Monitor</div><pre id='voice_monitor'>…</pre></div>
      <div class='card'><div class='title'>DNS Sync</div><pre id='dns_sync'>…</pre></div>
      <div class='card'><div class='title'>Network</div><pre id='net_opt'>…</pre></div>
      <div class='card'><div class='title'>Performance</div><pre id='perf'>…</pre></div>
      <div class='card'><div class='title'>Drive Scanner</div><pre id='drive_scan'>…</pre></div>
    </div>
    <div class='card'><div class='title'>Telemetry</div><pre id='telemetry'>…</pre></div>
    <div class='card'><div class='title'>Remote Sync</div><pre id='remote_sync'>…</pre></div>
    <div class='card'><div class='title'>Predictions</div><pre id='predictions'>…</pre></div>
    <div class='card'><div class='title'>AutoUpdate</div><pre id='autoupdate'>…</pre></div>
    </div>
    <script>
      const topics=["diagnostics","repairs","audio_ops","voice_monitor","dns_sync","net_opt","perf","drive_scan","telemetry","remote_sync","predictions","autoupdate","client_intake","remote_bridge"];
      async function pull(){
        try{
          for(const t of topics){
            const r=await fetch(`/fetch/${t}`);
            const j=await r.json();
            const last=j.length?j[j.length-1].payload: {status:"no data"};
            const el = document.getElementById(t);
            if(el) {
              el.textContent=JSON.stringify(last,null,2);
              // Color code status
              if(last.status === 'ok') el.className = 'status-ok';
              else if(last.status === 'degraded') el.className = 'status-degraded';
              else if(last.status === 'critical') el.className = 'status-critical';
            }
          }
        }catch(e){console.error(e)}
      }
      pull(); setInterval(pull,1500);
    </script>
    </body></html>
    """
    return HTMLResponse(html)

# ----------------------------------------------------------------------------
# Optional WebSocket streaming (basic echo / placeholder for live events)
# ----------------------------------------------------------------------------
clients: List[WebSocket] = []

@app.websocket("/stream")
async def stream(ws: WebSocket):
    await ws.accept(); clients.append(ws)
    try:
        while True:
            # keepalive; broadcasts are sent on publish
            await ws.receive_text()
    except WebSocketDisconnect:
        if ws in clients:
            clients.remove(ws)

# ----------------------------------------------------------------------------
# CLIENT MODULE: replace EventBus in Mission Control 96
# ----------------------------------------------------------------------------
class MCPClient:
    def __init__(self, base_url: str = "http://127.0.0.1:8765"):
        import requests
        self.base = base_url.rstrip("/")
        self.s = requests.Session()

    def publish(self, topic: str, payload: Dict[str, Any]):
        try:
            r = self.s.post(f"{self.base}/publish", json={"topic": topic, "payload": payload}, timeout=3)
            r.raise_for_status()
        except Exception as e:
            print(f"[MCPClient] publish error: {e}")

    def publish_batch(self, events: List[Dict[str, Any]]):
        try:
            r = self.s.post(f"{self.base}/publish_batch", json={"events": events}, timeout=3)
            r.raise_for_status()
        except Exception as e:
            print(f"[MCPClient] publish_batch error: {e}")

    def fetch(self, topic: str) -> List[Dict[str, Any]]:
        try:
            r = self.s.get(f"{self.base}/fetch/{topic}", timeout=3)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            print(f"[MCPClient] fetch error: {e}")
            return []

    def fetch_since(self, topic: str, since_ts: float) -> List[Dict[str, Any]]:
        try:
            # For now, use regular fetch and filter client-side
            events = self.fetch(topic)
            return [e for e in events if e.get("ts", 0) >= since_ts]
        except Exception as e:
            print(f"[MCPClient] fetch_since error: {e}")
            return []

# ----------------------------------------------------------------------------
# Self-launcher — run from anywhere
# ----------------------------------------------------------------------------


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8765)