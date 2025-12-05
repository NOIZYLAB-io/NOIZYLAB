"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.showWarning = exports.showError = exports.showMessage = exports.pickItemWithIcons = exports.pickItem = exports.getName = exports.getPath = void 0;
const vscode_1 = require("vscode");
/**
 * Displays a message box with the provided message
 *
 * @param {string} prompt - The prompt to display
 * @param {string} placeHolder - The input placeholder
 * @param {string} currentPath - The current path
 * @param {string} validate - The validation function
 * @example
 * const path = await getPath('Enter a path', 'src/app', 'src/app', (path) => {
 *   if (path.length === 0) {
 *     return 'Path cannot be empty';
 * });
 *
 * @returns {Promise<string | undefined>} - The selected path
 */
const getPath = async (prompt, placeHolder, currentPath, validate) => {
    return await vscode_1.window.showInputBox({
        prompt,
        placeHolder,
        value: currentPath,
        validateInput: validate,
    });
};
exports.getPath = getPath;
/**
 * Displays a message box with the provided message
 *
 * @param {string} prompt - The prompt to display
 * @param {string} placeHolder - The input placeholder
 * @param {string} validate - The validation function
 * @returns {Promise<string | undefined>} - The selected name
 */
const getName = async (prompt, placeHolder, validate) => {
    return await vscode_1.window.showInputBox({
        prompt,
        placeHolder,
        validateInput: validate,
    });
};
exports.getName = getName;
/**
 * Displays a message box with the provided message
 *
 * @param {string[]} items - The list of items to select from
 * @param {string} placeHolder - The input placeholder
 * @example
 * const item = await pickItem(['foo', 'bar'], 'Select an item');
 *
 * @returns {Promise<string | undefined>} - The selected item
 */
const pickItem = async (items, placeHolder) => {
    return await vscode_1.window.showQuickPick(items, {
        placeHolder,
    });
};
exports.pickItem = pickItem;
/**
 * Displays an enhanced selection box with icons and descriptions
 *
 * @param {Array} items - Array of objects with label, value, icon and description
 * @param {string} placeHolder - The input placeholder
 * @example
 * const item = await pickItemWithIcons([
 *   { label: 'Component', value: 'component', icon: '$(preview)', description: 'Create a new UI component' },
 *   { label: 'Service', value: 'service', icon: '$(gear)', description: 'Create a new service' }
 * ], 'Select item type');
 *
 * @returns {Promise<string | undefined>} - The selected item value
 */
const pickItemWithIcons = async (items, placeHolder) => {
    // Convert items to EnhancedQuickPickItem format
    const quickPickItems = items.map((item) => ({
        label: item.icon ? `${item.icon} ${item.label}` : item.label,
        value: item.value,
        description: item.description || '',
    }));
    const selectedItem = await vscode_1.window.showQuickPick(quickPickItems, {
        placeHolder,
        matchOnDescription: true,
    });
    return selectedItem?.value;
};
exports.pickItemWithIcons = pickItemWithIcons;
/**
 * Displays a message box with the provided message
 *
 * @param {string} message - The message to display
 * @example
 * await showMessage('Hello, world!');
 *
 * @returns {Promise<void>} - No return value
 */
const showMessage = async (message) => {
    vscode_1.window.showInformationMessage(message);
};
exports.showMessage = showMessage;
/**
 * Displays a message box with the provided message
 *
 * @param {string} message - The message to display
 * @example
 * await showError('An error occurred');
 *
 * @returns {Promise<void>} - No return value
 */
const showError = async (message) => {
    vscode_1.window.showErrorMessage(message);
};
exports.showError = showError;
/**
 * Displays a message box with the provided message
 *
 * @param {string} message - The message to display
 * @example
 * await showWarning('This is a warning');
 *
 * @returns {Promise<void>} - No return value
 */
const showWarning = async (message) => {
    vscode_1.window.showWarningMessage(message);
};
exports.showWarning = showWarning;
//# sourceMappingURL=dialog.helper.js.map