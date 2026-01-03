/**
 * NoizyLab OS - Animation Engine Worker
 * Motion graphics, keyframes, transitions, and animation principles
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
    ANIMATION_DB: D1Database;
    ANIMATION_CACHE: KVNamespace;
    AI: any;
}

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// Animation software
const animationSoftware = {
    '2d': {
        'aftereffects': { name: 'Adobe After Effects', company: 'Adobe', use: 'Motion graphics, VFX', pricing: '$22.99/mo' },
        'animate': { name: 'Adobe Animate', company: 'Adobe', use: '2D animation, interactive', pricing: '$22.99/mo' },
        'toonboom': { name: 'Toon Boom Harmony', company: 'Toon Boom', use: 'Professional 2D animation', pricing: '$26-118/mo' },
        'opentoonz': { name: 'OpenToonz', company: 'Open source', use: '2D animation (Studio Ghibli)', pricing: 'Free' },
        'moho': { name: 'Moho (Anime Studio)', company: 'Smith Micro', use: '2D character animation', pricing: '$69-399' },
        'pencil2d': { name: 'Pencil2D', company: 'Open source', use: 'Traditional animation', pricing: 'Free' },
        'krita': { name: 'Krita', company: 'Open source', use: '2D animation, painting', pricing: 'Free' }
    },
    '3d': {
        'maya': { name: 'Autodesk Maya', company: 'Autodesk', use: 'Film/game 3D animation', pricing: '$225/mo' },
        'blender': { name: 'Blender', company: 'Open source', use: 'Full 3D suite', pricing: 'Free' },
        'cinema4d': { name: 'Cinema 4D', company: 'Maxon', use: 'Motion graphics 3D', pricing: '$59-119/mo' },
        'houdini': { name: 'Houdini', company: 'SideFX', use: 'Procedural VFX', pricing: 'Free (Apprentice)' },
        '3dsmax': { name: '3ds Max', company: 'Autodesk', use: 'Architectural, games', pricing: '$225/mo' }
    },
    'web': {
        'gsap': { name: 'GSAP', company: 'GreenSock', use: 'Web animation library', pricing: 'Free/Commercial' },
        'lottie': { name: 'Lottie', company: 'Airbnb', use: 'AE to web/mobile', pricing: 'Free' },
        'framer-motion': { name: 'Framer Motion', company: 'Framer', use: 'React animation', pricing: 'Free' },
        'animejs': { name: 'Anime.js', company: 'Open source', use: 'JavaScript animation', pricing: 'Free' },
        'threejs': { name: 'Three.js', company: 'Open source', use: 'WebGL 3D animation', pricing: 'Free' },
        'rive': { name: 'Rive', company: 'Rive Inc', use: 'Interactive animation', pricing: 'Free tier' }
    }
};

// Animation principles (Disney's 12)
const principles = [
    { name: 'Squash and Stretch', description: 'Gives weight and flexibility to objects', example: 'Bouncing ball squashing on impact' },
    { name: 'Anticipation', description: 'Prepares audience for action', example: 'Wind-up before a punch' },
    { name: 'Staging', description: 'Presents ideas clearly', example: 'Silhouette readability' },
    { name: 'Straight Ahead & Pose to Pose', description: 'Two animation approaches', example: 'Frame-by-frame vs keyframes' },
    { name: 'Follow Through & Overlapping', description: 'Parts move at different rates', example: 'Hair continues after head stops' },
    { name: 'Slow In and Slow Out', description: 'Easing for natural movement', example: 'ease-in-out curves' },
    { name: 'Arc', description: 'Natural curved motion paths', example: 'Arm swing follows arc' },
    { name: 'Secondary Action', description: 'Supporting actions add life', example: 'Walking while talking' },
    { name: 'Timing', description: 'Speed affects weight and mood', example: 'Fast = light, Slow = heavy' },
    { name: 'Exaggeration', description: 'Push reality for clarity', example: 'Cartoon expressions' },
    { name: 'Solid Drawing', description: '3D form understanding', example: 'Volume and weight' },
    { name: 'Appeal', description: 'Charismatic design', example: 'Likeable character design' }
];

// Easing functions
const easingFunctions = {
    linear: { css: 'linear', description: 'Constant speed', use: 'Progress bars, looping' },
    easeIn: { css: 'ease-in', cubic: 'cubic-bezier(0.42, 0, 1.0, 1.0)', description: 'Slow start', use: 'Exit animations' },
    easeOut: { css: 'ease-out', cubic: 'cubic-bezier(0, 0, 0.58, 1.0)', description: 'Slow end', use: 'Enter animations' },
    easeInOut: { css: 'ease-in-out', cubic: 'cubic-bezier(0.42, 0, 0.58, 1.0)', description: 'Slow both ends', use: 'Most UI animations' },
    easeOutBack: { cubic: 'cubic-bezier(0.34, 1.56, 0.64, 1)', description: 'Overshoot then settle', use: 'Playful bounces' },
    easeInBack: { cubic: 'cubic-bezier(0.36, 0, 0.66, -0.56)', description: 'Pull back before going', use: 'Anticipation' },
    easeOutElastic: { description: 'Elastic bounce at end', use: 'Attention-grabbing' },
    easeOutBounce: { description: 'Bouncing settle', use: 'Playful UI' }
};

// Frame rates
const frameRates = {
    '12fps': { use: 'Limited animation, anime style', feel: 'Choppy but stylistic' },
    '24fps': { use: 'Film standard, traditional animation', feel: 'Cinematic' },
    '25fps': { use: 'PAL video standard', feel: 'European broadcast' },
    '30fps': { use: 'NTSC video, streaming', feel: 'Smooth video' },
    '48fps': { use: 'HFR film (The Hobbit)', feel: 'Very smooth, "soap opera"' },
    '60fps': { use: 'Games, smooth UI, sports', feel: 'Ultra smooth' },
    '120fps': { use: 'High-end gaming, VR', feel: 'Maximum smoothness' }
};

// Health check
app.get('/', (c) => {
    return c.json({
        worker: 'animation-engine',
        status: 'operational',
        version: '1.0.0',
        description: 'Animation principles, tools, and motion design intelligence',
        capabilities: [
            'Animation software comparison',
            '12 principles of animation',
            'Easing function reference',
            'Frame rate guidance',
            'Keyframe techniques',
            'Motion design patterns',
            'Web animation libraries'
        ]
    });
});

// Get animation software
app.get('/software', (c) => {
    const type = c.req.query('type');
    if (type && animationSoftware[type as keyof typeof animationSoftware]) {
        return c.json({ type, software: animationSoftware[type as keyof typeof animationSoftware] });
    }
    return c.json({ software: animationSoftware, types: Object.keys(animationSoftware) });
});

// Get animation principles
app.get('/principles', (c) => {
    return c.json({ principles, count: principles.length, source: "Disney's 12 Principles of Animation" });
});

// Get easing functions
app.get('/easing', (c) => {
    return c.json({ easingFunctions, total: Object.keys(easingFunctions).length });
});

// Get frame rates
app.get('/framerates', (c) => {
    return c.json({ frameRates });
});

// Generate keyframe CSS
app.post('/keyframes', async (c) => {
    const body = await c.req.json();
    const { name = 'fadeIn', from = { opacity: 0 }, to = { opacity: 1 }, duration = '0.3s', easing = 'ease-out' } = body;

    const fromCSS = Object.entries(from).map(([k, v]) => `${k}: ${v};`).join(' ');
    const toCSS = Object.entries(to).map(([k, v]) => `${k}: ${v};`).join(' ');

    return c.json({
        css: `@keyframes ${name} {
  from { ${fromCSS} }
  to { ${toCSS} }
}

.${name} {
  animation: ${name} ${duration} ${easing} forwards;
}`,
        gsap: `gsap.to('.element', { ${Object.entries(to).map(([k, v]) => `${k}: ${v}`).join(', ')}, duration: ${parseFloat(duration)}, ease: '${easing}' });`,
        framerMotion: `<motion.div initial={${JSON.stringify(from)}} animate={${JSON.stringify(to)}} transition={{ duration: ${parseFloat(duration)} }} />`
    });
});

// AI-powered animation query
app.post('/ask', async (c) => {
    const { question } = await c.req.json();

    if (!question) {
        return c.json({ error: 'Question is required' }, 400);
    }

    try {
        const context = `You are an animation expert with knowledge of:
- Animation software (After Effects, Maya, Blender, etc.)
- Disney's 12 principles of animation
- Easing functions and timing curves
- Web animation (GSAP, Framer Motion, CSS animations)
- Motion design patterns and UI animation
- Frame rates for different media
- Keyframe animation techniques`;

        const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
            messages: [{ role: 'system', content: context }, { role: 'user', content: question }],
            max_tokens: 1024
        });

        return c.json({ question, answer: response.response });
    } catch (error) {
        return c.json({ question, answer: 'Animation guidance available. Use the 12 principles for natural motion, ease-out for enters, ease-in for exits, 60fps for smooth UI.', error: 'AI unavailable' });
    }
});

export default app;
