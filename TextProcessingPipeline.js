"use strict";
// TextProcessingPipeline.ts - Coordinator for the complete text processing workflow
Object.defineProperty(exports, "__esModule", { value: true });
exports.TextProcessingPipeline = void 0;
const GlobalOutput_1 = require("../utils/GlobalOutput");
/**
 * Coordinates the complete text processing workflow:
 * Audio Blob → Whisper Transcription → Post-processing → Text Insertion
 */
class TextProcessingPipeline {
    whisperClient;
    postProcessingService;
    textInserter;
    configurationManager;
    constructor(whisperClient, postProcessingService, textInserter, configurationManager) {
        this.whisperClient = whisperClient;
        this.postProcessingService = postProcessingService;
        this.textInserter = textInserter;
        this.configurationManager = configurationManager;
    }
    /**
     * Execute the complete processing pipeline
     */
    async processAudio(audioBlob, insertionMode = 'cursor', progressCallback) {
        const startTime = Date.now();
        const steps = [];
        GlobalOutput_1.ExtensionLog.info(`🔄 [PIPELINE] Starting audio processing pipeline`, {
            audioBlobSize: audioBlob.size,
            insertionMode: insertionMode
        });
        try {
            // Step 1: Whisper Transcription
            const transcriptionStep = this.createStep('Whisper Transcription');
            steps.push(transcriptionStep);
            this.updateProgress(progressCallback, 'Transcribing audio...', 0, 3);
            const transcriptionResult = await this.executeTranscription(audioBlob, transcriptionStep);
            if (!transcriptionResult) {
                return this.createFailureResult(audioBlob, steps, startTime, insertionMode, new Error('Transcription failed'));
            }
            // Step 2: Post-processing (conditional)
            const postProcessingStep = this.createStep('Post-processing');
            steps.push(postProcessingStep);
            this.updateProgress(progressCallback, 'Improving text quality...', 1, 3);
            const postProcessingResult = await this.executePostProcessing(transcriptionResult, postProcessingStep);
            const finalText = postProcessingResult.processedText;
            // Step 3: Text Insertion
            const insertionStep = this.createStep('Text Insertion');
            steps.push(insertionStep);
            this.updateProgress(progressCallback, 'Inserting text...', 2, 3);
            await this.executeTextInsertion(finalText, insertionMode, insertionStep);
            const totalTime = Date.now() - startTime;
            GlobalOutput_1.ExtensionLog.info(`🔄 [PIPELINE] Processing completed successfully`, {
                totalTime: totalTime,
                originalLength: transcriptionResult.length,
                finalLength: finalText.length,
                wasPostProcessed: postProcessingResult.wasProcessed,
                insertionMode: insertionMode
            });
            return {
                success: true,
                originalAudioBlob: audioBlob,
                transcriptionResult: transcriptionResult,
                postProcessingResult: postProcessingResult,
                finalText: finalText,
                steps: steps,
                totalProcessingTime: totalTime,
                insertionMode: insertionMode
            };
        }
        catch (error) {
            GlobalOutput_1.ExtensionLog.error(`🔄 [PIPELINE] Processing failed:`, undefined, error);
            return this.createFailureResult(audioBlob, steps, startTime, insertionMode, error);
        }
    }
    /**
     * Execute Whisper transcription step
     */
    async executeTranscription(audioBlob, step) {
        step.status = 'in-progress';
        step.startTime = Date.now();
        try {
            // Check if whisperClient is initialized
            if (!this.whisperClient) {
                throw new Error('WhisperClient not initialized. Please check your OpenAI API key configuration.');
            }
            const whisperConfig = this.configurationManager.getWhisperConfiguration();
            const options = {
                language: whisperConfig.language === 'auto' ? undefined : whisperConfig.language,
                model: whisperConfig.whisperModel,
                prompt: whisperConfig.prompt,
                temperature: whisperConfig.temperature,
                response_format: 'text'
            };
            const result = await this.whisperClient.transcribe(audioBlob, options);
            step.status = 'completed';
            step.endTime = Date.now();
            step.result = { text: result, length: result.length };
            GlobalOutput_1.ExtensionLog.info(`🔄 [PIPELINE] Transcription completed:`, {
                textLength: result.length,
                processingTime: step.endTime - (step.startTime || 0)
            });
            return result;
        }
        catch (error) {
            step.status = 'failed';
            step.endTime = Date.now();
            step.error = error;
            GlobalOutput_1.ExtensionLog.error(`🔄 [PIPELINE] Transcription failed:`, undefined, error);
            throw error;
        }
    }
    /**
     * Execute post-processing step
     */
    async executePostProcessing(text, step) {
        step.status = 'in-progress';
        step.startTime = Date.now();
        try {
            // Check if post-processing should be applied
            if (!this.postProcessingService.shouldProcess(text)) {
                step.status = 'skipped';
                step.endTime = Date.now();
                GlobalOutput_1.ExtensionLog.info(`🔄 [PIPELINE] Post-processing skipped`);
                return {
                    originalText: text,
                    processedText: text,
                    wasProcessed: false
                };
            }
            const result = await this.postProcessingService.processText(text);
            step.status = 'completed';
            step.endTime = Date.now();
            step.result = {
                wasProcessed: result.wasProcessed,
                originalLength: result.originalText.length,
                processedLength: result.processedText.length,
                model: result.model,
                processingTime: result.processingTime
            };
            GlobalOutput_1.ExtensionLog.info(`🔄 [PIPELINE] Post-processing completed:`, {
                wasProcessed: result.wasProcessed,
                processingTime: step.endTime - (step.startTime || 0)
            });
            return result;
        }
        catch (error) {
            step.status = 'failed';
            step.endTime = Date.now();
            step.error = error;
            GlobalOutput_1.ExtensionLog.error(`🔄 [PIPELINE] Post-processing failed, using original text:`, undefined, error);
            // Fallback to original text on error
            return {
                originalText: text,
                processedText: text,
                wasProcessed: false
            };
        }
    }
    /**
     * Execute text insertion step
     */
    async executeTextInsertion(text, mode, step) {
        step.status = 'in-progress';
        step.startTime = Date.now();
        try {
            if (mode === 'cursor') {
                await this.textInserter.insertAtCursor(text);
            }
            else {
                await this.textInserter.copyToClipboard(text);
            }
            step.status = 'completed';
            step.endTime = Date.now();
            step.result = { mode: mode, textLength: text.length };
            GlobalOutput_1.ExtensionLog.info(`🔄 [PIPELINE] Text insertion completed:`, {
                mode: mode,
                textLength: text.length,
                processingTime: step.endTime - (step.startTime || 0)
            });
        }
        catch (error) {
            step.status = 'failed';
            step.endTime = Date.now();
            step.error = error;
            GlobalOutput_1.ExtensionLog.error(`🔄 [PIPELINE] Text insertion failed:`, undefined, error);
            throw error;
        }
    }
    /**
     * Create a new processing step
     */
    createStep(name) {
        return {
            name: name,
            status: 'pending'
        };
    }
    /**
     * Update progress callback if provided
     */
    updateProgress(callback, message, stepIndex, totalSteps) {
        if (callback) {
            callback({
                currentStep: message,
                stepIndex: stepIndex,
                totalSteps: totalSteps,
                message: message
            });
        }
    }
    /**
     * Create a failure result
     */
    createFailureResult(audioBlob, steps, startTime, insertionMode, error) {
        const totalTime = Date.now() - startTime;
        return {
            success: false,
            originalAudioBlob: audioBlob,
            finalText: '',
            steps: steps,
            totalProcessingTime: totalTime,
            insertionMode: insertionMode,
            error: error
        };
    }
    /**
     * Get pipeline configuration status
     */
    getConfigurationStatus() {
        const whisperConfig = this.configurationManager.getWhisperConfiguration();
        const postProcessingStatus = this.postProcessingService.getConfigurationStatus();
        return {
            whisperConfigured: !!whisperConfig.apiKey,
            postProcessingEnabled: postProcessingStatus.isEnabled,
            postProcessingConfigured: postProcessingStatus.isConfigValid
        };
    }
    /**
     * Validate pipeline configuration
     */
    validateConfiguration() {
        const errors = [];
        // Validate Whisper configuration
        const whisperConfig = this.configurationManager.getWhisperConfiguration();
        if (!whisperConfig.apiKey) {
            errors.push('OpenAI API key is required');
        }
        // Validate post-processing configuration if enabled
        const postProcessingStatus = this.postProcessingService.getConfigurationStatus();
        if (postProcessingStatus.isEnabled && !postProcessingStatus.isConfigValid) {
            errors.push(...postProcessingStatus.validationResult.errors);
        }
        return {
            isValid: errors.length === 0,
            errors: errors
        };
    }
    /**
     * Reset all services (useful for configuration changes)
     */
    reset() {
        this.postProcessingService.resetProcessor();
        GlobalOutput_1.ExtensionLog.info(`🔄 [PIPELINE] Pipeline reset`);
    }
    /**
     * Dispose of resources
     */
    dispose() {
        this.postProcessingService.dispose();
        GlobalOutput_1.ExtensionLog.info(`🔄 [PIPELINE] Pipeline disposed`);
    }
}
exports.TextProcessingPipeline = TextProcessingPipeline;
//# sourceMappingURL=TextProcessingPipeline.js.map