"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getPrefix = void 0;
const style_1 = require("../types/style");
const getPrefix = (depth, style, isLastItem = false, isFile = false) => {
    const repeatStr = '  '.repeat(depth);
    let prefix;
    const folderPrefixes = {
        [style_1.Style.ClassicDashes]: `${repeatStr}└── `,
        [style_1.Style.MinimalistDots]: `${repeatStr} • `,
        [style_1.Style.EmojiFun]: `${repeatStr}📁 `,
        [style_1.Style.EmojiMinimalist]: `${repeatStr}📁 `,
        [style_1.Style.Arrows]: `${repeatStr}➜ `,
        [style_1.Style.NestedCircles]: `${repeatStr}◉ `,
        [style_1.Style.BoldBlocks]: `${repeatStr}■ `,
        [style_1.Style.SlashSeparators]: `${repeatStr}/ `,
        [style_1.Style.ChevronIndicators]: `${repeatStr}» `,
        [style_1.Style.DotDashMix]: `${repeatStr}• `,
        [style_1.Style.Triangles]: `${repeatStr}▶ `,
        [style_1.Style.Zigzag]: `${repeatStr}↳ `,
        [style_1.Style.PipesAndHyphens]: `${repeatStr}|- `,
        [style_1.Style.NestedSquares]: `${repeatStr}■ `,
        [style_1.Style.CirclesAndLines]: `${repeatStr}◯ `,
        [style_1.Style.SparklesDesing]: `${repeatStr}📁✨ `,
        [style_1.Style.TrailDesign]: `${repeatStr}👣📁 `,
        [style_1.Style.FloralDesign]: `${repeatStr}🌸📁 `,
        [style_1.Style.GalacticDesign]: `${repeatStr}🌌📁 `,
        [style_1.Style.EmojiDashes]: `${repeatStr}└── 📁`,
    };
    const filePrefixes = {
        [style_1.Style.ClassicDashes]: `${repeatStr}├── `,
        [style_1.Style.MinimalistDots]: `${repeatStr}• `,
        [style_1.Style.EmojiFun]: `${repeatStr}📄 `,
        [style_1.Style.EmojiMinimalist]: `${repeatStr}─ `,
        [style_1.Style.Arrows]: `${repeatStr}➜ `,
        [style_1.Style.NestedCircles]: `${repeatStr}○ `,
        [style_1.Style.BoldBlocks]: `${repeatStr}■ `,
        [style_1.Style.SlashSeparators]: `${repeatStr}/ `,
        [style_1.Style.ChevronIndicators]: `${repeatStr}» `,
        [style_1.Style.DotDashMix]: `${repeatStr}- `,
        [style_1.Style.Triangles]: `${repeatStr}▶ `,
        [style_1.Style.Zigzag]: `${repeatStr}↳ `,
        [style_1.Style.PipesAndHyphens]: `${repeatStr}|- `,
        [style_1.Style.NestedSquares]: `${repeatStr}□ `,
        [style_1.Style.CirclesAndLines]: `${repeatStr}─ `,
        [style_1.Style.SparklesDesing]: `${repeatStr}✨ `,
        [style_1.Style.TrailDesign]: `${repeatStr}👣📄 `,
        [style_1.Style.FloralDesign]: `${repeatStr}🌸📄 `,
        [style_1.Style.GalacticDesign]: `${repeatStr}🌌📄 `,
        [style_1.Style.EmojiDashes]: `${repeatStr}├── `,
    };
    const lastItemPrefixes = {
        [style_1.Style.ClassicDashes]: `${repeatStr}└── `,
        [style_1.Style.MinimalistDots]: `${repeatStr}• `,
        [style_1.Style.EmojiFun]: `${repeatStr}📄 `,
        [style_1.Style.EmojiMinimalist]: `${repeatStr}─ `,
        [style_1.Style.Arrows]: `${repeatStr}➜ `,
        [style_1.Style.NestedCircles]: `${repeatStr}○ `,
        [style_1.Style.BoldBlocks]: `${repeatStr}■ `,
        [style_1.Style.SlashSeparators]: `${repeatStr}/ `,
        [style_1.Style.ChevronIndicators]: `${repeatStr}» `,
        [style_1.Style.DotDashMix]: `${repeatStr}- `,
        [style_1.Style.Triangles]: `${repeatStr}▶ `,
        [style_1.Style.Zigzag]: `${repeatStr}↳ `,
        [style_1.Style.PipesAndHyphens]: `${repeatStr}|- `,
        [style_1.Style.NestedSquares]: `${repeatStr}□ `,
        [style_1.Style.CirclesAndLines]: `${repeatStr}─ `,
        [style_1.Style.SparklesDesing]: `${repeatStr}✨ `,
        [style_1.Style.TrailDesign]: `${repeatStr}👣📄 `,
        [style_1.Style.FloralDesign]: `${repeatStr}🌸📄 `,
        [style_1.Style.GalacticDesign]: `${repeatStr}🌌📄 `,
        [style_1.Style.EmojiDashes]: `${repeatStr}└── `,
    };
    if (isFile) {
        prefix = isLastItem ? lastItemPrefixes[style] : filePrefixes[style];
    }
    else {
        prefix = isLastItem ? lastItemPrefixes[style] : folderPrefixes[style];
    }
    return repeatStr + prefix;
};
exports.getPrefix = getPrefix;
//# sourceMappingURL=get-prefix.js.map