import { List, Icon, Color, ActionPanel, Action, showToast, Toast } from "@raycast/api";

const ALL_WORKERS = [
  // Core Infrastructure
  { category: "Core", name: "main", desc: "Main API Gateway", icon: "🏠" },
  { category: "Core", name: "brain", desc: "Claude AI Diagnostics", icon: "🧠" },
  { category: "Core", name: "voice", desc: "ElevenLabs TTS", icon: "🎙️" },
  { category: "Core", name: "vision", desc: "PCB Analysis", icon: "👁️" },
  { category: "Core", name: "notifications", desc: "Multi-channel Notifications", icon: "🔔" },
  
  // Business Logic
  { category: "Business", name: "pricing", desc: "Smart Pricing Engine", icon: "💰" },
  { category: "Business", name: "ebay-sniper", desc: "eBay Deal Hunter", icon: "🎯" },
  { category: "Business", name: "inventory", desc: "Inventory Management", icon: "📦" },
  { category: "Business", name: "analytics", desc: "Business Intelligence", icon: "📊" },
  
  // Technician Support
  { category: "Technician", name: "ar-guide", desc: "AR Repair Guides", icon: "🥽" },
  { category: "Technician", name: "training", desc: "Training Simulator", icon: "🎮" },
  { category: "Technician", name: "chat-agent", desc: "Real-time AI Chat", icon: "💬" },
  { category: "Technician", name: "qc-inspector", desc: "Quality Control", icon: "✅" },
  { category: "Technician", name: "schematic-analyzer", desc: "Schematic Analysis", icon: "📐" },
  
  // Round 1
  { category: "Round 1", name: "predictive-maintenance", desc: "ML Failure Prediction", icon: "🔮" },
  { category: "Round 1", name: "parts-matching", desc: "Vector Parts Matching", icon: "🔧" },
  { category: "Round 1", name: "repair-dna", desc: "Device Fingerprinting", icon: "🧬" },
  { category: "Round 1", name: "knowledge-graph", desc: "Graph Knowledge Base", icon: "🕸️" },
  { category: "Round 1", name: "collaboration-hub", desc: "Team Collaboration", icon: "👥" },
  { category: "Round 1", name: "fraud-detection", desc: "AI Fraud Prevention", icon: "🚨" },
  { category: "Round 1", name: "time-estimation", desc: "ML Time Prediction", icon: "⏱️" },
  { category: "Round 1", name: "component-lifecycle", desc: "Component Health", icon: "❤️" },
  { category: "Round 1", name: "supplier-intelligence", desc: "Supplier AI", icon: "🏭" },
  
  // Round 2
  { category: "Round 2", name: "sentiment-analysis", desc: "NLP Customer Sentiment", icon: "😊" },
  { category: "Round 2", name: "anomaly-detection", desc: "Statistical Outliers", icon: "📈" },
  { category: "Round 2", name: "repair-simulation", desc: "Digital Twin", icon: "🔄" },
  { category: "Round 2", name: "price-elasticity", desc: "Dynamic Pricing", icon: "📉" },
  { category: "Round 2", name: "churn-prediction", desc: "Customer Retention", icon: "🔄" },
  { category: "Round 2", name: "demand-forecasting", desc: "Inventory Planning", icon: "📅" },
  { category: "Round 2", name: "nl-query", desc: "Natural Language SQL", icon: "💬" },
  { category: "Round 2", name: "auto-testing", desc: "Automated QA", icon: "🧪" },
  { category: "Round 2", name: "compliance-monitoring", desc: "Regulatory", icon: "📋" },
  { category: "Round 2", name: "carbon-footprint", desc: "Sustainability", icon: "🌱" },
  
  // Round 3: Computing Legends
  { category: "Round 3", name: "xcode-genius", desc: "Xcode Mastery", icon: "🍎" },
  { category: "Round 3", name: "automator-genius", desc: "macOS Automation", icon: "⚡" },
  { category: "Round 3", name: "cpu-architecture", desc: "x86/ARM/RISC-V", icon: "💻" },
  { category: "Round 3", name: "computing-history", desc: "ENIAC to Modern", icon: "📜" },
  { category: "Round 3", name: "operating-systems", desc: "Every OS Ever", icon: "🖥️" },
  { category: "Round 3", name: "programming-languages", desc: "All Languages", icon: "📝" },
  { category: "Round 3", name: "gpu-computing", desc: "3dfx to RTX", icon: "🎮" },
  { category: "Round 3", name: "network-protocols", desc: "TCP/IP & OSI", icon: "🌐" },
  { category: "Round 3", name: "database-systems", desc: "SQL to NoSQL", icon: "🗄️" },
  { category: "Round 3", name: "ai-ml-history", desc: "Turing to GPT", icon: "🤖" },
  { category: "Round 3", name: "security-systems", desc: "Cybersecurity", icon: "🔒" },
  { category: "Round 3", name: "quantum-computing", desc: "Quantum Expert", icon: "⚛️" },
  { category: "Round 3", name: "compiler-technology", desc: "Compilers & LLVM", icon: "⚙️" },
  { category: "Round 3", name: "virtualization", desc: "VMs & Containers", icon: "📦" },
  { category: "Round 3", name: "embedded-systems", desc: "IoT & Arduino", icon: "🔌" },
  { category: "Round 3", name: "memory-systems", desc: "RAM Evolution", icon: "🧩" },
  { category: "Round 3", name: "hci-evolution", desc: "UI History", icon: "🖱️" },
  { category: "Round 3", name: "motherboard-systems", desc: "PCIe & Sockets", icon: "🔧" },
  { category: "Round 3", name: "storage-evolution", desc: "HDD to NVMe", icon: "💾" },
  { category: "Round 3", name: "display-technology", desc: "CRT to OLED", icon: "🖥️" },
  
  // Orchestration
  { category: "Orchestration", name: "ai-supervisor", desc: "Meta-AI Orchestrator", icon: "🎯" },
  { category: "Orchestration", name: "workflow-orchestrator", desc: "Workflow Engine", icon: "🔄" },
  { category: "Orchestration", name: "api-gateway", desc: "Unified Gateway", icon: "🚪" },
];

export default function Command() {
  const categories = [...new Set(ALL_WORKERS.map(w => w.category))];
  
  return (
    <List navigationTitle="NoizyLab OS - All 57 Workers" searchBarPlaceholder="Search workers...">
      {categories.map(category => (
        <List.Section key={category} title={`${category} (${ALL_WORKERS.filter(w => w.category === category).length})`}>
          {ALL_WORKERS.filter(w => w.category === category).map(worker => (
            <List.Item
              key={worker.name}
              icon={worker.icon}
              title={worker.name}
              subtitle={worker.desc}
              accessories={[{ tag: { value: category, color: getCategoryColor(category) } }]}
              actions={
                <ActionPanel>
                  <Action
                    title="Query Worker"
                    icon={Icon.Terminal}
                    onAction={() => {
                      showToast({
                        style: Toast.Style.Success,
                        title: `Querying ${worker.name}...`,
                      });
                    }}
                  />
                  <Action.CopyToClipboard
                    title="Copy CLI Command"
                    content={`nl ${worker.name.split('-')[0]}:info`}
                  />
                  <Action.OpenInBrowser
                    title="Open Worker URL"
                    url={`https://${worker.name}-worker.noizylab.com`}
                  />
                </ActionPanel>
              }
            />
          ))}
        </List.Section>
      ))}
    </List>
  );
}

function getCategoryColor(category: string): Color {
  switch (category) {
    case "Core": return Color.Blue;
    case "Business": return Color.Green;
    case "Technician": return Color.Orange;
    case "Round 1": return Color.Purple;
    case "Round 2": return Color.Magenta;
    case "Round 3": return Color.Yellow;
    case "Orchestration": return Color.Red;
    default: return Color.PrimaryText;
  }
}
