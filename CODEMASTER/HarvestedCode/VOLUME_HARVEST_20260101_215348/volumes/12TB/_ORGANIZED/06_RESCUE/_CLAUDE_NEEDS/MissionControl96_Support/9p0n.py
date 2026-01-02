import os
from godaddypy import Client, Account
import requests

gd_key = os.getenv('GODADDY_API_KEY')
gd_secret = os.getenv('GODADDY_API_SECRET')
domain = 'missioncontrol96.com'
public_ip = requests.get('https://api64.ipify.org').text

if not gd_key or not gd_secret:
    print("❌ GoDaddy API credentials not set.\nGet your API key/secret at https://sso.godaddy.com/?realm=idp&path=%2Fkeys&app=developer&referrer=sso&auth_reason=1\nThen set them in your shell:\nexport GODADDY_API_KEY='your_api_key'\nexport GODADDY_API_SECRET='your_api_secret'")
    exit(1)

account = Account(api_key=gd_key, api_secret=gd_secret)
client = Client(account)

def update_a_record(name):
    try:
        client.update_record(domain, 'A', name, public_ip)
        print(f"✅ DNS A record for {name}.{domain} updated to {public_ip}")
    except Exception as e:
        print(f"❌ Error updating DNS for {name}.{domain}: {e}")

if __name__ == '__main__':
    update_a_record('@')
    update_a_record('www')
