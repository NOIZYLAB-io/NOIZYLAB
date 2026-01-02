
import requests
import csv
import time

platforms = [
    {
        "Platform": "Microsoft",
        "Login URL": "https://login.microsoftonline.com",
        "2FA": "enabled"
    },
    {
        "Platform": "Instagram",
        "Login URL": "https://www.instagram.com/accounts/login/",
        "2FA": "enabled"
    },
    {
        "Platform": "TikTok",
        "Login URL": "https://www.tiktok.com/login",
        "2FA": "needs setup"
    }
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

def save_sync_log(results, filepath="data/sync_log.csv"):
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
