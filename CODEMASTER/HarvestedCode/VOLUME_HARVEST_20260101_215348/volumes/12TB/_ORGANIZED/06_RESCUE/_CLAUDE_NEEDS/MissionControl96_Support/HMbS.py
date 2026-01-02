from __future__ import annotations
import os, time
from uap.protocol import UapEvent, Signer
import requests

from onvif import ONVIFCamera
from wsdiscovery import WSDiscovery

# Constants
SIG = os.getenv("MESH_SHARED_SECRET", "changeme")
UAP_BASE = f"http://{os.getenv('NOIZY_BIND','127.0.0.1')}:{os.getenv('UAP_WS_PORT','8123')}"
signer = Signer(SIG)

DISCOVER_TIMEOUT = 5  # seconds to wait for discovery

def _publish(topic: str, payload: dict):
    body = UapEvent(topic=topic, payload=payload).to_json()
    try:
        requests.post(
            UAP_BASE + "/uap/publish",
            data=body,
            headers={"x-uap-signature": signer.sign(body)},
            timeout=1.5,
        )
    except Exception:
        pass

def discover_onvif():
    wsd = WSDiscovery()
    wsd.start()
    services = wsd.searchServices(timeout=DISCOVER_TIMEOUT)
    # services is list of dictionaries with "XAddrs" etc.
    cams = []
    for s in services:
        xaddrs = s.get("XAddrs", [])
        scopes = s.get("Scopes", [])
        for addr in xaddrs:
            # Only include http/onvif endpoints
            if "http://" in addr or "onvif" in addr.lower():
                cams.append({"xaddr": addr, "scopes": scopes})
    wsd.stop()
    return cams

def try_control(cam_info, username, password):
    """
    Try to connect via ONVIF and fetch snapshot URI
    Returns dict with status
    """
    result = {"xaddr": cam_info["xaddr"]}
    try:
        # parse host / port from xaddr
        # xaddr like http://192.168.1.50:80/onvif/device_service
        import urllib.parse as up
        parsed = up.urlparse(cam_info["xaddr"])
        host = parsed.hostname
        port = parsed.port or 80
        path = parsed.path or "/onvif/device_service"

        cam = ONVIFCamera(host, port, username, password, wsdl_dir=None)
        media = cam.create_media_service()
        profiles = media.GetProfiles()
        token = profiles[0].token
        uri = media.GetSnapshotUri({"ProfileToken": token})
        result["snapshot"] = uri.Uri
        result["status"] = "ok"
    except Exception as e:
        result["error"] = str(e)
        result["status"] = "fail"
    return result

def make_agent(bus=None):
    """
    UAP agent to discover D-Link ONVIF cameras and fetch snapshot
    periodically.
    """
    # config: set credentials to try
    USER = os.getenv("DLINK_ONVIF_USER", "admin")
    PASS = os.getenv("DLINK_ONVIF_PASS", "admin")

    def run():
        try:
            cams = discover_onvif()
            for c in cams:
                info = try_control(c, USER, PASS)
                _publish("dlink_onvif_camera", info)
        except Exception as e:
            _publish("dlink_onvif_camera", {"error": str(e), "status": "discover_fail"})
    return run