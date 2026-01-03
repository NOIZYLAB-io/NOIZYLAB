import { Hono } from 'hono';

interface Env {
    HCI_DB: D1Database;
    HCI_KV: KVNamespace;
    AI: any;
}

const app = new Hono<{ Bindings: Env }>();

// Complete Human-Computer Interaction evolution
const inputDeviceHistory = {
    punchCards: {
        era: "1890-1970s",
        inventor: "Herman Hollerith",
        originalUse: "1890 US Census",
        columns: 80,
        legacy: "80-column terminal standard"
    },
    teletypes: {
        era: "1930s-1980s",
        technology: "Electromechanical typewriters",
        protocol: "RS-232 serial",
        legacy: "TTY device names in Unix"
    },
    keyboards: {
        QWERTY: { year: 1873, inventor: "Christopher Sholes", reason: "Reduce jamming" },
        IBM_Model_M: { year: 1984, technology: "Buckling spring", legendary: true },
        DEC_LK201: { year: 1982, pioneered: "Function key layout" },
        membrane: { era: "1980s-present", common: true },
        mechanical: { switches: ["Cherry MX", "Alps", "Topre", "Kailh", "Gateron"] },
        ergonomic: { examples: ["Microsoft Natural", "Kinesis Advantage", "ErgoDox"] }
    },
    mice: {
        first: { year: 1964, inventor: "Douglas Engelbart", type: "Wooden, two wheels" },
        ball: { era: "1970s-2000s", mechanism: "Rubber ball + rollers" },
        optical: { year: 1999, pioneer: "Microsoft IntelliMouse Explorer" },
        laser: { year: 2004, improvement: "More surface compatibility" },
        gaming: { features: ["High DPI", "Low latency", "Programmable buttons"] }
    },
    trackballs: { advantage: "Stationary, less desk space", usage: "CAD, accessibility" },
    touchpads: { year: 1994, pioneer: "Apple PowerBook 500", technology: "Capacitive" },
    trackpoints: { year: 1992, inventor: "IBM ThinkPad", nickname: "Pointing stick" }
};

const displayEvolution = {
    CRT: {
        inventor: "Karl Ferdinand Braun (1897)",
        principle: "Electron beam on phosphor screen",
        era: "1950s-2000s",
        refresh: "60-85Hz typical",
        response: "Near instant phosphor decay"
    },
    LCD: {
        TN: { year: 1970s, response: "Fast", viewingAngles: "Poor", colorAccuracy: "Moderate" },
        IPS: { year: 1996, response: "Slower", viewingAngles: "Excellent", colorAccuracy: "High" },
        VA: { year: 1996, contrast: "Best", viewingAngles: "Good", response: "Medium" }
    },
    OLED: {
        principle: "Organic compounds emit light",
        advantages: ["Perfect blacks", "Thin", "Fast response", "Wide viewing angles"],
        concerns: ["Burn-in", "Cost", "Brightness limits"]
    },
    miniLED: { principle: "Thousands of LED backlight zones", benefit: "LCD with better HDR" },
    microLED: { principle: "Self-emissive LED pixels", future: "OLED benefits without burn-in" }
};

const guiHistory = {
    xeroxAlto: { year: 1973, first: "GUI with mouse, windows, WYSIWYG" },
    xeroxStar: { year: 1981, introduced: "Desktop metaphor, icons, folders" },
    appleLisa: { year: 1983, features: ["Pull-down menus", "Clipboard"] },
    macintosh: { year: 1984, milestone: "First mass-market GUI" },
    amigaWorkbench: { year: 1985, features: ["Multitasking GUI", "Color icons"] },
    windows1: { year: 1985, type: "Tiled window manager" },
    windows3: { year: 1990, milestone: "First successful Windows" },
    windows95: { year: 1995, introduced: ["Start menu", "Taskbar", "Long filenames"] },
    macOSX: { year: 2001, features: ["Aqua interface", "Unix foundation"] },
    windows7: { year: 2009, refined: "Aero Glass, improved taskbar" },
    flatDesign: { year: 2012, pioneers: ["Windows 8", "iOS 7"], trend: "Minimal, flat aesthetics" },
    materialDesign: { year: 2014, creator: "Google", principles: "Paper metaphor, shadows" },
    fluentDesign: { year: 2017, creator: "Microsoft", features: ["Acrylic", "Reveal", "Depth"] }
};

const touchAndGesture = {
    multiTouch: {
        pioneer: "Jeff Han (2006)",
        mainstream: "iPhone (2007)",
        gestures: ["Pinch to zoom", "Swipe", "Rotate", "Multi-finger taps"]
    },
    stylus: {
        wacom: { year: 1984, technology: "Electromagnetic resonance" },
        applePencil: { year: 2015, features: ["Pressure", "Tilt", "Low latency"] },
        surfacePen: { technology: "N-trig" }
    },
    voiceControl: {
        speechRecognition: { pioneers: ["Dragon Dictate", "ViaVoice"] },
        virtualAssistants: ["Siri (2011)", "Google Now (2012)", "Alexa (2014)", "Cortana (2014)"]
    },
    gestureControl: {
        kinect: { year: 2010, technology: "Depth camera + IR" },
        leapMotion: { year: 2013, technology: "Hand tracking" }
    },
    eyeTracking: {
        use: ["Accessibility", "Gaming", "Research"],
        products: ["Tobii Eye Tracker", "Eye Tribe"]
    },
    brainComputerInterface: {
        research: ["Neuralink", "OpenBCI", "Emotiv"],
        applications: ["Accessibility", "Gaming", "Medical"]
    }
};

const vrArHistory = {
    earlyVR: {
        sensorama: { year: 1962, creator: "Morton Heilig", type: "Multi-sensory experience" },
        swordOfDamocles: { year: 1968, creator: "Ivan Sutherland", first: "Head-mounted display" }
    },
    modernVR: {
        oculusRift: { year: 2012, kickstarter: "VR renaissance" },
        HTCVive: { year: 2016, feature: "Room-scale tracking" },
        valveIndex: { year: 2019, feature: "High refresh rate, finger tracking" },
        quest2: { year: 2020, breakthrough: "Standalone VR mainstream" },
        appleVisionPro: { year: 2024, feature: "Spatial computing, pass-through AR" }
    },
    AR: {
        googleGlass: { year: 2013, attempt: "Consumer AR" },
        hololens: { year: 2016, feature: "Mixed reality, enterprise focus" },
        magicLeap: { year: 2018, technology: "Waveguide optics" }
    }
};

app.get('/', (c) => c.json({
    worker: "HCI Evolution Genius",
    coverage: "Complete Human-Computer Interaction history",
    fromPunchCardsToVR: true,
    endpoints: ['/input', '/displays', '/gui', '/touch', '/vr-ar', '/accessibility']
}));

app.get('/input', (c) => c.json(inputDeviceHistory));
app.get('/keyboards', (c) => c.json(inputDeviceHistory.keyboards));
app.get('/mice', (c) => c.json(inputDeviceHistory.mice));
app.get('/displays', (c) => c.json(displayEvolution));
app.get('/gui', (c) => c.json(guiHistory));
app.get('/touch', (c) => c.json(touchAndGesture));
app.get('/vr-ar', (c) => c.json(vrArHistory));

app.get('/accessibility', (c) => c.json({
    screenReaders: ["JAWS", "NVDA", "VoiceOver", "TalkBack", "Orca"],
    standards: ["WCAG 2.1", "Section 508", "ADA compliance"],
    features: ["High contrast", "Screen magnification", "Voice control", "Switch access"],
    pioneers: ["T.V. Raman (Google)", "Gregg Vanderheiden"]
}));

app.post('/ai/query', async (c) => {
    const { question } = await c.req.json();
    const context = `HCI expert: Input devices (keyboards, mice, touchscreens, stylus), display technology (CRT, LCD, OLED), GUI history (Xerox PARC, Mac, Windows), touch gestures, voice interfaces, VR/AR (Oculus, HoloLens, Vision Pro), accessibility, UX design principles.`;

    const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
        messages: [
            { role: 'system', content: context },
            { role: 'user', content: question }
        ]
    });
    return c.json({ answer: response.response });
});

export default app;
