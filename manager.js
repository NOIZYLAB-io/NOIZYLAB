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
exports.ReplManager = void 0;
const vscode = __importStar(require("vscode"));
const fs = __importStar(require("fs"));
/**
 * Manages the SAPF REPL terminal lifecycle and provides code evaluation interface.
 * Singleton in charge of creating and managing the SAPF REPL terminal.
 */
class ReplManager {
    terminal;
    /**
     * Ensures the REPL terminal exists and returns it.
     * @returns The active REPL terminal
     * @throws Error if terminal creation fails
     */
    ensure() {
        if (!this.terminal) {
            const cfg = vscode.workspace.getConfiguration('sapf');
            const binaryPath = cfg.get('binaryPath', 'sapf');
            const preludePath = cfg.get('preludePath', '');
            // Validate prelude path if provided
            if (preludePath && !fs.existsSync(preludePath)) {
                vscode.window.showWarningMessage(`Prelude file not found: ${preludePath}`);
            }
            try {
                this.terminal = vscode.window.createTerminal('sapf');
                const command = `${binaryPath}${preludePath && fs.existsSync(preludePath) ? ` -p ${preludePath}` : ''}`;
                this.terminal.sendText(command);
                this.terminal.show(true);
            }
            catch (error) {
                vscode.window.showErrorMessage(`Failed to start SAPF terminal: ${error}`);
                throw error;
            }
        }
        return this.terminal;
    }
    /**
     * Sends code to the REPL, creating it if necessary.
     * @param code The code to send to the REPL
     */
    send(code) {
        try {
            this.ensure().sendText(code, true);
        }
        catch (error) {
            vscode.window.showErrorMessage(`Failed to send code to SAPF: ${error}`);
        }
    }
    /**
     * Disposes the REPL terminal if it is ours.
     */
    dispose() {
        this.terminal?.dispose();
        this.terminal = undefined;
    }
    /**
     * Clears internal handle when the user closes the terminal manually.
     * @param closed The terminal that was closed
     */
    handleClose(closed) {
        if (closed === this.terminal) {
            this.terminal = undefined;
        }
    }
}
exports.ReplManager = ReplManager;
//# sourceMappingURL=manager.js.map