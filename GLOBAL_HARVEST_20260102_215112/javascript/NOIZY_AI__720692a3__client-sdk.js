// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  VALIDATOR CLIENT SDK                                                      ║
// ║  Call from any Claude session or Worker to validate code in real-time      ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

const VALIDATOR_URL = 'https://validator.fishmusicinc.workers.dev';

class ValidatorClient {
  constructor(baseUrl = VALIDATOR_URL) {
    this.baseUrl = baseUrl;
  }

  async _post(endpoint, data) {
    const res = await fetch(`${this.baseUrl}${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    return res.json();
  }

  // ═══════════════════════════════════════════════════════════════════════
  // SPELL CHECK
  // ═══════════════════════════════════════════════════════════════════════

  async spellCheck(text, language = 'en') {
    return this._post('/api/spell', { text, language });
  }

  // ═══════════════════════════════════════════════════════════════════════
  // CODE CHECKS
  // ═══════════════════════════════════════════════════════════════════════

  async checkJavaScript(code, strict = false) {
    return this._post('/api/check/js', { code, strict });
  }

  async checkPython(code) {
    return this._post('/api/check/python', { code });
  }

  async checkHTML(code) {
    return this._post('/api/check/html', { code });
  }

  async checkCSS(code) {
    return this._post('/api/check/css', { code });
  }

  async checkSQL(code) {
    return this._post('/api/check/sql', { code });
  }

  async checkJSON(code) {
    return this._post('/api/check/json', { code });
  }

  // ═══════════════════════════════════════════════════════════════════════
  // UNIVERSAL CHECK (auto-detect type)
  // ═══════════════════════════════════════════════════════════════════════

  async check(code, options = {}) {
    return this._post('/api/check', {
      code,
      type: options.type,
      filename: options.filename
    });
  }

  // ═══════════════════════════════════════════════════════════════════════
  // BATCH CHECK (multiple files)
  // ═══════════════════════════════════════════════════════════════════════

  async checkBatch(files) {
    return this._post('/api/check/batch', { files });
  }

  // ═══════════════════════════════════════════════════════════════════════
  // CONDUCTOR INTEGRATION
  // ═══════════════════════════════════════════════════════════════════════

  async validateTask(taskId, code, type) {
    return this._post('/api/validate/task', { task_id: taskId, code, type });
  }

  // ═══════════════════════════════════════════════════════════════════════
  // STATS
  // ═══════════════════════════════════════════════════════════════════════

  async getStats() {
    const res = await fetch(`${this.baseUrl}/api/stats`);
    return res.json();
  }

  async getHistory(limit = 50, type = null) {
    const params = new URLSearchParams({ limit });
    if (type) params.set('type', type);
    const res = await fetch(`${this.baseUrl}/api/history?${params}`);
    return res.json();
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// QUICK FUNCTIONS (no client instance needed)
// ═══════════════════════════════════════════════════════════════════════════

async function validateCode(code, type = null) {
  const client = new ValidatorClient();
  return client.check(code, { type });
}

async function spellCheck(text) {
  const client = new ValidatorClient();
  return client.spellCheck(text);
}

async function validateJS(code) {
  const client = new ValidatorClient();
  return client.checkJavaScript(code);
}

async function validatePython(code) {
  const client = new ValidatorClient();
  return client.checkPython(code);
}

async function validateHTML(code) {
  const client = new ValidatorClient();
  return client.checkHTML(code);
}

async function validateCSS(code) {
  const client = new ValidatorClient();
  return client.checkCSS(code);
}

// ═══════════════════════════════════════════════════════════════════════════
// USAGE EXAMPLES
// ═══════════════════════════════════════════════════════════════════════════

/*
// 1. Quick validation (one-liner)
const result = await validateCode('const x = 1');
console.log(result.pass ? '✅ Valid' : '❌ Invalid');

// 2. Spell check text
const spelling = await spellCheck('Teh quik brown fox');
console.log(spelling.errors);  // [{ word: 'teh', suggestion: 'the' }, ...]

// 3. Validate JavaScript
const jsResult = await validateJS(`
  var x = 1;
  console.log(x);
  if (x == 1) { }
`);
console.log(jsResult.warnings);  // [var warning, console.log warning, == warning]

// 4. Batch validate multiple files
const client = new ValidatorClient();
const batch = await client.checkBatch([
  { filename: 'app.js', code: 'const x = 1;' },
  { filename: 'style.css', code: 'body { color: red; }' },
  { filename: 'index.html', code: '<html><body>Hi</body></html>' }
]);
console.log(`Checked ${batch.files_checked} files, ${batch.total_errors} errors`);

// 5. Validate before submitting to Conductor
const validation = await client.validateTask(123, myCode, 'javascript');
if (validation.blocked) {
  console.log('Task blocked due to validation errors!');
}
*/

// Export
if (typeof module !== 'undefined') {
  module.exports = { 
    ValidatorClient, 
    validateCode, 
    spellCheck, 
    validateJS, 
    validatePython, 
    validateHTML, 
    validateCSS,
    VALIDATOR_URL
  };
}
