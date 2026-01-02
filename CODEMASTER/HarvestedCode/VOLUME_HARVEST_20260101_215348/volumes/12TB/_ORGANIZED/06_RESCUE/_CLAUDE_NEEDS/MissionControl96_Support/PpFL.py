# Genie Mode Configuration

SLAB_NAME = "Mac Pro"
SLAB_IPS = ["192.168.2.2", "192.168.3.2", "macpro.local"]
SLAB_USERS = ["RSP"]
RITUAL_COMMAND = "ssh RSP@192.168.2.2 \"bash ~/NoizyFish/Rituals/voice_engine.sh\""
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
FFMPEG_COMMAND = 'ffmpeg -f avfoundation -i "DeckLink SDI" -t 00:10:00 output.mov'
softwareupdate --install --all
