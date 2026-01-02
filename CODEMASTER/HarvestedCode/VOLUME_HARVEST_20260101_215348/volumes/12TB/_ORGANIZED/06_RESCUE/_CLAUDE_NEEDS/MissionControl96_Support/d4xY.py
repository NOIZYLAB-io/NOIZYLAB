#!/usr/bin/env python3
"""
Agent Runner: spins up 96 parallel agents and retries until clean.
"""

import concurrent.futures, subprocess, sys, time

TARGET_SCRIPT = "your_code.py"  # Change to the file you want to test

def worker_task(i):
    try:
        subprocess.run([sys.executable, TARGET_SCRIPT], check=True)
        return f"Agent {i} finished clean."
    except subprocess.CalledProcessError:
        return f"Agent {i} failed."

def run_with_agents(num_agents=96):
    while True:
        with concurrent.futures.ProcessPoolExecutor(max_workers=num_agents) as executor:
            futures = [executor.submit(worker_task, i) for i in range(num_agents)]
            results = [f.result() for f in concurrent.futures.as_completed(futures)]
        if all("finished clean" in r for r in results):
            print("✅ All 96 agents ran clean!")
            break
        else:
            print("❌ Errors detected, retrying in 2s…")
            time.sleep(2)

if __name__ == "__main__":
    run_with_agents()

sudo gem install cocoapods