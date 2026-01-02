# DNS Autofix Script for MissionControl96
# Checks and auto-corrects A, MX, CNAME, TXT records for all domains
# Requires: GoDaddy API credentials (GODADDY_API_KEY, GODADDY_API_SECRET)

import requests, os, sys

domains = [
    "fishmusicinc.com",
    "noizy.ai",
    "noizyfish.com",
    "missioncontrol96.com"
]
public_ip = requests.get("https://api64.ipify.org").text
headers = {
    "Authorization": f"sso-key {os.getenv('GODADDY_API_KEY')}:{os.getenv('GODADDY_API_SECRET')}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def fix_a_record(domain):
    url = f"https://api.godaddy.com/v1/domains/{domain}/records/A/@"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        current_ip = resp.json()[0]['data']
        if current_ip != public_ip:
            print(f"[FIX] Updating A record for {domain} from {current_ip} to {public_ip}")
            data = [{"data": public_ip, "ttl": 600}]
            r = requests.put(url, headers=headers, json=data)
            print(f"[RESULT] {r.status_code}: {r.text}")
        else:
            print(f"[OK] A record for {domain} matches public IP.")
    else:
        print(f"[ERROR] Could not fetch A record for {domain}: {resp.text}")

def main():
    for domain in domains:
        fix_a_record(domain)
        # Add MX, CNAME, TXT autofix logic here as needed

if __name__ == "__main__":
    main()
