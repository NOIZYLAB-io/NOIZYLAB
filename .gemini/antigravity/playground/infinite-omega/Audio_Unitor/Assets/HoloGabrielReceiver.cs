using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

// ==============================================================================
// 🥽 HOLO-GABRIEL RECEIVER (Unity C#)
// ==============================================================================
// Attaches to the Gabriel Avatar in Unity.
// Listens for UDP Packets from M2 Ultra (Gabriel Core).
// Controls: Color (Emotion), Animation (Speaking).

[RequireComponent(typeof(Animator))]
public class HoloGabrielReceiver : MonoBehaviour
{
    [Header("Network Settings")]
    public int port = 9000;
    public bool showDebug = true;

    [Header("Visuals")]
    public Renderer coreRenderer;
    public Color colorIdle = Color.green;
    public Color colorThinking = Color.blue;
    public Color colorCreative = Color.yellow;
    public Color colorError = Color.red;

    // Private Network
    private UdpClient client;
    private Thread receiveThread;
    private bool isRunning;

    // State Data
    private string currentEmotion = "neutral";
    private bool isSpeaking = false;
    private float lastTimestamp = 0f;

    // Animator
    private Animator animator;

    void Start()
    {
        animator = GetComponent<Animator>();
        StartUDP();
    }

    void Update()
    {
        // Update Visuals on Main Thread
        UpdateColor();
        UpdateAnimation();
    }

    // --------------------------------------------------------------------------
    // 📡 UDP LISTENER
    // --------------------------------------------------------------------------
    private void StartUDP()
    {
        isRunning = true;
        receiveThread = new Thread(new ThreadStart(ReceiveData));
        receiveThread.IsBackground = true;
        receiveThread.Start();
        if (showDebug) Debug.Log("Holo-Gabriel: Listening on Port " + port);
    }

    private void ReceiveData()
    {
        client = new UdpClient(port);
        IPEndPoint anyIP = new IPEndPoint(IPAddress.Any, 0);

        while (isRunning)
        {
            try
            {
                byte[] data = client.Receive(ref anyIP);
                string json = Encoding.UTF8.GetString(data);
                ParseState(json);
            }
            catch (System.Exception e)
            {
                if (showDebug) Debug.LogWarning("UDP Error: " + e.Message);
            }
        }
    }

    [System.Serializable]
    public class AvatarState
    {
        public string e; // emotion
        public bool s;   // speaking
        public float t;  // timestamp
    }

    private void ParseState(string json)
    {
        try
        {
            AvatarState state = JsonUtility.FromJson<AvatarState>(json);
            
            // Sync logic
            if (state.t > lastTimestamp)
            {
                currentEmotion = state.e;
                isSpeaking = state.s;
                lastTimestamp = state.t;
            }
        }
        catch { }
    }

    // --------------------------------------------------------------------------
    // 🎨 VISUAL UPDATE
    // --------------------------------------------------------------------------
    private void UpdateColor()
    {
        if (coreRenderer == null) return;

        Color targetColor = colorIdle;
        switch (currentEmotion)
        {
            case "processing": targetColor = colorThinking; break;
            case "creative": targetColor = colorCreative; break;
            case "error": targetColor = colorError; break;
            case "happy": targetColor = colorCreative; break; // Gold/Yellow
        }

        // Smooth Lerp
        coreRenderer.material.color = Color.Lerp(coreRenderer.material.color, targetColor, Time.deltaTime * 5f);
        coreRenderer.material.SetColor("_EmissionColor", coreRenderer.material.color * 2f); // Glow
    }

    private void UpdateAnimation()
    {
        if (animator == null) return;
        animator.SetBool("IsSpeaking", isSpeaking);
    }

    void OnApplicationQuit()
    {
        isRunning = false;
        if (client != null) client.Close();
        if (receiveThread != null) receiveThread.Abort();
    }
}
