"""
NoizyCore API Routes
====================
REST API for kernel control and monitoring.
"""

from fastapi import APIRouter
from typing import Optional

router = APIRouter(prefix="/core", tags=["NoizyCore"])


@router.get("/status")
async def get_status():
    """
    Get kernel status.
    """
    from ..noizycore.core import get_core
    return get_core().status()


@router.get("/state")
async def get_state():
    """
    Get global state.
    """
    from ..noizycore.state import get_state
    return get_state()


@router.post("/state")
async def update_state(payload: dict):
    """
    Update state values.
    """
    from ..noizycore.state import update_state, update_states
    
    if "key" in payload and "value" in payload:
        return update_state(payload["key"], payload["value"])
    else:
        return update_states(payload)


@router.get("/diagnostics")
async def get_diagnostics():
    """
    Get system diagnostics.
    """
    from ..noizycore.core import get_core
    return get_core().diagnostics()


@router.get("/health")
async def get_health():
    """
    Get full health report.
    """
    from ..noizycore.core import get_core
    return get_core().health_report()


@router.get("/self-check")
async def self_check():
    """
    Run self-check.
    """
    from ..noizycore.core import get_core
    return get_core().self_check()


@router.get("/stable")
async def is_stable():
    """
    Check if system is stable.
    """
    from ..noizycore.core import get_core
    return {"stable": get_core().is_stable()}


@router.get("/modules")
async def get_modules():
    """
    Get module status.
    """
    from ..noizycore.loader import get_module_status, get_load_summary
    return {
        "status": get_module_status(),
        "summary": get_load_summary(),
    }


@router.post("/modules/reload")
async def reload_modules(payload: dict = None):
    """
    Reload modules.
    """
    from ..noizycore.loader import reload_module, reload_all_modules
    
    if payload and "module" in payload:
        result = reload_module(payload["module"])
        return {"module": payload["module"], "success": result is not None}
    else:
        results = reload_all_modules()
        return {"reloaded": len([r for r in results.values() if r])}


@router.get("/heartbeat")
async def get_heartbeat():
    """
    Get heartbeat stats.
    """
    from ..noizycore.heartbeat import get_stats
    return get_stats()


@router.get("/watchdog")
async def get_watchdog():
    """
    Get watchdog status.
    """
    from ..noizycore.watchdog import get_status
    return get_status()


@router.post("/watchdog/enable")
async def enable_module(payload: dict):
    """
    Re-enable a disabled module.
    """
    from ..noizycore.watchdog import enable_module
    return {"success": enable_module(payload["module"])}


@router.get("/events")
async def get_events(limit: int = 100, event_type: Optional[str] = None):
    """
    Get event history.
    """
    from ..noizycore.bus import get_history
    return get_history(limit, event_type)


@router.post("/emit")
async def emit_event(payload: dict):
    """
    Emit an event.
    """
    from ..noizycore.core import get_core
    event = get_core().emit(
        payload.get("type", "custom"),
        payload.get("data", {}),
        payload.get("source", "api")
    )
    return event.to_dict()


@router.get("/uptime")
async def get_uptime():
    """
    Get system uptime.
    """
    from ..noizycore.core import get_core
    return {"uptime_seconds": get_core().uptime()}

