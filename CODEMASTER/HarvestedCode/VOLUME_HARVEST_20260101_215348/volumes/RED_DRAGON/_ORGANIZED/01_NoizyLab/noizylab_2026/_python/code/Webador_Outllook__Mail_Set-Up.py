import imaplib
import email
from email.header import decode_header

# Outlook IMAP settings
IMAP_SERVER = "outlook.office365.com"
EMAIL_USER = "your_email@outlook.com"
EMAIL_PASS = "your_password"

# Connect to Outlook IMAP
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL_USER, EMAIL_PASS)
mail.select("inbox")

# Search for all emails
status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()[-5:]  # Get the latest 5 emails

for eid in email_ids:
    status, msg_data = mail.fetch(eid, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")
            print("Subject:", subject)
            print("From:", msg.get("From"))
            print("Date:", msg.get("Date"))
            # Print email body (plain text only)
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        print("Body:", part.get_payload(decode=True).decode())
            else:
                print("Body:", msg.get_payload(decode=True).decode())

mail.logout()

print("\033[1;34mThis is bold blue text!\033[0m")
print("\033[1;32m✔ Success!\033[0m")
print("\033[1;31m✖ Error!\033[0m")