"""
Automated GoDaddy + Microsoft 365 Email Setup for fishmusicinc.com
- Checks for Microsoft tenant conflicts
- Verifies GoDaddy DNS for Microsoft 365
- Creates rp@fishmusicinc.com mailbox if safe
- Logs all actions and errors
"""
import requests
import os

GODADDY_API_KEY = os.getenv('GODADDY_API_KEY')
GODADDY_API_SECRET = os.getenv('GODADDY_API_SECRET')
MS365_TOKEN = os.getenv('MS365_TOKEN')  # Microsoft Graph API OAuth token
DOMAIN = 'fishmusicinc.com'
EMAIL = 'rp@fishmusicinc.com'
LOGFILE = os.path.expanduser('~/MissionControl96/DOMAIN_RITUALS/ms365_email_autosetup.log')

headers_gd = {
    'Authorization': f'sso-key {GODADDY_API_KEY}:{GODADDY_API_SECRET}',
    'Accept': 'application/json'
}
headers_ms = {
    'Authorization': f'Bearer {MS365_TOKEN}',
    'Content-Type': 'application/json'
}

def log(msg: str) -> None:
    with open(LOGFILE, 'a') as f:
        f.write(msg + '\n')
    print(msg)

def check_godaddy_dns(domain: str) -> bool:
    url = f'https://api.godaddy.com/v1/domains/{domain}/records/MX'
    resp = requests.get(url, headers=headers_gd)
    if resp.status_code == 200:
        mx_records = resp.json()
        for rec in mx_records:
            if 'outlook.com' in rec.get('data', ''):
                log(f'[OK] MX record for {domain} is set for Microsoft 365.')
                return True
        log(f'[ERROR] MX record for {domain} is not set for Microsoft 365.')
        return False
    else:
        log(f'[ERROR] Could not fetch MX record for {domain}: {resp.text}')
        return False

def check_ms365_tenant(domain: str) -> bool:
    url = f'https://graph.microsoft.com/v1.0/domains/{domain}'
    resp = requests.get(url, headers=headers_ms)
    if resp.status_code == 200:
        log(f'[ERROR] {domain} is already registered to a Microsoft tenant. Manual intervention required.')
        return True
    elif resp.status_code == 404:
        log(f'[OK] {domain} is not registered to any Microsoft tenant.')
        return False
    else:
        log(f'[ERROR] Could not check Microsoft tenant status: {resp.text}')
        return True

def create_ms365_email(email: str) -> bool:
    url = 'https://graph.microsoft.com/v1.0/users'
    payload: dict = {
        "accountEnabled": True,
        "displayName": "RP Fishmusic",
        "mailNickname": "rp",
        "userPrincipalName": email,
        "passwordProfile": {
            "forceChangePasswordNextSignIn": True,
            "password": "TempPassword123!"
        }
    }
    resp = requests.post(url, headers=headers_ms, json=payload)
    if resp.status_code == 201:
        log(f'[OK] Created mailbox for {email}.')
        return True
    else:
        log(f'[ERROR] Failed to create mailbox: {resp.text}')
        return False

def main():
    if not check_godaddy_dns(DOMAIN):
        return
    if check_ms365_tenant(DOMAIN):
        return
    create_ms365_email(EMAIL)

if __name__ == '__main__':
    main()
