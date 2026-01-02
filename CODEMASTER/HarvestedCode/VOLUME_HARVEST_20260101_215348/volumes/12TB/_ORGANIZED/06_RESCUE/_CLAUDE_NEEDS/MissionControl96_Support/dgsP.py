import subprocess
import time
import winrm

# Step 1: Start NOIZYWIN VM via Parallels
def start_vm():
    print("🔮 Starting NOIZYWIN VM...")
    subprocess.run(["prlctl", "start", "NOIZYWIN"], check=True)
    time.sleep(15)  # Wait for VM to boot

# Step 2: Connect to Windows 11 via WinRM
def connect_winrm():
    print("🔗 Connecting to NOIZYWIN via WinRM...")
    session = winrm.Session('http://NOIZYWIN:5985/wsman', auth=('admin', 'yourpassword'))
    return session

# Step 3: Customize Desktop
def customize_desktop(session):
    print("🎨 Customizing Windows 11 desktop...")
    commands = [
        'taskkill /F /IM Cortana.exe',
        'taskkill /F /IM SpeechRuntime.exe',
        'powershell.exe -Command "Set-ItemProperty -Path HKCU:\\Control Panel\\Desktop -Name Wallpaper -Value C:\\NOIZYGRID\\NOIZY.jpg"',
        'powershell.exe -Command "Checkpoint-Computer -Description NOIZYFISH_Rebirth -RestorePointType MODIFY_SETTINGS"'
    ]
    for cmd in commands:
        result = session.run_cmd(cmd)
        print(f"✅ {cmd}\n{result.std_out.decode()}")

# Main ritual
if __name__ == "__main__":
    start_vm()
    session = connect_winrm()
    customize_desktop(session)
    print("🌟 NOIZYWIN is mythically reborn and customized.")
