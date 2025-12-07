"""NoizyFlow API Routes"""
from fastapi import APIRouter
from ..noizyflow.store import save_workflow, list_workflows, get_workflow, delete_workflow, get_run_history

router = APIRouter(prefix="/flow", tags=["NoizyFlow"])

@router.post("/create")
def create(payload: dict):
    return save_workflow(payload)

@router.get("/all")
def all_flows():
    return [w.to_dict() if hasattr(w, 'to_dict') else w for w in list_workflows()]

@router.get("/{flow_id}")
def get_flow(flow_id: str):
    return get_workflow(flow_id)

@router.delete("/{flow_id}")
def del_flow(flow_id: str):
    return {"deleted": delete_workflow(flow_id)}

@router.get("/history/runs")
def runs(limit: int = 50):
    return [r.to_dict() if hasattr(r, 'to_dict') else r for r in get_run_history(limit)]

