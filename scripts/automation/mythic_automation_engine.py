# Mythic Automation Engine for Visual Sentinel & NOIZYGRID
# Features: AutoRun, AutoSave, AutoFix, Run Keep Until Complete

import os
import time
import threading
from datetime import datetime

LOG_PATH = "./automation_engine.log"

class AutomationEngine:
    def __init__(self):
        self.jobs = []
        self.running = True
        self.log("Mythic Automation Engine started.")

    def log(self, msg):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_PATH, "a") as f:
            f.write(f"[{timestamp}] {msg}\n")
        print(f"🧾 {msg}")

    def add_job(self, job_func, name):
        self.jobs.append({"func": job_func, "name": name, "status": "pending", "retries": 0})
        self.log(f"Job added: {name}")

    def run_jobs(self):
        while self.running:
            for job in self.jobs:
                if job["status"] != "complete":
                    try:
                        self.log(f"AutoRun: Executing {job['name']}")
                        job["func"]()
                        job["status"] = "complete"
                        self.log(f"AutoSave: {job['name']} completed and saved.")
                    except Exception as e:
                        job["retries"] += 1
                        self.log(f"AutoFix: {job['name']} failed (attempt {job['retries']}). Error: {e}")
                        if job["retries"] < 5:
                            self.log(f"Run Keep Until Complete: Retrying {job['name']}...")
                        else:
                            self.log(f"Run Keep Until Complete: {job['name']} failed after 5 attempts.")
            time.sleep(5)

    def stop(self):
        self.running = False
        self.log("Mythic Automation Engine stopped.")

# Example job functions
def heal_node():
    # Simulate healing
    print("Healing node...")
    time.sleep(2)

def silence_node():
    # Simulate silence enforcement
    print("Enforcing silence...")
    time.sleep(1)

def save_snapshot():
    # Simulate snapshot
    print("Saving snapshot...")
    time.sleep(1)

if __name__ == "__main__":
    engine = AutomationEngine()
    engine.add_job(heal_node, "Heal Node")
    engine.add_job(silence_node, "Silence Node")
    engine.add_job(save_snapshot, "Save Snapshot")
    t = threading.Thread(target=engine.run_jobs)
    t.start()
    # Let it run for demonstration
    time.sleep(20)
    engine.stop()
    t.join()
