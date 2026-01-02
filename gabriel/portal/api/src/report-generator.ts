/**
 * PDF Report Generation for GABRIEL Scans
 * 
 * Generates professional PDF reports for board inspections
 * with detailed issue analysis, repair guidance, and visual
 * annotations.
 */

export interface ReportOptions {
  includeImages: boolean;
  includeRepairGuide: boolean;
  includeHistory: boolean;
  branding: 'gabriel' | 'whitelabel' | 'none';
  language: string;
}

export interface ScanData {
  scanId: string;
  boardType: string;
  boardName: string;
  timestamp: string;
  confidence: number;
  issues: Issue[];
  imageUrl?: string;
  annotations?: Annotation[];
  metadata?: Record<string, unknown>;
}

export interface Issue {
  id: string;
  component: string;
  type: string;
  severity: 'critical' | 'warning' | 'info';
  description: string;
  confidence: number;
  location: { x: number; y: number; width: number; height: number };
  repairGuide?: string;
  estimatedTime?: number;
  difficulty?: 'easy' | 'medium' | 'hard' | 'expert';
  parts?: string[];
}

export interface Annotation {
  x: number;
  y: number;
  text: string;
  type: 'arrow' | 'circle' | 'box' | 'text';
}

// Color scheme
const COLORS = {
  primary: '#f59e0b',
  secondary: '#3b82f6',
  critical: '#ef4444',
  warning: '#f59e0b',
  info: '#3b82f6',
  success: '#22c55e',
  dark: '#0f172a',
  light: '#f8fafc',
  gray: '#64748b',
};

/**
 * Generate a complete PDF report
 */
export async function generatePDFReport(
  scan: ScanData,
  options: ReportOptions
): Promise<ArrayBuffer> {
  // This would use a PDF library like jsPDF or PDFKit
  // For now, we generate the report structure
  
  const sections: string[] = [];
  
  // Header
  sections.push(generateHeader(scan, options));
  
  // Executive Summary
  sections.push(generateExecutiveSummary(scan));
  
  // Issue Details
  sections.push(generateIssueSection(scan.issues));
  
  // Images with annotations
  if (options.includeImages && scan.imageUrl) {
    sections.push(generateImageSection(scan));
  }
  
  // Repair Guide
  if (options.includeRepairGuide) {
    sections.push(generateRepairSection(scan.issues));
  }
  
  // Parts List
  sections.push(generatePartsSection(scan.issues));
  
  // Footer
  sections.push(generateFooter(options));
  
  // Convert to PDF buffer (placeholder - would use PDF library)
  const html = sections.join('\n');
  return new TextEncoder().encode(html).buffer;
}

function generateHeader(scan: ScanData, options: ReportOptions): string {
  const logo = options.branding === 'gabriel' 
    ? '🔬 GABRIEL Board Inspection Report'
    : 'Board Inspection Report';
    
  return `
    <header>
      <h1>${logo}</h1>
      <div class="meta">
        <p><strong>Scan ID:</strong> ${scan.scanId}</p>
        <p><strong>Board:</strong> ${scan.boardName} (${scan.boardType})</p>
        <p><strong>Date:</strong> ${new Date(scan.timestamp).toLocaleString()}</p>
        <p><strong>Confidence:</strong> ${(scan.confidence * 100).toFixed(1)}%</p>
      </div>
    </header>
  `;
}

function generateExecutiveSummary(scan: ScanData): string {
  const critical = scan.issues.filter(i => i.severity === 'critical').length;
  const warning = scan.issues.filter(i => i.severity === 'warning').length;
  const info = scan.issues.filter(i => i.severity === 'info').length;
  
  const totalTime = scan.issues.reduce((sum, i) => sum + (i.estimatedTime || 0), 0);
  
  let verdict = 'PASS';
  let verdictColor = COLORS.success;
  
  if (critical > 0) {
    verdict = 'NEEDS REPAIR';
    verdictColor = COLORS.critical;
  } else if (warning > 0) {
    verdict = 'ATTENTION NEEDED';
    verdictColor = COLORS.warning;
  }
  
  return `
    <section class="summary">
      <h2>Executive Summary</h2>
      
      <div class="verdict" style="color: ${verdictColor}">
        ${verdict}
      </div>
      
      <div class="stats">
        <div class="stat critical">
          <span class="count">${critical}</span>
          <span class="label">Critical Issues</span>
        </div>
        <div class="stat warning">
          <span class="count">${warning}</span>
          <span class="label">Warnings</span>
        </div>
        <div class="stat info">
          <span class="count">${info}</span>
          <span class="label">Info</span>
        </div>
      </div>
      
      <p class="time-estimate">
        <strong>Estimated Repair Time:</strong> ${formatTime(totalTime)}
      </p>
    </section>
  `;
}

function generateIssueSection(issues: Issue[]): string {
  const sortedIssues = [...issues].sort((a, b) => {
    const severityOrder = { critical: 0, warning: 1, info: 2 };
    return severityOrder[a.severity] - severityOrder[b.severity];
  });
  
  const issueRows = sortedIssues.map((issue, index) => `
    <tr class="issue-row ${issue.severity}">
      <td>${index + 1}</td>
      <td>
        <span class="severity-badge ${issue.severity}">
          ${issue.severity.toUpperCase()}
        </span>
      </td>
      <td>${issue.component}</td>
      <td>${formatIssueType(issue.type)}</td>
      <td>${issue.description}</td>
      <td>${(issue.confidence * 100).toFixed(0)}%</td>
      <td>${issue.difficulty || '-'}</td>
    </tr>
  `).join('');
  
  return `
    <section class="issues">
      <h2>Issue Details</h2>
      
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Severity</th>
            <th>Component</th>
            <th>Issue Type</th>
            <th>Description</th>
            <th>Confidence</th>
            <th>Difficulty</th>
          </tr>
        </thead>
        <tbody>
          ${issueRows}
        </tbody>
      </table>
    </section>
  `;
}

function generateImageSection(scan: ScanData): string {
  // Generate SVG annotations overlay
  const annotations = scan.annotations?.map(ann => {
    switch (ann.type) {
      case 'circle':
        return `<circle cx="${ann.x}" cy="${ann.y}" r="20" class="annotation-circle"/>`;
      case 'arrow':
        return `<path d="M${ann.x},${ann.y} L${ann.x + 30},${ann.y}" class="annotation-arrow"/>`;
      case 'box':
        return `<rect x="${ann.x - 15}" y="${ann.y - 15}" width="30" height="30" class="annotation-box"/>`;
      default:
        return `<text x="${ann.x}" y="${ann.y}" class="annotation-text">${ann.text}</text>`;
    }
  }).join('') || '';
  
  return `
    <section class="images">
      <h2>Visual Analysis</h2>
      
      <div class="image-container">
        <img src="${scan.imageUrl}" alt="Board scan" />
        <svg class="annotations">
          ${annotations}
          ${scan.issues.map((issue, i) => `
            <circle 
              cx="${issue.location.x + issue.location.width / 2}" 
              cy="${issue.location.y + issue.location.height / 2}" 
              r="15" 
              class="issue-marker ${issue.severity}"
            />
            <text 
              x="${issue.location.x + issue.location.width / 2}" 
              y="${issue.location.y + issue.location.height / 2 + 5}" 
              class="issue-number"
            >${i + 1}</text>
          `).join('')}
        </svg>
      </div>
      
      <div class="legend">
        <span class="legend-item critical">● Critical</span>
        <span class="legend-item warning">● Warning</span>
        <span class="legend-item info">● Info</span>
      </div>
    </section>
  `;
}

function generateRepairSection(issues: Issue[]): string {
  const repairGuides = issues
    .filter(i => i.repairGuide)
    .map((issue, index) => `
      <div class="repair-guide">
        <h4>${index + 1}. ${issue.component} - ${formatIssueType(issue.type)}</h4>
        
        <div class="repair-meta">
          <span class="difficulty ${issue.difficulty}">
            Difficulty: ${issue.difficulty || 'Unknown'}
          </span>
          <span class="time">
            Est. Time: ${formatTime(issue.estimatedTime || 0)}
          </span>
        </div>
        
        <div class="instructions">
          ${issue.repairGuide}
        </div>
        
        ${issue.parts?.length ? `
          <div class="parts-needed">
            <strong>Parts Needed:</strong>
            <ul>
              ${issue.parts.map(p => `<li>${p}</li>`).join('')}
            </ul>
          </div>
        ` : ''}
      </div>
    `).join('');
  
  return `
    <section class="repair">
      <h2>Repair Guide</h2>
      ${repairGuides || '<p>No specific repair guidance available.</p>'}
    </section>
  `;
}

function generatePartsSection(issues: Issue[]): string {
  // Aggregate all parts needed
  const partsMap = new Map<string, number>();
  
  for (const issue of issues) {
    for (const part of issue.parts || []) {
      partsMap.set(part, (partsMap.get(part) || 0) + 1);
    }
  }
  
  if (partsMap.size === 0) {
    return '';
  }
  
  const partsList = Array.from(partsMap.entries())
    .map(([part, qty]) => `
      <tr>
        <td>${part}</td>
        <td>${qty}</td>
        <td>-</td>
        <td>-</td>
      </tr>
    `).join('');
  
  return `
    <section class="parts">
      <h2>Parts List</h2>
      
      <table>
        <thead>
          <tr>
            <th>Part</th>
            <th>Quantity</th>
            <th>Part Number</th>
            <th>Supplier</th>
          </tr>
        </thead>
        <tbody>
          ${partsList}
        </tbody>
      </table>
      
      <p class="note">
        Note: Part numbers and suppliers may vary. Verify compatibility before ordering.
      </p>
    </section>
  `;
}

function generateFooter(options: ReportOptions): string {
  const branding = options.branding === 'gabriel' 
    ? `
      <p>Generated by GABRIEL - AI Board Inspection</p>
      <p>gabriel.noizylab.com</p>
    `
    : `<p>Generated ${new Date().toISOString()}</p>`;
  
  return `
    <footer>
      ${branding}
      <p class="disclaimer">
        This report is generated by AI analysis and should be verified by a qualified technician.
        GABRIEL provides guidance only and is not responsible for repair outcomes.
      </p>
    </footer>
  `;
}

// Utility functions
function formatTime(minutes: number): string {
  if (minutes < 60) {
    return `${minutes} min`;
  }
  const hours = Math.floor(minutes / 60);
  const mins = minutes % 60;
  return `${hours}h ${mins}m`;
}

function formatIssueType(type: string): string {
  return type
    .split('_')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

// ============================================================================
// REPORT STYLES (CSS)
// ============================================================================

export const REPORT_STYLES = `
  @page {
    size: A4;
    margin: 20mm;
  }
  
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 12px;
    line-height: 1.5;
    color: #1e293b;
  }
  
  header {
    border-bottom: 2px solid ${COLORS.primary};
    padding-bottom: 20px;
    margin-bottom: 30px;
  }
  
  h1 {
    color: ${COLORS.primary};
    font-size: 24px;
    margin-bottom: 10px;
  }
  
  h2 {
    color: ${COLORS.dark};
    font-size: 18px;
    margin: 30px 0 15px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 5px;
  }
  
  .verdict {
    font-size: 32px;
    font-weight: bold;
    text-align: center;
    padding: 20px;
    background: #f8fafc;
    border-radius: 8px;
    margin: 20px 0;
  }
  
  .stats {
    display: flex;
    justify-content: space-around;
    margin: 20px 0;
  }
  
  .stat {
    text-align: center;
    padding: 15px 25px;
    border-radius: 8px;
  }
  
  .stat.critical { background: #fef2f2; color: ${COLORS.critical}; }
  .stat.warning { background: #fffbeb; color: ${COLORS.warning}; }
  .stat.info { background: #eff6ff; color: ${COLORS.info}; }
  
  .stat .count {
    font-size: 36px;
    font-weight: bold;
    display: block;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
  }
  
  th, td {
    padding: 10px 12px;
    text-align: left;
    border-bottom: 1px solid #e2e8f0;
  }
  
  th {
    background: #f8fafc;
    font-weight: 600;
  }
  
  .severity-badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: bold;
  }
  
  .severity-badge.critical { background: #fef2f2; color: ${COLORS.critical}; }
  .severity-badge.warning { background: #fffbeb; color: ${COLORS.warning}; }
  .severity-badge.info { background: #eff6ff; color: ${COLORS.info}; }
  
  .image-container {
    position: relative;
    max-width: 100%;
    margin: 20px 0;
  }
  
  .image-container img {
    max-width: 100%;
    border-radius: 8px;
  }
  
  .annotations {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
  }
  
  .issue-marker {
    stroke-width: 2;
    fill: none;
  }
  
  .issue-marker.critical { stroke: ${COLORS.critical}; }
  .issue-marker.warning { stroke: ${COLORS.warning}; }
  .issue-marker.info { stroke: ${COLORS.info}; }
  
  .issue-number {
    font-size: 12px;
    font-weight: bold;
    fill: white;
    text-anchor: middle;
  }
  
  .repair-guide {
    background: #f8fafc;
    padding: 15px;
    border-radius: 8px;
    margin: 15px 0;
  }
  
  .repair-guide h4 {
    margin: 0 0 10px;
    color: ${COLORS.dark};
  }
  
  .repair-meta {
    display: flex;
    gap: 20px;
    margin-bottom: 10px;
    font-size: 11px;
    color: ${COLORS.gray};
  }
  
  footer {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #e2e8f0;
    text-align: center;
    color: ${COLORS.gray};
    font-size: 10px;
  }
  
  .disclaimer {
    font-style: italic;
    margin-top: 10px;
  }
  
  @media print {
    .no-print { display: none; }
    
    section {
      page-break-inside: avoid;
    }
  }
`;

// ============================================================================
// EXPORT FORMATS
// ============================================================================

export async function generateReport(
  scan: ScanData,
  format: 'pdf' | 'html' | 'json' | 'csv',
  options: ReportOptions
): Promise<{ data: ArrayBuffer | string; mimeType: string; filename: string }> {
  switch (format) {
    case 'pdf':
      return {
        data: await generatePDFReport(scan, options),
        mimeType: 'application/pdf',
        filename: `gabriel-report-${scan.scanId}.pdf`
      };
      
    case 'html':
      const html = await generateHTMLReport(scan, options);
      return {
        data: html,
        mimeType: 'text/html',
        filename: `gabriel-report-${scan.scanId}.html`
      };
      
    case 'json':
      return {
        data: JSON.stringify(scan, null, 2),
        mimeType: 'application/json',
        filename: `gabriel-report-${scan.scanId}.json`
      };
      
    case 'csv':
      return {
        data: generateCSV(scan),
        mimeType: 'text/csv',
        filename: `gabriel-report-${scan.scanId}.csv`
      };
      
    default:
      throw new Error(`Unsupported format: ${format}`);
  }
}

async function generateHTMLReport(scan: ScanData, options: ReportOptions): Promise<string> {
  const sections: string[] = [
    generateHeader(scan, options),
    generateExecutiveSummary(scan),
    generateIssueSection(scan.issues),
  ];
  
  if (options.includeImages && scan.imageUrl) {
    sections.push(generateImageSection(scan));
  }
  
  if (options.includeRepairGuide) {
    sections.push(generateRepairSection(scan.issues));
  }
  
  sections.push(generatePartsSection(scan.issues));
  sections.push(generateFooter(options));
  
  return `
    <!DOCTYPE html>
    <html lang="${options.language}">
    <head>
      <meta charset="UTF-8">
      <title>GABRIEL Report - ${scan.scanId}</title>
      <style>${REPORT_STYLES}</style>
    </head>
    <body>
      ${sections.join('\n')}
    </body>
    </html>
  `;
}

function generateCSV(scan: ScanData): string {
  const headers = ['ID', 'Component', 'Type', 'Severity', 'Description', 'Confidence', 'Location'];
  const rows = scan.issues.map(issue => [
    issue.id,
    issue.component,
    issue.type,
    issue.severity,
    `"${issue.description.replace(/"/g, '""')}"`,
    (issue.confidence * 100).toFixed(1),
    `"${issue.location.x},${issue.location.y}"`,
  ]);
  
  return [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
}
