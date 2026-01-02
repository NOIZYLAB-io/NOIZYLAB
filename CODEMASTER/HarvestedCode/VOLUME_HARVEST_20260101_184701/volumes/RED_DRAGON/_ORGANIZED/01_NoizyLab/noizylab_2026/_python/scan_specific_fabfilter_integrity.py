import os
import subprocess

VOLUMES_ROOT = '/Volumes/'
plugins = [
    'FabFilter Pro-L 2',
    'FabFilter Saturn 2',
    'FabFilter Pro-DS',
    'FabFilter Pro-MB',
    'FabFilter Micro',
    'FabFilter Pro-R 2',
    'FabFilter Pro-C 2',
    'FabFilter Pro-Q 4',
    'FabFilter Simplon',
    'FabFilter Volcano 3',
    'FabFilter Timeless 3',
    'FabFilter Twin 3',
    'FabFilter One',
    'FabFilter Pro-G'
]
report = []
found_plugins = {name: False for name in plugins}

for volume in os.listdir(VOLUMES_ROOT):
    volume_path = os.path.join(VOLUMES_ROOT, volume)
    if not os.path.isdir(volume_path):
        continue
    for dirpath, dirnames, filenames in os.walk(volume_path):
        for name in dirnames + filenames:
            for plugin in plugins:
                if plugin.lower().replace(' ', '') in name.lower().replace(' ', ''):
                    path = os.path.join(dirpath, name)
                    found_plugins[plugin] = True
                    if os.path.isfile(path):
                        try:
                            result = subprocess.run(['codesign', '--verify', '--verbose=2', path], capture_output=True, text=True)
                            if result.returncode == 0:
                                status = 'OK'
                            else:
                                status = f'ERROR: {result.stderr.strip()}'
                        except Exception as e:
                            status = f'EXCEPTION: {e}'
                        report.append((plugin, path, status))
                    else:
                        report.append((plugin, path, 'FOLDER'))

# Check for missing plugins
for plugin, found in found_plugins.items():
    if not found:
        report.append((plugin, 'NOT FOUND', 'MISSING'))

# Save report
with open('/Volumes/4TBSG/2025_NOIZYFISH/Python_Codes/fabfilter_specific_integrity_report.txt', 'w') as f:
    for plugin, path, status in report:
        f.write(f'{plugin}: {path}: {status}\n')

print('Specific FabFilter integrity scan complete. See fabfilter_specific_integrity_report.txt for details.')
