from fastapi import APIRouter
import httpx

router = APIRouter()

# Configure your HP Omen's IP address here
OMEN_IP = "192.168.1.40"
OMEN_PORT = 8989


@router.get("/omen/live")
async def omen_live():
    """Get live stats from HP Omen"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.get(f"http://{OMEN_IP}:{OMEN_PORT}/stats")
            return r.json()
    except httpx.ConnectError:
        return {"error": "OMEN offline", "ip": OMEN_IP}
    except httpx.TimeoutException:
        return {"error": "OMEN timeout", "ip": OMEN_IP}
    except Exception as e:
        return {"error": str(e)}


@router.get("/omen/health")
async def omen_health():
    """Quick health check from HP Omen"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.get(f"http://{OMEN_IP}:{OMEN_PORT}/health")
            return r.json()
    except:
        return {"status": "offline", "ip": OMEN_IP}


@router.get("/omen/processes")
async def omen_processes():
    """Get running processes from HP Omen"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.get(f"http://{OMEN_IP}:{OMEN_PORT}/processes")
            return r.json()
    except:
        return {"error": "OMEN offline"}


@router.post("/omen/command")
async def omen_command(payload: dict):
    """Send a command to HP Omen"""
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            r = await client.post(
                f"http://{OMEN_IP}:{OMEN_PORT}/command",
                json=payload
            )
            return r.json()
    except:
        return {"error": "OMEN offline"}


@router.post("/omen/config")
def update_omen_config(payload: dict):
    """Update Omen IP configuration"""
    global OMEN_IP, OMEN_PORT
    if "ip" in payload:
        OMEN_IP = payload["ip"]
    if "port" in payload:
        OMEN_PORT = payload["port"]
    return {"ok": True, "ip": OMEN_IP, "port": OMEN_PORT}


@router.get("/omen/config")
def get_omen_config():
    """Get current Omen configuration"""
    return {"ip": OMEN_IP, "port": OMEN_PORT}

