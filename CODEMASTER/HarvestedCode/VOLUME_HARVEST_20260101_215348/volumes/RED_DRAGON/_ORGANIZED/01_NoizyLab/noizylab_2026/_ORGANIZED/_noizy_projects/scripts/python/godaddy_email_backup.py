"""
Automate Microsoft 365/Google Workspace Email Backup
- Uses IMAP to export mailbox data for rp@fishmusicinc.com
- Stores backup in local directory or pushes to GitHub
"""
import imaplib
import email
import os
from datetime import datetime

EMAIL = 'rp@fishmusicinc.com'
IMAP_SERVER = 'outlook.office365.com'  # or 'imap.gmail.com' for Google Workspace
IMAP_PORT = 993
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
BACKUP_DIR = os.path.expanduser('~/MissionControl96/backups/email')

os.makedirs(BACKUP_DIR, exist_ok=True)

def backup_email():
    ts = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    mbox_file = f'{BACKUP_DIR}/{EMAIL}_backup_{ts}.mbox'
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL, EMAIL_PASSWORD)
    mail.select('inbox')
    typ, data = mail.search(None, 'ALL')
    with open(mbox_file, 'w') as f:
        for num in data[0].split():
            typ, msg_data = mail.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])
            f.write(msg.as_string() + '\n')
    print(f'Backed up email to {mbox_file}')
    mail.logout()

if __name__ == '__main__':
    backup_email()
