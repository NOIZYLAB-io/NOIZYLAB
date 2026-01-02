from flask import Blueprint, Response
from ..dlink import service

bp = Blueprint("metrics", __name__)

@bp.get("/metrics")
def metrics():
    devices = service.list_devices()
    lines = []
    for d in devices:
        s = service.device_status(d.id)
        lines += [
            f'grid_device_online{{id="{d.id}"}} {1 if s.online else 0}',
            f'grid_device_cpu{{id="{d.id}"}} {s.cpu}',
            f'grid_device_mem{{id="{d.id}"}} {s.mem}',
        ]
    return Response("\n".join(lines) + "\n", mimetype="text/plain")
