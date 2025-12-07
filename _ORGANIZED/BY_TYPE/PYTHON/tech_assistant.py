"""
NoizyOS Ultra — GEN-3 AI Technician Assistant Route
====================================================
Merges live Omen stats with AI Tech Brain analysis.
Provides real-time diagnostics, warnings, and repair suggestions.
"""

from fastapi import APIRouter
import httpx
from ..ai.tech_brain import analyze_stats, generate_summary

router = APIRouter()

# Configure your HP Omen's IP address
OMEN_IP = "192.168.1.40"
OMEN_PORT = 8989


@router.get("/live")
async def tech_assistant_live():
    """
    Get live stats from Omen + AI analysis in one hit.
    Returns stats, warnings, suggestions, predictions, and repair plan.
    """
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.get(f"http://{OMEN_IP}:{OMEN_PORT}/stats")
            stats = r.json()
    except httpx.ConnectError:
        return {"error": "Omen offline", "ip": OMEN_IP}
    except httpx.TimeoutException:
        return {"error": "Omen timeout", "ip": OMEN_IP}
    except Exception as e:
        return {"error": str(e)}

    # Run AI analysis
    analysis = analyze_stats(stats)
    summary = generate_summary(analysis)

    return {
        "stats": stats,
        "analysis": analysis,
        "summary": summary,
        "connected": True
    }


@router.get("/analyze")
async def analyze_current():
    """Get just the AI analysis without raw stats."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.get(f"http://{OMEN_IP}:{OMEN_PORT}/stats")
            stats = r.json()
    except:
        return {"error": "Cannot reach Omen"}

    analysis = analyze_stats(stats)
    return analysis


@router.post("/analyze-custom")
def analyze_custom_stats(payload: dict):
    """Analyze custom stats (for testing or manual input)."""
    stats = payload.get("stats", {})
    analysis = analyze_stats(stats)
    summary = generate_summary(analysis)
    return {
        "analysis": analysis,
        "summary": summary
    }


@router.get("/severity")
async def get_severity():
    """Quick severity check — returns just the severity level."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.get(f"http://{OMEN_IP}:{OMEN_PORT}/stats")
            stats = r.json()
    except:
        return {"severity": "unknown", "error": "Cannot reach Omen"}

    analysis = analyze_stats(stats)
    return {
        "severity": analysis["severity"],
        "warning_count": len(analysis["warnings"])
    }


@router.get("/repair-plan")
async def get_repair_plan():
    """Get AI-generated repair plan based on current stats."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.get(f"http://{OMEN_IP}:{OMEN_PORT}/stats")
            stats = r.json()
    except:
        return {"error": "Cannot reach Omen"}

    analysis = analyze_stats(stats)
    return {
        "repair_plan": analysis["repair_plan"],
        "severity": analysis["severity"]
    }


@router.post("/config")
def update_config(payload: dict):
    """Update Omen connection config."""
    global OMEN_IP, OMEN_PORT
    if "ip" in payload:
        OMEN_IP = payload["ip"]
    if "port" in payload:
        OMEN_PORT = payload["port"]
    return {"ok": True, "ip": OMEN_IP, "port": OMEN_PORT}

