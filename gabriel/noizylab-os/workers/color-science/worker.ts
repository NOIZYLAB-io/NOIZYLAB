/**
 * NoizyLab OS - Color Science Worker
 * Color theory, grading, LUTs, HDR, and color management
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
    COLOR_DB: D1Database;
    COLOR_CACHE: KVNamespace;
    AI: any;
}

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// Color spaces
const colorSpaces = {
    'srgb': { name: 'sRGB', gamut: 'Standard', bitDepth: '8-bit', use: ['Web', 'Consumer monitors'], whitePoint: 'D65' },
    'display-p3': { name: 'Display P3', gamut: '25% larger than sRGB', bitDepth: '10-bit', use: ['Apple devices', 'HDR content'], whitePoint: 'D65' },
    'adobe-rgb': { name: 'Adobe RGB', gamut: '35% larger than sRGB', bitDepth: '16-bit', use: ['Print', 'Photography'], whitePoint: 'D65' },
    'prophoto': { name: 'ProPhoto RGB', gamut: 'Very wide', bitDepth: '16-bit', use: ['Professional photography', 'Archival'], whitePoint: 'D50' },
    'rec709': { name: 'Rec. 709', gamut: 'Same as sRGB', bitDepth: '8-bit', use: ['HDTV', 'Streaming'], whitePoint: 'D65' },
    'rec2020': { name: 'Rec. 2020', gamut: 'Ultra-wide', bitDepth: '10/12-bit', use: ['4K/8K HDR', 'Cinema'], whitePoint: 'D65' },
    'dci-p3': { name: 'DCI-P3', gamut: 'Wide', bitDepth: '12-bit', use: ['Digital cinema'], whitePoint: 'DCI white (6300K)' },
    'aces': { name: 'ACES', gamut: 'Scene-referred, all visible', bitDepth: '16/32-bit float', use: ['VFX', 'Film production'], whitePoint: 'D60' }
};

// HDR formats
const hdrFormats = {
    'hdr10': { name: 'HDR10', type: 'Static metadata', bitDepth: '10-bit', maxNits: 1000, colorSpace: 'Rec. 2020', adoption: 'Universal' },
    'hdr10plus': { name: 'HDR10+', type: 'Dynamic metadata', bitDepth: '10-bit', maxNits: 4000, developer: 'Samsung/Amazon', adoption: 'Growing' },
    'dolby-vision': { name: 'Dolby Vision', type: 'Dynamic metadata', bitDepth: '12-bit', maxNits: 10000, adoption: 'Premium TVs/Streaming' },
    'hlg': { name: 'HLG', type: 'Hybrid Log-Gamma', bitDepth: '10-bit', use: 'Broadcast, backwards compatible', adoption: 'Broadcast' }
};

// Color grading software
const gradingSoftware = {
    'davinci': { name: 'DaVinci Resolve', company: 'Blackmagic', pricing: 'Free / $295 (Studio)', strength: 'Industry standard grading' },
    'premiere': { name: 'Adobe Premiere Pro', company: 'Adobe', pricing: '$22.99/mo', strength: 'Lumetri Color, integration' },
    'fcpx': { name: 'Final Cut Pro', company: 'Apple', pricing: '$299.99', strength: 'Color wheels, HDR workflow' },
    'baselight': { name: 'Baselight', company: 'FilmLight', pricing: 'Professional licensing', strength: 'High-end film grading' },
    'colorista': { name: 'Magic Bullet Colorista', company: 'Red Giant', pricing: '$199', strength: 'Plugin for NLEs' }
};

// Color harmony types
const colorHarmony = {
    complementary: { description: 'Opposite on color wheel', example: 'Blue + Orange', feel: 'High contrast, vibrant' },
    analogous: { description: 'Adjacent colors', example: 'Blue + Cyan + Green', feel: 'Harmonious, natural' },
    triadic: { description: '120° apart', example: 'Red + Yellow + Blue', feel: 'Balanced, vibrant' },
    splitComplementary: { description: 'Complement + adjacent', example: 'Blue + Yellow-Orange + Red-Orange', feel: 'Contrast with variety' },
    tetradic: { description: 'Rectangle pattern', example: 'Red + Green + Blue + Orange', feel: 'Rich, requires balance' },
    monochromatic: { description: 'Single hue, varied lightness', example: 'Light blue to dark blue', feel: 'Cohesive, elegant' }
};

// Health check
app.get('/', (c) => {
    return c.json({
        worker: 'color-science',
        status: 'operational',
        version: '1.0.0',
        description: 'Color theory, grading, and color science intelligence',
        capabilities: ['Color space information', 'HDR format comparison', 'Color harmony', 'LUT guidance', 'Grading software', 'Color conversion']
    });
});

// Get color spaces
app.get('/spaces', (c) => {
    return c.json({ colorSpaces, total: Object.keys(colorSpaces).length });
});

// Get HDR formats
app.get('/hdr', (c) => {
    return c.json({ hdrFormats, recommendation: 'HDR10 for maximum compatibility, Dolby Vision for premium quality' });
});

// Get grading software
app.get('/software', (c) => {
    return c.json({ software: gradingSoftware });
});

// Get color harmony
app.get('/harmony', (c) => {
    return c.json({ harmony: colorHarmony, types: Object.keys(colorHarmony) });
});

// Convert colors
app.post('/convert', async (c) => {
    const body = await c.req.json();
    const { color, from = 'hex', to = 'rgb' } = body;

    // Simple hex to RGB conversion
    let result: any = {};
    if (from === 'hex' && color) {
        const hex = color.replace('#', '');
        const r = parseInt(hex.substring(0, 2), 16);
        const g = parseInt(hex.substring(2, 4), 16);
        const b = parseInt(hex.substring(4, 6), 16);

        result = {
            hex: `#${hex}`,
            rgb: `rgb(${r}, ${g}, ${b})`,
            hsl: rgbToHsl(r, g, b),
            oklch: 'Use CSS oklch() for perceptually uniform',
            css: { hex: `#${hex}`, rgb: `rgb(${r} ${g} ${b})`, rgba: `rgba(${r}, ${g}, ${b}, 1)` }
        };
    }

    return c.json({ input: { color, from, to }, result });
});

function rgbToHsl(r: number, g: number, b: number): string {
    r /= 255; g /= 255; b /= 255;
    const max = Math.max(r, g, b), min = Math.min(r, g, b);
    let h = 0, s = 0, l = (max + min) / 2;
    if (max !== min) {
        const d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch (max) {
            case r: h = ((g - b) / d + (g < b ? 6 : 0)) / 6; break;
            case g: h = ((b - r) / d + 2) / 6; break;
            case b: h = ((r - g) / d + 4) / 6; break;
        }
    }
    return `hsl(${Math.round(h * 360)}, ${Math.round(s * 100)}%, ${Math.round(l * 100)}%)`;
}

// AI-powered color query
app.post('/ask', async (c) => {
    const { question } = await c.req.json();
    if (!question) return c.json({ error: 'Question required' }, 400);

    try {
        const context = `You are a color science expert with knowledge of: color spaces (sRGB, P3, Rec.2020, ACES), HDR formats, color grading, LUTs, color theory, harmony, and color management workflows.`;
        const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
            messages: [{ role: 'system', content: context }, { role: 'user', content: question }],
            max_tokens: 1024
        });
        return c.json({ question, answer: response.response });
    } catch (error) {
        return c.json({ question, answer: 'Color guidance: Use sRGB for web, P3 for Apple/HDR, ACES for VFX pipelines. HDR10 for wide compatibility, Dolby Vision for premium.', error: 'AI unavailable' });
    }
});

export default app;
