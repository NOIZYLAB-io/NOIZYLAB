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
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.playSound = playSound;
const vscode = __importStar(require("vscode"));
const fs = __importStar(require("node:fs"));
const node_web_audio_api_1 = require("node-web-audio-api");
const audioContext = new node_web_audio_api_1.AudioContext();
async function playSound(filePath) {
    if (!fs.existsSync(filePath)) {
        throw new Error(`Sound file not found: ${filePath}`);
    }
    try {
        const audioBuffer = await loadAudioBuffer(filePath);
        const source = audioContext.createBufferSource();
        const gainNode = audioContext.createGain();
        const volume = getVolume();
        gainNode.gain.value = volume ? volume / 100 : 1;
        gainNode.connect(audioContext.destination);
        source.connect(gainNode);
        source.buffer = audioBuffer;
        source.start(0);
    }
    catch (error) {
        throw new Error(`AudioPlayer: ${error}`);
    }
}
async function loadAudioBuffer(filePath) {
    const fileBuffer = fs.readFileSync(filePath);
    const audioDecode = (await import("audio-decode")).default;
    const decoded = await audioDecode(fileBuffer.buffer);
    const audioBuffer = audioContext.createBuffer(decoded.numberOfChannels, decoded.length, decoded.sampleRate);
    for (let channel = 0; channel < decoded.numberOfChannels; channel++) {
        audioBuffer.copyToChannel(decoded.getChannelData(channel), channel);
    }
    return audioBuffer;
}
function getVolume() {
    const config = vscode.workspace.getConfiguration("soundSyntax");
    return config.get("volume") || 100;
}
//# sourceMappingURL=audioPlayer.js.map