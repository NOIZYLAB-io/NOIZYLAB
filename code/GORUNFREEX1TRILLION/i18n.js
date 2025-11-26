/**
 * GORUNFREEX1TRILLION - INTERNATIONALIZATION (i18n)
 * Translations, Pluralization, Date/Number formatting, RTL support
 */

const { EventEmitter } = require('events');

// ============================================
// I18N MANAGER
// ============================================

class I18nManager extends EventEmitter {
  constructor(options = {}) {
    super();
    this.defaultLocale = options.defaultLocale || 'en';
    this.fallbackLocale = options.fallbackLocale || 'en';
    this.currentLocale = this.defaultLocale;
    this.locales = new Map();
    this.formatters = new Map();
    this.pluralRules = new Map();
    this.missingKeyHandler = options.missingKeyHandler || ((key) => key);

    this.setupPluralRules();
  }

  setupPluralRules() {
    // English plural rules
    this.pluralRules.set('en', (n) => n === 1 ? 'one' : 'other');

    // French
    this.pluralRules.set('fr', (n) => n <= 1 ? 'one' : 'other');

    // Russian (complex pluralization)
    this.pluralRules.set('ru', (n) => {
      const mod10 = n % 10;
      const mod100 = n % 100;
      if (mod10 === 1 && mod100 !== 11) return 'one';
      if (mod10 >= 2 && mod10 <= 4 && (mod100 < 12 || mod100 > 14)) return 'few';
      return 'many';
    });

    // Arabic
    this.pluralRules.set('ar', (n) => {
      if (n === 0) return 'zero';
      if (n === 1) return 'one';
      if (n === 2) return 'two';
      if (n % 100 >= 3 && n % 100 <= 10) return 'few';
      if (n % 100 >= 11) return 'many';
      return 'other';
    });

    // Japanese, Chinese, Korean (no pluralization)
    ['ja', 'zh', 'ko'].forEach(locale => {
      this.pluralRules.set(locale, () => 'other');
    });
  }

  // Load translations for a locale
  addLocale(locale, translations) {
    const existing = this.locales.get(locale) || {};
    this.locales.set(locale, this.mergeDeep(existing, translations));
    this.emit('locale:added', { locale });
    return this;
  }

  // Set current locale
  setLocale(locale) {
    if (!this.locales.has(locale) && locale !== this.fallbackLocale) {
      console.warn(`Locale '${locale}' not found, using fallback`);
    }
    this.currentLocale = locale;
    this.emit('locale:changed', { locale });
    return this;
  }

  getLocale() {
    return this.currentLocale;
  }

  getAvailableLocales() {
    return Array.from(this.locales.keys());
  }

  // Translate a key
  t(key, params = {}, locale = this.currentLocale) {
    let translation = this.getTranslation(key, locale);

    if (!translation) {
      translation = this.getTranslation(key, this.fallbackLocale);
    }

    if (!translation) {
      this.emit('missing:key', { key, locale });
      return this.missingKeyHandler(key, locale);
    }

    // Handle pluralization
    if (typeof translation === 'object' && params.count !== undefined) {
      translation = this.pluralize(translation, params.count, locale);
    }

    // Interpolate parameters
    return this.interpolate(translation, params);
  }

  // Alias for t
  translate(key, params, locale) {
    return this.t(key, params, locale);
  }

  getTranslation(key, locale) {
    const translations = this.locales.get(locale);
    if (!translations) return null;

    return key.split('.').reduce((obj, k) => obj?.[k], translations);
  }

  interpolate(text, params) {
    return text.replace(/\{\{?\s*(\w+)\s*\}?\}/g, (match, key) => {
      return params[key] !== undefined ? params[key] : match;
    });
  }

  pluralize(translations, count, locale) {
    const rule = this.pluralRules.get(locale) || this.pluralRules.get('en');
    const form = rule(count);

    return translations[form] || translations.other || translations.one || Object.values(translations)[0];
  }

  // Number formatting
  formatNumber(value, options = {}, locale = this.currentLocale) {
    return new Intl.NumberFormat(locale, options).format(value);
  }

  formatCurrency(value, currency = 'USD', locale = this.currentLocale) {
    return new Intl.NumberFormat(locale, {
      style: 'currency',
      currency
    }).format(value);
  }

  formatPercent(value, locale = this.currentLocale) {
    return new Intl.NumberFormat(locale, {
      style: 'percent',
      minimumFractionDigits: 0,
      maximumFractionDigits: 2
    }).format(value);
  }

  // Date formatting
  formatDate(date, options = {}, locale = this.currentLocale) {
    const d = date instanceof Date ? date : new Date(date);
    return new Intl.DateTimeFormat(locale, options).format(d);
  }

  formatDateTime(date, locale = this.currentLocale) {
    return this.formatDate(date, {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: 'numeric',
      minute: 'numeric'
    }, locale);
  }

  formatRelativeTime(date, locale = this.currentLocale) {
    const d = date instanceof Date ? date : new Date(date);
    const now = new Date();
    const diff = d.getTime() - now.getTime();
    const seconds = Math.round(diff / 1000);
    const minutes = Math.round(seconds / 60);
    const hours = Math.round(minutes / 60);
    const days = Math.round(hours / 24);

    const rtf = new Intl.RelativeTimeFormat(locale, { numeric: 'auto' });

    if (Math.abs(seconds) < 60) return rtf.format(seconds, 'second');
    if (Math.abs(minutes) < 60) return rtf.format(minutes, 'minute');
    if (Math.abs(hours) < 24) return rtf.format(hours, 'hour');
    if (Math.abs(days) < 30) return rtf.format(days, 'day');

    return this.formatDate(date, { dateStyle: 'medium' }, locale);
  }

  // List formatting
  formatList(items, options = {}, locale = this.currentLocale) {
    return new Intl.ListFormat(locale, {
      style: options.style || 'long',
      type: options.type || 'conjunction'
    }).format(items);
  }

  // Direction (LTR/RTL)
  getDirection(locale = this.currentLocale) {
    const rtlLocales = ['ar', 'he', 'fa', 'ur'];
    return rtlLocales.includes(locale.split('-')[0]) ? 'rtl' : 'ltr';
  }

  isRTL(locale = this.currentLocale) {
    return this.getDirection(locale) === 'rtl';
  }

  // Deep merge helper
  mergeDeep(target, source) {
    const output = { ...target };
    for (const key in source) {
      if (source[key] instanceof Object && key in target) {
        output[key] = this.mergeDeep(target[key], source[key]);
      } else {
        output[key] = source[key];
      }
    }
    return output;
  }

  // Export/Import
  export(locale) {
    return this.locales.get(locale) || {};
  }

  exportAll() {
    return Object.fromEntries(this.locales);
  }
}

// ============================================
// TRANSLATION LOADER
// ============================================

class TranslationLoader {
  constructor(i18n) {
    this.i18n = i18n;
    this.loadedLocales = new Set();
  }

  async loadFromJSON(locale, translations) {
    this.i18n.addLocale(locale, translations);
    this.loadedLocales.add(locale);
  }

  async loadFromURL(locale, url) {
    try {
      const response = await fetch(url);
      const translations = await response.json();
      this.i18n.addLocale(locale, translations);
      this.loadedLocales.add(locale);
    } catch (error) {
      console.error(`Failed to load translations for ${locale}:`, error);
    }
  }

  isLoaded(locale) {
    return this.loadedLocales.has(locale);
  }
}

// ============================================
// TRANSLATION BUILDER
// ============================================

class TranslationBuilder {
  constructor() {
    this.translations = {};
  }

  add(key, value) {
    const keys = key.split('.');
    let current = this.translations;

    for (let i = 0; i < keys.length - 1; i++) {
      if (!current[keys[i]]) current[keys[i]] = {};
      current = current[keys[i]];
    }

    current[keys[keys.length - 1]] = value;
    return this;
  }

  plural(key, forms) {
    return this.add(key, forms);
  }

  namespace(ns) {
    return new NamespacedBuilder(this, ns);
  }

  build() {
    return this.translations;
  }
}

class NamespacedBuilder {
  constructor(parent, namespace) {
    this.parent = parent;
    this.namespace = namespace;
  }

  add(key, value) {
    this.parent.add(`${this.namespace}.${key}`, value);
    return this;
  }

  plural(key, forms) {
    return this.add(key, forms);
  }

  end() {
    return this.parent;
  }
}

// ============================================
// REACT/TEMPLATE HELPERS
// ============================================

class I18nHelpers {
  constructor(i18n) {
    this.i18n = i18n;
  }

  // Template literal tag
  t(strings, ...values) {
    const key = strings[0];
    const params = values[0] || {};
    return this.i18n.t(key, params);
  }

  // HTML with translations
  html(key, params = {}) {
    const translation = this.i18n.t(key, params);
    return translation; // Would normally sanitize for XSS
  }

  // Attribute helper
  attr(key, params = {}) {
    return this.i18n.t(key, params).replace(/"/g, '&quot;');
  }
}

// ============================================
// LOCALE DETECTOR
// ============================================

class LocaleDetector {
  constructor(options = {}) {
    this.supportedLocales = options.supportedLocales || ['en'];
    this.defaultLocale = options.defaultLocale || 'en';
  }

  detect(sources = {}) {
    // Check explicit setting
    if (sources.query) {
      const locale = this.normalize(sources.query);
      if (this.isSupported(locale)) return locale;
    }

    // Check cookie
    if (sources.cookie) {
      const locale = this.normalize(sources.cookie);
      if (this.isSupported(locale)) return locale;
    }

    // Check Accept-Language header
    if (sources.header) {
      const locales = this.parseAcceptLanguage(sources.header);
      for (const locale of locales) {
        if (this.isSupported(locale)) return locale;
      }
    }

    // Check navigator (browser)
    if (typeof navigator !== 'undefined' && navigator.language) {
      const locale = this.normalize(navigator.language);
      if (this.isSupported(locale)) return locale;
    }

    return this.defaultLocale;
  }

  parseAcceptLanguage(header) {
    return header
      .split(',')
      .map(part => {
        const [locale, q = 'q=1'] = part.trim().split(';');
        return { locale: this.normalize(locale), q: parseFloat(q.split('=')[1]) };
      })
      .sort((a, b) => b.q - a.q)
      .map(item => item.locale);
  }

  normalize(locale) {
    return locale.toLowerCase().replace('_', '-').split('-')[0];
  }

  isSupported(locale) {
    return this.supportedLocales.includes(locale);
  }
}

// ============================================
// EXPORTS
// ============================================

module.exports = {
  I18nManager,
  TranslationLoader,
  TranslationBuilder,
  I18nHelpers,
  LocaleDetector,

  createI18n: (options) => new I18nManager(options),
  createBuilder: () => new TranslationBuilder(),
  createDetector: (options) => new LocaleDetector(options),

  // Preset translations
  presets: {
    common: {
      en: {
        common: {
          yes: 'Yes',
          no: 'No',
          ok: 'OK',
          cancel: 'Cancel',
          save: 'Save',
          delete: 'Delete',
          edit: 'Edit',
          close: 'Close',
          loading: 'Loading...',
          error: 'Error',
          success: 'Success',
          search: 'Search',
          noResults: 'No results found'
        }
      },
      es: {
        common: {
          yes: 'Sí',
          no: 'No',
          ok: 'Aceptar',
          cancel: 'Cancelar',
          save: 'Guardar',
          delete: 'Eliminar',
          edit: 'Editar',
          close: 'Cerrar',
          loading: 'Cargando...',
          error: 'Error',
          success: 'Éxito',
          search: 'Buscar',
          noResults: 'Sin resultados'
        }
      },
      fr: {
        common: {
          yes: 'Oui',
          no: 'Non',
          ok: 'OK',
          cancel: 'Annuler',
          save: 'Enregistrer',
          delete: 'Supprimer',
          edit: 'Modifier',
          close: 'Fermer',
          loading: 'Chargement...',
          error: 'Erreur',
          success: 'Succès',
          search: 'Rechercher',
          noResults: 'Aucun résultat'
        }
      }
    }
  }
};
