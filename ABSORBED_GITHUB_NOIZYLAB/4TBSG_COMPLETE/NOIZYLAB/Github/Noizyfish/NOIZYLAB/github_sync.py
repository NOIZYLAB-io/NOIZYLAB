# GitHub Sync for NOIZYGATE
import subprocess

def sync_logs():
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'NOIZYGATE: Sync logs'])
    subprocess.run(['git', 'push'])

if __name__ == '__main__':
    sync_logs()
