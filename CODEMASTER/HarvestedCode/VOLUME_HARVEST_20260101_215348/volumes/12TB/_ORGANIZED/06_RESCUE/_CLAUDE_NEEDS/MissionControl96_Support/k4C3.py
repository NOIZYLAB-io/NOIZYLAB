from .routes.topology import bp as topo_bp
from dlink_dashboard.routes.devices import bp as devices_bp
from .health.sentinel import Sentinel
from .routes.metrics import bp as metrics_bp

sentinel = Sentinel(interval=15)
app = create_app()
sentinel.start(app)

app.register_blueprint(topo_bp)
app.register_blueprint(devices_bp)
app.register_blueprint(metrics_bp)