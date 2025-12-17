# 🚀 GABRIEL Web Avatar - Quick Start Guide

## Your Living AI Avatar with Three.js r128 is Ready!

The complete web-based GABRIEL system has been built with all features from your vision:

### ✅ What's Included

**Core Systems:**
- 🎨 **Three.js r128** 3D rendering with advanced lighting
- 🧠 **OpenAI GPT-4** AI brain with personality
- 🎤 **Voice I/O** Web Speech API + ElevenLabs support
- 👄 **Lip-Sync** Real-time phoneme-to-viseme mapping
- 👋 **Gestures** Camera-based hand tracking
- ⚡ **Physics** Hair & cloth simulation (Verlet integration)
- 🥽 **WebXR** VR/AR immersive mode

**Files Created:**
```
WebAvatar/
├── index.html              # Main web app with modern UI
├── js/
│   ├── main.js            # Application controller
│   ├── avatar.js          # Three.js 3D rendering (450 lines)
│   ├── ai-brain.js        # OpenAI GPT-4 integration (350 lines)
│   ├── voice-system.js    # Speech recognition & synthesis (280 lines)
│   ├── lip-sync.js        # Phoneme animation engine (350 lines)
│   ├── gestures.js        # Hand tracking system (320 lines)
│   ├── physics.js         # Particle simulation (380 lines)
│   └── webxr.js           # VR/AR controller (310 lines)
├── models/                # Place your GLB avatar model here
└── assets/                # Additional resources
```

---

## 🎯 Quick Start (30 Seconds)

### Step 1: Start Local Server
```bash
cd /Users/rsp_ms/GABRIEL/WebAvatar
python3 -m http.server 8000
```

### Step 2: Open in Browser
Navigate to: **http://localhost:8000**

### Step 3: Enter OpenAI API Key
- You'll be prompted for your OpenAI API key on first run
- Get one at: https://platform.openai.com/api-keys
- Key is stored in browser localStorage for future sessions

### Step 4: Start Chatting!
- Type in chat box or click "🎤 Voice Chat"
- Watch GABRIEL respond with emotions and expressions
- Try "👋 Gestures" for hand tracking
- Click "🥽 Enter VR" for immersive mode

---

## 🎨 Features In Action

### **AI Conversations**
GABRIEL uses GPT-4 with a commanding personality inspired by your vision:
- Confident and authoritative voice
- Emotional intelligence and memory
- Context-aware responses
- Natural conversation flow

### **Emotional Expressions**
6 emotion states with smooth transitions:
- 😌 Calm (default)
- 😊 Happy
- 🤩 Excited
- 🤔 Thinking
- 😟 Concerned
- 😲 Surprised

### **Voice System**
- **Input:** Web Speech Recognition (built-in browser)
- **Output:** 
  - Web Speech Synthesis (free, instant)
  - ElevenLabs API (premium, ultra-realistic)
- Deep voice preference (Daniel, Alex, Google UK English Male)

### **Lip-Sync Animation**
Real-time phoneme mapping:
```
Text → Phonemes → BlendShapes → Avatar Mouth
"Hello" → [H, EH, L, OW] → mouthShapes → Animated
```

### **Hand Gestures**
Camera-based tracking recognizes:
- 👋 Wave
- 👆 Point
- 👍 Thumbs up
- ✋ Open hand
- ✊ Fist

### **Physics Simulation**
- **Hair:** 50 strands × 8 particles = 400 simulated points
- **Cloth:** 10×10 grid = 100 vertices
- **Forces:** Gravity, wind, collision
- **Algorithm:** Verlet integration with constraint satisfaction

---

## 🔧 Configuration

### Add Your Avatar Model
1. Export your 3D character as `.glb` format
2. Name it `gabriel_avatar.glb`
3. Place in `WebAvatar/models/` folder
4. Refresh browser - model loads automatically
5. **Fallback:** Stylized placeholder avatar renders if no model found

### API Keys

**OpenAI (Required):**
- Get key: https://platform.openai.com/api-keys
- Stored in: Browser localStorage
- Cost: ~$0.002 per conversation message

**ElevenLabs (Optional):**
- Get key: https://elevenlabs.io
- Add to `voice-system.js` line 10
- Premium ultra-realistic voice

### Customize Personality

Edit `ai-brain.js` lines 18-38 to change GABRIEL's character:
```javascript
this.systemPrompt = `You are GABRIEL...
[Your custom personality here]
`;
```

---

## 🎮 Controls & Interaction

### **Chat Interface** (Bottom Right)
- Type messages in input box
- Press Enter or click → button
- View conversation history
- Auto-scroll to latest message

### **Voice Chat** (Bottom Center)
- Click "🎤 Voice Chat" to start listening
- Speak your message
- GABRIEL responds with voice
- Real-time lip-sync animation

### **Gesture Control** (Bottom Center)
- Click "👋 Gestures" to enable camera
- Allow camera permission
- Perform hand gestures
- Avatar reacts in real-time

### **Emotion Selector** (Bottom Center)
- Click "😊 Emotions" for menu
- Select from 6 emotion states
- Watch avatar facial expressions change
- Emotion auto-detected from AI responses

### **VR Mode** (Bottom Left)
- Click "🥽 Enter VR" with VR headset connected
- Immersive full-presence experience
- Controller-based interaction
- Hand tracking support (Quest 2+)

### **Camera Controls**
- **Left Mouse:** Rotate view
- **Right Mouse:** Pan view
- **Scroll Wheel:** Zoom in/out
- **Target:** Avatar head level

---

## 🌐 Browser Requirements

### **Recommended:**
- Chrome 90+ or Edge 90+
- Firefox 88+
- Safari 14.1+

### **Required Features:**
- ✅ WebGL 2.0
- ✅ ES6 JavaScript
- ✅ Web Speech API (voice)
- ✅ MediaDevices API (camera)
- ✅ WebXR Device API (VR)

### **Check Compatibility:**
```javascript
// Open browser console (F12) and run:
console.log('WebGL:', !!document.createElement('canvas').getContext('webgl2'));
console.log('WebXR:', 'xr' in navigator);
console.log('Speech:', 'speechSynthesis' in window);
```

---

## 📊 Performance Optimization

### **High-End Systems** (RTX 3070+, 16GB RAM)
Default settings work perfectly:
- 1000 particles
- 2048×2048 shadow maps
- 60 FPS target

### **Mid-Range Systems** (GTX 1660, 8GB RAM)
Edit `avatar.js`:
```javascript
// Line 61: Reduce particles
const particleCount = 500; // Was: 1000

// Line 76: Lower shadow quality
this.lights.key.shadow.mapSize.width = 1024; // Was: 2048
```

### **Low-End Systems** (Integrated Graphics)
```javascript
// Disable shadows (avatar.js line 72)
this.renderer.shadowMap.enabled = false;

// Reduce particles (avatar.js line 61)
const particleCount = 200;

// Lower resolution (avatar.js line 68)
this.renderer.setPixelRatio(1); // Was: Math.min(devicePixelRatio, 2)
```

---

## 🐛 Troubleshooting

### **Problem:** "Avatar not loading"
**Solutions:**
- Check browser console (F12) for errors
- Verify `index.html` loads all 8 JS files
- Clear browser cache (Ctrl+Shift+R)
- Check Three.js CDN connection

### **Problem:** "AI not responding"
**Solutions:**
- Verify OpenAI API key is correct
- Check API key has credits: https://platform.openai.com/usage
- Open Network tab (F12) to see API errors
- Try clearing localStorage: `localStorage.removeItem('openai_api_key')`

### **Problem:** "Voice not working"
**Solutions:**
- Check microphone permissions in browser
- Test: https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API
- Firefox requires `media.webspeech.recognition.enable` = true in about:config
- Safari requires HTTPS or localhost

### **Problem:** "Gestures not detecting"
**Solutions:**
- Allow camera permission when prompted
- Ensure good lighting
- Position hand 1-2 feet from camera
- MediaPipe library loads from CDN - check network

### **Problem:** "VR button not appearing"
**Solutions:**
- Connect VR headset first
- Chrome requires WebXR flag enabled
- Check: `chrome://flags/#webxr`
- Oculus Browser recommended for Quest

---

## 🚀 Advanced Usage

### **Memory Bank Export**
Save conversation history:
```javascript
// Open browser console (F12)
const memory = app.aiBrain.exportMemory();
console.log(memory);
// Copy and save to file
```

### **Custom Animations**
Add your own avatar animations:
```javascript
// In avatar.js, add to loadAvatar() method
if (gltf.animations) {
    const walkAction = this.mixer.clipAction(gltf.animations[0]);
    walkAction.play();
}
```

### **Gesture Training**
Add custom gestures in `gestures.js`:
```javascript
// Line 180, add to classifyGesture()
if (/* your detection logic */) {
    return 'yourGesture';
}
```

---

## 📱 Mobile Support

### **iOS Safari:**
- ✅ 3D rendering works
- ✅ Touch controls supported
- ⚠️ Voice input requires user gesture
- ⚠️ Camera requires HTTPS

### **Android Chrome:**
- ✅ Full feature support
- ✅ WebXR AR mode available
- ✅ Voice and camera work
- 🎯 Best mobile experience

### **Mobile Optimizations:**
```javascript
// Detect mobile (main.js)
const isMobile = /iPhone|iPad|Android/i.test(navigator.userAgent);
if (isMobile) {
    // Reduce particles, disable shadows, etc.
}
```

---

## 🌟 Next Steps

### **Enhance Your Avatar:**
1. Create custom 3D model in Blender/Maya
2. Add blend shapes for expressions
3. Export as GLB with animations
4. Replace `gabriel_avatar.glb`

### **Upgrade Voice:**
1. Sign up for ElevenLabs
2. Clone your voice or choose pre-made
3. Add API key to `voice-system.js`
4. Ultra-realistic speech output

### **Add More Features:**
- Emotion detection from user's camera
- Background environment scenes
- Multiple avatar models to choose from
- Save/load conversation transcripts
- Multi-language support

---

## 📚 Resources

### **Documentation:**
- Three.js: https://threejs.org/docs/
- OpenAI API: https://platform.openai.com/docs
- Web Speech: https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API
- WebXR: https://immersive-web.github.io/webxr/

### **3D Models:**
- Ready Player Me: https://readyplayer.me (free avatars)
- Mixamo: https://www.mixamo.com (animations)
- Sketchfab: https://sketchfab.com (models)

### **Voice Services:**
- ElevenLabs: https://elevenlabs.io (premium)
- Google Cloud TTS: https://cloud.google.com/text-to-speech
- Azure Speech: https://azure.microsoft.com/en-us/products/cognitive-services/text-to-speech

---

## 🎉 You're All Set!

Your GABRIEL Living Avatar is ready to go. The system you envisioned - a complete 3D living avatar with AI, voice, gestures, physics, and VR - is fully implemented with **3+++ quality**.

**Start now:**
```bash
cd /Users/rsp_ms/GABRIEL/WebAvatar
python3 -m http.server 8000
# Open http://localhost:8000
```

**Questions?** Check the console log (F12) for detailed system status.

**Enjoy your living avatar! 🚀**
