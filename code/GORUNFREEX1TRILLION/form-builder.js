/**
 * GORUNFREEX1TRILLION - FORM BUILDER
 * Dynamic forms, Validation, Multi-step, File uploads, Conditional logic
 */

const { EventEmitter } = require('events');
const crypto = require('crypto');

// ============================================
// FORM SCHEMA
// ============================================

class FormSchema {
  constructor(config = {}) {
    this.id = config.id || crypto.randomBytes(8).toString('hex');
    this.name = config.name || 'Untitled Form';
    this.description = config.description || '';
    this.fields = [];
    this.steps = [];
    this.validation = {};
    this.conditionalLogic = [];
    this.settings = {
      multiStep: config.multiStep || false,
      showProgressBar: config.showProgressBar || true,
      submitButton: config.submitButton || 'Submit',
      successMessage: config.successMessage || 'Form submitted successfully!',
      ...config.settings
    };
  }

  addField(field) {
    const fieldConfig = new FormField(field);
    this.fields.push(fieldConfig);

    if (field.validation) {
      this.validation[field.name] = field.validation;
    }

    return this;
  }

  addStep(step) {
    this.steps.push({
      id: step.id || `step-${this.steps.length + 1}`,
      title: step.title,
      description: step.description,
      fields: step.fields || []
    });
    return this;
  }

  addCondition(condition) {
    this.conditionalLogic.push(condition);
    return this;
  }

  getField(name) {
    return this.fields.find(f => f.name === name);
  }

  toJSON() {
    return {
      id: this.id,
      name: this.name,
      description: this.description,
      fields: this.fields.map(f => f.toJSON()),
      steps: this.steps,
      validation: this.validation,
      conditionalLogic: this.conditionalLogic,
      settings: this.settings
    };
  }
}

// ============================================
// FORM FIELD
// ============================================

class FormField {
  constructor(config) {
    this.name = config.name;
    this.type = config.type || 'text';
    this.label = config.label || config.name;
    this.placeholder = config.placeholder || '';
    this.defaultValue = config.defaultValue;
    this.required = config.required || false;
    this.disabled = config.disabled || false;
    this.hidden = config.hidden || false;
    this.validation = config.validation || {};
    this.options = config.options || []; // For select, radio, checkbox
    this.min = config.min;
    this.max = config.max;
    this.step = config.step;
    this.pattern = config.pattern;
    this.accept = config.accept; // For file inputs
    this.multiple = config.multiple || false;
    this.rows = config.rows; // For textarea
    this.helpText = config.helpText;
    this.prefix = config.prefix;
    this.suffix = config.suffix;
    this.className = config.className;
    this.conditionalLogic = config.conditionalLogic;
  }

  toJSON() {
    return { ...this };
  }
}

// ============================================
// FORM VALIDATOR
// ============================================

class FormValidator {
  constructor() {
    this.rules = new Map();
    this.setupDefaultRules();
  }

  setupDefaultRules() {
    this.addRule('required', (value) => {
      if (Array.isArray(value)) return value.length > 0;
      if (typeof value === 'string') return value.trim().length > 0;
      return value !== null && value !== undefined;
    }, 'This field is required');

    this.addRule('email', (value) => {
      if (!value) return true;
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    }, 'Please enter a valid email address');

    this.addRule('url', (value) => {
      if (!value) return true;
      try { new URL(value); return true; } catch { return false; }
    }, 'Please enter a valid URL');

    this.addRule('phone', (value) => {
      if (!value) return true;
      return /^[\d\s\-+()]+$/.test(value) && value.replace(/\D/g, '').length >= 10;
    }, 'Please enter a valid phone number');

    this.addRule('minLength', (value, min) => {
      if (!value) return true;
      return String(value).length >= min;
    }, (min) => `Must be at least ${min} characters`);

    this.addRule('maxLength', (value, max) => {
      if (!value) return true;
      return String(value).length <= max;
    }, (max) => `Must be no more than ${max} characters`);

    this.addRule('min', (value, min) => {
      if (value === null || value === undefined || value === '') return true;
      return Number(value) >= min;
    }, (min) => `Must be at least ${min}`);

    this.addRule('max', (value, max) => {
      if (value === null || value === undefined || value === '') return true;
      return Number(value) <= max;
    }, (max) => `Must be no more than ${max}`);

    this.addRule('pattern', (value, pattern) => {
      if (!value) return true;
      return new RegExp(pattern).test(value);
    }, 'Invalid format');

    this.addRule('match', (value, fieldName, formData) => {
      return value === formData[fieldName];
    }, (fieldName) => `Must match ${fieldName}`);

    this.addRule('date', (value) => {
      if (!value) return true;
      return !isNaN(Date.parse(value));
    }, 'Please enter a valid date');

    this.addRule('number', (value) => {
      if (!value) return true;
      return !isNaN(Number(value));
    }, 'Please enter a valid number');

    this.addRule('integer', (value) => {
      if (!value) return true;
      return Number.isInteger(Number(value));
    }, 'Please enter a whole number');

    this.addRule('creditCard', (value) => {
      if (!value) return true;
      const digits = value.replace(/\D/g, '');
      if (digits.length < 13 || digits.length > 19) return false;
      // Luhn algorithm
      let sum = 0;
      let isEven = false;
      for (let i = digits.length - 1; i >= 0; i--) {
        let digit = parseInt(digits[i], 10);
        if (isEven) {
          digit *= 2;
          if (digit > 9) digit -= 9;
        }
        sum += digit;
        isEven = !isEven;
      }
      return sum % 10 === 0;
    }, 'Please enter a valid credit card number');

    this.addRule('fileSize', (files, maxSize) => {
      if (!files || files.length === 0) return true;
      const maxBytes = maxSize * 1024 * 1024; // MB to bytes
      for (const file of files) {
        if (file.size > maxBytes) return false;
      }
      return true;
    }, (maxSize) => `File size must be less than ${maxSize}MB`);

    this.addRule('fileType', (files, types) => {
      if (!files || files.length === 0) return true;
      const allowedTypes = Array.isArray(types) ? types : types.split(',');
      for (const file of files) {
        const ext = file.name.split('.').pop().toLowerCase();
        if (!allowedTypes.includes(ext) && !allowedTypes.includes(file.type)) {
          return false;
        }
      }
      return true;
    }, (types) => `Allowed file types: ${types}`);
  }

  addRule(name, validator, message) {
    this.rules.set(name, { validator, message });
    return this;
  }

  validate(value, rules, formData = {}) {
    const errors = [];

    for (const [ruleName, ruleConfig] of Object.entries(rules)) {
      const rule = this.rules.get(ruleName);
      if (!rule) continue;

      const ruleValue = ruleConfig === true ? undefined : ruleConfig;
      const isValid = rule.validator(value, ruleValue, formData);

      if (!isValid) {
        const message = typeof rule.message === 'function'
          ? rule.message(ruleValue)
          : rule.message;
        errors.push({ rule: ruleName, message });
      }
    }

    return { valid: errors.length === 0, errors };
  }

  validateForm(formData, schema) {
    const fieldErrors = {};
    let isValid = true;

    for (const field of schema.fields) {
      const value = formData[field.name];
      const rules = { ...field.validation };

      if (field.required) {
        rules.required = true;
      }

      const result = this.validate(value, rules, formData);
      if (!result.valid) {
        fieldErrors[field.name] = result.errors;
        isValid = false;
      }
    }

    return { valid: isValid, errors: fieldErrors };
  }
}

// ============================================
// FORM RENDERER
// ============================================

class FormRenderer {
  constructor(schema, options = {}) {
    this.schema = schema;
    this.options = options;
    this.theme = options.theme || 'default';
  }

  render() {
    const fields = this.schema.fields.map(f => this.renderField(f)).join('\n');

    return `<form id="${this.schema.id}" class="noizy-form noizy-form--${this.theme}">
      ${this.schema.name ? `<h2 class="form-title">${this.schema.name}</h2>` : ''}
      ${this.schema.description ? `<p class="form-description">${this.schema.description}</p>` : ''}
      <div class="form-fields">${fields}</div>
      <div class="form-actions">
        <button type="submit" class="btn btn-primary">${this.schema.settings.submitButton}</button>
      </div>
    </form>`;
  }

  renderField(field) {
    const wrapper = `<div class="form-field form-field--${field.type} ${field.className || ''}" ${field.hidden ? 'style="display:none"' : ''}>`;
    const label = field.label ? `<label for="${field.name}">${field.label}${field.required ? ' <span class="required">*</span>' : ''}</label>` : '';
    const help = field.helpText ? `<small class="help-text">${field.helpText}</small>` : '';
    const error = `<div class="error-message" data-field="${field.name}"></div>`;

    let input;
    switch (field.type) {
      case 'textarea':
        input = `<textarea name="${field.name}" id="${field.name}" placeholder="${field.placeholder}" rows="${field.rows || 4}" ${field.required ? 'required' : ''} ${field.disabled ? 'disabled' : ''}>${field.defaultValue || ''}</textarea>`;
        break;

      case 'select':
        const options = field.options.map(o =>
          `<option value="${o.value}" ${o.value === field.defaultValue ? 'selected' : ''}>${o.label}</option>`
        ).join('');
        input = `<select name="${field.name}" id="${field.name}" ${field.required ? 'required' : ''} ${field.disabled ? 'disabled' : ''} ${field.multiple ? 'multiple' : ''}>${options}</select>`;
        break;

      case 'radio':
        input = field.options.map(o =>
          `<label class="radio-label"><input type="radio" name="${field.name}" value="${o.value}" ${o.value === field.defaultValue ? 'checked' : ''} ${field.disabled ? 'disabled' : ''}> ${o.label}</label>`
        ).join('');
        break;

      case 'checkbox':
        if (field.options?.length) {
          input = field.options.map(o =>
            `<label class="checkbox-label"><input type="checkbox" name="${field.name}[]" value="${o.value}" ${field.disabled ? 'disabled' : ''}> ${o.label}</label>`
          ).join('');
        } else {
          input = `<label class="checkbox-label"><input type="checkbox" name="${field.name}" ${field.defaultValue ? 'checked' : ''} ${field.disabled ? 'disabled' : ''}> ${field.label}</label>`;
        }
        break;

      case 'file':
        input = `<input type="file" name="${field.name}" id="${field.name}" accept="${field.accept || ''}" ${field.multiple ? 'multiple' : ''} ${field.required ? 'required' : ''}>`;
        break;

      case 'range':
        input = `<input type="range" name="${field.name}" id="${field.name}" min="${field.min || 0}" max="${field.max || 100}" step="${field.step || 1}" value="${field.defaultValue || 50}"><output>${field.defaultValue || 50}</output>`;
        break;

      case 'hidden':
        return `<input type="hidden" name="${field.name}" value="${field.defaultValue || ''}">`;

      default:
        const inputType = ['email', 'password', 'number', 'tel', 'url', 'date', 'time', 'datetime-local', 'color'].includes(field.type) ? field.type : 'text';
        input = `${field.prefix ? `<span class="input-prefix">${field.prefix}</span>` : ''}<input type="${inputType}" name="${field.name}" id="${field.name}" placeholder="${field.placeholder}" value="${field.defaultValue || ''}" ${field.min !== undefined ? `min="${field.min}"` : ''} ${field.max !== undefined ? `max="${field.max}"` : ''} ${field.pattern ? `pattern="${field.pattern}"` : ''} ${field.required ? 'required' : ''} ${field.disabled ? 'disabled' : ''}>${field.suffix ? `<span class="input-suffix">${field.suffix}</span>` : ''}`;
    }

    return `${wrapper}${label}<div class="input-wrapper">${input}</div>${help}${error}</div>`;
  }

  renderMultiStep() {
    const steps = this.schema.steps.map((step, index) => {
      const fields = step.fields.map(fieldName => {
        const field = this.schema.getField(fieldName);
        return field ? this.renderField(field) : '';
      }).join('\n');

      return `<div class="form-step" data-step="${index + 1}" ${index > 0 ? 'style="display:none"' : ''}>
        <h3 class="step-title">${step.title}</h3>
        ${step.description ? `<p class="step-description">${step.description}</p>` : ''}
        <div class="step-fields">${fields}</div>
      </div>`;
    }).join('\n');

    const progressBar = this.schema.settings.showProgressBar
      ? `<div class="progress-bar"><div class="progress" style="width: ${100 / this.schema.steps.length}%"></div></div>`
      : '';

    return `<form id="${this.schema.id}" class="noizy-form noizy-form--multistep">
      ${this.schema.name ? `<h2 class="form-title">${this.schema.name}</h2>` : ''}
      ${progressBar}
      <div class="form-steps">${steps}</div>
      <div class="form-navigation">
        <button type="button" class="btn btn-prev" style="display:none">Previous</button>
        <button type="button" class="btn btn-next">Next</button>
        <button type="submit" class="btn btn-primary btn-submit" style="display:none">${this.schema.settings.submitButton}</button>
      </div>
    </form>`;
  }

  getCSS() {
    return `.noizy-form{max-width:600px;margin:0 auto;font-family:system-ui,sans-serif}
.form-field{margin-bottom:20px}.form-field label{display:block;margin-bottom:6px;font-weight:500}
.form-field input,.form-field textarea,.form-field select{width:100%;padding:10px 12px;border:1px solid #ddd;border-radius:6px;font-size:14px}
.form-field input:focus,.form-field textarea:focus,.form-field select:focus{outline:none;border-color:#00ff88;box-shadow:0 0 0 3px rgba(0,255,136,0.1)}
.required{color:#ff4444}.help-text{display:block;margin-top:4px;color:#666;font-size:12px}
.error-message{color:#ff4444;font-size:12px;margin-top:4px}.error-message:empty{display:none}
.form-field.has-error input,.form-field.has-error textarea,.form-field.has-error select{border-color:#ff4444}
.btn{padding:12px 24px;border:none;border-radius:6px;font-size:14px;cursor:pointer;transition:all 0.2s}
.btn-primary{background:#00ff88;color:#000}.btn-primary:hover{background:#00cc6a}
.progress-bar{height:4px;background:#eee;border-radius:2px;margin-bottom:24px}
.progress{height:100%;background:#00ff88;border-radius:2px;transition:width 0.3s}
.radio-label,.checkbox-label{display:flex;align-items:center;gap:8px;margin:8px 0;cursor:pointer}`;
  }

  getJS() {
    return `class NoizyForm{constructor(e){this.form=document.getElementById(e),this.form&&this.init()}init(){this.form.addEventListener("submit",e=>this.handleSubmit(e)),this.form.querySelectorAll("input,textarea,select").forEach(e=>e.addEventListener("blur",()=>this.validateField(e)))}validateField(e){const t=e.name,a=e.value;return!0}handleSubmit(e){e.preventDefault(),console.log("Form submitted",new FormData(this.form))}}`;
  }
}

// ============================================
// FORM BUILDER (FLUENT API)
// ============================================

class FormBuilder {
  constructor(name) {
    this.schema = new FormSchema({ name });
  }

  description(desc) { this.schema.description = desc; return this; }

  text(name, label, options = {}) { return this.field({ type: 'text', name, label, ...options }); }
  email(name, label = 'Email', options = {}) { return this.field({ type: 'email', name, label, validation: { email: true }, ...options }); }
  password(name, label = 'Password', options = {}) { return this.field({ type: 'password', name, label, ...options }); }
  number(name, label, options = {}) { return this.field({ type: 'number', name, label, validation: { number: true }, ...options }); }
  tel(name, label = 'Phone', options = {}) { return this.field({ type: 'tel', name, label, validation: { phone: true }, ...options }); }
  url(name, label = 'URL', options = {}) { return this.field({ type: 'url', name, label, validation: { url: true }, ...options }); }
  date(name, label, options = {}) { return this.field({ type: 'date', name, label, ...options }); }
  time(name, label, options = {}) { return this.field({ type: 'time', name, label, ...options }); }
  textarea(name, label, options = {}) { return this.field({ type: 'textarea', name, label, ...options }); }
  select(name, label, opts, options = {}) { return this.field({ type: 'select', name, label, options: opts, ...options }); }
  radio(name, label, opts, options = {}) { return this.field({ type: 'radio', name, label, options: opts, ...options }); }
  checkbox(name, label, opts, options = {}) { return this.field({ type: 'checkbox', name, label, options: opts, ...options }); }
  file(name, label = 'File', options = {}) { return this.field({ type: 'file', name, label, ...options }); }
  hidden(name, value) { return this.field({ type: 'hidden', name, defaultValue: value }); }
  range(name, label, options = {}) { return this.field({ type: 'range', name, label, ...options }); }

  field(config) { this.schema.addField(config); return this; }

  step(title, description) {
    this.currentStep = { title, description, fields: [] };
    this.schema.addStep(this.currentStep);
    this.schema.settings.multiStep = true;
    return this;
  }

  addToStep(fieldName) {
    if (this.currentStep) this.currentStep.fields.push(fieldName);
    return this;
  }

  when(fieldName, operator, value) {
    this.pendingCondition = { field: fieldName, operator, value };
    return this;
  }

  show(targetField) {
    if (this.pendingCondition) {
      this.schema.addCondition({ ...this.pendingCondition, action: 'show', target: targetField });
      this.pendingCondition = null;
    }
    return this;
  }

  hide(targetField) {
    if (this.pendingCondition) {
      this.schema.addCondition({ ...this.pendingCondition, action: 'hide', target: targetField });
      this.pendingCondition = null;
    }
    return this;
  }

  submitButton(text) { this.schema.settings.submitButton = text; return this; }
  successMessage(msg) { this.schema.settings.successMessage = msg; return this; }

  build() { return this.schema; }

  render(options = {}) {
    const renderer = new FormRenderer(this.schema, options);
    return this.schema.settings.multiStep ? renderer.renderMultiStep() : renderer.render();
  }
}

// ============================================
// EXPORTS
// ============================================

module.exports = {
  FormSchema,
  FormField,
  FormValidator,
  FormRenderer,
  FormBuilder,

  createForm: (name) => new FormBuilder(name),
  createValidator: () => new FormValidator(),
  createRenderer: (schema, options) => new FormRenderer(schema, options)
};
