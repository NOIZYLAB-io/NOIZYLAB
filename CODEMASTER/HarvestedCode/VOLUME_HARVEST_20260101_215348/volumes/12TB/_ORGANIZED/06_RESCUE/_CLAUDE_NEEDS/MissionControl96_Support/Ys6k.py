import os
import shutil
from pathlib import Path

# Set source to the Application Support folder inside bobby-mission-control
SOURCE = os.path.expanduser("~/bobby-mission-control/Application Support")
DEST = "/Volumes/4TB_UTILITY/Audio_Migrated"
AUDIO_EXTS = {".wav"}
DRY_RUN = True      # Set to False to actually move files
MIN_MB = 0          # Move all .wav files regardless of size

def scan_audio_files():
    files = []
    for root, _, fs in os.walk(SOURCE):
        for f in fs:
            if Path(f).suffix.lower() in AUDIO_EXTS:
                p = os.path.join(root, f)
                try:
                    sz = os.path.getsize(p)
                    if sz >= MIN_MB * 1024 * 1024:
                        files.append((sz, p))
                except Exception as e:
                    print(f"Could not access {p}: {e}")
    return files

def get_manufacturer(rel_path):
    # Manufacturer is the first folder in the relative path
    parts = rel_path.split(os.sep)
    return parts[0] if len(parts) > 1 else "Unknown"

def main():
    audio_files = scan_audio_files()
    audio_files.sort(reverse=True)

    print(f"\nFound {len(audio_files)} .wav files.")
    print("Top 20 largest .wav files:")
    for sz, p in audio_files[:20]:
        print(f"{sz/1024/1024:.2f} MB\t{p}")

    moved = 0
    for sz, src in audio_files:
        rel = os.path.relpath(src, SOURCE)
        manufacturer = get_manufacturer(rel)
        ext = Path(src).suffix.lower().lstrip(".")
        # New path: DEST/manufacturer/extension/original_file
        dst = os.path.join(DEST, manufacturer, ext, os.path.basename(src))
        if DRY_RUN:
            print(f"[DRY RUN] Would move {src} -> {dst}")
        else:
            try:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.move(src, dst)
                print(f"Moved {src} -> {dst}")
                moved += 1
            except Exception as e:
                print(f"Failed to move {src}: {e}")

    print(f"\n{'[DRY RUN] ' if DRY_RUN else ''}Done! {len(audio_files)} files would be moved to {DEST}")

if __name__ == "__main__":
    main()

import React, { useState } from "react";

type Agent = {
  id: number;
  name: string;
  role: string;
  status: "idle" | "busy" | "online" | "error";
};

const AGENT_ROLES = [
  "Baby", "Composer", "Mentor", "Historian", "Producer", "Performer", "Archivist",
  "Syntax", "Style", "Security", "Test", "Watcher", "Runner", "Narrator"
  // ...repeat or expand as needed to cover 96 agents
];

const AGENTS: Agent[] = Array.from({ length: 96 }, (_, i) => ({
  id: i + 1,
  name: `Agent ${i + 1}`,
  role: AGENT_ROLES[i % AGENT_ROLES.length],
  status: "idle" as const,
}));

export default function AgentsPanel() {
  const [agents, setAgents] = useState(AGENTS);

  const setStatus = (id: number, status: Agent["status"]) => {
    setAgents(agents => agents.map(a => a.id === id ? { ...a, status } : a));
  };

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">🧑‍🚀 All 96 Agents</h2>
      <div className="grid grid-cols-4 md:grid-cols-8 gap-3">
        {agents.map(agent => (
          <div key={agent.id} className="rounded-xl border p-3 bg-zinc-900/80">
            <div className="font-bold">{agent.name}</div>
            <div className="text-xs text-cyan-300">{agent.role}</div>
            <div className={`mt-2 text-xs ${
              agent.status === "online" ? "text-green-400" :
              agent.status === "busy" ? "text-yellow-400" :
              agent.status === "error" ? "text-red-400" : "text-zinc-400"
            }`}>
              {agent.status}
            </div>
            <button
              className="mt-2 px-2 py-1 rounded bg-emerald-700 text-xs"
              onClick={() => setStatus(agent.id, "busy")}
            >
              Engage
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}