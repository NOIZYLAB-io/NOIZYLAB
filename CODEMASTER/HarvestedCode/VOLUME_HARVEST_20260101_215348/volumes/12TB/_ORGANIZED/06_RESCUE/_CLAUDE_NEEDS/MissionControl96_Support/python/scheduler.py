from flask import Blueprint, jsonify, request
import threading, time, sched
from ..dlink import service

bp = Blueprint("scheduler", __name__, url_prefix="/api")
scheduler = sched.scheduler(time.time, time.sleep)

jobs = []

@bp.post("/schedule")
def schedule_job():
    data = request.json or {}
    job_type = data.get("type")
    device_id = data.get("device_id")
    when = data.get("when", time.time() + 60)
    job = {"type": job_type, "device_id": device_id, "when": when}
    jobs.append(job)
    scheduler.enterabs(when, 1, run_job, (job,))
    return jsonify({"ok": True, "job": job})

def run_job(job):
    if job["type"] == "reboot":
        service.reboot(job["device_id"], dry_run=False)
    elif job["type"] == "heal":
        service.apply_config(job["device_id"], {"wifi_power": "medium"}, dry_run=False)
    # ...other job types...

threading.Thread(target=scheduler.run, daemon=True).start()

@bp.get("/jobs")
def list_jobs():
    return jsonify({"jobs": jobs})
