"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.RetryManager = exports.RetryStrategy = void 0;
exports.withRetry = withRetry;
const ErrorHandler_1 = require("./ErrorHandler");
const GlobalOutput_1 = require("./GlobalOutput");
/**
 * Retry strategies
 */
var RetryStrategy;
(function (RetryStrategy) {
    RetryStrategy["EXPONENTIAL_BACKOFF"] = "exponential_backoff";
    RetryStrategy["LINEAR_BACKOFF"] = "linear_backoff";
    RetryStrategy["FIXED_DELAY"] = "fixed_delay";
    RetryStrategy["IMMEDIATE"] = "immediate";
})(RetryStrategy || (exports.RetryStrategy = RetryStrategy = {}));
/**
 * Retry manager
 */
class RetryManager {
    defaultConfig = {
        maxAttempts: 3,
        strategy: RetryStrategy.EXPONENTIAL_BACKOFF,
        baseDelay: 1000,
        maxDelay: 10000,
        multiplier: 2,
        jitter: true
    };
    errorHandler;
    constructor(errorHandler) {
        this.errorHandler = errorHandler;
    }
    /**
     * Execution of the operation with retries
     */
    async retry(operation, operationName, config, errorContext) {
        const finalConfig = { ...this.defaultConfig, ...config };
        const startTime = Date.now();
        let lastError;
        for (let attempt = 1; attempt <= finalConfig.maxAttempts; attempt++) {
            try {
                GlobalOutput_1.RetryManagerLog.info(`🔄 Attempting ${operationName} (${attempt}/${finalConfig.maxAttempts})`);
                const result = await operation();
                const totalTime = Date.now() - startTime;
                GlobalOutput_1.RetryManagerLog.info(`✅ ${operationName} succeeded on attempt ${attempt} (${totalTime}ms)`);
                return {
                    success: true,
                    result,
                    attempts: attempt,
                    totalTime
                };
            }
            catch (error) {
                // Correctly handle non-Error objects
                lastError = error instanceof Error
                    ? error
                    : new Error(String(error));
                GlobalOutput_1.RetryManagerLog.warn(`❌ ${operationName} failed on attempt ${attempt}: ${lastError.message}`);
                // If this is the last attempt, do not make a delay
                if (attempt === finalConfig.maxAttempts) {
                    break;
                }
                // Check if we can retry this error
                const errorType = this.classifyError(lastError);
                if (!this.errorHandler.isRetryable(errorType)) {
                    GlobalOutput_1.RetryManagerLog.warn(`🚫 Error type ${errorType} is not retryable, stopping attempts`);
                    break;
                }
                // Calculate the delay and wait
                const delay = this.calculateDelay(attempt, finalConfig);
                GlobalOutput_1.RetryManagerLog.info(`⏳ Waiting ${delay}ms before next attempt...`);
                await this.sleep(delay);
            }
        }
        const totalTime = Date.now() - startTime;
        GlobalOutput_1.RetryManagerLog.error(`💥 ${operationName} failed after ${finalConfig.maxAttempts} attempts (${totalTime}ms)`);
        return {
            success: false,
            lastError,
            attempts: finalConfig.maxAttempts,
            totalTime
        };
    }
    /**
     * Retry specifically for API requests with network error detection
     */
    async retryApiRequest(operation, operationName, config) {
        const apiConfig = {
            maxAttempts: 3,
            strategy: RetryStrategy.EXPONENTIAL_BACKOFF,
            baseDelay: 1000,
            maxDelay: 8000,
            multiplier: 2,
            jitter: true,
            ...config
        };
        return await this.retry(operation, operationName, apiConfig, {
            type: 'api_request'
        });
    }
    /**
     * Retry for microphone operations
     */
    async retryMicrophoneOperation(operation, operationName, config) {
        const micConfig = {
            maxAttempts: 2,
            strategy: RetryStrategy.FIXED_DELAY,
            baseDelay: 500,
            maxDelay: 1000,
            multiplier: 1,
            jitter: false,
            ...config
        };
        return await this.retry(operation, operationName, micConfig, {
            type: 'microphone_operation'
        });
    }
    /**
     * Error classification (simplified version)
     */
    classifyError(error) {
        const message = error.message.toLowerCase();
        if (message.includes('network') || message.includes('timeout') ||
            message.includes('fetch') || message.includes('connection')) {
            return ErrorHandler_1.ErrorType.NETWORK_ERROR;
        }
        if (message.includes('rate limit')) {
            return ErrorHandler_1.ErrorType.API_RATE_LIMIT;
        }
        if (message.includes('api key')) {
            return ErrorHandler_1.ErrorType.API_KEY_INVALID;
        }
        if (message.includes('microphone') || message.includes('permission')) {
            return ErrorHandler_1.ErrorType.MICROPHONE_ACCESS;
        }
        return ErrorHandler_1.ErrorType.UNKNOWN_ERROR;
    }
    /**
     * Calculating the delay based on the strategy
     */
    calculateDelay(attempt, config) {
        let delay;
        switch (config.strategy) {
            case RetryStrategy.EXPONENTIAL_BACKOFF:
                delay = Math.min(config.baseDelay * Math.pow(config.multiplier, attempt - 1), config.maxDelay);
                break;
            case RetryStrategy.LINEAR_BACKOFF:
                delay = Math.min(config.baseDelay * attempt, config.maxDelay);
                break;
            case RetryStrategy.FIXED_DELAY:
                delay = config.baseDelay;
                break;
            case RetryStrategy.IMMEDIATE:
                delay = 0;
                break;
            default:
                delay = config.baseDelay;
        }
        // Add jitter if enabled
        if (config.jitter) {
            const jitterAmount = delay * 0.1; // 10% of the delay
            const randomJitter = (Math.random() - 0.5) * 2 * jitterAmount;
            delay = Math.max(0, delay + randomJitter);
        }
        return Math.round(delay);
    }
    /**
     * Utility for waiting
     */
    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    /**
     * Creating a pre-configured RetryManager for different types of operations
     */
    static createForApiOperations(errorHandler) {
        const manager = new RetryManager(errorHandler);
        return manager;
    }
    static createForMicrophoneOperations(errorHandler) {
        const manager = new RetryManager(errorHandler);
        return manager;
    }
}
exports.RetryManager = RetryManager;
/**
 * Decorator for automatic retry
 */
function withRetry(retryManager, operationName, config) {
    return function (target, propertyKey, descriptor) {
        const originalMethod = descriptor.value;
        descriptor.value = async function (...args) {
            const result = await retryManager.retry(() => originalMethod.apply(this, args), `${target.constructor.name}.${operationName}`, config);
            if (result.success) {
                return result.result;
            }
            else {
                throw result.lastError || new Error(`${operationName} failed after retries`);
            }
        };
        return descriptor;
    };
}
//# sourceMappingURL=RetryManager.js.map