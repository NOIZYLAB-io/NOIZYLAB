# GoDaddy API Setup for MissionControl96
# 1. Install godaddy-api Python SDK
#    pip install godaddypy
# 2. Store your API key/secret securely (use environment variables or .env file)
# 3. Example: Automated DNS update script

import os
from godaddypy import Client, Account

gd_key = os.getenv('GODADDY_API_KEY')
gd_secret = os.getenv('GODADDY_API_SECRET')
domain = 'missioncontrol96.com'
record_type = 'A'
record_name = '@'
public_ip = 'YOUR_PUBLIC_IP'  # Replace with dynamic fetch if needed

account = Account(api_key=gd_key, api_secret=gd_secret)
client = Client(account)

# Update A record
def update_dns():
    client.update_record(domain, record_type, record_name, public_ip)
    print(f"✅ DNS A record for {domain} updated to {public_ip}")

if __name__ == '__main__':
    update_dns()
