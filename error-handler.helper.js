"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.throwError = throwError;
exports.formatError = formatError;
/**
 * Centralized error handler for parsing and provider modules.
 * Throws or formats errors in a consistent way across the codebase.
 *
 * @param message The error message.
 * @param originalError (Optional) The original error object.
 * @throws Error
 *
 * @example
 * throwError('Invalid format', err);
 */
function throwError(message, originalError) {
    const details = originalError instanceof Error ? `: ${originalError.message}` : '';
    throw new Error(`[JSON Flow] ${message}${details}`);
}
/**
 * Formats an error for display or logging.
 * @param message The error message.
 * @param originalError (Optional) The original error object.
 * @returns Formatted error string.
 */
function formatError(message, originalError) {
    const details = originalError instanceof Error ? `: ${originalError.message}` : '';
    return `[JSON Flow] ${message}${details}`;
}
//# sourceMappingURL=error-handler.helper.js.map