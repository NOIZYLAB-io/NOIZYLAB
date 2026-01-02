"""
Google Cloud Encrypted Backup Script for MissionControl96
- Encrypts files with Fernet (AES)
- Uploads to Google Cloud Storage
- Keys managed in Google Cloud KMS (recommended for production)
"""
import os, sys, glob
from cryptography.fernet import Fernet
from google.cloud import storage

# === CONFIG ===
SOURCE_DIRS = [
    r'C:\NOIZYGRID',
    r'C:\Users\rsp_ms\Documents\MissionControl96',
    r'C:\Users\rsp_ms\AppData\Roaming\Microsoft\Windows\PowerShell\Scripts'
]
BUCKET_NAME = 'your-gcs-bucket-name'
BACKUP_PREFIX = 'MissionControl96_Snapshot'
KEY_FILE = 'fernet.key'  # For demo; use Google KMS for production

# === KEY MANAGEMENT ===
def get_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as f:
            return f.read()
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    return key

fernet = Fernet(get_key())

# === ENCRYPT & UPLOAD ===
def encrypt_file(path):
    with open(path, 'rb') as f:
        data = f.read()
    return fernet.encrypt(data)

def upload_to_gcs(blob_name, data):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(data)
    print(f'Uploaded: {blob_name}')

if __name__ == '__main__':
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    for src_dir in SOURCE_DIRS:
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, src_dir)
                blob_name = f'{BACKUP_PREFIX}/{timestamp}/{os.path.basename(src_dir)}/{rel_path}.enc'
                try:
                    encrypted = encrypt_file(full_path)
                    upload_to_gcs(blob_name, encrypted)
                except Exception as e:
                    print(f'Error backing up {full_path}: {e}')
    print('Backup complete.')
