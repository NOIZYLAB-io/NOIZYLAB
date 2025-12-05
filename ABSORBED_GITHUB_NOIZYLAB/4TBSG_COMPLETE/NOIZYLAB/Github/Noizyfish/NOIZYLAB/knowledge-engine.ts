/**
 * ============================================
 * NOIZYLAB KNOWLEDGE ENGINE
 * Complete Computer Repair Knowledge Base
 * From First Deployment (1976) → Today's AI CPU Repair (2024)
 * Updates Hourly via Cloudflare Workers Cron
 * ============================================
 * 
 * @module knowledge-engine
 * @version 1.0.0
 * @author NoizyLab
 */

// ============================================
// TYPE DEFINITIONS
// ============================================

export interface AppleHistory {
  era: string;
  year: string;
  models: string[];
  architecture: string;
  commonIssues: string[];
  repairMethods: string[];
  tools: string[];
}

export interface PCHistory {
  era: string;
  year: string;
  architecture: string;
  commonIssues: string[];
  repairMethods: string[];
  tools: string[];
}

export interface ModernApple {
  model: string;
  year: string;
  chip: string;
  knownIssues: string[];
  repairProcedures: string[];
  diagnosticTools: string[];
}

export interface ModernPC {
  architecture: string;
  cpu: string;
  knownIssues: string[];
  repairProcedures: string[];
  diagnosticTools: string[];
}

export interface AICPURepair {
  chip: string;
  manufacturer: string;
  repairTechniques: string[];
  diagnosticMethods: string[];
  tools: string[];
  breakthrough: string;
  tops?: string;
}

export interface RepairProtocol {
  issue: string;
  os: 'macos' | 'windows' | 'linux' | 'all';
  steps: string[];
  tools: string[];
  difficulty: 'easy' | 'medium' | 'hard' | 'expert';
}

export interface KnowledgeBase {
  historical: {
    apple: AppleHistory[];
    pc: PCHistory[];
  };
  modern: {
    apple: ModernApple[];
    pc: ModernPC[];
  };
  aiCpu: AICPURepair[];
  repairProtocols: RepairProtocol[];
  lastUpdated: number;
}

// ============================================
// COMPREHENSIVE KNOWLEDGE BASE
// Complete from 1976 Apple I → 2024 AI CPUs
// ============================================

export const KNOWLEDGE_BASE: KnowledgeBase = {
  historical: {
    apple: [
      {
        era: 'Apple I (1976)',
        year: '1976',
        models: ['Apple I'],
        architecture: 'MOS 6502 @ 1MHz',
        commonIssues: ['Power supply failures', 'Memory corruption', 'Display issues'],
        repairMethods: ['Capacitor replacement', 'Memory chip reseating', 'Voltage regulation'],
        tools: ['Multimeter', 'Oscilloscope', 'Soldering iron']
      },
      {
        era: 'Apple II Series (1977-1993)',
        year: '1977-1993',
        models: ['Apple II', 'Apple II Plus', 'Apple IIe', 'Apple IIc', 'Apple IIGS'],
        architecture: 'MOS 6502 / 65C02 / 65816',
        commonIssues: ['Floppy drive failures', 'Keyboard issues', 'Power supply problems'],
        repairMethods: ['Drive belt replacement', 'Contact cleaning', 'PSU recap'],
        tools: ['Floppy drive alignment tool', 'Contact cleaner', 'Capacitor tester']
      },
      {
        era: 'Macintosh Classic (1984-1996)',
        year: '1984-1996',
        models: ['Macintosh 128K', 'Macintosh 512K', 'Macintosh Plus', 'Macintosh SE', 'Macintosh Classic'],
        architecture: 'Motorola 68000 / 68030',
        commonIssues: ['CRT display failures', 'Hard drive crashes', 'RAM failures'],
        repairMethods: ['CRT flyback replacement', 'SCSI drive repair', 'RAM module replacement'],
        tools: ['CRT discharge tool', 'SCSI terminator', 'RAM tester']
      },
      {
        era: 'PowerPC Era (1994-2006)',
        year: '1994-2006',
        models: ['Power Macintosh', 'iMac G3/G4/G5', 'PowerBook', 'iBook'],
        architecture: 'PowerPC 601/603/604/G3/G4/G5',
        commonIssues: ['Logic board failures', 'PRAM battery issues', 'Thermal problems'],
        repairMethods: ['Logic board reflow', 'PRAM reset', 'Thermal paste replacement'],
        tools: ['Heat gun', 'PRAM battery', 'Thermal paste']
      },
      {
        era: 'Intel Transition (2006-2020)',
        year: '2006-2020',
        models: ['Mac Pro', 'iMac', 'MacBook Pro', 'MacBook Air', 'Mac mini'],
        architecture: 'Intel Core 2 Duo / Core i5/i7/i9',
        commonIssues: ['GPU failures', 'SSD failures', 'Keyboard issues', 'Display problems'],
        repairMethods: ['GPU reballing', 'SSD replacement', 'Keyboard replacement', 'Display assembly'],
        tools: ['BGA rework station', 'SSD adapter', 'Pentalobe screwdriver']
      }
    ],
    pc: [
      {
        era: 'IBM PC (1981)',
        year: '1981',
        architecture: 'Intel 8088 @ 4.77MHz',
        commonIssues: ['Power supply failures', 'Floppy drive issues', 'Memory errors'],
        repairMethods: ['PSU replacement', 'Drive alignment', 'Memory reseating'],
        tools: ['Multimeter', 'Floppy alignment tool', 'Memory tester']
      },
      {
        era: '286/386/486 Era (1982-1994)',
        year: '1982-1994',
        architecture: 'Intel 80286/80386/80486',
        commonIssues: ['BIOS corruption', 'CMOS battery failure', 'ISA card conflicts'],
        repairMethods: ['BIOS reflash', 'CMOS battery replacement', 'IRQ conflict resolution'],
        tools: ['EPROM programmer', 'CMOS battery', 'IRQ analyzer']
      },
      {
        era: 'Pentium Era (1993-2006)',
        year: '1993-2006',
        architecture: 'Intel Pentium / AMD K6/K7',
        commonIssues: ['CPU overheating', 'Motherboard capacitor failures', 'RAM errors'],
        repairMethods: ['Thermal paste application', 'Capacitor replacement', 'RAM testing'],
        tools: ['Thermal paste', 'Capacitor kit', 'Memtest86']
      },
      {
        era: 'Core Era (2006-2017)',
        year: '2006-2017',
        architecture: 'Intel Core 2 / Core i3/i5/i7',
        commonIssues: ['GPU failures', 'HDD failures', 'USB port issues'],
        repairMethods: ['GPU replacement', 'HDD to SSD upgrade', 'USB controller repair'],
        tools: ['GPU rework station', 'SSD upgrade kit', 'USB tester']
      },
      {
        era: 'Modern Era (2017-2024)',
        year: '2017-2024',
        architecture: 'Intel 8th-14th Gen / AMD Ryzen',
        commonIssues: ['Thermal throttling', 'NVMe failures', 'Thunderbolt issues'],
        repairMethods: ['Liquid metal application', 'NVMe replacement', 'Thunderbolt controller repair'],
        tools: ['Liquid metal', 'NVMe adapter', 'Thunderbolt tester']
      }
    ]
  },
  modern: {
    apple: [
      {
        model: 'Mac Studio M1 Ultra / M2 Ultra / M3 Ultra',
        year: '2022-2024',
        chip: 'Apple Silicon M1 Ultra / M2 Ultra / M3 Ultra',
        knownIssues: ['Thermal throttling under load', 'Thunderbolt port failures', 'SSD wear'],
        repairProcedures: [
          'Thermal paste replacement with high-performance compound',
          'Thunderbolt controller diagnostics via Apple Configurator',
          'SSD health check via System Information',
          'Power delivery system verification'
        ],
        diagnosticTools: ['Apple Diagnostics', 'System Information', 'Activity Monitor', 'Terminal (system_profiler)']
      },
      {
        model: 'MacBook Pro M1/M2/M3',
        year: '2020-2024',
        chip: 'Apple Silicon M1/M2/M3',
        knownIssues: ['Display flex cable issues', 'Battery degradation', 'Trackpad failures'],
        repairProcedures: [
          'Display assembly replacement',
          'Battery health check via coconutBattery',
          'Trackpad calibration',
          'Logic board diagnostics'
        ],
        diagnosticTools: ['Apple Diagnostics', 'coconutBattery', 'System Information']
      }
    ],
    pc: [
      {
        architecture: 'Intel 12th-14th Gen',
        cpu: 'Core i5/i7/i9 (Alder Lake / Raptor Lake)',
        knownIssues: ['E-core/P-core scheduling', 'DDR5 compatibility', 'Thermal throttling'],
        repairProcedures: [
          'BIOS update for proper core scheduling',
          'DDR5 XMP profile configuration',
          'Advanced thermal paste application',
          'Power limit adjustment'
        ],
        diagnosticTools: ['CPU-Z', 'HWiNFO64', 'Prime95', 'Memtest86']
      },
      {
        architecture: 'AMD Ryzen 7000/8000/9000 Series',
        cpu: 'Ryzen 5/7/9 (Zen 4/Zen 5)',
        knownIssues: ['EXPO memory issues', 'Thermal paste pump-out', 'USB dropouts'],
        repairProcedures: [
          'EXPO profile optimization',
          'Liquid metal application',
          'USB controller driver update',
          'Chipset driver update'
        ],
        diagnosticTools: ['Ryzen Master', 'HWiNFO64', 'Memtest86', 'USB device analyzer']
      }
    ]
  },
  aiCpu: [
    {
      chip: 'Apple Neural Engine (ANE)',
      manufacturer: 'Apple',
      repairTechniques: [
        'ANE diagnostics: system_profiler SPNeuralEngineDataType',
        'Machine learning workload testing',
        'Core ML performance verification',
        'Thermal monitoring during ML tasks'
      ],
      diagnosticMethods: [
        'Activity Monitor → Energy tab',
        'Terminal: powermetrics --samplers neall',
        'Xcode Instruments → Neural Engine',
        'Core ML performance profiler'
      ],
      tools: ['Xcode', 'Terminal', 'Activity Monitor', 'Instruments'],
      breakthrough: 'First consumer-grade neural processing unit (2017)',
      tops: '35 TOPS (M3)'
    },
    {
      chip: 'Intel AI Boost (NPU)',
      manufacturer: 'Intel',
      repairTechniques: [
        'NPU diagnostics via Intel DSA',
        'AI workload stress testing',
        'Power delivery verification',
        'Thermal monitoring'
      ],
      diagnosticMethods: [
        'Intel Driver & Support Assistant',
        'Task Manager → Performance → NPU',
        'Windows Performance Toolkit',
        'Intel VTune Profiler'
      ],
      tools: ['Intel DSA', 'VTune', 'Windows Performance Toolkit'],
      breakthrough: 'First x86 NPU in consumer CPUs (2024)',
      tops: '34 TOPS'
    },
    {
      chip: 'AMD XDNA AI Engine',
      manufacturer: 'AMD',
      repairTechniques: [
        'XDNA diagnostics via AMD Software',
        'AI workload testing',
        'Power management verification',
        'Thermal paste application for optimal heat transfer'
      ],
      diagnosticMethods: [
        'AMD Software → Performance → AI',
        'Ryzen Master AI monitoring',
        'HWiNFO64 → AI Engine sensors',
        'Windows Task Manager → NPU'
      ],
      tools: ['AMD Software', 'Ryzen Master', 'HWiNFO64'],
      breakthrough: 'First consumer AMD NPU (2024)',
      tops: '50 TOPS (XDNA 2)'
    }
  ],
  repairProtocols: [
    {
      issue: 'CPU Thermal Throttling',
      os: 'all',
      steps: [
        'Remove heatsink/fan assembly',
        'Clean old thermal paste completely',
        'Apply high-performance thermal paste (Arctic MX-6, Thermal Grizzly Kryonaut)',
        'For AI CPUs: Consider liquid metal for extreme performance',
        'Reinstall heatsink with proper torque',
        'Verify temperatures under load',
        'Check fan curves in BIOS/UEFI'
      ],
      tools: ['Thermal paste', 'Isopropyl alcohol', 'Lint-free cloth', 'Torque screwdriver', 'Temperature monitoring software'],
      difficulty: 'medium'
    },
    {
      issue: 'Apple Silicon Neural Engine Failure',
      os: 'macos',
      steps: [
        'Run: system_profiler SPNeuralEngineDataType',
        'Check Activity Monitor → Energy tab for ANE usage',
        'Test Core ML workloads',
        'Reset NVRAM: Option+Command+P+R at boot',
        'Run Apple Diagnostics',
        'If persistent: Logic board replacement (authorized service)'
      ],
      tools: ['Terminal', 'Activity Monitor', 'Apple Diagnostics', 'Xcode (for Core ML testing)'],
      difficulty: 'expert'
    },
    {
      issue: 'Intel/AMD NPU Not Detected',
      os: 'windows',
      steps: [
        'Check Device Manager → System devices → NPU',
        'Update chipset drivers',
        'Update BIOS/UEFI to latest version',
        'Enable NPU in BIOS settings',
        'Install Windows 11 24H2 or later (NPU support)',
        'Verify in Task Manager → Performance → NPU tab',
        'Run manufacturer diagnostic tools'
      ],
      tools: ['Device Manager', 'Manufacturer update tools', 'BIOS/UEFI', 'Windows Update'],
      difficulty: 'hard'
    }
  ],
  lastUpdated: Date.now()
};

/**
 * Generates enhanced prompt with complete historical and modern repair knowledge
 * 
 * @param agent - Agent name (e.g., 'ENGR_KEITH', 'LUCY', 'WARDIE')
 * @param basePrompt - The original prompt/question
 * @param env - Cloudflare Workers environment (for KV access)
 * @returns Enhanced prompt with full knowledge context
 */
export async function getEnhancedPrompt(
  agent: string,
  basePrompt: string,
  env: any
): Promise<string> {
  let knowledgeBase: KnowledgeBase = KNOWLEDGE_BASE;
  
  try {
    const knowledgeJson = await env.AGENT_MEMORY.get('knowledge_base');
    if (knowledgeJson) {
      knowledgeBase = JSON.parse(knowledgeJson);
    }
  } catch (error) {
    console.warn('Failed to load knowledge from KV, using base knowledge:', error);
  }

  const knowledgeContext = buildKnowledgeContext(knowledgeBase);

  return `
${knowledgeContext}

YOU ARE ${agent}, A NOIZYLAB SUPER-TECH WITH COMPLETE HISTORICAL AND MODERN REPAIR KNOWLEDGE.

${basePrompt}

Use your complete knowledge base to provide the most accurate, historically-informed, and cutting-edge repair solution.
`;
}

function buildKnowledgeContext(kb: KnowledgeBase): string {
  const sections = [
    'HISTORICAL APPLE (1976-2020):',
    ...kb.historical.apple.map(a => 
      `  ${a.era} (${a.year}): Architecture ${a.architecture}\n` +
      `    Common Issues: ${a.commonIssues.join(', ')}\n` +
      `    Repair Methods: ${a.repairMethods.join(', ')}\n` +
      `    Tools: ${a.tools.join(', ')}`
    ),
    '',
    'HISTORICAL PC (1981-2024):',
    ...kb.historical.pc.map(p => 
      `  ${p.era} (${p.year}): Architecture ${p.architecture}\n` +
      `    Common Issues: ${p.commonIssues.join(', ')}\n` +
      `    Repair Methods: ${p.repairMethods.join(', ')}\n` +
      `    Tools: ${p.tools.join(', ')}`
    ),
    '',
    'MODERN APPLE (2020-2024):',
    ...kb.modern.apple.map(m => 
      `  ${m.model} (${m.year}): Chip ${m.chip}\n` +
      `    Known Issues: ${m.knownIssues.join(', ')}\n` +
      `    Diagnostic Tools: ${m.diagnosticTools.join(', ')}`
    ),
    '',
    'MODERN PC (2017-2024):',
    ...kb.modern.pc.map(p => 
      `  ${p.architecture}: CPU ${p.cpu}\n` +
      `    Known Issues: ${p.knownIssues.join(', ')}\n` +
      `    Diagnostic Tools: ${p.diagnosticTools.join(', ')}`
    ),
    '',
    'AI CPU REPAIR (2024):',
    ...kb.aiCpu.map(ai => 
      `  ${ai.chip} (${ai.manufacturer}) - ${ai.breakthrough}${ai.tops ? ` - ${ai.tops}` : ''}\n` +
      `    Repair Techniques: ${ai.repairTechniques.join('; ')}\n` +
      `    Diagnostic Methods: ${ai.diagnosticMethods.join('; ')}`
    ),
    '',
    'REPAIR PROTOCOLS:',
    ...kb.repairProtocols.map(rp => 
      `  ${rp.issue} (${rp.os}) [${rp.difficulty}]:\n` +
      `    Steps: ${rp.steps.join(' → ')}\n` +
      `    Tools: ${rp.tools.join(', ')}`
    )
  ];

  return sections.join('\n');
}

/**
 * Initializes knowledge base in KV storage
 */
export async function initializeKnowledgeBase(env: any): Promise<void> {
  try {
    await env.AGENT_MEMORY.put('knowledge_base', JSON.stringify(KNOWLEDGE_BASE));
    await env.AGENT_MEMORY.put('knowledge_last_updated', Date.now().toString());
    console.log('✅ Knowledge base initialized in KV');
  } catch (error) {
    console.error('❌ Failed to initialize knowledge base:', error);
    throw error;
  }
}
