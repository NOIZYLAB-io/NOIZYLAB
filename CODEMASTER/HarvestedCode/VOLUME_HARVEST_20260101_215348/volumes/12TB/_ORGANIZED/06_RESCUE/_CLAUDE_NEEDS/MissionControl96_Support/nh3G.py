mkdir -p ~/Desktop/NoizyFish/scripts
nano ~/Desktop/NoizyFish/scripts/setup_vscode_noizyfish.py
# (Paste your code, save with Ctrl+O, Enter, exit with Ctrl+X)
source ~/Desktop/NoizyFish/.venv/bin/activate
python3 ~/Desktop/NoizyFish/scripts/noizy_editor.py
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
    [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
