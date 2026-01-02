from __future__ import annotations
import time
from fastapi import APIRouter, Request

router = APIRouter()
FLEET = {}  # node_id -> {"ts": timestamp, "status": "online/offline"}

@router.post("/api/fleet/heartbeat")
async def heartbeat(req: Request):
    data = await req.json()
    node = data.get("node", "unknown")
    FLEET[node] = {"ts": time.time(), "status": "online"}
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
            "last_seen": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info["ts"])),
            "age_sec": int(age)
        })
    return {"fleet": results, "count": len(results)}