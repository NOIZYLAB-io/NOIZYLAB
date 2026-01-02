from ..dlink import service
from ..utils.audit import audit_event

def adopt_clients(from_id, to_id):
    # Placeholder: ask AP to steer clients (model-specific)
    res = service.apply_config(to_id, {"adopt_clients_from": from_id}, dry_run=False)
    audit_event("adopt-clients", to_id, res, extra={"from": from_id})
