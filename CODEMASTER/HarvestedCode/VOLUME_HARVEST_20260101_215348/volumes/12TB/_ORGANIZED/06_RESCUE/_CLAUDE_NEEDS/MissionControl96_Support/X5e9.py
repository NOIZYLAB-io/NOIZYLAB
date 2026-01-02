import os
from godaddypy import Client, Account
import requests

gd_key = os.getenv('GODADDY_API_KEY')
gd_secret = os.getenv('GODADDY_API_SECRET')
domain = 'missioncontrol96.com'
public_ip = requests.get('https://api64.ipify.org').text

account = Account(api_key=gd_key, api_secret=gd_secret)
client = Client(account)

def update_a_record(name):
    record = {
        'data': public_ip,
        'name': name,
        'type': 'A',
        'ttl': 600
    }
    client.update_records(domain, [record])
    print(f"✅ DNS A record for {name}.{domain} updated to {public_ip}")

if __name__ == '__main__':
    update_a_record('@')
    update_a_record('www')
