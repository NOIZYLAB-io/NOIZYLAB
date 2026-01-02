import os
import subprocess
import time
import getpass

# 🔧 CONFIGURATION
USER = getpass.getuser()
BASE_DIR = os.path.expanduser(f"~/Desktop/MissionControl96/noizy-pxe")
ISO_PATH = os.path.expanduser(f"~/Desktop/MissionControl96/Windows10.iso")
TFTP_ROOT = os.path.join(BASE_DIR, "tftp")
DHCP_CONFIG = os.path.join(BASE_DIR, "dhcp.conf")
LOG_PATH = os.path.join(BASE_DIR, "pxe.log")

def log(msg):
    with open(LOG_PATH, "a") as log_file:
        log_file.write(f"{time.ctime()}: {msg}\n")
    print(msg)

def setup_dirs():
    os.makedirs(TFTP_ROOT, exist_ok=True)
    log("📦 PXE directories initialized")

def extract_iso():
    log("📀 Mounting ISO...")
    subprocess.run(f"hdiutil mount '{ISO_PATH}'", shell=True)
    log("📁 Copying ISO contents to TFTP root...")
    subprocess.run(f"cp -R /Volumes/CCCOMA_X64FRE_EN-US_DV9/* '{TFTP_ROOT}/'", shell=True)
    subprocess.run("hdiutil unmount /Volumes/CCCOMA_X64FRE_EN-US_DV9", shell=True)
    log("✅ ISO extracted and unmounted")

def start_tftp():
    log("🌐 Starting TFTP server...")
    subprocess.run(f"sudo launchctl load -w /System/Library/LaunchDaemons/tftp.plist", shell=True)
    subprocess.run(f"sudo tftpd -l -s '{TFTP_ROOT}'", shell=True)
    log("✅ TFTP server started")

def start_dhcp():
    log("🔧 Writing DHCP config...")
    with open(DHCP_CONFIG, "w") as conf:
        conf.write(f"""
default-lease-time 600;
max-lease-time 7200;
subnet 192.168.1.0 netmask 255.255.255.0 {{
  range 192.168.1.100 192.168.1.200;
  option routers 192.168.1.1;
  filename "pxeboot.n12";
  next-server 192.168.1.10;
}}
""")
    log("🚀 Starting DHCP server...")
    subprocess.run(f"sudo dhcpd -cf '{DHCP_CONFIG}'", shell=True)
    log("✅ DHCP server started")

def run_pxe():
    log("🧬 Starting NOIZY PXE Boot Ritual")
    setup_dirs()
    extract_iso()
    start_tftp()
    start_dhcp()
    log("🔥 PXE boot server is live. OMEN can now boot over LAN.")

if __name__ == "__main__":
    run_pxe()
