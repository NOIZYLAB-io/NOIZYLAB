/*
 * ✨ GABRIEL AI BRIDGE - UNITY TO PYTHON INTEGRATION ✨
 * 
 * Bridges Unity 3D environment with GABRIEL's Python AI systems:
 * - Voice synthesis with Ian McShane tone
 * - Emotional AI and sentiment analysis
 * - Proactive assistance
 * - Real-time responses
 * 
 * Version: 1.0 ULTIMATE
 * Created: November 11, 2025
 */

using UnityEngine;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Gabriel.Ultimate
{
    public class GabrielAIBridge : MonoBehaviour
    {
        #region Configuration
        [Header("AI Server Settings")]
        [SerializeField] private string serverUrl = "http://localhost:8000";
        [SerializeField] private bool autoConnect = true;
        [SerializeField] private float connectionTimeout = 5.0f;

        [Header("Voice Settings")]
        [SerializeField] private AudioSource voiceAudioSource;
        [SerializeField] private bool enableVoicePlayback = true;
        [SerializeField] private float voiceVolume = 0.8f;

        [Header("Response Settings")]
        [SerializeField] private float maxResponseTime = 3.0f;
        [SerializeField] private bool cacheResponses = true;
        #endregion

        #region Private Variables
        private GabrielController controller;
        private HttpClient httpClient;
        private bool isConnected = false;
        private Queue<AIRequest> requestQueue;
        private Dictionary<string, string> responseCache;
        
        private class AIRequest
        {
            public string text;
            public Dictionary<string, object> context;
            public Action<AIResponse> callback;
        }

        private class AIResponse
        {
            public string response_text;
            public string emotion;
            public List<string> suggestions;
            public Dictionary<string, object> sentiment_analysis;
            public string voice_file;
        }
        #endregion

        #region Initialization
        public void Initialize(GabrielController controller)
        {
            this.controller = controller;
            
            // Setup HTTP client
            httpClient = new HttpClient();
            httpClient.Timeout = TimeSpan.FromSeconds(maxResponseTime);
            
            // Initialize queues
            requestQueue = new Queue<AIRequest>();
            responseCache = new Dictionary<string, string>();
            
            // Setup audio
            if (!voiceAudioSource)
            {
                voiceAudioSource = gameObject.AddComponent<AudioSource>();
            }
            voiceAudioSource.volume = voiceVolume;
            voiceAudioSource.spatialBlend = 0; // 2D sound
            
            if (autoConnect)
            {
                StartCoroutine(ConnectToAIServer());
            }
            
            Debug.Log("🤖 GABRIEL AI Bridge initialized");
        }

        private IEnumerator ConnectToAIServer()
        {
            Debug.Log($"🔌 Connecting to AI server at {serverUrl}...");
            
            float startTime = Time.time;
            bool connected = false;
            
            while (!connected && Time.time - startTime < connectionTimeout)
            {
                Task<bool> pingTask = PingServer();
                yield return new WaitUntil(() => pingTask.IsCompleted);
                
                if (pingTask.Result)
                {
                    connected = true;
                    isConnected = true;
                    Debug.Log("✅ Connected to GABRIEL AI server");
                    
                    // Initialize GABRIEL on server
                    yield return StartCoroutine(InitializeAISystem());
                }
                else
                {
                    yield return new WaitForSeconds(1.0f);
                }
            }
            
            if (!connected)
            {
                Debug.LogWarning("⚠️ Could not connect to AI server - running in offline mode");
                isConnected = false;
            }
        }

        private async Task<bool> PingServer()
        {
            try
            {
                var response = await httpClient.GetAsync($"{serverUrl}/health");
                return response.IsSuccessStatusCode;
            }
            catch (Exception)
            {
                return false;
            }
        }

        private IEnumerator InitializeAISystem()
        {
            var initData = new
            {
                mode = "ultimate_smooth",
                version = "2.0",
                smoothness = 10.0f,
                features = new[] { "voice", "emotion", "proactive", "cinematic" }
            };
            
            Task<string> task = PostRequest("/api/initialize", initData);
            yield return new WaitUntil(() => task.IsCompleted);
            
            if (task.IsCompletedSuccessfully)
            {
                Debug.Log($"✨ GABRIEL AI initialized: {task.Result}");
            }
        }
        #endregion

        #region Public API
        public void RequestAIResponse(string context)
        {
            if (string.IsNullOrEmpty(context)) return;
            
            var request = new AIRequest
            {
                text = context,
                context = BuildContextData(),
                callback = OnAIResponseReceived
            };
            
            requestQueue.Enqueue(request);
            StartCoroutine(ProcessRequestQueue());
        }

        public void UpdateContext(Dictionary<string, object> context)
        {
            if (!isConnected) return;
            
            StartCoroutine(SendContextUpdate(context));
        }

        public void OnEmotionChanged(string emotion)
        {
            if (!isConnected) return;
            
            var data = new { emotion = emotion };
            StartCoroutine(SendEmotionUpdate(data));
        }

        public void Speak(string text, string emotion = "calm")
        {
            if (!isConnected)
            {
                Debug.Log($"🎤 GABRIEL (offline): {text}");
                return;
            }
            
            StartCoroutine(SynthesizeAndPlaySpeech(text, emotion));
        }
        #endregion

        #region Request Processing
        private IEnumerator ProcessRequestQueue()
        {
            while (requestQueue.Count > 0)
            {
                AIRequest request = requestQueue.Dequeue();
                
                // Check cache first
                if (cacheResponses && responseCache.ContainsKey(request.text))
                {
                    string cachedResponse = responseCache[request.text];
                    var response = JsonConvert.DeserializeObject<AIResponse>(cachedResponse);
                    request.callback?.Invoke(response);
                    continue;
                }
                
                // Make API request
                var data = new
                {
                    text = request.text,
                    context = request.context
                };
                
                Task<string> task = PostRequest("/api/interact", data);
                yield return new WaitUntil(() => task.IsCompleted);
                
                if (task.IsCompletedSuccessfully)
                {
                    try
                    {
                        AIResponse response = JsonConvert.DeserializeObject<AIResponse>(task.Result);
                        
                        // Cache response
                        if (cacheResponses)
                        {
                            responseCache[request.text] = task.Result;
                        }
                        
                        // Invoke callback
                        request.callback?.Invoke(response);
                    }
                    catch (Exception ex)
                    {
                        Debug.LogError($"Failed to parse AI response: {ex.Message}");
                    }
                }
                
                yield return null;
            }
        }

        private Dictionary<string, object> BuildContextData()
        {
            if (!controller) return new Dictionary<string, object>();
            
            return new Dictionary<string, object>
            {
                { "position", controller.GetPosition() },
                { "is_moving", controller.IsMoving() },
                { "speed", controller.GetSpeed() },
                { "emotion", controller.GetCurrentEmotion() },
                { "timestamp", DateTime.Now.ToString("o") },
                { "environment", "Unity3D" }
            };
        }
        #endregion

        #region API Communication
        private async Task<string> PostRequest(string endpoint, object data)
        {
            try
            {
                string jsonData = JsonConvert.SerializeObject(data);
                var content = new StringContent(jsonData, Encoding.UTF8, "application/json");
                
                var response = await httpClient.PostAsync($"{serverUrl}{endpoint}", content);
                response.EnsureSuccessStatusCode();
                
                return await response.Content.ReadAsStringAsync();
            }
            catch (Exception ex)
            {
                Debug.LogError($"API request failed: {ex.Message}");
                return null;
            }
        }

        private async Task<byte[]> GetAudioData(string voiceFile)
        {
            try
            {
                var response = await httpClient.GetAsync($"{serverUrl}/api/voice/{voiceFile}");
                response.EnsureSuccessStatusCode();
                
                return await response.Content.ReadAsByteArrayAsync();
            }
            catch (Exception ex)
            {
                Debug.LogError($"Failed to get audio: {ex.Message}");
                return null;
            }
        }
        #endregion

        #region Voice Synthesis
        private IEnumerator SynthesizeAndPlaySpeech(string text, string emotion)
        {
            var data = new
            {
                text = text,
                emotion = emotion,
                voice_profile = "ian_mcshane"
            };
            
            Task<string> task = PostRequest("/api/synthesize", data);
            yield return new WaitUntil(() => task.IsCompleted);
            
            if (task.IsCompletedSuccessfully && enableVoicePlayback)
            {
                try
                {
                    var response = JsonConvert.DeserializeObject<AIResponse>(task.Result);
                    
                    if (!string.IsNullOrEmpty(response.voice_file))
                    {
                        yield return StartCoroutine(PlayVoiceAudio(response.voice_file));
                    }
                }
                catch (Exception ex)
                {
                    Debug.LogError($"Voice synthesis failed: {ex.Message}");
                }
            }
        }

        private IEnumerator PlayVoiceAudio(string voiceFile)
        {
            Task<byte[]> audioTask = GetAudioData(voiceFile);
            yield return new WaitUntil(() => audioTask.IsCompleted);
            
            if (audioTask.IsCompletedSuccessfully && audioTask.Result != null)
            {
                AudioClip clip = ConvertToAudioClip(audioTask.Result);
                
                if (clip)
                {
                    voiceAudioSource.clip = clip;
                    voiceAudioSource.Play();
                    
                    Debug.Log($"🎤 Playing GABRIEL voice: {voiceFile}");
                }
            }
        }

        private AudioClip ConvertToAudioClip(byte[] audioData)
        {
            // Note: This is a simplified version. In production, use proper WAV parsing
            // or use Unity's AudioClip.Create with PCM data
            
            try
            {
                // Create temporary file
                string tempPath = System.IO.Path.GetTempFileName() + ".wav";
                System.IO.File.WriteAllBytes(tempPath, audioData);
                
                // Load using UnityWebRequest (requires coroutine in real implementation)
                // For now, return null - implement proper audio loading
                
                Debug.LogWarning("Audio conversion needs full implementation");
                return null;
            }
            catch (Exception ex)
            {
                Debug.LogError($"Audio conversion failed: {ex.Message}");
                return null;
            }
        }
        #endregion

        #region Context Updates
        private IEnumerator SendContextUpdate(Dictionary<string, object> context)
        {
            var data = new { context = context };
            
            Task<string> task = PostRequest("/api/context", data);
            yield return new WaitUntil(() => task.IsCompleted);
            
            if (task.IsCompletedSuccessfully)
            {
                // Context updated successfully
            }
        }

        private IEnumerator SendEmotionUpdate(object data)
        {
            Task<string> task = PostRequest("/api/emotion", data);
            yield return new WaitUntil(() => task.IsCompleted);
        }
        #endregion

        #region Response Handling
        private void OnAIResponseReceived(AIResponse response)
        {
            if (response == null) return;
            
            // Update controller
            if (controller)
            {
                List<string> suggestions = response.suggestions ?? new List<string>();
                controller.OnAIResponse(response.response_text, response.emotion, suggestions);
            }
            
            // Play voice if available
            if (enableVoicePlayback && !string.IsNullOrEmpty(response.voice_file))
            {
                StartCoroutine(PlayVoiceAudio(response.voice_file));
            }
            
            // Log sentiment
            if (response.sentiment_analysis != null)
            {
                Debug.Log($"📊 Sentiment: {JsonConvert.SerializeObject(response.sentiment_analysis)}");
            }
        }
        #endregion

        #region Cleanup
        void OnDestroy()
        {
            httpClient?.Dispose();
        }
        #endregion
    }
}
