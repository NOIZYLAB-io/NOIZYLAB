/**
 * NoizyLab OS - Computing History Worker
 * 
 * The ultimate historical computing knowledge base covering every
 * significant machine, innovation, and breakthrough since the dawn
 * of computing.
 * 
 * Features:
 * - Complete computing timeline (1800s-present)
 * - Historical machine specifications
 * - Pioneering figure biographies
 * - Architecture evolution tracking
 * - Software milestone documentation
 * - Patent and innovation history
 * - Retrocomputing support
 * - Emulator recommendations
 * - Historical code preservation
 * - Museum and archive links
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  DB: D1Database;
  HISTORY_CACHE: KVNamespace;
  AI: any;
  ENVIRONMENT: string;
}

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// ===========================================
// COMPUTING TIMELINE
// ===========================================

const COMPUTING_TIMELINE: Record<string, any[]> = {
  'mechanical-era': [
    { year: 1642, event: 'Pascaline', description: 'Blaise Pascal invents mechanical calculator', significance: 'First mechanical adding machine' },
    { year: 1673, event: 'Leibniz Wheel', description: 'Gottfried Leibniz creates stepped drum calculator', significance: 'First to multiply mechanically' },
    { year: 1801, event: 'Jacquard Loom', description: 'Joseph Marie Jacquard uses punch cards for weaving', significance: 'First programmable machine' },
    { year: 1822, event: 'Difference Engine', description: 'Charles Babbage designs automatic calculating machine', significance: 'First automatic calculator design' },
    { year: 1837, event: 'Analytical Engine', description: 'Babbage designs general-purpose computer', significance: 'First general-purpose computer design' },
    { year: 1843, event: 'First Program', description: 'Ada Lovelace writes first algorithm', significance: 'First computer programmer' },
    { year: 1890, event: 'Tabulating Machine', description: 'Herman Hollerith creates census machine', significance: 'Founded company that became IBM' },
  ],
  'electromechanical-era': [
    { year: 1936, event: 'Turing Machine', description: 'Alan Turing publishes theoretical computer model', significance: 'Foundation of computer science' },
    { year: 1937, event: 'ABC Computer', description: 'Atanasoff-Berry Computer begun', significance: 'First electronic digital computer' },
    { year: 1941, event: 'Z3', description: 'Konrad Zuse builds first programmable computer', significance: 'First working programmable computer' },
    { year: 1943, event: 'Colossus', description: 'British codebreaking computer operational', significance: 'First electronic programmable computer' },
    { year: 1944, event: 'Harvard Mark I', description: 'IBM/Harvard electromechanical computer', significance: 'First American programmable computer' },
    { year: 1945, event: 'ENIAC', description: 'Electronic Numerical Integrator and Computer', significance: 'First general-purpose electronic computer' },
    { year: 1945, event: 'von Neumann Architecture', description: 'John von Neumann proposes stored-program concept', significance: 'Foundation of modern computer architecture' },
  ],
  'mainframe-era': [
    { year: 1951, event: 'UNIVAC I', description: 'First commercial computer in US', significance: 'Predicted 1952 election results' },
    { year: 1952, event: 'IBM 701', description: 'IBM\'s first commercial scientific computer', significance: 'Established IBM in computing' },
    { year: 1956, event: 'Hard Disk Drive', description: 'IBM 305 RAMAC with first HDD', significance: 'Random access storage revolution' },
    { year: 1957, event: 'FORTRAN', description: 'First high-level programming language', significance: 'Made programming accessible' },
    { year: 1958, event: 'Integrated Circuit', description: 'Jack Kilby and Robert Noyce invent IC', significance: 'Foundation of modern electronics' },
    { year: 1959, event: 'COBOL', description: 'Common business programming language', significance: 'Still running today' },
    { year: 1964, event: 'IBM System/360', description: 'Family of compatible mainframes', significance: 'Defined modern computer industry' },
    { year: 1969, event: 'ARPANET', description: 'First packet-switched network', significance: 'Precursor to Internet' },
    { year: 1969, event: 'UNIX', description: 'Ken Thompson and Dennis Ritchie at Bell Labs', significance: 'Foundation of modern operating systems' },
  ],
  'minicomputer-era': [
    { year: 1965, event: 'PDP-8', description: 'First successful minicomputer', significance: 'Made computers accessible to smaller organizations' },
    { year: 1970, event: 'PDP-11', description: 'Most successful minicomputer', significance: 'Ran original UNIX' },
    { year: 1971, event: 'Intel 4004', description: 'First microprocessor', significance: 'Computer on a chip' },
    { year: 1972, event: 'C Language', description: 'Dennis Ritchie creates C', significance: 'Most influential programming language' },
    { year: 1973, event: 'Ethernet', description: 'Bob Metcalfe invents Ethernet', significance: 'Foundation of local networking' },
    { year: 1973, event: 'Xerox Alto', description: 'First computer with GUI', significance: 'Inspired Macintosh and Windows' },
    { year: 1974, event: 'Intel 8080', description: 'First widely adopted microprocessor', significance: 'Powered first personal computers' },
    { year: 1975, event: 'Altair 8800', description: 'First successful personal computer kit', significance: 'Launched PC industry' },
    { year: 1975, event: 'Microsoft Founded', description: 'Bill Gates and Paul Allen start Microsoft', significance: 'Software industry beginning' },
  ],
  'personal-computer-era': [
    { year: 1976, event: 'Apple I', description: 'Steve Wozniak designs first Apple', significance: 'Apple Computer founded' },
    { year: 1977, event: 'Apple II', description: 'First successful mass-produced PC', significance: 'Defined personal computing' },
    { year: 1977, event: 'Commodore PET', description: 'First all-in-one personal computer', significance: 'Business computing pioneer' },
    { year: 1977, event: 'TRS-80', description: 'Radio Shack personal computer', significance: 'Made PCs mainstream' },
    { year: 1979, event: 'VisiCalc', description: 'First spreadsheet software', significance: '"Killer app" for personal computers' },
    { year: 1981, event: 'IBM PC', description: 'IBM Personal Computer', significance: 'Established PC standard' },
    { year: 1981, event: 'MS-DOS', description: 'Microsoft Disk Operating System', significance: 'Foundation of Microsoft empire' },
    { year: 1983, event: 'TCP/IP', description: 'ARPANET adopts TCP/IP', significance: 'Birth of modern Internet' },
    { year: 1984, event: 'Macintosh', description: 'Apple Macintosh with GUI', significance: 'Mainstream graphical interface' },
    { year: 1985, event: 'Windows 1.0', description: 'Microsoft Windows released', significance: 'Start of Windows dominance' },
    { year: 1985, event: 'Intel 80386', description: 'First 32-bit x86 processor', significance: 'Foundation of modern PCs' },
    { year: 1989, event: 'World Wide Web', description: 'Tim Berners-Lee invents WWW', significance: 'Transformed human communication' },
  ],
  'internet-era': [
    { year: 1991, event: 'Linux', description: 'Linus Torvalds releases Linux kernel', significance: 'Open source revolution' },
    { year: 1993, event: 'Mosaic', description: 'First graphical web browser', significance: 'Made web accessible' },
    { year: 1995, event: 'Java', description: 'Sun Microsystems releases Java', significance: '"Write once, run anywhere"' },
    { year: 1995, event: 'Windows 95', description: 'Microsoft Windows 95', significance: 'Mainstream GUI computing' },
    { year: 1995, event: 'JavaScript', description: 'Brendan Eich creates JavaScript', significance: 'Web interactivity' },
    { year: 1998, event: 'Google Founded', description: 'Larry Page and Sergey Brin start Google', significance: 'Search engine dominance' },
    { year: 1999, event: 'WiFi', description: '802.11b wireless networking standard', significance: 'Wireless connectivity mainstream' },
    { year: 2001, event: 'Mac OS X', description: 'Apple releases Unix-based OS X', significance: 'Modern Apple platform' },
    { year: 2001, event: 'Wikipedia', description: 'Wikipedia launched', significance: 'Collaborative knowledge' },
    { year: 2004, event: 'Facebook', description: 'Mark Zuckerberg launches Facebook', significance: 'Social media era' },
  ],
  'mobile-cloud-era': [
    { year: 2006, event: 'AWS', description: 'Amazon Web Services launched', significance: 'Cloud computing revolution' },
    { year: 2007, event: 'iPhone', description: 'Apple iPhone released', significance: 'Smartphone revolution' },
    { year: 2008, event: 'Android', description: 'Google Android released', significance: 'Open mobile platform' },
    { year: 2008, event: 'GitHub', description: 'GitHub launched', significance: 'Social coding' },
    { year: 2010, event: 'iPad', description: 'Apple iPad released', significance: 'Tablet computing' },
    { year: 2011, event: 'IBM Watson', description: 'Watson wins Jeopardy!', significance: 'AI milestone' },
    { year: 2012, event: 'Deep Learning', description: 'AlexNet wins ImageNet', significance: 'Deep learning revolution' },
    { year: 2014, event: 'Swift', description: 'Apple releases Swift language', significance: 'Modern Apple development' },
    { year: 2016, event: 'AlphaGo', description: 'DeepMind AI beats Go champion', significance: 'AI surpasses human in complex game' },
    { year: 2017, event: 'Transformer', description: '"Attention Is All You Need" paper', significance: 'Foundation of modern AI' },
  ],
  'ai-era': [
    { year: 2020, event: 'GPT-3', description: 'OpenAI releases GPT-3', significance: 'Large language model breakthrough' },
    { year: 2020, event: 'Apple Silicon', description: 'Apple M1 chip released', significance: 'ARM desktop computing' },
    { year: 2022, event: 'ChatGPT', description: 'OpenAI releases ChatGPT', significance: 'AI goes mainstream' },
    { year: 2022, event: 'Stable Diffusion', description: 'Open source image generation', significance: 'Democratized AI art' },
    { year: 2023, event: 'GPT-4', description: 'OpenAI GPT-4 multimodal AI', significance: 'Multimodal AI systems' },
    { year: 2024, event: 'Claude 3', description: 'Anthropic releases Claude 3', significance: 'Constitutional AI advances' },
    { year: 2024, event: 'Apple Intelligence', description: 'Apple integrates AI into products', significance: 'On-device AI' },
  ]
};

// ===========================================
// HISTORICAL MACHINES DATABASE
// ===========================================

const HISTORICAL_MACHINES: Record<string, any> = {
  'eniac': {
    name: 'ENIAC',
    fullName: 'Electronic Numerical Integrator and Computer',
    year: 1945,
    location: 'University of Pennsylvania',
    inventors: ['John Mauchly', 'J. Presper Eckert'],
    specs: {
      weight: '30 tons',
      size: '1,800 square feet',
      power: '150 kilowatts',
      tubes: 17468,
      memory: '20 words',
      speed: '5,000 additions/second'
    },
    significance: 'First general-purpose electronic computer',
    fate: 'Disassembled 1955, parts at Smithsonian'
  },
  'univac-i': {
    name: 'UNIVAC I',
    fullName: 'Universal Automatic Computer I',
    year: 1951,
    manufacturer: 'Remington Rand',
    inventors: ['John Mauchly', 'J. Presper Eckert'],
    specs: {
      weight: '16,000 lbs',
      memory: '1000 words (12,000 characters)',
      speed: '1,905 operations/second',
      wordLength: '12 decimal digits',
      storage: 'Mercury delay lines',
      input: 'Magnetic tape'
    },
    significance: 'First commercial computer in US',
    notable: 'Predicted 1952 election results'
  },
  'pdp-8': {
    name: 'PDP-8',
    fullName: 'Programmed Data Processor-8',
    year: 1965,
    manufacturer: 'Digital Equipment Corporation',
    designer: 'Edson de Castro',
    specs: {
      wordLength: '12 bits',
      memory: '4K words (expandable)',
      speed: '1.5 microseconds',
      price: '$18,000',
      weight: '250 lbs'
    },
    significance: 'First successful minicomputer',
    units: '50,000 sold'
  },
  'altair-8800': {
    name: 'Altair 8800',
    year: 1975,
    manufacturer: 'MITS',
    designer: 'Ed Roberts',
    processor: 'Intel 8080',
    specs: {
      memory: '256 bytes (expandable)',
      price: '$439 kit, $621 assembled',
      programming: 'Front panel switches'
    },
    significance: 'Launched personal computer industry',
    notable: 'Microsoft wrote first product (Altair BASIC) for it'
  },
  'apple-ii': {
    name: 'Apple II',
    year: 1977,
    manufacturer: 'Apple Computer',
    designers: ['Steve Wozniak', 'Steve Jobs'],
    processor: 'MOS 6502 @ 1 MHz',
    specs: {
      memory: '4-48 KB RAM',
      display: '40x24 text, 280x192 graphics',
      colors: 6,
      storage: 'Cassette tape, later floppy disk',
      price: '$1,298'
    },
    significance: 'First successful mass-produced personal computer',
    units: '5-6 million sold'
  },
  'ibm-pc': {
    name: 'IBM Personal Computer',
    model: '5150',
    year: 1981,
    manufacturer: 'IBM',
    processor: 'Intel 8088 @ 4.77 MHz',
    specs: {
      memory: '16-256 KB RAM',
      display: 'MDA or CGA',
      storage: 'Cassette or floppy',
      os: 'PC DOS (MS-DOS)',
      price: '$1,565'
    },
    significance: 'Established IBM PC standard',
    architecture: 'Open architecture led to clone industry'
  },
  'macintosh': {
    name: 'Macintosh 128K',
    year: 1984,
    manufacturer: 'Apple Computer',
    processor: 'Motorola 68000 @ 8 MHz',
    specs: {
      memory: '128 KB RAM',
      display: '512x342 monochrome',
      storage: '400K floppy',
      os: 'System 1.0',
      price: '$2,495'
    },
    significance: 'Brought GUI to mainstream',
    notable: '1984 Super Bowl commercial'
  },
  'commodore-64': {
    name: 'Commodore 64',
    year: 1982,
    manufacturer: 'Commodore',
    processor: 'MOS 6510 @ 1 MHz',
    specs: {
      memory: '64 KB RAM',
      display: '320x200 16 colors',
      sound: 'SID chip (3 voices)',
      price: '$595 (later $199)',
    },
    significance: 'Best-selling computer model ever',
    units: '12.5-17 million sold'
  },
  'cray-1': {
    name: 'Cray-1',
    year: 1976,
    manufacturer: 'Cray Research',
    designer: 'Seymour Cray',
    specs: {
      speed: '160 MFLOPS',
      memory: '8 MB',
      wordLength: '64 bits',
      cooling: 'Freon',
      power: '115 kW',
      price: '$8.8 million',
      weight: '5.5 tons'
    },
    significance: 'First successful vector supercomputer',
    notable: 'Iconic C-shaped design with bench seating'
  }
};

// ===========================================
// PIONEERS DATABASE
// ===========================================

const COMPUTING_PIONEERS: Record<string, any> = {
  'ada-lovelace': {
    name: 'Ada Lovelace',
    birth: 1815,
    death: 1852,
    nationality: 'British',
    contributions: [
      'First computer programmer',
      'Notes on Analytical Engine',
      'First algorithm intended for machine processing'
    ],
    awards: ['Ada programming language named after her'],
    quote: 'The Analytical Engine weaves algebraic patterns just as the Jacquard loom weaves flowers and leaves.'
  },
  'alan-turing': {
    name: 'Alan Turing',
    birth: 1912,
    death: 1954,
    nationality: 'British',
    contributions: [
      'Turing machine concept',
      'Breaking Enigma code',
      'Turing test for AI',
      'ACE computer design'
    ],
    awards: ['Turing Award named after him', 'OBE'],
    quote: 'We can only see a short distance ahead, but we can see plenty there that needs to be done.'
  },
  'john-von-neumann': {
    name: 'John von Neumann',
    birth: 1903,
    death: 1957,
    nationality: 'Hungarian-American',
    contributions: [
      'von Neumann architecture',
      'EDVAC design',
      'Game theory',
      'Cellular automata'
    ],
    significance: 'Father of modern computer architecture',
    quote: 'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.'
  },
  'grace-hopper': {
    name: 'Grace Hopper',
    birth: 1906,
    death: 1992,
    nationality: 'American',
    rank: 'Rear Admiral, US Navy',
    contributions: [
      'First compiler (A-0)',
      'COBOL development',
      'Popularized term "debugging"'
    ],
    awards: ['Presidential Medal of Freedom', 'Defense Distinguished Service Medal'],
    quote: 'The most dangerous phrase in the language is "we\'ve always done it this way."'
  },
  'dennis-ritchie': {
    name: 'Dennis Ritchie',
    birth: 1941,
    death: 2011,
    nationality: 'American',
    contributions: [
      'C programming language',
      'UNIX operating system (with Ken Thompson)',
      'Plan 9'
    ],
    awards: ['Turing Award', 'National Medal of Technology'],
    quote: 'UNIX is basically a simple operating system, but you have to be a genius to understand the simplicity.'
  },
  'steve-wozniak': {
    name: 'Steve Wozniak',
    birth: 1950,
    nationality: 'American',
    contributions: [
      'Apple I and Apple II design',
      'Apple Computer co-founder',
      'Floppy disk controller',
      'Apple DOS'
    ],
    awards: ['National Medal of Technology', 'ACM Grace Murray Hopper Award'],
    significance: 'Father of personal computing'
  },
  'linus-torvalds': {
    name: 'Linus Torvalds',
    birth: 1969,
    nationality: 'Finnish-American',
    contributions: [
      'Linux kernel',
      'Git version control'
    ],
    awards: ['Millennium Technology Prize', 'IEEE Computer Pioneer Award'],
    quote: 'Talk is cheap. Show me the code.'
  }
};

// ===========================================
// API ENDPOINTS
// ===========================================

app.get('/history/timeline', async (c) => {
  const era = c.req.query('era');
  const decade = c.req.query('decade');
  
  if (era) {
    return c.json({
      success: true,
      era,
      events: COMPUTING_TIMELINE[era] || []
    });
  }
  
  if (decade) {
    const startYear = parseInt(decade);
    const allEvents = Object.values(COMPUTING_TIMELINE).flat();
    const filtered = allEvents.filter((e: any) => e.year >= startYear && e.year < startYear + 10);
    return c.json({
      success: true,
      decade,
      events: filtered.sort((a: any, b: any) => a.year - b.year)
    });
  }
  
  return c.json({
    success: true,
    eras: Object.keys(COMPUTING_TIMELINE),
    totalEvents: Object.values(COMPUTING_TIMELINE).flat().length
  });
});

app.get('/history/machine/:id', async (c) => {
  const id = c.req.param('id');
  const machine = HISTORICAL_MACHINES[id];
  
  if (!machine) {
    return c.json({ success: false, error: 'Machine not found' }, 404);
  }
  
  return c.json({
    success: true,
    machine,
    relatedMachines: findRelatedMachines(machine)
  });
});

app.get('/history/machines', async (c) => {
  const era = c.req.query('era');
  const type = c.req.query('type');
  
  let machines = Object.entries(HISTORICAL_MACHINES).map(([id, m]) => ({ id, ...m }));
  
  if (era) {
    const yearRanges: Record<string, number[]> = {
      'mainframe': [1940, 1960],
      'minicomputer': [1960, 1975],
      'microcomputer': [1975, 1985],
      'pc': [1980, 2000]
    };
    const range = yearRanges[era];
    if (range) {
      machines = machines.filter(m => m.year >= range[0] && m.year <= range[1]);
    }
  }
  
  return c.json({
    success: true,
    machines
  });
});

app.get('/history/pioneer/:id', async (c) => {
  const id = c.req.param('id');
  const pioneer = COMPUTING_PIONEERS[id];
  
  if (!pioneer) {
    return c.json({ success: false, error: 'Pioneer not found' }, 404);
  }
  
  return c.json({
    success: true,
    pioneer
  });
});

app.get('/history/pioneers', async (c) => {
  const pioneers = Object.entries(COMPUTING_PIONEERS).map(([id, p]) => ({
    id,
    name: p.name,
    birth: p.birth,
    death: p.death,
    primaryContribution: p.contributions[0]
  }));
  
  return c.json({
    success: true,
    pioneers
  });
});

app.get('/history/search', async (c) => {
  const env = c.env;
  const query = c.req.query('q') || '';
  const queryLower = query.toLowerCase();
  
  // Search timeline
  const timelineResults = Object.values(COMPUTING_TIMELINE)
    .flat()
    .filter((e: any) => 
      e.event?.toLowerCase().includes(queryLower) ||
      e.description?.toLowerCase().includes(queryLower)
    );
  
  // Search machines
  const machineResults = Object.entries(HISTORICAL_MACHINES)
    .filter(([id, m]) => 
      m.name?.toLowerCase().includes(queryLower) ||
      m.fullName?.toLowerCase().includes(queryLower) ||
      m.significance?.toLowerCase().includes(queryLower)
    )
    .map(([id, m]) => ({ id, name: m.name, year: m.year, type: 'machine' }));
  
  // Search pioneers
  const pioneerResults = Object.entries(COMPUTING_PIONEERS)
    .filter(([id, p]) => 
      p.name?.toLowerCase().includes(queryLower) ||
      p.contributions?.some((c: string) => c.toLowerCase().includes(queryLower))
    )
    .map(([id, p]) => ({ id, name: p.name, type: 'pioneer' }));
  
  return c.json({
    success: true,
    query,
    results: {
      events: timelineResults,
      machines: machineResults,
      pioneers: pioneerResults,
      total: timelineResults.length + machineResults.length + pioneerResults.length
    }
  });
});

app.post('/history/ask', async (c) => {
  const env = c.env;
  const { question } = await c.req.json();
  
  const prompt = `You are a computing history expert. Answer this question about computing history:

${question}

Provide accurate historical information with dates and sources when possible.`;

  try {
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      prompt,
      max_tokens: 1000
    });
    
    return c.json({
      success: true,
      question,
      answer: response.response
    });
  } catch (error) {
    return c.json({
      success: false,
      error: 'Failed to generate answer'
    });
  }
});

app.get('/history/emulators', async (c) => {
  const emulators = {
    'apple-ii': [
      { name: 'AppleWin', platform: 'Windows', url: 'https://github.com/AppleWin/AppleWin' },
      { name: 'Virtual ][', platform: 'macOS', url: 'http://www.virtualii.com/' },
      { name: 'JACE', platform: 'Web/Java', url: 'https://github.com/badvision/jace' },
    ],
    'commodore-64': [
      { name: 'VICE', platform: 'Cross-platform', url: 'https://vice-emu.sourceforge.io/' },
      { name: 'C64 Forever', platform: 'Windows', url: 'https://www.c64forever.com/' },
    ],
    'dos': [
      { name: 'DOSBox', platform: 'Cross-platform', url: 'https://www.dosbox.com/' },
      { name: 'DOSBox-X', platform: 'Cross-platform', url: 'https://dosbox-x.com/' },
    ],
    'classic-mac': [
      { name: 'Mini vMac', platform: 'Cross-platform', url: 'https://www.gryphel.com/c/minivmac/' },
      { name: 'Basilisk II', platform: 'Cross-platform', url: 'https://basilisk.cebix.net/' },
      { name: 'SheepShaver', platform: 'Cross-platform', url: 'https://sheepshaver.cebix.net/' },
    ],
    'amiga': [
      { name: 'WinUAE', platform: 'Windows', url: 'https://www.winuae.net/' },
      { name: 'FS-UAE', platform: 'Cross-platform', url: 'https://fs-uae.net/' },
    ],
    'atari': [
      { name: 'Stella', platform: 'Cross-platform', url: 'https://stella-emu.github.io/' },
      { name: 'Hatari', platform: 'Cross-platform', url: 'https://hatari.tuxfamily.org/' },
    ],
  };
  
  return c.json({
    success: true,
    emulators,
    note: 'Use legally obtained ROMs only'
  });
});

app.get('/history/museums', async (c) => {
  const museums = [
    { name: 'Computer History Museum', location: 'Mountain View, CA', url: 'https://computerhistory.org/', highlights: ['PDP-1', 'Cray-1', 'Apple I'] },
    { name: 'The National Museum of Computing', location: 'Bletchley Park, UK', url: 'https://www.tnmoc.org/', highlights: ['Colossus', 'WITCH', 'Tunny'] },
    { name: 'Heinz Nixdorf MuseumsForum', location: 'Paderborn, Germany', url: 'https://www.hnf.de/', highlights: ['Largest computer museum in the world'] },
    { name: 'Living Computer Museum', location: 'Seattle, WA', url: 'https://livingcomputers.org/', highlights: ['Working vintage mainframes'] },
    { name: 'Computer Museum of America', location: 'Roswell, GA', url: 'https://computermuseumofamerica.org/', highlights: ['Apple collection', 'IBM collection'] },
  ];
  
  return c.json({
    success: true,
    museums
  });
});

// ===========================================
// HELPER FUNCTIONS
// ===========================================

function findRelatedMachines(machine: any): string[] {
  const related: string[] = [];
  const year = machine.year;
  
  Object.entries(HISTORICAL_MACHINES).forEach(([id, m]) => {
    if (m.name !== machine.name && Math.abs(m.year - year) <= 5) {
      related.push(id);
    }
  });
  
  return related.slice(0, 5);
}

export default app;
