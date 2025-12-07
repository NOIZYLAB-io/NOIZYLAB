from fastapi import APIRouter

router = APIRouter()


@router.get("/repairplan")
def get_default_plan():
    return {
        "steps": [
            "Clear temp files",
            "Check startup programs",
            "Optimize registry",
            "Check drive health",
            "Apply OS patches",
            "Final system test"
        ]
    }


@router.post("/repairplan")
def generate_plan(payload: dict):
    issue = payload.get("issue", "").lower()
    
    plans = {
        "slow": [
            "Run performance diagnostics",
            "Identify resource-heavy processes",
            "Clear temporary files",
            "Disable unnecessary startup programs",
            "Check for malware",
            "Optimize disk",
            "Verify fix with benchmark"
        ],
        "crash": [
            "Check system event logs",
            "Run memory diagnostics",
            "Update device drivers",
            "Check disk integrity",
            "Scan for corrupted files",
            "Apply stability patches",
            "Monitor for 24 hours"
        ],
        "network": [
            "Test connection speed",
            "Flush DNS cache",
            "Reset network adapter",
            "Check router status",
            "Verify firewall settings",
            "Test with alternate DNS",
            "Confirm stable connection"
        ],
        "virus": [
            "Disconnect from network",
            "Boot in safe mode",
            "Run full antivirus scan",
            "Remove detected threats",
            "Check browser extensions",
            "Reset browser settings",
            "Reconnect and verify clean"
        ]
    }
    
    # Find matching plan
    for key in plans:
        if key in issue:
            return {"steps": plans[key], "issue_type": key}
    
    return {"steps": plans.get("slow"), "issue_type": "general"}

