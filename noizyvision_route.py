"""
NoizyVision API Routes
======================
REST API for vision ingestion and analysis.
"""

from fastapi import APIRouter, UploadFile, File, Query
from typing import Optional

router = APIRouter(prefix="/vision", tags=["NoizyVision"])


@router.post("/frame")
async def analyze_frame(
    device: str = Query(..., description="Device ID"),
    file: UploadFile = File(..., description="Frame image data")
):
    """
    Ingest and analyze a frame from a device.
    """
    from ..noizyvision.ingest import ingest_frame
    
    data = await file.read()
    result = ingest_frame(data, device)
    
    return result


@router.post("/snapshot")
async def save_snapshot(
    file: UploadFile = File(...),
    tag: str = Query("vision", description="Snapshot tag"),
):
    """
    Save a snapshot to NoizyDrive.
    """
    from ..noizyvision.snapshot import save_snapshot as save_snap
    
    data = await file.read()
    path = save_snap(data, tag)
    
    return {"saved": True, "path": path}


@router.get("/devices")
async def get_devices():
    """
    Get all devices with vision feeds.
    """
    from ..noizyvision.ingest import get_all_devices
    
    return get_all_devices()


@router.get("/device/{device_id}")
async def get_device_status(device_id: str):
    """
    Get status for a specific device.
    """
    from ..noizyvision.ingest import get_device_status
    
    status = get_device_status(device_id)
    if not status:
        return {"error": "Device not found"}
    
    return status


@router.get("/history")
async def get_analysis_history(limit: int = Query(50, le=200)):
    """
    Get recent analysis history.
    """
    from ..noizyvision.ingest import get_recent_analyses
    
    return get_recent_analyses(limit)


@router.get("/motion")
async def get_motion_devices():
    """
    Get devices currently detecting motion.
    """
    from ..noizyvision.ingest import get_devices_with_motion
    
    return {"devices": get_devices_with_motion()}


@router.get("/faces")
async def get_face_devices():
    """
    Get devices currently detecting faces.
    """
    from ..noizyvision.ingest import get_devices_with_faces
    
    return {"devices": get_devices_with_faces()}


@router.get("/threats")
async def get_threats(limit: int = Query(50, le=200)):
    """
    Get visual threat history.
    """
    from ..noizyvision.shield_bridge import get_threat_history
    
    return get_threat_history(limit)


@router.get("/threats/active")
async def get_active_threats():
    """
    Get currently active threats.
    """
    from ..noizyvision.shield_bridge import get_active_threats
    
    return get_active_threats()


@router.get("/snapshots")
async def list_snapshots(
    tag: Optional[str] = None,
    limit: int = Query(50, le=200)
):
    """
    List saved snapshots.
    """
    from ..noizyvision.snapshot import list_snapshots as list_snaps
    
    return list_snaps(tag, limit)


@router.get("/memory")
async def get_visual_memory(limit: int = Query(50, le=200)):
    """
    Get visual memory entries.
    """
    from ..noizyvision.mind_bridge import get_visual_memory
    
    return get_visual_memory(limit)


@router.get("/memory/search")
async def search_visual_memory(query: str):
    """
    Search visual memory.
    """
    from ..noizyvision.mind_bridge import search_visual_memory
    
    return search_visual_memory(query)


@router.get("/stats")
async def get_vision_stats():
    """
    Get vision system statistics.
    """
    from ..noizyvision.ingest import get_all_devices, get_recent_analyses
    from ..noizyvision.snapshot import get_storage_stats
    from ..noizyvision.mind_bridge import get_memory_stats
    
    return {
        "devices": len(get_all_devices()),
        "recent_analyses": len(get_recent_analyses(100)),
        "storage": get_storage_stats(),
        "memory": get_memory_stats(),
    }

