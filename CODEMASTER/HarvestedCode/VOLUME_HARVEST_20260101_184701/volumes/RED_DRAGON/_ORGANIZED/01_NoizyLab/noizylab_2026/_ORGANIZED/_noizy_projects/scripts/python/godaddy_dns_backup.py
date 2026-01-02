"""
Automate GoDaddy DNS Zone Backup
- Uses GoDaddy API to export DNS zone file for all domains
- Stores backup in local directory or pushes to GitHub
"""
import requests
import os
from datetime import datetime

GODADDY_API_KEY = os.getenv('GODADDY_API_KEY')
GODADDY_API_SECRET = os.getenv('GODADDY_API_SECRET')
DOMAINS = ['fishmusicinc.com', 'noizy.ai', 'noizyfish.com']
BACKUP_DIR = os.path.expanduser('~/MissionControl96/backups/dns')

os.makedirs(BACKUP_DIR, exist_ok=True)

headers = {
    'Authorization': f'sso-key {GODADDY_API_KEY}:{GODADDY_API_SECRET}',
    'Accept': 'application/json'
}

def backup_dns(domain):
    url = f'https://api.godaddy.com/v1/domains/{domain}/records'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        ts = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        fname = f'{BACKUP_DIR}/{domain}_dns_{ts}.json'
        with open(fname, 'w') as f:
            f.write(resp.text)
        print(f'Backed up DNS for {domain} to {fname}')
    else:
        print(f'Failed to backup DNS for {domain}: {resp.text}')

if __name__ == '__main__':
    for domain in DOMAINS:
        backup_dns(domain)
