# ✨ GABRIEL ULTIMATE - UNITY 3D COMPLETE SETUP GUIDE ✨

## 🎮 COMPLETE UNITY IMPLEMENTATION

This guide provides everything needed to bring GABRIEL to life in Unity 3D with smooth animations, AI integration, and cinematic quality.

---

## 📋 TABLE OF CONTENTS

1. [Project Setup](#project-setup)
2. [Avatar Import](#avatar-import)
3. [Animator Controller Setup](#animator-controller-setup)
4. [Script Integration](#script-integration)
5. [AI Server Setup](#ai-server-setup)
6. [Scene Setup](#scene-setup)
7. [Testing & Deployment](#testing--deployment)

---

## 1. PROJECT SETUP

### Create New Unity Project

```bash
# Unity 2022.3 LTS or newer recommended
Unity Hub → New Project
Template: 3D (URP) Core
Project Name: GabrielUltimate3D
```

### Install Required Packages

Open **Window → Package Manager** and install:

- ✅ Universal Render Pipeline (URP)
- ✅ NavMesh Components
- ✅ Cinemachine
- ✅ Input System (New)
- ✅ Animation Rigging
- ✅ Post Processing

### Package Dependencies

Add to `Packages/manifest.json`:

```json
{
  "dependencies": {
    "com.unity.render-pipelines.universal": "14.0.8",
    "com.unity.ai.navigation": "1.1.5",
    "com.unity.cinemachine": "2.9.7",
    "com.unity.inputsystem": "1.7.0",
    "com.unity.animation.rigging": "1.3.1",
    "com.newtonsoft.json": "3.2.1"
  }
}
```

---

## 2. AVATAR IMPORT

### Option A: Custom GABRIEL Model (Blender)

1. **Export from Blender**:
   ```bash
   cd /Users/rsp_ms/GABRIEL/BlenderExport
   blender --background --python gabriel_blender_exporter.py
   ```

2. **Import to Unity**:
   - Copy `Gabriel_Ultimate.fbx` to `Assets/Models/`
   - Copy textures to `Assets/Models/Textures/`

3. **Configure Model**:
   - Select `Gabriel_Ultimate.fbx`
   - Inspector → Rig → Animation Type: **Humanoid**
   - Click **Configure** → Verify bone mapping
   - Apply changes

### Option B: Mixamo Character (Quick Start)

1. **Download from Mixamo**:
   - Go to https://www.mixamo.com
   - Select mature male character
   - Download as FBX for Unity
   - Download animations: Idle, Walk, Run, Wave, Thinking

2. **Import to Unity**:
   - Drag FBX files into `Assets/Models/`
   - Set Animation Type to **Humanoid**

### Material Setup

Create materials for:
- **Gabriel_Face**: Skin shader with subsurface scattering
- **Gabriel_Hair**: Anisotropic hair shader (silver)
- **Gabriel_Suit**: Fabric shader (dark charcoal)
- **Gabriel_Cufflinks**: Emission shader (golden glow)

---

## 3. ANIMATOR CONTROLLER SETUP

### Create Animator Controller

1. **Create Controller**:
   - `Assets → Create → Animator Controller`
   - Name: `GabrielAnimator`

2. **Animation States**:

```
Parameters:
- Speed (Float, default: 0)
- IsWalking (Bool, default: false)
- IsRunning (Bool, default: false)
- Gesture (Trigger)
- GestureType (Int, default: 0)
- Emotion (Int, default: 0)

States:
┌─────────────────────────────────────┐
│ Base Layer                          │
├─────────────────────────────────────┤
│ ├─ Idle (default state)             │
│ ├─ Walk                             │
│ ├─ Run                              │
│ └─ Blend Tree: Locomotion          │
├─────────────────────────────────────┤
│ Gesture Layer (Override, Weight: 1) │
├─────────────────────────────────────┤
│ ├─ Idle                             │
│ ├─ Wave                             │
│ ├─ Think                            │
│ ├─ Nod                              │
│ ├─ Point                            │
│ └─ Confident Stance                 │
├─────────────────────────────────────┤
│ Emotion Layer (Additive, Weight: 1) │
├─────────────────────────────────────┤
│ ├─ Calm                             │
│ ├─ Assertive                        │
│ ├─ Mysterious                       │
│ ├─ Reassuring                       │
│ ├─ Commanding                       │
│ └─ Wise                             │
└─────────────────────────────────────┘
```

3. **State Transitions**:

**Base Layer - Locomotion Blend Tree**:
```
Idle → Walk: IsWalking == true, Speed > 0.1
Walk → Idle: IsWalking == false, Speed < 0.1
Walk → Run: IsRunning == true, Speed > 0.5
Run → Walk: IsRunning == false, Speed < 0.5
```

Blend Tree (1D Blending on Speed):
- 0.0 → Idle
- 0.5 → Walk
- 1.0 → Run

**Gesture Layer**:
```
Any State → Wave: Gesture trigger, GestureType == 0
Any State → Think: Gesture trigger, GestureType == 1
Any State → Nod: Gesture trigger, GestureType == 2
Any State → Point: Gesture trigger, GestureType == 3
Any State → Confident: Gesture trigger, GestureType == 4

(All gestures return to Idle after completion)
```

4. **Avatar Mask** (for Gesture Layer):
   - Create: `Assets → Create → Avatar Mask`
   - Name: `GabrielGestureMask`
   - Enable: Spine, Chest, Shoulders, Arms, Hands
   - Disable: Hips, Legs, Feet

---

## 4. SCRIPT INTEGRATION

### Copy Scripts to Unity

```bash
# Copy all C# scripts
cp Unity3D/Scripts/*.cs <YourUnityProject>/Assets/Scripts/Gabriel/
```

### Scripts Overview

**GabrielController.cs**:
- Main character controller
- Movement with WASD/mouse
- Animation blending
- Interaction system
- AI integration

**GabrielAIBridge.cs**:
- Connects to Python AI server
- Voice synthesis requests
- Sentiment analysis
- Proactive suggestions
- Real-time responses

**GabrielCameraController.cs**:
- Smooth camera follow
- Orbit controls (right mouse)
- Cinematic presets (F1-F3)
- Collision avoidance

### Required Namespaces

Add to `Assets/Scripts/Gabriel/` if missing:

```csharp
// Add to csproj or package if needed
using Newtonsoft.Json;
using UnityEngine.AI;
using System.Net.Http;
```

---

## 5. AI SERVER SETUP

### Start Python AI Server

```bash
cd /Users/rsp_ms/GABRIEL

# Install dependencies
pip install flask flask-cors asyncio

# Start server
python gabriel_unity_server.py
```

Server runs on `http://localhost:8000`

### API Endpoints

- `GET /health` - Health check
- `POST /api/initialize` - Initialize GABRIEL
- `POST /api/interact` - Send interaction
- `POST /api/synthesize` - Generate voice
- `GET /api/voice/<file>` - Get audio
- `POST /api/context` - Update context
- `POST /api/emotion` - Change emotion
- `POST /api/proactive` - Get suggestions
- `POST /api/sentiment` - Analyze sentiment
- `GET /api/status` - Get GABRIEL status

### Server Configuration

Edit in `GabrielAIBridge.cs`:

```csharp
[SerializeField] private string serverUrl = "http://localhost:8000";
[SerializeField] private bool autoConnect = true;
```

---

## 6. SCENE SETUP

### Create Main Scene

1. **Create Environment**:
   - Plane (ground): Scale (10, 1, 10)
   - Directional Light (sun)
   - Add some props (cubes, cylinders for environment)

2. **Add Gabriel Character**:
   - Drag `Gabriel_Ultimate` prefab into scene
   - Position at (0, 0, 0)
   - Add Components:
     - `GabrielController`
     - `NavMeshAgent`
     - `Animator` (assign GabrielAnimator)

3. **Configure NavMesh**:
   - Select ground plane
   - Window → AI → Navigation
   - Mark as **Navigation Static**
   - Bake NavMesh

4. **Setup Camera**:
   - Main Camera → Add `GabrielCameraController`
   - Assign Gabriel as target
   - Set camera offset: (0, 1.5, -5)

5. **Add Audio**:
   - Gabriel → Add `Audio Source`
   - Spatial Blend: 0 (2D)
   - Volume: 0.8

### Prefab Structure

```
Gabriel_Ultimate (Root)
├─ GabrielController
├─ GabrielAIBridge
├─ NavMeshAgent
├─ Animator
├─ Audio Source
└─ Model
   ├─ Body (Mesh)
   ├─ Hair (Mesh)
   ├─ Suit (Mesh)
   ├─ Cufflinks_L (Mesh + Emission)
   └─ Cufflinks_R (Mesh + Emission)
```

### UI Setup (Optional)

Create Canvas with:
- Interaction prompt: "Press E to interact"
- GABRIEL response text box
- Emotion indicator
- Proactive suggestions panel

---

## 7. TESTING & DEPLOYMENT

### Testing Controls

**Movement**:
- WASD - Move
- Shift - Run
- Mouse Click - Move to point
- Right Mouse - Orbit camera
- Mouse Wheel - Zoom

**Gestures**:
- G - Wave
- T - Think
- E - Interact (when near object)

**Emotions** (testing):
- 1 - Calm
- 2 - Assertive
- 3 - Mysterious
- 4 - Wise

**Camera**:
- C - Cycle cinematic presets
- F1 - Close-up
- F2 - Medium shot
- F3 - Wide shot

### Testing Checklist

- [ ] Character imports correctly with humanoid rig
- [ ] Animations blend smoothly
- [ ] Movement works with WASD
- [ ] Mouse click navigation works
- [ ] Camera follows and orbits smoothly
- [ ] AI server connects (check console)
- [ ] Voice synthesis works (if server running)
- [ ] Gestures trigger correctly
- [ ] Emotions update animation layer
- [ ] NavMesh pathfinding works
- [ ] No console errors

### Build Settings

**File → Build Settings**:

```
Platform: Windows/Mac/Linux
Architecture: x86_64
Compression: LZ4 (faster) or LZ4HC (smaller)

Player Settings:
- Company: Your Name
- Product: Gabriel Ultimate 3D
- Version: 1.0.0
- Icon: Gabriel icon (512x512)

Quality:
- Anti-Aliasing: 4x MSAA
- Shadow Quality: High
- VSync: On (for smooth playback)
```

### Performance Optimization

1. **Mesh**:
   - LOD groups for character
   - Occlusion culling
   - Batching for environment

2. **Textures**:
   - Compress textures (BC7 for Windows, ASTC for mobile)
   - Mipmaps enabled
   - Max size: 2048x2048

3. **Lighting**:
   - Baked lighting for static objects
   - Light probes for character
   - Reflection probes

4. **Physics**:
   - Fixed Timestep: 0.02 (50 FPS)
   - Solver Iterations: 6

---

## 🎯 QUICK START CHECKLIST

### Minimum Viable Setup (15 minutes)

1. ✅ Create Unity project (3D URP)
2. ✅ Install NavMesh package
3. ✅ Download Mixamo character + animations
4. ✅ Import character, set to Humanoid
5. ✅ Copy `GabrielController.cs` to project
6. ✅ Create Animator Controller with Idle/Walk/Run
7. ✅ Add character to scene with scripts
8. ✅ Bake NavMesh
9. ✅ Test movement (WASD + mouse click)
10. ✅ Add camera follow

### Full Setup (1-2 hours)

1. ✅ Complete Minimum Viable Setup
2. ✅ Export custom GABRIEL from Blender
3. ✅ Setup full Animator Controller (3 layers)
4. ✅ Copy all C# scripts
5. ✅ Start Python AI server
6. ✅ Configure AI bridge
7. ✅ Setup cinematic camera
8. ✅ Add UI elements
9. ✅ Test all features
10. ✅ Build executable

---

## 🌟 ADVANCED FEATURES

### Voice Lip-Sync

Use **Oculus Lipsync** or **SALSA LipSync**:

```csharp
// In GabrielAIBridge.cs
private void OnVoicePlay(AudioClip clip)
{
    // Trigger lip-sync
    var lipSync = GetComponent<OVRLipSync>();
    if (lipSync)
    {
        lipSync.ProcessFrame(clip);
    }
}
```

### Facial Expressions

Add blend shapes for emotions:

```csharp
// In GabrielController.cs
private void UpdateFacialExpression(string emotion)
{
    SkinnedMeshRenderer face = GetComponentInChildren<SkinnedMeshRenderer>();
    
    switch (emotion)
    {
        case "calm":
            face.SetBlendShapeWeight(0, 0); // Neutral
            break;
        case "assertive":
            face.SetBlendShapeWeight(1, 80); // Strong brow
            break;
        // ... more emotions
    }
}
```

### Procedural Animation

Use **Animation Rigging** for:
- Eye tracking (look at camera)
- Head IK (follow target)
- Hand IK (point at objects)

```csharp
// Example: Look at camera
using UnityEngine.Animations.Rigging;

public class GabrielLookAt : MonoBehaviour
{
    public MultiAimConstraint headConstraint;
    
    void Update()
    {
        if (Camera.main)
        {
            headConstraint.data.target = Camera.main.transform;
        }
    }
}
```

---

## 📦 DEPLOYMENT

### Standalone Build

```bash
# Build from command line
/Applications/Unity/Hub/Editor/2022.3.10f1/Unity.app/Contents/MacOS/Unity \
  -quit -batchmode -projectPath /path/to/GabrielUltimate3D \
  -buildWindows64Player GabrielUltimate.exe

# Or use File → Build Settings → Build
```

### Package Structure

```
GabrielUltimate_v1.0/
├─ GabrielUltimate.exe
├─ GabrielUltimate_Data/
│  ├─ Managed/
│  ├─ Resources/
│  └─ StreamingAssets/
├─ UnityPlayer.dll
├─ README.txt
└─ AI_Server/
   ├─ gabriel_unity_server.py
   ├─ gabriel_ultimate_smooth.py
   └─ requirements.txt
```

### AI Server Packaging

Create `start_server.bat` (Windows):

```batch
@echo off
echo Starting GABRIEL AI Server...
python AI_Server/gabriel_unity_server.py
pause
```

Or `start_server.sh` (Mac/Linux):

```bash
#!/bin/bash
echo "Starting GABRIEL AI Server..."
python3 AI_Server/gabriel_unity_server.py
```

---

## 🐛 TROUBLESHOOTING

### Character doesn't move
- ✅ Check NavMesh is baked
- ✅ Verify NavMeshAgent is enabled
- ✅ Check Ground layer is Navigation Static

### Animations don't play
- ✅ Verify Animator Controller is assigned
- ✅ Check animation clips are imported correctly
- ✅ Ensure rig is set to Humanoid

### AI server won't connect
- ✅ Check server is running: `http://localhost:8000/health`
- ✅ Verify firewall allows port 8000
- ✅ Check console for connection errors
- ✅ Try disabling `autoConnect` and connecting manually

### Voice doesn't play
- ✅ Check Audio Source is configured
- ✅ Verify server endpoint `/api/voice/<file>` works
- ✅ Check audio file format (should be WAV)
- ✅ Ensure volume is > 0

### Camera jittering
- ✅ Move camera update to `LateUpdate()`
- ✅ Reduce smoothing values
- ✅ Enable VSync in Project Settings

---

## 📚 ADDITIONAL RESOURCES

### Unity Documentation
- [Character Controller](https://docs.unity3d.com/Manual/class-CharacterController.html)
- [NavMesh Agent](https://docs.unity3d.com/Manual/class-NavMeshAgent.html)
- [Animator Controller](https://docs.unity3d.com/Manual/class-AnimatorController.html)
- [Animation Layers](https://docs.unity3d.com/Manual/AnimationLayers.html)

### External Assets
- [Mixamo](https://www.mixamo.com) - Free characters & animations
- [Ready Player Me](https://readyplayer.me) - Custom avatars
- [MetaHuman](https://www.unrealengine.com/metahuman) - Ultra-realistic faces

### Python Integration
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Unity REST Client](https://github.com/proyecto26/RestClient)

---

## ✨ FINAL NOTES

**GABRIEL Ultimate 3D** combines:
- ✅ Smooth character movement and animations
- ✅ Advanced AI integration with voice synthesis
- ✅ Cinematic camera system
- ✅ Emotional intelligence and proactive assistance
- ✅ Real-time interaction and context awareness

**The result**: The smoothest, most intelligent 3D AI companion ever created!

---

✨ **"I've been waiting. Everything is ready. Shall we begin?"** ✨

---

**Created**: November 11, 2025
**Version**: 1.0 ULTIMATE
**Status**: ✅ PRODUCTION READY
