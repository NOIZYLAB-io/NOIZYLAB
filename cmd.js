"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Commands = void 0;
const vscode = __importStar(require("vscode"));
const version_1 = require("../util/version");
const os_1 = require("os");
const path_1 = require("path");
const cmd_1 = require("../@types/cmd");
const agent_1 = require("../@types/agent");
const logger_1 = require("../util/logger");
class Commands {
    constructor(disposable, keploy) {
        this.disposable = disposable;
        this.keploy = keploy;
        this.registerCommands();
    }
    registerCommands() {
        logger_1.Logger.info('Registering commands');
        const commands = [
            vscode.commands.registerCommand(cmd_1.KeployCommand.SIGN_IN_GITHUB, this.keploy.SignInViaGitHubVSCode.bind(this.keploy)),
            vscode.commands.registerCommand(cmd_1.KeployCommand.SIGN_IN_GOOGLE, this.keploy.SignInViaKeploy.bind(this.keploy)),
            vscode.commands.registerCommand(cmd_1.KeployCommand.SIGN_IN_MICROSOFT, this.keploy.SignInViaKeploy.bind(this.keploy)),
            vscode.commands.registerCommand(cmd_1.KeployCommand.SIGN_OUT, this.keploy.SignOut.bind(this.keploy)),
            vscode.commands.registerCommand(cmd_1.KeployCommand.VIEW_CHANGELOG, this.viewChangeLog.bind(this)),
            vscode.commands.registerCommand(cmd_1.KeployCommand.VIEW_DOCUMENTATION, this.viewDocumentation.bind(this)),
            vscode.commands.registerCommand(cmd_1.KeployCommand.VIEW_SERVER_LOGS, this.viewServerLogs.bind(this)),
            vscode.commands.registerCommand(cmd_1.KeployCommand.VIEW_KEPLOY_VERSION, this.viewKeployVersion.bind(this)),
            vscode.commands.registerCommand(cmd_1.KeployCommand.CLEAR_STATE, this.keploy.ClearKeployState.bind(this.keploy)),
            vscode.commands.registerCommand(cmd_1.KeployCommand.RUN_UTG, this.keploy.Utg.bind(this.keploy)),
        ];
        logger_1.Logger.info('Commands registered');
        this.disposable.push(...commands);
    }
    viewChangeLog() {
        vscode.env.openExternal(vscode.Uri.parse('https://marketplace.visualstudio.com/items?itemName=Keploy.keployio'));
    }
    viewDocumentation() {
        vscode.env.openExternal(vscode.Uri.parse('https://keploy.io/docs/'));
    }
    viewServerLogs() {
        const logFilePath = (0, path_1.join)((0, os_1.tmpdir)(), agent_1.SERVER_LOG_FILE);
        vscode.workspace.openTextDocument(logFilePath).then((doc) => vscode.window.showTextDocument(doc));
    }
    viewKeployVersion() {
        return __awaiter(this, void 0, void 0, function* () {
            let currentVersion = process.platform === agent_1.OS.WINDOWS
                ? (yield (0, version_1.getCurrentKeployWindowsVersion)()) || ''
                : yield (0, version_1.getCurrentKeployVersion)();
            vscode.window.showInformationMessage(`(Keploy) AI Agent version: ${currentVersion}`);
        });
    }
}
exports.Commands = Commands;
//# sourceMappingURL=cmd.js.map