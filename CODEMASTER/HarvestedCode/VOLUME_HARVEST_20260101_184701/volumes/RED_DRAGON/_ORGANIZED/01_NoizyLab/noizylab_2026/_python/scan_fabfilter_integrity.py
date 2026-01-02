import os
import subprocess

# Start from root directory
ROOT = '/'
report = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    for name in dirnames + filenames:
        if 'fabfilter' in name.lower():
            path = os.path.join(dirpath, name)
            # Only check files (not folders) for codesign
            if os.path.isfile(path):
                try:
                    result = subprocess.run(['codesign', '--verify', '--verbose=2', path], capture_output=True, text=True)
                    if result.returncode == 0:
                        status = 'OK'
                    else:
                        status = f'ERROR: {result.stderr.strip()}'
                except Exception as e:
                    status = f'EXCEPTION: {e}'
                report.append((path, status))
            else:
                report.append((path, 'FOLDER'))

# Save report
with open('/Volumes/4TBSG/2025_NOIZYFISH/Python_Codes/fabfilter_integrity_report.txt', 'w') as f:
    for path, status in report:
        f.write(f'{path}: {status}\n')

print('FabFilter integrity scan complete. See fabfilter_integrity_report.txt for details.')
