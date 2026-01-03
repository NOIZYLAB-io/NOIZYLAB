// ============================================================================
// VOICE SYSTEM - Speech Recognition and Synthesis
// ============================================================================

class VoiceSystem {
    constructor() {
        this.recognition = null;
        this.synthesis = window.speechSynthesis;
        this.isListening = false;
        this.selectedVoice = null;
        
        // Voice preferences
        this.voicePreferences = {
            pitch: 0.8,
            rate: 0.9,
            volume: 1.0,
            preferredVoice: 'deep', // Look for deep male voice
        };
    }
    
    async init() {
        // Initialize Speech Recognition
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            this.recognition = new SpeechRecognition();
            
            this.recognition.continuous = false;
            this.recognition.interimResults = false;
            this.recognition.lang = 'en-US';
            
            console.log('✅ Speech Recognition initialized');
        } else {
            console.warn('⚠️ Speech Recognition not supported in this browser');
        }
        
        // Initialize Speech Synthesis
        if (this.synthesis) {
            // Wait for voices to load
            await this.loadVoices();
            console.log('✅ Speech Synthesis initialized');
        } else {
            console.warn('⚠️ Speech Synthesis not supported in this browser');
        }
    }
    
    async loadVoices() {
        return new Promise((resolve) => {
            const voices = this.synthesis.getVoices();
            
            if (voices.length > 0) {
                this.selectBestVoice(voices);
                resolve();
            } else {
                // Wait for voices to load
                this.synthesis.addEventListener('voiceschanged', () => {
                    const voices = this.synthesis.getVoices();
                    this.selectBestVoice(voices);
                    resolve();
                });
            }
        });
    }
    
    selectBestVoice(voices) {
        // Try to find a deep male voice
        const preferences = [
            'Daniel', // macOS deep voice
            'Alex', // macOS alternative
            'Google UK English Male',
            'Microsoft David',
            'Microsoft Mark'
        ];
        
        for (const pref of preferences) {
            const voice = voices.find(v => v.name.includes(pref));
            if (voice) {
                this.selectedVoice = voice;
                console.log('Selected voice:', voice.name);
                return;
            }
        }
        
        // Fallback: any male English voice
        const maleVoice = voices.find(v => 
            v.lang.startsWith('en') && 
            (v.name.toLowerCase().includes('male') || v.name.toLowerCase().includes('david') || v.name.toLowerCase().includes('mark'))
        );
        
        if (maleVoice) {
            this.selectedVoice = maleVoice;
        } else {
            // Last resort: first English voice
            this.selectedVoice = voices.find(v => v.lang.startsWith('en')) || voices[0];
        }
        
        console.log('Selected voice:', this.selectedVoice?.name || 'Default');
    }
    
    speak(text) {
        return new Promise((resolve, reject) => {
            if (!this.synthesis) {
                reject(new Error('Speech synthesis not available'));
                return;
            }
            
            // Cancel any ongoing speech
            this.synthesis.cancel();
            
            const utterance = new SpeechSynthesisUtterance(text);
            
            // Apply voice settings
            if (this.selectedVoice) {
                utterance.voice = this.selectedVoice;
            }
            utterance.pitch = this.voicePreferences.pitch;
            utterance.rate = this.voicePreferences.rate;
            utterance.volume = this.voicePreferences.volume;
            
            // Event handlers
            utterance.onend = () => {
                console.log('Speech finished');
                resolve();
            };
            
            utterance.onerror = (error) => {
                console.error('Speech error:', error);
                reject(error);
            };
            
            // Speak
            this.synthesis.speak(utterance);
        });
    }
    
    startListening(onResult) {
        if (!this.recognition) {
            alert('Speech recognition not supported in this browser');
            return;
        }
        
        if (this.isListening) {
            return;
        }
        
        this.isListening = true;
        
        this.recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            console.log('Heard:', transcript);
            
            if (onResult) {
                onResult(transcript);
            }
            
            this.isListening = false;
        };
        
        this.recognition.onerror = (event) => {
            console.error('Recognition error:', event.error);
            this.isListening = false;
        };
        
        this.recognition.onend = () => {
            this.isListening = false;
        };
        
        try {
            this.recognition.start();
            console.log('Listening...');
        } catch (error) {
            console.error('Failed to start recognition:', error);
            this.isListening = false;
        }
    }
    
    stopListening() {
        if (this.recognition && this.isListening) {
            this.recognition.stop();
            this.isListening = false;
        }
    }
    
    stopSpeaking() {
        if (this.synthesis) {
            this.synthesis.cancel();
        }
    }
    
    setVoiceSettings(settings) {
        if (settings.pitch !== undefined) {
            this.voicePreferences.pitch = Math.max(0, Math.min(2, settings.pitch));
        }
        if (settings.rate !== undefined) {
            this.voicePreferences.rate = Math.max(0.1, Math.min(10, settings.rate));
        }
        if (settings.volume !== undefined) {
            this.voicePreferences.volume = Math.max(0, Math.min(1, settings.volume));
        }
    }
    
    getAvailableVoices() {
        return this.synthesis ? this.synthesis.getVoices() : [];
    }
    
    setVoice(voiceName) {
        const voices = this.getAvailableVoices();
        const voice = voices.find(v => v.name === voiceName);
        
        if (voice) {
            this.selectedVoice = voice;
            return true;
        }
        
        return false;
    }
    
    // Advanced: Use ElevenLabs API for ultra-realistic voice (requires API key)
    async speakWithElevenLabs(text, apiKey) {
        if (!apiKey) {
            throw new Error('ElevenLabs API key required');
        }
        
        const voiceId = 'pNInz6obpgDQGcFmaJgB'; // Adam - deep, authoritative voice
        const url = `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;
        
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Accept': 'audio/mpeg',
                    'Content-Type': 'application/json',
                    'xi-api-key': apiKey
                },
                body: JSON.stringify({
                    text: text,
                    model_id: 'eleven_monolingual_v1',
                    voice_settings: {
                        stability: 0.75,
                        similarity_boost: 0.75
                    }
                })
            });
            
            if (!response.ok) {
                throw new Error('ElevenLabs API request failed');
            }
            
            const audioBlob = await response.blob();
            const audioUrl = URL.createObjectURL(audioBlob);
            const audio = new Audio(audioUrl);
            
            return new Promise((resolve, reject) => {
                audio.onended = resolve;
                audio.onerror = reject;
                audio.play();
            });
            
        } catch (error) {
            console.error('ElevenLabs error:', error);
            // Fallback to Web Speech API
            return this.speak(text);
        }
    }
    
    // Test audio with different settings
    test(testText = "Hello, I am GABRIEL. This is a test of my voice synthesis system.") {
        console.log('Testing voice with text:', testText);
        this.speak(testText);
    }
}
