import { Hono } from 'hono';

interface Env {
    STORAGE_DB: D1Database;
    STORAGE_KV: KVNamespace;
    AI: any;
}

const app = new Hono<{ Bindings: Env }>();

// Complete storage evolution - from punch cards to NVMe
const storageHistory = {
    punchCards: {
        era: "1890-1970s",
        inventor: "Herman Hollerith",
        capacity: "80 bytes per card",
        legacy: "80-column standard"
    },
    magneticTape: {
        era: "1951-present",
        first: "UNIVAC I (1951)",
        modern: "LTO-9: 18TB native, 45TB compressed",
        use: "Archival, backup",
        futureRoadmap: "LTO-14: 1.44PB compressed"
    },
    magneticDrum: {
        era: "1950s-1960s",
        capacity: "10KB-4MB",
        use: "Primary memory, paging"
    },
    hardDiskDrives: {
        first: { name: "IBM 350 RAMAC", year: 1956, capacity: "5MB", size: "Two refrigerators", platters: 50 },
        milestones: {
            "1973": "IBM Winchester (3340) - sealed unit design",
            "1980": "Seagate ST-506 - 5MB, 5.25\" form factor",
            "1983": "10MB standard for IBM PC XT",
            "1991": "First 2.5\" notebook drive",
            "1998": "IBM Deskstar - first >10GB drive",
            "2003": "First SATA interface drives",
            "2005": "Perpendicular recording (higher density)",
            "2007": "First 1TB drive (Hitachi)",
            "2019": "First 16TB drive (Seagate)",
            "2023": "30TB+ drives with SMR"
        },
        technologies: {
            PMR: "Perpendicular Magnetic Recording",
            SMR: "Shingled Magnetic Recording",
            HAMR: "Heat-Assisted Magnetic Recording",
            MAMR: "Microwave-Assisted Magnetic Recording"
        }
    }
};

const solidStateEvolution = {
    early: {
        first: "StorageTek SSD (1978) - $400,000, RAM-based",
        flash: "M-Systems (1995) - first flash-based SSD"
    },
    interfaces: {
        SATA: { year: 2003, bandwidth: "6 Gbps (SATA III)", latency: "Higher" },
        SAS: { use: "Enterprise", bandwidth: "24 Gbps (SAS-4)" },
        NVMe: { year: 2011, bandwidth: "PCIe dependent", latency: "Lower", parallelism: "64K queues" },
        U2: { use: "Enterprise 2.5\" NVMe" }
    },
    formFactors: {
        "2.5inch": { use: "SATA SSD standard", thickness: "7mm or 9.5mm" },
        "M.2": {
            sizes: ["2230", "2242", "2260", "2280", "22110"],
            keys: { B: "SATA/PCIe x2", M: "PCIe x4", "B+M": "SATA only typically" }
        },
        "U.2": { use: "Enterprise 2.5\" with NVMe" },
        "EDSFF": { types: ["E1.S", "E1.L", "E3.S", "E3.L"], use: "Data center" }
    },
    NVMe: {
        gen3: { perLane: "985 MB/s", x4: "3940 MB/s" },
        gen4: { perLane: "1969 MB/s", x4: "7880 MB/s" },
        gen5: { perLane: "3938 MB/s", x4: "15750 MB/s" },
        controllers: ["Phison E18", "Phison E26", "Samsung Elpis", "WD Black G2", "Innogrit IG5236"]
    }
};

const opticalStorage = {
    CD: { year: 1982, capacity: "700MB", technology: "780nm laser" },
    DVD: { year: 1996, capacity: "4.7GB (single)/8.5GB (dual)", technology: "650nm laser" },
    BluRay: { year: 2006, capacity: "25GB (single)/50GB (dual)/128GB (BDXL)", technology: "405nm laser" },
    HDDVD: { year: 2006, capacity: "15GB/30GB", status: "Failed format war" },
    UHDBluRay: { year: 2015, capacity: "66GB/100GB", features: "4K HDR video" }
};

const networkStorage = {
    SAN: {
        technology: "Storage Area Network",
        protocols: ["Fibre Channel", "iSCSI", "FCoE"],
        use: "Enterprise block storage"
    },
    NAS: {
        technology: "Network Attached Storage",
        protocols: ["NFS", "SMB/CIFS", "AFP"],
        use: "File sharing, home/SOHO storage"
    },
    objectStorage: {
        examples: ["AWS S3", "Azure Blob", "Cloudflare R2"],
        protocol: "HTTP/REST APIs",
        use: "Cloud-native applications, unstructured data"
    }
};

const fileSystemEvolution = {
    FAT: { versions: ["FAT12", "FAT16", "FAT32", "exFAT"], creator: "Microsoft" },
    NTFS: { year: 1993, features: ["Journaling", "ACLs", "Compression", "Encryption"] },
    ext: { versions: ["ext2", "ext3", "ext4"], os: "Linux" },
    XFS: { creator: "SGI", use: "High-performance Linux" },
    Btrfs: { features: ["Copy-on-write", "Snapshots", "RAID"] },
    ZFS: { creator: "Sun", features: ["128-bit", "Checksumming", "RAID-Z", "Dedup"] },
    APFS: { year: 2017, creator: "Apple", features: ["Copy-on-write", "Encryption", "Snapshots"] },
    ReFS: { year: 2012, creator: "Microsoft", use: "Windows Server resilience" }
};

const raidLevels = {
    RAID0: { stripes: true, redundancy: false, performance: "Best", efficiency: "100%" },
    RAID1: { mirrors: true, redundancy: true, overhead: "50%" },
    RAID5: { stripes: true, parity: 1, minDrives: 3, efficiency: "(n-1)/n" },
    RAID6: { stripes: true, parity: 2, minDrives: 4, efficiency: "(n-2)/n" },
    RAID10: { mirrors: true, stripes: true, minDrives: 4, efficiency: "50%" },
    RAIDZ: { type: "ZFS RAID5 equivalent" },
    RAIDZ2: { type: "ZFS RAID6 equivalent" },
    RAIDZ3: { type: "ZFS triple parity" }
};

app.get('/', (c) => c.json({
    worker: "Storage Evolution Genius",
    coverage: "Complete storage technology history",
    fromPunchCardsToNVMe: true,
    endpoints: ['/history', '/ssd', '/optical', '/network', '/filesystems', '/raid', '/nvme']
}));

app.get('/history', (c) => c.json(storageHistory));
app.get('/hdd', (c) => c.json(storageHistory.hardDiskDrives));
app.get('/ssd', (c) => c.json(solidStateEvolution));
app.get('/nvme', (c) => c.json(solidStateEvolution.NVMe));
app.get('/optical', (c) => c.json(opticalStorage));
app.get('/network', (c) => c.json(networkStorage));
app.get('/filesystems', (c) => c.json(fileSystemEvolution));
app.get('/raid', (c) => c.json(raidLevels));

app.get('/capacity-timeline', (c) => c.json({
    "1956": "5MB (IBM RAMAC)",
    "1980": "5MB (Seagate ST-506)",
    "1991": "100MB typical",
    "1998": "10GB milestone",
    "2007": "1TB milestone",
    "2019": "16TB milestone",
    "2024": "30TB+ HDD, 8TB+ SSD consumer"
}));

app.post('/ai/query', async (c) => {
    const { question } = await c.req.json();
    const context = `Storage expert: HDD technology (PMR, SMR, HAMR), SSD/NVMe (NAND types, controllers, Gen3/4/5), interfaces (SATA, SAS, NVMe, U.2), file systems (NTFS, ext4, ZFS, APFS, Btrfs), RAID levels, NAS/SAN, object storage (S3, R2), optical media, tape backup (LTO).`;

    const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
        messages: [
            { role: 'system', content: context },
            { role: 'user', content: question }
        ]
    });
    return c.json({ answer: response.response });
});

export default app;
