from flask import Blueprint, render_template

bp = Blueprint("devices", __name__)

@bp.get("/topology")
def topology_page():
    return render_template("topology.html")

# ...existing code...
