#!/usr/bin/env python3
import wave, audioop, json, sys, math, pathlib, subprocess, os, yaml

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

def scan_vendor_libraries(vendors):
    results = []
    for vendor in vendors:
        for product in vendor.get("products", []):
            for lib_path in product.get("library_paths", []):
                p = pathlib.Path(lib_path).expanduser()
                if p.exists():
                    for file in p.rglob("*"):
                        if file.is_file():
                            results.append({
                                "vendor": vendor["name"],
                                "product": product["title"],
                                "path": str(file)
                            })
    return results

def main():
    p = pathlib.Path(sys.argv[1])
    if p.suffix.lower() not in (".wav",".aiff",".aif"):
        print(json.dumps({"error":"unsupported"})); return
    print(json.dumps(analyze_wav(p)))
    subprocess.run(["launchctl", "unload", "~/Library/LaunchAgents/com.noizyfish.catalog.plist"])
    subprocess.run(["launchctl", "list", "|", "grep", "noizyfish"])

    with open("vendors.yaml") as f:
        vendors = yaml.safe_load(f)
    results = scan_vendor_libraries(vendors)
    for r in results:
        print(f"{r['vendor']} | {r['product']} | {r['path']}")

if __name__ == "__main__":
    main()