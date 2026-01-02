#!/usr/bin/env python3
"""
DGS-1210-10 Smart Control Script
- Network discovery (nmap)
- Web login & config (requests)
- SNMP info & control (pysnmp)
- Backup & restore config
- Password recovery (RouterPassView)
- Advanced settings (IP, VLAN, reboot, firmware)
"""

import requests, subprocess, sys, os, time
from pysnmp.hlapi import *

# CONFIG
ROUTER_IP = "192.168.0.1"
USERNAME = "admin"
PASSWORD = "your_password"
NEW_IP = "192.168.0.2"
VLAN_ID = "10"
FIRMWARE_PATH = "/path/to/firmware.bin"

def discover_router():
    print("🔎 Scanning for D-Link routers...")
    subprocess.run(["nmap", "-O", "192.168.0.0/24"])
    print("Scan complete.\n")

def login_router():
    print("🔐 Logging in to web interface...")
    session = requests.Session()
    login_url = f"http://{ROUTER_IP}/login.cgi"
    payload = {"username": USERNAME, "password": PASSWORD}
    resp = session.post(login_url, data=payload)
    if resp.ok:
        print("✅ Login successful.")
        return session
    print("❌ Login failed."); sys.exit(1)

def change_ip(session):
    print(f"🌐 Changing IP to {NEW_IP}...")
    config_url = f"http://{ROUTER_IP}/config.cgi"
    payload = {"ip": NEW_IP, "submit": "Save"}
    resp = session.post(config_url, data=payload)
    print("✅ IP change request sent." if resp.ok else "❌ Failed to change IP.")

def set_vlan(session):
    print(f"🛠️ Setting VLAN {VLAN_ID}...")
    vlan_url = f"http://{ROUTER_IP}/vlan.cgi"
    payload = {"vlan_id": VLAN_ID, "submit": "Apply"}
    resp = session.post(vlan_url, data=payload)
    print("✅ VLAN set." if resp.ok else "❌ VLAN failed.")

def reboot_router(session):
    print("🔄 Rebooting router...")
    reboot_url = f"http://{ROUTER_IP}/reboot.cgi"
    resp = session.post(reboot_url)
    print("✅ Reboot command sent." if resp.ok else "❌ Reboot failed.")

def upgrade_firmware(session):
    print("⬆️ Upgrading firmware...")
    fw_url = f"http://{ROUTER_IP}/fw_upload.cgi"
    with open(FIRMWARE_PATH, 'rb') as fw:
        files = {'file': fw}
        resp = session.post(fw_url, files=files)
    print("✅ Firmware uploaded." if resp.ok else "❌ Firmware upload failed.")

def snmp_get(oid):
    print(f"📡 SNMP GET {oid}...")
    for (errorIndication, errorStatus, errorIndex, varBinds) in getCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget((ROUTER_IP, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    ):
        if errorIndication: print(errorIndication); break
        elif errorStatus: print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex)-1][0] or '?')); break
        else: print(' = '.join([x.prettyPrint() for x in varBinds[0]]))

def backup_config():
    print("💾 Backing up config...")
    subprocess.run(["curl", f"http://{ROUTER_IP}/backup.cgi", "-o", "router_config.bin"])
    print("✅ Config backup saved as router_config.bin.")

def restore_config():
    print("♻️ Restoring config...")
    subprocess.run(["curl", "-F", "file=@router_config.bin", f"http://{ROUTER_IP}/restore.cgi"])
    print("✅ Config restore sent.")

def run_routerpassview():
    print("🔑 Running RouterPassView...")
    print("(Add your RouterPassView command here)")

if __name__ == "__main__":
    discover_router()
    session = login_router()
    change_ip(session)
    set_vlan(session)
    reboot_router(session)
    upgrade_firmware(session)
    snmp_get('1.3.6.1.2.1.1.1.0')  # sysDescr
    backup_config()
    restore_config()
    run_routerpassview()
    print("🚀 DGS-1210-10 Smart Control Complete.")