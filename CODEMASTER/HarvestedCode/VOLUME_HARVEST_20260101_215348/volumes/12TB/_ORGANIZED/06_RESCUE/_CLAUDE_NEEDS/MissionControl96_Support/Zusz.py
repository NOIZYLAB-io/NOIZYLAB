from __future__ import annotations
import os, subprocess, shutil
from pathlib import Path
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, PlainTextResponse

ADMIN_TOKEN = os.getenv("NOIZY_ADMIN_TOKEN", "some_long_random_string")
ROOT = Path(__file__).resolve().parents[0]
ENV_FILE = ROOT / ".env"
LOG_FILE = ROOT / "logs" / "noizy.log"

TELEMETRY = []  # populated via /telemetry/push

SYSTEMD_SERVICES = {
    "core": "noizy-core.service",
    "mind": "noizy-mind.service",
}

router = APIRouter()

def _has_systemd() -> bool:
    return shutil.which("systemctl") is not None

def _require_admin(req: Request):
    tok = req.headers.get("x-noizy-admin") or req.query_params.get("token")
    if tok != ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="unauthorized")

@router.get("/admin", response_class=HTMLResponse)
async def admin_index(req: Request):
    _require_admin(req)
    html = (ROOT / "admin_dashboard" / "index.html").read_text(encoding="utf-8")
    return HTMLResponse(html)

@router.get("/admin/api/env")
async def admin_get_env(req: Request):
    _require_admin(req)
    if not ENV_FILE.exists():
        return {"vars": {}}
    lines = ENV_FILE.read_text(encoding="utf-8").splitlines()
    kv = {}
    for ln in lines:
        if not ln.strip() or ln.strip().startswith("#"): continue
        k, _, v = ln.partition("=")
        kv[k.strip()] = v
    return {"vars": kv}

@router.post("/admin/api/env")
async def admin_save_env(req: Request):
    _require_admin(req)
    data = await req.json()
    if not isinstance(data, dict): data = {}
    # merge with existing
    cur = {}
    if ENV_FILE.exists():
        for ln in ENV_FILE.read_text(encoding="utf-8").splitlines():
            if not ln.strip() or ln.strip().startswith("#"):
                continue
            k, _, v = ln.partition("=")
            cur[k.strip()] = v
    cur.update({k: str(v) for k, v in data.items()})
    ENV_FILE.write_text("\n".join(f"{k}={v}" for k, v in cur.items()) + "\n", encoding="utf-8")
    return {"ok": True, "updated": list(data.keys())}

@router.get("/admin/api/telemetry")
async def admin_get_telemetry(req: Request):
    _require_admin(req)
    # Return telemetry data
    return {"events": TELEMETRY[-200:]}

@router.get("/admin/api/logs")
async def admin_get_logs(req: Request, n: int = 500):
    _require_admin(req)
    if not LOG_FILE.exists():
        return PlainTextResponse("no logs yet")
    lines = LOG_FILE.read_text(encoding="utf-8", errors="ignore").splitlines()
    tail = lines[-max(10, min(2000, n)):]
    return PlainTextResponse("\n".join(tail))

@router.get("/admin/api/status")
async def admin_status(req: Request):
    _require_admin(req)
    results = {}
    if _has_systemd():
        for name, svc in SYSTEMD_SERVICES.items():
            try:
                out = subprocess.check_output(["systemctl", "is-active", svc], text=True).strip()
            except subprocess.CalledProcessError:
                out = "inactive"
            results[name] = out
    else:
        for name in SYSTEMD_SERVICES:
            try:
                res = subprocess.check_output(["pgrep", "-f", f"noizy_part1_{name}.py" if name=="core" else "noizy_part2_intelligence.py"])
                results[name] = "running" if res else "stopped"
            except Exception:
                results[name] = "stopped"
    return results

@router.post("/admin/api/restart")
async def admin_restart(req: Request):
    _require_admin(req)
    data = await req.json()
    target = (data.get("target") or "").lower()
    if target not in SYSTEMD_SERVICES:
        raise HTTPException(400, f"invalid target {target}")

    svc = SYSTEMD_SERVICES[target]
    if _has_systemd():
        cmd = ["sudo", "systemctl", "restart", svc]
        subprocess.run(cmd, check=False)
        mode = "systemd"
    else:
        script = f"noizy_part1_{target}.py" if target == "core" else "noizy_part2_intelligence.py"
        subprocess.run(["pkill", "-f", script], check=False)
        subprocess.run(["python3", script], check=False)
        mode = "manual"

    return {"ok": True, "mode": mode, "restarted": target}

@router.post("/admin/api/shutdown")
async def admin_shutdown(req: Request):
    _require_admin(req)
    if _has_systemd():
        for svc in SYSTEMD_SERVICES.values():
            subprocess.run(["sudo", "systemctl", "stop", svc], check=False)
    else:
        os.system("pkill -f noizy_part1_core.py || true")
        os.system("pkill -f noizy_part2_intelligence.py || true")
    return {"ok": True, "message": "Noizy system stopped"}