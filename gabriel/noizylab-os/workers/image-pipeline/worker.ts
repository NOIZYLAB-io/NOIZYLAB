/**
 * NoizyLab OS - Image Pipeline Worker
 * Image processing, formats, filters, and AI enhancement
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
    IMAGE_PIPELINE_DB: D1Database;
    IMAGE_PIPELINE_CACHE: KVNamespace;
    IMAGE_ASSETS: R2Bucket;
    AI: any;
    VECTORIZE: any;
}

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// Image format knowledge base
const imageFormats = {
    'jpeg': {
        name: 'JPEG',
        fullName: 'Joint Photographic Experts Group',
        extension: ['.jpg', '.jpeg'],
        mimeType: 'image/jpeg',
        released: 1992,
        compression: 'Lossy',
        colorModes: ['RGB', 'CMYK', 'Grayscale'],
        maxDimensions: '65,535 x 65,535 pixels',
        features: ['Progressive loading', 'EXIF metadata', 'DCT compression'],
        useCases: ['Photography', 'Web images', 'Social media'],
        pros: ['Wide support', 'Small file sizes', 'Adjustable quality'],
        cons: ['Lossy compression', 'No transparency', 'Artifacts at low quality']
    },
    'png': {
        name: 'PNG',
        fullName: 'Portable Network Graphics',
        extension: ['.png'],
        mimeType: 'image/png',
        released: 1996,
        compression: 'Lossless',
        colorModes: ['RGB', 'RGBA', 'Indexed', 'Grayscale'],
        maxDimensions: '2,147,483,647 x 2,147,483,647 pixels',
        features: ['Alpha transparency', 'Interlacing', 'Gamma correction'],
        useCases: ['Web graphics', 'Screenshots', 'Logos', 'UI elements'],
        pros: ['Lossless', 'Transparency support', 'Sharp edges'],
        cons: ['Larger files than JPEG', 'Not ideal for photos']
    },
    'webp': {
        name: 'WebP',
        fullName: 'WebP Image Format',
        extension: ['.webp'],
        mimeType: 'image/webp',
        released: 2010,
        compression: 'Lossy and Lossless',
        colorModes: ['RGB', 'RGBA'],
        maxDimensions: '16,383 x 16,383 pixels',
        features: ['Animation support', 'Alpha transparency', 'ICC profiles'],
        useCases: ['Web optimization', 'Modern websites', 'Apps'],
        pros: ['Smaller than JPEG/PNG', 'Both lossy and lossless', 'Animation'],
        cons: ['Limited legacy browser support', 'Color profile issues']
    },
    'avif': {
        name: 'AVIF',
        fullName: 'AV1 Image File Format',
        extension: ['.avif'],
        mimeType: 'image/avif',
        released: 2019,
        compression: 'Lossy and Lossless',
        colorModes: ['RGB', 'RGBA', 'HDR'],
        features: ['HDR support', 'Wide color gamut', 'Animation', '10/12-bit depth'],
        useCases: ['Next-gen web images', 'HDR photography'],
        pros: ['Best compression', 'HDR support', 'Royalty-free'],
        cons: ['Slow encoding', 'Limited software support']
    },
    'heic': {
        name: 'HEIC/HEIF',
        fullName: 'High Efficiency Image Container',
        extension: ['.heic', '.heif'],
        mimeType: 'image/heic',
        released: 2015,
        compression: 'Lossy (typically)',
        colorModes: ['RGB', 'RGBA', 'HDR'],
        features: ['Live photos', 'Depth maps', 'Image sequences', 'HDR'],
        useCases: ['iPhone photos', 'Apple ecosystem'],
        pros: ['50% smaller than JPEG', 'Multiple images in one file', 'HDR'],
        cons: ['Limited web support', 'Licensing issues']
    },
    'tiff': {
        name: 'TIFF',
        fullName: 'Tagged Image File Format',
        extension: ['.tiff', '.tif'],
        mimeType: 'image/tiff',
        released: 1986,
        compression: 'Various (LZW, ZIP, None)',
        colorModes: ['RGB', 'CMYK', 'LAB', 'Grayscale', 'Indexed'],
        features: ['Layers', 'Multiple pages', 'High bit depth', 'ICC profiles'],
        useCases: ['Print publishing', 'Archiving', 'Professional photography'],
        pros: ['Lossless quality', 'Industry standard for print', 'Flexible'],
        cons: ['Large file sizes', 'Limited web support']
    },
    'gif': {
        name: 'GIF',
        fullName: 'Graphics Interchange Format',
        extension: ['.gif'],
        mimeType: 'image/gif',
        released: 1987,
        compression: 'Lossless (LZW)',
        colorModes: ['Indexed (256 colors max)'],
        features: ['Animation', 'Transparency (1-bit)', 'Interlacing'],
        useCases: ['Animations', 'Memes', 'Simple graphics'],
        pros: ['Universal animation support', 'Wide compatibility'],
        cons: ['256 color limit', 'Large animated files']
    },
    'svg': {
        name: 'SVG',
        fullName: 'Scalable Vector Graphics',
        extension: ['.svg'],
        mimeType: 'image/svg+xml',
        released: 2001,
        compression: 'None (XML text)',
        type: 'Vector',
        features: ['Infinite scaling', 'CSS styling', 'JavaScript interaction', 'Animation'],
        useCases: ['Icons', 'Logos', 'Illustrations', 'Data visualization'],
        pros: ['Resolution independent', 'Small file sizes', 'Editable'],
        cons: ['Not suitable for photos', 'Complex images = large files']
    },
    'raw': {
        name: 'RAW',
        fullName: 'Camera Raw Image',
        extensions: ['.raw', '.cr2', '.cr3', '.nef', '.arw', '.dng', '.orf', '.rw2'],
        compression: 'Lossless or uncompressed',
        bitDepth: '12-16 bit per channel',
        features: ['Maximum data retention', 'Non-destructive editing', 'White balance flexibility'],
        useCases: ['Professional photography', 'Post-processing', 'Archiving'],
        vendors: {
            'Canon': ['.cr2', '.cr3'],
            'Nikon': ['.nef', '.nrw'],
            'Sony': ['.arw'],
            'Adobe': ['.dng'],
            'Fujifilm': ['.raf'],
            'Olympus': ['.orf'],
            'Panasonic': ['.rw2']
        }
    }
};

// Image processing operations
const imageOperations = {
    resize: ['Bicubic', 'Bilinear', 'Nearest neighbor', 'Lanczos', 'Mitchell'],
    filters: ['Blur', 'Sharpen', 'Emboss', 'Edge detect', 'Noise reduction'],
    adjustments: ['Brightness', 'Contrast', 'Saturation', 'Hue', 'Levels', 'Curves'],
    transforms: ['Rotate', 'Flip', 'Crop', 'Perspective', 'Distort'],
    effects: ['Vignette', 'Grain', 'Glow', 'HDR', 'Sepia', 'Black & White'],
    ai: ['Super resolution', 'Denoising', 'Background removal', 'Face enhancement', 'Colorization']
};

// Color spaces
const colorSpaces = {
    'srgb': { name: 'sRGB', description: 'Standard RGB for web', gamut: 'Standard', useCases: ['Web', 'Monitors'] },
    'adobe-rgb': { name: 'Adobe RGB', description: 'Wider gamut for print', gamut: 'Wide', useCases: ['Print', 'Photography'] },
    'p3': { name: 'Display P3', description: 'Apple wide color', gamut: 'Wide', useCases: ['Apple devices', 'HDR'] },
    'rec2020': { name: 'Rec. 2020', description: 'Ultra-wide gamut for HDR', gamut: 'Ultra-wide', useCases: ['HDR video', '8K'] },
    'cmyk': { name: 'CMYK', description: 'Print color space', type: 'Subtractive', useCases: ['Print', 'Publishing'] },
    'lab': { name: 'CIE LAB', description: 'Perceptually uniform', type: 'Device-independent', useCases: ['Color science', 'Conversions'] }
};

// Health check
app.get('/', (c) => {
    return c.json({
        worker: 'image-pipeline',
        status: 'operational',
        version: '1.0.0',
        description: 'Image processing and format intelligence',
        capabilities: [
            'Format conversion guidance',
            'Optimization recommendations',
            'Color space information',
            'Processing parameters',
            'AI enhancement tips',
            'Quality vs size tradeoffs',
            'Responsive image strategies'
        ]
    });
});

// Get all image formats
app.get('/formats', (c) => {
    return c.json({
        formats: imageFormats,
        totalFormats: Object.keys(imageFormats).length,
        categories: {
            raster: ['jpeg', 'png', 'webp', 'avif', 'heic', 'tiff', 'gif'],
            vector: ['svg'],
            raw: ['raw']
        }
    });
});

// Get specific format
app.get('/formats/:formatId', (c) => {
    const formatId = c.req.param('formatId').toLowerCase();
    const format = imageFormats[formatId as keyof typeof imageFormats];

    if (!format) {
        return c.json({ error: 'Format not found', available: Object.keys(imageFormats) }, 404);
    }

    return c.json(format);
});

// Get color spaces
app.get('/colorspaces', (c) => {
    return c.json({
        colorSpaces,
        total: Object.keys(colorSpaces).length
    });
});

// Get processing operations
app.get('/operations', (c) => {
    return c.json({
        operations: imageOperations,
        categories: Object.keys(imageOperations)
    });
});

// Optimize image recommendation
app.post('/optimize', async (c) => {
    const body = await c.req.json();
    const {
        width = 1920,
        height = 1080,
        format = 'jpeg',
        quality = 80,
        useCase = 'web'
    } = body;

    const recommendations: Record<string, any> = {
        web: {
            format: 'webp',
            fallback: 'jpeg',
            quality: 80,
            maxWidth: 1920,
            lazy: true,
            responsive: true,
            srcset: [480, 768, 1024, 1440, 1920]
        },
        social: {
            format: 'jpeg',
            quality: 85,
            dimensions: {
                instagram: { square: '1080x1080', portrait: '1080x1350', story: '1080x1920' },
                twitter: { post: '1200x675', header: '1500x500' },
                facebook: { post: '1200x630', cover: '820x312' },
                linkedin: { post: '1200x627', cover: '1584x396' }
            }
        },
        print: {
            format: 'tiff',
            colorSpace: 'cmyk',
            dpi: 300,
            quality: 100,
            compression: 'lzw'
        },
        email: {
            format: 'jpeg',
            quality: 70,
            maxWidth: 600,
            maxSize: '100KB'
        }
    };

    const pixels = width * height;
    const estimatedSizes: Record<string, number> = {
        jpeg: pixels * 0.15 / 1024, // KB
        png: pixels * 0.5 / 1024,
        webp: pixels * 0.1 / 1024,
        avif: pixels * 0.07 / 1024
    };

    return c.json({
        input: { width, height, format, quality, useCase },
        recommendation: recommendations[useCase] || recommendations.web,
        estimatedSizes: {
            jpeg: `${Math.round(estimatedSizes.jpeg)} KB`,
            png: `${Math.round(estimatedSizes.png)} KB`,
            webp: `${Math.round(estimatedSizes.webp)} KB`,
            avif: `${Math.round(estimatedSizes.avif)} KB`
        },
        savings: {
            webpVsJpeg: `${Math.round((1 - estimatedSizes.webp / estimatedSizes.jpeg) * 100)}%`,
            avifVsJpeg: `${Math.round((1 - estimatedSizes.avif / estimatedSizes.jpeg) * 100)}%`
        },
        sharpCommand: `sharp input.${format} --resize ${width} --webp --quality ${quality} -o output.webp`,
        imageMagickCommand: `convert input.${format} -resize ${width}x${height} -quality ${quality} output.webp`
    });
});

// AI-powered image query
app.post('/ask', async (c) => {
    const { question } = await c.req.json();

    if (!question) {
        return c.json({ error: 'Question is required' }, 400);
    }

    try {
        const context = `You are an image processing expert with deep knowledge of:
- Image formats (JPEG, PNG, WebP, AVIF, HEIC, TIFF, GIF, SVG, RAW)
- Color spaces (sRGB, Adobe RGB, P3, CMYK, LAB)
- Processing operations (resize, filters, adjustments, transforms)
- Optimization techniques for web and print
- AI-powered enhancement (super resolution, denoising, background removal)
- Responsive images and modern web practices

Available formats: ${Object.keys(imageFormats).join(', ')}
Color spaces: ${Object.keys(colorSpaces).join(', ')}`;

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
            sources: ['Image format specifications', 'Web standards', 'Color science'],
            relatedFormats: Object.keys(imageFormats).slice(0, 4)
        });
    } catch (error) {
        return c.json({
            question,
            answer: 'Image processing guidance: Use WebP for web (30% smaller than JPEG), AVIF for modern browsers (50% smaller), PNG for transparency, and TIFF for print.',
            error: 'AI temporarily unavailable'
        });
    }
});

// Format comparison
app.get('/compare/:format1/:format2', (c) => {
    const format1 = c.req.param('format1').toLowerCase();
    const format2 = c.req.param('format2').toLowerCase();

    const f1 = imageFormats[format1 as keyof typeof imageFormats];
    const f2 = imageFormats[format2 as keyof typeof imageFormats];

    if (!f1 || !f2) {
        return c.json({ error: 'Format not found', available: Object.keys(imageFormats) }, 404);
    }

    return c.json({
        comparison: {
            [format1]: { name: f1.name, compression: f1.compression, useCases: f1.useCases },
            [format2]: { name: f2.name, compression: f2.compression, useCases: f2.useCases }
        },
        recommendation: getFormatRecommendation(format1, format2)
    });
});

function getFormatRecommendation(f1: string, f2: string): string {
    const modern = ['avif', 'webp', 'heic'];
    if (modern.includes(f1) && !modern.includes(f2)) {
        return `${f1.toUpperCase()} offers better compression but ${f2.toUpperCase()} has wider compatibility`;
    }
    if (modern.includes(f2) && !modern.includes(f1)) {
        return `${f2.toUpperCase()} offers better compression but ${f1.toUpperCase()} has wider compatibility`;
    }
    return 'Choose based on your specific use case and browser/software support requirements';
}

export default app;
