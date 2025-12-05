"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.createCacheCleanupListeners = exports.getMdcComponentPropCompletionItemProvider = exports.getMdcComponentCompletionItemProvider = void 0;
/* eslint-disable no-template-curly-in-string */
const scule_1 = require("scule");
const vscode = require("vscode");
const logger_1 = require("./logger");
const MDC_COMPONENT_START_REGEX = /^\s*:{2,}([\w-]+)\s*$/;
const MULTILINE_STRING_REGEX = /^([\w-]+):\s*[|>]/g;
/** Cache for storing model line content to avoid repeated getLinesContent() calls */
const lineContentCache = new WeakMap();
/** Cache for storing prop name conversions between kebab-case and camelCase */
const propNameCache = new Map();
/** Cache for storing nested props by component name */
const nestedPropsCache = new Map();
/** Cache for storing prop value types by component name */
const propTypeCache = new Map();
/** Cache for storing documentation links by component name */
const docsLinkCache = new Map();
/** Cache for storing YAML block boundaries by model and line number */
const yamlBlockBoundaryCache = new WeakMap();
/**
 * Retrieves the lines of content from a vscode document, using cache when available.
 *
 * @param {vscode.TextDocument} document - The VS Code text document
 * @returns {string[]} - Array of text lines from the document
 */
function getModelLines(document) {
    let lines = lineContentCache.get(document);
    if (!lines) {
        lines = document.getText().split('\n');
        lineContentCache.set(document, lines);
    }
    return lines;
}
/**
 * Invalidates all caches associated with a specific VS Code text document.
 * Should be called when the document content changes or when starting a new completion request.
 *
 * @param {vscode.TextDocument} document - The VS Code text document to invalidate caches for
 */
function invalidateLineCache(document) {
    lineContentCache.delete(document);
    yamlBlockBoundaryCache.delete(document);
}
/**
 * Retrieves cached prop name conversions or generates new ones for a component's prop.
 *
 * @param {string} componentName - The MDC component name
 * @param {string} propName - The property name to convert
 * @returns {{ kebab: string; camel: string }} - Object containing both kebab-case and camelCase versions
 */
function getCachedPropNames(componentName, propName) {
    const cacheKey = `${componentName}:${propName}`;
    let cached = propNameCache.get(cacheKey);
    if (!cached) {
        cached = {
            kebab: (0, scule_1.kebabCase)(propName),
            camel: (0, scule_1.camelCase)(propName)
        };
        propNameCache.set(cacheKey, cached);
    }
    return cached;
}
/**
 * Retrieves nested props from a component's prop schema, using cache when available.
 *
 * @param {MDCComponentData} component - The MDC component
 * @param {any} prop - The prop to extract nested props from
 * @returns {Record<string, any> | null} - Object containing nested props or null if none exist
 */
function getNestedProps(component, prop) {
    var _a;
    if (!component.mdc_name) {
        return null;
    }
    let componentCache = nestedPropsCache.get(component.mdc_name);
    if (!componentCache) {
        componentCache = new Map();
        nestedPropsCache.set(component.mdc_name, componentCache);
    }
    const cacheKey = prop.name;
    let cached = componentCache.get(cacheKey);
    if (cached === undefined) {
        if (!((_a = prop.schema) === null || _a === void 0 ? void 0 : _a.schema)) {
            cached = null;
        }
        else {
            const objectSchema = Object.values(prop.schema.schema).find((s) => typeof s === 'object' && (s === null || s === void 0 ? void 0 : s.kind) === 'object');
            cached = objectSchema ? objectSchema.schema : null;
        }
        componentCache.set(cacheKey, cached);
    }
    return cached;
}
/**
 * Determines the value type of a prop, using cache when available.
 *
 * @param {MDCComponentData} component - The MDC component
 * @param {any} prop - The prop to determine the type for
 * @returns {MdcPropType} - The determined prop value type
 */
function getPropValueType(component, prop) {
    var _a, _b, _c, _d, _e, _f, _g, _h, _j, _k, _l, _m, _o, _p;
    if (!component.mdc_name) {
        return 'string';
    }
    let componentCache = propTypeCache.get(component.mdc_name);
    if (!componentCache) {
        componentCache = new Map();
        propTypeCache.set(component.mdc_name, componentCache);
    }
    const cacheKey = prop.name;
    let propType = componentCache.get(cacheKey);
    if (!propType) {
        if (((_a = prop.type) === null || _a === void 0 ? void 0 : _a.includes('Record<')) || ((_c = (_b = prop.type) === null || _b === void 0 ? void 0 : _b.toLowerCase()) === null || _c === void 0 ? void 0 : _c.includes('object')) || ((_d = prop.type) === null || _d === void 0 ? void 0 : _d.includes('Array<string,'))) {
            return 'object';
        }
        else if (((_e = prop.type) === null || _e === void 0 ? void 0 : _e.includes('string[]')) || ((_f = prop.type) === null || _f === void 0 ? void 0 : _f.includes('Array<string'))) {
            propType = 'array';
        }
        else if (((_g = prop.type) === null || _g === void 0 ? void 0 : _g.includes('number[]')) || ((_h = prop.type) === null || _h === void 0 ? void 0 : _h.includes('Array<number')) || ((_j = prop.type) === null || _j === void 0 ? void 0 : _j.includes('Array<boolean'))) {
            propType = 'array-unquoted';
        }
        else if ((_k = prop.type) === null || _k === void 0 ? void 0 : _k.includes('boolean')) {
            propType = 'boolean';
        }
        else if ((_l = prop.type) === null || _l === void 0 ? void 0 : _l.includes('number')) {
            propType = 'number';
        }
        else if ((_m = prop.type) === null || _m === void 0 ? void 0 : _m.includes('string')) {
            propType = 'string';
        }
        else if (((_o = prop.schema) === null || _o === void 0 ? void 0 : _o.schema) && Object.values((_p = prop.schema) === null || _p === void 0 ? void 0 : _p.schema).some((s) => typeof s === 'object' && (s === null || s === void 0 ? void 0 : s.kind) === 'object')) {
            propType = 'object';
        }
        else {
            propType = 'string';
        }
        componentCache.set(cacheKey, propType);
    }
    return propType;
}
/**
 * Determines if the current position is inside a MDC block component.
 *
 * @param {vscode.TextDocument} document - The VS Code text document.
 * @param {number} lineNumber - The 1-based line number of the current cursor position.
 * @returns {boolean} - True if inside a MDC block component, false otherwise.
 */
function isInsideMDCComponent(document, lineNumber) {
    var _a;
    const lines = getModelLines(document);
    const componentStack = [];
    for (let i = 0; i < lineNumber; i++) {
        const line = (_a = lines === null || lines === void 0 ? void 0 : lines[i]) === null || _a === void 0 ? void 0 : _a.trim();
        if (!line) {
            continue;
        }
        // Check for component start
        const startMatch = line.match(MDC_COMPONENT_START_REGEX);
        if (startMatch) {
            componentStack.push(startMatch[1]);
            continue;
        }
        // Check for component end
        if (line === '::') {
            componentStack.pop();
        }
    }
    // If stack has any components, we're inside at least one MDC component
    return componentStack.length > 0;
}
/**
 * Determines if the current position is inside a YAML block.
 *
 * @param {vscode.TextDocument} document - The VS Code text document.
 * @param {number} lineNumber - The 1-based line number of the current cursor position.
 * @returns {boolean} - True if inside a YAML block, false otherwise.
 */
function isInsideYAMLBlock(document, lineNumber) {
    var _a;
    const lines = getModelLines(document);
    let insideYAMLBlock = false;
    for (let i = 0; i < lineNumber; i++) {
        const line = (_a = lines === null || lines === void 0 ? void 0 : lines[i]) === null || _a === void 0 ? void 0 : _a.trim();
        if (!line) {
            continue;
        }
        // Toggle insideYAMLBlock flag when encountering YAML block delimiters (---)
        if (/^\s*---\s*$/.test(line)) {
            insideYAMLBlock = !insideYAMLBlock;
        }
    }
    // Return true if inside a YAML block
    return insideYAMLBlock;
}
/**
 * Determines if the current position is inside a markdown code block.
 *
 * @param {vscode.TextDocument} document - The VS Code text document.
 * @param {number} lineNumber - The 1-based line number of the current cursor position.
 * @returns {boolean} - True if inside a markdown code block, false otherwise.
 */
function isInsideCodeBlock(document, lineNumber) {
    var _a;
    const lines = getModelLines(document);
    let insideCodeBlock = false;
    for (let i = 0; i < lineNumber; i++) {
        const line = (_a = lines === null || lines === void 0 ? void 0 : lines[i]) === null || _a === void 0 ? void 0 : _a.trim();
        if (!line) {
            continue;
        }
        // Toggle insideCodeBlock flag when encountering a code block delimiter (``` or ~~~)
        if (/^\s*(?:`{3,}|~{3,})/.test(line)) {
            insideCodeBlock = !insideCodeBlock;
        }
    }
    // Return true if inside a markdown code block
    return insideCodeBlock;
}
/**
 * Determines if the current position is inside a YAML multiline string.
 * Returns false when cursor returns to the same indentation level as the multiline property.
 *
 * @param {vscode.TextDocument} document - The VS Code text document.
 * @param {number} lineNumber - The 1-based line number of the current cursor position.
 * @returns {boolean} - True if inside a YAML multiline string, false otherwise.
 */
function isInsideYAMLMultilineString(document, lineNumber) {
    const lines = getModelLines(document);
    const currentLine = lines[lineNumber - 1];
    const currentIndentation = currentLine.length - currentLine.trimStart().length;
    let multilineStartIndentation = null;
    // Work backwards from current line to find the last multiline string start
    for (let i = lineNumber - 1; i >= 0; i--) {
        const line = lines[i];
        const trimmedLine = line.trim();
        const lineIndentation = line.length - line.trimStart().length;
        // If we find a YAML marker (---) before a multiline marker, we're not in a multiline string
        if (trimmedLine === '---') {
            return false;
        }
        // Check for multiline string start
        MULTILINE_STRING_REGEX.lastIndex = 0;
        if (MULTILINE_STRING_REGEX.test(trimmedLine)) {
            multilineStartIndentation = lineIndentation;
            break;
        }
    }
    // If we didn't find a multiline string start, or we're at the same indentation level
    // as the multiline property, we're not inside the multiline string
    if (multilineStartIndentation === null || currentIndentation <= multilineStartIndentation) {
        return false;
    }
    return true;
}
/**
 * Generates a string representing slot content.
 */
function getSlotContent(cursorIndex) {
    const placeholderText = '<!-- Slot content -->';
    // Two spaces before the content to auto-indent
    return typeof cursorIndex === 'number' ? '\n${' + cursorIndex + ':' + placeholderText + '}' : `\n${placeholderText}`;
}
/**
 * Retrieves the name of the current MDC component at a given line number in a VS Code text document.
 *
 * This function scans through the lines of the provided text document up to the specified line number,
 * maintaining a stack of component names to determine the current nesting level of MDC components.
 *
 * @param {vscode.TextDocument} document - The VS Code text document.
 * @param {number} lineNumber - The 1-based line number of the current cursor position.
 * @returns {string} - The name of the current MDC component at the specified line number, or `undefined` if no component is found.
 */
function getCurrentMDCComponentName(document, lineNumber) {
    var _a;
    const lines = getModelLines(document);
    const componentStack = [];
    // Scan through lines up to current position
    for (let i = 0; i < lineNumber; i++) {
        const line = (_a = lines === null || lines === void 0 ? void 0 : lines[i]) === null || _a === void 0 ? void 0 : _a.trim();
        if (!line) {
            continue;
        }
        // Check for component start
        const startMatch = line.match(MDC_COMPONENT_START_REGEX);
        if (startMatch) {
            componentStack.push({ name: startMatch[1], line: i });
            continue;
        }
        // Check for component end
        if (line === '::') {
            componentStack.pop();
        }
    }
    // Get the most recently added component (last item in stack)
    // This will be the innermost component at the cursor position
    const currentComponent = componentStack[componentStack.length - 1];
    return currentComponent === null || currentComponent === void 0 ? void 0 : currentComponent.name;
}
/**
 * Gets the documentation link for a component, using cache when available.
 *
 * @param {MDCComponentData | undefined} component - The MDC component
 * @returns {string} - Markdown formatted documentation link or empty string
 */
function getComponentDocsLink(component) {
    if (!(component === null || component === void 0 ? void 0 : component.mdc_name)) {
        return '';
    }
    let cached = docsLinkCache.get(component.mdc_name);
    if (cached === undefined) {
        cached = (!component.docs_url)
            ? ''
            : `[View the '${component.mdc_name}' docs ↗](${component.docs_url})`;
        docsLinkCache.set(component.mdc_name, cached);
    }
    return cached;
}
/**
 * Gets the boundaries of a YAML block at a specific line, using cache when available.
 *
 * @param {vscode.TextDocument} document - The VS Code text document
 * @param {number} lineNumber - The 1-based line number to get YAML block boundaries for
 * @returns {{ start: number; end: number } | undefined} - Object containing block boundaries or undefined if not in a YAML block
 */
function getYAMLBlockBoundaries(document, lineNumber) {
    let documentCache = yamlBlockBoundaryCache.get(document);
    if (!documentCache) {
        documentCache = new Map();
        yamlBlockBoundaryCache.set(document, documentCache);
    }
    let boundaries = documentCache.get(lineNumber);
    if (!boundaries) {
        const lines = getModelLines(document);
        let blockStart = -1;
        let blockEnd = lines.length;
        // Find start of current YAML block
        for (let i = lineNumber - 1; i >= 0; i--) {
            if (lines[i].trim() === '---') {
                blockStart = i;
                break;
            }
        }
        // Find end of current YAML block
        for (let i = lineNumber; i < lines.length; i++) {
            if (lines[i].trim() === '---') {
                blockEnd = i;
                break;
            }
        }
        if (blockStart !== -1) {
            boundaries = { start: blockStart, end: blockEnd };
            documentCache.set(lineNumber, boundaries);
        }
    }
    return boundaries;
}
/**
 * Get the current YAML path based on indentation levels and MDC component context
 */
function getCurrentYAMLPath(document, lineNumber) {
    var _a;
    const lines = getModelLines(document);
    const path = [];
    // Handle case where we're at line start
    if (lineNumber <= 0 || lineNumber > lines.length) {
        return path;
    }
    // Get current line, do **not** need to subtract 1
    const currentLine = lines[lineNumber];
    const currentIndentation = currentLine.length - currentLine.trimStart().length;
    const boundaries = getYAMLBlockBoundaries(document, lineNumber);
    if (!boundaries) {
        return path;
    }
    let lastIndentation = currentIndentation;
    // Scan backwards to find parent prop
    for (let i = lineNumber - 1; i >= boundaries.start; i--) {
        const line = lines[i];
        const lineIndentation = line.length - line.trimStart().length;
        const trimmedLine = line.trim();
        // Skip empty lines, YAML block markers, or lines beyond the block end
        if (!trimmedLine || trimmedLine === '---' || i > boundaries.end) {
            continue;
        }
        // A line is a potential parent if:
        // 1. It ends with a colon (allowing for whitespace)
        // 2. It has less indentation than current line
        const isParentProp = trimmedLine.match(/:\s*$/) && lineIndentation < lastIndentation;
        if (isParentProp) {
            const propMatch = (_a = trimmedLine.match(/^([\w-]+):/)) === null || _a === void 0 ? void 0 : _a[1];
            if (propMatch) {
                path.unshift(propMatch);
                lastIndentation = lineIndentation;
            }
        }
    }
    return path;
}
/**
 * Get existing props from the current YAML block
 */
function getCurrentYAMLBlockProps(document, lineNumber) {
    const lines = getModelLines(document);
    const existingProps = new Set();
    const currentIndentation = lines[lineNumber - 1].length - lines[lineNumber - 1].trimStart().length;
    const boundaries = getYAMLBlockBoundaries(document, lineNumber);
    if (!boundaries) {
        return existingProps;
    }
    // Extract props at the same indentation level from the current YAML block
    for (let i = boundaries.start + 1; i < boundaries.end; i++) {
        const line = lines[i];
        const lineIndentation = line.length - line.trimStart().length;
        // Only process lines at the same indentation level as the cursor
        if (lineIndentation === currentIndentation) {
            const match = line.trim().match(/^([\w-]+):/);
            if (match) {
                const propName = match[1];
                existingProps.add((0, scule_1.kebabCase)(propName));
                existingProps.add((0, scule_1.camelCase)(propName));
            }
        }
    }
    return existingProps;
}
/**
 * Generate the VS Code completion item provider for MDC components.
 *
 * @param {MDCComponentData[]} componentData - The MDC component data
 * @param {MdcCompletionItemProviderConfig} { document, position }
 * @return {*}  {(vscode.CompletionItem[] | undefined)}
 */
function getMdcComponentCompletionItemProvider(componentData = [], { document, position }) {
    var _a, _b, _c;
    // Get the text until the current cursor position
    const lineContent = document.lineAt(position.line).text;
    const textUntilPosition = lineContent.slice(0, position.character);
    /**
     * Define basic pattern to identify MDC component usage,
     * meaning a line that starts with a colon or double colon.
     *
     * Example: `:` or `::` - it will then suggest MDC component names.
     */
    const mdcPattern = /^\s*:{1,}[a-zA-Z-]{0,}\s*$/;
    // If conditions not met, exit early
    if (!mdcPattern.test(textUntilPosition) || // If it doesn't match the syntax
        componentData.length === 0 || // If there is no component data
        isInsideYAMLBlock(document, position.line) || // If inside a YAML block
        isInsideCodeBlock(document, position.line) // If inside a code block
    ) {
        return;
    }
    // Count the number of `:` colon characters in the input text in order to properly match in the output
    const colonCharacterCount = (textUntilPosition.match(/:/g) || []).length;
    // Ensure there is always a minimum of 2 colons
    const blockSeparator = ':'.repeat(Math.max(2, colonCharacterCount));
    function getMdcComponentInsertText({ name, contentPlaceholder = '' }) {
        const componentName = (0, scule_1.kebabCase)(name);
        const propsPlaceholder = '\n---${1:}\n---';
        // If the colon character count is 1, add a colon before the component name to make it a block component
        return `${colonCharacterCount === 1 ? ':' : ''}${componentName}${propsPlaceholder}${contentPlaceholder}\n${blockSeparator}\n`;
    }
    // Get the word at current position
    const wordRange = document.getWordRangeAtPosition(position);
    // const wordInfo = wordRange ? document.getText(wordRange) : ''
    // Create a Map to store unique suggestions
    const uniqueSuggestions = new Map();
    // Loop through the component data and generate suggestions
    for (const component of componentData) {
        if (!!component.mdc_name && !uniqueSuggestions.has(component.mdc_name)) {
            const docsMarkdownLink = getComponentDocsLink(component);
            const documentationMarkdown = component.documentation_markdown ? component.documentation_markdown : component.docs_url ? docsMarkdownLink : undefined;
            uniqueSuggestions.set(component.mdc_name, {
                label: component.mdc_name,
                kind: vscode.CompletionItemKind.Function,
                range: wordRange,
                insertText: new vscode.SnippetString(getMdcComponentInsertText({
                    name: component.mdc_name,
                    // Conditionally render the default slot content placeholder if the component has slots
                    contentPlaceholder: ((_c = (_b = (_a = component.component_meta) === null || _a === void 0 ? void 0 : _a.meta) === null || _b === void 0 ? void 0 : _b.slots) === null || _c === void 0 ? void 0 : _c.length) ? getSlotContent(2) : ''
                })),
                detail: component.description,
                documentation: documentationMarkdown
                    ? new vscode.MarkdownString(documentationMarkdown)
                    : undefined,
                command: {
                    command: 'editor.action.formatDocument',
                    title: 'Format Document'
                }
            });
        }
    }
    // Create an array of unique suggestions from the Map
    const suggestions = Array.from(uniqueSuggestions.values());
    return suggestions;
}
exports.getMdcComponentCompletionItemProvider = getMdcComponentCompletionItemProvider;
/**
 * Generate the VS Code completion item provider for MDC component props.
 *
 * @param {MDCComponentData[]} componentData - The MDC component data
 * @param {MdcCompletionItemProviderConfig} { document, position }: MdcCompletionItemProviderConfig
 * @return {*}  {(vscode.CompletionItem[] | undefined)}
 */
function getMdcComponentPropCompletionItemProvider(componentData = [], { document, position }) {
    var _a, _b, _c;
    // Invalidate cache at the start of a new completion request
    invalidateLineCache(document);
    // Get the text until the current cursor position
    const lineContent = document.lineAt(position.line).text;
    const textUntilPosition = lineContent.slice(0, position.character);
    /**
     * Define basic pattern to identify MDC component prop usage,
     * meaning a line that starts with at least one alphabetic character.
     *
     * Example: `a` or `  a` - it will then suggest MDC component props.
     */
    const propNamePattern = /^\s*[a-zA-Z-]{0,}$/;
    // If conditions not met, exit early
    if (!propNamePattern.test(textUntilPosition) || // If it doesn't match the syntax
        componentData.length === 0 || // If there is no component data
        !isInsideMDCComponent(document, position.line) || // If NOT inside a MDC block component
        !isInsideYAMLBlock(document, position.line) || // If NOT inside a YAML block
        isInsideCodeBlock(document, position.line) || // If inside a code block
        isInsideYAMLMultilineString(document, position.line) // If inside a YAML multiline string
    ) {
        return;
    }
    const currentYAMLPath = getCurrentYAMLPath(document, position.line);
    const currentMdcBlockName = getCurrentMDCComponentName(document, position.line);
    if (!currentMdcBlockName) {
        return;
    }
    const mdcComponent = componentData.find(c => c.mdc_name === currentMdcBlockName);
    const docsMarkdownLink = getComponentDocsLink(mdcComponent);
    if (!((_b = (_a = mdcComponent === null || mdcComponent === void 0 ? void 0 : mdcComponent.component_meta) === null || _a === void 0 ? void 0 : _a.meta) === null || _b === void 0 ? void 0 : _b.props)) {
        return;
    }
    // Get the word at current position
    const wordRange = document.getWordRangeAtPosition(position);
    // const wordInfo = wordRange ? document.getText(wordRange) : ''
    const suggestionsByComponent = new Map();
    suggestionsByComponent.set(currentMdcBlockName, []);
    // Get either top-level props or nested props based on YAML path
    let propsToSuggest = [];
    if (currentYAMLPath.length > 0) {
        // Find the parent prop
        const parentProp = mdcComponent.component_meta.meta.props.find(p => (0, scule_1.kebabCase)(p.name) === currentYAMLPath[0]);
        if (parentProp) {
            const nestedProps = getNestedProps(mdcComponent, parentProp);
            if (nestedProps) {
                // Convert nested props schema to array format
                propsToSuggest = Object.entries(nestedProps).map(([name, schema]) => (Object.assign({ name }, schema)));
            }
        }
    }
    else {
        // Use top-level props
        propsToSuggest = mdcComponent.component_meta.meta.props;
    }
    const existingProps = getCurrentYAMLBlockProps(document, position.line);
    for (const prop of propsToSuggest) {
        const { kebab: propNameKebab, camel: propNameCamel } = getCachedPropNames(currentMdcBlockName, prop.name);
        // Skip existing props
        if (existingProps.has(propNameKebab) || existingProps.has(propNameCamel)) {
            continue;
        }
        // Determine the prop value type
        const propValueType = getPropValueType(mdcComponent, prop);
        function getPropInsertText(name, type) {
            if (prop.name === 'styles') {
                // Special handling for the `styles` prop since it's always a multiline string
                return `${name}: |\n` + '  ${0:/** Add CSS */}';
            }
            else if (type === 'boolean') {
                return `${name}: ` + '${0:true}';
            }
            else if (type === 'number') {
                return `${name}: ` + '${0:}';
            }
            else if (type === 'array') {
                return `${name}: ` + '["${0:}"]';
            }
            else if (type === 'array-unquoted') {
                return `${name}: ` + '[${0:}]';
            }
            else if (type === 'string') {
                return `${name}: ` + '"${0:}"';
            }
            else {
                // Object
                return `${name}: ` + '\n  ${0:}';
            }
        }
        suggestionsByComponent.get(currentMdcBlockName).push({
            // @ts-ignore - This satisfies the `CompletionItemLabel` interface: https://code.visualstudio.com/api/references/vscode-api#CompletionItemLabel
            label: {
                label: propNameKebab,
                description: (_c = prop.type) === null || _c === void 0 ? void 0 : _c.replace('| undefined', '').replace('| null', ''),
                detail: prop.required ? ' (required)' : undefined // Shows up as dimmed text after description
            },
            filterText: `${propNameKebab} ${propNameCamel}`,
            sortText: prop.required ? '_' + propNameKebab : propNameKebab,
            kind: vscode.CompletionItemKind.Property,
            range: wordRange,
            insertText: new vscode.SnippetString(getPropInsertText(propNameKebab, propValueType)),
            detail: prop.description,
            documentation: new vscode.MarkdownString(docsMarkdownLink),
            command: {
                command: 'editor.action.triggerSuggest',
                title: 'Trigger Suggestions'
            }
        });
    }
    return Array.from(suggestionsByComponent.values()).flat();
}
exports.getMdcComponentPropCompletionItemProvider = getMdcComponentPropCompletionItemProvider;
/**
 * Creates document lifecycle listeners to manage cache cleanup
 */
function createCacheCleanupListeners() {
    const watchedDocuments = new Set();
    /**
     * Check if the document is a markdown or MDC file by checking both extension and language ID
     */
    function isMarkdownOrMDCDocument(document) {
        const extension = document.uri.fsPath.toLowerCase();
        const isMDCOrMDFile = extension.endsWith('.mdc') || extension.endsWith('.md');
        const isMDCOrMDLanguage = document.languageId === 'mdc' || document.languageId === 'markdown';
        return isMDCOrMDFile || isMDCOrMDLanguage;
    }
    const disposable = vscode.Disposable.from(
    // Listen for document close events
    vscode.workspace.onDidCloseTextDocument((document) => {
        if (!isMarkdownOrMDCDocument(document)) {
            return;
        }
        const uri = document.uri.toString();
        if (watchedDocuments.has(uri)) {
            cleanupDocumentCaches(document);
            watchedDocuments.delete(uri);
        }
    }), 
    // Listen for document open events
    vscode.workspace.onDidOpenTextDocument((document) => {
        if (!isMarkdownOrMDCDocument(document)) {
            return;
        }
        watchedDocuments.add(document.uri.toString());
    }));
    // Return disposable that cleans up everything
    return {
        dispose: () => {
            disposable.dispose();
            // Clean up any remaining caches
            propNameCache.clear();
            nestedPropsCache.clear();
            propTypeCache.clear();
            docsLinkCache.clear();
            watchedDocuments.clear();
        }
    };
}
exports.createCacheCleanupListeners = createCacheCleanupListeners;
/**
 * Cleans up all caches associated with a document
 */
function cleanupDocumentCaches(document) {
    (0, logger_1.logger)('Clean up caches for document: ' + document.uri.toString());
    // Clear document-specific caches
    lineContentCache.delete(document);
    yamlBlockBoundaryCache.delete(document);
    // Clear component-related caches if this is the last document
    if (vscode.workspace.textDocuments.length <= 1) {
        (0, logger_1.logger)('Clean up component-related caches');
        propNameCache.clear();
        nestedPropsCache.clear();
        propTypeCache.clear();
        docsLinkCache.clear();
    }
}
//# sourceMappingURL=completion-providers.js.map