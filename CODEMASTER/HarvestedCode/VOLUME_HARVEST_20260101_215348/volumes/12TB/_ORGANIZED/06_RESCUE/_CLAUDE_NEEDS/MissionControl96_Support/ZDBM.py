import datetime
import os

def timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
