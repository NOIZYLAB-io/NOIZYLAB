#!/usr/bin/env python3
"""
Noizy.ai — Part 1: Core Infrastructure
- Creates/loads .env
- Ensures deps; fast boot with retries
- Launches Monetization API (Stripe Checkout, Webhook, License)
- Verifies SMTP for rsp@noizy.ai (optional)
- (Optional) Sync A records at GoDaddy for @, www, portal
- Health endpoint + graceful shutdown
"""

from __future__ import annotations
import os, sys, time, subprocess, signal, json
from pathlib import Path

# ---------- Config ----------
ROOT = Path(__file__).resolve().parent
ENV  = ROOT / ".env"
BIND_HOST = os.getenv("NOIZY_BIND", "127.0.0.1")  # set to 0.0.0.0 on a VPS
API_PORT  = int(os.getenv("NOIZY_PORT", "8000"))
MONETIZATION_MODULE = "noizy_monetization"

# ---------- Helpers ----------
def log(msg: str):
    ts = time.strftime("%H:%M:%S")
    print(f"[CORE {ts}] {msg}", flush=True)

def ensure_env():
    if not ENV.exists():
        (ROOT/".env.example").exists() and ENV.write_text((ROOT/".env.example").read_text())
        if not ENV.exists():
            ENV.write_text(
                "HOSTING_URL=http://127.0.0.1:8000\n"
                "STRIPE_SECRET=sk_test_REPLACE_ME\n"
                "STRIPE_PLAN_PRO=price_test_REPLACE_ME\n"
                "STRIPE_WEBHOOK_SECRET=whsec_test_REPLACE_ME\n"
                "ADMIN_EMAIL=rsp@noizy.ai\n"
                "SUPPORT_EMAIL=rsp@noizy.ai\n"
                "CLIENT_INTAKE_EMAIL=info@noizy.ai\n"
                "CLIENT_INTAKE_PASSWORD=REPLACE_ME\n"
                "SMTP_SERVER=smtp.secureserver.net\n"
                "SMTP_PORT=465\n"
                "SMTP_USER=rsp@noizy.ai\n"
                "SMTP_PASS=REPLACE_ME\n"
                "SMTP_USE_TLS=1\n"
                "GODADDY_API_KEY=\n"
                "GODADDY_API_SECRET=\n"
                "DNS_DOMAIN=noizy.ai\n"
            )
        log("Created .env template. Fill in keys when ready.")

def run(cmd: list[str], check=False) -> int:
    return subprocess.run(cmd, check=check).returncode

def ensure_deps():
    pkgs = [
        "fastapi","uvicorn","pydantic","stripe","PyJWT","python-dotenv",
        "requests","aiofiles","websockets","imapclient"
    ]
    try:
        import fastapi, uvicorn, stripe, jwt  # noqa
    except Exception:
        log("Installing Python dependencies…")
        run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        run([sys.executable, "-m", "pip", "install", *pkgs])

def public_ip(timeout=5) -> str|None:
    try:
        import requests
        return requests.get("https://api.ipify.org", timeout=timeout).text.strip()
    except Exception:
        return None

# ---------- Optional: GoDaddy DNS sync ----------
def sync_godaddy_records():
    try:
        from dotenv import load_dotenv; load_dotenv()
        import requests
        key = os.getenv("GODADDY_API_KEY") or ""
        sec = os.getenv("GODADDY_API_SECRET") or ""
        dom = os.getenv("DNS_DOMAIN","noizy.ai")
        if not (key and sec and dom):
            log("GoDaddy creds missing — skipping DNS sync.")
            return
        ip = public_ip()
        if not ip:
            log("Could not detect public IP — skipping DNS sync.")
            return
        h = {"Authorization": f"sso-key {key}:{sec}", "Content-Type":"application/json"}
        base = f"https://api.godaddy.com/v1/domains/{dom}/records/A"
        for name in ["@", "www", "portal"]:
            body = json.dumps([{"data": ip, "ttl": 600}])
            r = requests.put(f"{base}/{name}", headers=h, data=body, timeout=8)
            if r.status_code >= 400:
                log(f"GoDaddy {name} error {r.status_code}: {r.text[:200]}")
            else:
                log(f"GoDaddy A {name} → {ip} ✔")
    except Exception as e:
        log(f"GoDaddy sync error: {e}")

# ---------- Launch Monetization API ----------
_uvicorn_proc: subprocess.Popen|None = None

def launch_api():
    global _uvicorn_proc
    # Serve the package module: noizy_monetization:app
    _uvicorn_proc = subprocess.Popen([
        sys.executable, "-m", "uvicorn",
        f"{MONETIZATION_MODULE}:app",
        "--host", BIND_HOST, "--port", str(API_PORT),
        "--workers", "1"
    ])
    log(f"Monetization API launching on http://{BIND_HOST}:{API_PORT}")

def api_healthcheck(max_wait=20):
    import time, requests
    url = f"http://{BIND_HOST}:{API_PORT}/"
    for _ in range(max_wait):
        time.sleep(1)
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200:
                log("Monetization API healthy ✔")
                return True
        except Exception:
            pass
    log("Monetization API healthcheck failed.")
    return False

# ---------- SMTP sanity check ----------
def smtp_self_test():
    try:
        from noizy_monetization.emailer import send_license
        # Generate a throwaway license token locally (no Stripe path)
        from noizy_monetization import LICENSE_DIR
        LICENSE_DIR.mkdir(exist_ok=True)
        (LICENSE_DIR/"rsp@noizy.ai.jwt").write_text("TEST_TOKEN")
        send_license("rsp@noizy.ai", "pro")
        log("SMTP test attempted (check mail or local SMTP capture).")
    except Exception as e:
        log(f"SMTP test skipped/failed: {e}")

# ---------- Graceful shutdown ----------
def shutdown(signum=None, frame=None):
    log("Shutting down…")
    try:
        if _uvicorn_proc and _uvicorn_proc.poll() is None:
            _uvicorn_proc.terminate()
            _uvicorn_proc.wait(timeout=6)
    except Exception:
        pass
    sys.exit(0)

def main():
    ensure_env()
    ensure_deps()

    # Optional DNS align (safe to skip during dev)
    if os.getenv("NOIZY_SYNC_DNS","1") == "1":
        sync_godaddy_records()

    # Launch API
    launch_api()
    api_healthcheck()

    # Optional SMTP smoke test (disable by default)
    if os.getenv("NOIZY_SMTP_TEST","0") == "1":
        smtp_self_test()

    log("Core online. Press Ctrl+C to stop.")
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)
    while True:
        # watchdog
        time.sleep(5)
        if _uvicorn_proc and _uvicorn_proc.poll() is not None:
            log("API crashed — restarting…")
            launch_api()

if __name__ == "__main__":
    main()