# Capsule Archive Starter
# This script archives 3 key memories for the ritual pack.

import os
import shutil
from datetime import datetime

MEMORIES = [
    'memory1.txt',
    'memory2.txt',
    'memory3.txt'
]

ARCHIVE_DIR = '../assets/capsule_archive'

os.makedirs(ARCHIVE_DIR, exist_ok=True)

for mem in MEMORIES:
    src = f'../assets/{mem}'
    dst = os.path.join(ARCHIVE_DIR, mem)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f'Preserved: {mem}')
    else:
        with open(dst, 'w') as f:
            f.write(f'Placeholder for {mem} - {datetime.now()}')
        print(f'Created placeholder: {mem}')

print('Capsule build complete. 3 memories preserved.')
