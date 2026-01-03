/**
 * NoizyLab OS - Video Codec Worker
 * H.264/H.265 video encoding/decoding with OpenH264 v2.6.0 integration
 * Comprehensive video processing knowledge base
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
    VIDEO_CODEC_DB: D1Database;
    VIDEO_CODEC_CACHE: KVNamespace;
    VIDEO_ASSETS: R2Bucket;
    AI: any;
    VECTORIZE: any;
}

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// Video codec knowledge base
const videoCodecs = {
    'h264': {
        name: 'H.264/AVC',
        fullName: 'Advanced Video Coding',
        standard: 'ITU-T H.264 / ISO/IEC 14496-10',
        released: 2003,
        profiles: ['Baseline', 'Main', 'High', 'High 10', 'High 4:2:2', 'High 4:4:4'],
        features: ['B-frames', 'CABAC', 'Deblocking filter', 'Multiple reference frames'],
        openH264: {
            version: '2.6.0',
            releaseDate: '2025-02-12',
            license: 'BSD-2-Clause (source), Cisco Binary License (binaries)',
            platforms: ['android-arm', 'android-arm64', 'android-x64', 'android-x86',
                'ios', 'linux32', 'linux64', 'linux-arm', 'linux-arm64',
                'mac-arm64', 'mac-x64', 'win32', 'win64', 'win-arm64'],
            features: [
                'PSNR calculation for Y/U/V components',
                'Temporal layer info via GMP API',
                'LoongArch architecture support',
                'PowerPC support (meson.build)',
                'Windows VC17 compile support',
                'OpenBSD/NetBSD CPU detection'
            ],
            binaryUrl: 'http://ciscobinary.openh264.org/'
        },
        useCases: ['Web video', 'Blu-ray', 'Video conferencing', 'Broadcasting']
    },
    'h265': {
        name: 'H.265/HEVC',
        fullName: 'High Efficiency Video Coding',
        standard: 'ITU-T H.265 / ISO/IEC 23008-2',
        released: 2013,
        profiles: ['Main', 'Main 10', 'Main Still Picture', 'Main 4:2:2 10', 'Main 4:4:4'],
        features: ['CTU up to 64x64', 'Improved entropy coding', '35 intra prediction modes'],
        useCases: ['4K/8K video', 'Streaming', 'Broadcasting', 'Security cameras']
    },
    'av1': {
        name: 'AV1',
        fullName: 'AOMedia Video 1',
        standard: 'AOMedia',
        released: 2018,
        profiles: ['Main', 'High', 'Professional'],
        features: ['Royalty-free', 'Film grain synthesis', 'Super-resolution', 'Reference frame scaling'],
        useCases: ['YouTube', 'Netflix', 'Web streaming', 'Video calls']
    },
    'vp9': {
        name: 'VP9',
        fullName: 'Video Processor 9',
        standard: 'Google/WebM',
        released: 2013,
        profiles: ['Profile 0', 'Profile 1', 'Profile 2', 'Profile 3'],
        features: ['Superframes', 'Parallel decoding', '10/12-bit depth'],
        useCases: ['YouTube', 'WebRTC', 'Chrome browser']
    },
    'prores': {
        name: 'Apple ProRes',
        fullName: 'Apple ProRes Codec Family',
        standard: 'Apple',
        released: 2007,
        variants: ['ProRes 422 Proxy', 'ProRes 422 LT', 'ProRes 422', 'ProRes 422 HQ', 'ProRes 4444', 'ProRes 4444 XQ', 'ProRes RAW'],
        features: ['Intra-frame only', 'Variable bitrate', 'Full-resolution 4:2:2'],
        useCases: ['Final Cut Pro', 'Professional video editing', 'Broadcast']
    },
    'dnxhd': {
        name: 'DNxHD/DNxHR',
        fullName: 'Digital Nonlinear Extensible High Definition',
        standard: 'Avid',
        released: 2004,
        variants: ['DNxHD', 'DNxHR LB', 'DNxHR SQ', 'DNxHR HQ', 'DNxHR HQX', 'DNxHR 444'],
        features: ['Frame-based', 'Predictable bitrate', '10-bit support'],
        useCases: ['Avid Media Composer', 'Broadcast', 'Post-production']
    }
};

// Container formats
const containerFormats = {
    'mp4': {
        name: 'MPEG-4 Part 14',
        extension: '.mp4',
        mimeType: 'video/mp4',
        codecs: ['H.264', 'H.265', 'AAC', 'MP3'],
        features: ['Streaming support', 'Metadata', 'Chapters']
    },
    'mkv': {
        name: 'Matroska',
        extension: '.mkv',
        mimeType: 'video/x-matroska',
        codecs: ['Almost any codec'],
        features: ['Multiple audio/subtitle tracks', 'Chapters', 'Attachments']
    },
    'webm': {
        name: 'WebM',
        extension: '.webm',
        mimeType: 'video/webm',
        codecs: ['VP8', 'VP9', 'AV1', 'Vorbis', 'Opus'],
        features: ['Open format', 'Web optimized', 'Royalty-free']
    },
    'mov': {
        name: 'QuickTime',
        extension: '.mov',
        mimeType: 'video/quicktime',
        codecs: ['ProRes', 'H.264', 'H.265', 'AAC'],
        features: ['Professional quality', 'Timeline editing', 'Apple ecosystem']
    }
};

// Video processing history
const videoHistory = [
    { year: 1951, event: 'First video tape recorder (VTR) by Bing Crosby Enterprises' },
    { year: 1956, event: 'Ampex introduces first commercial VTR' },
    { year: 1967, event: 'First consumer VCR by Sony (CV-2000)' },
    { year: 1975, event: 'Sony Betamax introduced' },
    { year: 1976, event: 'JVC VHS format launched' },
    { year: 1982, event: 'First CD released - digital audio revolution' },
    { year: 1988, event: 'MPEG (Moving Picture Experts Group) established' },
    { year: 1993, event: 'MPEG-1 standard published' },
    { year: 1995, event: 'DVD format announced' },
    { year: 1996, event: 'MPEG-2 enables DVD video' },
    { year: 1999, event: 'MPEG-4 Part 2 released' },
    { year: 2003, event: 'H.264/AVC standard completed' },
    { year: 2006, event: 'Blu-ray format launched' },
    { year: 2008, event: 'VP8 codec released by On2' },
    { year: 2010, event: 'Google acquires On2, open sources VP8' },
    { year: 2013, event: 'H.265/HEVC standard completed' },
    { year: 2013, event: 'VP9 released by Google' },
    { year: 2013, event: 'Cisco open sources OpenH264' },
    { year: 2015, event: 'Alliance for Open Media (AOM) founded' },
    { year: 2018, event: 'AV1 codec released' },
    { year: 2020, event: 'H.266/VVC standard completed' },
    { year: 2025, event: 'OpenH264 v2.6.0 with expanded platform support' }
];

// Health check
app.get('/', (c) => {
    return c.json({
        worker: 'video-codec',
        status: 'operational',
        version: '1.0.0',
        description: 'Video encoding/decoding and codec intelligence',
        openH264Version: '2.6.0',
        capabilities: [
            'H.264/AVC encoding parameters',
            'H.265/HEVC optimization',
            'AV1/VP9 web codecs',
            'ProRes/DNxHD professional formats',
            'Container format guidance',
            'OpenH264 integration',
            'Bitrate calculation',
            'Quality optimization'
        ]
    });
});

// Get codec information
app.get('/codecs', (c) => {
    return c.json({
        codecs: videoCodecs,
        containers: containerFormats,
        totalCodecs: Object.keys(videoCodecs).length,
        totalContainers: Object.keys(containerFormats).length
    });
});

// Get specific codec
app.get('/codecs/:codecId', (c) => {
    const codecId = c.req.param('codecId').toLowerCase();
    const codec = videoCodecs[codecId as keyof typeof videoCodecs];

    if (!codec) {
        return c.json({ error: 'Codec not found', available: Object.keys(videoCodecs) }, 404);
    }

    return c.json(codec);
});

// OpenH264 specific endpoint
app.get('/openh264', (c) => {
    const openh264 = videoCodecs.h264.openH264;
    return c.json({
        ...openh264,
        binaries: openh264.platforms.map(platform => ({
            platform,
            url: `http://ciscobinary.openh264.org/libopenh264-${openh264.version}-${platform}.${platform.includes('win') ? 'dll' : platform === 'ios' ? 'a' : platform.includes('mac') ? 'dylib' : 'so'}.bz2`,
            md5: `http://ciscobinary.openh264.org/libopenh264-${openh264.version}-${platform}.${platform.includes('win') ? 'dll' : platform === 'ios' ? 'a' : platform.includes('mac') ? 'dylib' : 'so'}.signed.md5.txt`
        })),
        v260Changes: [
            'Initialize PSNR to 0 instead of NAN',
            'Enable PIC in x86 assembly code',
            'Add QEMU test for LoongArch architecture',
            'Add support for calculating PSNR for Y/U/V components',
            'Add support for PowerPC architecture in meson.build',
            'Fix potential bug in the codebase',
            'Pass the actual temporal ID to GMPVideoEncodedFrame',
            'Use HW_NCPUONLINE on OpenBSD / NetBSD for CPU detection',
            'Add Windows VSBuildTools VC17 compile support',
            'Expose temporal layer info via GMP API at encoder initialization',
            'Remove the use of -Werror to prevent warnings as errors',
            'Use void casts to silence warnings about memcpy to a class'
        ]
    });
});

// Video history timeline
app.get('/history', (c) => {
    const era = c.req.query('era');
    let filtered = videoHistory;

    if (era === 'analog') {
        filtered = videoHistory.filter(e => e.year < 1988);
    } else if (era === 'mpeg') {
        filtered = videoHistory.filter(e => e.year >= 1988 && e.year < 2010);
    } else if (era === 'modern') {
        filtered = videoHistory.filter(e => e.year >= 2010);
    }

    return c.json({
        timeline: filtered,
        totalEvents: filtered.length,
        filter: era || 'all'
    });
});

// Calculate encoding parameters
app.post('/calculate', async (c) => {
    const body = await c.req.json();
    const {
        width = 1920,
        height = 1080,
        fps = 30,
        duration = 60,
        codec = 'h264',
        quality = 'high'
    } = body;

    const pixels = width * height;
    const totalFrames = fps * duration;

    // Bits per pixel based on quality and codec
    const bppMap: Record<string, Record<string, number>> = {
        h264: { low: 0.05, medium: 0.1, high: 0.15, ultra: 0.2 },
        h265: { low: 0.03, medium: 0.06, high: 0.1, ultra: 0.15 },
        av1: { low: 0.025, medium: 0.05, high: 0.08, ultra: 0.12 },
        vp9: { low: 0.035, medium: 0.07, high: 0.11, ultra: 0.16 }
    };

    const bpp = bppMap[codec]?.[quality] || 0.1;
    const bitrate = Math.round(pixels * fps * bpp / 1000); // kbps
    const fileSize = Math.round((bitrate * duration) / 8 / 1024); // MB

    // Recommended settings
    const recommendations = {
        h264: {
            profile: quality === 'ultra' ? 'High' : quality === 'high' ? 'High' : 'Main',
            preset: quality === 'ultra' ? 'slower' : quality === 'high' ? 'slow' : 'medium',
            crf: quality === 'ultra' ? 18 : quality === 'high' ? 20 : quality === 'medium' ? 23 : 26,
            keyframeInterval: fps * 2
        },
        h265: {
            profile: quality === 'ultra' ? 'Main 10' : 'Main',
            preset: quality === 'ultra' ? 'slower' : quality === 'high' ? 'slow' : 'medium',
            crf: quality === 'ultra' ? 20 : quality === 'high' ? 22 : quality === 'medium' ? 25 : 28,
            keyframeInterval: fps * 2
        },
        av1: {
            profile: 'Main',
            preset: quality === 'ultra' ? 4 : quality === 'high' ? 5 : quality === 'medium' ? 6 : 7,
            crf: quality === 'ultra' ? 22 : quality === 'high' ? 25 : quality === 'medium' ? 30 : 35,
            keyframeInterval: fps * 2
        }
    };

    return c.json({
        input: { width, height, fps, duration, codec, quality },
        calculations: {
            resolution: `${width}x${height}`,
            totalPixels: pixels,
            totalFrames,
            bitsPerPixel: bpp,
            bitrateKbps: bitrate,
            bitrateMbps: (bitrate / 1000).toFixed(2),
            estimatedFileSizeMB: fileSize,
            estimatedFileSizeGB: (fileSize / 1024).toFixed(2)
        },
        recommendations: recommendations[codec as keyof typeof recommendations] || recommendations.h264,
        ffmpegCommand: generateFFmpegCommand(width, height, fps, codec, quality, bitrate)
    });
});

function generateFFmpegCommand(width: number, height: number, fps: number, codec: string, quality: string, bitrate: number): string {
    const codecMap: Record<string, string> = {
        h264: 'libx264',
        h265: 'libx265',
        av1: 'libaom-av1',
        vp9: 'libvpx-vp9'
    };

    const crfMap: Record<string, Record<string, number>> = {
        h264: { low: 26, medium: 23, high: 20, ultra: 18 },
        h265: { low: 28, medium: 25, high: 22, ultra: 20 },
        av1: { low: 35, medium: 30, high: 25, ultra: 22 },
        vp9: { low: 35, medium: 30, high: 25, ultra: 20 }
    };

    return `ffmpeg -i input.mp4 -c:v ${codecMap[codec]} -crf ${crfMap[codec][quality]} -preset medium -s ${width}x${height} -r ${fps} -c:a aac -b:a 128k output.${codec === 'vp9' || codec === 'av1' ? 'webm' : 'mp4'}`;
}

// AI-powered video codec query
app.post('/ask', async (c) => {
    const { question } = await c.req.json();

    if (!question) {
        return c.json({ error: 'Question is required' }, 400);
    }

    try {
        const context = `You are a video codec expert with deep knowledge of:
- H.264/AVC (including OpenH264 v2.6.0)
- H.265/HEVC
- AV1 and VP9
- ProRes and DNxHD/DNxHR
- Container formats (MP4, MKV, WebM, MOV)
- FFmpeg encoding
- Bitrate optimization
- Quality vs file size tradeoffs

OpenH264 v2.6.0 (released Feb 12, 2025) features:
- PSNR calculation for Y/U/V components
- Temporal layer info via GMP API
- LoongArch and PowerPC support
- Windows VC17 build support
- OpenBSD/NetBSD CPU detection

Available codecs: ${Object.keys(videoCodecs).join(', ')}
Container formats: ${Object.keys(containerFormats).join(', ')}`;

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
            sources: ['Video codec standards', 'OpenH264 documentation', 'FFmpeg wiki'],
            relatedCodecs: Object.keys(videoCodecs).slice(0, 4)
        });
    } catch (error) {
        return c.json({
            question,
            answer: 'Video codec knowledge available offline. H.264 (via OpenH264 v2.6.0), H.265, AV1, VP9, ProRes, and DNxHD are the major codecs for modern video.',
            error: 'AI temporarily unavailable'
        });
    }
});

// Compare codecs
app.get('/compare/:codec1/:codec2', (c) => {
    const codec1 = c.req.param('codec1').toLowerCase();
    const codec2 = c.req.param('codec2').toLowerCase();

    const c1 = videoCodecs[codec1 as keyof typeof videoCodecs];
    const c2 = videoCodecs[codec2 as keyof typeof videoCodecs];

    if (!c1 || !c2) {
        return c.json({ error: 'One or both codecs not found', available: Object.keys(videoCodecs) }, 404);
    }

    return c.json({
        comparison: {
            [codec1]: {
                name: c1.name,
                released: c1.released,
                useCases: c1.useCases
            },
            [codec2]: {
                name: c2.name,
                released: c2.released,
                useCases: c2.useCases
            }
        },
        summary: `${c1.name} (${c1.released}) vs ${c2.name} (${c2.released})`,
        recommendation: c1.released > c2.released
            ? `${c1.name} is newer and typically offers better compression`
            : `${c2.name} is newer and typically offers better compression`
    });
});

export default app;
