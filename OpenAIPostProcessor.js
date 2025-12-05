"use strict";
// OpenAIPostProcessor.ts - HTTP client for text post-processing using OpenAI GPT API
Object.defineProperty(exports, "__esModule", { value: true });
exports.OpenAIPostProcessor = void 0;
const GlobalOutput_1 = require("../utils/GlobalOutput");
/**
 * HTTP client for post-processing text using OpenAI GPT API
 */
class OpenAIPostProcessor {
    apiKey;
    baseURL;
    timeout;
    maxRetries;
    retryDelay;
    // Supported models for post-processing (актуальные модели на 2025 год)
    supportedModels = [
        // GPT-4.1 series (April 2025) - Новейшие модели
        'gpt-4.1',
        'gpt-4.1-mini',
        'gpt-4.1-nano',
        // GPT-4o series
        'gpt-4o',
        'gpt-4o-mini',
        'gpt-4o-2024-11-20',
        'gpt-4o-2024-08-06',
        'gpt-4o-2024-05-13',
        // GPT-4.5 series
        'gpt-4.5-preview',
        // GPT-4 Turbo
        'gpt-4-turbo',
        'gpt-4-turbo-2024-04-09',
        // o-series models
        'o1',
        'o1-preview',
        'o1-mini',
        'o3',
        'o3-mini',
        'o4-mini',
        // Legacy models
        'gpt-3.5-turbo',
        'gpt-3.5-turbo-0125',
        'gpt-3.5-turbo-1106',
        // Special models
        'chatgpt-4o-latest'
    ];
    constructor(config) {
        this.apiKey = config.apiKey;
        this.baseURL = config.baseURL || 'https://api.openai.com/v1';
        this.timeout = config.timeout || 30000; // 30 seconds
        this.maxRetries = config.maxRetries || 3;
        this.retryDelay = config.retryDelay || 1000; // 1 second
    }
    /**
     * Process text to improve quality
     */
    async processText(text, options = {}) {
        // Validate input
        this.validateText(text);
        const model = options.model || 'gpt-4o-mini';
        this.validateModel(model);
        // Log the request parameters
        this.logRequestParameters(text, options);
        // Prepare the request payload
        const requestBody = this.prepareRequestBody(text, options);
        for (let attempt = 1; attempt <= this.maxRetries; attempt++) {
            try {
                const response = await this.makeRequest('/chat/completions', requestBody);
                return this.processResponse(response, text);
            }
            catch (error) {
                GlobalOutput_1.ExtensionLog.error(`🤖 [POST-PROCESSOR] Attempt ${attempt} failed:`, undefined, error);
                const isRetryable = this.isRetryableError(error);
                const enhancedError = this.enhanceError(error);
                if (attempt === this.maxRetries || !isRetryable) {
                    // Fallback: return original text on any error
                    GlobalOutput_1.ExtensionLog.warn(`🤖 [POST-PROCESSOR] All attempts failed, returning original text`);
                    return text;
                }
                // Wait before the next attempt
                await this.delay(this.retryDelay * attempt);
            }
        }
        // Final fallback (should not reach here, but just in case)
        GlobalOutput_1.ExtensionLog.warn(`🤖 [POST-PROCESSOR] Exhausted all retries, returning original text`);
        return text;
    }
    /**
     * Check if API key is valid
     */
    async checkApiKey() {
        try {
            const response = await fetch(`${this.baseURL}/models`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${this.apiKey}`,
                    'User-Agent': 'SpeechToTextWhisper-Extension/1.0'
                },
                signal: AbortSignal.timeout(this.timeout)
            });
            return response.ok;
        }
        catch {
            return false;
        }
    }
    /**
     * Validate input text
     */
    validateText(text) {
        if (!text || text.trim().length === 0) {
            throw this.createError('Input text is empty', 'EMPTY_TEXT');
        }
        // OpenAI has a context limit, but we'll let the API handle that
        if (text.length > 100000) { // 100k characters as a reasonable limit
            throw this.createError('Text is too long for processing', 'TEXT_TOO_LONG');
        }
    }
    /**
     * Validate model selection
     */
    validateModel(model) {
        if (!this.supportedModels.includes(model)) {
            throw this.createError(`Unsupported model: ${model}`, 'UNSUPPORTED_MODEL');
        }
    }
    /**
     * Prepare request body for OpenAI API
     */
    prepareRequestBody(text, options) {
        const model = options.model || 'gpt-4o-mini';
        const temperature = options.temperature ?? 0.1; // Low temperature for consistency
        const maxTokens = options.maxTokens || 4000; // Reasonable limit
        // Build the system prompt
        const systemPrompt = options.prompt || this.getDefaultPrompt();
        return {
            model: model,
            messages: [
                {
                    role: 'system',
                    content: systemPrompt
                },
                {
                    role: 'user',
                    content: text
                }
            ],
            temperature: temperature,
            max_tokens: maxTokens,
            stream: false
        };
    }
    /**
     * Get default prompt for text improvement
     */
    getDefaultPrompt() {
        return `Please improve this transcribed text by:
1. Adding proper punctuation and capitalization
2. Removing filler words (um, uh, like, you know)
3. Structuring sentences for better readability
4. Maintaining the original meaning and technical terms

Return only the improved text without any additional comments or explanations.`;
    }
    /**
     * Log request parameters
     */
    logRequestParameters(text, options) {
        const requestInfo = {
            endpoint: `${this.baseURL}/chat/completions`,
            method: 'POST',
            parameters: {
                model: options.model || 'gpt-4o-mini',
                temperature: options.temperature ?? 0.1,
                maxTokens: options.maxTokens || 4000,
                promptLength: (options.prompt || this.getDefaultPrompt()).length
            },
            inputText: {
                length: text.length,
                preview: text.substring(0, 100) + (text.length > 100 ? '...' : '')
            }
        };
        GlobalOutput_1.ExtensionLog.info(`🤖 [POST-PROCESSOR] Starting text processing:`, requestInfo);
    }
    /**
     * Make HTTP request to OpenAI API
     */
    async makeRequest(endpoint, requestBody) {
        const url = `${this.baseURL}${endpoint}`;
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.apiKey}`,
                'User-Agent': 'SpeechToTextWhisper-Extension/1.0'
            },
            body: JSON.stringify(requestBody),
            signal: AbortSignal.timeout(this.timeout)
        });
        if (!response.ok) {
            const errorData = await this.parseErrorResponse(response);
            throw this.createApiError(response.status, response.statusText, errorData);
        }
        return response;
    }
    /**
     * Process API response
     */
    async processResponse(response, originalText) {
        try {
            const result = await response.json();
            if (!result.choices || result.choices.length === 0) {
                throw this.createError('No choices in API response', 'NO_CHOICES');
            }
            const processedText = result.choices[0].message?.content?.trim();
            if (!processedText) {
                GlobalOutput_1.ExtensionLog.warn(`🤖 [POST-PROCESSOR] Empty response, returning original text`);
                return originalText;
            }
            GlobalOutput_1.ExtensionLog.info(`🤖 [POST-PROCESSOR] Text processed successfully:`, {
                originalLength: originalText.length,
                processedLength: processedText.length,
                tokensUsed: result.usage?.total_tokens || 'unknown'
            });
            return processedText;
        }
        catch (error) {
            GlobalOutput_1.ExtensionLog.error(`🤖 [POST-PROCESSOR] Error processing response:`, undefined, error);
            throw this.enhanceError(error);
        }
    }
    /**
     * Parse error response from API
     */
    async parseErrorResponse(response) {
        try {
            return await response.json();
        }
        catch {
            return { error: { message: response.statusText } };
        }
    }
    /**
     * Create API error with detailed information
     */
    createApiError(status, statusText, errorData) {
        let message = `OpenAI API Error: ${status} ${statusText}`;
        let code = `HTTP_${status}`;
        if (errorData?.error?.message) {
            message = errorData.error.message;
        }
        if (errorData?.error?.code) {
            code = errorData.error.code;
        }
        // Handle specific error cases
        switch (status) {
            case 401:
                message = 'Invalid API key for OpenAI';
                code = 'INVALID_API_KEY';
                break;
            case 429:
                message = 'Rate limit exceeded for OpenAI API';
                code = 'RATE_LIMIT_EXCEEDED';
                break;
            case 500:
                message = 'OpenAI server error';
                code = 'SERVER_ERROR';
                break;
        }
        return this.createError(message, code, status, errorData);
    }
    /**
     * Create enhanced error object
     */
    createError(message, code, statusCode, details) {
        const error = new Error(message);
        error.name = 'PostProcessingError';
        if (code)
            error.code = code;
        if (statusCode)
            error.statusCode = statusCode;
        if (details)
            error.details = details;
        return error;
    }
    /**
     * Enhance generic error with additional context
     */
    enhanceError(error) {
        if (error.name === 'PostProcessingError') {
            return error;
        }
        const enhanced = this.createError(error.message);
        enhanced.stack = error.stack;
        // Handle specific error types
        if (error.name === 'AbortError') {
            enhanced.code = 'TIMEOUT';
            enhanced.message = 'Post-processing request timed out';
        }
        else if (error.name === 'TypeError' && error.message.includes('fetch')) {
            enhanced.code = 'NETWORK_ERROR';
            enhanced.message = 'Network error during post-processing';
        }
        return enhanced;
    }
    /**
     * Check if error is retryable
     */
    isRetryableError(error) {
        // Network errors and timeouts are retryable
        if (error.name === 'AbortError' || error.name === 'TypeError') {
            return true;
        }
        // HTTP errors
        if (error.statusCode) {
            // Retry on server errors and rate limits
            return error.statusCode >= 500 || error.statusCode === 429;
        }
        // Default to retryable for unknown errors
        return true;
    }
    /**
     * Delay utility for retries
     */
    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    /**
     * Static method to validate API key format
     */
    static validateApiKey(apiKey) {
        return typeof apiKey === 'string' &&
            apiKey.length > 0 &&
            apiKey.startsWith('sk-');
    }
    /**
     * Get supported models (актуальные модели на 2025 год)
     */
    static getSupportedModels() {
        return [
            // GPT-4.1 series (April 2025) - Новейшие модели
            'gpt-4.1',
            'gpt-4.1-mini',
            'gpt-4.1-nano',
            // GPT-4o series
            'gpt-4o',
            'gpt-4o-mini',
            'gpt-4o-2024-11-20',
            'gpt-4o-2024-08-06',
            'gpt-4o-2024-05-13',
            // GPT-4.5 series
            'gpt-4.5-preview',
            // GPT-4 Turbo
            'gpt-4-turbo',
            'gpt-4-turbo-2024-04-09',
            // o-series models
            'o1',
            'o1-preview',
            'o1-mini',
            'o3',
            'o3-mini',
            'o4-mini',
            // Legacy models
            'gpt-3.5-turbo',
            'gpt-3.5-turbo-0125',
            'gpt-3.5-turbo-1106',
            // Special models
            'chatgpt-4o-latest'
        ];
    }
}
exports.OpenAIPostProcessor = OpenAIPostProcessor;
//# sourceMappingURL=OpenAIPostProcessor.js.map