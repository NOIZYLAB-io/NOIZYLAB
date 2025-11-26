/**
 * GORUNFREEX1TRILLION - PDF GENERATOR
 * Document builder, Templates, Charts, Invoices, Reports
 */

const { EventEmitter } = require('events');
const crypto = require('crypto');

// ============================================
// PDF DOCUMENT
// ============================================

class PDFDocument extends EventEmitter {
  constructor(options = {}) {
    super();
    this.id = crypto.randomBytes(8).toString('hex');
    this.pages = [];
    this.currentPage = null;
    this.fonts = new Map();
    this.images = new Map();
    this.metadata = {
      title: options.title || 'Document',
      author: options.author || 'NOIZYLAB',
      subject: options.subject || '',
      keywords: options.keywords || [],
      creator: 'GORUNFREEX1TRILLION PDF Engine',
      creationDate: new Date()
    };
    this.options = {
      size: options.size || 'A4',
      orientation: options.orientation || 'portrait',
      margins: options.margins || { top: 72, right: 72, bottom: 72, left: 72 },
      ...options
    };
    this.styles = new Map();
    this.setupDefaultStyles();
    this.addPage();
  }

  setupDefaultStyles() {
    this.registerStyle('h1', { fontSize: 24, fontWeight: 'bold', marginBottom: 12 });
    this.registerStyle('h2', { fontSize: 18, fontWeight: 'bold', marginBottom: 10 });
    this.registerStyle('h3', { fontSize: 14, fontWeight: 'bold', marginBottom: 8 });
    this.registerStyle('body', { fontSize: 12, lineHeight: 1.5 });
    this.registerStyle('small', { fontSize: 10, color: '#666666' });
    this.registerStyle('caption', { fontSize: 9, fontStyle: 'italic', color: '#888888' });
  }

  registerStyle(name, style) {
    this.styles.set(name, style);
    return this;
  }

  getStyle(name) {
    return this.styles.get(name) || {};
  }

  addPage(options = {}) {
    const page = new PDFPage({
      ...this.options,
      ...options,
      pageNumber: this.pages.length + 1
    });
    this.pages.push(page);
    this.currentPage = page;
    this.emit('page:added', { pageNumber: page.pageNumber });
    return this;
  }

  // Text methods
  text(content, options = {}) {
    this.currentPage.addElement({ type: 'text', content, ...options });
    return this;
  }

  heading(content, level = 1) {
    const style = this.getStyle(`h${level}`);
    return this.text(content, style);
  }

  paragraph(content, options = {}) {
    const style = { ...this.getStyle('body'), ...options };
    return this.text(content, style);
  }

  // List methods
  list(items, options = {}) {
    this.currentPage.addElement({
      type: 'list',
      items,
      ordered: options.ordered || false,
      ...options
    });
    return this;
  }

  // Table methods
  table(data, options = {}) {
    this.currentPage.addElement({ type: 'table', data, ...options });
    return this;
  }

  // Image methods
  image(src, options = {}) {
    this.currentPage.addElement({ type: 'image', src, ...options });
    return this;
  }

  // Shape methods
  line(x1, y1, x2, y2, options = {}) {
    this.currentPage.addElement({ type: 'line', x1, y1, x2, y2, ...options });
    return this;
  }

  rect(x, y, width, height, options = {}) {
    this.currentPage.addElement({ type: 'rect', x, y, width, height, ...options });
    return this;
  }

  circle(x, y, radius, options = {}) {
    this.currentPage.addElement({ type: 'circle', x, y, radius, ...options });
    return this;
  }

  // Chart methods
  chart(type, data, options = {}) {
    this.currentPage.addElement({ type: 'chart', chartType: type, data, ...options });
    return this;
  }

  barChart(data, options = {}) { return this.chart('bar', data, options); }
  lineChart(data, options = {}) { return this.chart('line', data, options); }
  pieChart(data, options = {}) { return this.chart('pie', data, options); }

  // Layout methods
  columns(count, content) {
    this.currentPage.addElement({ type: 'columns', count, content });
    return this;
  }

  spacer(height = 20) {
    this.currentPage.addElement({ type: 'spacer', height });
    return this;
  }

  divider(options = {}) {
    this.currentPage.addElement({ type: 'divider', ...options });
    return this;
  }

  pageBreak() {
    return this.addPage();
  }

  // Header/Footer
  header(content, options = {}) {
    this.currentPage.header = { content, ...options };
    return this;
  }

  footer(content, options = {}) {
    this.currentPage.footer = { content, ...options };
    return this;
  }

  // Watermark
  watermark(text, options = {}) {
    this.currentPage.watermark = { text, ...options };
    return this;
  }

  // Generate output
  toBuffer() {
    const content = this.render();
    return Buffer.from(content, 'utf-8');
  }

  toBase64() {
    return this.toBuffer().toString('base64');
  }

  render() {
    // Generate PDF-like structure (simplified representation)
    const output = {
      version: '1.7',
      metadata: this.metadata,
      pages: this.pages.map(p => p.render()),
      fonts: Array.from(this.fonts.entries()),
      images: Array.from(this.images.entries())
    };
    return JSON.stringify(output, null, 2);
  }

  // Generate HTML preview
  toHTML() {
    const pages = this.pages.map(page => page.toHTML()).join('\n');
    return `<!DOCTYPE html>
<html><head>
<title>${this.metadata.title}</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: system-ui, sans-serif; background: #888; padding: 20px; }
  .page { background: white; width: 210mm; min-height: 297mm; margin: 20px auto; padding: 20mm; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
  h1 { font-size: 24pt; margin-bottom: 12pt; }
  h2 { font-size: 18pt; margin-bottom: 10pt; }
  h3 { font-size: 14pt; margin-bottom: 8pt; }
  p { font-size: 12pt; line-height: 1.5; margin-bottom: 12pt; }
  table { width: 100%; border-collapse: collapse; margin: 16pt 0; }
  th, td { border: 1px solid #ddd; padding: 8pt; text-align: left; }
  th { background: #f5f5f5; font-weight: 600; }
  .spacer { height: 20pt; }
  .divider { border-top: 1px solid #ddd; margin: 16pt 0; }
  ul, ol { margin: 12pt 0; padding-left: 24pt; }
  li { margin-bottom: 4pt; }
  .chart { background: #f9f9f9; border: 1px solid #eee; padding: 20pt; text-align: center; margin: 16pt 0; }
</style>
</head><body>${pages}</body></html>`;
  }

  getPageCount() { return this.pages.length; }
}

// ============================================
// PDF PAGE
// ============================================

class PDFPage {
  constructor(options = {}) {
    this.pageNumber = options.pageNumber || 1;
    this.size = options.size || 'A4';
    this.orientation = options.orientation || 'portrait';
    this.margins = options.margins || { top: 72, right: 72, bottom: 72, left: 72 };
    this.elements = [];
    this.header = null;
    this.footer = null;
    this.watermark = null;
  }

  addElement(element) {
    this.elements.push(element);
  }

  render() {
    return {
      pageNumber: this.pageNumber,
      size: this.size,
      orientation: this.orientation,
      margins: this.margins,
      elements: this.elements,
      header: this.header,
      footer: this.footer,
      watermark: this.watermark
    };
  }

  toHTML() {
    const elements = this.elements.map(el => this.elementToHTML(el)).join('\n');
    return `<div class="page" data-page="${this.pageNumber}">${elements}</div>`;
  }

  elementToHTML(el) {
    switch (el.type) {
      case 'text':
        const tag = el.fontSize >= 18 ? 'h1' : el.fontSize >= 14 ? 'h2' : 'p';
        return `<${tag}>${el.content}</${tag}>`;

      case 'list':
        const listTag = el.ordered ? 'ol' : 'ul';
        const items = el.items.map(i => `<li>${i}</li>`).join('');
        return `<${listTag}>${items}</${listTag}>`;

      case 'table':
        const headers = el.data.headers?.map(h => `<th>${h}</th>`).join('') || '';
        const rows = el.data.rows?.map(row =>
          `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`
        ).join('') || '';
        return `<table>${headers ? `<thead><tr>${headers}</tr></thead>` : ''}<tbody>${rows}</tbody></table>`;

      case 'spacer':
        return `<div class="spacer" style="height:${el.height}pt"></div>`;

      case 'divider':
        return `<div class="divider"></div>`;

      case 'chart':
        return `<div class="chart">[${el.chartType.toUpperCase()} CHART]</div>`;

      case 'image':
        return `<img src="${el.src}" style="max-width:100%;${el.width ? `width:${el.width}px;` : ''}" />`;

      default:
        return '';
    }
  }
}

// ============================================
// TEMPLATE ENGINE
// ============================================

class PDFTemplate {
  constructor(name, options = {}) {
    this.name = name;
    this.options = options;
    this.sections = [];
  }

  addSection(name, renderer) {
    this.sections.push({ name, renderer });
    return this;
  }

  async render(data) {
    const doc = new PDFDocument(this.options);

    for (const section of this.sections) {
      await section.renderer(doc, data);
    }

    return doc;
  }
}

// ============================================
// INVOICE TEMPLATE
// ============================================

class InvoiceTemplate extends PDFTemplate {
  constructor(options = {}) {
    super('invoice', options);

    this.addSection('header', (doc, data) => {
      doc.heading(data.company?.name || 'INVOICE', 1);
      doc.text(`Invoice #: ${data.invoiceNumber}`, { fontSize: 12 });
      doc.text(`Date: ${data.date}`, { fontSize: 12 });
      doc.text(`Due Date: ${data.dueDate}`, { fontSize: 12 });
      doc.spacer(20);
    });

    this.addSection('addresses', (doc, data) => {
      doc.heading('Bill To:', 3);
      doc.text(data.customer?.name || '');
      doc.text(data.customer?.address || '');
      doc.text(data.customer?.email || '');
      doc.spacer(20);
    });

    this.addSection('items', (doc, data) => {
      const tableData = {
        headers: ['Description', 'Qty', 'Price', 'Total'],
        rows: (data.items || []).map(item => [
          item.description,
          item.quantity.toString(),
          `$${(item.price / 100).toFixed(2)}`,
          `$${(item.quantity * item.price / 100).toFixed(2)}`
        ])
      };
      doc.table(tableData);
      doc.spacer(10);
    });

    this.addSection('totals', (doc, data) => {
      doc.text(`Subtotal: $${((data.subtotal || 0) / 100).toFixed(2)}`, { align: 'right' });
      if (data.tax) doc.text(`Tax: $${(data.tax / 100).toFixed(2)}`, { align: 'right' });
      doc.text(`Total: $${((data.total || 0) / 100).toFixed(2)}`, { fontSize: 16, fontWeight: 'bold', align: 'right' });
    });

    this.addSection('footer', (doc, data) => {
      doc.spacer(40);
      doc.divider();
      if (data.notes) doc.text(`Notes: ${data.notes}`, { fontSize: 10, color: '#666' });
      if (data.terms) doc.text(`Terms: ${data.terms}`, { fontSize: 10, color: '#666' });
    });
  }
}

// ============================================
// REPORT TEMPLATE
// ============================================

class ReportTemplate extends PDFTemplate {
  constructor(options = {}) {
    super('report', options);

    this.addSection('cover', (doc, data) => {
      doc.spacer(100);
      doc.heading(data.title || 'Report', 1);
      doc.text(data.subtitle || '', { fontSize: 16, color: '#666' });
      doc.spacer(40);
      doc.text(`Author: ${data.author || 'NOIZYLAB'}`);
      doc.text(`Date: ${data.date || new Date().toLocaleDateString()}`);
      doc.pageBreak();
    });

    this.addSection('toc', (doc, data) => {
      if (data.sections?.length) {
        doc.heading('Table of Contents', 2);
        doc.list(data.sections.map((s, i) => `${i + 1}. ${s.title}`));
        doc.pageBreak();
      }
    });

    this.addSection('content', (doc, data) => {
      (data.sections || []).forEach((section, index) => {
        doc.heading(`${index + 1}. ${section.title}`, 2);
        if (section.content) doc.paragraph(section.content);
        if (section.chart) doc.chart(section.chart.type, section.chart.data);
        if (section.table) doc.table(section.table);
        doc.spacer(20);
      });
    });

    this.addSection('appendix', (doc, data) => {
      if (data.appendix) {
        doc.pageBreak();
        doc.heading('Appendix', 2);
        doc.paragraph(data.appendix);
      }
    });
  }
}

// ============================================
// CERTIFICATE TEMPLATE
// ============================================

class CertificateTemplate extends PDFTemplate {
  constructor(options = {}) {
    super('certificate', { orientation: 'landscape', ...options });

    this.addSection('content', (doc, data) => {
      doc.spacer(60);
      doc.heading('Certificate of Completion', 1);
      doc.spacer(30);
      doc.text('This is to certify that', { fontSize: 14, align: 'center' });
      doc.spacer(20);
      doc.text(data.recipientName || 'Recipient Name', { fontSize: 28, fontWeight: 'bold', align: 'center' });
      doc.spacer(20);
      doc.text('has successfully completed', { fontSize: 14, align: 'center' });
      doc.spacer(10);
      doc.text(data.courseName || 'Course Name', { fontSize: 20, align: 'center' });
      doc.spacer(40);
      doc.text(`Date: ${data.date || new Date().toLocaleDateString()}`, { align: 'center' });
      doc.spacer(20);
      doc.text(data.issuerName || 'NOIZYLAB', { align: 'center', fontStyle: 'italic' });
    });
  }
}

// ============================================
// PDF BUILDER (FLUENT API)
// ============================================

class PDFBuilder {
  constructor(options = {}) {
    this.doc = new PDFDocument(options);
  }

  title(text) { this.doc.heading(text, 1); return this; }
  subtitle(text) { this.doc.heading(text, 2); return this; }
  h1(text) { this.doc.heading(text, 1); return this; }
  h2(text) { this.doc.heading(text, 2); return this; }
  h3(text) { this.doc.heading(text, 3); return this; }
  p(text, opts) { this.doc.paragraph(text, opts); return this; }
  text(text, opts) { this.doc.text(text, opts); return this; }
  ul(items) { this.doc.list(items, { ordered: false }); return this; }
  ol(items) { this.doc.list(items, { ordered: true }); return this; }
  table(data, opts) { this.doc.table(data, opts); return this; }
  image(src, opts) { this.doc.image(src, opts); return this; }
  chart(type, data, opts) { this.doc.chart(type, data, opts); return this; }
  space(h) { this.doc.spacer(h); return this; }
  hr() { this.doc.divider(); return this; }
  page() { this.doc.addPage(); return this; }
  header(content) { this.doc.header(content); return this; }
  footer(content) { this.doc.footer(content); return this; }

  build() { return this.doc; }
  toBuffer() { return this.doc.toBuffer(); }
  toHTML() { return this.doc.toHTML(); }
}

// ============================================
// EXPORTS
// ============================================

module.exports = {
  PDFDocument,
  PDFPage,
  PDFTemplate,
  InvoiceTemplate,
  ReportTemplate,
  CertificateTemplate,
  PDFBuilder,

  createDocument: (options) => new PDFDocument(options),
  createBuilder: (options) => new PDFBuilder(options),
  createInvoice: (data) => new InvoiceTemplate().render(data),
  createReport: (data) => new ReportTemplate().render(data),
  createCertificate: (data) => new CertificateTemplate().render(data)
};
