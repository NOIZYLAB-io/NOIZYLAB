"""
NoizyHome API Routes
====================
Smart home control and environmental intelligence endpoints.
"""

from fastapi import APIRouter
from typing import Optional
from ..noizyhome.mood_engine import choose_environment, apply_preset, get_preset
from ..noizyhome.hvac_predict import predict_hvac, get_hvac_schedule, get_efficiency_report
from ..noizyhome.sensor_fusion import fuse_sensors, get_current_state, get_trend
from ..noizyhome.room_fingerprint import identify_room, register_room, list_rooms
from ..noizyhome.room_memory import (
    update_room_memory, 
    get_room_profile, 
    predict_room_use,
    get_room_insights,
    suggest_room_for_activity,
)
from ..noizyhome.access_guard import (
    evaluate_access,
    get_access_status,
    get_access_log,
    get_alerts,
    get_occupancy_summary,
)


router = APIRouter()


# === ENVIRONMENT CONTROL ===

@router.post("/home/mood")
def set_mood_environment(payload: dict):
    """
    Set environment based on mood, energy, and stress.
    """
    return choose_environment(
        mood=payload.get("mood", "neutral"),
        energy=payload.get("energy", 0.5),
        stress=payload.get("stress", "low"),
        time_of_day=payload.get("time_of_day"),
    )


@router.post("/home/preset/{name}")
def apply_environment_preset(name: str):
    """
    Apply a named environment preset.
    """
    return apply_preset(name)


@router.get("/home/preset/{name}")
def get_environment_preset(name: str):
    """
    Get a preset configuration.
    """
    preset = get_preset(name)
    if not preset:
        return {"error": "Unknown preset"}
    return preset


# === HVAC ===

@router.post("/home/hvac")
def get_hvac_adjustment(payload: dict):
    """
    Get predicted HVAC adjustment.
    """
    return {"adjust": predict_hvac(payload)}


@router.get("/home/hvac/schedule")
def hvac_schedule():
    """
    Get HVAC schedule for the day.
    """
    return get_hvac_schedule()


@router.get("/home/hvac/efficiency")
def hvac_efficiency(days: int = 7):
    """
    Get HVAC efficiency report.
    """
    return get_efficiency_report(days)


# === SENSORS ===

@router.post("/home/sensors/fuse")
def fuse_sensor_data(payload: dict):
    """
    Fuse sensor data into unified state.
    """
    return fuse_sensors(payload)


@router.get("/home/sensors/state")
def get_sensor_state():
    """
    Get current fused sensor state.
    """
    return get_current_state()


@router.get("/home/sensors/trend/{metric}")
def get_sensor_trend(metric: str, minutes: int = 30):
    """
    Get trend for a specific metric.
    """
    return get_trend(metric, minutes)


# === ROOMS ===

@router.post("/home/room/identify")
def identify_current_room(payload: dict):
    """
    Identify room from sensor data.
    """
    room_id = identify_room(payload)
    return {"room_id": room_id}


@router.post("/home/room/register")
def register_new_room(payload: dict):
    """
    Register a new room.
    """
    room_id = register_room(payload.get("data", {}), payload.get("name"))
    return {"room_id": room_id}


@router.get("/home/rooms")
def list_all_rooms():
    """
    List all registered rooms.
    """
    return {"rooms": list_rooms()}


@router.post("/home/room/{room_id}/activity")
def log_room_activity(room_id: str, payload: dict):
    """
    Log activity in a room.
    """
    return {"history": update_room_memory(room_id, payload)}


@router.get("/home/room/{room_id}/profile")
def room_profile(room_id: str):
    """
    Get learned profile for a room.
    """
    return get_room_profile(room_id) or {"message": "No profile yet"}


@router.get("/home/room/{room_id}/predict")
def predict_room_activity(room_id: str, hour: Optional[int] = None):
    """
    Predict room usage at a given time.
    """
    return predict_room_use(room_id, hour)


@router.get("/home/room/{room_id}/insights")
def room_insights(room_id: str):
    """
    Get insights about room usage.
    """
    return get_room_insights(room_id)


@router.get("/home/suggest/{activity}")
def suggest_room(activity: str):
    """
    Suggest best room for an activity.
    """
    room = suggest_room_for_activity(activity)
    return {"suggested_room": room}


# === ACCESS & SECURITY ===

@router.post("/home/access/event")
def log_access_event(payload: dict):
    """
    Log and evaluate an access event.
    """
    alert = evaluate_access(payload)
    return {"alert": alert}


@router.get("/home/access/status")
def access_status():
    """
    Get status of all access points.
    """
    return get_access_status()


@router.get("/home/access/log")
def access_log(limit: int = 50, location: Optional[str] = None):
    """
    Get access event history.
    """
    return {"events": get_access_log(limit, location)}


@router.get("/home/access/alerts")
def access_alerts(hours: int = 24):
    """
    Get recent access alerts.
    """
    return {"alerts": get_alerts(hours)}


@router.get("/home/occupancy")
def occupancy():
    """
    Get current occupancy summary.
    """
    return get_occupancy_summary()

