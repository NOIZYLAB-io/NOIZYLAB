// ============================================================================
// GABRIEL LIVING AVATAR - MAIN APPLICATION CONTROLLER
// ============================================================================

class GabrielApp {
    constructor() {
        this.avatar = null;
        this.aiBrain = null;
        this.voiceSystem = null;
        this.lipSync = null;
        this.gestureSystem = null;
        this.physicsEngine = null;
        this.vrController = null;
        
        // NEW: Integration systems
        this.integrationHub = null;
        this.dashboard = null;
        
        this.isInitialized = false;
        this.isListening = false;
        this.currentEmotion = 'calm';
        
        this.init();
    }
    
    async init() {
        console.log('🚀 Initializing GABRIEL Living Avatar System...');
        
        try {
            // Initialize 3D Avatar
            console.log('📦 Loading 3D Avatar...');
            this.avatar = new AvatarController();
            await this.avatar.init();
            
            // Initialize AI Brain
            console.log('🧠 Initializing AI Brain...');
            this.aiBrain = new AIBrain();
            await this.aiBrain.init();
            
            // Initialize Voice System
            console.log('🎤 Initializing Voice System...');
            this.voiceSystem = new VoiceSystem();
            await this.voiceSystem.init();
            
            // Initialize Lip-Sync Engine
            console.log('👄 Initializing Lip-Sync Engine...');
            this.lipSync = new LipSyncEngine(this.avatar);
            
            // Initialize Gesture Recognition
            console.log('👋 Initializing Gesture Recognition...');
            this.gestureSystem = new GestureSystem(this.avatar);
            await this.gestureSystem.init();
            
            // Initialize Physics Engine
            console.log('⚡ Initializing Physics Engine...');
            this.physicsEngine = new PhysicsEngine(this.avatar);
            await this.physicsEngine.init();
            
            // Initialize WebXR Support
            console.log('🥽 Initializing WebXR Support...');
            this.vrController = new WebXRController(this.avatar);
            
            // NEW: Initialize Integration Hub
            console.log('🔌 Initializing Integration Hub...');
            this.integrationHub = new IntegrationHub();
            const systemsStatus = await this.integrationHub.init();
            console.log('🔌 Connected systems:', systemsStatus);
            
            // NEW: Initialize Unified Dashboard
            console.log('📊 Initializing Unified Dashboard...');
            this.dashboard = new UnifiedDashboard(document.body);
            await this.dashboard.init(this.integrationHub);
            dashboard = this.dashboard; // Make globally accessible
            
            // Setup UI Event Listeners
            this.setupEventListeners();
            
            // Setup integration hub voice commands
            this.setupIntegratedVoiceCommands();
            
            // Hide loading screen
            document.getElementById('loading').style.display = 'none';
            
            // Update status
            document.getElementById('ai-status').textContent = 'Active';
            document.getElementById('avatar-status').textContent = 'Ready';
            
            this.isInitialized = true;
            console.log('✅ GABRIEL initialized successfully!');
            console.log('🎯 Integration Hub Active - All Systems Ready');
            
            // Start animation loop
            this.animate();
            
            // Initial greeting
            this.speak("Hello! I'm GABRIEL. I'm fully initialized and ready to interact with you and all your connected systems.");
            
        } catch (error) {
            console.error('❌ Initialization Error:', error);
            alert('Failed to initialize GABRIEL. Please check console for details.');
        }
    }
    
    setupEventListeners() {
        // Voice Chat Button
        document.getElementById('voice-btn').addEventListener('click', () => {
            this.toggleVoiceChat();
        });
        
        // Gesture Button
        document.getElementById('gesture-btn').addEventListener('click', () => {
            this.toggleGestures();
        });
        
        // Emotion Button
        document.getElementById('emotion-btn').addEventListener('click', () => {
            this.cycleEmotions();
        });
        
        // VR Button
        document.getElementById('vr-btn').addEventListener('click', () => {
            this.enterVR();
        });
        
        // Chat Input
        document.getElementById('send-btn').addEventListener('click', () => {
            this.sendMessage();
        });
        
        document.getElementById('chat-input').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });
    }
    
    async sendMessage() {
        const input = document.getElementById('chat-input');
        const message = input.value.trim();
        
        if (!message) return;
        
        // Add user message to chat
        this.addChatMessage('user', message);
        input.value = '';
        
        // Get AI response
        try {
            const response = await this.aiBrain.chat(message);
            
            // Add Gabriel's response to chat
            this.addChatMessage('gabriel', response);
            
            // Speak the response with lip-sync
            await this.speak(response);
            
            // Update emotion based on sentiment
            const emotion = this.aiBrain.analyzeEmotion(response);
            this.setEmotion(emotion);
            
        } catch (error) {
            console.error('Chat Error:', error);
            this.addChatMessage('gabriel', 'I apologize, but I encountered an issue processing your message.');
        }
    }
    
    addChatMessage(sender, text) {
        const messagesDiv = document.getElementById('chat-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;
        
        if (sender === 'gabriel') {
            messageDiv.innerHTML = `<strong>GABRIEL:</strong> ${text}`;
        } else {
            messageDiv.innerHTML = `<strong>You:</strong> ${text}`;
        }
        
        messagesDiv.appendChild(messageDiv);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }
    
    async speak(text) {
        if (!this.voiceSystem || !this.lipSync) return;
        
        try {
            // Generate phonemes for lip-sync
            const phonemes = this.lipSync.extractPhonemes(text);
            
            // Start lip-sync animation
            this.lipSync.animate(phonemes);
            
            // Speak using voice system
            await this.voiceSystem.speak(text);
            
        } catch (error) {
            console.error('Speech Error:', error);
        }
    }
    
    toggleVoiceChat() {
        const btn = document.getElementById('voice-btn');
        
        if (this.isListening) {
            this.voiceSystem.stopListening();
            btn.classList.remove('active');
            btn.textContent = '🎤 Voice Chat';
            this.isListening = false;
        } else {
            this.voiceSystem.startListening((transcript) => {
                // Handle voice input
                document.getElementById('chat-input').value = transcript;
                this.sendMessage();
            });
            btn.classList.add('active');
            btn.textContent = '🔴 Listening...';
            this.isListening = true;
        }
    }
    
    toggleGestures() {
        const btn = document.getElementById('gesture-btn');
        
        if (this.gestureSystem.isActive) {
            this.gestureSystem.stop();
            btn.classList.remove('active');
        } else {
            this.gestureSystem.start();
            btn.classList.add('active');
        }
    }
    
    cycleEmotions() {
        const emotions = ['calm', 'happy', 'excited', 'thinking', 'concerned'];
        const currentIndex = emotions.indexOf(this.currentEmotion);
        const nextIndex = (currentIndex + 1) % emotions.length;
        
        this.setEmotion(emotions[nextIndex]);
    }
    
    setEmotion(emotion) {
        this.currentEmotion = emotion;
        
        // Update avatar facial expression
        if (this.avatar) {
            this.avatar.setEmotion(emotion);
        }
        
        // Update UI
        const emotionStatus = document.getElementById('emotion-status');
        const emotionMap = {
            calm: { icon: '😌', class: 'emotion-calm' },
            happy: { icon: '😊', class: 'emotion-happy' },
            excited: { icon: '🤩', class: 'emotion-excited' },
            thinking: { icon: '🤔', class: 'emotion-thinking' },
            concerned: { icon: '😟', class: 'emotion-concerned' }
        };
        
        const emotionData = emotionMap[emotion];
        emotionStatus.innerHTML = `<span class="emotion-indicator ${emotionData.class}"></span>${emotionData.icon} ${emotion.charAt(0).toUpperCase() + emotion.slice(1)}`;
    }
    
    async enterVR() {
        if (!this.vrController) {
            alert('WebXR not supported in this browser');
            return;
        }
        
        try {
            await this.vrController.enterVR();
        } catch (error) {
            console.error('VR Error:', error);
            alert('Failed to enter VR mode: ' + error.message);
        }
    }
    
    animate() {
        requestAnimationFrame(() => this.animate());
        
        // Update avatar animation
        if (this.avatar) {
            this.avatar.update();
        }
        
        // Update physics
        if (this.physicsEngine) {
            this.physicsEngine.update();
        }
        
        // Update gesture detection
        if (this.gestureSystem && this.gestureSystem.isActive) {
            this.gestureSystem.update();
        }
        
        // Render scene
        if (this.avatar) {
            this.avatar.render();
        }
    }
    
    // NEW: Setup integrated voice commands for all systems
    setupIntegratedVoiceCommands() {
        if (!this.voiceSystem || !this.integrationHub) return;
        
        // Override voice recognition callback to include system commands
        const originalCallback = this.voiceSystem.onResult;
        this.voiceSystem.onResult = async (transcript) => {
            console.log(`[Voice] Received: "${transcript}"`);
            
            // Check if it's a system command
            if (this.isSystemCommand(transcript)) {
                await this.handleSystemCommand(transcript);
            } else {
                // Regular AI conversation
                if (originalCallback) {
                    originalCallback.call(this.voiceSystem, transcript);
                }
                await this.sendMessage(transcript);
            }
        };
    }
    
    isSystemCommand(text) {
        const systemKeywords = [
            'status', 'check', 'execute', 'create banner', 'stream', 'family', 
            'drive', 'query', 'health', 'optimize', 'noizylab', 'gdrive'
        ];
        
        const lower = text.toLowerCase();
        return systemKeywords.some(keyword => lower.includes(keyword));
    }
    
    async handleSystemCommand(transcript) {
        this.dashboard.logToConsole(`Processing: "${transcript}"`, 'info');
        
        const result = await this.integrationHub.processVoiceCommand(transcript);
        
        if (result.success) {
            const response = `Command executed successfully. ${JSON.stringify(result.result)}`;
            this.dashboard.logToConsole(response, 'success');
            await this.speak(response);
        } else {
            const error = `Command failed: ${result.error}`;
            this.dashboard.logToConsole(error, 'error');
            await this.speak(error);
        }
    }
}

// ============================================================================
// APPLICATION ENTRY POINT
// ============================================================================

// Initialize application when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    console.log('🎬 Starting GABRIEL Application...');
    window.gabrielApp = new GabrielApp();
});

// Handle window resize
window.addEventListener('resize', () => {
    if (window.gabrielApp && window.gabrielApp.avatar) {
        window.gabrielApp.avatar.handleResize();
    }
});

// Prevent context menu on canvas
document.addEventListener('contextmenu', (e) => {
    if (e.target.tagName === 'CANVAS') {
        e.preventDefault();
    }
});
