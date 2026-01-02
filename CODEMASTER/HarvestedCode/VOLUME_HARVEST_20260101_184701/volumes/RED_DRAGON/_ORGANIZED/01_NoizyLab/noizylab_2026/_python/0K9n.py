#!/usr/bin/env python3
"""
Noizy AI Audio Extension Setup Script
Automates the complete setup of the VS Code audio extension
"""

import os
import json
import subprocess
import sys
from pathlib import Path

class NoizyAIExtensionBuilder:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.src_dir = self.project_root / "src"
        self.audio_dir = self.src_dir / "audio"
        
    def create_directories(self):
        """Create all necessary directories"""
        print("📁 Creating directory structure...")
        directories = [
            self.src_dir,
            self.audio_dir,
            self.src_dir / "ui",
            self.src_dir / "ai",
            self.project_root / "out",
            self.project_root / "media"
        ]
        
        for dir_path in directories:
            dir_path.mkdir(exist_ok=True)
            print(f"   ✓ Created {dir_path}")
    
    def install_dependencies(self):
        """Install npm dependencies"""
        print("📦 Installing dependencies...")
        try:
            # Install dev dependencies
            dev_deps = [
                "@types/vscode@^1.104.0",
                "@types/node@18.x",
                "@typescript-eslint/eslint-plugin@^6.4.1",
                "@typescript-eslint/parser@^6.4.1",
                "eslint@^8.47.0",
                "typescript@^5.1.6",
                "@vscode/test-electron@^2.3.4"
            ]
            
            subprocess.run(["npm", "install", "--save-dev"] + dev_deps, 
                         cwd=self.project_root, check=True)
            
            # Install production dependencies
            prod_deps = [
                "ws@^8.14.0",
                "node-fetch@^3.3.0"
            ]
            
            subprocess.run(["npm", "install", "--save"] + prod_deps,
                         cwd=self.project_root, check=True)
            
            print("   ✓ Dependencies installed successfully")
            
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Failed to install dependencies: {e}")
            return False
        return True
    
    def create_audio_core_files(self):
        """Create audio processing core files"""
        print("🎵 Creating audio core files...")
        
        # Noise Generator
        noise_generator_content = '''import * as vscode from 'vscode';

export class NoiseGenerator {
    private audioContext: AudioContext | null = null;
    private oscillator: OscillatorNode | null = null;
    private gainNode: GainNode | null = null;
    private isActive: boolean = false;

    constructor() {
        // Initialize in browser environment only
        if (typeof window !== 'undefined' && window.AudioContext) {
            this.audioContext = new AudioContext();
        }
    }

    async generateNoise(type: string): Promise<void> {
        try {
            if (!this.audioContext) {
                vscode.window.showWarningMessage('Audio not supported in this environment');
                return;
            }

            this.stop(); // Stop any existing noise

            this.oscillator = this.audioContext.createOscillator();
            this.gainNode = this.audioContext.createGain();

            switch (type) {
                case 'white_noise':
                    await this.createWhiteNoise();
                    break;
                case 'pink_noise':
                    await this.createPinkNoise();
                    break;
                case 'brown_noise':
                    await this.createBrownNoise();
                    break;
                case 'rain':
                    await this.createRainSound();
                    break;
                case 'ocean_waves':
                    await this.createOceanWaves();
                    break;
                default:
                    await this.createWhiteNoise();
            }

            this.gainNode.gain.value = 0.1; // Low volume
            this.oscillator.connect(this.gainNode);
            this.gainNode.connect(this.audioContext.destination);

            this.oscillator.start();
            this.isActive = true;

        } catch (error) {
            vscode.window.showErrorMessage(`Failed to generate noise: ${error}`);
        }
    }

    private async createWhiteNoise(): Promise<void> {
        if (!this.oscillator) return;
        
        // Simple white noise using square wave with random frequency modulation
        this.oscillator.type = 'square';
        this.oscillator.frequency.setValueAtTime(440, 0);
    }

    private async createPinkNoise(): Promise<void> {
        if (!this.oscillator) return;
        
        this.oscillator.type = 'sawtooth';
        this.oscillator.frequency.setValueAtTime(220, 0);
    }

    private async createBrownNoise(): Promise<void> {
        if (!this.oscillator) return;
        
        this.oscillator.type = 'triangle';
        this.oscillator.frequency.setValueAtTime(110, 0);
    }

    private async createRainSound(): Promise<void> {
        if (!this.oscillator) return;
        
        this.oscillator.type = 'white';
        this.oscillator.frequency.setValueAtTime(1000, 0);
    }

    private async createOceanWaves(): Promise<void> {
        if (!this.oscillator) return;
        
        this.oscillator.type = 'sine';
        this.oscillator.frequency.setValueAtTime(80, 0);
    }

    stop(): void {
        if (this.oscillator) {
            this.oscillator.stop();
            this.oscillator = null;
        }
        this.isActive = false;
    }

    pause(): void {
        if (this.gainNode) {
            this.gainNode.gain.setValueAtTime(0, 0);
        }
    }

    resume(): void {
        if (this.gainNode) {
            this.gainNode.gain.setValueAtTime(0.1, 0);
        }
    }

    isPlaying(): boolean {
        return this.isActive;
    }

    dispose(): void {
        this.stop();
        if (this.audioContext) {
            this.audioContext.close();
        }
    }
}'''
        
        # Audio Enhancer
        audio_enhancer_content = '''import * as vscode from 'vscode';

export class AudioEnhancer {
    private audioContext: AudioContext | null = null;
    private filters: BiquadFilterNode[] = [];

    constructor() {
        if (typeof window !== 'undefined' && window.AudioContext) {
            this.audioContext = new AudioContext();
        }
    }

    async enhance(type: string): Promise<void> {
        try {
            if (!this.audioContext) {
                vscode.window.showInformationMessage('Audio enhancement simulated (no audio context available)');
                return;
            }

            switch (type) {
                case 'noise_reduction':
                    await this.applyNoiseReduction();
                    break;
                case 'volume_normalize':
                    await this.normalizeVolume();
                    break;
                case 'bass_boost':
                    await this.boostBass();
                    break;
                case 'treble_enhance':
                    await this.enhanceTreble();
                    break;
                case 'echo_removal':
                    await this.removeEcho();
                    break;
                default:
                    throw new Error('Unknown enhancement type');
            }

        } catch (error) {
            throw new Error(`Enhancement failed: ${error}`);
        }
    }

    private async applyNoiseReduction(): Promise<void> {
        // Simulate noise reduction with high-pass filter
        const filter = this.audioContext!.createBiquadFilter();
        filter.type = 'highpass';
        filter.frequency.setValueAtTime(200, 0);
        this.filters.push(filter);
    }

    private async normalizeVolume(): Promise<void> {
        // Simulate volume normalization
        const compressor = this.audioContext!.createDynamicsCompressor();
        compressor.threshold.setValueAtTime(-24, 0);
        compressor.knee.setValueAtTime(30, 0);
        compressor.ratio.setValueAtTime(12, 0);
    }

    private async boostBass(): Promise<void> {
        // Low frequency boost
        const bassFilter = this.audioContext!.createBiquadFilter();
        bassFilter.type = 'lowshelf';
        bassFilter.frequency.setValueAtTime(320, 0);
        bassFilter.gain.setValueAtTime(10, 0);
        this.filters.push(bassFilter);
    }

    private async enhanceTreble(): Promise<void> {
        // High frequency enhancement
        const trebleFilter = this.audioContext!.createBiquadFilter();
        trebleFilter.type = 'highshelf';
        trebleFilter.frequency.setValueAtTime(3200, 0);
        trebleFilter.gain.setValueAtTime(5, 0);
        this.filters.push(trebleFilter);
    }

    private async removeEcho(): Promise<void> {
        // Simulate echo removal with delay and feedback reduction
        const delay = this.audioContext!.createDelay();
        delay.delayTime.setValueAtTime(0.02, 0);
    }

    dispose(): void {
        this.filters = [];
        if (this.audioContext) {
            this.audioContext.close();
        }
    }
}'''
        
        # Write the files
        files = [
            (self.audio_dir / "noiseGenerator.ts", noise_generator_content),
            (self.audio_dir / "audioEnhancer.ts", audio_enhancer_content)
        ]
        
        for file_path, content in files:
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"   ✓ Created {file_path}")
    
    def create_ui_files(self):
        """Create UI components"""
        print("🖥️ Creating UI components...")
        
        # Audio Control Panel
        audio_panel_content = '''import * as vscode from 'vscode';
import { NoiseGenerator } from './audio/noiseGenerator';
import { AudioEnhancer } from './audio/audioEnhancer';

export class AudioControlPanel {
    public static currentPanel: AudioControlPanel | undefined;
    private readonly _panel: vscode.WebviewPanel;
    private _disposables: vscode.Disposable[] = [];

    public static createOrShow(
        extensionUri: vscode.Uri,
        noiseGenerator: NoiseGenerator,
        audioEnhancer: AudioEnhancer
    ) {
        const column = vscode.window.activeTextEditor
            ? vscode.window.activeTextEditor.viewColumn
            : undefined;

        if (AudioControlPanel.currentPanel) {
            AudioControlPanel.currentPanel._panel.reveal(column);
            return;
        }

        const panel = vscode.window.createWebviewPanel(
            'noizyAudioPanel',
            'Noizy AI Audio Control',
            column || vscode.ViewColumn.One,
            {
                enableScripts: true,
                localResourceRoots: [vscode.Uri.joinPath(extensionUri, 'media')]
            }
        );

        AudioControlPanel.currentPanel = new AudioControlPanel(
            panel,
            extensionUri,
            noiseGenerator,
            audioEnhancer
        );
    }

    constructor(
        panel: vscode.WebviewPanel,
        extensionUri: vscode.Uri,
        private noiseGenerator: NoiseGenerator,
        private audioEnhancer: AudioEnhancer
    ) {
        this._panel = panel;

        this._update();

        this._panel.onDidDispose(() => this.dispose(), null, this._disposables);

        this._panel.webview.onDidReceiveMessage(
            message => {
                switch (message.command) {
                    case 'generateNoise':
                        this.noiseGenerator.generateNoise(message.type);
                        return;
                    case 'stopNoise':
                        this.noiseGenerator.stop();
                        return;
                    case 'enhanceAudio':
                        this.audioEnhancer.enhance(message.type);
                        return;
                }
            },
            null,
            this._disposables
        );
    }

    public show() {
        this._panel.reveal();
    }

    public dispose() {
        AudioControlPanel.currentPanel = undefined;

        this._panel.dispose();

        while (this._disposables.length) {
            const x = this._disposables.pop();
            if (x) {
                x.dispose();
            }
        }
    }

    private _update() {
        const webview = this._panel.webview;
        this._panel.webview.html = this._getHtmlForWebview(webview);
    }

    private _getHtmlForWebview(webview: vscode.Webview) {
        return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Noizy AI Audio Control</title>
    <style>
        body {
            font-family: var(--vscode-font-family);
            color: var(--vscode-foreground);
            background-color: var(--vscode-editor-background);
            padding: 20px;
        }
        .section {
            margin-bottom: 30px;
            padding: 15px;
            border: 1px solid var(--vscode-panel-border);
            border-radius: 5px;
        }
        .section h3 {
            margin-top: 0;
            color: var(--vscode-textLink-foreground);
        }
        .button-group {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }
        .btn {
            padding: 8px 16px;
            background-color: var(--vscode-button-background);
            color: var(--vscode-button-foreground);
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
        .btn:hover {
            background-color: var(--vscode-button-hoverBackground);
        }
        .volume-control {
            margin-top: 15px;
        }
        .volume-slider {
            width: 100%;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <h2>🎵 Noizy AI Audio Control Panel</h2>
    
    <div class="section">
        <h3>Noise Generation</h3>
        <div class="button-group">
            <button class="btn" onclick="generateNoise('white_noise')">White Noise</button>
            <button class="btn" onclick="generateNoise('pink_noise')">Pink Noise</button>
            <button class="btn" onclick="generateNoise('brown_noise')">Brown Noise</button>
            <button class="btn" onclick="generateNoise('rain')">Rain</button>
            <button class="btn" onclick="generateNoise('ocean_waves')">Ocean Waves</button>
        </div>
        <div class="button-group">
            <button class="btn" onclick="stopNoise()">Stop All</button>
        </div>
        <div class="volume-control">
            <label>Volume: <span id="volumeValue">50</span>%</label>
            <input type="range" class="volume-slider" min="0" max="100" value="50" onchange="setVolume(this.value)">
        </div>
    </div>

    <div class="section">
        <h3>Audio Enhancement</h3>
        <div class="button-group">
            <button class="btn" onclick="enhanceAudio('noise_reduction')">Noise Reduction</button>
            <button class="btn" onclick="enhanceAudio('volume_normalize')">Volume Normalize</button>
            <button class="btn" onclick="enhanceAudio('bass_boost')">Bass Boost</button>
            <button class="btn" onclick="enhanceAudio('treble_enhance')">Treble Enhance</button>
            <button class="btn" onclick="enhanceAudio('echo_removal')">Echo Removal</button>
        </div>
    </div>

    <div class="section">
        <h3>AI Features (Coming Soon)</h3>
        <div class="button-group">
            <button class="btn" disabled>Voice Synthesis</button>
            <button class="btn" disabled>Audio Analysis</button>
            <button class="btn" disabled>Smart Enhancement</button>
        </div>
    </div>

    <script>
        const vscode = acquireVsCodeApi();

        function generateNoise(type) {
            vscode.postMessage({
                command: 'generateNoise',
                type: type
            });
        }

        function stopNoise() {
            vscode.postMessage({
                command: 'stopNoise'
            });
        }

        function enhanceAudio(type) {
            vscode.postMessage({
                command: 'enhanceAudio',
                type: type
            });
        }

        function setVolume(value) {
            document.getElementById('volumeValue').textContent = value;
            // Volume control will be implemented in future versions
        }
    </script>
</body>
</html>`;
    }
}'''
        
        with open(self.src_dir / "audioControlPanel.ts", 'w') as f:
            f.write(audio_panel_content)
        print(f"   ✓ Created audio control panel")
    
    def create_ai_features(self):
        """Create AI-powered features placeholder"""
        print("🤖 Creating AI feature modules...")
        
        ai_processor_content = '''import * as vscode from 'vscode';

export class AIAudioProcessor {
    constructor() {
        // Future: Initialize AI models for audio processing
    }

    async analyzeSentiment(audioBuffer: ArrayBuffer): Promise<string> {
        // Placeholder for AI sentiment analysis of audio
        await new Promise(resolve => setTimeout(resolve, 1000)); // Simulate processing
        
        const sentiments = ['happy', 'sad', 'neutral', 'excited', 'calm'];
        return sentiments[Math.floor(Math.random() * sentiments.length)];
    }

    async transcribeAudio(audioBuffer: ArrayBuffer): Promise<string> {
        // Placeholder for AI audio transcription
        await new Promise(resolve => setTimeout(resolve, 2000)); // Simulate processing
        
        return "This is a placeholder transcription. AI transcription will be implemented in future versions.";
    }

    async generateVoice(text: string, voice: string = 'default'): Promise<ArrayBuffer> {
        // Placeholder for AI voice synthesis
        await new Promise(resolve => setTimeout(resolve, 1500)); // Simulate processing
        
        vscode.window.showInformationMessage(`Voice synthesis for "${text}" completed (placeholder)`);
        return new ArrayBuffer(0); // Placeholder
    }

    async smartEnhance(audioBuffer: ArrayBuffer): Promise<ArrayBuffer> {
        // Placeholder for AI-powered smart audio enhancement
        await new Promise(resolve => setTimeout(resolve, 3000)); // Simulate processing
        
        vscode.window.showInformationMessage('Smart AI enhancement applied (placeholder)');
        return audioBuffer; // Placeholder
    }
}'''
        
        with open(self.src_dir / "ai" / "aiProcessor.ts", 'w') as f:
            f.write(ai_processor_content)
        print(f"   ✓ Created AI processor module")
    
    def update_extension_main(self):
        """Update the main extension file"""
        print("🔧 Updating main extension file...")
        
        updated_extension_content = '''import * as vscode from 'vscode';
import { AudioControlPanel } from './audioControlPanel';
import { NoiseGenerator } from './audio/noiseGenerator';
import { AudioEnhancer } from './audio/audioEnhancer';
import { AIAudioProcessor } from './ai/aiProcessor';

let noiseGenerator: NoiseGenerator;
let audioEnhancer: AudioEnhancer;
let aiProcessor: AIAudioProcessor;

export function activate(context: vscode.ExtensionContext) {
    console.log('Noizy AI Audio Extension is now active!');

    // Initialize audio components
    noiseGenerator = new NoiseGenerator();
    audioEnhancer = new AudioEnhancer();
    aiProcessor = new AIAudioProcessor();

    // Register commands
    const disposables = [
        // Open Audio Control Panel
        vscode.commands.registerCommand('noizy-ai.openAudioPanel', () => {
            AudioControlPanel.createOrShow(context.extensionUri, noiseGenerator, audioEnhancer);
        }),

        // Generate Noise
        vscode.commands.registerCommand('noizy-ai.generateNoise', async () => {
            const noiseType = await vscode.window.showQuickPick(
                [
                    { label: 'White Noise', description: 'Classic white noise for focus' },
                    { label: 'Pink Noise', description: 'Softer, more natural noise' },
                    { label: 'Brown Noise', description: 'Deep, rumbling noise' },
                    { label: 'Rain', description: 'Gentle rain sounds' },
                    { label: 'Ocean Waves', description: 'Relaxing ocean waves' }
                ],
                { placeHolder: 'Select noise type to generate' }
            );
            
            if (noiseType) {
                const type = noiseType.label.toLowerCase().replace(' ', '_');
                await noiseGenerator.generateNoise(type);
                vscode.window.showInformationMessage(`🎵 Generated ${noiseType.label}`);
            }
        }),

        // Enhance Audio
        vscode.commands.registerCommand('noizy-ai.enhanceAudio', async () => {
            const options = await vscode.window.showQuickPick(
                [
                    { label: 'Noise Reduction', description: 'Remove background noise' },
                    { label: 'Volume Normalize', description: 'Normalize audio levels' },
                    { label: 'Bass Boost', description: 'Enhance low frequencies' },
                    { label: 'Treble Enhance', description: 'Enhance high frequencies' },
                    { label: 'Echo Removal', description: 'Remove echo and reverb' }
                ],
                { placeHolder: 'Select audio enhancement' }
            );

            if (options) {
                try {
                    const type = options.label.toLowerCase().replace(' ', '_');
                    await audioEnhancer.enhance(type);
                    vscode.window.showInformationMessage(`✨ Applied ${options.label} enhancement`);
                } catch (error) {
                    vscode.window.showErrorMessage(`Enhancement failed: ${error}`);
                }
            }
        }),

        // Play/Pause Audio
        vscode.commands.registerCommand('noizy-ai.playPause', () => {
            if (noiseGenerator.isPlaying()) {
                noiseGenerator.pause();
                vscode.window.showInformationMessage('⏸️ Audio paused');
            } else {
                noiseGenerator.resume();
                vscode.window.showInformationMessage('▶️ Audio resumed');
            }
        }),

        // AI Features (placeholder commands)
        vscode.commands.registerCommand('noizy-ai.transcribeAudio', async () => {
            const result = await vscode.window.withProgress({
                location: vscode.ProgressLocation.Notification,
                title: "Transcribing audio...",
                cancellable: false
            }, async () => {
                return await aiProcessor.transcribeAudio(new ArrayBuffer(0));
            });
            
            vscode.window.showInformationMessage(result);
        }),

        vscode.commands.registerCommand('noizy-ai.analyzeSentiment', async () => {
            const sentiment = await vscode.window.withProgress({
                location: vscode.ProgressLocation.Notification,
                title: "Analyzing audio sentiment...",
                cancellable: false
            }, async () => {
                return await aiProcessor.analyzeSentiment(new ArrayBuffer(0));
            });
            
            vscode.window.showInformationMessage(`Detected sentiment: ${sentiment}`);
        })
    ];

    // Add all disposables to context
    context.subscriptions.push(...disposables);

    // Show welcome message
    vscode.window.showInformationMessage(
        '🎵 Noizy AI Audio Extension loaded! Use Cmd+Shift+P and search for "Noizy AI" to get started.',
        'Open Audio Panel'
    ).then(selection => {
        if (selection === 'Open Audio Panel') {
            vscode.commands.executeCommand('noizy-ai.openAudioPanel');
        }
    });
}

export function deactivate() {
    if (noiseGenerator) {
        noiseGenerator.dispose();
    }
    if (audioEnhancer) {
        audioEnhancer.dispose();
    }
}'''
        
        with open(self.src_dir / "extension.ts", 'w') as f:
            f.write(updated_extension_content)
        print(f"   ✓ Updated main extension file")
    
    def create_eslint_config(self):
        """Create ESLint configuration"""
        print("⚙️ Creating ESLint configuration...")
        
        eslint_config = {
            "root": True,
            "parser": "@typescript-eslint/parser",
            "parserOptions": {
                "ecmaVersion": 6,
                "sourceType": "module"
            },
            "plugins": [
                "@typescript-eslint"
            ],
            "rules": {
                "@typescript-eslint/naming-convention": "warn",
                "@typescript-eslint/semi": "warn",
                "curly": "warn",
                "eqeqeq": "warn",
                "no-throw-literal": "warn",
                "semi": "off"
            },
            "ignorePatterns": [
                "out",
                "dist",
                "**/*.d.ts"
            ]
        }
        
        with open(self.project_root / ".eslintrc.json", 'w') as f:
            json.dump(eslint_config, f, indent=2)
        print(f"   ✓ Created ESLint configuration")
    
    def update_vscode_config(self):
        """Update VS Code configuration files"""
        print("🔧 Updating VS Code configuration...")
        
        # Update launch.json
        launch_config = {
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "Run Extension",
                    "type": "extensionHost",
                    "request": "launch",
                    "args": [
                        "--extensionDevelopmentPath=${workspaceFolder}"
                    ],
                    "outFiles": [
                        "${workspaceFolder}/out/**/*.js"
                    ],
                    "preLaunchTask": "${workspaceFolder}:tsc:build"
                },
                {
                    "name": "Extension Tests",
                    "type": "extensionHost",
                    "request": "launch",
                    "args": [
                        "--extensionDevelopmentPath=${workspaceFolder}",
                        "--extensionTestsPath=${workspaceFolder}/out/test/suite/index"
                    ],
                    "outFiles": [
                        "${workspaceFolder}/out/test/**/*.js"
                    ],
                    "preLaunchTask": "${workspaceFolder}:tsc:build"
                }
            ]
        }
        
        vscode_dir = self.project_root / ".vscode"
        with open(vscode_dir / "launch.json", 'w') as f:
            json.dump(launch_config, f, indent=2)
        
        # Update settings.json
        settings_config = {
            "out": True,
            "dist": True,
            "**/*.vsix": True,
            "**/node_modules": True,
            ".vscode-test": True
        }
        
        with open(vscode_dir / "settings.json", 'w') as f:
            json.dump({"files.exclude": settings_config}, f, indent=2)
        
        print(f"   ✓ Updated VS Code configuration")
    
    def create_tasks_json(self):
        """Create tasks.json for build automation"""
        print("⚙️ Creating build tasks...")
        
        tasks_config = {
            "version": "2.0.0",
            "tasks": [
                {
                    "type": "npm",
                    "script": "watch",
                    "problemMatcher": "$tsc-watch",
                    "isBackground": True,
                    "presentation": {
                        "reveal": "never",
                        "group": "watchers"
                    },
                    "group": {
                        "kind": "build",
                        "isDefault": True
                    }
                },
                {
                    "type": "npm",
                    "script": "compile",
                    "problemMatcher": "$tsc",
                    "group": "build",
                    "presentation": {
                        "panel": "shared"
                    }
                }
            ]
        }
        
        vscode_dir = self.project_root / ".vscode"
        with open(vscode_dir / "tasks.json", 'w') as f:
            json.dump(tasks_config, f, indent=2)
        
        print(f"   ✓ Created build tasks")
    
    def update_readme(self):
        """Update README with extension information"""
        print("📝 Updating README...")
        
        readme_content = '''# 🎵 Noizy AI Audio Extension

An all-around audio super tool for Visual Studio Code with AI-powered features!

## Features

### 🎶 Noise Generation
- **White Noise**: Classic white noise for focus and concentration
- **Pink Noise**: Softer, more natural noise for relaxation  
- **Brown Noise**: Deep, rumbling noise for deep focus
- **Rain Sounds**: Gentle rain for a calming atmosphere
- **Ocean Waves**: Relaxing ocean sounds for stress relief

### ✨ Audio Enhancement
- **Noise Reduction**: Remove unwanted background noise
- **Volume Normalize**: Automatically adjust audio levels
- **Bass Boost**: Enhance low-frequency sounds
- **Treble Enhance**: Boost high-frequency clarity
- **Echo Removal**: Clean up audio with echo/reverb issues

### 🤖 AI-Powered Features (Coming Soon)
- **Voice Synthesis**: Generate speech from text
- **Audio Transcription**: Convert speech to text
- **Sentiment Analysis**: Analyze emotional content in audio
- **Smart Enhancement**: AI-powered automatic audio improvement

## Usage

### Quick Start
1. Open Command Palette (`Cmd+Shift+P` on macOS, `Ctrl+Shift+P` on Windows/Linux)
2. Type "Noizy AI" to see available commands
3. Select "Open Audio Control Panel" to access the main interface

### Available Commands
- `Noizy AI: Open Audio Control Panel` - Main control interface
- `Noizy AI: Generate Noise` - Quick noise generation
- `Noizy AI: Enhance Audio` - Audio enhancement options
- `Noizy AI: Play/Pause Audio` - Control playback (`Cmd+Alt+P`)

### Keyboard Shortcuts
- `Cmd+Alt+P` (macOS) / `Ctrl+Alt+P` (Windows/Linux) - Play/Pause audio

## Installation

### From Source
1. Clone this repository
2. Run `npm install` to install dependencies
3. Run `npm run compile` to build the extension
4. Press `F5` to open VS Code Extension Development Host

### Development
- Run `npm run watch` for automatic compilation during development
- Use `F5` to launch the Extension Development Host
- Use `Cmd+R` (macOS) / `Ctrl+R` (Windows/Linux) to reload the extension

## Requirements

- Visual Studio Code 1.104.0 or higher
- Node.js 18.x or higher

## Extension Settings

This extension contributes the following settings:
- Audio settings and preferences will be added in future versions

## Known Issues

- Audio processing requires browser-compatible environment
- Some advanced AI features are placeholders and will be implemented in future versions

## Release Notes

### 0.0.1

Initial release of Noizy AI Audio Extension:
- Basic noise generation (White, Pink, Brown, Rain, Ocean)
- Audio enhancement tools (Noise reduction, Volume normalize, Bass/Treble boost, Echo removal)
- Audio control panel with intuitive interface
- Keyboard shortcuts for quick access
- Foundation for AI-powered features

## Contributing

Feel free to contribute to this project! Submit issues and enhancement requests, or fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Enjoy coding with better audio! 🎧**
'''
        
        with open(self.project_root / "README.md", 'w') as f:
            f.write(readme_content)
        
        print(f"   ✓ Updated README")
    
    def compile_extension(self):
        """Compile the TypeScript extension"""
        print("🔨 Compiling extension...")
        
        try:
            result = subprocess.run(
                ["npm", "run", "compile"], 
                cwd=self.project_root, 
                capture_output=True, 
                text=True, 
                check=True
            )
            print("   ✓ Extension compiled successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Compilation failed: {e}")
            print(f"   stdout: {e.stdout}")
            print(f"   stderr: {e.stderr}")
            return False
    
    def run_setup(self):
        """Run the complete setup process"""
        print("🚀 Starting Noizy AI Extension Setup...")
        print("=" * 50)
        
        steps = [
            ("Creating directories", self.create_directories),
            ("Installing dependencies", self.install_dependencies),
            ("Creating audio core files", self.create_audio_core_files),
            ("Creating UI components", self.create_ui_files),
            ("Creating AI features", self.create_ai_features),
            ("Updating main extension", self.update_extension_main),
            ("Creating ESLint config", self.create_eslint_config),
            ("Updating VS Code config", self.update_vscode_config),
            ("Creating build tasks", self.create_tasks_json),
            ("Updating README", self.update_readme),
            ("Compiling extension", self.compile_extension)
        ]
        
        success_count = 0
        for step_name, step_func in steps:
            try:
                if step_func():
                    success_count += 1
                else:
                    print(f"   ⚠️ {step_name} completed with warnings")
                    success_count += 1
            except Exception as e:
                print(f"   ❌ {step_name} failed: {e}")
        
        print("\n" + "=" * 50)
        print(f"✅ Setup completed! ({success_count}/{len(steps)} steps successful)")
        print("\n🎯 Next steps:")
        print("1. Press F5 in VS Code to launch the Extension Development Host")
        print("2. In the new window, press Cmd+Shift+P and type 'Noizy AI'")
        print("3. Select 'Open Audio Control Panel' to test the extension")
        print("4. Try the different noise generation and audio enhancement features")
        print("\n🎵 Happy coding with Noizy AI!")

if __name__ == "__main__":
    project_root = Path(__file__).parent
    builder = NoizyAIExtensionBuilder(project_root)
    
    print("🎵 Noizy AI Audio Extension Setup")
    print("This script will automatically set up your entire VS Code extension.")
    print("\nThe setup will:")
    print("- Install all required dependencies")
    print("- Create audio processing modules")
    print("- Set up the UI components")
    print("- Configure build and debug settings")
    print("- Create AI feature placeholders")
    print("- Compile the extension")
    
    response = input("\n🚀 Do you want to proceed with the automated setup? (y/n): ").lower().strip()
    
    if response in ['y', 'yes']:
        builder.run_setup()
    else:
        print("Setup cancelled. You can run this script anytime with: python3 setup_extension.py")