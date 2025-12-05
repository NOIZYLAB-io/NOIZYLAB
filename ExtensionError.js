"use strict";
/**
 * Custom error classes for the extension
 * @module errors
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.ErrorHandler = exports.AugmentAPIError = exports.ConfigurationError = exports.UIError = exports.ProcessingError = exports.ValidationError = exports.ExtensionError = void 0;
const types_1 = require("../types");
/**
 * Base extension error class
 */
class ExtensionError extends Error {
    type;
    code;
    details;
    timestamp;
    constructor(message, type = types_1.ErrorType.PROCESSING_ERROR, code, details) {
        super(message);
        this.name = 'ExtensionError';
        this.type = type;
        this.code = code;
        this.details = details;
        this.timestamp = new Date();
        // Maintains proper stack trace for where our error was thrown (only available on V8)
        if (Error.captureStackTrace) {
            Error.captureStackTrace(this, ExtensionError);
        }
    }
    /**
     * Convert error to JSON for logging
     */
    toJSON() {
        return {
            name: this.name,
            message: this.message,
            type: this.type,
            code: this.code,
            details: this.details,
            timestamp: this.timestamp.toISOString(),
            stack: this.stack
        };
    }
}
exports.ExtensionError = ExtensionError;
/**
 * Validation error
 */
class ValidationError extends ExtensionError {
    constructor(message, code, details) {
        super(message, types_1.ErrorType.VALIDATION_ERROR, code, details);
        this.name = 'ValidationError';
    }
}
exports.ValidationError = ValidationError;
/**
 * Processing error
 */
class ProcessingError extends ExtensionError {
    constructor(message, code, details) {
        super(message, types_1.ErrorType.PROCESSING_ERROR, code, details);
        this.name = 'ProcessingError';
    }
}
exports.ProcessingError = ProcessingError;
/**
 * UI error
 */
class UIError extends ExtensionError {
    constructor(message, code, details) {
        super(message, types_1.ErrorType.UI_ERROR, code, details);
        this.name = 'UIError';
    }
}
exports.UIError = UIError;
/**
 * Configuration error
 */
class ConfigurationError extends ExtensionError {
    constructor(message, code, details) {
        super(message, types_1.ErrorType.CONFIGURATION_ERROR, code, details);
        this.name = 'ConfigurationError';
    }
}
exports.ConfigurationError = ConfigurationError;
/**
 * Augment API error
 */
class AugmentAPIError extends ExtensionError {
    constructor(message, code, details) {
        super(message, types_1.ErrorType.AUGMENT_API_ERROR, code, details);
        this.name = 'AugmentAPIError';
    }
}
exports.AugmentAPIError = AugmentAPIError;
/**
 * Error handler utility
 */
class ErrorHandler {
    /**
     * Handle error and show appropriate message to user
     */
    static handle(error, context) {
        const errorMessage = context
            ? `${context}: ${error.message}`
            : error.message;
        if (error instanceof ExtensionError) {
            console.error(`[${error.type}] ${errorMessage}`, error.toJSON());
        }
        else {
            console.error(errorMessage, error);
        }
    }
    /**
     * Wrap async function with error handling
     */
    static async wrapAsync(fn, context) {
        try {
            return await fn();
        }
        catch (error) {
            this.handle(error, context);
            return null;
        }
    }
    /**
     * Wrap sync function with error handling
     */
    static wrapSync(fn, context) {
        try {
            return fn();
        }
        catch (error) {
            this.handle(error, context);
            return null;
        }
    }
}
exports.ErrorHandler = ErrorHandler;
//# sourceMappingURL=ExtensionError.js.map