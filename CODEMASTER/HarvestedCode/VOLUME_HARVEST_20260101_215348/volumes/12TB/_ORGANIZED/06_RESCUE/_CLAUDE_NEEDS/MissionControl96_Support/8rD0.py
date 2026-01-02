from .routes.topology import bp as topo_bp
from dlink_dashboard.routes.devices import bp as devices_bp

app.register_blueprint(topo_bp)
app.register_blueprint(devices_bp)

# ...existing code...