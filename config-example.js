"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.validateApiKey = exports.watchConfigurationChanges = exports.updateApiKey = exports.getYouTubeMusicApiKey = void 0;
const vscode = require("vscode");
/**
 * Example snippet showing how to read YouTube Music configuration
 * This demonstrates the usage requested by the user.
 */
// Get the YouTube Music configuration section
const config = vscode.workspace.getConfiguration('youtubeMusic');
// Read specific configuration values
const apiKey = config.get('apiKey', ''); // Default to empty string if not set
const autoStart = config.get('autoStart', false); // Default to false if not set
// Alternative: Get all configuration as an object
const allConfig = config.get('youtubeMusic');
// Example function to safely get API key with validation
function getYouTubeMusicApiKey() {
    const config = vscode.workspace.getConfiguration('youtubeMusic');
    const apiKey = config.get('apiKey', '');
    if (!apiKey || apiKey.trim() === '') {
        vscode.window.showWarningMessage('YouTube Music: Please configure your API key in settings');
        return null;
    }
    return apiKey;
}
exports.getYouTubeMusicApiKey = getYouTubeMusicApiKey;
// Example function to update configuration programmatically
async function updateApiKey(newApiKey) {
    const config = vscode.workspace.getConfiguration('youtubeMusic');
    try {
        // Update the setting globally (can also use ConfigurationTarget.Workspace)
        await config.update('apiKey', newApiKey, vscode.ConfigurationTarget.Global);
        vscode.window.showInformationMessage('YouTube Music: API key updated successfully');
    }
    catch (error) {
        vscode.window.showErrorMessage(`Failed to update API key: ${error}`);
    }
}
exports.updateApiKey = updateApiKey;
// Example: Listen for configuration changes
function watchConfigurationChanges(context) {
    const disposable = vscode.workspace.onDidChangeConfiguration((event) => {
        if (event.affectsConfiguration('youtubeMusic')) {
            console.log('YouTube Music configuration changed');
            // Check which specific setting changed
            if (event.affectsConfiguration('youtubeMusic.apiKey')) {
                console.log('API key configuration changed');
                // Handle API key change
            }
            if (event.affectsConfiguration('youtubeMusic.autoStart')) {
                console.log('Auto-start configuration changed');
                // Handle auto-start change
            }
        }
    });
    context.subscriptions.push(disposable);
}
exports.watchConfigurationChanges = watchConfigurationChanges;
// Example: Validate API key format (basic validation)
function validateApiKey(apiKey) {
    // Basic validation - YouTube API keys are typically 39 characters
    // This is a simple check, actual validation would require an API call
    return apiKey.length >= 30 && /^[A-Za-z0-9_-]+$/.test(apiKey);
}
exports.validateApiKey = validateApiKey;
//# sourceMappingURL=config-example.js.map