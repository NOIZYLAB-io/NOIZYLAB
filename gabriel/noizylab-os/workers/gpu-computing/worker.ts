import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  GPU_DB: D1Database;
  GPU_CACHE: KVNamespace;
  GPU_STORAGE: R2Bucket;
  AI: any;
  GPU_VECTORS: VectorizeIndex;
}

// ==============================================================================
// NOIZYLAB OS - GPU COMPUTING WORKER
// Complete History of Graphics & Compute Hardware/Software
// ==============================================================================

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// ==============================================================================
// COMPLETE GPU DATABASE - FROM 1970s TO PRESENT
// ==============================================================================

const GPU_DATABASE = {
  // ===========================================================================
  // EARLY GRAPHICS HARDWARE (1970s-1980s)
  // ===========================================================================
  earlyGraphics: {
    evans_sutherland: {
      name: 'Evans & Sutherland Picture System',
      year: 1968,
      significance: 'Pioneer in computer graphics hardware',
      type: 'Vector graphics'
    },
    imsai_vio: {
      name: 'IMSAI VIO',
      year: 1977,
      significance: 'Early video interface option'
    },
    tms9918: {
      name: 'TI TMS9918',
      year: 1979,
      manufacturer: 'Texas Instruments',
      significance: 'Video display processor for home computers',
      usedIn: ['MSX', 'TI-99/4A', 'ColecoVision', 'Sega SG-1000']
    },
    motorola_6845: {
      name: 'Motorola 6845',
      year: 1977,
      significance: 'CRT controller, used in many systems'
    },
    vic: {
      name: 'MOS VIC (6560/6561)',
      year: 1980,
      manufacturer: 'MOS Technology',
      significance: 'VIC-20 graphics chip'
    },
    vic_ii: {
      name: 'MOS VIC-II (6567/6569)',
      year: 1982,
      manufacturer: 'MOS Technology',
      significance: 'Commodore 64 graphics chip',
      features: ['Sprites', 'Scrolling', 'Color RAM']
    },
    amiga_custom: {
      name: 'Amiga Custom Chips (Agnus, Denise, Paula)',
      year: 1985,
      manufacturer: 'Commodore',
      significance: 'Revolutionary multimedia chipset',
      features: ['Blitter', 'Copper', 'Sprites', 'HAM mode']
    },
    ega: {
      name: 'IBM EGA',
      year: 1984,
      manufacturer: 'IBM',
      resolution: '640x350',
      colors: '16 from 64',
      significance: 'Enhanced Graphics Adapter'
    },
    vga: {
      name: 'IBM VGA',
      year: 1987,
      manufacturer: 'IBM',
      resolution: '640x480 (standard)',
      colors: '256 from 262,144',
      significance: 'Video Graphics Array - became standard'
    }
  },

  // ===========================================================================
  // 3D ACCELERATOR ERA (1990s)
  // ===========================================================================
  accelerators3D: {
    voodoo1: {
      name: '3dfx Voodoo Graphics',
      year: 1996,
      manufacturer: '3dfx',
      significance: 'Started the 3D gaming revolution',
      memory: '4MB',
      fillRate: '50 Mpixels/s',
      features: ['Texture mapping', 'Bilinear filtering', 'Z-buffering']
    },
    voodoo2: {
      name: '3dfx Voodoo2',
      year: 1998,
      manufacturer: '3dfx',
      significance: 'SLI pioneer - could combine two cards',
      memory: '8-12MB',
      fillRate: '90 Mpixels/s'
    },
    voodoo3: {
      name: '3dfx Voodoo3',
      year: 1999,
      manufacturer: '3dfx',
      variants: ['2000', '3000', '3500'],
      memory: '16MB'
    },
    voodoo5: {
      name: '3dfx Voodoo5',
      year: 2000,
      manufacturer: '3dfx',
      variants: ['5500', '6000'],
      significance: 'Last 3dfx cards before NVIDIA acquisition'
    },
    s3_virge: {
      name: 'S3 ViRGE',
      year: 1995,
      manufacturer: 'S3',
      significance: 'First mainstream 3D accelerator (often called "decelerator")'
    },
    rage_128: {
      name: 'ATI Rage 128',
      year: 1999,
      manufacturer: 'ATI',
      significance: 'ATI\'s entry into competitive 3D'
    },
    riva_128: {
      name: 'NVIDIA RIVA 128',
      year: 1997,
      manufacturer: 'NVIDIA',
      significance: 'NVIDIA\'s first hit product'
    },
    riva_tnt: {
      name: 'NVIDIA RIVA TNT',
      year: 1998,
      manufacturer: 'NVIDIA',
      significance: 'Twin-texel architecture'
    },
    riva_tnt2: {
      name: 'NVIDIA RIVA TNT2',
      year: 1999,
      manufacturer: 'NVIDIA',
      variants: ['TNT2', 'TNT2 Ultra', 'TNT2 M64'],
      significance: '32-bit color gaming'
    }
  },

  // ===========================================================================
  // NVIDIA GPUs
  // ===========================================================================
  nvidia: {
    // GeForce Era
    geforce_256: {
      name: 'GeForce 256',
      year: 1999,
      significance: 'First GPU - coined the term',
      memory: '32MB DDR',
      features: ['T&L hardware', 'Cube mapping']
    },
    geforce2: {
      name: 'GeForce2 Series',
      year: 2000,
      variants: ['MX', 'GTS', 'Pro', 'Ultra', 'Ti'],
      significance: 'Mainstream GPU success'
    },
    geforce3: {
      name: 'GeForce3',
      year: 2001,
      significance: 'First programmable shaders (Xbox GPU)',
      features: ['Vertex shaders', 'Pixel shaders']
    },
    geforce4: {
      name: 'GeForce4 Series',
      year: 2002,
      variants: ['MX', 'Ti'],
      significance: 'Last fixed-function GPUs'
    },
    geforcefx: {
      name: 'GeForce FX (5xxx)',
      year: 2003,
      variants: ['5200', '5600', '5700', '5800', '5900', '5950'],
      significance: 'DirectX 9, but hot and loud'
    },
    geforce6: {
      name: 'GeForce 6 Series',
      year: 2004,
      variants: ['6200', '6600', '6800'],
      significance: 'SM 3.0, return to form'
    },
    geforce7: {
      name: 'GeForce 7 Series',
      year: 2005,
      variants: ['7300', '7600', '7800', '7900', '7950'],
      significance: 'Last DirectX 9 generation'
    },
    geforce8: {
      name: 'GeForce 8 Series',
      year: 2006,
      variants: ['8400', '8500', '8600', '8800'],
      significance: 'Unified shaders, CUDA, DirectX 10',
      architecture: 'Tesla'
    },
    geforce9: {
      name: 'GeForce 9 Series',
      year: 2008,
      variants: ['9400', '9500', '9600', '9800'],
      significance: 'Refined Tesla'
    },
    geforce_200: {
      name: 'GeForce 200 Series',
      year: 2008,
      variants: ['GTX 260', 'GTX 275', 'GTX 280', 'GTX 285', 'GTX 295'],
      significance: 'High-end gaming'
    },
    geforce_400: {
      name: 'GeForce 400 Series (Fermi)',
      year: 2010,
      variants: ['GTX 460', 'GTX 470', 'GTX 480'],
      architecture: 'Fermi',
      significance: 'DirectX 11, compute focus'
    },
    geforce_500: {
      name: 'GeForce 500 Series',
      year: 2011,
      variants: ['GTX 560', 'GTX 570', 'GTX 580', 'GTX 590'],
      architecture: 'Fermi (refined)'
    },
    geforce_600: {
      name: 'GeForce 600 Series (Kepler)',
      year: 2012,
      variants: ['GTX 650', 'GTX 660', 'GTX 670', 'GTX 680', 'GTX 690'],
      architecture: 'Kepler',
      significance: 'Efficiency, GPU Boost'
    },
    geforce_700: {
      name: 'GeForce 700 Series',
      year: 2013,
      variants: ['GTX 750', 'GTX 760', 'GTX 770', 'GTX 780', 'GTX Titan'],
      architecture: 'Kepler (refined)'
    },
    geforce_900: {
      name: 'GeForce 900 Series (Maxwell)',
      year: 2014,
      variants: ['GTX 960', 'GTX 970', 'GTX 980', 'GTX Titan X'],
      architecture: 'Maxwell',
      significance: 'Excellent efficiency'
    },
    geforce_10: {
      name: 'GeForce 10 Series (Pascal)',
      year: 2016,
      variants: ['GTX 1050', 'GTX 1060', 'GTX 1070', 'GTX 1080', 'GTX 1080 Ti', 'Titan X/Xp'],
      architecture: 'Pascal',
      significance: '16nm FinFET, huge performance leap'
    },
    geforce_16: {
      name: 'GeForce 16 Series (Turing)',
      year: 2019,
      variants: ['GTX 1650', 'GTX 1660', 'GTX 1660 Super', 'GTX 1660 Ti'],
      architecture: 'Turing (no RT cores)',
      significance: 'Mainstream Turing'
    },
    geforce_20: {
      name: 'GeForce 20 Series (Turing)',
      year: 2018,
      variants: ['RTX 2060', 'RTX 2070', 'RTX 2080', 'RTX 2080 Ti', 'Titan RTX'],
      architecture: 'Turing',
      significance: 'First real-time ray tracing, Tensor cores'
    },
    geforce_30: {
      name: 'GeForce 30 Series (Ampere)',
      year: 2020,
      variants: ['RTX 3050', 'RTX 3060', 'RTX 3070', 'RTX 3080', 'RTX 3090'],
      architecture: 'Ampere',
      significance: '2nd gen RT, 3rd gen Tensor cores'
    },
    geforce_40: {
      name: 'GeForce 40 Series (Ada Lovelace)',
      year: 2022,
      variants: ['RTX 4060', 'RTX 4070', 'RTX 4080', 'RTX 4090'],
      architecture: 'Ada Lovelace',
      significance: 'DLSS 3, Frame Generation'
    },
    geforce_50: {
      name: 'GeForce 50 Series (Blackwell)',
      year: 2025,
      variants: ['RTX 5070', 'RTX 5080', 'RTX 5090'],
      architecture: 'Blackwell',
      significance: 'Latest generation'
    },

    // Data Center / AI
    tesla_k80: { name: 'Tesla K80', year: 2014, significance: 'Kepler data center' },
    tesla_p100: { name: 'Tesla P100', year: 2016, significance: 'First Pascal GPU, NVLink' },
    tesla_v100: { name: 'Tesla V100', year: 2017, significance: 'Volta, Tensor Cores, AI powerhouse' },
    a100: { name: 'A100', year: 2020, significance: 'Ampere data center, MIG' },
    h100: { name: 'H100', year: 2022, architecture: 'Hopper', significance: 'AI training beast' },
    h200: { name: 'H200', year: 2024, significance: 'HBM3e, more memory' },
    b100: { name: 'B100/B200', year: 2024, architecture: 'Blackwell', significance: 'Next-gen AI' },
    gb200: { name: 'GB200', year: 2024, significance: 'Grace Hopper Superchip' }
  },

  // ===========================================================================
  // AMD/ATI GPUs
  // ===========================================================================
  amd: {
    // ATI Era
    radeon_7200: {
      name: 'Radeon DDR (7200)',
      year: 2000,
      manufacturer: 'ATI',
      significance: 'ATI\'s answer to GeForce'
    },
    radeon_8500: {
      name: 'Radeon 8500',
      year: 2001,
      manufacturer: 'ATI',
      significance: 'First competitive ATI GPU'
    },
    radeon_9700: {
      name: 'Radeon 9700 Pro',
      year: 2002,
      manufacturer: 'ATI',
      significance: 'First DirectX 9 GPU, beat NVIDIA'
    },
    radeon_9800: {
      name: 'Radeon 9800 Pro/XT',
      year: 2003,
      manufacturer: 'ATI',
      significance: 'Legendary gaming card'
    },
    radeon_x800: {
      name: 'Radeon X800 Series',
      year: 2004,
      manufacturer: 'ATI',
      variants: ['Pro', 'XT', 'XT PE']
    },
    radeon_x1800: {
      name: 'Radeon X1800/X1900',
      year: 2005,
      manufacturer: 'ATI',
      significance: 'Last ATI before AMD'
    },

    // AMD Era
    radeon_hd_2000: {
      name: 'Radeon HD 2000 Series',
      year: 2007,
      architecture: 'TeraScale',
      variants: ['HD 2400', 'HD 2600', 'HD 2900'],
      significance: 'First unified shader AMD GPU'
    },
    radeon_hd_3000: {
      name: 'Radeon HD 3000 Series',
      year: 2007,
      variants: ['HD 3450', 'HD 3650', 'HD 3850', 'HD 3870']
    },
    radeon_hd_4000: {
      name: 'Radeon HD 4000 Series',
      year: 2008,
      variants: ['HD 4350', 'HD 4650', 'HD 4770', 'HD 4850', 'HD 4870', 'HD 4870 X2'],
      significance: 'Price/performance king'
    },
    radeon_hd_5000: {
      name: 'Radeon HD 5000 Series',
      year: 2009,
      architecture: 'TeraScale 2',
      variants: ['HD 5450', 'HD 5670', 'HD 5770', 'HD 5850', 'HD 5870', 'HD 5970'],
      significance: 'First DirectX 11 GPUs, Eyefinity'
    },
    radeon_hd_6000: {
      name: 'Radeon HD 6000 Series',
      year: 2010,
      variants: ['HD 6450', 'HD 6670', 'HD 6850', 'HD 6870', 'HD 6950', 'HD 6970', 'HD 6990']
    },
    radeon_hd_7000: {
      name: 'Radeon HD 7000 Series (GCN)',
      year: 2012,
      architecture: 'GCN 1.0',
      variants: ['HD 7770', 'HD 7850', 'HD 7870', 'HD 7950', 'HD 7970', 'HD 7990'],
      significance: 'First GCN architecture'
    },
    radeon_rx_200: {
      name: 'Radeon R7/R9 200 Series',
      year: 2013,
      variants: ['R7 260X', 'R9 270X', 'R9 280X', 'R9 290', 'R9 290X'],
      significance: 'GCN refined, Hawaii chip'
    },
    radeon_rx_300: {
      name: 'Radeon R7/R9 300 Series',
      year: 2015,
      variants: ['R7 370', 'R9 380', 'R9 390', 'R9 390X', 'R9 Fury', 'R9 Fury X', 'R9 Nano'],
      significance: 'HBM memory introduction'
    },
    radeon_rx_400: {
      name: 'Radeon RX 400 Series (Polaris)',
      year: 2016,
      architecture: 'Polaris (GCN 4)',
      variants: ['RX 460', 'RX 470', 'RX 480'],
      significance: '14nm, excellent value'
    },
    radeon_rx_500: {
      name: 'Radeon RX 500 Series',
      year: 2017,
      variants: ['RX 550', 'RX 560', 'RX 570', 'RX 580', 'RX 590'],
      significance: 'Refined Polaris'
    },
    radeon_vega: {
      name: 'Radeon RX Vega',
      year: 2017,
      architecture: 'Vega (GCN 5)',
      variants: ['Vega 56', 'Vega 64', 'Radeon VII'],
      significance: 'HBM2, compute focus'
    },
    radeon_rx_5000: {
      name: 'Radeon RX 5000 Series (Navi/RDNA)',
      year: 2019,
      architecture: 'RDNA 1',
      variants: ['RX 5500 XT', 'RX 5600 XT', 'RX 5700', 'RX 5700 XT'],
      significance: 'New RDNA architecture'
    },
    radeon_rx_6000: {
      name: 'Radeon RX 6000 Series (RDNA 2)',
      year: 2020,
      architecture: 'RDNA 2',
      variants: ['RX 6500 XT', 'RX 6600', 'RX 6700 XT', 'RX 6800', 'RX 6800 XT', 'RX 6900 XT', 'RX 6950 XT'],
      significance: 'Ray tracing, Infinity Cache'
    },
    radeon_rx_7000: {
      name: 'Radeon RX 7000 Series (RDNA 3)',
      year: 2022,
      architecture: 'RDNA 3',
      variants: ['RX 7600', 'RX 7700 XT', 'RX 7800 XT', 'RX 7900 XT', 'RX 7900 XTX'],
      significance: 'Chiplet design, AI accelerators'
    },
    radeon_rx_9000: {
      name: 'Radeon RX 9000 Series (RDNA 4)',
      year: 2025,
      architecture: 'RDNA 4',
      significance: 'Next-gen RDNA'
    },

    // Data Center
    mi250x: { name: 'Instinct MI250X', year: 2021, significance: 'CDNA 2, exascale AI' },
    mi300x: { name: 'Instinct MI300X', year: 2023, significance: 'CDNA 3, AI competitor to H100' }
  },

  // ===========================================================================
  // INTEL GPUs
  // ===========================================================================
  intel: {
    i740: {
      name: 'Intel i740',
      year: 1998,
      significance: 'Intel\'s first discrete GPU (unsuccessful)'
    },
    gma: {
      name: 'Intel GMA Series',
      years: '2004-2010',
      significance: 'Integrated graphics, notoriously slow'
    },
    hd_graphics: {
      name: 'Intel HD Graphics',
      years: '2010-present',
      significance: 'Integrated graphics in CPUs'
    },
    iris: {
      name: 'Intel Iris Graphics',
      years: '2013-present',
      significance: 'Higher-end integrated graphics'
    },
    arc_a380: {
      name: 'Intel Arc A380',
      year: 2022,
      architecture: 'Alchemist (Xe-HPG)',
      significance: 'Intel\'s return to discrete GPUs'
    },
    arc_a750: {
      name: 'Intel Arc A750',
      year: 2022,
      architecture: 'Alchemist',
      significance: 'Midrange Arc'
    },
    arc_a770: {
      name: 'Intel Arc A770',
      year: 2022,
      architecture: 'Alchemist',
      significance: 'Flagship Arc GPU'
    },
    arc_b580: {
      name: 'Intel Arc B580',
      year: 2024,
      architecture: 'Battlemage (Xe2)',
      significance: 'Second-gen Arc'
    },
    gaudi: {
      name: 'Intel Gaudi',
      years: '2019-present',
      significance: 'AI accelerator (from Habana)'
    }
  },

  // ===========================================================================
  // CONSOLE GPUs
  // ===========================================================================
  consoles: {
    ps1_gpu: {
      name: 'PlayStation GPU',
      year: 1994,
      significance: 'First major 3D console'
    },
    ps2_gs: {
      name: 'PlayStation 2 Graphics Synthesizer',
      year: 2000,
      manufacturer: 'Sony',
      significance: 'Emotion Engine companion'
    },
    xbox_nv2a: {
      name: 'Xbox NV2A',
      year: 2001,
      manufacturer: 'NVIDIA',
      significance: 'Custom GeForce 3'
    },
    gamecube_flipper: {
      name: 'GameCube Flipper',
      year: 2001,
      manufacturer: 'ArtX/ATI',
      significance: 'Nintendo\'s first modern GPU'
    },
    ps3_rsx: {
      name: 'PlayStation 3 RSX',
      year: 2006,
      manufacturer: 'NVIDIA',
      significance: 'Modified GeForce 7'
    },
    xbox_360_xenos: {
      name: 'Xbox 360 Xenos',
      year: 2005,
      manufacturer: 'ATI',
      significance: 'First unified shader console GPU'
    },
    wii_hollywood: {
      name: 'Wii Hollywood',
      year: 2006,
      manufacturer: 'ATI',
      significance: 'Enhanced Flipper'
    },
    ps4_gpu: {
      name: 'PlayStation 4 GPU',
      year: 2013,
      manufacturer: 'AMD',
      architecture: 'GCN 1.1',
      significance: 'Custom Radeon'
    },
    xbox_one_gpu: {
      name: 'Xbox One GPU',
      year: 2013,
      manufacturer: 'AMD',
      architecture: 'GCN 1.0'
    },
    ps5_gpu: {
      name: 'PlayStation 5 GPU',
      year: 2020,
      manufacturer: 'AMD',
      architecture: 'RDNA 2',
      features: ['Ray tracing', '10.28 TFLOPs']
    },
    xbox_series_x_gpu: {
      name: 'Xbox Series X GPU',
      year: 2020,
      manufacturer: 'AMD',
      architecture: 'RDNA 2',
      features: ['Ray tracing', '12 TFLOPs']
    },
    switch_tegra: {
      name: 'Nintendo Switch Tegra X1',
      year: 2017,
      manufacturer: 'NVIDIA',
      architecture: 'Maxwell'
    }
  },

  // ===========================================================================
  // MOBILE GPUs
  // ===========================================================================
  mobile: {
    // Apple
    apple_gpu: {
      name: 'Apple GPU',
      series: ['A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18'],
      significance: 'Custom Apple GPU design since A11'
    },
    apple_m_series: {
      name: 'Apple M-Series GPU',
      variants: ['M1', 'M1 Pro', 'M1 Max', 'M1 Ultra', 'M2', 'M2 Pro', 'M2 Max', 'M2 Ultra', 'M3', 'M3 Pro', 'M3 Max', 'M4', 'M4 Pro', 'M4 Max'],
      significance: 'Desktop-class mobile GPUs'
    },

    // Qualcomm Adreno
    adreno: {
      name: 'Qualcomm Adreno',
      series: ['200', '300', '400', '500', '600', '700'],
      significance: 'Leading mobile GPU for Android'
    },

    // ARM Mali
    mali: {
      name: 'ARM Mali',
      series: ['Mali-400', 'Mali-T6xx', 'Mali-T7xx', 'Mali-T8xx', 'Mali-G7x', 'Mali-G5xx', 'Mali-Immortalis'],
      significance: 'Most-used mobile GPU IP'
    },

    // Imagination PowerVR
    powervr: {
      name: 'Imagination PowerVR',
      series: ['SGX', 'Series5', 'Series6', 'Series7', 'IMG A', 'IMG B', 'IMG C', 'IMG D'],
      significance: 'Used in Apple devices (A4-A10), many others'
    }
  },

  // ===========================================================================
  // GRAPHICS APIs
  // ===========================================================================
  apis: {
    opengl: {
      name: 'OpenGL',
      year: 1992,
      developer: 'Silicon Graphics/Khronos',
      significance: 'Cross-platform 3D standard',
      currentVersion: '4.6'
    },
    direct3d: {
      name: 'Direct3D',
      year: 1996,
      developer: 'Microsoft',
      significance: 'Windows gaming standard',
      versions: ['DX1-DX7', 'DX8', 'DX9', 'DX10', 'DX11', 'DX12']
    },
    vulkan: {
      name: 'Vulkan',
      year: 2016,
      developer: 'Khronos Group',
      significance: 'Modern low-level cross-platform API'
    },
    metal: {
      name: 'Metal',
      year: 2014,
      developer: 'Apple',
      significance: 'Low-level Apple graphics API'
    },
    webgpu: {
      name: 'WebGPU',
      year: 2023,
      developer: 'W3C',
      significance: 'Modern web graphics API'
    },
    glide: {
      name: 'Glide',
      year: 1996,
      developer: '3dfx',
      significance: 'Proprietary 3dfx API (historical)'
    }
  },

  // ===========================================================================
  // COMPUTE PLATFORMS
  // ===========================================================================
  compute: {
    cuda: {
      name: 'NVIDIA CUDA',
      year: 2007,
      significance: 'GPU compute pioneer, AI standard',
      features: ['CUDA cores', 'Tensor cores', 'RT cores']
    },
    opencl: {
      name: 'OpenCL',
      year: 2009,
      developer: 'Khronos Group',
      significance: 'Cross-platform GPU compute'
    },
    rocm: {
      name: 'AMD ROCm',
      year: 2016,
      significance: 'AMD\'s open compute platform'
    },
    sycl: {
      name: 'SYCL',
      year: 2014,
      developer: 'Khronos Group',
      significance: 'C++ abstraction for heterogeneous computing'
    },
    oneapi: {
      name: 'Intel oneAPI',
      year: 2019,
      significance: 'Intel\'s unified programming model'
    },
    directcompute: {
      name: 'DirectCompute',
      year: 2009,
      developer: 'Microsoft',
      significance: 'Microsoft compute API'
    },
    metal_compute: {
      name: 'Metal Performance Shaders',
      year: 2015,
      developer: 'Apple',
      significance: 'Apple GPU compute'
    }
  },

  // ===========================================================================
  // AI ACCELERATORS
  // ===========================================================================
  aiAccelerators: {
    tpu: {
      name: 'Google TPU',
      versions: ['TPU v1', 'TPU v2', 'TPU v3', 'TPU v4', 'TPU v5'],
      year: 2016,
      significance: 'Custom AI training/inference accelerator'
    },
    inferentia: {
      name: 'AWS Inferentia',
      versions: ['Inferentia 1', 'Inferentia 2'],
      year: 2019,
      significance: 'Amazon custom inference chip'
    },
    trainium: {
      name: 'AWS Trainium',
      versions: ['Trainium 1', 'Trainium 2'],
      year: 2021,
      significance: 'Amazon custom training chip'
    },
    apple_neural_engine: {
      name: 'Apple Neural Engine',
      year: 2017,
      significance: 'On-device AI acceleration'
    },
    graphcore_ipu: {
      name: 'Graphcore IPU',
      year: 2017,
      significance: 'Intelligence Processing Unit'
    },
    cerebras_wse: {
      name: 'Cerebras Wafer Scale Engine',
      versions: ['WSE-1', 'WSE-2', 'WSE-3'],
      year: 2019,
      significance: 'Largest chip ever made'
    },
    groq_lpu: {
      name: 'Groq LPU',
      year: 2022,
      significance: 'Language Processing Unit, fast inference'
    },
    sambanova: {
      name: 'SambaNova RDU',
      year: 2019,
      significance: 'Reconfigurable Dataflow Unit'
    }
  }
};

// ==============================================================================
// API ENDPOINTS
// ==============================================================================

// Get all categories
app.get('/api/gpu/categories', (c) => {
  const categories = Object.keys(GPU_DATABASE);
  return c.json({
    success: true,
    categories,
    totalCategories: categories.length
  });
});

// Search GPUs
app.get('/api/gpu/search', (c) => {
  const query = (c.req.query('q') || '').toLowerCase();
  const results: any[] = [];

  Object.entries(GPU_DATABASE).forEach(([category, items]) => {
    Object.entries(items).forEach(([key, item]: [string, any]) => {
      const name = item.name || key;
      if (
        name.toLowerCase().includes(query) ||
        (item.manufacturer && item.manufacturer.toLowerCase().includes(query)) ||
        (item.architecture && item.architecture.toLowerCase().includes(query)) ||
        (item.significance && item.significance.toLowerCase().includes(query))
      ) {
        results.push({ category, key, ...item });
      }
    });
  });

  return c.json({
    success: true,
    query,
    resultCount: results.length,
    results
  });
});

// Get category
app.get('/api/gpu/category/:category', (c) => {
  const category = c.req.param('category') as keyof typeof GPU_DATABASE;
  const data = GPU_DATABASE[category];

  if (!data) {
    return c.json({ error: 'Category not found' }, 404);
  }

  return c.json({
    success: true,
    category,
    items: data
  });
});

// Get NVIDIA GPUs
app.get('/api/gpu/nvidia', (c) => {
  return c.json({
    success: true,
    manufacturer: 'NVIDIA',
    gpus: GPU_DATABASE.nvidia
  });
});

// Get AMD GPUs
app.get('/api/gpu/amd', (c) => {
  return c.json({
    success: true,
    manufacturer: 'AMD',
    gpus: GPU_DATABASE.amd
  });
});

// Get Intel GPUs
app.get('/api/gpu/intel', (c) => {
  return c.json({
    success: true,
    manufacturer: 'Intel',
    gpus: GPU_DATABASE.intel
  });
});

// Get APIs
app.get('/api/gpu/apis', (c) => {
  return c.json({
    success: true,
    apis: GPU_DATABASE.apis
  });
});

// Get compute platforms
app.get('/api/gpu/compute', (c) => {
  return c.json({
    success: true,
    platforms: GPU_DATABASE.compute
  });
});

// Get AI accelerators
app.get('/api/gpu/ai-accelerators', (c) => {
  return c.json({
    success: true,
    accelerators: GPU_DATABASE.aiAccelerators
  });
});

// Get timeline
app.get('/api/gpu/timeline', (c) => {
  const timeline: { year: number; name: string; category: string; significance?: string }[] = [];

  Object.entries(GPU_DATABASE).forEach(([category, items]) => {
    Object.entries(items).forEach(([key, item]: [string, any]) => {
      if (item.year) {
        timeline.push({
          year: item.year,
          name: item.name || key,
          category,
          significance: item.significance
        });
      }
    });
  });

  timeline.sort((a, b) => a.year - b.year);

  return c.json({
    success: true,
    totalEntries: timeline.length,
    timeline
  });
});

// AI-powered GPU recommendation
app.post('/api/gpu/recommend', async (c) => {
  const { useCase, budget, requirements } = await c.req.json();

  const prompt = `Based on this use case: "${useCase}"
Budget: ${budget}
Requirements: ${JSON.stringify(requirements)}

Recommend the best GPU(s) and explain why.
Consider: performance, power consumption, features, and value.`;

  const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
    prompt,
    max_tokens: 1000
  });

  return c.json({
    success: true,
    recommendation: response.response
  });
});

// Health check
app.get('/health', (c) => {
  return c.json({
    status: 'healthy',
    worker: 'gpu-computing-worker',
    version: '1.0.0',
    timestamp: new Date().toISOString(),
    capabilities: [
      'Complete GPU history from 1970s to present',
      'NVIDIA complete lineup (all GeForce generations)',
      'AMD/ATI complete lineup',
      'Intel discrete and integrated',
      'Console GPUs',
      'Mobile GPUs (Apple, Qualcomm, ARM, PowerVR)',
      'Graphics APIs (OpenGL, DirectX, Vulkan, Metal)',
      'Compute platforms (CUDA, OpenCL, ROCm)',
      'AI accelerators (TPU, Inferentia, etc.)',
      'AI-powered recommendations'
    ]
  });
});

export default app;
