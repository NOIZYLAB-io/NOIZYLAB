from fastapi import APIRouter
from datetime import datetime
import io
import uuid

router = APIRouter()

# Shared client store
clients = {}

# Report storage
REPORTS = {}


@router.post("/generate")
def generate_report(payload: dict):
    email = payload["email"]
    issue = payload["issue"]
    steps = payload["steps"]
    notes = payload.get("notes", "")

    job_id = str(uuid.uuid4())[:8]
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Build report content (text-based for now, ReportLab optional)
    report_content = f"""
=====================================
       NOIZYLAB REPAIR REPORT
=====================================

Client: {email}
Job ID: {job_id}
Date: {date}

-------------------------------------
ISSUE
-------------------------------------
{issue}

-------------------------------------
REPAIR STEPS
-------------------------------------
"""
    for i, s in enumerate(steps, 1):
        report_content += f"{i}. {s}\n"

    report_content += f"""
-------------------------------------
TECHNICIAN NOTES
-------------------------------------
{notes or 'None'}

=====================================
     Thank you for choosing NoizyLab
           GORUNFREE!
=====================================
"""

    # Store report
    REPORTS[job_id] = {
        "content": report_content,
        "email": email,
        "date": date,
        "issue": issue,
        "hex": report_content.encode().hex()
    }

    # Save to client history if exists
    if email in clients:
        clients[email]["history"].append({
            "date": date,
            "summary": issue,
            "job_id": job_id
        })

    return {
        "ok": True,
        "job_id": job_id,
        "report": report_content
    }


@router.get("/file/{job_id}")
def get_report_file(job_id: str):
    if job_id not in REPORTS:
        return {"error": "not_found"}
    return {"hex": REPORTS[job_id]["hex"], "content": REPORTS[job_id]["content"]}


@router.get("/list")
def list_reports():
    return {"reports": list(REPORTS.keys())}

