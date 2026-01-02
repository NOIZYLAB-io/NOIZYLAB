mkdir -p ~/Desktop/NoizyFish/scripts
nano ~/Desktop/NoizyFish/scripts/setup_vscode_noizyfish.py
# (Paste your code, save with Ctrl+O, Enter, exit with Ctrl+X)
source ~/Desktop/NoizyFish/.venv/bin/activate
python3 ~/Desktop/NoizyFish/scripts/noizy_editor.py
Set-ExecutionPolicy Bypass -Scope Process -Force
./noizywind_vscode_setup.ps1

# Install VS Code and essentials
choco install -y vscode git python nodejs-lts 7zip googlechrome

# Install VS Code extensions
$extensions = @(
  "ms-python.python",
  "ms-python.vscode-pylance",
  "ms-toolsai.jupyter",
  "ms-vscode.powershell",
  "ms-azuretools.vscode-docker",
  "github.copilot",
  "esbenp.prettier-vscode",
  "eamodio.gitlens"
)
foreach ($ext in $extensions) {
    code --install-extension $ext
}

# Create workspace folder
$workspace = "$env:USERPROFILE\Desktop\NoizyFish"
$scripts = "$workspace\scripts"
New-Item -Path $workspace -ItemType Directory -Force | Out-Null
New-Item -Path $scripts -ItemType Directory -Force | Out-Null

# Configure VS Code settings
$settingsPath = "$env:APPDATA\Code\User\settings.json"
$settings = @{
    "editor.fontFamily" = "Consolas, 'Courier New', monospace"
    "editor.fontSize" = 14
    "editor.formatOnSave" = $true
    "python.defaultInterpreterPath" = "python"
    "files.autoSave" = "afterDelay"
    "files.autoSaveDelay" = 1000
}
$settings | ConvertTo-Json -Depth 3 | Set-Content $settingsPath

# Create a workspace file
$workspaceFile = "$workspace\NoizyFish.code-workspace"
$workspaceConfig = @{
    folders = @(@{ path = "." })
}
$workspaceConfig | ConvertTo-Json -Depth 3 | Set-Content $workspaceFile

# Launch VS Code with workspace
code $workspaceFile
