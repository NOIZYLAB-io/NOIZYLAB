from .routes.topology import bp as topo_bp

app.register_blueprint(topo_bp)

# ...existing code...