import { List, Icon, Color, ActionPanel, Action } from "@raycast/api";

const WORKERS = {
  core: [
    { name: "main", desc: "Main API Gateway" },
    { name: "brain", desc: "Claude AI Diagnostics" },
    { name: "voice", desc: "ElevenLabs TTS" },
    { name: "vision", desc: "PCB Analysis" },
    { name: "notifications", desc: "Multi-channel Notifications" },
  ],
  business: [
    { name: "pricing", desc: "Smart Pricing Engine" },
    { name: "ebay-sniper", desc: "eBay Deal Hunter" },
    { name: "inventory", desc: "Inventory Management" },
    { name: "analytics", desc: "Business Intelligence" },
  ],
  round3: [
    { name: "cpu-architecture", desc: "x86/ARM/RISC-V Expert" },
    { name: "operating-systems", desc: "Every OS Ever Made" },
    { name: "programming-languages", desc: "All Languages Since FORTRAN" },
    { name: "gpu-computing", desc: "3dfx to RTX 5090" },
    { name: "network-protocols", desc: "TCP/IP, OSI, DNS" },
    { name: "database-systems", desc: "Hierarchical to NoSQL" },
    { name: "ai-ml-history", desc: "Turing to GPT" },
    { name: "security-systems", desc: "Cybersecurity Evolution" },
    { name: "quantum-computing", desc: "Qubits & Algorithms" },
    { name: "compiler-technology", desc: "Lexers to LLVM" },
    { name: "virtualization", desc: "VMware to Kubernetes" },
    { name: "embedded-systems", desc: "Arduino to Automotive" },
    { name: "memory-systems", desc: "Core to HBM3E" },
    { name: "hci-evolution", desc: "Punch Cards to VR" },
    { name: "motherboard-systems", desc: "S-100 to Z890" },
    { name: "storage-evolution", desc: "RAMAC to NVMe" },
    { name: "display-technology", desc: "CRT to microLED" },
    { name: "xcode-genius", desc: "Xcode Mastery" },
    { name: "automator-genius", desc: "macOS Automation" },
    { name: "computing-history", desc: "ENIAC to Modern" },
  ],
};

export default function Command() {
  return (
    <List navigationTitle="NoizyLab OS - 57 AI Workers">
      <List.Section title="📊 Status Overview">
        <List.Item
          icon={{ source: Icon.CheckCircle, tintColor: Color.Green }}
          title="All Systems Operational"
          subtitle="57 Workers Active"
          accessories={[{ text: "3 Rounds Complete" }]}
        />
      </List.Section>

      <List.Section title="🏗️ Core Infrastructure (5)">
        {WORKERS.core.map((w) => (
          <List.Item
            key={w.name}
            icon={{ source: Icon.Circle, tintColor: Color.Green }}
            title={w.name}
            subtitle={w.desc}
            actions={
              <ActionPanel>
                <Action.CopyToClipboard title="Copy Worker Name" content={w.name} />
              </ActionPanel>
            }
          />
        ))}
      </List.Section>

      <List.Section title="💼 Business Logic (4)">
        {WORKERS.business.map((w) => (
          <List.Item
            key={w.name}
            icon={{ source: Icon.Circle, tintColor: Color.Blue }}
            title={w.name}
            subtitle={w.desc}
          />
        ))}
      </List.Section>

      <List.Section title="🏆 Round 3: Computing Legends (20)">
        {WORKERS.round3.map((w) => (
          <List.Item
            key={w.name}
            icon={{ source: Icon.Star, tintColor: Color.Yellow }}
            title={w.name}
            subtitle={w.desc}
            actions={
              <ActionPanel>
                <Action.OpenInBrowser
                  title="View Worker"
                  url={`https://${w.name}-worker.noizylab.com`}
                />
              </ActionPanel>
            }
          />
        ))}
      </List.Section>
    </List>
  );
}
