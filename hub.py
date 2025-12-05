from fastapi import APIRouter
from ..services.diagnostics import run_full_scan
from ..services.noizyfix import run_noizyfix

router = APIRouter()


@router.get("/")
def hub_status():
    return {"status": "hub_online"}


@router.post("/scan")
def scan_all(payload: dict):
    return run_full_scan(payload)


@router.post("/noizyfix")
def fix_all(payload: dict):
    return run_noizyfix(payload)
