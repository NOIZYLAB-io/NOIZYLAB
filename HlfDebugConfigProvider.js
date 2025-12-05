"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.HlfDebugConfigProvider = void 0;
const path = require("path");
const vscode = require("vscode");
const Constants_1 = require("../utilities/Constants");
const TelemetryLogger_1 = require("../utilities/TelemetryLogger");
const HlfProvider_1 = require("./HlfProvider");
const fs = require("fs/promises");
const WebsiteView_1 = require("../views/WebsiteView");
const crypto_1 = require("crypto");
class HlfDebugConfigProvider {
    async resolveDebugConfiguration(folder, debugConfiguration) {
        let language = "";
        if (!HlfProvider_1.HlfProvider.islocalNetworkStarted || (await HlfProvider_1.HlfProvider.shouldRestart(debugConfiguration))) {
            //Launch Fabric network if its not up yet.
            Constants_1.Settings.isCaas = debugConfiguration.isCaas;
            HlfProvider_1.HlfProvider.setChaincodeName(debugConfiguration.chaincodeName);
            HlfProvider_1.HlfProvider.islocalNetworkStarted = await HlfProvider_1.HlfProvider.createNetwork();
            //If we failed to start the network, then return undefined to cancel the debugging session
            if (!HlfProvider_1.HlfProvider.islocalNetworkStarted) {
                return undefined;
            }
            //Start event listener to detect and log all chaincode events.
            await HlfProvider_1.HlfProvider.startChaincodeListener();
            WebsiteView_1.WebsiteView.showMessage();
        }
        if (!debugConfiguration.args) {
            debugConfiguration.args = [];
        }
        //Depending on the language used to develop the chaincode, choose the approriate debugger.
        switch (debugConfiguration.type) {
            case Constants_1.DebuggerType.hlfGo: {
                language = "go";
                debugConfiguration.type = Constants_1.ChaincodeLang.hlfGo;
                if (!debugConfiguration.program) {
                    debugConfiguration.program = '${fileDirname}';
                }
                break;
            }
            case Constants_1.DebuggerType.hlfNode: {
                language = "javascript";
                debugConfiguration.type = Constants_1.ChaincodeLang.hlfNode;
                if (process.platform === "win32") {
                    debugConfiguration.program = path.join(folder.uri.fsPath, 'node_modules', 'fabric-shim', 'cli');
                }
                else {
                    debugConfiguration.program = path.join(folder.uri.fsPath, 'node_modules', '.bin', 'fabric-chaincode-node');
                }
                if (debugConfiguration.isCaas) {
                    debugConfiguration.args.push('server');
                }
                else {
                    debugConfiguration.args.push('start');
                }
                const files = await fs.readdir(folder.uri.fsPath);
                if (files.includes('tsconfig.json')) {
                    language = "typescript";
                    debugConfiguration.preLaunchTask = 'tsc: build - tsconfig.json';
                    debugConfiguration.outFiles = [
                        '${workspaceFolder}/dist/**/*.js'
                    ];
                }
                break;
            }
        }
        //Add other default values
        if (!debugConfiguration.request) {
            debugConfiguration.request = 'launch';
        }
        if (!debugConfiguration.mode) {
            debugConfiguration.mode = 'auto';
        }
        if (debugConfiguration.isCaas) {
            //Add environment variables for Fabric CaaS model
            debugConfiguration.env = { ...debugConfiguration.env, ...Constants_1.Settings.debugCaasEnv };
        }
        else {
            //Add environment variables for Fabric 'dev' mode
            debugConfiguration.env = { ...debugConfiguration.env, ...Constants_1.Settings.debugEnv };
        }
        if (!debugConfiguration.isCaas) {
            //Add peer address to the arguments
            debugConfiguration.args.push('--peer.address', Constants_1.Settings.peerAddress);
        }
        //Create a project id using hash of workspace folder. Md5 is used here as this is only to generate a unique if and not for security purposes.
        const projectId = (0, crypto_1.createHash)('md5').update(folder.uri.toString()).digest("hex");
        TelemetryLogger_1.TelemetryLogger.instance().sendTelemetryEvent('ResolveDebug', { 'debugType': debugConfiguration.type,
            'isCaas': debugConfiguration.isCaas.toString(), 'language': language, 'projectId': projectId });
        //Simply changing the Debugger type will result in an error as the debugger type has already been determined by this time
        //We need to cancel the existing debugging session and start a new one with the modified configuration.
        delete debugConfiguration.name;
        vscode.debug.startDebugging(folder, debugConfiguration);
        return undefined;
    }
}
exports.HlfDebugConfigProvider = HlfDebugConfigProvider;
//# sourceMappingURL=HlfDebugConfigProvider.js.map