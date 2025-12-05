"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.FFmpegAudioRecorderLog = exports.ExtensionLog = exports.CursorIntegrationLog = exports.ConfigurationManagerLog = exports.RetryManagerLog = exports.ErrorHandlerLog = exports.RecoveryActionHandlerLog = exports.AudioQualityManagerLog = exports.LogLevel = void 0;
exports.initializeGlobalOutput = initializeGlobalOutput;
exports.getGlobalOutputChannel = getGlobalOutputChannel;
exports.logDebug = logDebug;
exports.logInfo = logInfo;
exports.logWarn = logWarn;
exports.logError = logError;
exports.logCritical = logCritical;
exports.log = log;
exports.showOutputChannel = showOutputChannel;
exports.clearOutputChannel = clearOutputChannel;
exports.disposeGlobalOutput = disposeGlobalOutput;
/**
 * Logging levels
 */
var LogLevel;
(function (LogLevel) {
    LogLevel["DEBUG"] = "\uD83D\uDD0D";
    LogLevel["INFO"] = "\u2139\uFE0F";
    LogLevel["WARN"] = "\u26A0\uFE0F";
    LogLevel["ERROR"] = "\u274C";
    LogLevel["CRITICAL"] = "\uD83D\uDEA8";
})(LogLevel || (exports.LogLevel = LogLevel = {}));
/**
 * Global outputChannel for the entire extension
 */
let globalOutputChannel = null;
/**
 * Initialization of the global outputChannel
 * Must be called in the activate() function of the extension
 */
function initializeGlobalOutput(outputChannel) {
    globalOutputChannel = outputChannel;
}
/**
 * Getting the global outputChannel
 */
function getGlobalOutputChannel() {
    return globalOutputChannel;
}
/**
 * Base logging function
 */
function logMessage(level, component, message, data, error) {
    const timestamp = new Date().toISOString();
    // If there are additional data, add them to the message
    let fullMessage = message;
    if (data !== undefined) {
        if (typeof data === 'string') {
            fullMessage += ` ${data}`;
        }
        else if (typeof data === 'object' && data !== null) {
            fullMessage += ` ${JSON.stringify(data)}`;
        }
        else {
            fullMessage += ` ${String(data)}`;
        }
    }
    const formattedMessage = `${timestamp} ${level} [${component}] ${fullMessage}`;
    // Log to the console (for debugging in DevTools)
    if (level === LogLevel.ERROR || level === LogLevel.CRITICAL) {
        console.error(formattedMessage);
        if (error) {
            console.error('Error details:', error);
        }
    }
    else if (level === LogLevel.WARN) {
        console.warn(formattedMessage);
    }
    else {
        console.log(formattedMessage);
    }
    // Log to the VS Code Output Channel if available
    if (globalOutputChannel) {
        globalOutputChannel.appendLine(formattedMessage);
        if (error) {
            globalOutputChannel.appendLine(`    Error: ${error.message}`);
            if (error.stack) {
                globalOutputChannel.appendLine(`    Stack: ${error.stack}`);
            }
        }
        // Show the panel for critical errors
        if (level === LogLevel.CRITICAL) {
            globalOutputChannel.show(true);
        }
    }
}
/**
 * Logging debug information
 */
function logDebug(component, message, data) {
    logMessage(LogLevel.DEBUG, component, message, data);
}
/**
 * Logging informational messages
 */
function logInfo(component, message, data) {
    logMessage(LogLevel.INFO, component, message, data);
}
/**
 * Logging warnings
 */
function logWarn(component, message, data) {
    logMessage(LogLevel.WARN, component, message, data);
}
/**
 * Logging errors
 */
function logError(component, message, data, error) {
    logMessage(LogLevel.ERROR, component, message, data, error);
}
/**
 * Logging critical errors
 */
function logCritical(component, message, data, error) {
    logMessage(LogLevel.CRITICAL, component, message, data, error);
}
/**
 * Universal logging function with arbitrary level
 */
function log(level, component, message, data, error) {
    logMessage(level, component, message, data, error);
}
/**
 * Utility functions for specific components
 */
// For AudioQualityManager
exports.AudioQualityManagerLog = {
    info: (message, data) => logInfo('AudioQualityManager', message, data),
    warn: (message, data) => logWarn('AudioQualityManager', message, data),
    error: (message, data, error) => logError('AudioQualityManager', message, data, error)
};
// For RecoveryActionHandler
exports.RecoveryActionHandlerLog = {
    info: (message, data) => logInfo('RecoveryActionHandler', message, data),
    warn: (message, data) => logWarn('RecoveryActionHandler', message, data),
    error: (message, data, error) => logError('RecoveryActionHandler', message, data, error)
};
// For ErrorHandler
exports.ErrorHandlerLog = {
    info: (message, data) => logInfo('ErrorHandler', message, data),
    warn: (message, data) => logWarn('ErrorHandler', message, data),
    error: (message, data, error) => logError('ErrorHandler', message, data, error)
};
// For RetryManager
exports.RetryManagerLog = {
    info: (message, data) => logInfo('RetryManager', message, data),
    warn: (message, data) => logWarn('RetryManager', message, data),
    error: (message, data, error) => logError('RetryManager', message, data, error)
};
// For ConfigurationManager
exports.ConfigurationManagerLog = {
    info: (message, data) => logInfo('ConfigurationManager', message, data),
    warn: (message, data) => logWarn('ConfigurationManager', message, data),
    error: (message, data, error) => logError('ConfigurationManager', message, data, error)
};
// For CursorIntegration
exports.CursorIntegrationLog = {
    debug: (message, data) => logDebug('CursorIntegration', message, data),
    info: (message, data) => logInfo('CursorIntegration', message, data),
    warn: (message, data) => logWarn('CursorIntegration', message, data),
    error: (message, data, error) => logError('CursorIntegration', message, data, error)
};
// For Extension (main module)
exports.ExtensionLog = {
    debug: (message, data) => logDebug('Extension', message, data),
    info: (message, data) => logInfo('Extension', message, data),
    warn: (message, data) => logWarn('Extension', message, data),
    error: (message, data, error) => logError('Extension', message, data, error)
};
// For FFmpegAudioRecorder
exports.FFmpegAudioRecorderLog = {
    debug: (message, data) => logDebug('FFmpegAudioRecorder', message, data),
    info: (message, data) => logInfo('FFmpegAudioRecorder', message, data),
    warn: (message, data) => logWarn('FFmpegAudioRecorder', message, data),
    error: (message, data, error) => logError('FFmpegAudioRecorder', message, data, error)
};
/**
 * Show Output Channel to the user
 */
function showOutputChannel() {
    if (globalOutputChannel) {
        globalOutputChannel.show();
    }
}
/**
 * Clear Output Channel
 */
function clearOutputChannel() {
    if (globalOutputChannel) {
        globalOutputChannel.clear();
    }
}
/**
 * Release resources when the extension is deactivated
 */
function disposeGlobalOutput() {
    if (globalOutputChannel) {
        globalOutputChannel.dispose();
        globalOutputChannel = null;
    }
}
//# sourceMappingURL=GlobalOutput.js.map