import os
import subprocess
import time

PXE_DIR = "/Users/rob/noizy-pxe"
ISO_PATH = "/Users/rob/Windows10.iso"
TFTP_ROOT = os.path.join(PXE_DIR, "tftp")
DHCP_CONFIG = os.path.join(PXE_DIR, "dhcp.conf")
LOG_PATH = os.path.join(PXE_DIR, "pxe.log")

def setup_dirs():
    os.makedirs(TFTP_ROOT, exist_ok=True)
    with open(LOG_PATH, "a") as log:
        log.write(f"{time.ctime()}: 📦 PXE directories initialized\n")

def extract_iso():
    cmd = f"hdiutil mount '{ISO_PATH}'"
    subprocess.run(cmd, shell=True)
    cmd = f"cp -R /Volumes/CCCOMA_X64FRE_EN-US_DV9/* '{TFTP_ROOT}/'"
    subprocess.run(cmd, shell=True)
    cmd = "hdiutil unmount /Volumes/CCCOMA_X64FRE_EN-US_DV9"
    subprocess.run(cmd, shell=True)
    with open(LOG_PATH, "a") as log:
        log.write(f"{time.ctime()}: 📀 ISO extracted to TFTP root\n")

def start_tftp():
    cmd = f"sudo tftpd -l -s '{TFTP_ROOT}'"
    subprocess.run(cmd, shell=True)
    with open(LOG_PATH, "a") as log:
        log.write(f"{time.ctime()}: 🌐 TFTP server started\n")

def start_dhcp():
    with open(DHCP_CONFIG, "w") as conf:
        conf.write("""
default-lease-time 600;
max-lease-time 7200;
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.200;
  option routers 192.168.1.1;
  filename "pxeboot.n12";
  next-server 192.168.1.10;
}
""")
    cmd = f"sudo dhcpd -cf '{DHCP_CONFIG}'"
    subprocess.run(cmd, shell=True)
    with open(LOG_PATH, "a") as log:
        log.write(f"{time.ctime()}: 🔧 DHCP server started\n")

def run_pxe():
    setup_dirs()
    extract_iso()
    start_tftp()
    start_dhcp()
    print("✅ PXE boot server is live. OMEN can now boot over LAN.")

if __name__ == "__main__":
    run_pxe()
