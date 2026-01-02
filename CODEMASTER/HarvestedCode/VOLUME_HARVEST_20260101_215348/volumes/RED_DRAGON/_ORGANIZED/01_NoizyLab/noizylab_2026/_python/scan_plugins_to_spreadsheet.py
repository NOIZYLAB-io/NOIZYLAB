import os
import re
import plistlib
from openpyxl import Workbook
import webbrowser

PLUGIN_ROOT = '/Library/Audio/Plug-Ins'
OUTPUT_FILE = os.path.expanduser('~/Desktop/Plugin_List.xlsx')

# Helper to extract version from Info.plist if present

def get_version_from_plist(plist_path):
    try:
        with open(plist_path, 'rb') as f:
            plist = plistlib.load(f)
        return plist.get('CFBundleShortVersionString', '')
    except Exception:
        return ''

wb = Workbook()
ws = wb.active
ws.title = "Plugins"
ws.append(["Plugin Name", "Format", "Version"])

for format_folder in os.listdir(PLUGIN_ROOT):
    format_path = os.path.join(PLUGIN_ROOT, format_folder)
    if not os.path.isdir(format_path):
        continue
    for plugin in os.listdir(format_path):
        plugin_path = os.path.join(format_path, plugin)
        plugin_name = plugin.replace('.component', '').replace('.clap', '').replace('.vst', '').replace('.vst3', '')
        version = ''
        # Try to find Info.plist for AU/Component plugins
        if plugin.endswith('.component'):
            info_plist = os.path.join(plugin_path, 'Contents', 'Info.plist')
            if os.path.exists(info_plist):
                version = get_version_from_plist(info_plist)
        # For CLAP/VST/VST3, version info may not be available
        ws.append([plugin_name, format_folder, version])

wb.save(OUTPUT_FILE)
print(f"Plugin list saved to {OUTPUT_FILE}")

def print_checklist():
    print("=== OpenAI Power Checklist for VS Code ===")
    print("1. Install GitHub Copilot: https://marketplace.visualstudio.com/items?itemName=GitHub.copilot")
    print("2. Install ChatGPT Extension: https://marketplace.visualstudio.com/items?itemName=genieai.chatgpt-vscode")
    print("3. Update VS Code and all extensions regularly.")
    print("4. Configure Copilot settings: Enable inline suggestions, adjust privacy, set prompt style.")
    print("5. Configure ChatGPT settings: Set API key, enable chat panel, adjust context length.")
    print("6. Learn keyboard shortcuts for Copilot and ChatGPT.")
    print("7. Use command palette for quick AI actions.")
    print("8. Provide clear, specific prompts for best results.")
    print("9. Review and edit AI-generated code for accuracy and security.")
    print("10. Explore Copilot Labs and advanced features for code explanations and transformations.")
    print("11. Use AI for test generation, code reviews, and automation.")
    print("12. Integrate AI into your workflow for brainstorming, debugging, and documentation.")
    print("==========================================")

def open_links():
    webbrowser.open("https://marketplace.visualstudio.com/items?itemName=GitHub.copilot")
    webbrowser.open("https://marketplace.visualstudio.com/items?itemName=genieai.chatgpt-vscode")

if __name__ == "__main__":
    print_checklist()
    # Uncomment below to open extension pages in your browser
    # open_links()
