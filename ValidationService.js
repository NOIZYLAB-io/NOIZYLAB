"use strict";
/**
 * Input validation service
 * @module services/ValidationService
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.ValidationService = void 0;
const constants_1 = require("../constants");
const ExtensionError_1 = require("../errors/ExtensionError");
const Logger_1 = require("../utils/Logger");
/**
 * Service for validating and fixing user input
 */
class ValidationService {
    static instance;
    log = Logger_1.logger.createChild('ValidationService');
    constructor() { }
    /**
     * Get singleton instance
     */
    static getInstance() {
        if (!ValidationService.instance) {
            ValidationService.instance = new ValidationService();
        }
        return ValidationService.instance;
    }
    /**
     * Comprehensive input validation
     */
    validateInput(text) {
        const endTimer = this.log.startTimer('validateInput');
        try {
            if (!text || typeof text !== 'string') {
                throw new ExtensionError_1.ValidationError('Invalid input: text must be a non-empty string');
            }
            const warnings = [];
            const sizeCheck = this.checkInputSize(text);
            const hasDoubleQuotes = this.hasUnescapedDoubleQuotes(text);
            const breakdown = this.suggestTaskBreakdown(text);
            if (sizeCheck.isLarge) {
                warnings.push(sizeCheck.suggestion || 'Input size exceeds recommended limit');
            }
            if (hasDoubleQuotes) {
                warnings.push('Contains unescaped double quotes that may cause errors');
            }
            if (breakdown) {
                warnings.push('Complex task detected - consider breaking down');
            }
            const result = {
                isValid: warnings.length === 0,
                isLarge: sizeCheck.isLarge,
                hasDoubleQuotes,
                needsBreakdown: breakdown !== null,
                suggestion: breakdown || sizeCheck.suggestion,
                warnings
            };
            this.log.debug('Input validation result', result);
            return result;
        }
        catch (error) {
            this.log.error('Validation failed', error);
            throw error;
        }
        finally {
            endTimer();
        }
    }
    /**
     * Fix double quotes by escaping them
     */
    fixDoubleQuotes(text) {
        if (!text) {
            return text;
        }
        // Escape unescaped double quotes
        // Negative lookbehind to avoid escaping already escaped quotes
        return text.replace(/(?<!\\)"/g, '\\"');
    }
    /**
     * Check if text has unescaped double quotes
     */
    hasUnescapedDoubleQuotes(text) {
        return /(?<!\\)"/.test(text);
    }
    /**
     * Check input size and provide suggestions
     */
    checkInputSize(text) {
        const size = text.length;
        const maxSize = constants_1.VALIDATION_LIMITS.MAX_SAFE_INPUT_SIZE;
        if (size > maxSize) {
            const ratio = Math.ceil(size / maxSize);
            return {
                isLarge: true,
                suggestion: `Input is ${size} characters (recommended max: ${maxSize}). ` +
                    `Consider breaking this into ${ratio} smaller tasks to avoid ` +
                    `"too large input" errors and credit consumption.`
            };
        }
        return { isLarge: false };
    }
    /**
     * Suggest task breakdown for complex prompts
     */
    suggestTaskBreakdown(text) {
        // Check for complexity indicators
        const hasComplexity = constants_1.COMPLEXITY_INDICATORS.some(pattern => pattern.test(text));
        if (hasComplexity && text.length > constants_1.VALIDATION_LIMITS.COMPLEXITY_THRESHOLD) {
            return this.generateBreakdownSuggestion(text);
        }
        return null;
    }
    /**
     * Generate breakdown suggestion based on text analysis
     */
    generateBreakdownSuggestion(text) {
        const suggestions = [
            'This looks like a complex task. Consider breaking it down:',
            '',
            '1. Start with the main structure or skeleton',
            '2. Implement core functionality first',
            '3. Add features incrementally',
            '4. Test and refine each component',
            '5. Use "continue from where you left off" for incomplete responses',
            '',
            'Benefits:',
            '- Prevents "too large input" errors',
            '- Reduces credit loss from failed operations',
            '- Allows for better quality control',
            '- Easier to debug and iterate'
        ];
        // Analyze text for specific patterns
        if (/documentation|docs/i.test(text)) {
            suggestions.push('', 'For documentation: Start with outline, then fill sections one by one');
        }
        if (/refactor|migrate/i.test(text)) {
            suggestions.push('', 'For refactoring: Tackle one module/file at a time');
        }
        if (/test|testing/i.test(text)) {
            suggestions.push('', 'For testing: Write tests for one component/function at a time');
        }
        return suggestions.join('\n');
    }
    /**
     * Validate and sanitize file path
     */
    validateFilePath(filePath) {
        if (!filePath || typeof filePath !== 'string') {
            return false;
        }
        // Check for path traversal attempts
        if (filePath.includes('..') || filePath.includes('~')) {
            this.log.warn('Potential path traversal detected', { filePath });
            return false;
        }
        return true;
    }
    /**
     * Sanitize text for safe display
     */
    sanitizeText(text) {
        if (!text) {
            return '';
        }
        return text
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#x27;')
            .replace(/\//g, '&#x2F;');
    }
    /**
     * Validate webview message
     */
    validateWebviewMessage(message) {
        if (!message || typeof message !== 'object') {
            return false;
        }
        if (!message.command || typeof message.command !== 'string') {
            return false;
        }
        // Whitelist of allowed commands
        const allowedCommands = [
            'refreshDashboard',
            'checkContextHealth',
            'refreshContext',
            'validateFileContext',
            'optimizePrompt',
            'fixDoubleQuotes',
            'checkInputSize',
            'suggestBreakdown',
            'openSettings',
            'openDashboard',
            'closeWelcome'
        ];
        return allowedCommands.includes(message.command);
    }
}
exports.ValidationService = ValidationService;
//# sourceMappingURL=ValidationService.js.map