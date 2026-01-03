/**
 * NoizyLab OS - Spatial Media Worker
 * VR, AR, 360 video, spatial audio, and immersive content
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
    SPATIAL_DB: D1Database;
    SPATIAL_CACHE: KVNamespace;
    AI: any;
}

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// VR headsets
const vrHeadsets = {
    'quest3': { name: 'Meta Quest 3', company: 'Meta', type: 'Standalone', resolution: '2064x2208/eye', refresh: '90/120Hz', tracking: '6DoF inside-out', passthrough: 'Color MR', price: '$499', sdk: 'Meta XR SDK' },
    'quest-pro': { name: 'Meta Quest Pro', company: 'Meta', type: 'Standalone', resolution: '1800x1920/eye', features: 'Eye+face tracking', price: '$999', sdk: 'Meta XR SDK' },
    'vision-pro': { name: 'Apple Vision Pro', company: 'Apple', type: 'Standalone', resolution: '23 million pixels', features: 'Eye tracking, hand tracking, spatial computing', price: '$3499', sdk: 'visionOS SDK' },
    'psvr2': { name: 'PlayStation VR2', company: 'Sony', type: 'Tethered (PS5)', resolution: '2000x2040/eye', refresh: '90/120Hz', features: 'Eye tracking, haptics', price: '$549', sdk: 'PS5 SDK' },
    'valve-index': { name: 'Valve Index', company: 'Valve', type: 'Tethered (PC)', resolution: '1440x1600/eye', refresh: '144Hz', tracking: 'Lighthouse', price: '$999', sdk: 'SteamVR/OpenXR' },
    'pico4': { name: 'Pico 4', company: 'ByteDance', type: 'Standalone', resolution: '2160x2160/eye', price: '$429', sdk: 'Pico SDK' }
};

// AR platforms
const arPlatforms = {
    'arkit': { name: 'ARKit', company: 'Apple', platforms: ['iOS', 'iPadOS', 'visionOS'], features: ['LiDAR', 'Plane detection', 'Face tracking', 'Body tracking', 'Object occlusion'], language: 'Swift/RealityKit' },
    'arcore': { name: 'ARCore', company: 'Google', platforms: ['Android', 'iOS'], features: ['Plane detection', 'Light estimation', 'Cloud anchors', 'Depth API'], language: 'Java/Kotlin/Unity' },
    'webxr': { name: 'WebXR', company: 'W3C', platforms: ['Web browsers'], features: ['VR/AR in browser', 'Immersive sessions', 'Input handling'], language: 'JavaScript' },
    'spark-ar': { name: 'Spark AR', company: 'Meta', platforms: ['Instagram', 'Facebook'], features: ['Face filters', 'World effects', 'Social AR'], language: 'Visual/JavaScript' },
    'lens-studio': { name: 'Lens Studio', company: 'Snap', platforms: ['Snapchat'], features: ['Lenses', 'Face tracking', 'World lenses'], language: 'Visual/JavaScript' }
};

// XR development frameworks
const xrFrameworks = {
    'unity-xr': { name: 'Unity XR', type: 'Engine', platforms: 'All major headsets', features: ['XR Interaction Toolkit', 'AR Foundation', 'Multi-platform'] },
    'unreal-xr': { name: 'Unreal Engine XR', type: 'Engine', platforms: 'All major headsets', features: ['High fidelity', 'Blueprint VR', 'OpenXR'] },
    'aframe': { name: 'A-Frame', type: 'Web framework', platforms: 'WebXR browsers', features: ['HTML-like syntax', 'Entity-component', 'VR websites'] },
    'threejs-xr': { name: 'Three.js + WebXR', type: 'Library', platforms: 'WebXR browsers', features: ['Low-level control', 'WebGL/WebGPU'] },
    'babylonjs-xr': { name: 'Babylon.js XR', type: 'Library', platforms: 'WebXR browsers', features: ['Full XR support', 'GUI in VR'] },
    'godot-xr': { name: 'Godot XR', type: 'Engine', platforms: 'OpenXR headsets', features: ['Open source', 'GDScript', 'OpenXR'] }
};

// 360 video specs
const video360Specs = {
    resolutions: {
        '4K mono': { pixels: '3840x2160', pixelsPerDegree: '~11 PPD', quality: 'Minimum acceptable' },
        '5.7K': { pixels: '5760x2880', pixelsPerDegree: '~16 PPD', quality: 'Good consumer' },
        '8K mono': { pixels: '7680x3840', pixelsPerDegree: '~21 PPD', quality: 'High quality' },
        '8K stereo': { pixels: '7680x7680', pixelsPerDegree: '~21 PPD', quality: 'Premium stereoscopic' },
        '12K+': { pixels: '12288x6144+', pixelsPerDegree: '~34+ PPD', quality: 'Professional/theatrical' }
    },
    projections: {
        equirectangular: { description: 'Standard 2:1 mapping', use: 'Most common, easy editing' },
        cubemap: { description: '6 faces of cube', use: 'Efficient rendering, gaming' },
        eac: { description: 'Equi-Angular Cubemap', use: 'YouTube, efficient bandwidth' }
    },
    cameras: ['Insta360', 'GoPro MAX', 'Ricoh Theta', 'Kandao QooCam', 'RED Komodo (multi-rig)']
};

// Spatial audio
const spatialAudio = {
    formats: {
        'ambisonics': { description: '360° sound field capture/playback', orders: ['First order (4ch)', 'Second order (9ch)', 'Third order (16ch)'], use: 'VR, 360 video' },
        'object-based': { description: 'Individual sound sources in 3D', examples: ['Dolby Atmos', 'MPEG-H'], use: 'Cinema, gaming, music' },
        'binaural': { description: 'Headphone 3D audio', technique: 'HRTF (Head-Related Transfer Function)', use: 'Headphone playback' }
    },
    tools: {
        'fb360': { name: 'FB360 Spatial Workstation', company: 'Meta', use: 'Ambisonics for 360 video' },
        'resonance': { name: 'Resonance Audio', company: 'Google', use: 'Spatial audio SDK' },
        'steam-audio': { name: 'Steam Audio', company: 'Valve', use: 'Game spatial audio' },
        'dolby-atmos': { name: 'Dolby Atmos Production Suite', use: 'Object-based mixing' }
    }
};

// Health check
app.get('/', (c) => {
    return c.json({
        worker: 'spatial-media',
        status: 'operational',
        version: '1.0.0',
        description: 'VR, AR, 360 video, and spatial audio intelligence',
        capabilities: ['VR headset comparison', 'AR platform guidance', 'XR development frameworks', '360 video specs', 'Spatial audio formats', 'WebXR development']
    });
});

// Get VR headsets
app.get('/vr', (c) => {
    return c.json({ headsets: vrHeadsets, total: Object.keys(vrHeadsets).length });
});

// Get AR platforms
app.get('/ar', (c) => {
    return c.json({ platforms: arPlatforms, total: Object.keys(arPlatforms).length });
});

// Get XR frameworks
app.get('/frameworks', (c) => {
    return c.json({ frameworks: xrFrameworks, recommendation: 'Unity XR for cross-platform, A-Frame for web, visionOS SDK for Apple Vision Pro' });
});

// Get 360 video specs
app.get('/360video', (c) => {
    return c.json({ specs: video360Specs });
});

// Get spatial audio info
app.get('/spatial-audio', (c) => {
    return c.json({ spatialAudio });
});

// Platform recommendation
app.post('/recommend', async (c) => {
    const body = await c.req.json();
    const { target = 'consumer', platform = 'cross-platform', budget = 'medium' } = body;

    let recommendation;
    if (platform === 'web') {
        recommendation = { framework: 'A-Frame or Three.js', reason: 'WebXR for browser-based experiences, no app install needed' };
    } else if (platform === 'apple') {
        recommendation = { framework: 'visionOS + RealityKit', reason: 'Native Apple Vision Pro and iOS AR experiences' };
    } else if (target === 'gaming') {
        recommendation = { framework: 'Unity XR or Unreal XR', reason: 'Full game engine capabilities, multi-platform support' };
    } else if (budget === 'low') {
        recommendation = { framework: 'Godot XR + OpenXR', reason: 'Free, open source, growing ecosystem' };
    } else {
        recommendation = { framework: 'Unity XR Interaction Toolkit', reason: 'Industry standard, excellent documentation, AR Foundation included' };
    }

    return c.json({ input: { target, platform, budget }, recommendation });
});

// AI-powered spatial media query
app.post('/ask', async (c) => {
    const { question } = await c.req.json();
    if (!question) return c.json({ error: 'Question required' }, 400);

    try {
        const context = `You are a spatial media expert with knowledge of: VR headsets (Quest, Vision Pro, Index), AR platforms (ARKit, ARCore, WebXR), XR development frameworks, 360 video production, spatial audio (ambisonics, binaural), and immersive content creation.`;
        const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
            messages: [{ role: 'system', content: context }, { role: 'user', content: question }],
            max_tokens: 1024
        });
        return c.json({ question, answer: response.response });
    } catch (error) {
        return c.json({ question, answer: 'Spatial media guidance: Quest 3 for accessible VR, Vision Pro for spatial computing, Unity XR for development, WebXR for browser experiences, 8K minimum for quality 360 video.', error: 'AI unavailable' });
    }
});

export default app;
