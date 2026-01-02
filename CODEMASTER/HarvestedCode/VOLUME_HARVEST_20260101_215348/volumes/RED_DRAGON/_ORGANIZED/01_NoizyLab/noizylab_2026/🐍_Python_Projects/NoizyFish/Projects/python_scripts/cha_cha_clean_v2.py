#!/usr/bin/env python3
import subprocess, sys, os
from pathlib import Path
from datetime import datetime
import openai  # pip install openai

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
BUBBA_BITZ = WORKSPACE / "Bubbas_Bitz_v2"
LOGS = BUBBA_BITZ / "Logs"
LOGS.mkdir(parents=True, exist_ok=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return e.output

def lint_and_format(filepath: Path):
    ext = filepath.suffix
    report = []
    if ext == ".py":
        report.append(run_cmd(["black", str(filepath)]))
        report.append(run_cmd(["pylint", str(filepath), "--disable=all", "--enable=E,F,W,C"]))
    elif ext in (".js", ".ts"):
        report.append(run_cmd(["npx", "prettier", "--write", str(filepath)]))
        report.append(run_cmd(["npx", "eslint", str(filepath)]))
    else:
        report.append(f"No formatter/linter configured for {ext}")
    return "\n".join(report)

def cha_cha_refactor(code: str, language: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Cha-Cha, an elegant code refactorer. Improve readability, add docstrings, optimize loops, but do NOT change logic."},
                {"role": "user", "content": f"Refactor this {language} code:\n{code}"}
            ],
            max_tokens=1500,
            temperature=0.3,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[Cha-Cha ERROR] {e}"

def clean_code(filepath: Path):
    language = "Python" if filepath.suffix == ".py" else "JavaScript/TypeScript"
    original = filepath.read_text(encoding="utf-8")
    lint_report = lint_and_format(filepath)
    refactored = cha_cha_refactor(original, language)

    cleaned_path = filepath.parent / f"{filepath.stem}_cleaned{filepath.suffix}"
    cleaned_path.write_text(refactored, encoding="utf-8")

    log_file = LOGS / f"cha_cha_clean_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_file.write_text(lint_report, encoding="utf-8")

    return f"""
✅ Cha-Cha Cleanup Complete (v2)
File: {filepath}
Refactored: {cleaned_path}
Log: {log_file}
"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: cha2 <file>")
        sys.exit(1)
    filepath = Path(sys.argv[1]).expanduser()
    if not filepath.exists():
        print(f"❌ File not found: {filepath}")
        sys.exit(1)
    print(clean_code(filepath))
