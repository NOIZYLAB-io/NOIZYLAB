
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.service_account import Credentials
import base64
import email
import csv
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    if os.path.exists('credentials.json'):
        try:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            print("🔑 Using credentials.json (manual OAuth)")
            return build('gmail', 'v1', credentials=creds)
        except Exception as e:
            print(f"❌ Error with credentials.json: {e}")
    if os.path.exists('service_account.json'):
        try:
            creds = Credentials.from_service_account_file('service_account.json', scopes=SCOPES)
            print("🤖 Using service_account.json (headless)")
            return build('gmail', 'v1', credentials=creds)
        except Exception as e:
            print(f"❌ Error with service_account.json: {e}")
    print("⚠️ No credentials found. Please add credentials.json or service_account.json to your project directory.")
    return None

def scan_inbox(service, max_results=50, out_csv='data/inbox_scan_log.csv'):
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])
    rows = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '')
        date = next((h['value'] for h in headers if h['name'] == 'Date'), '')
        rows.append({'Sender': sender, 'Subject': subject, 'Date': date})
        print(f"From: {sender} | Subject: {subject} | Date: {date}")
    # Save to CSV
    with open(out_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Sender', 'Subject', 'Date'])
        writer.writeheader()
        writer.writerows(rows)
    print(f"📄 Inbox scan log saved to {out_csv}")

if __name__ == "__main__":
    service = get_gmail_service()
    if service:
        scan_inbox(service)
    else:
        print("❌ No valid credentials found. Inbox scan aborted.")
