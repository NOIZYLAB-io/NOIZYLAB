"""
Move all MissionControl96 modules into NoizyFish_Aquarium for clean, unified control.
"""
import os
import shutil

BASE = '/Users/rsp_ms/Desktop/MissionControl96'
TARGET = os.path.join(BASE, 'NoizyFish_Aquarium')

MODULES = [
    ('business_modules/alliance_officer.py', 'business_modules/alliance_officer.py'),
    ('business_modules/intuitive_compliance.py', 'business_modules/intuitive_compliance.py'),
    ('business_modules/nda_manager.py', 'business_modules/nda_manager.py'),
    ('business_modules/idea_manager.py', 'business_modules/idea_manager.py'),
    ('daemons/ai_health.py', 'daemons/ai_health.py'),
    ('daemons/ai_business.py', 'daemons/ai_business.py'),
    ('oracle/dashboard_server.py', 'oracle/dashboard_server.py'),
]

def move_file(src_rel, dst_rel):
    src = os.path.join(BASE, src_rel)
    dst = os.path.join(TARGET, dst_rel)
    dst_dir = os.path.dirname(dst)
    if not os.path.exists(src):
        print(f"Source missing: {src_rel}")
        return
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    if os.path.exists(dst):
        print(f"Already exists: {dst_rel}")
        return
    shutil.move(src, dst)
    print(f"Moved: {src_rel} -> {dst_rel}")

if __name__ == '__main__':
    for src_rel, dst_rel in MODULES:
        move_file(src_rel, dst_rel)
    print("Migration to NoizyFish_Aquarium complete.")
