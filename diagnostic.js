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
Object.defineProperty(exports, "__esModule", { value: true });
exports.CommandDiagnostics = void 0;
exports.registerDiagnosticCommand = registerDiagnosticCommand;
const vscode = __importStar(require("vscode"));
/**
 * Diagnostics for checking command registration and operation
 */
class CommandDiagnostics {
    /**
     * Checks if extension commands are registered
     */
    static async checkCommandRegistration() {
        const expectedCommands = [
            'speechToTextWhisper.recordAndInsertOrClipboard',
            'speechToTextWhisper.recordAndOpenCurrentChat',
            'speechToTextWhisper.runDiagnostics',
            'speechToTextWhisper.testFFmpeg',
            'speechToTextWhisper.testAudioRecorder',
            'speechToTextWhisper.openSettings',
            'speechToTextWhisper.toggleMode'
        ];
        const registrationStatus = {};
        for (const commandId of expectedCommands) {
            try {
                // Get list of all commands
                const allCommands = await vscode.commands.getCommands(true);
                registrationStatus[commandId] = allCommands.includes(commandId);
            }
            catch (error) {
                registrationStatus[commandId] = false;
            }
        }
        return registrationStatus;
    }
    /**
     * Checks extension activation
     */
    static async checkExtensionActivation() {
        try {
            const extension = vscode.extensions.getExtension('speak-y.speech-to-text-whisper');
            if (!extension) {
                return { isActive: false };
            }
            return {
                isActive: extension.isActive,
                packageJson: extension.packageJSON,
                extensionId: extension.id,
                activationEvents: extension.packageJSON?.activationEvents || []
            };
        }
        catch (error) {
            return {
                isActive: false,
                packageJson: { error: error.message }
            };
        }
    }
    /**
     * Attempts to execute a command and check its functionality
     */
    static async testCommandExecution(commandId) {
        const startTime = Date.now();
        try {
            await vscode.commands.executeCommand(commandId);
            return {
                success: true,
                executionTime: Date.now() - startTime
            };
        }
        catch (error) {
            return {
                success: false,
                error: error.message,
                executionTime: Date.now() - startTime
            };
        }
    }
    /**
     * Full extension diagnostics
     */
    static async runFullDiagnostics() {
        console.log('🔍 Running full extension diagnostics...');
        // Check extension activation
        const extensionStatus = await this.checkExtensionActivation();
        console.log('📊 Extension status:', extensionStatus);
        // Check command registration
        const commandStatus = await this.checkCommandRegistration();
        console.log('📊 Command status:', commandStatus);
        // Test command execution (safe ones only)
        const safeCommandsToTest = [
            'speechToTextWhisper.runDiagnostics',
            'speechToTextWhisper.testFFmpeg',
            'speechToTextWhisper.testAudioRecorder',
            'speechToTextWhisper.openSettings'
        ];
        const commandTests = {};
        for (const commandId of safeCommandsToTest) {
            if (commandStatus[commandId]) {
                commandTests[commandId] = await this.testCommandExecution(commandId);
            }
            else {
                commandTests[commandId] = { success: false, error: 'Command not registered' };
            }
        }
        // Check keybindings
        const keybindings = await this.getKeybindings();
        const result = {
            extension: extensionStatus,
            commands: commandStatus,
            commandTests,
            keybindings
        };
        console.log('📊 Diagnostics results:', JSON.stringify(result, null, 2));
        return result;
    }
    /**
     * Gets keybinding information
     */
    static async getKeybindings() {
        try {
            // VS Code API does not provide direct access to keybindings
            // Returning expected bindings from package.json
            const expectedKeybindings = [
                { command: 'speechToTextWhisper.recordAndInsertOrClipboard', key: 'ctrl+shift+m', mac: 'cmd+shift+m' },
                { command: 'speechToTextWhisper.recordAndOpenCurrentChat', key: 'ctrl+shift+n', mac: 'cmd+shift+n' }
            ];
            return expectedKeybindings;
        }
        catch (error) {
            return [];
        }
    }
}
exports.CommandDiagnostics = CommandDiagnostics;
/**
 * Command for diagnosing extension issues
 */
async function registerDiagnosticCommand(context) {
    const disposable = vscode.commands.registerCommand('speechToTextWhisper.runFullDiagnostics', async () => {
        try {
            const diagnostics = await CommandDiagnostics.runFullDiagnostics();
            // Create report
            const report = [
                '🔍 Speech-to-Text Whisper Extension Diagnostics',
                '='.repeat(50),
                '',
                '📊 Extension Status:',
                `- Active: ${diagnostics.extension.isActive}`,
                '',
                '📋 Commands:',
                ...Object.entries(diagnostics.commands).map(([cmd, registered]) => `- ${cmd}: ${registered ? '✅' : '❌'}`),
                '',
                '🧪 Command Tests:',
                ...Object.entries(diagnostics.commandTests).map(([cmd, result]) => `- ${cmd}: ${result.success ? '✅' : '❌'} ${result.error ? `(${result.error})` : ''}`),
                '',
                '⌨️ Keybindings:',
                ...diagnostics.keybindings.map(kb => `- ${kb.command}: ${kb.key}${kb.mac ? ` / ${kb.mac}` : ''}`)
            ].join('\n');
            // Show report in a new document
            const doc = await vscode.workspace.openTextDocument({
                content: report,
                language: 'plaintext'
            });
            await vscode.window.showTextDocument(doc);
            // Also show a brief result in a notification
            const registeredCount = Object.values(diagnostics.commands).filter(Boolean).length;
            const totalCount = Object.keys(diagnostics.commands).length;
            vscode.window.showInformationMessage(`🔍 Diagnostics complete: ${registeredCount}/${totalCount} commands registered`);
        }
        catch (error) {
            vscode.window.showErrorMessage(`❌ Diagnostics error: ${error.message}`);
        }
    });
    context.subscriptions.push(disposable);
}
//# sourceMappingURL=diagnostic.js.map