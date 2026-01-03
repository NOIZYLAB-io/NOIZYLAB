import { Hono } from 'hono';

interface Env {
    DISPLAY_DB: D1Database;
    DISPLAY_KV: KVNamespace;
    AI: any;
}

const app = new Hono<{ Bindings: Env }>();

// Complete display technology evolution
const displayHistory = {
    CRT: {
        inventor: "Karl Ferdinand Braun (1897)",
        principle: "Electron beam excites phosphors",
        computerUse: "1950s-2000s",
        advantages: ["Near-instant response", "True blacks", "No native resolution"],
        disadvantages: ["Bulky", "Heavy", "Power hungry", "Radiation emissions"]
    },
    plasma: {
        era: "1997-2014",
        principle: "Ionized gas between glass panels",
        pioneer: "Fujitsu (1992 prototype)",
        advantages: ["Deep blacks", "Wide viewing angles", "Fast response"],
        demise: "Outcompeted by LCD on price and efficiency"
    },
    LCD: {
        invention: { year: 1968, by: "RCA" },
        firstWatch: { year: 1973, by: "Seiko" },
        types: {
            TN: { fullName: "Twisted Nematic", response: "1-5ms", angles: "Poor", color: "6-bit+FRC" },
            VA: { fullName: "Vertical Alignment", response: "4-8ms", contrast: "3000-6000:1", angles: "Good" },
            IPS: { fullName: "In-Plane Switching", response: "4-8ms", angles: "178°", color: "8-10bit true" }
        },
        backlighting: {
            CCFL: { era: "1990s-2010s", type: "Cold Cathode Fluorescent" },
            LED: { era: "2004-present", types: ["Edge-lit", "Direct-lit", "Full-array"] },
            miniLED: { era: "2021-present", zones: "1000-2500+ dimming zones" }
        }
    }
};

const modernTechnologies = {
    OLED: {
        principle: "Organic compounds emit light when current applied",
        types: {
            WOLED: { use: "LG TVs", method: "White OLED + color filters" },
            RGBOLED: { use: "Samsung phones", method: "RGB sub-pixels" },
            QD_OLED: { year: 2022, maker: "Samsung Display", benefit: "Better color volume" },
            QDEL: { future: true, principle: "Electroluminescent quantum dots" }
        },
        concerns: {
            burnIn: "Static elements can cause permanent damage",
            brightness: "Peak brightness limited by heat",
            lifespan: "Blue OLED degrades faster"
        }
    },
    microLED: {
        principle: "Microscopic LED chips as individual pixels",
        advantages: ["OLED-like + no burn-in", "Higher brightness", "Longer lifespan"],
        challenges: ["Extremely expensive", "Difficult to manufacture at small sizes"],
        products: ["Samsung The Wall", "Sony Crystal LED"]
    },
    ePaper: {
        principle: "Electrophoretic display (charged particles)",
        maker: "E Ink Corporation",
        advantages: ["Sunlight readable", "No power when static", "Paper-like"],
        use: ["E-readers", "Signage", "Shelf labels"],
        color: ["Kaleido (2019)", "Gallery (2020)", "Spectra 6 (2024)"]
    }
};

const gamingDisplays = {
    refreshRates: {
        "60Hz": "Standard, 16.67ms frame time",
        "75Hz": "Budget gaming",
        "120Hz": "Common console target",
        "144Hz": "Competitive gaming standard",
        "165Hz": "Sweet spot for many",
        "240Hz": "Competitive esports",
        "360Hz": "Pro-level esports",
        "500Hz+": "Cutting edge 2024"
    },
    adaptiveSync: {
        GSync: { maker: "NVIDIA", year: 2013, hardware: "Proprietary module" },
        GSync_Compatible: { year: 2019, type: "Software, VESA VRR" },
        FreeSync: { maker: "AMD", year: 2015, standard: "VESA Adaptive-Sync" },
        FreeSync_Premium: { features: ["LFC", "120Hz+"] },
        FreeSync_Premium_Pro: { features: ["HDR support"] },
        HDMI_VRR: { standard: "HDMI 2.1" }
    },
    HDR: {
        HDR10: { standard: "Static metadata, 10-bit", maxNits: 1000 },
        HDR10Plus: { dynamic: true, maker: "Samsung" },
        DolbyVision: { dynamic: true, bits: 12, maxNits: 10000 },
        DisplayHDR: {
            "400": "Entry-level HDR",
            "600": "Adequate HDR",
            "1000": "Good HDR",
            "1400": "Excellent HDR",
            "True Black": "OLED-specific"
        }
    },
    responseTime: {
        MPRT: "Moving Picture Response Time",
        GtG: "Gray-to-Gray transition",
        overdrive: "Pixel response acceleration",
        ghosting: "Visible trail from slow pixels"
    }
};

const resolutions = {
    SD: { "480p": "720x480 (NTSC)", "576p": "720x576 (PAL)" },
    HD: { "720p": "1280x720", "1080p": "1920x1080" },
    QHD: { "1440p": "2560x1440", pixels: "3.7M" },
    "4K": { "2160p": "3840x2160", pixels: "8.3M", standard: "UHD-1" },
    "5K": { resolution: "5120x2880", use: "iMac 27\", pro monitors" },
    "8K": { "4320p": "7680x4320", pixels: "33.2M", standard: "UHD-2" },
    ultrawide: {
        "WQHD": "3440x1440 (21:9)",
        "UWQHD": "3840x1600 (21:9)",
        "DQHD": "5120x1440 (32:9)"
    },
    aspectRatios: {
        "4:3": "Classic CRT/LCD",
        "16:9": "Standard widescreen",
        "16:10": "Productivity, MacBooks",
        "21:9": "Ultrawide",
        "32:9": "Super ultrawide"
    }
};

const connectors = {
    VGA: { year: 1987, analog: true, maxRes: "2048x1536@85Hz" },
    DVI: { year: 1999, types: ["DVI-A (analog)", "DVI-D (digital)", "DVI-I (both)"] },
    HDMI: {
        "1.4": { year: 2009, bandwidth: "10.2Gbps", max: "4K@30Hz" },
        "2.0": { year: 2013, bandwidth: "18Gbps", max: "4K@60Hz" },
        "2.1": { year: 2017, bandwidth: "48Gbps", max: "10K@120Hz", features: ["VRR", "eARC", "DSC"] }
    },
    DisplayPort: {
        "1.2": { year: 2010, bandwidth: "21.6Gbps", max: "4K@60Hz" },
        "1.4": { year: 2016, bandwidth: "32.4Gbps", max: "8K@60Hz (DSC)" },
        "2.0": { year: 2019, bandwidth: "80Gbps", max: "16K@60Hz" },
        "2.1": { year: 2022, bandwidth: "80Gbps", clarified: "UHBR modes" }
    },
    Thunderbolt: {
        "3": { bandwidth: "40Gbps", connector: "USB-C", DP: "1.2" },
        "4": { bandwidth: "40Gbps", guaranteed: "Dual 4K or single 8K" },
        "5": { year: 2024, bandwidth: "80/120Gbps", DP: "2.1" }
    }
};

app.get('/', (c) => c.json({
    worker: "Display Technology Genius",
    coverage: "Complete display technology evolution",
    fromCRTToMicroLED: true,
    endpoints: ['/history', '/lcd', '/oled', '/gaming', '/resolutions', '/connectors', '/hdr']
}));

app.get('/history', (c) => c.json(displayHistory));
app.get('/lcd', (c) => c.json(displayHistory.LCD));
app.get('/oled', (c) => c.json(modernTechnologies.OLED));
app.get('/microled', (c) => c.json(modernTechnologies.microLED));
app.get('/gaming', (c) => c.json(gamingDisplays));
app.get('/refresh-rates', (c) => c.json(gamingDisplays.refreshRates));
app.get('/hdr', (c) => c.json(gamingDisplays.HDR));
app.get('/resolutions', (c) => c.json(resolutions));
app.get('/connectors', (c) => c.json(connectors));
app.get('/adaptive-sync', (c) => c.json(gamingDisplays.adaptiveSync));

app.post('/ai/query', async (c) => {
    const { question } = await c.req.json();
    const context = `Display technology expert: CRT history, LCD types (TN, VA, IPS), OLED/QD-OLED, microLED, gaming displays (refresh rates, VRR, G-Sync/FreeSync), HDR standards (HDR10, Dolby Vision), resolutions (1080p to 8K), connectors (HDMI 2.1, DisplayPort 2.1, Thunderbolt), color science.`;

    const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
        messages: [
            { role: 'system', content: context },
            { role: 'user', content: question }
        ]
    });
    return c.json({ answer: response.response });
});

export default app;
