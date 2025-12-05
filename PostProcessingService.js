"use strict";
// PostProcessingService.ts - Main service for text post-processing coordination
Object.defineProperty(exports, "__esModule", { value: true });
exports.PostProcessingService = void 0;
const OpenAIPostProcessor_1 = require("./OpenAIPostProcessor");
const GlobalOutput_1 = require("../utils/GlobalOutput");
/**
 * Main service for coordinating text post-processing
 * Handles configuration validation, processing decisions, and integration with OpenAI
 */
class PostProcessingService {
    processor = null;
    configurationManager;
    constructor(configurationManager) {
        this.configurationManager = configurationManager;
    }
    /**
     * Process text based on current configuration
     */
    async processText(text) {
        const startTime = Date.now();
        const config = this.configurationManager.getPostProcessingConfiguration();
        try {
            GlobalOutput_1.ExtensionLog.info(`🧠 [POST-PROCESSING] Starting text processing`, {
                textLength: text.length,
                model: config.model,
                minTextLength: config.minTextLength
            });
            // Check if processing should occur
            if (!this.shouldProcess(text, config)) {
                GlobalOutput_1.ExtensionLog.info(`🧠 [POST-PROCESSING] Skipping processing (model: ${config.model}, length: ${text.length})`);
                return {
                    originalText: text,
                    processedText: text,
                    wasProcessed: false
                };
            }
            // Validate configuration before processing
            const validation = this.validateConfiguration();
            if (!validation.isValid) {
                GlobalOutput_1.ExtensionLog.error(`🧠 [POST-PROCESSING] Configuration invalid:`, validation.errors);
                return {
                    originalText: text,
                    processedText: text,
                    wasProcessed: false
                };
            }
            // Ensure processor is initialized
            await this.ensureProcessor();
            if (!this.processor) {
                GlobalOutput_1.ExtensionLog.error(`🧠 [POST-PROCESSING] Processor not available`);
                return {
                    originalText: text,
                    processedText: text,
                    wasProcessed: false
                };
            }
            // Process the text
            const options = {
                model: config.model,
                prompt: config.prompt,
                temperature: 0.1, // Low temperature for consistency
                maxTokens: Math.min(4000, Math.ceil(text.length * 2)) // Reasonable limit based on input
            };
            const processedText = await this.processor.processText(text, options);
            const processingTime = Date.now() - startTime;
            GlobalOutput_1.ExtensionLog.info(`🧠 [POST-PROCESSING] Processing completed`, {
                originalLength: text.length,
                processedLength: processedText.length,
                processingTime: processingTime,
                wasActuallyProcessed: processedText !== text
            });
            return {
                originalText: text,
                processedText: processedText,
                wasProcessed: processedText !== text, // True only if text was actually changed
                model: config.model,
                processingTime: processingTime
            };
        }
        catch (error) {
            const processingTime = Date.now() - startTime;
            GlobalOutput_1.ExtensionLog.error(`🧠 [POST-PROCESSING] Error during processing:`, undefined, error);
            // Always return original text on error (fallback)
            return {
                originalText: text,
                processedText: text,
                wasProcessed: false,
                processingTime: processingTime
            };
        }
    }
    /**
     * Check if text should be processed based on configuration
     */
    shouldProcess(text, config) {
        const postConfig = config || this.configurationManager.getPostProcessingConfiguration();
        // Skip if model is set to "Without post-processing"
        if (postConfig.model === 'Without post-processing') {
            return false;
        }
        // Skip if text is empty or too short
        if (!text || text.trim().length === 0) {
            return false;
        }
        // Check minimum text length
        if (text.length < postConfig.minTextLength) {
            GlobalOutput_1.ExtensionLog.info(`🧠 [POST-PROCESSING] Text too short (${text.length} < ${postConfig.minTextLength})`);
            return false;
        }
        return true;
    }
    /**
     * Validate current configuration for post-processing
     */
    validateConfiguration() {
        const config = this.configurationManager.getPostProcessingConfiguration();
        const whisperConfig = this.configurationManager.getWhisperConfiguration();
        const errors = [];
        const warnings = [];
        // Check if API key is available
        if (!whisperConfig.apiKey || whisperConfig.apiKey.trim() === '') {
            errors.push('OpenAI API key is required for post-processing');
        }
        // Validate model selection (актуальные модели на 2025 год)
        const validModels = [
            'Without post-processing',
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
        if (!validModels.includes(config.model)) {
            errors.push(`Invalid model selection: ${config.model}`);
        }
        // Validate timeout
        if (config.timeout <= 0) {
            errors.push('Timeout must be greater than 0');
        }
        // Validate minimum text length
        if (config.minTextLength < 0) {
            errors.push('Minimum text length cannot be negative');
        }
        // Check if prompt is empty (warning, not error)
        if (!config.prompt || config.prompt.trim().length === 0) {
            warnings.push('Post-processing prompt is empty, using default');
        }
        // Check for very long timeout (warning)
        if (config.timeout > 60000) {
            warnings.push('Timeout is very long (>60s), may affect user experience');
        }
        return {
            isValid: errors.length === 0,
            errors,
            warnings
        };
    }
    /**
     * Get current configuration status
     */
    getConfigurationStatus() {
        const config = this.configurationManager.getPostProcessingConfiguration();
        const validation = this.validateConfiguration();
        return {
            isEnabled: config.model !== 'Without post-processing',
            model: config.model,
            minTextLength: config.minTextLength,
            isConfigValid: validation.isValid,
            validationResult: validation
        };
    }
    /**
     * Check if post-processing is currently enabled
     */
    isEnabled() {
        const config = this.configurationManager.getPostProcessingConfiguration();
        return config.model !== 'Without post-processing';
    }
    /**
     * Reset processor instance (useful for configuration changes)
     */
    resetProcessor() {
        this.processor = null;
        GlobalOutput_1.ExtensionLog.info(`🧠 [POST-PROCESSING] Processor reset`);
    }
    /**
     * Ensure processor is initialized with current configuration
     */
    async ensureProcessor() {
        if (this.processor) {
            return; // Already initialized
        }
        const whisperConfig = this.configurationManager.getWhisperConfiguration();
        const postConfig = this.configurationManager.getPostProcessingConfiguration();
        if (!whisperConfig.apiKey) {
            throw new Error('OpenAI API key is required for post-processing');
        }
        try {
            this.processor = new OpenAIPostProcessor_1.OpenAIPostProcessor({
                apiKey: whisperConfig.apiKey,
                timeout: postConfig.timeout,
                maxRetries: 3, // Fixed retry count
                retryDelay: 1000 // 1 second
            });
            // Validate the API key
            const isValidKey = await this.processor.checkApiKey();
            if (!isValidKey) {
                GlobalOutput_1.ExtensionLog.warn(`🧠 [POST-PROCESSING] API key validation failed`);
                this.processor = null;
                throw new Error('Invalid OpenAI API key');
            }
            GlobalOutput_1.ExtensionLog.info(`🧠 [POST-PROCESSING] Processor initialized successfully`);
        }
        catch (error) {
            GlobalOutput_1.ExtensionLog.error(`🧠 [POST-PROCESSING] Failed to initialize processor:`, undefined, error);
            this.processor = null;
            throw error;
        }
    }
    /**
     * Dispose of resources
     */
    dispose() {
        this.processor = null;
        GlobalOutput_1.ExtensionLog.info(`🧠 [POST-PROCESSING] Service disposed`);
    }
}
exports.PostProcessingService = PostProcessingService;
//# sourceMappingURL=PostProcessingService.js.map