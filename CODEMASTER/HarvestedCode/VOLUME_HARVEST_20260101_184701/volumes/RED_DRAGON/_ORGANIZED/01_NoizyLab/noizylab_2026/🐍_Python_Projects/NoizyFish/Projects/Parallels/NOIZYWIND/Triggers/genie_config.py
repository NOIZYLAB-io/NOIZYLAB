# Genie Mode Configuration

SLAB_NAME = "Mac Pro"
SLAB_IPS = ["192.168.2.2", "192.168.3.2", "macpro.local"]
SLAB_USERS = ["RSP"]
RITUAL_COMMAND = "bash ~/NoizyFish/CreativeMode/activate.sh"
LOG_PATH = "/Users/rsp_ms/NoizyFish/Logs/slablink.log"
SYNC_PATHS = ["/Users/rsp_ms/Documents/Important"]
VOICE_FEEDBACK = True
ALERT_EMAIL = "your_email@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your_email@example.com"
SMTP_PASS = "your_password"
HOMEKIT_DEVICES = ["lights", "speakers"]
AV_COMMANDS = ["volup", "voldown"]
WEB_DASHBOARD = True
SCHEDULE_INTERVAL = 3600
SECURITY_LOGGING = True

# Mac Studio Hardware Info (system_profiler SPHardwareDataType)
hardware_info = {
	"Model Name": "Mac Studio",
	"Model Identifier": "Mac14,14",
	"Model Number": "Z180000HYVC/A",
	"Chip": "Apple M2 Ultra",
	"Total Number of Cores": "24 (16 performance, 8 efficiency)",
	"Memory": "192 GB",
	"System Firmware Version": "13822.1.2",
	"OS Loader Version": "11881.140.96",
	"Serial Number": "YRCYX224N4",
	"Hardware UUID": "B3CEC2E5-30DE-5958-A781-538F03E26E95",
	"Activation Lock Status": "Enabled"
}

ssh_command = "ssh RSP@192.168.2.2"
ssh_command_with_script = 'ssh RSP@192.168.2.2 "bash ~/NoizyFish/Rituals/voice_engine.sh"'
ssh RSP@192.168.2.2

ifconfig | grep -B3 "inet " | grep -v "127.0.0.1"
~/NoizyFish/Triggers/genie_full_automation.sh
