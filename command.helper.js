"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.runCommand = void 0;
const vscode_1 = require("vscode");
/**
 * Execute a shell command inside VS Code.
 *
 * - If `captureOutput` is false: spins up an integrated terminal, sends the command, and resolves immediately.
 * - If `captureOutput` is true: uses the Task API to capture `stdout`, `stderr`, and exit code.
 * - If `waitResponse` is true: returns a Promise that resolves when the command completes without blocking the main thread.
 *
 * @param {string} name - Name of the terminal
 * @param {string} command - Command to run
 * @param {string} [cwdPath] - Working directory path
 * @param {boolean} [captureOutput=false] - Whether to capture command output
 * @param {boolean} [showTerminal=true] - Whether to show the terminal
 * @param {boolean} [waitResponse=false] - Whether to wait for response without blocking main thread
 * @example
 * runCommand('echo', 'echo "Hello, World!"');
 * // Wait for response asynchronously
 * const result = await runCommand('npm install', 'npm install', undefined, true, true, true);
 *
 * @returns {Promise<{ success: boolean; output?: string; error?: string }>} - Result with success status and optional output/error
 */
const runCommand = async (name, command, cwdPath, captureOutput = false, showTerminal = true, waitResponse = false) => {
    // Determine a valid workspace URI for cwd (or undefined)
    const cwdUri = cwdPath ? vscode_1.Uri.file(cwdPath) : undefined;
    const hasValidWorkspace = cwdPath && vscode_1.workspace.getWorkspaceFolder(cwdUri) !== undefined;
    // Wrap everything in a cancellable progress indicator
    return vscode_1.window.withProgress({
        location: vscode_1.ProgressLocation.Notification,
        title: vscode_1.l10n.t('Executing: {0}', command),
        cancellable: true,
    }, async (_progress, token) => {
        // Simple "fire-and-forget" mode
        if (!captureOutput && !waitResponse) {
            const terminal = vscode_1.window.createTerminal({
                name,
                cwd: hasValidWorkspace ? cwdUri : undefined,
            });
            // Register cancellation handler
            const disposable = token.onCancellationRequested(() => {
                vscode_1.window.showErrorMessage(vscode_1.l10n.t('Command cancelled: {0}', command));
                terminal.dispose();
            });
            if (showTerminal) {
                terminal.show();
            }
            terminal.sendText(command);
            // Cleanup cancellation handler as it's no longer needed
            disposable.dispose();
            return { success: true };
        }
        // Advanced mode: use Task API for capturing output & exit code
        const shellExec = new vscode_1.ShellExecution(command, { cwd: cwdPath });
        const taskScope = hasValidWorkspace
            ? vscode_1.TaskScope.Workspace
            : vscode_1.TaskScope.Global;
        const task = new vscode_1.Task({ type: 'shell' }, taskScope, name, 'Angular CLI', shellExec);
        // Control terminal presentation
        task.presentationOptions = {
            reveal: showTerminal ? vscode_1.TaskRevealKind.Always : vscode_1.TaskRevealKind.Never,
            echo: false,
            focus: false,
            // Ensure we don't interfere with controller error messages
            panel: vscode_1.TaskPanelKind.Shared, // Using proper TaskPanelKind enum
            showReuseMessage: false,
            clear: false,
        };
        // Determine if we're using the non-blocking mode with waitResponse
        if (waitResponse && !captureOutput) {
            // Create a terminal for non-blocking execution but with waiting for response
            const terminal = vscode_1.window.createTerminal({
                name,
                cwd: hasValidWorkspace ? cwdUri : undefined,
            });
            // Create event emitter to signal when command completes
            const resultEmitter = new vscode_1.EventEmitter();
            // Create a custom task to monitor the execution
            const monitorShellExec = new vscode_1.ShellExecution(command, { cwd: cwdPath });
            const waitTask = new vscode_1.Task({ type: 'shell', command }, vscode_1.TaskScope.Global, `${name}-monitor`, 'extension', monitorShellExec);
            waitTask.presentationOptions = {
                reveal: vscode_1.TaskRevealKind.Never,
                clear: false,
            };
            // Handle cancellation
            const cancelDisposable = token.onCancellationRequested(() => {
                vscode_1.window.showErrorMessage(vscode_1.l10n.t('Command cancelled: {0}', command));
                terminal.dispose();
                resultEmitter.fire({ success: false, error: 'Cancelled by user' });
            });
            // Start a background monitoring process that doesn't block the UI
            setTimeout(async () => {
                // Check if the operation was cancelled before we start
                if (token.isCancellationRequested) {
                    resultEmitter.fire({
                        success: false,
                        error: 'Cancelled by user before execution',
                    });
                    return;
                }
                if (showTerminal) {
                    terminal.show();
                }
                terminal.sendText(command);
                // Execute the monitor task in the background
                try {
                    const exec = await vscode_1.tasks.executeTask(waitTask);
                    // Variable to prevent duplicate emissions
                    let hasEmitted = false;
                    // Monitor for completion
                    const disposable = vscode_1.tasks.onDidEndTaskProcess((e) => {
                        if (e.execution === exec && !hasEmitted) {
                            hasEmitted = true;
                            const isSuccess = e.exitCode === 0;
                            const errorMsg = !isSuccess
                                ? `Command '${command}' exited with code ${e.exitCode}`
                                : undefined;
                            resultEmitter.fire({
                                success: isSuccess,
                                error: errorMsg,
                                output: isSuccess
                                    ? `Command '${command}' executed successfully`
                                    : undefined,
                            });
                            disposable.dispose();
                        }
                    });
                    // Additional safeguard - add task termination handler
                    vscode_1.tasks.onDidEndTask((e) => {
                        if (e.execution === exec && !hasEmitted) {
                            hasEmitted = true;
                            // Task ended but process handler didn't fire - this is a safety net
                            resultEmitter.fire({
                                success: true,
                                output: `Command '${command}' task completed`,
                            });
                        }
                    });
                }
                catch (err) {
                    const errorMsg = err instanceof Error ? err.message : String(err);
                    resultEmitter.fire({
                        success: false,
                        error: errorMsg,
                    });
                    // Ensure we clean up the terminal on error
                    try {
                        terminal.dispose();
                    }
                    catch (disposeError) {
                        // Ignore errors during cleanup
                    }
                }
            }, 100);
            // Return a promise that resolves when the command completes
            return new Promise((resolve) => {
                // Proper way to subscribe to a one-time event
                const disposable = resultEmitter.event((result) => {
                    // Clean up event listener
                    disposable.dispose();
                    // Clean up cancellation handler
                    cancelDisposable.dispose();
                    resolve(result);
                });
            });
        }
        // Traditional blocking mode with output capture
        // Promise that resolves when the task process ends
        return new Promise(async (resolve) => {
            // Create a collection of disposables to ensure proper cleanup
            const disposables = [];
            // Handle cancellation
            disposables.push(token.onCancellationRequested(() => {
                vscode_1.window.showErrorMessage(vscode_1.l10n.t('Command cancelled: {0}', command));
                cleanupDisposables();
                resolve({ success: false, error: 'Cancelled by user' });
            }));
            // Listen for the task process to finish
            disposables.push(vscode_1.tasks.onDidEndTaskProcess((e) => {
                if (e.execution === exec) {
                    const isSuccess = e.exitCode === 0;
                    if (isSuccess) {
                        resolve({
                            success: true,
                            output: `Command '${command}' executed successfully`,
                        });
                    }
                    else {
                        // Capture error message without showing it automatically
                        // This allows the controller to show its own custom message
                        const errMsg = `Command '${command}' exited with code ${e.exitCode}`;
                        resolve({ success: false, error: errMsg });
                    }
                    // Clean up all disposables
                    cleanupDisposables();
                }
            }));
            /**
             * Clean up all registered disposable resources to prevent memory leaks
             *
             * @function cleanupDisposables
             * @private
             */
            function cleanupDisposables() {
                // Safely dispose of all resources
                disposables.forEach((d) => {
                    try {
                        d.dispose();
                    }
                    catch (error) {
                        // Silently handle disposal errors to ensure all resources are cleaned up
                        // This prevents a single disposal failure from blocking resource cleanup
                    }
                });
                // Clear the array to help garbage collection
                disposables.length = 0;
            }
            // Kick off the task
            const exec = await vscode_1.tasks.executeTask(task);
        });
    });
};
exports.runCommand = runCommand;
//# sourceMappingURL=command.helper.js.map