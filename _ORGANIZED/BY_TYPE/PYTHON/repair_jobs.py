from typing import Dict, List
import time

REPAIR_QUEUE = {}


class RepairJobManager:
    """Automated repair job management"""

    def __init__(self, org_id: str):
        self.org_id = org_id
        if org_id not in REPAIR_QUEUE:
            REPAIR_QUEUE[org_id] = []

    def queue_repair(self, device_id: str, repair_type: str, priority: int = 5) -> Dict:
        """Queue a repair job"""
        job = {
            "job_id": f"repair_{int(time.time())}_{device_id}",
            "device_id": device_id,
            "repair_type": repair_type,
            "priority": priority,
            "status": "queued",
            "created": time.time()
        }
        REPAIR_QUEUE[self.org_id].append(job)
        # Sort by priority
        REPAIR_QUEUE[self.org_id].sort(key=lambda x: x["priority"], reverse=True)
        return {"queued": True, "job_id": job["job_id"]}

    def get_queue(self) -> List[Dict]:
        return REPAIR_QUEUE.get(self.org_id, [])

    def process_next(self) -> Dict:
        """Process next job in queue"""
        queue = REPAIR_QUEUE.get(self.org_id, [])
        if not queue:
            return {"status": "empty"}

        job = queue.pop(0)
        job["status"] = "processing"
        job["started"] = time.time()

        # Simulate repair
        job["status"] = "completed"
        job["completed"] = time.time()

        return job

    def bulk_queue(self, device_ids: List[str], repair_type: str) -> Dict:
        """Queue repairs for multiple devices"""
        jobs = []
        for device_id in device_ids:
            result = self.queue_repair(device_id, repair_type)
            jobs.append(result["job_id"])
        return {"queued": len(jobs), "job_ids": jobs}


def get_repair_manager(org_id: str) -> RepairJobManager:
    return RepairJobManager(org_id)

