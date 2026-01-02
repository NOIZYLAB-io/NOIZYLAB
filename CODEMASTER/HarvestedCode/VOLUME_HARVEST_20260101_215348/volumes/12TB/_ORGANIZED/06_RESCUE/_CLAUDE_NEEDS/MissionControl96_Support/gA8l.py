import requests
import time

PLATFORMS = {
    "Instagram": {
        "login_url": "https://www.instagram.com/accounts/login/",
        "api_url": "https://graph.instagram.com/me",
    },
    "TikTok": {
        "login_url": "https://www.tiktok.com/login",
        "api_url": "https://open-api.tiktok.com/oauth/userinfo/",
    },
    # Add more platforms as needed
}

def check_login_status(platform):
    url = PLATFORMS[platform]["login_url"]
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ {platform} login page reachable.")
        else:
            print(f"⚠️ {platform} login page returned status {response.status_code}.")
    except Exception as e:
        print(f"❌ {platform} login page error: {e}")

def check_api_health(platform):
    url = PLATFORMS[platform]["api_url"]
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ {platform} API reachable.")
        else:
            print(f"⚠️ {platform} API returned status {response.status_code}.")
    except Exception as e:
        print(f"❌ {platform} API error: {e}")

def sync_status():
    print("\n🔄 Platform Sync Status\n")
    for platform in PLATFORMS:
        check_login_status(platform)
        check_api_health(platform)
        print("")
    print("2FA checks and deeper API integration coming soon!")
