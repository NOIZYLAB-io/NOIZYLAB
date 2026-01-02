/**
 * Board Database - Known PCB Reference Library
 * 
 * Contains metadata about known board types for automatic detection
 * and matching against golden references
 */

export interface BoardDefinition {
  id: string;
  name: string;
  manufacturer: string;
  category: 'phone' | 'laptop' | 'tablet' | 'console' | 'pc' | 'other';
  model?: string;
  year?: number;
  
  // Identification features
  identifiers: {
    boardNumber?: string;    // e.g., "820-00875-A"
    modelNumber?: string;    // e.g., "A2111"
    fccId?: string;
    serialPrefix?: string[];
  };
  
  // Board characteristics
  specs: {
    layers?: number;
    dimensions?: { width: number; height: number }; // mm
    mainCPU?: string;
    powerIC?: string;
    chargeIC?: string;
  };
  
  // Known components and their locations
  components: ComponentDefinition[];
  
  // Common failure points
  commonIssues: CommonIssue[];
  
  // Related resources
  schematicAvailable: boolean;
  boardviewAvailable: boolean;
  referenceImageId?: string;
}

export interface ComponentDefinition {
  designator: string;      // e.g., "U3100"
  name: string;            // e.g., "Tristar IC"
  partNumber?: string;     // e.g., "1612A1"
  category: ComponentCategory;
  location: {
    x: number;             // percentage from left
    y: number;             // percentage from top
    rotation?: number;     // degrees
  };
  package?: string;        // e.g., "BGA", "QFN", "0402"
  critical: boolean;       // Is this a commonly failing component?
  replacementDifficulty: 'easy' | 'medium' | 'hard' | 'expert';
}

type ComponentCategory = 
  | 'cpu'
  | 'power_ic'
  | 'charge_ic'
  | 'usb_ic'
  | 'audio_ic'
  | 'baseband'
  | 'nand'
  | 'ram'
  | 'capacitor'
  | 'resistor'
  | 'inductor'
  | 'diode'
  | 'fuse'
  | 'connector'
  | 'filter'
  | 'crystal'
  | 'other';

export interface CommonIssue {
  component: string;       // Component designator
  symptom: string;
  cause: string;
  solution: string;
  frequency: 'rare' | 'occasional' | 'common' | 'very_common';
  repairCost?: { min: number; max: number };
}

// ============================================================================
// BOARD DATABASE
// ============================================================================

export const boardDatabase: BoardDefinition[] = [
  // iPhone 13 Pro
  {
    id: 'iphone-13-pro',
    name: 'iPhone 13 Pro Logic Board',
    manufacturer: 'Apple',
    category: 'phone',
    model: 'A2483',
    year: 2021,
    identifiers: {
      boardNumber: '820-02645-A',
      modelNumber: 'A2483',
      serialPrefix: ['G0', 'G1'],
    },
    specs: {
      layers: 12,
      dimensions: { width: 110, height: 50 },
      mainCPU: 'A15 Bionic',
      powerIC: 'SN2611A0',
      chargeIC: 'U3300',
    },
    components: [
      {
        designator: 'U3100',
        name: 'Tristar/Hydra USB IC',
        partNumber: '1616A1',
        category: 'usb_ic',
        location: { x: 25, y: 45 },
        package: 'BGA',
        critical: true,
        replacementDifficulty: 'hard',
      },
      {
        designator: 'U3300',
        name: 'Tigris Charge IC',
        partNumber: 'SN2611A0',
        category: 'charge_ic',
        location: { x: 30, y: 50 },
        package: 'BGA',
        critical: true,
        replacementDifficulty: 'hard',
      },
      {
        designator: 'U2700',
        name: 'Power Management IC',
        partNumber: '338S00770',
        category: 'power_ic',
        location: { x: 45, y: 40 },
        package: 'BGA',
        critical: true,
        replacementDifficulty: 'expert',
      },
      {
        designator: 'U1501',
        name: 'Audio Codec IC',
        partNumber: '338S00537',
        category: 'audio_ic',
        location: { x: 60, y: 55 },
        package: 'BGA',
        critical: false,
        replacementDifficulty: 'medium',
      },
      {
        designator: 'FL3250',
        name: 'Backlight Filter',
        category: 'filter',
        location: { x: 15, y: 30 },
        package: '0402',
        critical: true,
        replacementDifficulty: 'medium',
      },
    ],
    commonIssues: [
      {
        component: 'U3100',
        symptom: 'No charge, USB not recognized',
        cause: 'Water damage, static discharge, or forced cable insertion',
        solution: 'Replace Tristar IC with reballed chip',
        frequency: 'very_common',
        repairCost: { min: 75, max: 150 },
      },
      {
        component: 'FL3250',
        symptom: 'No backlight, dim display',
        cause: 'Short circuit or physical damage',
        solution: 'Replace backlight filter or bypass if necessary',
        frequency: 'common',
        repairCost: { min: 50, max: 100 },
      },
      {
        component: 'U2700',
        symptom: 'Device dead, no response',
        cause: 'Power surge, battery issue, or failed update',
        solution: 'PMIC replacement (requires micro-soldering)',
        frequency: 'occasional',
        repairCost: { min: 150, max: 300 },
      },
    ],
    schematicAvailable: true,
    boardviewAvailable: true,
  },

  // MacBook Pro M1
  {
    id: 'macbook-pro-m1-2020',
    name: 'MacBook Pro 13" M1 2020 Logic Board',
    manufacturer: 'Apple',
    category: 'laptop',
    model: 'A2338',
    year: 2020,
    identifiers: {
      boardNumber: '820-02020-A',
      modelNumber: 'A2338',
    },
    specs: {
      layers: 14,
      dimensions: { width: 200, height: 130 },
      mainCPU: 'Apple M1',
      powerIC: 'CD3217',
    },
    components: [
      {
        designator: 'U7100',
        name: 'M1 SoC',
        category: 'cpu',
        location: { x: 50, y: 40 },
        package: 'BGA',
        critical: true,
        replacementDifficulty: 'expert',
      },
      {
        designator: 'U8000',
        name: 'USB-C Controller',
        partNumber: 'CD3217',
        category: 'usb_ic',
        location: { x: 20, y: 60 },
        package: 'BGA',
        critical: true,
        replacementDifficulty: 'hard',
      },
      {
        designator: 'U5110',
        name: 'ISL9240',
        category: 'power_ic',
        location: { x: 35, y: 70 },
        package: 'QFN',
        critical: true,
        replacementDifficulty: 'medium',
      },
    ],
    commonIssues: [
      {
        component: 'U8000',
        symptom: 'USB-C port not working, no charge on one side',
        cause: 'ESD damage or forced cable insertion',
        solution: 'Replace CD3217 USB-C controller',
        frequency: 'common',
        repairCost: { min: 100, max: 200 },
      },
      {
        component: 'U5110',
        symptom: 'Battery not charging, won\'t turn on',
        cause: 'Power surge or liquid damage',
        solution: 'Replace ISL9240 charger IC',
        frequency: 'occasional',
        repairCost: { min: 80, max: 150 },
      },
    ],
    schematicAvailable: true,
    boardviewAvailable: true,
  },

  // Samsung Galaxy S21
  {
    id: 'samsung-s21',
    name: 'Samsung Galaxy S21 Main Board',
    manufacturer: 'Samsung',
    category: 'phone',
    model: 'SM-G991',
    year: 2021,
    identifiers: {
      modelNumber: 'SM-G991',
    },
    specs: {
      layers: 10,
      dimensions: { width: 100, height: 45 },
      mainCPU: 'Exynos 2100 / Snapdragon 888',
      chargeIC: 'SM5714',
    },
    components: [
      {
        designator: 'U100',
        name: 'Application Processor',
        category: 'cpu',
        location: { x: 50, y: 45 },
        package: 'PoP BGA',
        critical: true,
        replacementDifficulty: 'expert',
      },
      {
        designator: 'U300',
        name: 'Charge IC',
        partNumber: 'SM5714',
        category: 'charge_ic',
        location: { x: 25, y: 55 },
        package: 'BGA',
        critical: true,
        replacementDifficulty: 'hard',
      },
    ],
    commonIssues: [
      {
        component: 'U300',
        symptom: 'Not charging, slow charge',
        cause: 'Water damage or third-party charger damage',
        solution: 'Replace SM5714 charge IC',
        frequency: 'common',
        repairCost: { min: 60, max: 120 },
      },
    ],
    schematicAvailable: false,
    boardviewAvailable: false,
  },

  // PlayStation 5
  {
    id: 'ps5-main',
    name: 'PlayStation 5 Main Board',
    manufacturer: 'Sony',
    category: 'console',
    model: 'CFI-1015A',
    year: 2020,
    identifiers: {
      modelNumber: 'CFI-1015A',
    },
    specs: {
      layers: 8,
      dimensions: { width: 280, height: 200 },
      mainCPU: 'AMD Zen 2 + RDNA 2',
    },
    components: [
      {
        designator: 'APU',
        name: 'Main APU',
        category: 'cpu',
        location: { x: 50, y: 50 },
        package: 'BGA',
        critical: true,
        replacementDifficulty: 'expert',
      },
      {
        designator: 'U1',
        name: 'HDMI Encoder IC',
        partNumber: 'MN864739',
        category: 'other',
        location: { x: 30, y: 40 },
        package: 'QFN',
        critical: true,
        replacementDifficulty: 'hard',
      },
      {
        designator: 'F1',
        name: 'HDMI Port Fuse',
        category: 'fuse',
        location: { x: 25, y: 45 },
        package: '0603',
        critical: true,
        replacementDifficulty: 'easy',
      },
    ],
    commonIssues: [
      {
        component: 'U1',
        symptom: 'No HDMI output, black screen',
        cause: 'HDMI cable force or ESD',
        solution: 'Replace MN864739 HDMI encoder',
        frequency: 'very_common',
        repairCost: { min: 80, max: 150 },
      },
      {
        component: 'F1',
        symptom: 'No HDMI output',
        cause: 'Short circuit protection triggered',
        solution: 'Replace HDMI fuse',
        frequency: 'common',
        repairCost: { min: 30, max: 60 },
      },
    ],
    schematicAvailable: false,
    boardviewAvailable: false,
  },
];

// ============================================================================
// BOARD DETECTION SERVICE
// ============================================================================

export class BoardDetector {
  /**
   * Find matching board by identifiers
   */
  static findByIdentifiers(identifiers: {
    boardNumber?: string;
    modelNumber?: string;
    fccId?: string;
  }): BoardDefinition | null {
    for (const board of boardDatabase) {
      if (identifiers.boardNumber && 
          board.identifiers.boardNumber === identifiers.boardNumber) {
        return board;
      }
      if (identifiers.modelNumber && 
          board.identifiers.modelNumber === identifiers.modelNumber) {
        return board;
      }
      if (identifiers.fccId && 
          board.identifiers.fccId === identifiers.fccId) {
        return board;
      }
    }
    return null;
  }

  /**
   * Search boards by name or category
   */
  static search(query: string): BoardDefinition[] {
    const q = query.toLowerCase();
    return boardDatabase.filter(board =>
      board.name.toLowerCase().includes(q) ||
      board.manufacturer.toLowerCase().includes(q) ||
      board.category.includes(q) ||
      board.model?.toLowerCase().includes(q)
    );
  }

  /**
   * Get common issues for a board
   */
  static getCommonIssues(boardId: string): CommonIssue[] {
    const board = boardDatabase.find(b => b.id === boardId);
    return board?.commonIssues || [];
  }

  /**
   * Get component info
   */
  static getComponent(
    boardId: string,
    designator: string
  ): ComponentDefinition | null {
    const board = boardDatabase.find(b => b.id === boardId);
    return board?.components.find(c => c.designator === designator) || null;
  }

  /**
   * List all boards
   */
  static listAll(): BoardDefinition[] {
    return boardDatabase;
  }

  /**
   * Filter by category
   */
  static byCategory(category: BoardDefinition['category']): BoardDefinition[] {
    return boardDatabase.filter(b => b.category === category);
  }
}

export default {
  boardDatabase,
  BoardDetector,
};
