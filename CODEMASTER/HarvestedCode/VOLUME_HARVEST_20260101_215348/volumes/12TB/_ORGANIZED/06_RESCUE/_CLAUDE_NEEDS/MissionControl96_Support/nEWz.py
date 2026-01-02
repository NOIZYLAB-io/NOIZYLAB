"""
AutoRun script for NoizyFish_Aquarium
Automatically launches all core modules and dashboard backend for unified control.
"""
import subprocess
import sys
import os

BASE = os.path.dirname(os.path.abspath(__file__))
AQUARIUM = os.path.join(BASE, 'NoizyFish_Aquarium')

modules = [
    os.path.join(AQUARIUM, 'business_modules', 'alliance_officer.py'),
    os.path.join(AQUARIUM, 'business_modules', 'intuitive_compliance.py'),
    os.path.join(AQUARIUM, 'business_modules', 'nda_manager.py'),
    os.path.join(AQUARIUM, 'business_modules', 'idea_manager.py'),
    os.path.join(AQUARIUM, 'daemons', 'ai_health.py'),
    os.path.join(AQUARIUM, 'daemons', 'ai_business.py'),
]

def run_module(path):
    print(f"Launching: {os.path.basename(path)}")
    subprocess.run([sys.executable, path])

def run_dashboard():
    dashboard = os.path.join(AQUARIUM, 'oracle', 'dashboard_server.py')
    print("Starting dashboard backend...")
    subprocess.Popen([sys.executable, dashboard])

if __name__ == '__main__':
    for mod in modules:
        run_module(mod)
    run_dashboard()
    print("All NoizyFish_Aquarium modules launched. Dashboard backend running in background.")
