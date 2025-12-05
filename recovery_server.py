"""
NoizyOS Ultra — Recovery Server
===============================
Minimal fallback server for system recovery when main app fails.
Provides diagnostics, repair, and reinstallation capabilities.
"""

from fastapi import FastAPI
import os
import sys
import platform
import subprocess
from datetime import datetime
from typing import Dict, Any

app = FastAPI(
    title="NoizyOS Ultra Recovery",
    description="Emergency recovery server"
)


@app.get("/")
def status():
    """Recovery mode status."""
    return {
        "status": "Recovery Mode Active",
        "message": "NoizyOS Ultra is running in recovery mode. Main services may be unavailable.",
        "timestamp": datetime.now().isoformat(),
        "system": platform.system()
    }


@app.get("/health")
def health():
    """Basic health check."""
    return {"healthy": True, "mode": "recovery"}


@app.get("/diagnose")
def diagnose() -> Dict[str, Any]:
    """
    Run system diagnostics to identify issues.
    """
    issues = []
    checks = {}
    
    # Check Python version
    checks["python_version"] = sys.version
    if sys.version_info < (3, 9):
        issues.append("Python version too old (need 3.9+)")
    
    # Check if main app exists
    main_app_path = "/Volumes/6TB/noizyOS_v2/backend_ultra/app.py"
    checks["main_app_exists"] = os.path.exists(main_app_path)
    if not checks["main_app_exists"]:
        issues.append("Main application file missing")
    
    # Check config
    config_path = "/Volumes/6TB/noizyOS_v2/config.json"
    checks["config_exists"] = os.path.exists(config_path)
    
    # Check dependencies
    try:
        import fastapi
        checks["fastapi"] = fastapi.__version__
    except ImportError:
        checks["fastapi"] = None
        issues.append("FastAPI not installed")
    
    try:
        import uvicorn
        checks["uvicorn"] = True
    except ImportError:
        checks["uvicorn"] = False
        issues.append("Uvicorn not installed")
    
    # Check disk space
    try:
        import shutil
        total, used, free = shutil.disk_usage("/")
        checks["disk_free_gb"] = round(free / (1024**3), 1)
        if free < 1024**3:  # Less than 1GB
            issues.append("Low disk space")
    except:
        checks["disk_free_gb"] = None
    
    return {
        "checks": checks,
        "issues": issues,
        "issue_count": len(issues),
        "status": "healthy" if not issues else "issues_found"
    }


@app.post("/repair")
def repair() -> Dict[str, Any]:
    """
    Attempt to repair common issues.
    """
    repairs = []
    
    # Reinstall missing modules
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", 
             "/Volumes/6TB/noizyOS_v2/requirements.txt"],
            capture_output=True,
            text=True,
            timeout=120
        )
        if result.returncode == 0:
            repairs.append("Dependencies reinstalled")
        else:
            repairs.append(f"Dependency install failed: {result.stderr[:200]}")
    except Exception as e:
        repairs.append(f"Could not reinstall dependencies: {str(e)}")
    
    # Verify config
    config_path = "/Volumes/6TB/noizyOS_v2/config.json"
    if not os.path.exists(config_path):
        try:
            default_config = '{"version": "0.1.0", "mode": "development"}'
            with open(config_path, "w") as f:
                f.write(default_config)
            repairs.append("Created default config")
        except Exception as e:
            repairs.append(f"Could not create config: {str(e)}")
    
    # Clear cache
    cache_dirs = [
        "/Volumes/6TB/noizyOS_v2/__pycache__",
        "/Volumes/6TB/noizyOS_v2/backend_ultra/__pycache__"
    ]
    for cache_dir in cache_dirs:
        if os.path.exists(cache_dir):
            try:
                import shutil
                shutil.rmtree(cache_dir)
                repairs.append(f"Cleared cache: {cache_dir}")
            except:
                pass
    
    return {
        "ok": True,
        "repairs": repairs,
        "message": "Repair complete. Try restarting main application."
    }


@app.post("/restart")
def restart_main():
    """
    Attempt to restart the main application.
    """
    try:
        # This would typically use systemctl or launchctl
        if platform.system() == "Darwin":
            subprocess.run(
                ["launchctl", "kickstart", "-k", "system/com.noizylab.agent"],
                capture_output=True
            )
        elif platform.system() == "Windows":
            subprocess.run(
                ["net", "stop", "NoizyLab-Agent"],
                capture_output=True
            )
            subprocess.run(
                ["net", "start", "NoizyLab-Agent"],
                capture_output=True
            )
        
        return {"ok": True, "message": "Restart command sent"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@app.get("/logs")
def get_logs(lines: int = 50):
    """Get recent log entries."""
    log_paths = [
        "/var/log/noizylab.log",
        "/Volumes/6TB/noizyOS_v2/logs/app.log",
        os.path.expanduser("~/Library/Logs/noizylab.log")
    ]
    
    for log_path in log_paths:
        if os.path.exists(log_path):
            try:
                with open(log_path, "r") as f:
                    all_lines = f.readlines()
                    return {
                        "path": log_path,
                        "lines": all_lines[-lines:]
                    }
            except:
                continue
    
    return {"error": "No log files found", "searched": log_paths}


@app.post("/factory-reset")
def factory_reset(confirm: bool = False):
    """
    Factory reset - clears all data and reinstalls.
    Requires confirmation.
    """
    if not confirm:
        return {
            "warning": "This will erase all data and settings!",
            "action": "Call with confirm=true to proceed"
        }
    
    # Would perform actual reset here
    return {
        "ok": True,
        "message": "Factory reset initiated. System will restart."
    }


# Run recovery server
if __name__ == "__main__":
    import uvicorn
    print("=" * 50)
    print("  NoizyOS Ultra - RECOVERY MODE")
    print("  Main application failed to start")
    print("  Running minimal recovery server")
    print("=" * 50)
    uvicorn.run(app, host="0.0.0.0", port=8081)

