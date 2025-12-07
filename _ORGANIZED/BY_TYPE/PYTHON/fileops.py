from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def fileops_ping():
    return {"fileops": "ready"}
