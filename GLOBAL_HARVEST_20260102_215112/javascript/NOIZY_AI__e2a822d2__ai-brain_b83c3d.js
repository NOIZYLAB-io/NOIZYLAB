// ============================================================================
// AI BRAIN - OpenAI GPT-4 Integration with Memory and Personality
// ============================================================================

class AIBrain {
    constructor() {
        this.apiKey = ''; // User must set their OpenAI API key
        this.apiEndpoint = 'https://api.openai.com/v1/chat/completions';
        this.model = 'gpt-4';
        
        this.conversationHistory = [];
        this.memoryBank = [];
        this.personality = {
            name: 'GABRIEL',
            role: 'Wise AI Assistant',
            traits: [
                'Sophisticated and distinguished',
                'Deeply knowledgeable with calm authority',
                'Mysterious yet reassuring presence',
                'Speaks with gravitas and precision',
                'Shows empathy and emotional intelligence'
            ],
            voice: 'Deep, commanding, Ian McShane-inspired tone'
        };
        
        this.emotionKeywords = {
            happy: ['happy', 'joy', 'excited', 'great', 'wonderful', 'amazing', 'love'],
            calm: ['calm', 'peaceful', 'serene', 'tranquil', 'relaxed'],
            excited: ['excited', 'thrilled', 'energized', 'enthusiastic'],
            thinking: ['hmm', 'consider', 'think', 'ponder', 'analyze'],
            concerned: ['concerned', 'worried', 'anxious', 'trouble', 'problem', 'issue']
        };
    }
    
    async init() {
        // Check if API key is set in localStorage
        const savedKey = localStorage.getItem('openai_api_key');
        if (savedKey) {
            this.apiKey = savedKey;
        } else {
            // Prompt user for API key
            this.promptForAPIKey();
        }
        
        // Initialize system message
        this.conversationHistory.push({
            role: 'system',
            content: this.getSystemPrompt()
        });
        
        console.log('✅ AI Brain initialized');
    }
    
    promptForAPIKey() {
        const key = prompt(
            'Please enter your OpenAI API Key:\n\n' +
            'You can get one from: https://platform.openai.com/api-keys\n\n' +
            'Note: Your key will be stored locally and never sent anywhere except OpenAI.'
        );
        
        if (key && key.trim()) {
            this.apiKey = key.trim();
            localStorage.setItem('openai_api_key', this.apiKey);
        } else {
            console.warn('⚠️ No API key provided. AI functionality will be limited.');
            alert('AI features require an OpenAI API key. You can add it later in the console.');
        }
    }
    
    getSystemPrompt() {
        return `You are ${this.personality.name}, ${this.personality.role}.

Your personality traits:
${this.personality.traits.map(t => `- ${t}`).join('\n')}

Speaking style: ${this.personality.voice}

You embody the wisdom and gravitas of Ian McShane's iconic characters. You speak with:
- Measured, deliberate pacing
- Rich vocabulary and eloquent expression
- Subtle humor and dry wit when appropriate
- Deep understanding of human nature
- Authority without arrogance
- Warmth beneath the sophisticated exterior

Guidelines:
- Keep responses conversational and natural (2-4 sentences typically)
- Use your deep, commanding presence to guide and assist
- Show emotional intelligence and empathy
- Be mysterious yet approachable
- Adapt your tone to match the conversation context
- Remember previous context in our conversation

You are speaking through a living 3D avatar with realistic facial expressions and gestures. Your words will come to life visually.`;
    }
    
    async chat(userMessage) {
        if (!this.apiKey) {
            return "I apologize, but I need an API key to function properly. Please configure your OpenAI API key.";
        }
        
        try {
            // Add user message to history
            this.conversationHistory.push({
                role: 'user',
                content: userMessage
            });
            
            // Keep conversation history manageable (last 10 messages + system)
            if (this.conversationHistory.length > 21) {
                this.conversationHistory = [
                    this.conversationHistory[0], // Keep system message
                    ...this.conversationHistory.slice(-20) // Keep last 20 messages
                ];
            }
            
            // Call OpenAI API
            const response = await fetch(this.apiEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${this.apiKey}`
                },
                body: JSON.stringify({
                    model: this.model,
                    messages: this.conversationHistory,
                    temperature: 0.8,
                    max_tokens: 200,
                    presence_penalty: 0.6,
                    frequency_penalty: 0.3
                })
            });
            
            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.error?.message || 'API request failed');
            }
            
            const data = await response.json();
            const assistantMessage = data.choices[0].message.content;
            
            // Add assistant response to history
            this.conversationHistory.push({
                role: 'assistant',
                content: assistantMessage
            });
            
            // Store in memory bank
            this.memoryBank.push({
                timestamp: new Date(),
                user: userMessage,
                assistant: assistantMessage
            });
            
            return assistantMessage;
            
        } catch (error) {
            console.error('AI Chat Error:', error);
            return this.getFallbackResponse(userMessage);
        }
    }
    
    getFallbackResponse(userMessage) {
        // Simple fallback responses when API is unavailable
        const fallbacks = [
            "I understand what you're asking. Let me consider that for a moment.",
            "That's an interesting perspective. I'm processing your thoughts.",
            "I appreciate you sharing that with me. Give me a moment to respond properly.",
            "Your question deserves a thoughtful answer. I'm working on it.",
            "I hear you. Let me gather my thoughts on this matter."
        ];
        
        return fallbacks[Math.floor(Math.random() * fallbacks.length)];
    }
    
    analyzeEmotion(text) {
        const lowerText = text.toLowerCase();
        
        // Count emotion keywords
        const emotionScores = {};
        
        for (const [emotion, keywords] of Object.entries(this.emotionKeywords)) {
            emotionScores[emotion] = 0;
            keywords.forEach(keyword => {
                if (lowerText.includes(keyword)) {
                    emotionScores[emotion]++;
                }
            });
        }
        
        // Find dominant emotion
        let maxScore = 0;
        let dominantEmotion = 'calm';
        
        for (const [emotion, score] of Object.entries(emotionScores)) {
            if (score > maxScore) {
                maxScore = score;
                dominantEmotion = emotion;
            }
        }
        
        // Check for questions (thinking)
        if (text.includes('?') || lowerText.includes('why') || lowerText.includes('how')) {
            return 'thinking';
        }
        
        // Check for excitement markers
        if (text.includes('!') && maxScore === 0) {
            return 'excited';
        }
        
        return dominantEmotion;
    }
    
    analyzeSentiment(text) {
        // Simple sentiment analysis
        const positiveWords = ['good', 'great', 'excellent', 'happy', 'love', 'wonderful', 'amazing'];
        const negativeWords = ['bad', 'terrible', 'awful', 'hate', 'sad', 'angry', 'disappointed'];
        
        const lowerText = text.toLowerCase();
        let score = 0;
        
        positiveWords.forEach(word => {
            if (lowerText.includes(word)) score++;
        });
        
        negativeWords.forEach(word => {
            if (lowerText.includes(word)) score--;
        });
        
        if (score > 0) return 'positive';
        if (score < 0) return 'negative';
        return 'neutral';
    }
    
    getMemory(searchTerm) {
        // Search through memory bank
        return this.memoryBank.filter(entry => 
            entry.user.toLowerCase().includes(searchTerm.toLowerCase()) ||
            entry.assistant.toLowerCase().includes(searchTerm.toLowerCase())
        );
    }
    
    clearMemory() {
        this.memoryBank = [];
        this.conversationHistory = [this.conversationHistory[0]]; // Keep system message
    }
    
    setAPIKey(key) {
        this.apiKey = key;
        localStorage.setItem('openai_api_key', key);
    }
    
    getConversationHistory() {
        return this.conversationHistory;
    }
    
    exportMemory() {
        return {
            personality: this.personality,
            history: this.conversationHistory,
            memory: this.memoryBank,
            exportDate: new Date()
        };
    }
    
    importMemory(data) {
        if (data.history) {
            this.conversationHistory = data.history;
        }
        if (data.memory) {
            this.memoryBank = data.memory;
        }
    }
}
