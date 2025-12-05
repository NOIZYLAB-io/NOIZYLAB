"use strict";
/**
 * Code formatting and syntax highlighting service
 * @module services/FormattingService
 */
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.FormattingService = void 0;
const highlight_js_1 = __importDefault(require("highlight.js"));
const constants_1 = require("../constants");
const ExtensionError_1 = require("../errors/ExtensionError");
const Logger_1 = require("../utils/Logger");
// Use require for marked to ensure compatibility
const { marked } = require('marked');
/**
 * Service for formatting code and text output
 */
class FormattingService {
    static instance;
    log = Logger_1.logger.createChild('FormattingService');
    constructor() {
        this.configureMarked();
    }
    /**
     * Get singleton instance
     */
    static getInstance() {
        if (!FormattingService.instance) {
            FormattingService.instance = new FormattingService();
        }
        return FormattingService.instance;
    }
    /**
     * Configure marked options
     */
    configureMarked() {
        marked.setOptions({
            highlight: (code, lang) => {
                return this.highlightCode(code, lang);
            },
            breaks: true,
            gfm: true
        });
    }
    /**
     * Format output based on specified format
     */
    async formatOutput(text, format) {
        const endTimer = this.log.startTimer('formatOutput');
        try {
            if (!text) {
                return text;
            }
            switch (format) {
                case 'default':
                    return text;
                case 'enhanced':
                    return this.enhanceOutput(text);
                case 'markdown':
                    return this.formatMarkdown(text);
                case 'html':
                    return await this.formatHTML(text);
                default:
                    return text;
            }
        }
        catch (error) {
            this.log.error('Format output failed', error);
            throw new ExtensionError_1.ProcessingError('Failed to format output', 'FORMAT_ERROR', { format });
        }
        finally {
            endTimer();
        }
    }
    /**
     * Enhance output with better formatting
     */
    enhanceOutput(text) {
        let enhanced = text;
        // Improve code block formatting
        enhanced = enhanced.replace(/```(\w+)?\s*([\s\S]*?)```/g, (_, language, code) => {
            const detectedLang = language || this.detectLanguage(code).language || '';
            return `\`\`\`${detectedLang}\n${code.trim()}\n\`\`\``;
        });
        // Improve function call formatting
        enhanced = enhanced.replace(/<function_results>([\s\S]*?)<\/function_results>/g, (_, content) => {
            return `<details>\n<summary>Function Results</summary>\n\n\`\`\`\n${content.trim()}\n\`\`\`\n</details>\n`;
        });
        // Format augment code snippets
        enhanced = enhanced.replace(/<augment_code_snippet([^>]*)>([\s\S]*?)<\/augment_code_snippet>/g, (_, attrs, content) => {
            const pathMatch = attrs.match(/path="([^"]*)"/i);
            const modeMatch = attrs.match(/mode="([^"]*)"/i);
            const path = pathMatch ? pathMatch[1] : 'unknown';
            const mode = modeMatch ? modeMatch[1] : 'EXCERPT';
            return `<augment_code_snippet path="${path}" mode="${mode}">\n${content.trim()}\n</augment_code_snippet>`;
        });
        return enhanced;
    }
    /**
     * Format as markdown
     */
    formatMarkdown(text) {
        return this.enhanceOutput(text);
    }
    /**
     * Format as HTML
     */
    async formatHTML(text) {
        try {
            let html = marked.parse(text);
            // Add syntax highlighting to code blocks
            html = html.replace(/<pre><code class="language-(\w+)">([\s\S]*?)<\/code><\/pre>/g, (match, language, code) => {
                try {
                    const highlighted = this.highlightCode(code, language);
                    return `<pre><code class="language-${language} hljs">${highlighted}</code></pre>`;
                }
                catch (e) {
                    this.log.warn('Highlight failed for language', { language });
                    return match;
                }
            });
            return html;
        }
        catch (error) {
            this.log.error('HTML formatting failed', error);
            return text;
        }
    }
    /**
     * Detect programming language from code
     */
    detectLanguage(code) {
        if (!code || code.trim().length === 0) {
            return { confidence: 0 };
        }
        const detections = [];
        // Check each language pattern
        for (const [language, pattern] of Object.entries(constants_1.LANGUAGE_PATTERNS)) {
            if (pattern.test(code)) {
                // Calculate confidence based on pattern matches
                const matches = code.match(pattern);
                const confidence = matches ? Math.min(matches.length * 0.2, 1.0) : 0;
                detections.push({ language, confidence });
            }
        }
        // Sort by confidence and return best match
        detections.sort((a, b) => b.confidence - a.confidence);
        if (detections.length > 0 && detections[0].confidence > 0.3) {
            return detections[0];
        }
        return { confidence: 0 };
    }
    /**
     * Highlight code with syntax highlighting
     */
    highlightCode(code, language) {
        try {
            // Validate language
            if (language && highlight_js_1.default.getLanguage(language)) {
                const result = highlight_js_1.default.highlight(code, { language });
                return result.value;
            }
            // Auto-detect if language not specified or invalid
            const result = highlight_js_1.default.highlightAuto(code);
            return result.value;
        }
        catch (error) {
            this.log.warn('Highlight failed, returning plain code', { language });
            // Return escaped code if highlighting fails
            return this.escapeHtml(code);
        }
    }
    /**
     * Optimize code blocks in text
     */
    optimizeCodeBlocks(text) {
        return text.replace(/```(\w+)?\s*([\s\S]*?)```/g, (_, language, code) => {
            // Add proper language tag if missing
            if (!language) {
                const detected = this.detectLanguage(code);
                language = detected.language || '';
            }
            // Format the code block
            const formattedCode = code
                .trim()
                .replace(/^\s+/gm, (spaces) => spaces.replace(/\t/g, '  ')) // Replace tabs with spaces
                .replace(/\n{3,}/g, '\n\n'); // Remove excessive blank lines
            return `\`\`\`${language}\n${formattedCode}\n\`\`\``;
        });
    }
    /**
     * Escape HTML special characters
     */
    escapeHtml(text) {
        return text
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }
    /**
     * Strip HTML tags from text
     */
    stripHtml(html) {
        return html.replace(/<[^>]*>/g, '');
    }
    /**
     * Format file size for display
     */
    formatFileSize(bytes) {
        if (bytes === 0) {
            return '0 Bytes';
        }
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i];
    }
}
exports.FormattingService = FormattingService;
//# sourceMappingURL=FormattingService.js.map