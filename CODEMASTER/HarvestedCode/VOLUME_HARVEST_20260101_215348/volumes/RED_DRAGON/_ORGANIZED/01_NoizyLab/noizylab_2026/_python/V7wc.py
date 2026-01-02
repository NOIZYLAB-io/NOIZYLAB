import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURATION ---
EMAIL_ADDRESS = "your_email@webador.com"  # <-- Replace with your Webador email
EMAIL_PASSWORD = "your_password"           # <-- Replace with your password
SMTP_SERVER = "mail.webador.com"
SMTP_PORT = 587
IMAP_SERVER = "mail.webador.com"
IMAP_PORT = 993

# --- SEND EMAIL ---
def send_email(to_address, subject, body):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_address
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_address, msg.as_string())
    print(f"Email sent to {to_address}")

# --- RECEIVE EMAILS ---
def receive_emails():
    with imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT) as mail:
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        mail.select("inbox")
        typ, data = mail.search(None, "ALL")
        mail_ids = data[0].split()
        print(f"Found {len(mail_ids)} emails.")
        for num in mail_ids[-5:]:  # Show last 5 emails
            typ, msg_data = mail.fetch(num, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    print(f"From: {msg['From']}")
                    print(f"Subject: {msg['Subject']}")
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                print(f"Body: {part.get_payload(decode=True).decode()}")
                    else:
                        print(f"Body: {msg.get_payload(decode=True).decode()}")
                    print("-"*40)

if __name__ == "__main__":
    # Example usage
    # send_email("recipient@example.com", "Test Subject", "Hello from Webador!")
    receive_emails()
