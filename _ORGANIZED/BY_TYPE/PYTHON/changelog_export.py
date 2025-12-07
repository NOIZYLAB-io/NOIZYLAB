import csv
import datetime
import os
import subprocess
from pathlib import Path

REPORTS_DIR = Path("reports")
OUTPUT = REPORTS_DIR / "changelog.csv"

def ensure_reports_dir() -> None:
  REPORTS_DIR.mkdir(parents=True, exist_ok=True)

def gather_git_log() -> list[str]:
  result = subprocess.run(
      ["git", "log", "--pretty=format:%h|%ad|%an|%s", "--date=iso"],
      capture_output=True,
      text=True,
      check=True,
  )
  return result.stdout.splitlines()

def write_csv(rows: list[str]) -> None:
  timestamp = datetime.datetime.utcnow().isoformat() + "Z"
  with OUTPUT.open("w", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["hash", "date", "author", "subject", "exported_at"])
    for line in rows:
      parts = line.split("|")
      writer.writerow(parts + [timestamp])

def main() -> None:
  ensure_reports_dir()
  rows = gather_git_log()
  write_csv(rows)
  print(f"{OUTPUT} written")

if __name__ == "__main__":
  main()
