from fastapi import APIRouter
import time

router = APIRouter()


@router.post("/scan")
def scan():
    # Simulate scan
    time.sleep(0.5)
    return {
        "status": "complete",
        "details": {
            "cpu": "32% load",
            "ram": "47% used",
            "disk": "Good",
            "temp": "54°C",
            "network": "Stable"
        },
        "issues_found": 0,
        "recommendations": []
    }


@router.post("/quickscan")
def quick_scan():
    return {
        "status": "complete",
        "health_score": 92,
        "message": "System is healthy"
    }

