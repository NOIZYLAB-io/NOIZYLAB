import os
import re

NKI_ROOT = '/Volumes/JOE/NKI'
REPORT_TXT = '/Users/m2ultra/nki_strings_report.txt'

# Regex for printable ASCII strings (4+ chars)
STRING_RE = re.compile(rb'([\x20-\x7E]{4,})')

def extract_strings_from_file(filepath):
    strings = set()
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
            for match in STRING_RE.finditer(data):
                s = match.group(0).decode('ascii', errors='ignore').strip()
                if s:
                    strings.add(s)
    except Exception as e:
        strings.add(f'ERROR: {e}')
    return sorted(strings)

def scan_nki_files(root):
    report = []
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.lower().endswith('.nki'):
                full_path = os.path.join(dirpath, fname)
                rel_path = os.path.relpath(full_path, root)
                strings = extract_strings_from_file(full_path)
                report.append({'file': rel_path, 'strings': strings})
    return report

def write_report(report, out_path):
    with open(out_path, 'w') as f:
        for entry in report:
            f.write(f"File: {entry['file']}\n")
            for s in entry['strings']:
                f.write(f"  {s}\n")
            f.write('\n')

def main():
    print(f'Scanning {NKI_ROOT} for .nki files and extracting readable strings...')
    report = scan_nki_files(NKI_ROOT)
    write_report(report, REPORT_TXT)
    print(f'Report written to {REPORT_TXT}')

if __name__ == '__main__':
    main()
