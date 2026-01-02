import subprocess

def check_slab(ip):
    try:
        subprocess.run(["ping", "-c", "1", ip], check=True)
        return True
    except:
        return False

def resurrect(ip):
    subprocess.run(["ssh", f"RSP@{ip}", "sudo reboot"])

if not check_slab("192.168.2.2"):
    print("❌ PowerSlab offline. Initiating resurrection.")
    resurrect("192.168.2.2")
