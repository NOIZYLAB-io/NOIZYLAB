const vscode = require('vscode');
const cp = require('child_process');
const path = require('path');
const fs = require('fs');

function activate(context) {
  const historyPath = path.join(vscode.workspace.rootPath || '.', 'chat_history.jsonl');
  
  let disposable = vscode.commands.registerCommand('noizychat.openChat', function () {
    const panel = vscode.window.createWebviewPanel(
      'noizychat',
      'Noizy Chat',
      vscode.ViewColumn.Two,
      { enableScripts: true }
    );

    const htmlPath = path.join(context.extensionPath, 'webview', 'chat.html');
    panel.webview.html = fs.readFileSync(htmlPath, 'utf8');

    panel.webview.onDidReceiveMessage(async message => {
      if (message.command === 'ask') {
        const prompt = message.text;
        const model = message.model;
        try {
          const output = cp.execSync(
            `python3 noizy_router.py "${model}" "${prompt.replace(/"/g, '\\"')}"`
          ).toString();
          panel.webview.postMessage({ command: 'reply', text: output });
        } catch (err) {
          panel.webview.postMessage({ command: 'reply', text: err.message });
        }
      }
    });
  });

  // Register virtual file provider for chat history
  vscode.workspace.registerTextDocumentContentProvider('vscode-resource', {
    provideTextDocumentContent: () => fs.existsSync(historyPath) ? fs.readFileSync(historyPath,'utf8') : ''
  });

  context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = { activate, deactivate };