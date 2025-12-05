from fastapi import APIRouter
import psutil, platform, time

router = APIRouter()


@router.get("/")
def get_snapshot():
    return {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "uptime": time.time() - psutil.boot_time(),
        "system": platform.system(),
    }
