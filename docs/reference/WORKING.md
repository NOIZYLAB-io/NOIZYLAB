# Overview of the extension

### important things to note

- Extension runs on Node.js runtime
- Webviews are made in React (JS) and compiled to HTML
- Compilation done using webpack
- Some incompatible things use webpack loaders in webpack.config
- Extension and webview communicate using message passing
- Extension files are compiled to dist/ and webview files are compiled to build/
- Run `npm run watch` to compile extension and webview files
- Press `F5` to run the extension in debug mode

### Extension structure

- `src/` contains the extension files (.ts files)
- `webviews/` contains the webview files (.jsx/.js files)
- `globals.ts` contains global variables for passing to the webviews (defined in the webview provider(ts)
  files inside script tags) Example: [SidebarProvier.ts](src/SidebarProvider.ts) at line 909
- `src/utils/` contains utility functions
- `src/config` contains only the firebase config for webviews not the extension backend

### References

- vscode api official docs: https://code.visualstudio.com/api
- sample extensions: https://github.com/microsoft/vscode-extension-samples
- sample webviews: https://github.com/microsoft/vscode-webview-ui-toolkit-samples
- ben awad's video:
  [link](https://www.youtube.com/watch?v=a5DX5pQ9p5M&t=2730s&pp=ygUZYmVuIGF3YWQgdnNjb2RlIGV4dGVuc2lvbg%3D%3D)
- open source extension example: https://github.com/sourcegraph/cody

## File overviews

### Webviews

- `SidebarProvider.ts`: Contains the sidebar provider class to render the sidebar panel + webview rendered
  from `webviews/pages/sidebar/Sidebar.js`
- `ChatProvider.ts`: Contains the chat provider class to render the chat panel + webview rendered from
  `webviews/pages/Chat/Chat.js`
- `ActionPanelProvider.ts`: Contains the action panel provider class to render the action panel for
  debug/review/optimize features + webview rendered from `webviews/pages/ActionPanel/ActionPanel.js`
- `FilesPanelProvider.ts`: Contains the files panel provider class to render the files panel for adding to KB
  from local codebase feature + webview rendered from `webviews/pages/FilesPanel/FilesPanel.js`
- `TestCasePanelProvider.ts`: Contains the test case panel provider class to render the test case panel for
  adding test cases to KB feature + webview rendered from `webviews/pages/TestCasePanel/TestCasePanel.js`
- `VoicePanelProvider.ts`: Contains the voice panel provider class to render the voice panel for voice
  commands feature + webview rendered from `webviews/pages/VoicePanel/VoicePanel.js`
- `webviews/pages/`: Contains the webview pages
- `extension.ts`: Entry point file of the extension, all logic inside `activate` function, deactivation logic
  inside `deactivate` function
   - Each registered commands/features must be pushed inside a disposables list which registers on activation
     event described in `package.json`
- `package.json`: Contains the extension details and commands/features to be registered. Following things can
  be defined:
   - commands
   - menu/title bar options
   - bottom nav bar options
   - comment options
   - command palette options
   - webview options
   - settings page options for the extension
      - can be accessed by `vscode.workspace.getConfiguration('extensionName')`
      - Example:
   ```ts
   vscode.workspace.getConfiguration("codemate").get("enableCodeLens", true)
   ```
- `authenticate.ts`: Starts a minimal polka server for storing auth credentials in Memento
- `TokenManager.ts`: Implementation of vscode.Memento = vscode's local storage API
- `getNonce.ts`: Generate nonce for webview security
