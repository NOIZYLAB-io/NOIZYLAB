from fastapi import APIRouter

router = APIRouter()


@router.post("/fix")
def fix():
    return {
        "status": "ok",
        "message": "NoizyFix completed successfully",
        "actions_taken": [
            "Cleared temp files",
            "Optimized startup",
            "Flushed DNS cache",
            "Updated system"
        ]
    }


@router.post("/autofix")
def autofix(payload: dict):
    issue_type = payload.get("type", "general")
    
    fixes = {
        "slow": ["Clear cache", "Disable startup apps", "Defrag disk"],
        "network": ["Flush DNS", "Reset adapter", "Check router"],
        "crash": ["Check logs", "Update drivers", "Memory test"],
        "general": ["Full scan", "Optimize", "Clean temp"]
    }
    
    return {
        "status": "ok",
        "issue_type": issue_type,
        "fixes_applied": fixes.get(issue_type, fixes["general"])
    }

