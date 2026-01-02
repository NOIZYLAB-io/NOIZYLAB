from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter, Request
import time, requests, socket

router = APIRouter()
FLEET = {}

def get_location(ip: str):
    try:
        r = requests.get(f"https://ipapi.co/{ip}/json/", timeout=2)
        data = r.json()
        return {
            "ip": ip,
            "city": data.get("city", ""),
            "region": data.get("region", ""),
            "country": data.get("country_name", ""),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
        }
    except Exception:
        return {"ip": ip, "city": "", "region": "", "country": "", "latitude": 0, "longitude": 0}

@router.post("/api/fleet/heartbeat")
async def heartbeat(req: Request):
    data = await req.json()
    node = data.get("node", socket.gethostname())
    ip = data.get("ip", req.client.host if req.client else "127.0.0.1")
    FLEET[node] = {"ts": time.time(), "ip": ip, "status": "online", "geo": get_location(ip)}
    return {"ok": True}

@router.get("/api/fleet/status")
def status():
    now = time.time()
    results = []
    for node, info in FLEET.items():
        age = now - info["ts"]
        status = "online" if age < 90 else "offline"
        results.append({
            "node": node,
            "status": status,
            "ip": info["ip"],
            "geo": info["geo"],
            "last_seen": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info["ts"])),
            "age_sec": int(age)
        })
    return {"fleet": results, "count": len(results)}

@router.get("/api/fleet/map")
def map_data():
    points = []
    for node, info in FLEET.items():
        g = info.get("geo", {})
        if g.get("latitude") and g.get("longitude"):
            points.append({
                "node": node,
                "status": info.get("status", "online"),
                "lat": g["latitude"],
                "lon": g["longitude"],
                "city": g.get("city", ""),
                "country": g.get("country", "")
            })
    return {"points": points, "count": len(points)}


import psutil

@router.get("/api/fleet/metrics/{node}")
def metrics(node: str):
    return {"cpu": psutil.cpu_percent(), "mem": psutil.virtual_memory().percent}


from fastapi import WebSocket
import asyncio

app = FastAPI()
app.include_router(router)
app.mount("/", StaticFiles(directory="admin_ui", html=True), name="admin_ui")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(1)
        await websocket.send_text('{"status": "live"}')
