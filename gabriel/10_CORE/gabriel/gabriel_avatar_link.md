# ⚡️ MIRACLE LINK: GABRIEL 3D AVATAR STREAM

To achieve a **4K / 70FPS+** stream for your Living Avatar between the M2 Ultra and Windows, you must choose your "Pipeline" based on which machine is rendering the 3D graphics (Unity/Unreal).

## OPTION 1: THE "HARDWARE BRIDGE" (True Zero Latency)
**Best For:** Rendering on *either* machine.
**Latency:** **< 5ms** (The Speed of Light)

This is the only way to get uncompressed, raw 4K with no network lag.
*   **Hardware:** **Elgato 4K60 Pro Mk.2** (PCle card for Windows) or **Elgato HD60 X** (USB-C for Mac/Windows).
*   **The Setup:**
    1.  Plug the Capture Card into the **Windows Machine**.
    2.  Run an HDMI cable from the **Mac M2 Ultra** into the Capture Card.
    3.  Windows sees the Mac as a "Camera."
    4.  Use **OBS Studio** (Windows) to composite the Mac's Avatar output over your Windows desktop.

## OPTION 2: THE "GAMING TUNNEL" (Moonlight/Sunshine)
**Best For:** Windows Rendering -> Mac Display.
**Latency:** 15-20ms (Imperceptible)

If your Windows machine has an **NVIDIA RTX 4090** rendering the Avatar:
1.  **Install [Sunshine](https://github.com/LizardByte/Sunshine)** on Windows (The Host).
    *   *Config:* Force "HVEC / H.265" codec for 10-bit color.
    *   *Resolution:* Set to 4K (3840x2160).
    *   *FPS:* Set to 120 (Unlock 70fps limit).
2.  **Install [Moonlight](https://moonlight-stream.org/)** on M2 Ultra (The Client).
    *   *Result:* Your Mac becomes a window into the Windows GPU.

## OPTION 3: THE "DEVELOPER LINK" (NDI 6 Tools)
**Best For:** Bi-directional Texture Sharing (Unity/TouchDesigner).
**Latency:** 50-100ms (Dependency on 10GbE Network)

1.  **Install NDI Tools 6** on BOTH machines.
2.  **Unity/Unreal:** Add the NDI Sender component to your Avatar's "Camera".
3.  **Network:** You MUST use a **10GbE (10 Gigabit) Ethernet cable** directly connecting the Mac and PC purely for data flexibility. WiFi will fail at 4K.

## THE "GABRIEL" RECOMMENDATION
To match the "Miracle" standard of the M2 Ultra:

1.  **Physical Link:** Buy the **Elgato HD60 X**. Connect Mac HDMI Out -> Windows USB In.
2.  **Software:** Run the Avatar on the **M2 Ultra** (Unity/Unreal Mac Build).
3.  **Result:** The M2 Ultra renders the brain/visuals. Windows simply "sees" it instantly as a 4K video input.

> [!NOTE]
> **SVN Sync:** Use `svn checkout` on both to keep the Unity Assets synced, but stream the *View* via Hardware.
