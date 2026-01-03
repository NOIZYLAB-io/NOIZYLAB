/**
 * NoizyLab OS - Typography Engine Worker
 * Fonts, text rendering, layout, and typographic principles
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
    TYPOGRAPHY_DB: D1Database;
    TYPOGRAPHY_CACHE: KVNamespace;
    AI: any;
}

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// Font formats
const fontFormats = {
    'woff2': { name: 'WOFF2', compression: 'Brotli', support: '96%+', recommended: true, use: 'Modern web' },
    'woff': { name: 'WOFF', compression: 'zlib', support: '98%+', recommended: false, use: 'Fallback' },
    'ttf': { name: 'TrueType', compression: 'None', support: 'Universal', recommended: false, use: 'Desktop, legacy' },
    'otf': { name: 'OpenType', compression: 'Optional', support: 'Universal', features: 'Advanced typography', use: 'Desktop, professional' },
    'eot': { name: 'EOT', compression: 'None', support: 'IE only', deprecated: true, use: 'Legacy IE' },
    'svg': { name: 'SVG Font', compression: 'None', support: 'Deprecated', deprecated: true, use: 'Old iOS Safari' },
    'variable': { name: 'Variable Fonts', format: 'WOFF2/TTF', features: 'Multiple weights/widths in one file', support: '95%+' }
};

// Type classifications
const typeClassifications = {
    serif: { description: 'Small decorative strokes', examples: ['Times New Roman', 'Georgia', 'Garamond', 'Baskerville'], use: 'Print, formal, editorial' },
    sansSerif: { description: 'No decorative strokes', examples: ['Helvetica', 'Arial', 'Inter', 'Roboto', 'Open Sans'], use: 'Digital, modern, UI' },
    monospace: { description: 'Fixed-width characters', examples: ['Fira Code', 'JetBrains Mono', 'Monaco', 'Consolas'], use: 'Code, technical' },
    display: { description: 'Decorative, large sizes', examples: ['Impact', 'Lobster', 'Pacifico'], use: 'Headlines, logos' },
    script: { description: 'Handwritten style', examples: ['Brush Script', 'Pacifico', 'Dancing Script'], use: 'Invitations, branding' },
    slab: { description: 'Thick block serifs', examples: ['Rockwell', 'Roboto Slab', 'Courier'], use: 'Headlines, impact' }
};

// Typography scale (major third)
const typographyScales = {
    'minor-second': { ratio: 1.067, use: 'Subtle hierarchy' },
    'major-second': { ratio: 1.125, use: 'Conservative' },
    'minor-third': { ratio: 1.2, use: 'Common, balanced' },
    'major-third': { ratio: 1.25, use: 'Most popular' },
    'perfect-fourth': { ratio: 1.333, use: 'Strong hierarchy' },
    'augmented-fourth': { ratio: 1.414, use: 'Dramatic' },
    'perfect-fifth': { ratio: 1.5, use: 'Very dramatic' },
    'golden-ratio': { ratio: 1.618, use: 'Classical proportion' }
};

// Font loading strategies
const loadingStrategies = {
    'font-display-swap': { css: "font-display: swap;", description: 'Show fallback, swap when loaded', use: 'Body text' },
    'font-display-block': { css: "font-display: block;", description: 'Hide text briefly', use: 'Icons, critical headings' },
    'font-display-fallback': { css: "font-display: fallback;", description: 'Short block, then fallback', use: 'Balance of swap/block' },
    'font-display-optional': { css: "font-display: optional;", description: 'Use only if cached', use: 'Performance-critical' },
    'preload': { html: '<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>', description: 'Prioritize font loading' }
};

// Popular font pairings
const fontPairings = [
    { heading: 'Playfair Display', body: 'Source Sans Pro', style: 'Elegant editorial' },
    { heading: 'Montserrat', body: 'Merriweather', style: 'Modern professional' },
    { heading: 'Oswald', body: 'Open Sans', style: 'Bold contemporary' },
    { heading: 'Roboto', body: 'Roboto', style: 'Google Material' },
    { heading: 'Inter', body: 'Inter', style: 'Modern UI' },
    { heading: 'Lora', body: 'Source Sans Pro', style: 'Classic readable' },
    { heading: 'Poppins', body: 'Lato', style: 'Friendly modern' },
    { heading: 'Space Grotesk', body: 'Work Sans', style: 'Tech/startup' }
];

// Health check
app.get('/', (c) => {
    return c.json({
        worker: 'typography-engine',
        status: 'operational',
        version: '1.0.0',
        description: 'Typography, fonts, and text layout intelligence',
        capabilities: ['Font format guidance', 'Type classification', 'Typography scales', 'Font loading', 'Font pairing', 'CSS typography']
    });
});

// Get font formats
app.get('/formats', (c) => {
    return c.json({ formats: fontFormats, recommended: 'WOFF2 for web, Variable Fonts for flexibility' });
});

// Get type classifications
app.get('/classifications', (c) => {
    return c.json({ classifications: typeClassifications });
});

// Get typography scales
app.get('/scales', (c) => {
    const scale = c.req.query('scale') || 'major-third';
    const baseSize = parseInt(c.req.query('base') || '16');
    const selectedScale = typographyScales[scale as keyof typeof typographyScales] || typographyScales['major-third'];

    const sizes = {
        xs: Math.round(baseSize / selectedScale.ratio / selectedScale.ratio),
        sm: Math.round(baseSize / selectedScale.ratio),
        base: baseSize,
        lg: Math.round(baseSize * selectedScale.ratio),
        xl: Math.round(baseSize * selectedScale.ratio * selectedScale.ratio),
        '2xl': Math.round(baseSize * Math.pow(selectedScale.ratio, 3)),
        '3xl': Math.round(baseSize * Math.pow(selectedScale.ratio, 4)),
        '4xl': Math.round(baseSize * Math.pow(selectedScale.ratio, 5))
    };

    return c.json({ scale, ratio: selectedScale.ratio, baseSize, sizes, allScales: typographyScales });
});

// Get loading strategies
app.get('/loading', (c) => {
    return c.json({ strategies: loadingStrategies });
});

// Get font pairings
app.get('/pairings', (c) => {
    return c.json({ pairings: fontPairings, tip: 'Contrast is key: pair serif with sans-serif, or use different weights of same family' });
});

// Generate @font-face CSS
app.post('/fontface', async (c) => {
    const body = await c.req.json();
    const { family = 'CustomFont', weight = 400, style = 'normal', url, format = 'woff2', display = 'swap' } = body;

    const css = `@font-face {
  font-family: '${family}';
  src: url('${url || `/fonts/${family.toLowerCase().replace(/\s/g, '-')}.${format}`}') format('${format}');
  font-weight: ${weight};
  font-style: ${style};
  font-display: ${display};
}`;

    return c.json({ css, usage: `font-family: '${family}', sans-serif;` });
});

// AI-powered typography query
app.post('/ask', async (c) => {
    const { question } = await c.req.json();
    if (!question) return c.json({ error: 'Question required' }, 400);

    try {
        const context = `You are a typography expert with knowledge of: font formats, type classifications, typography scales, font loading strategies, font pairing, CSS typography properties, variable fonts, and web font best practices.`;
        const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
            messages: [{ role: 'system', content: context }, { role: 'user', content: question }],
            max_tokens: 1024
        });
        return c.json({ question, answer: response.response });
    } catch (error) {
        return c.json({ question, answer: 'Typography guidance: Use WOFF2 for web, font-display: swap for body text, preload critical fonts. Aim for 45-75 characters per line.', error: 'AI unavailable' });
    }
});

export default app;
