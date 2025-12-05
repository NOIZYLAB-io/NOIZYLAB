"use strict";
// AudioRecorder.ts - module for recording audio through Web Audio API
Object.defineProperty(exports, "__esModule", { value: true });
exports.AudioRecorder = void 0;
class AudioRecorder {
    events;
    options;
    mediaRecorder = null;
    audioChunks = [];
    stream = null;
    isRecording = false;
    recordingStartTime = 0;
    maxDurationTimer = null;
    supportedMimeTypes = [];
    constructor(events, options = {}) {
        this.events = events;
        this.options = options;
        this.detectSupportedFormats();
    }
    /**
     * Determines supported audio formats
     */
    detectSupportedFormats() {
        const formats = [
            'audio/webm;codecs=opus',
            'audio/webm',
            'audio/mp4',
            'audio/wav',
            'audio/ogg;codecs=opus',
            'audio/ogg'
        ];
        this.supportedMimeTypes = formats.filter(format => MediaRecorder.isTypeSupported(format));
    }
    /**
     * Gets the optimal MIME type for recording
     */
    getBestMimeType() {
        // Priority: WebM/Opus > WebM > MP4 > WAV > OGG
        const preferred = [
            'audio/webm;codecs=opus',
            'audio/webm',
            'audio/mp4',
            'audio/wav',
            'audio/ogg;codecs=opus',
            'audio/ogg'
        ];
        for (const type of preferred) {
            if (this.supportedMimeTypes.includes(type)) {
                return type;
            }
        }
        throw new Error('Browser does not support audio recording');
    }
    /**
     * Checks browser compatibility with the recording API
     */
    static checkBrowserCompatibility() {
        const missing = [];
        if (!navigator?.mediaDevices?.getUserMedia) {
            missing.push('getUserMedia API');
        }
        if (typeof MediaRecorder === 'undefined') {
            missing.push('MediaRecorder API');
        }
        return {
            supported: missing.length === 0,
            missing
        };
    }
    /**
     * Starts recording audio
     */
    async startRecording() {
        if (this.isRecording) {
            const error = new Error('Recording already in progress');
            this.events.onError(error);
            return;
        }
        const compatibility = AudioRecorder.checkBrowserCompatibility();
        if (!compatibility.supported) {
            const error = new Error(`Browser does not support audio recording. Missing: ${compatibility.missing.join(', ')}`);
            this.events.onError(error);
            return;
        }
        try {
            // Audio stream settings
            const audioConstraints = this.getAudioConstraints();
            // Get access to the microphone
            this.stream = await navigator.mediaDevices.getUserMedia({
                audio: audioConstraints
            });
            // Get the supported MIME type
            const mimeType = this.getBestMimeType();
            // Create MediaRecorder with optimal settings
            const recorderOptions = {
                mimeType,
                audioBitsPerSecond: this.getAudioBitrate()
            };
            this.mediaRecorder = new MediaRecorder(this.stream, recorderOptions);
            this.audioChunks = [];
            this.isRecording = true;
            this.recordingStartTime = Date.now();
            // Setup event handlers
            this.setupMediaRecorderEvents();
            // Setup the maximum duration timer
            this.setupMaxDurationTimer();
            // Start recording
            this.mediaRecorder.start(100); // Collect data every 100ms
            this.events.onRecordingStart();
        }
        catch (error) {
            this.cleanup();
            this.events.onError(error);
        }
    }
    /**
     * Stops recording audio
     */
    stopRecording() {
        if (!this.isRecording || !this.mediaRecorder) {
            return;
        }
        try {
            this.mediaRecorder.stop();
            this.isRecording = false;
            this.clearMaxDurationTimer();
        }
        catch (error) {
            this.events.onError(error);
        }
    }
    /**
     * Gets audio stream settings
     */
    getAudioConstraints() {
        const quality = this.options.quality || 'standard';
        // Base settings for different quality levels
        let sampleRate;
        let sampleSize;
        switch (quality) {
            case 'ultra':
                sampleRate = 48000; // 48kHz for maximum quality
                sampleSize = 24; // 24-bit depth
                break;
            case 'high':
                sampleRate = 44100; // 44.1kHz CD quality
                sampleSize = 16; // 16-bit standard
                break;
            case 'standard':
            default:
                sampleRate = 16000; // 16kHz optimal for Whisper
                sampleSize = 16; // 16-bit
                break;
        }
        // Apply user settings if provided
        const finalSampleRate = this.options.sampleRate || sampleRate;
        const channelCount = this.options.channelCount || 1; // Mono by default
        return {
            sampleRate: finalSampleRate,
            sampleSize: sampleSize,
            channelCount: channelCount,
            echoCancellation: this.options.echoCancellation !== false,
            noiseSuppression: this.options.noiseSuppression !== false,
            autoGainControl: this.options.autoGainControl !== false,
            // Additional settings for improved quality
            latency: quality === 'ultra' ? 0.01 : 0.02 // Low latency for high quality
        };
    }
    /**
     * Gets audio bitrate based on quality settings
     */
    getAudioBitrate() {
        const quality = this.options.quality || 'standard';
        switch (quality) {
            case 'ultra':
                return 256000; // 256kbps for maximum quality
            case 'high':
                return 128000; // 128kbps for high quality
            case 'standard':
            default:
                return 64000; // 64kbps for standard quality
        }
    }
    /**
     * Sets up event handlers for MediaRecorder
     */
    setupMediaRecorderEvents() {
        if (!this.mediaRecorder) {
            return;
        }
        this.mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                this.audioChunks.push(event.data);
                this.events.onDataAvailable?.(event.data);
            }
        };
        this.mediaRecorder.onstop = () => {
            try {
                const audioBlob = this.createAudioBlob();
                this.events.onRecordingStop(audioBlob);
            }
            catch (error) {
                this.events.onError(error);
            }
            finally {
                this.cleanup();
            }
        };
        this.mediaRecorder.onerror = (event) => {
            this.events.onError(new Error(`Error in MediaRecorder: ${event}`));
            this.cleanup();
        };
    }
    /**
     * Creates the final audio blob
     */
    createAudioBlob() {
        if (this.audioChunks.length === 0) {
            throw new Error('No recorded audio data');
        }
        const mimeType = this.mediaRecorder?.mimeType || 'audio/webm';
        return new Blob(this.audioChunks, { type: mimeType });
    }
    /**
     * Sets up the maximum duration timer
     */
    setupMaxDurationTimer() {
        const maxDuration = this.options.maxDuration;
        if (maxDuration && maxDuration > 0) {
            this.maxDurationTimer = setTimeout(() => {
                if (this.isRecording) {
                    this.stopRecording();
                }
            }, maxDuration * 1000);
        }
    }
    /**
     * Clears the maximum duration timer
     */
    clearMaxDurationTimer() {
        if (this.maxDurationTimer) {
            clearTimeout(this.maxDurationTimer);
            this.maxDurationTimer = null;
        }
    }
    /**
     * Clears resources
     */
    cleanup() {
        this.clearMaxDurationTimer();
        if (this.stream) {
            this.stream.getTracks().forEach((track) => track.stop());
            this.stream = null;
        }
        this.mediaRecorder = null;
        this.audioChunks = [];
        this.isRecording = false;
        this.recordingStartTime = 0;
    }
    /**
     * Returns the current recording state
     */
    getIsRecording() {
        return this.isRecording;
    }
    /**
     * Returns the duration of the current recording in milliseconds
     */
    getRecordingDuration() {
        if (!this.isRecording) {
            return 0;
        }
        return Date.now() - this.recordingStartTime;
    }
    /**
     * Returns supported MIME types
     */
    getSupportedMimeTypes() {
        return [...this.supportedMimeTypes];
    }
    /**
     * Checks if the microphone is available
     */
    static async checkMicrophonePermission() {
        try {
            if (!navigator?.permissions) {
                return { state: 'unknown', available: false };
            }
            const permission = await navigator.permissions.query({ name: 'microphone' });
            const available = permission.state === 'granted';
            return {
                state: permission.state,
                available
            };
        }
        catch (error) {
            return { state: 'unknown', available: false };
        }
    }
}
exports.AudioRecorder = AudioRecorder;
//# sourceMappingURL=AudioRecorder.js.map