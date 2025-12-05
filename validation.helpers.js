"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.VALIDATION_MESSAGES = exports.ENTITY_NAME_VALIDATION_MESSAGE = exports.ENTITY_NAME_PATTERN = exports.INVALID_CLASS_NAME_MESSAGE = exports.CLASS_NAME_PATTERN = exports.FOLDER_NAME_VALIDATION_MESSAGE = exports.FOLDER_NAME_PATTERN = void 0;
exports.validateFolderName = validateFolderName;
exports.validateClassName = validateClassName;
exports.validateEntityName = validateEntityName;
const vscode_1 = require("vscode");
/**
 * Validation patterns used across the application.
 */
/**
 * Regular expression pattern for validating folder names
 */
exports.FOLDER_NAME_PATTERN = /^(?!\/)[^\sÀ-ÿ]+?$/;
/**
 * Message for folder name validation errors
 */
exports.FOLDER_NAME_VALIDATION_MESSAGE = 'The folder name must be a valid name';
/**
 * Regular expression pattern for validating class names
 */
exports.CLASS_NAME_PATTERN = /^[A-Z][A-Za-z0-9]{2,}$/;
/**
 * Error message for invalid class names.
 */
exports.INVALID_CLASS_NAME_MESSAGE = 'Invalid format! Class names MUST be declared in PascalCase and have at least 3 characters (e.g. User, AuthService)';
/**
 * Regular expression pattern for validating entity names.
 * Ensures entity names are in camelCase and have at least 1 character.
 */
exports.ENTITY_NAME_PATTERN = /^[a-z][A-Za-z0-9-]+$/;
/**
 * Error message for invalid entity names.
 */
exports.ENTITY_NAME_VALIDATION_MESSAGE = 'Invalid format! Entity names MUST be declared in camelCase and have at least 1 character (e.g. user, authService)';
/**
 * Error messages for validation
 */
exports.VALIDATION_MESSAGES = {
    // biome-ignore lint/style/useNamingConvention: Use constants for validation messages
    FOLDER_NAME_INVALID: 'folder.name.invalid',
    // biome-ignore lint/style/useNamingConvention: Use constants for validation messages
    CLASS_NAME_INVALID: 'class.name.invalid',
    // biome-ignore lint/style/useNamingConvention: Use constants for validation messages
    ENTITY_NAME_INVALID: 'entity.name.invalid',
};
/**
 * Validates a folder name using the centralized folder name pattern
 *
 * @param path - The path to validate
 * @returns A validation error message if invalid, undefined if valid
 */
function validateFolderName(path) {
    if (!exports.FOLDER_NAME_PATTERN.test(path)) {
        return vscode_1.l10n.t(exports.FOLDER_NAME_VALIDATION_MESSAGE);
    }
    return;
}
/**
 * Validates a class name using the centralized class name pattern
 *
 * @param name - The class name to validate
 * @returns A validation error message if invalid, undefined if valid
 */
function validateClassName(name) {
    if (!exports.CLASS_NAME_PATTERN.test(name)) {
        return vscode_1.l10n.t(exports.INVALID_CLASS_NAME_MESSAGE);
    }
    return;
}
/**
 * Validates an entity name using the centralized entity name pattern.
 *
 * @param name - The entity name to validate.
 * @returns A validation error message if invalid, undefined if valid.
 */
function validateEntityName(name) {
    if (!exports.ENTITY_NAME_PATTERN.test(name)) {
        return vscode_1.l10n.t(exports.ENTITY_NAME_VALIDATION_MESSAGE);
    }
    return;
}
//# sourceMappingURL=validation.helpers.js.map