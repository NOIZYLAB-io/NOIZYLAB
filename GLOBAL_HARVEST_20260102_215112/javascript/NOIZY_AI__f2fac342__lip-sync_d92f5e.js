// ============================================================================
// LIP-SYNC ENGINE - Real-time Phoneme to BlendShape Mapping
// ============================================================================

class LipSyncEngine {
    constructor(avatar) {
        this.avatar = avatar;
        this.isAnimating = false;
        this.currentAnimation = null;
        
        // Phoneme to BlendShape mapping
        // Based on standard visemes for realistic lip movement
        this.phonemeMap = {
            // Vowels
            'a': 'mouthOpen',
            'e': 'mouthSmile',
            'i': 'mouthSmile',
            'o': 'mouthRound',
            'u': 'mouthRound',
            
            // Consonants
            'b': 'mouthClosed',
            'p': 'mouthClosed',
            'm': 'mouthClosed',
            'f': 'mouthLowerLipBite',
            'v': 'mouthLowerLipBite',
            'th': 'mouthTongueOut',
            'd': 'mouthSmile',
            't': 'mouthSmile',
            'n': 'mouthSmile',
            'l': 'mouthSmile',
            'r': 'mouthRound',
            's': 'mouthSmile',
            'z': 'mouthSmile',
            'sh': 'mouthPucker',
            'ch': 'mouthPucker',
            'j': 'mouthPucker',
            'k': 'mouthOpen',
            'g': 'mouthOpen',
            'w': 'mouthRound',
            'y': 'mouthSmile',
            
            // Default
            'neutral': 'neutral'
        };
        
        // Viseme intensity mapping
        this.visemeIntensity = {
            'mouthOpen': 0.8,
            'mouthSmile': 0.6,
            'mouthRound': 0.7,
            'mouthClosed': 0.3,
            'mouthLowerLipBite': 0.5,
            'mouthTongueOut': 0.4,
            'mouthPucker': 0.6,
            'neutral': 0.0
        };
        
        // Timing constants
        this.phonemeDuration = 80; // ms per phoneme
        this.blendSpeed = 0.2; // Smoothing factor
    }
    
    extractPhonemes(text) {
        // Convert text to phoneme sequence
        // This is a simplified version - for production, use a proper TTS phoneme API
        const words = text.toLowerCase().split(/\s+/);
        const phonemes = [];
        
        words.forEach(word => {
            // Split word into characters and map to phonemes
            for (let i = 0; i < word.length; i++) {
                const char = word[i];
                
                // Check for digraphs (two-character phonemes)
                if (i < word.length - 1) {
                    const digraph = char + word[i + 1];
                    if (this.phonemeMap[digraph]) {
                        phonemes.push(digraph);
                        i++; // Skip next character
                        continue;
                    }
                }
                
                // Single character phoneme
                if (this.phonemeMap[char]) {
                    phonemes.push(char);
                } else {
                    phonemes.push('neutral');
                }
            }
            
            // Add pause between words
            phonemes.push('neutral');
        });
        
        return phonemes;
    }
    
    animate(phonemes) {
        if (this.isAnimating) {
            this.stop();
        }
        
        this.isAnimating = true;
        let currentIndex = 0;
        
        const animateNextPhoneme = () => {
            if (!this.isAnimating || currentIndex >= phonemes.length) {
                this.reset();
                return;
            }
            
            const phoneme = phonemes[currentIndex];
            const blendShape = this.phonemeMap[phoneme] || 'neutral';
            const intensity = this.visemeIntensity[blendShape] || 0.0;
            
            // Apply blend shape
            this.applyBlendShape(blendShape, intensity);
            
            currentIndex++;
            
            // Schedule next phoneme
            this.currentAnimation = setTimeout(animateNextPhoneme, this.phonemeDuration);
        };
        
        animateNextPhoneme();
    }
    
    applyBlendShape(shapeName, intensity) {
        if (!this.avatar || !this.avatar.avatar) return;
        
        // Reset all mouth shapes first
        this.resetMouthShapes();
        
        // Apply the target shape
        this.avatar.applyBlendShape(shapeName, intensity);
        
        // Add subtle jaw movement for more realism
        if (shapeName === 'mouthOpen') {
            this.avatar.applyBlendShape('jawOpen', intensity * 0.5);
        }
    }
    
    resetMouthShapes() {
        const mouthShapes = [
            'mouthOpen',
            'mouthSmile',
            'mouthRound',
            'mouthClosed',
            'mouthLowerLipBite',
            'mouthTongueOut',
            'mouthPucker',
            'jawOpen'
        ];
        
        mouthShapes.forEach(shape => {
            this.avatar.applyBlendShape(shape, 0);
        });
    }
    
    stop() {
        this.isAnimating = false;
        if (this.currentAnimation) {
            clearTimeout(this.currentAnimation);
            this.currentAnimation = null;
        }
    }
    
    reset() {
        this.stop();
        this.resetMouthShapes();
    }
    
    // Advanced: Sync with actual audio waveform
    syncWithAudio(audioElement, phonemes) {
        if (!audioElement) return;
        
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const analyser = audioContext.createAnalyser();
        const source = audioContext.createMediaElementSource(audioElement);
        
        source.connect(analyser);
        analyser.connect(audioContext.destination);
        
        analyser.fftSize = 256;
        const bufferLength = analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);
        
        let phonemeIndex = 0;
        const phonemeInterval = (audioElement.duration / phonemes.length) * 1000;
        
        const updateLipSync = () => {
            if (!this.isAnimating) return;
            
            analyser.getByteFrequencyData(dataArray);
            
            // Calculate average volume
            const average = dataArray.reduce((a, b) => a + b) / bufferLength;
            const normalizedVolume = average / 255;
            
            // Update phoneme based on time
            const currentPhonemeIndex = Math.floor((audioElement.currentTime * 1000) / phonemeInterval);
            
            if (currentPhonemeIndex !== phonemeIndex && currentPhonemeIndex < phonemes.length) {
                phonemeIndex = currentPhonemeIndex;
                const phoneme = phonemes[phonemeIndex];
                const blendShape = this.phonemeMap[phoneme] || 'neutral';
                const intensity = this.visemeIntensity[blendShape] * normalizedVolume;
                
                this.applyBlendShape(blendShape, intensity);
            }
            
            requestAnimationFrame(updateLipSync);
        };
        
        audioElement.play();
        this.isAnimating = true;
        updateLipSync();
        
        audioElement.addEventListener('ended', () => {
            this.reset();
        });
    }
    
    // Generate phoneme timing data for precise lip-sync
    generateTimingData(text, duration) {
        const phonemes = this.extractPhonemes(text);
        const timePerPhoneme = duration / phonemes.length;
        
        const timingData = phonemes.map((phoneme, index) => ({
            phoneme: phoneme,
            blendShape: this.phonemeMap[phoneme] || 'neutral',
            intensity: this.visemeIntensity[this.phonemeMap[phoneme]] || 0.0,
            startTime: index * timePerPhoneme,
            duration: timePerPhoneme
        }));
        
        return timingData;
    }
    
    // Apply timing data for frame-accurate lip-sync
    animateWithTiming(timingData, onComplete) {
        if (this.isAnimating) {
            this.stop();
        }
        
        this.isAnimating = true;
        const startTime = performance.now();
        
        const animate = (currentTime) => {
            if (!this.isAnimating) {
                if (onComplete) onComplete();
                return;
            }
            
            const elapsed = currentTime - startTime;
            
            // Find current phoneme
            const currentData = timingData.find(data => 
                elapsed >= data.startTime && elapsed < data.startTime + data.duration
            );
            
            if (currentData) {
                this.applyBlendShape(currentData.blendShape, currentData.intensity);
            }
            
            // Check if animation is complete
            const lastData = timingData[timingData.length - 1];
            if (elapsed >= lastData.startTime + lastData.duration) {
                this.reset();
                if (onComplete) onComplete();
                return;
            }
            
            requestAnimationFrame(animate);
        };
        
        requestAnimationFrame(animate);
    }
}
