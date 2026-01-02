import os
import yaml
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.user import User
from facebook_business.adobjects.page import Page

def safe_api_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"❌ API Error: {e}")
        return None

def log_pages_to_yaml(pages, filename='fb_pages_log.yaml'):
    data = [{'name': p.get('name'), 'id': p.get('id'), 'category': p.get('category')} for p in pages]
    with open(filename, 'w') as f:
        yaml.dump(data, f)

ACCESS_TOKEN = os.getenv('FB_ACCESS_TOKEN')
APP_ID = os.getenv('FB_APP_ID')
APP_SECRET = os.getenv('FB_APP_SECRET')

FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN)

me = User(fbid='me')
pages = safe_api_call(me.get_accounts)

if pages:
    page_list = [safe_api_call(lambda: page.api_get(fields=['name', 'id', 'category'])) for page in pages]
    page_list = [p for p in page_list if p]
    log_pages_to_yaml(page_list)
    print(f"Logged {len(page_list)} pages to fb_pages_log.yaml")
else:
    print("No pages found or API error.")
