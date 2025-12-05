"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.titleize = exports.singularize = exports.pluralize = exports.ordinalize = exports.ordinal = exports.dasherize = exports.isPluralizable = exports.humanize = exports.decamelize = exports.underscore = exports.pascalize = exports.camelize = void 0;
/**
 * Converts a string to camelCase, removing dashes/underscores and capitalizing each subsequent word.
 * Useful for generating variable or property names in Angular projects.
 *
 * @param {string} str - The string to convert to camelCase.
 * @returns {string} The camelCased version of the input string.
 * @example
 * camelize('foo-bar'); // 'fooBar'
 */
const camelize = (str) => {
    return str
        .replace(/(?:^\w|[A-Z]|\b\w)/g, (word, index) => index === 0 ? word.toLowerCase() : word.toUpperCase())
        .replace(/\s+/g, '');
};
exports.camelize = camelize;
/**
 * Converts a string to PascalCase, capitalizing the first letter of each word and removing spaces/underscores.
 * Useful for generating class, interface, or type names in Angular projects.
 *
 * @param {string} str - The string to convert to PascalCase.
 * @returns {string} The PascalCase version of the input string.
 * @example
 * pascalize('foo bar'); // 'FooBar'
 */
const pascalize = (str) => {
    return str
        .replace(/(?:^\w|[A-Z]|\b\w)/g, (word) => word.toUpperCase())
        .replace(/\s+/g, '');
};
exports.pascalize = pascalize;
/**
 * Converts a string to snake_case, replacing spaces, dashes, or camel/pascal case transitions with underscores and using lowercase.
 * Useful for generating constant names or file names in Angular projects.
 *
 * @param {string} str - The string to convert to snake_case.
 * @returns {string} The snake_case version of the input string.
 * @example
 * underscore('foo bar'); // 'foo_bar'
 */
const underscore = (str) => {
    return str
        .replace(/(?:^\w|[A-Z]|\b\w)/g, (word, index) => index === 0 ? word.toLowerCase() : `_${word.toLowerCase()}`)
        .replace(/\s+/g, '_');
};
exports.underscore = underscore;
/**
 * Converts a camelCase, PascalCase, or space-separated string to snake_case (lowercase with underscores).
 * Useful for transforming identifiers to a consistent, human-readable format in Angular projects.
 *
 * @param {string} str - The string to convert to snake_case.
 * @returns {string} The snake_case version of the input string.
 * @example
 * decamelize('fooBar'); // 'foo_bar'
 */
const decamelize = (str) => {
    return str
        .replace(/(?:^\w|[A-Z]|\b\w)/g, (word, index) => index === 0 ? word.toLowerCase() : `_${word.toLowerCase()}`)
        .replace(/\s+/g, '_');
};
exports.decamelize = decamelize;
/**
 * Converts a camelCase, PascalCase, snake_case or dash-separated string to a human-readable form (words separated by spaces, capitalized).
 * Useful for displaying variable names or identifiers in UI.
 *
 * @param {string} str - The string to humanize.
 * @returns {string} The human-readable version of the input string.
 * @example
 * humanize('fooBar_baz'); // 'Foo Bar Baz'
 */
const humanize = (str) => {
    return str
        .replace(/(?:^\w|[A-Z]|\b\w)/g, (word, index) => index === 0 ? word.toUpperCase() : ` ${word.toLowerCase()}`)
        .replace(/\s+/g, ' ');
};
exports.humanize = humanize;
/**
 * Checks if a string is pluralizable.
 *
 * @param {string} str - The string to check
 * @example
 * isPluralizable('foo');
 *
 * @returns {boolean} - Whether the string is pluralizable
 */
const isPluralizable = (str) => {
    return str.endsWith('s');
};
exports.isPluralizable = isPluralizable;
/**
 * Converts a camelCase, PascalCase, or space-separated string to kebab-case (lowercase with dashes).
 * This is useful for generating Angular file and selector names.
 *
 * @param {string} inputString - The string to convert.
 * @returns {string} The kebab-case version of the input string.
 */
const dasherize = (inputString) => {
    return inputString
        .replace(/(?:^\w|[A-Z]|\b\w)/g, (word, index) => index === 0 ? word.toLowerCase() : `-${word.toLowerCase()}`)
        .replace(/\s+/g, '-');
};
exports.dasherize = dasherize;
/**
 * Converts a number to its English ordinal string representation (e.g., 1st, 2nd, 3rd, 4th).
 * This is useful for formatting display values in UI or code generation.
 *
 * @param {number} num - The number to convert to ordinal form.
 * @returns {string} The ordinal string (e.g., '1st', '2nd').
 */
const ordinal = (num) => {
    const j = num % 10;
    const k = num % 100;
    if (j === 1 && k !== 11) {
        return `${num}st`;
    }
    if (j === 2 && k !== 12) {
        return `${num}nd`;
    }
    if (j === 3 && k !== 13) {
        return `${num}rd`;
    }
    return `${num}th`;
};
exports.ordinal = ordinal;
/**
 * Returns the ordinalized string for a given number (e.g., 1st, 2nd, 3rd, 4th).
 *
 * @param {number} num - The number to ordinalize.
 * @returns {string} The ordinalized number as a string.
 */
const ordinalize = (num) => {
    return `${num}${(0, exports.ordinal)(num)}`;
};
exports.ordinalize = ordinalize;
/**
 * Converts a singular English noun to its plural form using basic rules.
 * Useful for generating entity names, labels, or code artifacts in Angular projects.
 *
 * @param {string} str - The string to pluralize.
 * @returns {string} The pluralized string.
 * @example
 * pluralize('cat'); // 'cats'
 */
const pluralize = (str) => {
    if (str.endsWith('y')) {
        return str.slice(0, -1) + 'ies';
    }
    if (str.endsWith('s')) {
        return str;
    }
    return str + 's';
};
exports.pluralize = pluralize;
/**
 * Converts a plural English noun to its singular form using basic rules.
 * Useful for generating entity names, labels, or code artifacts in Angular projects.
 *
 * @param {string} str - The string to singularize.
 * @returns {string} The singularized string.
 */
const singularize = (str) => {
    if (str.endsWith('ies')) {
        return str.slice(0, -3) + 'y';
    }
    if (str.endsWith('s')) {
        return str.slice(0, -1);
    }
    return str;
};
exports.singularize = singularize;
/**
 * Converts a string to Title Case, capitalizing the first letter of each word and replacing dashes/underscores with spaces.
 * Useful for formatting labels, UI strings, or class names in Angular projects.
 *
 * @param {string} str - The string to convert to title case.
 * @returns {string} The title-cased version of the input string.
 * @example
 * titleize('foo bar'); // 'Foo Bar'
 */
const titleize = (str) => {
    return str
        .split(' ')
        .map((word) => word[0].toUpperCase() + word.slice(1))
        .join(' ');
};
exports.titleize = titleize;
//# sourceMappingURL=inflector.helper.js.map