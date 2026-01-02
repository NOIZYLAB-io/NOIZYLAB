# Key search email
KEY_EMAIL = "rp@fishmusicinc.com"

import requests
import csv
import time

platforms = [
    {"Platform": "Microsoft", "Login URL": "https://login.microsoftonline.com", "2FA": "enabled"},
    {"Platform": "Instagram", "Login URL": "https://www.instagram.com/accounts/login/", "2FA": "enabled"},
    {"Platform": "TikTok", "Login URL": "https://www.tiktok.com/login", "2FA": "needs setup"},
    {"Platform": "Bandcamp", "Login URL": "https://bandcamp.com/login", "2FA": "unknown"},
    {"Platform": "SoundCloud", "Login URL": "https://soundcloud.com/signin", "2FA": "unknown"},
    {"Platform": "Ko-fi", "Login URL": "https://ko-fi.com/home/login", "2FA": "unknown"},
    {"Platform": "Patreon", "Login URL": "https://www.patreon.com/login", "2FA": "enabled"},
    {"Platform": "Buy Me a Coffee", "Login URL": "https://www.buymeacoffee.com/login", "2FA": "unknown"},
    {"Platform": "Twitter", "Login URL": "https://twitter.com/login", "2FA": "enabled"},
    {"Platform": "Facebook", "Login URL": "https://www.facebook.com/login.php", "2FA": "enabled"},
    {"Platform": "YouTube", "Login URL": "https://accounts.google.com/ServiceLogin?service=youtube", "2FA": "enabled"},
    {"Platform": "LinkedIn", "Login URL": "https://www.linkedin.com/login", "2FA": "enabled"},
    {"Platform": "Reddit", "Login URL": "https://www.reddit.com/login", "2FA": "enabled"},
    {"Platform": "GitHub", "Login URL": "https://github.com/login", "2FA": "enabled"},
    {"Platform": "Dropbox", "Login URL": "https://www.dropbox.com/login", "2FA": "enabled"},
    {"Platform": "Google Drive", "Login URL": "https://accounts.google.com/ServiceLogin?service=wise", "2FA": "enabled"},
    {"Platform": "Zoom", "Login URL": "https://zoom.us/signin", "2FA": "enabled"},
    {"Platform": "Slack", "Login URL": "https://slack.com/signin", "2FA": "enabled"},
    {"Platform": "Discord", "Login URL": "https://discord.com/login", "2FA": "enabled"},
    # Add more platforms as needed
]

def check_platforms():
    results = []
    for p in platforms:
        try:
            response = requests.get(p["Login URL"], timeout=5)
            status = "✅ Online" if response.status_code == 200 else f"⚠️ {response.status_code}"
        except Exception as e:
            status = f"❌ Error: {e}"
        results.append({
            "Platform": p["Platform"],
            "Login Status": status,
            "2FA": p["2FA"]
        })
    return results

def save_sync_log(results, filepath="/Users/rsp_ms/NoizyFish_Aquarium/🐍 Python_Projects/NoizyCockPit/sync_log.csv"):
    if results:
        with open(filepath, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        print(f"📄 Sync log saved to {filepath}")

def sync_status():
    print("\n🔄 Platform Sync Status\n")
    results = check_platforms()
    for r in results:
        print(f"{r['Platform']}: {r['Login Status']} | 2FA: {r['2FA']}")
    save_sync_log(results)

def filter_results_by_email(results, email=KEY_EMAIL):
    # If results contain email field, filter by it
    filtered = [r for r in results if r.get("Email") == email]
    return filtered

def deep_email_summary(email=KEY_EMAIL):
    print(f"\n🔎 Deep Search for: {email}\n")
    results = check_platforms()
    # If platforms or results have email, show those
    filtered = filter_results_by_email(results, email)
    if filtered:
        for r in filtered:
            print(f"{r['Platform']}: {r['Login Status']} | 2FA: {r['2FA']}")
    else:
        print("No direct matches found in sync results.")
    print("\n(For deeper integration, connect account data sources with email fields.)\n")

if __name__ == "__main__":
    print("\n--- Deep Email Sync ---\n")
    deep_email_summary()

# To clone the repository
git clone https://<your-token>@github.com/your-username/fishmusic-cockpit.git

chmod 600 /Users/rsp_ms/NoizyFish_Aquarium/🐍 Python_Projects/NoizyCockPit/credentials.json
chmod 600 /Users/rsp_ms/NoizyFish_Aquarium/🐍 Python_Projects/NoizyCockPit/service_account.json
