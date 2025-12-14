# MISSING APIs/SDKs RESEARCH FOR NOIZY.AI
# Research Status: September 18, 2025

## ✅ AVAILABLE OFFICIAL SDKS (Already Installed)
- **OpenAI** - ✅ Official Python SDK available (`openai`)
- **ElevenLabs** - ✅ Official Python SDK available (`elevenlabs`)
- **Anthropic** - ✅ Official Python SDK available (`anthropic`)
- **HuggingFace** - ✅ Official transformers SDK available (`transformers`)

## 🔍 RESEARCH NEEDED - APIs WITH UNKNOWN SDK STATUS

### Music Production Platforms
1. **LANDR** 
   - Status: ❓ No official Python SDK found
   - Alternative: REST API endpoints available 
   - Integration: Direct HTTP requests via `requests` library
   - Documentation: https://developers.landr.com/

2. **iZotope**
   - Status: ❓ No public API documented
   - Alternative: VST plugin integration via `python-vst`
   - Integration: Audio file processing workflows
   - Note: May require direct file processing approach

3. **Splice**
   - Status: ❓ Limited API documentation
   - Alternative: Web scraping or third-party wrappers
   - Integration: Sample download/search functionality
   - Note: Terms of service may restrict automated access

### AI Music Generation
4. **AIVA** 
   - Status: ❓ No official Python SDK
   - Alternative: REST API available for Pro subscribers
   - Integration: HTTP requests for composition generation
   - Documentation: https://creators.aiva.ai/api

5. **Amper Music** (now Shutterstock Music)
   - Status: ❌ Service discontinued/changed
   - Alternative: Look into Shutterstock Music API
   - Integration: May need to pivot to alternative platform

6. **Soundraw**
   - Status: ❓ No official Python SDK found
   - Alternative: REST API endpoints may exist
   - Integration: Direct HTTP requests
   - Note: Need to investigate API availability

### Advanced AI Platforms
7. **Stable Audio** (Stability AI)
   - Status: ✅ API available through Stability AI
   - Integration: Use `stability-sdk` or direct API calls
   - Documentation: https://platform.stability.ai/docs

8. **Meta MusicGen**
   - Status: ✅ Available via HuggingFace
   - Integration: `transformers` library already installed
   - Model: `facebook/musicgen-small`, `facebook/musicgen-medium`

9. **Google AudioLM**
   - Status: ❌ Not publicly available
   - Alternative: Google Cloud Speech/Audio APIs
   - Integration: Use Google Cloud Client Libraries

### Development Tools
10. **Windsurf**
    - Status: ❓ API availability unknown
    - Alternative: Similar to Cursor/Copilot integration
    - Integration: May require custom implementation
    - Note: Check if they offer developer APIs

### Audio Enhancement
11. **Dolby.io**
    - Status: ✅ Official REST API available
    - Integration: Direct HTTP requests
    - Documentation: https://docs.dolby.io/
    - SDK: Custom wrapper needed

12. **AssemblyAI**
    - Status: ✅ Official Python SDK available
    - Installation: `pip install assemblyai`
    - Integration: Speech recognition and audio intelligence

### Music Platform APIs  
13. **Spotify Web API**
    - Status: ✅ Official API available
    - Integration: `spotipy` library
    - Installation: `pip install spotipy`

14. **Apple Music API**
    - Status: ✅ MusicKit for developers
    - Integration: REST API with JWT authentication
    - Note: Requires Apple Developer account

15. **SoundCloud API**
    - Status: ✅ REST API available
    - Integration: `soundcloud-python` library
    - Installation: `pip install soundcloud`

16. **Bandcamp API**
    - Status: ❌ No official public API
    - Alternative: Web scraping (terms permitting)
    - Integration: Custom scraping solution

## 🚀 IMMEDIATE ACTION ITEMS

### Install Additional Available SDKs
```bash
pip install assemblyai spotipy soundcloud-python stability-sdk
```

### Custom Wrappers Needed For:
- LANDR REST API
- AIVA API  
- Dolby.io API
- Stable Audio API
- Soundraw (if API exists)

### Investigation Required:
- Windsurf developer API availability
- iZotope plugin integration methods
- Splice API terms and availability
- Alternative platforms for discontinued services

## 📋 INTEGRATION STRATEGY

### Phase 1: Easy Integrations (This Week)
- AssemblyAI - Audio intelligence
- Spotify API - Music data
- SoundCloud API - Creator platform
- Meta MusicGen - HuggingFace model
- Stable Audio - Stability AI API

### Phase 2: Custom API Wrappers (Next Week)  
- LANDR REST API wrapper
- AIVA API wrapper
- Dolby.io API wrapper
- Custom iZotope file processing

### Phase 3: Advanced Integrations (Following Week)
- Apple Music API (requires dev account)
- Windsurf integration (if available)
- Alternative platforms research
- Custom audio processing pipelines

## 🎯 SUCCESS METRICS
- **Target**: 15+ AI engines integrated
- **Current**: 4 official SDKs installed
- **Remaining**: 11 integrations to research/build
- **Priority**: Focus on platforms with confirmed APIs first

## 📝 NOTES
- Some platforms may require paid subscriptions for API access
- Rate limiting and API quotas need consideration
- Terms of service compliance crucial for all integrations
- Fallback strategies needed for unavailable services