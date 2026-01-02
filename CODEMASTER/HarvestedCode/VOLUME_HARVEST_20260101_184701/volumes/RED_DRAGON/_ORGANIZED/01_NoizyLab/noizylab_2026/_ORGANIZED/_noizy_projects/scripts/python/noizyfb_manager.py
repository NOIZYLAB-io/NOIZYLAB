# SureFire NoizyFB Manager - All-In-One Facebook Cleanup
# Author: Rob Plowman + Copilot

import os, yaml, argparse
from datetime import datetime
from dotenv import load_dotenv
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.user import User
from facebook_business.adobjects.page import Page

# 🔐 Load credentials
load_dotenv()
ACCESS_TOKEN = os.getenv('FB_ACCESS_TOKEN')
APP_ID = os.getenv('FB_APP_ID')
APP_SECRET = os.getenv('FB_APP_SECRET')
FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN)

# 🔧 Safe API wrapper
def safe_api_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"❌ API Error: {e}")
        return None

# 📄 List all Pages
def list_pages():
    me = User(fbid='me')
    return safe_api_call(me.get_accounts)

# 🔍 Audit Page metadata
def audit_page(page_id):
    page = Page(page_id)
    details = safe_api_call(page.api_get, fields=['name', 'about', 'fan_count', 'category'])
    if details:
        print(f"\n📄 Page: {details['name']}")
        print(f"🗂 Category: {details.get('category')}")
        print(f"👥 Fans: {details.get('fan_count')}")
        print(f"📝 About: {details.get('about')}")

# 🔐 Snapshot admin roles
def get_admins(page_id):
    page = Page(page_id)
    roles = safe_api_call(page.get_user_permissions)
    if roles:
        for role in roles:
            print(f"👤 User: {role['user']}, Role: {role['role']}")

# 🧾 YAML snapshot with timestamped backup
def log_pages_snapshot(pages, filename='fb_pages_log.yaml'):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup = f"{filename.replace('.yaml', '')}_{timestamp}.yaml"
    data = {
        'timestamp': timestamp,
        'pages': [{'name': p['name'], 'id': p['id'], 'category': p.get('category')} for p in pages]
    }
    with open(filename, 'w') as f:
        yaml.dump(data, f)
    with open(backup, 'w') as f:
        yaml.dump(data, f)
    print(f"✅ Snapshot saved: {filename} and {backup}")

# ⚠️ Flag duplicate Pages
def flag_duplicates(pages):
    seen = {}
    for page in pages:
        name = page['name'].lower()
        if name in seen:
            print(f"⚠️ Duplicate: {name} → {page['id']} and {seen[name]}")
        else:
            seen[name] = page['id']

# 🔄 Suggest manual merges
def suggest_merges(pages):
    name_map = {}
    for page in pages:
        name = page['name'].lower()
        if name in name_map:
            print(f"🔄 Suggest merge: {name_map[name]} ↔ {page['id']}")
        else:
            name_map[name] = page['id']

# 🚀 Run full fixer
def run_all():
    pages = list_pages()
    if not pages:
        print("❌ No Pages found or API error.")
        return
    log_pages_snapshot(pages)
    flag_duplicates(pages)
    suggest_merges(pages)
    for page in pages:
        audit_page(page['id'])
        get_admins(page['id'])

# 🧭 CLI launcher
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SureFire NoizyFB Manager")
    parser.add_argument('--run', action='store_true', help='Run full Facebook cleanup')
    args = parser.parse_args()
    if args.run:
        run_all()
