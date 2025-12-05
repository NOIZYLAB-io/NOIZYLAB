"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.MochaAdapter = void 0;
const tslib_1 = require("tslib");
const vscode = tslib_1.__importStar(require("vscode"));
const configReader_1 = require("./configReader");
const core_1 = require("./core");
const configKeys_1 = require("./configKeys");
class MochaAdapter extends core_1.MochaAdapterCore {
    get tests() {
        return this.testsEmitter.event;
    }
    get testStates() {
        return this.testStatesEmitter.event;
    }
    get retire() {
        return this.retireEmitter.event;
    }
    get workspaceFolderPath() {
        return this.workspaceFolder.uri.fsPath;
    }
    constructor(workspaceFolder, workspaceState, outputChannel, log) {
        super(outputChannel, log);
        this.workspaceFolder = workspaceFolder;
        this.disposables = [];
        this.testsEmitter = new vscode.EventEmitter();
        this.testStatesEmitter = new vscode.EventEmitter();
        this.retireEmitter = new vscode.EventEmitter();
        this.configReader = new configReader_1.ConfigReader(workspaceFolder, workspaceState, (changedTestFiles, reloadConfig) => this.load(changedTestFiles, reloadConfig), (tests) => this.retireEmitter.fire({ tests }), log);
        this.disposables.push(this.configReader);
        this.disposables.push(this.testsEmitter);
        this.disposables.push(this.testStatesEmitter);
        this.disposables.push(this.retireEmitter);
        const config = vscode.workspace.getConfiguration(configKeys_1.configSection, this.workspaceFolder.uri);
        if (this.configReader.getAutoload(config) === false) {
            this.skipNextLoadRequest = true;
        }
    }
    enable() {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            yield this.configReader.enableAdapter();
            this.load();
        });
    }
    disable() {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            yield this.configReader.disableAdapter();
            this.load();
        });
    }
    startDebugging(config) {
        return tslib_1.__awaiter(this, void 0, void 0, function* () {
            const debuggerConfigName = config.debuggerConfig || 'Debug Mocha Tests';
            const debuggerConfig = config.debuggerConfig || {
                name: debuggerConfigName,
                type: 'pwa-node',
                request: 'attach',
                port: config.debuggerPort,
                continueOnAttach: true,
                autoAttachChildProcesses: false,
                resolveSourceMapLocations: [
                    "!**/node_modules/**",
                    "!**/.vscode/extensions/hbenl.vscode-mocha-test-adapter-*/**"
                ],
                skipFiles: [
                    "<node_internals>/**"
                ]
            };
            const debugSessionPromise = new Promise((resolve, reject) => {
                let subscription;
                subscription = vscode.debug.onDidStartDebugSession(debugSession => {
                    if ((debugSession.name === debuggerConfigName) && subscription) {
                        resolve(debugSession);
                        subscription.dispose();
                        subscription = undefined;
                    }
                });
                setTimeout(() => {
                    if (subscription) {
                        reject(new Error('Debug session failed to start within 5 seconds'));
                        subscription.dispose();
                        subscription = undefined;
                    }
                }, 5000);
            });
            const started = yield vscode.debug.startDebugging(this.workspaceFolder, debuggerConfig);
            if (started) {
                return yield debugSessionPromise;
            }
            else {
                throw new Error('Debug session couldn\'t be started');
            }
        });
    }
    onDidTerminateDebugSession(cb) {
        return vscode.debug.onDidTerminateDebugSession(cb);
    }
    dispose() {
        this.cancel();
        for (const disposable of this.disposables) {
            disposable.dispose();
        }
        this.disposables = [];
        this.nodesById.clear();
    }
}
exports.MochaAdapter = MochaAdapter;
//# sourceMappingURL=adapter.js.map