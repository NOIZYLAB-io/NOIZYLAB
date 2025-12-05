#!/usr/bin/env python3
import os
import py_compile

REPORT_FILE = "python_syntax_report.txt"

def check_python_scripts(directory=".", report_file=REPORT_FILE):
    errors = []
    checked = 0
    for root, dirs, files in os.walk(directory):
        for fname in files:
            if fname.endswith(".py"):
                checked += 1
                fpath = os.path.join(root, fname)
                try:
                    py_compile.compile(fpath, doraise=True)
                except Exception as e:
                    errors.append(f"{fpath}: {e}")
                    print(f"❌ Error in {fpath}: {e}")
    if errors:
        with open(report_file, "w") as f:
            f.write("\n".join(errors))
        print(f"\nErrors found! See {report_file} for details.")
    else:
        print("\nAll Python scripts passed syntax check!")
    print(f"Checked {checked} Python files.")

if __name__ == "__main__":
    check_python_scripts()
