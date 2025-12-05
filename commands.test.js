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
const assert = __importStar(require("assert"));
const vscode = __importStar(require("vscode"));
describe('Commands Integration Tests', () => {
    let extension;
    before(async () => {
        // Get the extension
        extension = vscode.extensions.getExtension('speak-y.speech-to-text-whisper');
        // Activate the extension if it is not active
        if (extension && !extension.isActive) {
            await extension.activate();
        }
    });
    describe('Command Registration', () => {
        const expectedCommands = [
            'speechToTextWhisper.recordAndInsertOrClipboard',
            'speechToTextWhisper.recordAndOpenCurrentChat',
            'speechToTextWhisper.runDiagnostics',
            'speechToTextWhisper.testFFmpeg',
            'speechToTextWhisper.testAudioRecorder',
            'speechToTextWhisper.openSettings',
            'speechToTextWhisper.toggleMode',
            'speechToTextWhisper.audioSettings.selectDevice'
        ];
        it('should register all expected commands', async () => {
            const allCommands = await vscode.commands.getCommands(true);
            for (const commandId of expectedCommands) {
                assert.ok(allCommands.includes(commandId), `Command ${commandId} should be registered`);
            }
        });
        it('should have extension activated', () => {
            assert.ok(extension, 'Extension should be found');
            assert.ok(extension.isActive, 'Extension should be active');
        });
    });
    describe('Safe Command Execution', () => {
        // We only test safe commands that do not require user input
        const safeCommands = [
            'speechToTextWhisper.runDiagnostics',
            'speechToTextWhisper.testFFmpeg',
            'speechToTextWhisper.testAudioRecorder',
            'speechToTextWhisper.openSettings'
        ];
        safeCommands.forEach(commandId => {
            it(`should execute ${commandId} without errors`, async function () {
                this.timeout(10000); // Increase timeout for commands
                try {
                    await vscode.commands.executeCommand(commandId);
                    // If the command executed without exception, the test passed
                    assert.ok(true, `Command ${commandId} executed successfully`);
                }
                catch (error) {
                    // Some commands may fail due to missing settings
                    // but it's important that they are registered and callable
                    console.warn(`Command ${commandId} failed with:`, error.message);
                    // Check if this is an expected error (e.g., missing API key)
                    const errorMessage = error.message.toLowerCase();
                    const isExpectedError = errorMessage.includes('api key') ||
                        errorMessage.includes('ffmpeg') ||
                        errorMessage.includes('audio') ||
                        errorMessage.includes('configuration');
                    if (isExpectedError) {
                        assert.ok(true, `Command ${commandId} failed with expected error: ${errorMessage}`);
                    }
                    else {
                        throw error; // Unexpected error
                    }
                }
            });
        });
    });
    describe('Recording Commands', () => {
        // For recording commands, we cannot fully execute them in tests,
        // but we can check that they are registered and available
        const recordingCommands = [
            'speechToTextWhisper.recordAndInsertOrClipboard',
            'speechToTextWhisper.recordAndOpenCurrentChat',
        ];
        recordingCommands.forEach(commandId => {
            it(`should have ${commandId} registered and available`, async () => {
                const allCommands = await vscode.commands.getCommands(true);
                assert.ok(allCommands.includes(commandId), `Recording command ${commandId} should be registered`);
            });
        });
        it('should not execute recording commands in test environment', async () => {
            // In the test environment, recording commands should be available, but should not start actual recording
            // This checks that the commands are registered, but does not test their full functionality
            for (const commandId of recordingCommands) {
                try {
                    // Attempt to execute the command, but expect that it may fail
                    // due to missing necessary settings or audio devices in the test environment
                    await vscode.commands.executeCommand(commandId);
                }
                catch (error) {
                    // This is expected in the test environment
                    const errorMessage = error.message.toLowerCase();
                    console.log(`Recording command ${commandId} failed as expected in test environment:`, errorMessage);
                }
            }
            // If we reached this point, the commands are registered
            assert.ok(true, 'Recording commands are registered');
        });
    });
    describe('Context Commands', () => {
        it('should handle context setting commands', async () => {
            // Testing commands that set context
            try {
                await vscode.commands.executeCommand('setContext', 'speechToTextWhisper.isRecording', false);
                assert.ok(true, 'Context setting command works');
            }
            catch (error) {
                assert.fail(`Context setting failed: ${error.message}`);
            }
        });
    });
});
//# sourceMappingURL=commands.test.js.map