#!/usr/bin/env python3
import os, sys, time, webbrowser, requests
from dotenv import load_dotenv

BANNER = """
🟣 Webador → GoDaddy: Interactive Transfer + DNS Script
------------------------------------------------------
This script will:
  1) Open Webador so you can unlock your domain and get the EPP/Auth code
  2) Open GoDaddy's transfer page so you can start the transfer
  3) Poll GoDaddy's API until the domain appears on your account
  4) Apply Microsoft 365 DNS records (MX, SPF, autodiscover CNAME)

It won't store your Webador/GoDaddy passwords.
"""

def die(msg):
    print(f"❌ {msg}")
    sys.exit(1)

def wait_enter(msg):
    input(f"\n{msg}\nPress Enter to continue...")

def open_url(u):
    try:
        webbrowser.open(u, new=2)
    except Exception:
        print(f"👉 Please open this URL manually: {u}")

def gd_headers(key, secret):
    return {"Authorization": f"sso-key {key}:{secret}", "Content-Type": "application/json"}

def gd_get_domain(base, headers, domain):
    r = requests.get(f"{base}/v1/domains/{domain}", headers=headers)
    return r

def gd_upsert_record(base, headers, domain, type_, name, data, ttl=600, priority=None):
    url = f"{base}/v1/domains/{domain}/records/{type_}/{name}"
    rec = {"data": data, "ttl": ttl}
    if priority is not None:
        rec["priority"] = priority
    r = requests.put(url, headers=headers, json=[rec])
    if r.status_code not in (200, 201, 204):
        raise RuntimeError(f"{type_} {name} -> {data} failed: {r.status_code} {r.text}")
    print(f"✅ {type_:<5} {name:<15} -> {data}")

def main():
    print(BANNER)

    # Load env
    load_dotenv()
    api_key = os.getenv("GODADDY_API_KEY")
    api_secret = os.getenv("GODADDY_API_SECRET")
    domain = os.getenv("DOMAIN")
    if not (api_key and api_secret and domain):
        die("Missing GODADDY_API_KEY / GODADDY_API_SECRET / DOMAIN in .env")

    mx_host = os.getenv("MX_HOST", "").strip()
    mx_prio = int(os.getenv("MX_PRIORITY", "0"))
    spf_txt = os.getenv("SPF_TXT", "").strip()
    autodisc = os.getenv("AUTODISCOVER_CNAME", "autodiscover.outlook.com").strip()

    base = "https://api.godaddy.com"
    headers = gd_headers(api_key, api_secret)

    # STEP 1: Webador → get EPP/Auth code
    print("\nSTEP 1 — Get your EPP/Auth code from Webador")
    print("   1) Log in and go to: My subscription → Manage domains → Transfer")
    print("   2) Unlock the domain if needed, request the EPP/Auth code (it may email it to you)")
    open_url("https://www.webador.com/login")
    wait_enter("After you have your EPP/Auth code (copy it), return here.")

    epp = input("Paste your EPP/Auth code: ").strip()
    if not epp:
        die("No EPP/Auth code provided.")

    # STEP 2: GoDaddy transfer
    print("\nSTEP 2 — Start the transfer at GoDaddy")
    print("   1) Paste your domain and the EPP/Auth code when prompted")
    open_url("https://www.godaddy.com/domains/transfer")
    wait_enter("Submit the transfer in your browser, then come back here.")

    print("\nSTEP 3 — Poll GoDaddy until domain is visible on your account")
    print("   (This checks whether the domain object is accessible via your GoDaddy API keys.)")
    print("   We'll try for up to ~15 minutes. You can also hit Ctrl+C and run again later.")

    attempts = 0
    max_attempts = 90  # 90 * 10s = 900s (~15min)
    while attempts < max_attempts:
        r = gd_get_domain(base, headers, domain)
        if r.status_code == 200:
            print(f"🎉 Domain '{domain}' is now visible in your GoDaddy account.")
            break
        elif r.status_code == 404:
            attempts += 1
            if attempts % 6 == 0:
                print("...still waiting (ask Webador to approve/expedite if it's been hours).")
            time.sleep(10)
        else:
            print(f"GoDaddy API response: {r.status_code} {r.text}")
            print("We'll keep polling, but verify your API key/secret if this persists.")
            attempts += 1
            time.sleep(10)
    else:
        die("Timed out waiting for the domain to appear in GoDaddy. Re-run this script later to continue.")

    # STEP 4: DNS setup for Microsoft 365
    print("\nSTEP 4 — Apply Microsoft 365 DNS (you can edit .env to change values)")
    try:
        if autodisc:
            gd_upsert_record(base, headers, domain, "CNAME", "autodiscover", autodisc)
        if spf_txt:
            gd_upsert_record(base, headers, domain, "TXT", "@", spf_txt)
        if mx_host:
            gd_upsert_record(base, headers, domain, "MX", "@", mx_host, priority=mx_prio)
        print("\n✅ DNS baseline applied. Give it a few minutes to propagate.")
    except Exception as e:
        die(str(e))

    print("\nNEXT STEPS:")
    print("  • Create your Microsoft 365 mailboxes in GoDaddy Email & Office:")
    print("      https://email.godaddy.com/")
    print("  • Webmail sign-in (Outlook): https://outlook.office.com/")
    print("  • Manage DNS (to double-check): https://dcc.godaddy.com/manage/{}/dns".format(domain))
    print("\nAll set. Re-run this script anytime to re-apply DNS if needed.")

if __name__ == "__main__":
    main()
