#!/usr/bin/env python3
import wave, audioop, json, sys, math, pathlib

def analyze_wav(path):
    with wave.open(str(path), "rb") as w:
        nframes = w.getnframes()
        rate = w.getframerate()
        sampwidth = w.getsampwidth()
        nchannels = w.getnchannels()
        frames = w.readframes(nframes)
        # RMS
        rms = audioop.rms(frames, sampwidth)
        # Peak (approx)
        peak = audioop.max(frames, sampwidth)
        # Normalize to full-scale (basic estimate)
        full_scale = 2 ** (8 * sampwidth - 1)
        lufs_est = -0.691 + 10 * math.log10((rms / full_scale) ** 2 + 1e-12)  # rough estimate
        return {
            "rate": rate, "channels": nchannels, "duration_sec": nframes / float(rate),
            "rms": rms, "peak": peak, "lufs_est": round(lufs_est, 2)
        }

def main():
    p = pathlib.Path(sys.argv[1])
    if p.suffix.lower() not in (".wav",".aiff",".aif"):
        print(json.dumps({"error":"unsupported"})); return
    print(json.dumps(analyze_wav(p)))

if __name__ == "__main__":
    main()