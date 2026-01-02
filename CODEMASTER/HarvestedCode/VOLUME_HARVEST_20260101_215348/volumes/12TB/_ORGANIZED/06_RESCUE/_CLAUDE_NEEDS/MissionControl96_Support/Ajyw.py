# NoizyFish Autorun - Full Universe Setup & Execution
# Author: Rob Plowman + Copilot

import os, yaml, subprocess
from datetime import datetime

BASE = os.path.expanduser("~/Desktop/NoizyFish")
folders = ["scripts", "env", "logs", "voice", "branding", "legacy"]

def create_folders():
    for folder in folders:
        path = os.path.join(BASE, folder)
        os.makedirs(path, exist_ok=True)
        print(f"📁 Created: {path}")

def create_env():
    env_path = os.path.join(BASE, "env", ".env")
    if not os.path.exists(env_path):
        env_content = """FB_ACCESS_TOKEN=your-access-token
FB_APP_ID=your-app-id
FB_APP_SECRET=your-app-secret
PRIMARY_PAGE_ID=your-main-page-id
"""
        with open(env_path, "w") as f:
            f.write(env_content)
        print(f"🔐 .env template created at {env_path}")
    else:
        print("🔐 .env already exists.")

def create_brand_kit():
    branding_yaml = {
        "name": "NoizyFish",
        "bio": "Conceptualist Composer | Mad Scientist of Sound & Systems | Founder of Noizy.AI",
        "logo": "branding/logo.svg",
        "cover": "branding/cover_image.png",
        "colors": ["#0F0F0F", "#FF00FF", "#00FFFF"],
        "fonts": ["Orbitron", "Roboto Mono"]
    }
    path = os.path.join(BASE, "branding", "brand_kit.yaml")
    with open(path, "w") as f:
        yaml.dump(branding_yaml, f)
    print(f"🎨 Brand kit saved at {path}")

def autosave_status(status):
    path = os.path.join(BASE, "logs", "autorun_status.yaml")
    with open(path, "w") as f:
        yaml.dump(status, f)
    print(f"🧾 Autorun status saved at {path}")

def run_modules():
    modules = [
        "scripts/token_manager.py",
        "scripts/noizyfb_consolidator.py",
        "scripts/admin_snapshot.py",
        "scripts/legacy_sync.py"
    ]
    for module in modules:
        path = os.path.join(BASE, module)
        if os.path.exists(path):
            print(f"🚀 Running: {path}")
            subprocess.run(["python3", path])
        else:
            print(f"⚠️ Missing: {path}")

if __name__ == "__main__":
    print("🔧 Booting NoizyFish Universe...")
    create_folders()
    create_env()
    create_brand_kit()
    run_modules()
    autosave_status({
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "modules_run": ["token_manager", "noizyfb_consolidator", "admin_snapshot", "legacy_sync"],
        "status": "complete"
    })
    print("✅ NoizyFish Universe is live and clean.")
