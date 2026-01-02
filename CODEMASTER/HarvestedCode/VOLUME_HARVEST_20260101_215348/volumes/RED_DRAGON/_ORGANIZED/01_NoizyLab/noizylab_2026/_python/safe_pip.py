#!/usr/bin/env python3
import os, sys, subprocess, venv

def create_venv(venv_path=".venv"):
    if not os.path.exists(venv_path):
        print(f"Creating virtual environment at {venv_path}...")
        venv.create(venv_path, with_pip=True)
    return os.path.abspath(venv_path)

def install_packages(venv_path, packages):
    python_exec = os.path.join(venv_path, "bin", "python3")
    if not os.path.exists(python_exec):
        python_exec = os.path.join(venv_path, "bin", "python")
    subprocess.check_call([python_exec, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([python_exec, "-m", "pip", "install"] + packages)

def main():
    if len(sys.argv) < 2:
        print("Usage: python safe_pip.py <package1> <package2> ...")
        sys.exit(1)
    packages = sys.argv[1:]
    venv_path = ".venv"
    venv_abs = create_venv(venv_path)
    install_packages(venv_abs, packages)
    print("\n✅ Installed:", " ".join(packages))
    print(f"Activate with: source {venv_path}/bin/activate")

if __name__ == "__main__":
    main()
