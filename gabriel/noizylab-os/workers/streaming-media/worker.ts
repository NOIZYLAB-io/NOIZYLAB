/**
 * NoizyLab OS - Streaming Media Worker
 * HLS, DASH, WebRTC, and streaming protocol intelligence
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
    STREAMING_DB: D1Database;
    STREAMING_CACHE: KVNamespace;
    STREAMING_ASSETS: R2Bucket;
    AI: any;
    VECTORIZE: any;
}

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// Streaming protocols
const streamingProtocols = {
    'hls': {
        name: 'HLS',
        fullName: 'HTTP Live Streaming',
        developer: 'Apple',
        released: 2009,
        standard: 'RFC 8216',
        containerFormat: 'MPEG-TS or fMP4',
        manifestFormat: 'm3u8',
        features: [
            'Adaptive bitrate',
            'AES-128 encryption',
            'Subtitles (WebVTT)',
            'Alternative audio tracks',
            'Low-latency HLS (LL-HLS)',
            'Server-side ad insertion'
        ],
        latency: {
            standard: '10-30 seconds',
            lowLatency: '2-5 seconds'
        },
        support: 'Universal (native iOS/Safari, JavaScript players elsewhere)',
        useCases: ['VOD', 'Live streaming', 'OTT platforms', 'iOS apps']
    },
    'dash': {
        name: 'MPEG-DASH',
        fullName: 'Dynamic Adaptive Streaming over HTTP',
        developer: 'MPEG',
        released: 2012,
        standard: 'ISO/IEC 23009-1',
        containerFormat: 'fMP4 or WebM',
        manifestFormat: 'MPD (XML)',
        features: [
            'Adaptive bitrate',
            'DRM support (Widevine, PlayReady)',
            'Multi-period content',
            'Server-side ad insertion',
            'Low-latency CMAF'
        ],
        latency: {
            standard: '10-30 seconds',
            lowLatency: '2-5 seconds'
        },
        support: 'Chrome, Edge, Firefox (via MSE/EME), Android',
        useCases: ['Netflix', 'YouTube', 'Amazon Prime', 'Sports streaming']
    },
    'webrtc': {
        name: 'WebRTC',
        fullName: 'Web Real-Time Communication',
        developer: 'W3C/IETF',
        released: 2011,
        features: [
            'Peer-to-peer',
            'Sub-second latency',
            'Bidirectional audio/video',
            'Screen sharing',
            'Data channels',
            'SRTP encryption'
        ],
        latency: '< 500ms (typically 100-300ms)',
        codecs: {
            video: ['VP8', 'VP9', 'H.264', 'AV1'],
            audio: ['Opus', 'G.711']
        },
        support: 'All modern browsers',
        useCases: ['Video calls', 'Live interaction', 'Gaming', 'Remote desktop']
    },
    'rtmp': {
        name: 'RTMP',
        fullName: 'Real-Time Messaging Protocol',
        developer: 'Adobe (Macromedia)',
        released: 2002,
        features: [
            'Low-latency ingest',
            'Persistent connections',
            'Multiplexing',
            'Authentication'
        ],
        latency: '1-5 seconds',
        status: 'Deprecated for playback, still used for ingest',
        useCases: ['Twitch ingest', 'YouTube Live ingest', 'Encoder output'],
        ports: 'TCP 1935'
    },
    'srt': {
        name: 'SRT',
        fullName: 'Secure Reliable Transport',
        developer: 'Haivision',
        released: 2017,
        features: [
            'AES encryption',
            'Error recovery',
            'Low latency',
            'Open source',
            'Firewall traversal'
        ],
        latency: '< 1 second',
        support: 'OBS, FFmpeg, Professional encoders',
        useCases: ['Contribution feeds', 'Remote production', 'First-mile delivery']
    },
    'whip-whep': {
        name: 'WHIP/WHEP',
        fullName: 'WebRTC HTTP Ingestion/Egress Protocol',
        developer: 'IETF',
        status: 'Draft standard',
        features: [
            'Simple WebRTC signaling',
            'HTTP-based',
            'Standardized WebRTC ingest',
            'Sub-second latency'
        ],
        latency: '< 500ms',
        useCases: ['Browser-based broadcasting', 'Low-latency streaming']
    }
};

// CDN providers
const cdnProviders = {
    'cloudflare': {
        name: 'Cloudflare Stream',
        features: ['Automatic encoding', 'Player included', 'Analytics', 'Live & VOD'],
        pricing: '$5/1000 minutes stored, $1/1000 minutes delivered'
    },
    'mux': {
        name: 'Mux',
        features: ['Real-time data', 'Per-title encoding', 'Automatic captions', 'Live'],
        pricing: 'Per-minute pricing, free tier available'
    },
    'aws': {
        name: 'AWS MediaServices',
        features: ['MediaLive', 'MediaConvert', 'CloudFront CDN', 'DRM'],
        pricing: 'Complex per-service pricing'
    },
    'akamai': {
        name: 'Akamai',
        features: ['Enterprise CDN', 'Live events', 'DRM', 'Analytics'],
        pricing: 'Enterprise contracts'
    },
    'fastly': {
        name: 'Fastly',
        features: ['Edge compute', 'Real-time logs', 'Low latency'],
        pricing: 'Usage-based'
    }
};

// DRM systems
const drmSystems = {
    'widevine': {
        name: 'Widevine',
        developer: 'Google',
        levels: ['L1 (hardware)', 'L2 (software)', 'L3 (software, lowest)'],
        platforms: ['Chrome', 'Firefox', 'Android', 'Chromecast', 'Smart TVs'],
        maxQuality: { L1: '4K HDR', L2: '720p', L3: '480p' }
    },
    'fairplay': {
        name: 'FairPlay Streaming',
        developer: 'Apple',
        platforms: ['Safari', 'iOS', 'tvOS', 'macOS'],
        maxQuality: '4K HDR'
    },
    'playready': {
        name: 'PlayReady',
        developer: 'Microsoft',
        levels: ['SL3000 (hardware)', 'SL2000 (software)'],
        platforms: ['Edge', 'Windows', 'Xbox', 'Smart TVs'],
        maxQuality: { SL3000: '4K HDR', SL2000: '1080p' }
    }
};

// Encoding ladder example
const encodingLadder = {
    '4k-premium': [
        { resolution: '3840x2160', bitrate: 16000, codec: 'H.265', profile: 'main10' },
        { resolution: '2560x1440', bitrate: 8000, codec: 'H.265', profile: 'main10' },
        { resolution: '1920x1080', bitrate: 4500, codec: 'H.264', profile: 'high' },
        { resolution: '1280x720', bitrate: 2500, codec: 'H.264', profile: 'main' },
        { resolution: '854x480', bitrate: 1000, codec: 'H.264', profile: 'main' },
        { resolution: '640x360', bitrate: 600, codec: 'H.264', profile: 'baseline' },
        { resolution: '426x240', bitrate: 300, codec: 'H.264', profile: 'baseline' }
    ],
    'hd-standard': [
        { resolution: '1920x1080', bitrate: 5000, codec: 'H.264', profile: 'high' },
        { resolution: '1280x720', bitrate: 3000, codec: 'H.264', profile: 'main' },
        { resolution: '854x480', bitrate: 1500, codec: 'H.264', profile: 'main' },
        { resolution: '640x360', bitrate: 800, codec: 'H.264', profile: 'baseline' },
        { resolution: '426x240', bitrate: 400, codec: 'H.264', profile: 'baseline' }
    ],
    'mobile-optimized': [
        { resolution: '1280x720', bitrate: 2000, codec: 'H.264', profile: 'main' },
        { resolution: '854x480', bitrate: 1000, codec: 'H.264', profile: 'main' },
        { resolution: '640x360', bitrate: 500, codec: 'H.264', profile: 'baseline' },
        { resolution: '426x240', bitrate: 250, codec: 'H.264', profile: 'baseline' }
    ]
};

// Health check
app.get('/', (c) => {
    return c.json({
        worker: 'streaming-media',
        status: 'operational',
        version: '1.0.0',
        description: 'Streaming protocols and media delivery intelligence',
        capabilities: [
            'HLS/DASH configuration',
            'WebRTC setup guidance',
            'Encoding ladder design',
            'CDN selection',
            'DRM implementation',
            'Latency optimization',
            'Player integration'
        ]
    });
});

// Get all streaming protocols
app.get('/protocols', (c) => {
    return c.json({
        protocols: streamingProtocols,
        totalProtocols: Object.keys(streamingProtocols).length
    });
});

// Get specific protocol
app.get('/protocols/:protocolId', (c) => {
    const protocolId = c.req.param('protocolId').toLowerCase();
    const protocol = streamingProtocols[protocolId as keyof typeof streamingProtocols];

    if (!protocol) {
        return c.json({ error: 'Protocol not found', available: Object.keys(streamingProtocols) }, 404);
    }

    return c.json(protocol);
});

// Get CDN providers
app.get('/cdn', (c) => {
    return c.json({
        providers: cdnProviders,
        totalProviders: Object.keys(cdnProviders).length
    });
});

// Get DRM systems
app.get('/drm', (c) => {
    return c.json({
        systems: drmSystems,
        recommendation: 'For universal coverage, implement Widevine + FairPlay + PlayReady'
    });
});

// Get encoding ladders
app.get('/ladder', (c) => {
    const profile = c.req.query('profile') || '4k-premium';
    const ladder = encodingLadder[profile as keyof typeof encodingLadder];

    if (!ladder) {
        return c.json({
            error: 'Profile not found',
            available: Object.keys(encodingLadder)
        }, 404);
    }

    return c.json({
        profile,
        ladder,
        totalRenditions: ladder.length,
        audioRecommendation: { codec: 'AAC', bitrate: 128, channels: 2 }
    });
});

// Calculate streaming parameters
app.post('/calculate', async (c) => {
    const body = await c.req.json();
    const {
        viewers = 1000,
        duration = 60, // minutes
        avgBitrate = 3000, // kbps
        protocol = 'hls'
    } = body;

    const bandwidthPerViewer = avgBitrate / 8 / 1024; // MB/s
    const totalBandwidth = bandwidthPerViewer * viewers * 1024; // GB/s
    const totalDataTransfer = bandwidthPerViewer * viewers * duration * 60; // GB

    // Cost estimates (rough)
    const costs = {
        cloudflare: totalDataTransfer * 0.05, // ~$0.05/GB
        aws: totalDataTransfer * 0.085, // ~$0.085/GB
        mux: viewers * duration * 0.00025 // ~$0.00025/viewer-minute
    };

    return c.json({
        input: { viewers, duration, avgBitrate, protocol },
        calculations: {
            bandwidthPerViewerMBps: bandwidthPerViewer.toFixed(2),
            totalBandwidthGbps: (totalBandwidth / 1024 * 8).toFixed(2),
            totalDataTransferGB: totalDataTransfer.toFixed(2),
            totalDataTransferTB: (totalDataTransfer / 1024).toFixed(2)
        },
        estimatedCosts: {
            cloudflare: `$${costs.cloudflare.toFixed(2)}`,
            aws: `$${costs.aws.toFixed(2)}`,
            mux: `$${costs.mux.toFixed(2)}`
        },
        recommendations: {
            segmentDuration: protocol === 'hls' ? '6 seconds' : '4 seconds',
            manifestType: protocol === 'hls' ? 'm3u8' : 'mpd',
            gop: avgBitrate > 4000 ? '2 seconds' : '4 seconds',
            bufferSize: protocol === 'webrtc' ? '0.5 seconds' : '10 seconds'
        }
    });
});

// Generate HLS/DASH configuration
app.post('/config', async (c) => {
    const body = await c.req.json();
    const { protocol = 'hls', profile = 'hd-standard' } = body;

    if (protocol === 'hls') {
        return c.json({
            protocol: 'HLS',
            manifest: 'master.m3u8',
            sampleManifest: `#EXTM3U
#EXT-X-VERSION:6
#EXT-X-STREAM-INF:BANDWIDTH=5000000,RESOLUTION=1920x1080,CODECS="avc1.640028,mp4a.40.2"
1080p/playlist.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=3000000,RESOLUTION=1280x720,CODECS="avc1.4d401f,mp4a.40.2"
720p/playlist.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1500000,RESOLUTION=854x480,CODECS="avc1.4d401e,mp4a.40.2"
480p/playlist.m3u8`,
            ffmpegCommand: `ffmpeg -i input.mp4 \\
  -c:v libx264 -preset fast -crf 22 \\
  -c:a aac -b:a 128k \\
  -hls_time 6 -hls_list_size 0 \\
  -hls_segment_filename 'segment_%03d.ts' \\
  -f hls playlist.m3u8`
        });
    } else if (protocol === 'dash') {
        return c.json({
            protocol: 'MPEG-DASH',
            manifest: 'manifest.mpd',
            sampleManifest: `<?xml version="1.0" encoding="UTF-8"?>
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" mediaPresentationDuration="PT1H">
  <Period>
    <AdaptationSet mimeType="video/mp4" codecs="avc1.640028">
      <Representation bandwidth="5000000" width="1920" height="1080">
        <SegmentTemplate media="1080p_$Number$.m4s" initialization="1080p_init.mp4"/>
      </Representation>
    </AdaptationSet>
  </Period>
</MPD>`,
            ffmpegCommand: `ffmpeg -i input.mp4 \\
  -c:v libx264 -preset fast -crf 22 \\
  -c:a aac -b:a 128k \\
  -f dash -seg_duration 4 \\
  -use_timeline 1 -use_template 1 \\
  manifest.mpd`
        });
    }

    return c.json({ error: 'Unknown protocol' }, 400);
});

// AI-powered streaming query
app.post('/ask', async (c) => {
    const { question } = await c.req.json();

    if (!question) {
        return c.json({ error: 'Question is required' }, 400);
    }

    try {
        const context = `You are a streaming media expert with deep knowledge of:
- HLS (HTTP Live Streaming) configuration and optimization
- MPEG-DASH implementation
- WebRTC for real-time communication
- RTMP and SRT for contribution
- Encoding ladders and adaptive bitrate
- CDN selection (Cloudflare, AWS, Mux, Akamai)
- DRM systems (Widevine, FairPlay, PlayReady)
- Low-latency streaming techniques
- FFmpeg for transcoding

Protocols: ${Object.keys(streamingProtocols).join(', ')}
CDN providers: ${Object.keys(cdnProviders).join(', ')}`;

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
            sources: ['Streaming specifications', 'CDN documentation', 'Industry best practices']
        });
    } catch (error) {
        return c.json({
            question,
            answer: 'Streaming guidance: Use HLS for broad compatibility, DASH for DRM, WebRTC for real-time. Standard ABR latency is 10-30s, low-latency ~2-5s, WebRTC <500ms.',
            error: 'AI temporarily unavailable'
        });
    }
});

export default app;
