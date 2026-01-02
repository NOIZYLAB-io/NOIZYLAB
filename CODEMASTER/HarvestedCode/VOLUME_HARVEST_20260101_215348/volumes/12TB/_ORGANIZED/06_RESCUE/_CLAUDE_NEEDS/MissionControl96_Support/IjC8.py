# GoDaddy Email & DNS Automation for MissionControl96
# Domains: fishmusicinc.com, noizy.ai, noizyfish.com
# Addresses: rp@fishmusicinc.com, info@fishmusicinc.com, rsp@noizy.ai, rsp@noizyfish.com, rsplowman@icloud.com
# All addresses forward to rsplowman@icloud.com

# 1. Add/verify email forwarding in GoDaddy dashboard (manual step, API not public for email setup)
# 2. Automate DNS records for email deliverability


import os
from godaddypy import Client, Account

gd_key = os.getenv('GODADDY_API_KEY')
gd_secret = os.getenv('GODADDY_API_SECRET')
domains = ['fishmusicinc.com', 'noizy.ai', 'noizyfish.com']
mx_record = {
    'type': 'MX',
    'name': '@',
    'data': 'smtp.secureserver.net',
    'priority': 10
}
spf_record = {
    'type': 'TXT',
    'name': '@',
    'data': 'v=spf1 include:secureserver.net ~all'
}
dmarc_record = {
    'type': 'TXT',
    'name': '_dmarc',
    'data': 'v=DMARC1; p=none; rua=mailto:rsplowman@icloud.com'
}

def setup_email_dns(domain, client):
    try:
        client.add_record(domain, mx_record['type'], mx_record['name'], mx_record['data'], mx_record['priority'])
        client.add_record(domain, spf_record['type'], spf_record['name'], spf_record['data'])
        client.add_record(domain, dmarc_record['type'], dmarc_record['name'], dmarc_record['data'])
        print(f"✅ Email DNS records set for {domain}")
    except Exception as e:
        print(f"❌ Error setting DNS for {domain}: {e}")

if __name__ == '__main__':
    if not gd_key or not gd_secret:
        print("❌ GODADDY_API_KEY or GODADDY_API_SECRET not set in environment.")
        exit(1)
    try:
        account = Account(api_key=gd_key, api_secret=gd_secret)
        client = Client(account)
    except Exception as e:
        print(f"❌ Error initializing GoDaddy client: {e}")
        exit(1)
    for d in domains:
        setup_email_dns(d, client)
    print("All addresses will forward to rsplowman@icloud.com (set in GoDaddy dashboard)")
