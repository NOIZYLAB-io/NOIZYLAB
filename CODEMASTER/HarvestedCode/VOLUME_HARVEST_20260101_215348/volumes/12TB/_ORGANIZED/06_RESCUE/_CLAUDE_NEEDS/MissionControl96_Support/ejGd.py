import os
import hashlib
import json
import mimetypes
import datetime
import argparse
import smtplib
from email.mime.text import MIMEText
import sys

# === CONFIG ===
def get_config():
    parser = argparse.ArgumentParser(description="MusicVault Full Scan")
    parser.add_argument('--root', type=str, default=r"D:\FishMusicVault", help="Root directory to scan")
    parser.add_argument('--log', type=str, default=r"D:\RitualLogs", help="Log directory")
    parser.add_argument('--email', type=str, help="Email to notify on completion")
    parser.add_argument('--webhook', type=str, help="Webhook URL to notify on completion")
    args = parser.parse_args()
    os.makedirs(args.log, exist_ok=True)
    return args

# === HELPERS ===
def hash_file(path, block_size=65536):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(block_size), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        return f"ERROR:{e}"

def log_event(logfile, data):
    with open(os.path.join(config.log, logfile), "a", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")

# === SCAN ===
def full_scan():
    seen_hashes = {}
    dupes, empties, bad_ext, errors = [], [], [], []
    total_files = 0
    scanned_files = 0
    # Count total files for progress
    for root, dirs, files in os.walk(config.root):
        total_files += len(files)
    print(f"Scanning {total_files} files in {config.root}...")
    for root, dirs, files in os.walk(config.root):
        # Empty folder check
        if not files and not dirs:
            empties.append(root)
            continue
        for file in files:
            scanned_files += 1
            path = os.path.join(root, file)
            # Hash for dupes
            h = hash_file(path)
            if h.startswith("ERROR"):
                errors.append({"file": path, "error": h})
                print(f"[ERROR] {path}: {h}")
                continue
            if h in seen_hashes:
                dupes.append({"file": path, "dupe_of": seen_hashes[h]})
                try:
                    os.remove(path)
                    print(f"[DUPE REMOVED] {path}")
                except Exception as e:
                    errors.append({"file": path, "error": str(e)})
            else:
                seen_hashes[h] = path
            # Extension validation
            mime, _ = mimetypes.guess_type(path)
            ext = os.path.splitext(file)[1].lower()
            if mime is not None:
                expected_ext = mimetypes.guess_extension(mime)
                if expected_ext and ext != expected_ext:
                    bad_ext.append({"file": path, "ext": ext, "mime": mime, "expected_ext": expected_ext})
            if scanned_files % 100 == 0:
                print(f"Progress: {scanned_files}/{total_files} files scanned...")
    # Purge empties
    for folder in empties:
        try:
            os.rmdir(folder)
            print(f"[EMPTY REMOVED] {folder}")
        except Exception as e:
            errors.append({"folder": folder, "error": str(e)})
    # Save logs
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    log_data = {
        "timestamp": ts,
        "dupes_removed": dupes,
        "empties_removed": empties,
        "bad_extensions": bad_ext,
        "errors": errors
    }
    log_event(f"autosave_{ts}.json", log_data)
    print(f"Scan complete. Logs saved to {config.log}")
    # Generate human-readable report
    report_path = os.path.join(config.log, f"report_{ts}.txt")
    with open(report_path, "w", encoding="utf-8") as rep:
        rep.write(f"MusicVault Full Scan Report\nTimestamp: {ts}\n\n")
        rep.write(f"Duplicates Removed: {len(dupes)}\n")
        rep.write(f"Empty Folders Removed: {len(empties)}\n")
        rep.write(f"Files with Bad Extensions: {len(bad_ext)}\n")
        rep.write(f"Errors: {len(errors)}\n\n")
        if dupes:
            rep.write("\n--- Duplicates ---\n")
            for d in dupes:
                rep.write(json.dumps(d) + "\n")
        if empties:
            rep.write("\n--- Empty Folders ---\n")
            for e in empties:
                rep.write(e + "\n")
        if bad_ext:
            rep.write("\n--- Bad Extensions ---\n")
            for b in bad_ext:
                rep.write(json.dumps(b) + "\n")
        if errors:
            rep.write("\n--- Errors ---\n")
            for err in errors:
                rep.write(json.dumps(err) + "\n")
    print(f"Report generated: {report_path}")
    # Email notification
    if config.email:
        try:
            msg = MIMEText(open(report_path).read())
            msg['Subject'] = f"MusicVault Scan Report {ts}"
            msg['From'] = config.email
            msg['To'] = config.email
            s = smtplib.SMTP('localhost')
            s.sendmail(config.email, [config.email], msg.as_string())
            s.quit()
            print(f"Email sent to {config.email}")
        except Exception as e:
            print(f"[EMAIL ERROR] {e}")
    # Webhook/callback
    if config.webhook:
        try:
            import requests
            with open(report_path, 'r', encoding='utf-8') as f:
                requests.post(config.webhook, data={'report': f.read()})
            print(f"Webhook sent to {config.webhook}")
        except Exception as e:
            print(f"[WEBHOOK ERROR] {e}")
    print("Scan and notifications complete.")

if __name__ == "__main__":
    config = get_config()
    full_scan()
    print("To schedule periodic scans, use Windows Task Scheduler or macOS LaunchAgent.")
