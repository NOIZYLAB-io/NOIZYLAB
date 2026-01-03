/**
 * NoizyLab OS - Audio Engine Worker
 * Professional audio processing, synthesis, and format intelligence
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
    AUDIO_ENGINE_DB: D1Database;
    AUDIO_ENGINE_CACHE: KVNamespace;
    AUDIO_ASSETS: R2Bucket;
    AI: any;
    VECTORIZE: any;
}

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// Audio codec knowledge base
const audioCodecs = {
    'aac': {
        name: 'AAC',
        fullName: 'Advanced Audio Coding',
        standard: 'ISO/IEC 14496-3',
        released: 1997,
        profiles: ['AAC-LC', 'HE-AAC', 'HE-AAC v2', 'AAC-LD', 'AAC-ELD'],
        sampleRates: [8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000],
        channels: 'Up to 48 channels',
        bitrates: '8-320 kbps per channel',
        features: ['Perceptual coding', 'Spectral band replication', 'Parametric stereo'],
        useCases: ['iTunes', 'YouTube', 'Streaming', 'Broadcasting']
    },
    'mp3': {
        name: 'MP3',
        fullName: 'MPEG-1 Audio Layer III',
        standard: 'ISO/IEC 11172-3',
        released: 1993,
        sampleRates: [32000, 44100, 48000],
        channels: 'Stereo, Joint Stereo, Dual Channel, Mono',
        bitrates: '32-320 kbps',
        features: ['Psychoacoustic model', 'Huffman coding', 'Modified DCT'],
        useCases: ['Music players', 'Podcasts', 'Web audio']
    },
    'opus': {
        name: 'Opus',
        fullName: 'Opus Interactive Audio Codec',
        standard: 'RFC 6716',
        released: 2012,
        sampleRates: [8000, 12000, 16000, 24000, 48000],
        channels: 'Up to 255 channels',
        bitrates: '6-510 kbps',
        features: ['Hybrid coding', 'Low latency', 'Variable bitrate', 'Royalty-free'],
        useCases: ['WebRTC', 'VoIP', 'Video conferencing', 'Game audio']
    },
    'flac': {
        name: 'FLAC',
        fullName: 'Free Lossless Audio Codec',
        standard: 'Xiph.Org Foundation',
        released: 2001,
        sampleRates: [1 - 655350],
        channels: 'Up to 8 channels',
        bitDepths: ['4-32 bit'],
        features: ['Lossless compression', 'Error detection', 'Seeking support', 'Open source'],
        useCases: ['Archiving', 'Hi-fi audio', 'Music production']
    },
    'alac': {
        name: 'ALAC',
        fullName: 'Apple Lossless Audio Codec',
        standard: 'Apple',
        released: 2004,
        sampleRates: [1 - 384000],
        channels: 'Up to 8 channels',
        bitDepths: ['16, 20, 24, 32 bit'],
        features: ['Lossless', 'Apple ecosystem', 'Open source since 2011'],
        useCases: ['iTunes', 'Apple Music', 'iOS devices']
    },
    'wav': {
        name: 'WAV',
        fullName: 'Waveform Audio File Format',
        standard: 'Microsoft/IBM',
        released: 1991,
        sampleRates: 'Any',
        channels: 'Up to 65535 channels',
        bitDepths: ['8, 16, 24, 32 bit integer', '32, 64 bit float'],
        features: ['Uncompressed', 'Universal support', 'Broadcast Wave (BWF)'],
        useCases: ['Professional audio', 'Mastering', 'Sound design']
    },
    'vorbis': {
        name: 'Vorbis',
        fullName: 'Ogg Vorbis',
        standard: 'Xiph.Org Foundation',
        released: 2000,
        sampleRates: [8000 - 192000],
        channels: 'Up to 255 channels',
        bitrates: '45-500 kbps',
        features: ['Variable bitrate', 'Patent-free', 'High quality at low bitrates'],
        useCases: ['Gaming', 'Streaming', 'Open source projects']
    },
    'dts': {
        name: 'DTS',
        fullName: 'Digital Theater Systems',
        standard: 'DTS Inc.',
        released: 1993,
        variants: ['DTS', 'DTS-HD MA', 'DTS-HD HRA', 'DTS:X'],
        channels: 'Up to 7.1 (or object-based)',
        features: ['Surround sound', 'Object-based audio', 'Cinema quality'],
        useCases: ['Blu-ray', 'Cinema', 'Home theater']
    },
    'dolby': {
        name: 'Dolby',
        fullName: 'Dolby Digital / Dolby Atmos',
        standard: 'Dolby Laboratories',
        released: 1992,
        variants: ['AC-3', 'E-AC-3', 'Dolby TrueHD', 'Dolby Atmos'],
        channels: 'Up to 7.1.4 (or object-based)',
        features: ['Surround sound', 'Height channels', 'Object-based audio'],
        useCases: ['Cinema', 'Streaming', 'Gaming', 'Home theater']
    }
};

// Audio effects knowledge
const audioEffects = {
    dynamics: ['Compressor', 'Limiter', 'Expander', 'Gate', 'De-esser', 'Multiband Compressor'],
    eq: ['Parametric EQ', 'Graphic EQ', 'Shelving', 'High-pass', 'Low-pass', 'Band-pass', 'Notch'],
    time: ['Reverb', 'Delay', 'Echo', 'Chorus', 'Flanger', 'Phaser'],
    distortion: ['Overdrive', 'Fuzz', 'Saturation', 'Bit Crusher', 'Amp Simulation'],
    modulation: ['Tremolo', 'Vibrato', 'Ring Modulator', 'Auto-pan', 'Rotary'],
    pitch: ['Pitch Shift', 'Harmonizer', 'Auto-tune', 'Vocoder'],
    spatial: ['Stereo Widener', 'Mid/Side Processing', 'Binaural Panning', '3D Audio']
};

// Audio history timeline
const audioHistory = [
    { year: 1877, event: 'Thomas Edison invents the phonograph' },
    { year: 1898, event: 'First magnetic wire recorder by Valdemar Poulsen' },
    { year: 1925, event: 'First electrical recording system' },
    { year: 1948, event: 'First commercial vinyl LP released by Columbia' },
    { year: 1958, event: 'First stereo LP records' },
    { year: 1963, event: 'First compact cassette by Philips' },
    { year: 1967, event: 'First 8-track cartridge system' },
    { year: 1972, event: 'First digital audio recording' },
    { year: 1979, event: 'Sony Walkman introduced' },
    { year: 1982, event: 'First commercial CD released' },
    { year: 1987, event: 'DAT (Digital Audio Tape) introduced' },
    { year: 1991, event: 'WAV format introduced by Microsoft' },
    { year: 1993, event: 'MP3 format standardized' },
    { year: 1995, event: 'First portable MP3 player' },
    { year: 1997, event: 'AAC codec standardized' },
    { year: 1999, event: 'Napster launches - digital music revolution' },
    { year: 2000, event: 'Ogg Vorbis released' },
    { year: 2001, event: 'FLAC released', milestone: true },
    { year: 2001, event: 'Apple iPod launched' },
    { year: 2003, event: 'iTunes Store opens' },
    { year: 2004, event: 'Apple Lossless (ALAC) introduced' },
    { year: 2008, event: 'Spotify launches' },
    { year: 2012, event: 'Opus codec released' },
    { year: 2015, event: 'Apple Music launches' },
    { year: 2017, event: 'Dolby Atmos Music introduced' },
    { year: 2021, event: 'Apple Spatial Audio with Dolby Atmos' }
];

// DAW (Digital Audio Workstation) knowledge
const daws = {
    'protools': { name: 'Pro Tools', company: 'Avid', year: 1989, platforms: ['macOS', 'Windows'] },
    'logic': { name: 'Logic Pro', company: 'Apple', year: 1987, platforms: ['macOS'] },
    'ableton': { name: 'Ableton Live', company: 'Ableton', year: 2001, platforms: ['macOS', 'Windows'] },
    'flstudio': { name: 'FL Studio', company: 'Image-Line', year: 1997, platforms: ['macOS', 'Windows'] },
    'cubase': { name: 'Cubase', company: 'Steinberg', year: 1989, platforms: ['macOS', 'Windows'] },
    'reaper': { name: 'REAPER', company: 'Cockos', year: 2006, platforms: ['macOS', 'Windows', 'Linux'] },
    'garageband': { name: 'GarageBand', company: 'Apple', year: 2004, platforms: ['macOS', 'iOS'] },
    'audacity': { name: 'Audacity', company: 'Open Source', year: 2000, platforms: ['macOS', 'Windows', 'Linux'] },
    'studio-one': { name: 'Studio One', company: 'PreSonus', year: 2009, platforms: ['macOS', 'Windows'] },
    'bitwig': { name: 'Bitwig Studio', company: 'Bitwig', year: 2014, platforms: ['macOS', 'Windows', 'Linux'] }
};

// Health check
app.get('/', (c) => {
    return c.json({
        worker: 'audio-engine',
        status: 'operational',
        version: '1.0.0',
        description: 'Professional audio processing and format intelligence',
        capabilities: [
            'Audio codec information',
            'Format conversion guidance',
            'Effect chain recommendations',
            'Bitrate optimization',
            'DAW knowledge',
            'Mastering tips',
            'Spatial audio processing',
            'Sample rate conversion'
        ]
    });
});

// Get all audio codecs
app.get('/codecs', (c) => {
    return c.json({
        codecs: audioCodecs,
        totalCodecs: Object.keys(audioCodecs).length,
        categories: {
            lossy: ['aac', 'mp3', 'opus', 'vorbis'],
            lossless: ['flac', 'alac', 'wav'],
            surround: ['dts', 'dolby']
        }
    });
});

// Get specific codec
app.get('/codecs/:codecId', (c) => {
    const codecId = c.req.param('codecId').toLowerCase();
    const codec = audioCodecs[codecId as keyof typeof audioCodecs];

    if (!codec) {
        return c.json({ error: 'Codec not found', available: Object.keys(audioCodecs) }, 404);
    }

    return c.json(codec);
});

// Get audio effects
app.get('/effects', (c) => {
    const category = c.req.query('category');

    if (category && audioEffects[category as keyof typeof audioEffects]) {
        return c.json({
            category,
            effects: audioEffects[category as keyof typeof audioEffects]
        });
    }

    return c.json({
        effects: audioEffects,
        categories: Object.keys(audioEffects)
    });
});

// Get DAW information
app.get('/daws', (c) => {
    return c.json({
        daws,
        totalDaws: Object.keys(daws).length
    });
});

// Calculate audio parameters
app.post('/calculate', async (c) => {
    const body = await c.req.json();
    const {
        sampleRate = 44100,
        bitDepth = 16,
        channels = 2,
        duration = 180, // seconds
        codec = 'wav'
    } = body;

    // Calculate uncompressed size
    const bytesPerSample = bitDepth / 8;
    const samplesPerSecond = sampleRate * channels;
    const bytesPerSecond = samplesPerSecond * bytesPerSample;
    const uncompressedSizeMB = (bytesPerSecond * duration) / (1024 * 1024);

    // Estimated compressed sizes
    const compressionRatios: Record<string, number> = {
        wav: 1.0,
        flac: 0.5,
        alac: 0.5,
        aac: 0.1,
        mp3: 0.1,
        opus: 0.08,
        vorbis: 0.1
    };

    const ratio = compressionRatios[codec] || 1.0;
    const compressedSizeMB = uncompressedSizeMB * ratio;

    // Bitrate calculations
    const bitrate = (bytesPerSecond * 8) / 1000; // kbps

    return c.json({
        input: { sampleRate, bitDepth, channels, duration, codec },
        calculations: {
            uncompressedSizeMB: uncompressedSizeMB.toFixed(2),
            compressedSizeMB: compressedSizeMB.toFixed(2),
            compressionRatio: `${Math.round((1 - ratio) * 100)}%`,
            bitrateKbps: bitrate.toFixed(0),
            bitrateMbps: (bitrate / 1000).toFixed(2),
            totalSamples: sampleRate * duration,
            nyquistFrequency: sampleRate / 2
        },
        recommendations: {
            musicStreaming: { codec: 'aac', bitrate: '256 kbps', quality: 'High' },
            podcasts: { codec: 'mp3', bitrate: '128 kbps', quality: 'Good' },
            voip: { codec: 'opus', bitrate: '32 kbps', quality: 'Excellent' },
            archival: { codec: 'flac', bitrate: 'Variable', quality: 'Lossless' },
            production: { codec: 'wav', bitrate: `${bitrate} kbps`, quality: 'Uncompressed' }
        },
        ffmpegCommand: `ffmpeg -i input.wav -c:a ${getFFmpegCodec(codec)} ${getFFmpegParams(codec)} output.${getExtension(codec)}`
    });
});

function getFFmpegCodec(codec: string): string {
    const map: Record<string, string> = {
        aac: 'aac', mp3: 'libmp3lame', opus: 'libopus',
        flac: 'flac', alac: 'alac', vorbis: 'libvorbis', wav: 'pcm_s16le'
    };
    return map[codec] || 'copy';
}

function getFFmpegParams(codec: string): string {
    const map: Record<string, string> = {
        aac: '-b:a 256k', mp3: '-b:a 192k', opus: '-b:a 128k',
        flac: '-compression_level 8', alac: '', vorbis: '-q:a 6', wav: ''
    };
    return map[codec] || '';
}

function getExtension(codec: string): string {
    const map: Record<string, string> = {
        aac: 'm4a', mp3: 'mp3', opus: 'opus',
        flac: 'flac', alac: 'm4a', vorbis: 'ogg', wav: 'wav'
    };
    return map[codec] || codec;
}

// Audio history timeline
app.get('/history', (c) => {
    const era = c.req.query('era');
    let filtered = audioHistory;

    if (era === 'analog') {
        filtered = audioHistory.filter(e => e.year < 1982);
    } else if (era === 'digital') {
        filtered = audioHistory.filter(e => e.year >= 1982 && e.year < 2000);
    } else if (era === 'streaming') {
        filtered = audioHistory.filter(e => e.year >= 2000);
    }

    return c.json({
        timeline: filtered,
        totalEvents: filtered.length,
        filter: era || 'all'
    });
});

// AI-powered audio query
app.post('/ask', async (c) => {
    const { question } = await c.req.json();

    if (!question) {
        return c.json({ error: 'Question is required' }, 400);
    }

    try {
        const context = `You are an audio engineering expert with deep knowledge of:
- Audio codecs (AAC, MP3, Opus, FLAC, WAV, etc.)
- Digital audio workstations (Pro Tools, Logic Pro, Ableton, etc.)
- Audio effects and signal processing
- Mastering and mixing techniques
- Spatial audio and surround sound
- Sample rates, bit depths, and audio quality
- Recording techniques and microphone selection

Available codecs: ${Object.keys(audioCodecs).join(', ')}
Effect categories: ${Object.keys(audioEffects).join(', ')}
DAWs: ${Object.keys(daws).join(', ')}`;

        const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
            messages: [
                { role: 'system', content: context },
                { role: 'user', content: question }
            ],
            max_tokens: 1024
        });

        return c.json({
            question,
            answer: response.response,
            sources: ['Audio engineering standards', 'Codec specifications', 'Industry practices'],
            relatedCodecs: Object.keys(audioCodecs).slice(0, 4)
        });
    } catch (error) {
        return c.json({
            question,
            answer: 'Audio engineering knowledge available. For streaming use AAC/Opus, for lossless use FLAC, for production use WAV at 24-bit/48kHz minimum.',
            error: 'AI temporarily unavailable'
        });
    }
});

// Effect chain recommendation
app.post('/effects/recommend', async (c) => {
    const body = await c.req.json();
    const { source = 'vocal', style = 'modern' } = body;

    const chains: Record<string, Record<string, string[]>> = {
        vocal: {
            modern: ['High-pass filter (80Hz)', 'De-esser', 'Compressor (4:1)', 'Parametric EQ', 'Reverb'],
            vintage: ['Preamp saturation', 'LA-2A Compressor', 'Pultec EQ', 'Plate reverb', 'Tape delay'],
            podcast: ['High-pass filter', 'Gate', 'Compressor', 'EQ', 'Limiter']
        },
        drums: {
            modern: ['Gate', 'Transient shaper', 'Parallel compression', 'EQ', 'Bus compression'],
            vintage: ['Tape saturation', '1176 compression', 'SSL EQ', 'Room reverb'],
            electronic: ['Transient designer', 'Saturator', 'Multiband compression', 'Sidechain']
        },
        guitar: {
            modern: ['Noise gate', 'Overdrive', 'Amp sim', 'Cabinet IR', 'Delay', 'Reverb'],
            vintage: ['Tube screamer', 'Fender Twin', 'Spring reverb', 'Tape delay'],
            acoustic: ['High-pass filter', 'Compressor', 'EQ notch (feedback)', 'Room reverb']
        },
        master: {
            modern: ['Linear phase EQ', 'Multiband compression', 'Stereo widener', 'Limiter'],
            vintage: ['Pultec EQ', 'Bus compressor', 'Tape saturation', 'Brick wall limiter'],
            streaming: ['LUFS targeting (-14)', 'True peak limiter', 'Dithering']
        }
    };

    const chain = chains[source]?.[style] || chains.vocal.modern;

    return c.json({
        source,
        style,
        effectChain: chain,
        tips: [
            'Always use high-pass filter on non-bass sources',
            'Apply compression in stages rather than heavy single-stage',
            'Use reference tracks to A/B your mix',
            'Leave headroom for mastering (-6dB peaks)'
        ]
    });
});

export default app;
