==============================================================
🧠 NOIZY.AI MISSION CONTROL - INSTALLER PACKAGE
==============================================================

Welcome to Noizy.ai Mission Control 96! This installer contains
everything you need to run your AI command center.

📦 WHAT'S INCLUDED:
--------------------------------------------------------------
✅ install_noizy.sh      - Mac/Linux installer
✅ install_noizy.ps1     - Windows PowerShell installer  
✅ noizy-vscode.vsix     - VS Code extension package
✅ MissionControl/       - Complete source code
✅ This README file

🚀 QUICK START:
--------------------------------------------------------------
1. EXTRACT this folder to your desired location
2. RUN the installer for your platform:
   
   Mac/Linux:   ./install_noizy.sh
   Windows:     .\install_noizy.ps1
   
3. INSTALL VS Code extension:
   code --install-extension noizy-vscode.vsix
   
4. OPEN your browser to:
   http://127.0.0.1:8765/dashboard

🔑 LICENSING:
--------------------------------------------------------------
• FREE VERSION: 6 agents, basic functionality
• PRO VERSION: 96 agents, full AI integration, HTTPS deployment

Visit https://noizy.ai to upgrade to Pro.

⚙️ REQUIREMENTS:
--------------------------------------------------------------
✅ Python 3.8 or higher
✅ 2GB RAM minimum (4GB recommended)
✅ Internet connection for AI providers
✅ VS Code (optional, for extension)

🌐 GETTING API KEYS:
--------------------------------------------------------------
1. OpenAI: https://platform.openai.com/api-keys
2. Anthropic: https://console.anthropic.com/
3. ElevenLabs: https://elevenlabs.io/speech-synthesis
4. GitHub: https://github.com/settings/tokens

Add these to your .env file after installation.

🆘 SUPPORT:
--------------------------------------------------------------
📧 Email: rsp@noizyfish.com
🌐 Website: https://noizy.ai
📖 Docs: https://docs.noizy.ai

🔧 TROUBLESHOOTING:
--------------------------------------------------------------
• Port 8765 already in use? 
  Run: lsof -ti:8765 | xargs kill
  
• Permission denied on Mac/Linux?
  Run: chmod +x install_noizy.sh
  
• Windows execution policy error?
  Run: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

==============================================================
🎯 Ready to launch your AI mission control center!
==============================================================