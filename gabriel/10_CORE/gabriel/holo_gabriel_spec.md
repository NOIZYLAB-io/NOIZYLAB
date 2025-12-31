# Holo-Gabriel Avatar Specification (Unity/Quest 2)

## 1. Concept

"A glowing, translucent, cybernetic humanoid that represents the soul of the machine."

- **Visual Style**: Tron-like, Wireframe or Holographic Shader.
- **Color**: Green (Idle), Blue (Processing), Red (Error), Gold (God Mode).

## 2. Data Protocol (UDP Port 9000)

- **Format**: JSON (UTF-8 encoded string).
- **Structure**:

  ```json
  {
    "e": "neutral",   // Emotion (string)
    "s": false,       // Is Speaking (boolean)
    "v": 0,           // Viseme ID (int, 0-15) - Optional
    "t": 123456.789   // Timestamp (float)
  }
  ```

## 3. Unity Implementation Guide

### Components

- **NetworkReceiver.cs**: Listens on UDP 9000.
- **AvatarController.cs**: Controls Animator and Materials.

### State Mapping

| Field | Value | Action |
| :--- | :--- | :--- |
| **e** (Emotion) | "neutral" | Default Pose, Green Emission. |
| | "processing"| Hand-to-Chin Pose, Blue pulsing. |
| | "creative" | Conductor Pose, Rainbow/Gold pulsing. |
| | "error" | Aggressive Stance, Red flashing. |
| **s** (Speaking) | true | Trigger "Talk" Animation Layer (Jaw/Hands). |

## 4. Optimization (Crystal Smooth)

- **Interpolation**: Smooth between state updates (Lerp color/bones).
- **Failsafe**: If no data for >2s, fade to "Sleep Mode" (Low opacity).
