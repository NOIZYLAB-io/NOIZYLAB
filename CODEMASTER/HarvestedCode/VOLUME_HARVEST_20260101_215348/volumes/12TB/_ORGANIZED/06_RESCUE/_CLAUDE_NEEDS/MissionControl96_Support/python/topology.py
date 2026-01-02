from flask import Blueprint, jsonify
from ..dlink import service

bp = Blueprint("topology", __name__, url_prefix="/api")

@bp.get("/topology")
def topology():
    devices = service.list_devices()
    nodes, edges = [], []

    # Devices as nodes
    for d in devices:
        s = service.device_status(d.id)
        nodes.append({
            "data": {"id": d.id, "label": f"{d.name}\n{d.model}", "type": "device",
                     "online": s.online, "cpu": s.cpu, "mem": s.mem, "firmware": s.firmware}
        })
        # Clients as child nodes and edges
        for c in service.device_clients(d.id):
            cid = f"cli-{c.mac}"
            nodes.append({"data": {"id": cid, "label": c.hostname or c.mac, "type": "client", "signal": c.signal}})
            edges.append({"data": {"id": f"{cid}-{d.id}", "source": cid, "target": d.id, "signal": c.signal}})

    # Optional: infer device-to-device links (uplink/backhaul) from status if available
    # edges.append({"data": {"id": "DL-002-DL-001", "source": "DL-002", "target": "DL-001", "type": "uplink"}})

    return jsonify({"nodes": nodes, "edges": edges})
