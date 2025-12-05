"use strict";
// ffmpegMocks.ts - FFmpeg and related module mocks for testing
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
exports.FFmpegTestScenarios = exports.mockDeviceListOutput = exports.mockPlatformCommands = exports.MockBlob = exports.mockPath = exports.mockFs = exports.mockChildProcess = exports.mockTmp = exports.mockWhich = exports.MockTempFile = exports.MockChildProcess = void 0;
exports.setupFFmpegMocks = setupFFmpegMocks;
exports.cleanupFFmpegMocks = cleanupFFmpegMocks;
exports.createMockAudioBlob = createMockAudioBlob;
exports.createMockFFmpegError = createMockFFmpegError;
exports.createMockDeviceList = createMockDeviceList;
exports.simulateFFmpegVersion = simulateFFmpegVersion;
exports.simulatePlatformSpecificBehavior = simulatePlatformSpecificBehavior;
const sinon = __importStar(require("sinon"));
const events_1 = require("events");
class MockChildProcess extends events_1.EventEmitter {
    stdin = {
        write: sinon.stub(),
        end: sinon.stub()
    };
    stdout = {
        on: sinon.stub()
    };
    stderr = {
        on: sinon.stub()
    };
    kill = sinon.stub();
    pid = 12345;
    exitCode = null;
    constructor() {
        super();
        // Simulate successful process completion by default
        setTimeout(() => {
            this.exitCode = 0;
            this.emit('exit', 0, null);
        }, 100);
    }
    simulateError(errorCode, signal) {
        this.exitCode = errorCode;
        this.emit('exit', errorCode, signal);
    }
    simulateFFmpegOutput(data) {
        this.stderr.on.callsArgWith(1, Buffer.from(data));
    }
}
exports.MockChildProcess = MockChildProcess;
class MockTempFile {
    path;
    fd;
    removeCallback;
    constructor(path = '/tmp/mock-audio-12345.wav') {
        this.path = path;
        this.fd = 3;
        this.removeCallback = sinon.stub();
    }
}
exports.MockTempFile = MockTempFile;
// Mock for 'which' module
exports.mockWhich = {
    sync: sinon.stub()
};
// Mock for 'tmp' module
exports.mockTmp = {
    file: sinon.stub(),
    setGracefulCleanup: sinon.stub()
};
// Mock for 'child_process' module
exports.mockChildProcess = {
    spawn: sinon.stub()
};
// Mock for 'fs' module
exports.mockFs = {
    createReadStream: sinon.stub(),
    createWriteStream: sinon.stub(),
    existsSync: sinon.stub(),
    readFileSync: sinon.stub(),
    writeFileSync: sinon.stub(),
    unlinkSync: sinon.stub(),
    promises: {
        access: sinon.stub(),
        unlink: sinon.stub(),
        readFile: sinon.stub(),
        writeFile: sinon.stub()
    }
};
// Mock for 'path' module
exports.mockPath = {
    join: sinon.stub(),
    resolve: sinon.stub(),
    dirname: sinon.stub(),
    basename: sinon.stub(),
    extname: sinon.stub()
};
// Mock for Node.js Blob (if available)
class MockBlob {
    size;
    type;
    _data;
    constructor(blobParts, options) {
        this.type = options?.type || 'audio/wav';
        this._data = blobParts || [];
        this.size = this._data.join('').length;
    }
    async arrayBuffer() {
        const data = this._data.join('');
        const buffer = new ArrayBuffer(data.length);
        const view = new Uint8Array(buffer);
        for (let i = 0; i < data.length; i++) {
            view[i] = data.charCodeAt(i);
        }
        return buffer;
    }
    stream() {
        const data = this._data;
        return new ReadableStream({
            start(controller) {
                controller.enqueue(new Uint8Array(Buffer.from(data.join(''))));
                controller.close();
            }
        });
    }
    slice(start, end, contentType) {
        const slicedData = this._data.join('').slice(start, end);
        return new MockBlob([slicedData], { type: contentType || this.type });
    }
    async text() {
        return this._data.join('');
    }
    async bytes() {
        const data = this._data.join('');
        const buffer = new Uint8Array(data.length);
        for (let i = 0; i < data.length; i++) {
            buffer[i] = data.charCodeAt(i);
        }
        return buffer;
    }
}
exports.MockBlob = MockBlob;
// Mock for platform-specific commands
exports.mockPlatformCommands = {
    win32: {
        ffmpeg: 'ffmpeg.exe',
        listDevices: ['-f', 'dshow', '-list_devices', 'true', '-i', 'dummy'],
        recordCommand: ['-f', 'dshow', '-i', 'audio="Microphone"']
    },
    darwin: {
        ffmpeg: 'ffmpeg',
        listDevices: ['-f', 'avfoundation', '-list_devices', 'true', '-i', '""'],
        recordCommand: ['-f', 'avfoundation', '-i', ':0']
    },
    linux: {
        ffmpeg: 'ffmpeg',
        listDevices: ['-f', 'pulse', '-list_devices', 'true', '-i', 'dummy'],
        recordCommand: ['-f', 'pulse', '-i', 'default']
    }
};
// Mock for list_devices command output
exports.mockDeviceListOutput = {
    win32: `[dshow @ 0x12345] DirectShow video devices
[dshow @ 0x12345]  "Integrated Camera"
[dshow @ 0x12345] DirectShow audio devices
[dshow @ 0x12345]  "Microphone (High Definition Audio Device)"
[dshow @ 0x12345]  "Line In (High Definition Audio Device)"`,
    darwin: `[AVFoundation indev @ 0x12345] AVFoundation video devices:
[AVFoundation indev @ 0x12345] [0] FaceTime HD Camera
[AVFoundation indev @ 0x12345] AVFoundation audio devices:
[AVFoundation indev @ 0x12345] [0] MacBook Pro Microphone
[AVFoundation indev @ 0x12345] [1] External Microphone`,
    linux: `[pulse @ 0x12345] PulseAudio audio devices:
[pulse @ 0x12345]  "default" (PulseAudio default)
[pulse @ 0x12345]  "alsa_input.pci-0000_00_1f.3.analog-stereo" (Built-in Audio Analog Stereo)`
};
// Global mocks for testing
function setupFFmpegMocks() {
    // Mock which - determines FFmpeg availability
    exports.mockWhich.sync.withArgs('ffmpeg').returns('/usr/local/bin/ffmpeg');
    exports.mockWhich.sync.withArgs('ffmpeg.exe').returns('C:\\ffmpeg\\bin\\ffmpeg.exe');
    // Mock tmp - creating temporary files
    const mockTempFile = new MockTempFile();
    exports.mockTmp.file.callsArgWith(1, null, mockTempFile.path, mockTempFile.fd, mockTempFile.removeCallback);
    // Mock child_process.spawn - starting FFmpeg
    const mockProcess = new MockChildProcess();
    exports.mockChildProcess.spawn.returns(mockProcess);
    // Mock fs operations
    exports.mockFs.existsSync.returns(true);
    exports.mockFs.createReadStream.returns({
        on: sinon.stub(),
        pipe: sinon.stub(),
        destroy: sinon.stub()
    });
    exports.mockFs.createWriteStream.returns({
        write: sinon.stub(),
        end: sinon.stub(),
        on: sinon.stub()
    });
    // Mock path operations
    exports.mockPath.join.callsFake((...args) => args.join('/'));
    exports.mockPath.resolve.callsFake((...args) => '/' + args.join('/'));
    exports.mockPath.dirname.returns('/tmp');
    exports.mockPath.basename.returns('mock-audio.wav');
    exports.mockPath.extname.returns('.wav');
    // Setup Node.js Blob if available
    if (!global.Blob) {
        global.Blob = MockBlob;
    }
    // Mock for process.platform
    Object.defineProperty(process, 'platform', {
        value: 'darwin', // default macOS for tests
        writable: true,
        configurable: true
    });
}
function cleanupFFmpegMocks() {
    // Clear all stubs
    sinon.restore();
    // Reset mocks to initial state
    exports.mockWhich.sync.reset();
    exports.mockTmp.file.reset();
    exports.mockChildProcess.spawn.reset();
    exports.mockFs.existsSync.reset();
    exports.mockFs.createReadStream.reset();
    exports.mockFs.createWriteStream.reset();
    exports.mockPath.join.reset();
    exports.mockPath.resolve.reset();
    exports.mockPath.dirname.reset();
    exports.mockPath.basename.reset();
    exports.mockPath.extname.reset();
}
function createMockAudioBlob(size = 1024) {
    const audioData = new Array(size).fill('0').join('');
    return new MockBlob([audioData], { type: 'audio/wav' });
}
function createMockFFmpegError(message, code = 'ENOENT') {
    const error = new Error(message);
    error.code = code;
    error.syscall = 'spawn ffmpeg';
    error.path = 'ffmpeg';
    return error;
}
function createMockDeviceList(platform = 'darwin') {
    switch (platform) {
        case 'win32':
            return ['Microphone (High Definition Audio Device)', 'Line In (High Definition Audio Device)'];
        case 'darwin':
            return ['MacBook Pro Microphone', 'External Microphone'];
        case 'linux':
            return ['default', 'alsa_input.pci-0000_00_1f.3.analog-stereo'];
        default:
            return ['Default Microphone'];
    }
}
function simulateFFmpegVersion() {
    return `ffmpeg version 4.4.0 Copyright (c) 2000-2021 the FFmpeg developers
built with Apple clang version 12.0.0
configuration: --enable-gpl --enable-version3`;
}
function simulatePlatformSpecificBehavior(platform) {
    Object.defineProperty(process, 'platform', {
        value: platform,
        writable: true,
        configurable: true
    });
    // Setup platform-specific mocks
    const commands = exports.mockPlatformCommands[platform];
    if (commands) {
        exports.mockWhich.sync.withArgs(commands.ffmpeg).returns(`/usr/local/bin/${commands.ffmpeg}`);
    }
}
// Utilities for testing various scenarios
exports.FFmpegTestScenarios = {
    // Successful recording
    successfulRecording: () => {
        const process = new MockChildProcess();
        exports.mockChildProcess.spawn.returns(process);
        return process;
    },
    // FFmpeg not found
    ffmpegNotFound: () => {
        exports.mockWhich.sync.throws(createMockFFmpegError('FFmpeg not found', 'ENOENT'));
    },
    // Recording error
    recordingError: () => {
        const process = new MockChildProcess();
        setTimeout(() => process.simulateError(1, 'SIGTERM'), 50);
        exports.mockChildProcess.spawn.returns(process);
        return process;
    },
    // No audio devices
    noAudioDevices: () => {
        const process = new MockChildProcess();
        process.simulateFFmpegOutput('No audio devices found');
        exports.mockChildProcess.spawn.returns(process);
        return process;
    },
    // Temporary file cannot be created
    tempFileError: () => {
        exports.mockTmp.file.callsArgWith(1, new Error('Cannot create temp file'), null, null, null);
    }
};
//# sourceMappingURL=ffmpegMocks.js.map