import { Hono } from 'hono';

interface Env {
    MOBO_DB: D1Database;
    MOBO_KV: KVNamespace;
    AI: any;
}

const app = new Hono<{ Bindings: Env }>();

// Complete motherboard systems knowledge
const motherboardHistory = {
    early: {
        S100Bus: { year: 1974, pioneer: "Altair 8800", slots: 100, width: "8-bit" },
        AppleII: { year: 1977, slots: 8, feature: "Expansion slots standard" },
        IBM_PC: { year: 1981, bus: "ISA 8-bit", slots: 5 }
    },
    formFactors: {
        AT: { year: 1984, size: "12x13.8 inches", obsolete: true },
        babyAT: { year: 1985, size: "8.5x13 inches" },
        ATX: { year: 1995, creator: "Intel", size: "12x9.6 inches", standard: true },
        microATX: { year: 1997, size: "9.6x9.6 inches" },
        miniITX: { year: 2001, creator: "VIA", size: "6.7x6.7 inches" },
        EATX: { size: "12x13 inches", use: "Workstations, HEDT" },
        flexATX: { year: 1999, size: "9x7.5 inches minimum" },
        BTX: { year: 2004, creator: "Intel", status: "Failed to replace ATX" },
        NUC: { creator: "Intel", size: "4x4 inches", type: "Mini PC" }
    }
};

const busEvolution = {
    ISA: {
        "ISA-8": { year: 1981, width: "8-bit", speed: "4.77MHz" },
        "ISA-16": { year: 1984, width: "16-bit", speed: "8MHz" }
    },
    EISA: { year: 1988, width: "32-bit", speed: "8.33MHz", backwards: "ISA compatible" },
    VLB: { year: 1992, width: "32-bit", speed: "33-50MHz", tied: "CPU bus" },
    PCI: { year: 1992, width: "32/64-bit", speed: "33/66MHz", bandwidth: "133/533 MB/s" },
    AGP: { year: 1997, dedicated: "Graphics only", speeds: ["1x", "2x", "4x", "8x"] },
    PCIExpress: {
        "1.0": { year: 2003, perLane: "250 MB/s" },
        "2.0": { year: 2007, perLane: "500 MB/s" },
        "3.0": { year: 2010, perLane: "985 MB/s" },
        "4.0": { year: 2017, perLane: "1969 MB/s" },
        "5.0": { year: 2019, perLane: "3938 MB/s" },
        "6.0": { year: 2022, perLane: "7877 MB/s" },
        "7.0": { expected: 2025, perLane: "15754 MB/s" }
    }
};

const chipsetHistory = {
    intel: {
        classic: ["430FX", "440BX", "850", "865", "945", "P35", "P45", "X58"],
        modern: {
            "Z690": { year: 2021, socket: "LGA1700", pcie: "5.0", ddr: "DDR4/DDR5" },
            "Z790": { year: 2022, socket: "LGA1700", features: "More PCIe 4.0 lanes" },
            "Z890": { year: 2024, socket: "LGA1851", platform: "Arrow Lake" },
            "X670E": { competitor: "AMD", socket: "AM5" }
        },
        HEDT: ["X99", "X299", "X399 (AMD)", "TRX40 (AMD)"]
    },
    amd: {
        classic: ["nForce", "780G", "790FX", "890FX"],
        AM4: ["A320", "B350", "X370", "B450", "X470", "B550", "X570"],
        AM5: ["A620", "B650", "B650E", "X670", "X670E"]
    }
};

const socketHistory = {
    intel: {
        vintage: ["Socket 1-8", "Slot 1", "Socket 370", "Socket 423", "Socket 478"],
        lga: {
            "LGA775": { years: "2004-2009", cpus: "Pentium 4, Core 2" },
            "LGA1366": { years: "2008-2012", cpus: "Core i7 (Nehalem/Westmere)" },
            "LGA1156": { years: "2009-2011", cpus: "Core i5/i7 (Lynnfield)" },
            "LGA1155": { years: "2011-2013", cpus: "Sandy Bridge, Ivy Bridge" },
            "LGA1150": { years: "2013-2015", cpus: "Haswell, Broadwell" },
            "LGA1151": { years: "2015-2019", cpus: "Skylake through Coffee Lake" },
            "LGA1200": { years: "2020-2021", cpus: "Comet Lake, Rocket Lake" },
            "LGA1700": { years: "2021-2024", cpus: "Alder Lake, Raptor Lake" },
            "LGA1851": { year: 2024, cpus: "Arrow Lake, Lunar Lake" }
        },
        server: ["LGA2011", "LGA2066", "LGA3647", "LGA4189", "LGA4677"]
    },
    amd: {
        vintage: ["Socket A (462)", "Socket 754", "Socket 939", "Socket 940", "AM2", "AM2+", "AM3", "AM3+"],
        modern: {
            "AM4": { years: "2016-2022", cpus: "Ryzen 1000-5000", pins: 1331 },
            "AM5": { year: 2022, cpus: "Ryzen 7000+", type: "LGA 1718" },
            "sTR4": { cpus: "Threadripper 1st/2nd gen" },
            "sTRX4": { cpus: "Threadripper 3rd gen" },
            "sWRX8": { cpus: "Threadripper PRO" }
        }
    }
};

const modernFeatures = {
    powerDelivery: {
        phases: "VRM phases (more = better power delivery)",
        components: ["MOSFETs", "Chokes", "Capacitors"],
        importance: "Critical for CPU overclocking"
    },
    cooling: {
        vrm: "Heatsinks on VRM components",
        m2: "M.2 heatsinks standard on enthusiast boards",
        chipset: "Active or passive chipset cooling"
    },
    connectivity: {
        networking: ["2.5GbE", "5GbE", "10GbE", "WiFi 6E", "WiFi 7"],
        usb: ["USB 3.2 Gen2x2", "USB4", "Thunderbolt 4/5"],
        storage: ["SATA 6Gbps", "M.2 NVMe", "U.2"]
    },
    debugging: {
        postCodes: "2-digit LED display",
        debugLEDs: "CPU, DRAM, VGA, Boot LEDs",
        clearCMOS: "Button or jumper"
    },
    audio: {
        codecs: ["Realtek ALC1220", "ALC4080", "ALC4082"],
        premium: ["ESS Sabre DACs", "Dedicated audio PCB isolation"]
    }
};

app.get('/', (c) => c.json({
    worker: "Motherboard Systems Genius",
    coverage: "Complete motherboard evolution and technology",
    fromS100ToZ890: true,
    endpoints: ['/history', '/form-factors', '/buses', '/chipsets', '/sockets', '/features', '/pcie']
}));

app.get('/history', (c) => c.json(motherboardHistory));
app.get('/form-factors', (c) => c.json(motherboardHistory.formFactors));
app.get('/buses', (c) => c.json(busEvolution));
app.get('/pcie', (c) => c.json(busEvolution.PCIExpress));
app.get('/chipsets', (c) => c.json(chipsetHistory));
app.get('/sockets', (c) => c.json(socketHistory));
app.get('/features', (c) => c.json(modernFeatures));

app.get('/socket/:name', (c) => {
    const name = c.req.param('name').toUpperCase();
    const allSockets = { ...socketHistory.intel.lga, ...socketHistory.amd.modern };
    return c.json(allSockets[name] || { error: "Socket not found", available: Object.keys(allSockets) });
});

app.post('/ai/query', async (c) => {
    const { question } = await c.req.json();
    const context = `Motherboard expert: Form factors (ATX, mATX, ITX), bus evolution (ISA to PCIe 6.0), chipsets (Intel Z-series, AMD X-series), sockets (LGA, AM4, AM5), VRM design, power delivery, connectivity (USB4, Thunderbolt, WiFi 7), BIOS/UEFI, debugging features.`;

    const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
        messages: [
            { role: 'system', content: context },
            { role: 'user', content: question }
        ]
    });
    return c.json({ answer: response.response });
});

export default app;
