from fastapi import APIRouter
from ..services.advanced_diagnostics import run_full_suite

router = APIRouter()


@router.get("/")
def run_adv():
    return run_full_suite()

