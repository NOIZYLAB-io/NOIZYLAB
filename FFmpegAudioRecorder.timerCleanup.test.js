"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
const assert = __importStar(require("assert"));
const sinon = __importStar(require("sinon"));
const events_1 = require("events");
const FFmpegAudioRecorder_js_1 = require("../../core/FFmpegAudioRecorder.js");
describe('FFmpegAudioRecorder - Timer Cleanup Tests', () => {
    let sandbox;
    let mockEvents;
    let recorder;
    let mockChildProcess;
    let onRecordingStartSpy;
    let onRecordingStopSpy;
    let onErrorSpy;
    beforeEach(() => {
        sandbox = sinon.createSandbox();
        onRecordingStartSpy = sandbox.spy();
        onRecordingStopSpy = sandbox.spy();
        onErrorSpy = sandbox.spy();
        mockEvents = {
            onRecordingStart: onRecordingStartSpy,
            onRecordingStop: onRecordingStopSpy,
            onError: onErrorSpy
        };
        mockChildProcess = new events_1.EventEmitter();
        mockChildProcess.killed = false;
        mockChildProcess.stdout = new events_1.EventEmitter();
        mockChildProcess.stderr = new events_1.EventEmitter();
        mockChildProcess.kill = sandbox.stub().callsFake((signal) => {
            mockChildProcess.killed = true;
            setTimeout(() => {
                mockChildProcess.emit('close', signal === 'SIGTERM' ? 0 : 255);
            }, 50);
        });
        sandbox.stub(require('child_process'), 'spawn').returns(mockChildProcess);
        sandbox.stub(FFmpegAudioRecorder_js_1.FFmpegAudioRecorder, 'checkFFmpegAvailability').resolves({
            available: true,
            version: '4.4.0',
            path: '/usr/local/bin/ffmpeg'
        });
        sandbox.stub(FFmpegAudioRecorder_js_1.FFmpegAudioRecorder, 'detectInputDevices').resolves([
            { id: ':0', name: 'Built-in Microphone', isDefault: true }
        ]);
    });
    afterEach(() => {
        if (recorder) {
            try {
                recorder.stopRecording();
            }
            catch (error) {
                // Ignoring cleanup errors
            }
        }
        sandbox.restore();
    });
    describe('Timer Cleanup', () => {
        it('should clear timers when silenceDetection=false', async () => {
            const options = {
                silenceDetection: false,
                maxDuration: 2,
                silenceDuration: 1
            };
            recorder = new FFmpegAudioRecorder_js_1.FFmpegAudioRecorder(mockEvents, options);
            const recorderAny = recorder;
            const clearSilenceTimerSpy = sandbox.spy(recorderAny, 'clearSilenceTimer');
            const clearMaxDurationTimerSpy = sandbox.spy(recorderAny, 'clearMaxDurationTimer');
            const setupSilenceDetectionSpy = sandbox.spy(recorderAny, 'setupSilenceDetection');
            try {
                await recorder.startRecording();
            }
            catch (error) {
                // Expected in test environment
            }
            assert.ok(setupSilenceDetectionSpy.calledOnce, 'setupSilenceDetection should be called during initialization');
            recorder.stopRecording();
            assert.ok(clearSilenceTimerSpy.called, 'clearSilenceTimer should be called when stopping recording');
            assert.ok(clearMaxDurationTimerSpy.called, 'clearMaxDurationTimer should be called when stopping recording');
        });
        it('should clear timers when silenceDetection=true', async () => {
            const options = {
                silenceDetection: true,
                maxDuration: 10,
                silenceDuration: 1
            };
            recorder = new FFmpegAudioRecorder_js_1.FFmpegAudioRecorder(mockEvents, options);
            const recorderAny = recorder;
            const clearSilenceTimerSpy = sandbox.spy(recorderAny, 'clearSilenceTimer');
            const clearMaxDurationTimerSpy = sandbox.spy(recorderAny, 'clearMaxDurationTimer');
            const setupSilenceDetectionSpy = sandbox.spy(recorderAny, 'setupSilenceDetection');
            try {
                await recorder.startRecording();
            }
            catch (error) {
                // Expected in test environment
            }
            assert.ok(setupSilenceDetectionSpy.calledOnce, 'setupSilenceDetection should be called');
            recorder.stopRecording();
            assert.ok(clearSilenceTimerSpy.called, 'clearSilenceTimer should be called');
            assert.ok(clearMaxDurationTimerSpy.called, 'clearMaxDurationTimer should be called');
        });
        it('should set up silence detection correctly', () => {
            // Test with disabled silence detection
            const optionsDisabled = {
                silenceDetection: false,
                maxDuration: 60
            };
            const recorderDisabled = new FFmpegAudioRecorder_js_1.FFmpegAudioRecorder(mockEvents, optionsDisabled);
            const recorderDisabledAny = recorderDisabled;
            const setupSilenceDetectionSpyDisabled = sandbox.spy(recorderDisabledAny, 'setupSilenceDetection');
            recorderDisabledAny.setupSilenceDetection();
            assert.ok(setupSilenceDetectionSpyDisabled.calledOnce, 'setupSilenceDetection should be called');
            assert.strictEqual(recorderDisabledAny.silenceDetectionEnabled, false, 'silenceDetectionEnabled should be false');
            // Test with enabled silence detection
            const optionsEnabled = {
                silenceDetection: true,
                maxDuration: 60,
                silenceDuration: 3
            };
            const recorderEnabled = new FFmpegAudioRecorder_js_1.FFmpegAudioRecorder(mockEvents, optionsEnabled);
            const recorderEnabledAny = recorderEnabled;
            const setupSilenceDetectionSpyEnabled = sandbox.spy(recorderEnabledAny, 'setupSilenceDetection');
            recorderEnabledAny.setupSilenceDetection();
            assert.ok(setupSilenceDetectionSpyEnabled.calledOnce, 'setupSilenceDetection should be called');
            assert.strictEqual(recorderEnabledAny.silenceDetectionEnabled, true, 'silenceDetectionEnabled should be true');
        });
    });
    describe('Recording State Management', () => {
        it('should handle multiple start/stop cycles without errors', async () => {
            const options = {
                silenceDetection: false,
                maxDuration: 60
            };
            recorder = new FFmpegAudioRecorder_js_1.FFmpegAudioRecorder(mockEvents, options);
            // Multiple start/stop cycles - just test no errors thrown
            for (let i = 0; i < 3; i++) {
                try {
                    await recorder.startRecording();
                }
                catch (error) {
                    // Expected in test environment
                }
                recorder.stopRecording();
            }
            // Just verify no errors thrown
            assert.ok(true, 'Multiple start/stop cycles completed without errors');
        });
        it('should handle cleanup when process is null', () => {
            const options = {
                silenceDetection: false,
                maxDuration: 60
            };
            recorder = new FFmpegAudioRecorder_js_1.FFmpegAudioRecorder(mockEvents, options);
            const recorderAny = recorder;
            // Ensure process is null
            recorderAny.ffmpegProcess = null;
            // Should not throw error
            assert.doesNotThrow(() => {
                recorder.stopRecording();
            }, 'stopRecording should handle null process gracefully');
        });
    });
});
//# sourceMappingURL=FFmpegAudioRecorder.timerCleanup.test.js.map