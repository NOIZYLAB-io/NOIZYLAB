"""
Google Cloud KMS-Integrated Encrypted Backup Script for MissionControl96
- Encrypts files with Google Cloud KMS
- Uploads to Google Cloud Storage

Dependencies:
    pip install google-cloud-storage google-cloud-kms
"""
import os
try:
    from google.cloud import storage, kms  # type: ignore
except ImportError:
    print('ERROR: google-cloud-storage and google-cloud-kms must be installed for backup functionality.')
    storage = None  # type: ignore
    kms = None  # type: ignore

# === CONFIG ===
SOURCE_DIRS = [
    os.path.expanduser('~/NOIZYGRID'),
    os.path.expanduser('~/Documents/MissionControl96'),
    os.path.expanduser('~/Library/Application Support/Microsoft/Windows PowerShell/Scripts')
]
BUCKET_NAME = 'your-gcs-bucket-name'
BACKUP_PREFIX = 'MissionControl96_Snapshot'
PROJECT_ID = 'your-gcp-project-id'
LOCATION_ID = 'your-kms-location'  # e.g., 'us-central1'
KEY_RING_ID = 'your-key-ring'
KEY_ID = 'your-key'

# === KMS ENCRYPTION ===
def encrypt_with_kms(plaintext: bytes) -> bytes:  # type: ignore
    if kms is None:
        raise ImportError('google-cloud-kms is not installed')
    client = kms.KeyManagementServiceClient()  # type: ignore
    key_name = client.crypto_key_path(PROJECT_ID, LOCATION_ID, KEY_RING_ID, KEY_ID)  # type: ignore
    response = client.encrypt(request={"name": key_name, "plaintext": plaintext})  # type: ignore
    return response.ciphertext  # type: ignore

# === UPLOAD TO GCS ===
def upload_to_gcs(blob_name: str, data: bytes) -> None:  # type: ignore
    if storage is None:
        raise ImportError('google-cloud-storage is not installed')
    client = storage.Client()  # type: ignore
    bucket = client.bucket(BUCKET_NAME)  # type: ignore
    blob = bucket.blob(blob_name)  # type: ignore
    blob.upload_from_string(data)  # type: ignore
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
                    with open(full_path, 'rb') as f:
                        plaintext = f.read()
                    encrypted = encrypt_with_kms(plaintext)
                    upload_to_gcs(blob_name, encrypted)
                except Exception as e:
                    print(f'Error backing up {full_path}: {e}')
    print('KMS backup complete.')
