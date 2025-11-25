// ═══════════════════════════════════════════════════════════════════════════════
// DOCUMENTATION GENERATOR - AUTO-DOCS FOR EVERYTHING
// Generate README, API docs, JSDoc, and more
// ═══════════════════════════════════════════════════════════════════════════════

import fs from "fs";
import path from "path";

export class DocGenerator {
  constructor(aiRouter) {
    this.ai = aiRouter;
  }

  // ─── README GENERATION ─────────────────────────────────────────────────────

  async generateReadme(projectPath, options = {}) {
    const {
      style = "comprehensive", // minimal, standard, comprehensive
      badges = true,
      tableOfContents = true,
      includeApi = true
    } = options;

    // Analyze project
    const analysis = await this.analyzeProject(projectPath);

    const prompt = `Generate a ${style} README.md for this project:

Project Analysis:
${JSON.stringify(analysis, null, 2)}

Requirements:
- ${badges ? "Include badges (npm, license, build)" : "No badges"}
- ${tableOfContents ? "Include table of contents" : "No ToC"}
- ${includeApi ? "Include API documentation section" : "Skip API section"}
- Use proper markdown formatting
- Include code examples
- Add installation instructions
- Include usage examples
- Add contributing guidelines

Return only the markdown content.`;

    const result = await this.ai.run(prompt);
    return result.response;
  }

  async analyzeProject(projectPath) {
    const analysis = {
      name: "",
      description: "",
      type: "unknown",
      dependencies: [],
      scripts: [],
      files: [],
      entryPoint: null
    };

    // Check for package.json
    const pkgPath = path.join(projectPath, "package.json");
    if (fs.existsSync(pkgPath)) {
      const pkg = JSON.parse(fs.readFileSync(pkgPath, "utf8"));
      analysis.name = pkg.name;
      analysis.description = pkg.description;
      analysis.dependencies = Object.keys(pkg.dependencies || {});
      analysis.scripts = Object.keys(pkg.scripts || {});
      analysis.entryPoint = pkg.main || "index.js";
      analysis.type = "node";
    }

    // List important files
    if (fs.existsSync(projectPath)) {
      const files = fs.readdirSync(projectPath);
      analysis.files = files.filter(f =>
        !f.startsWith(".") &&
        !["node_modules", "dist", "build"].includes(f)
      );

      // Detect project type
      if (files.includes("wrangler.toml")) analysis.type = "cloudflare-worker";
      if (files.includes("Dockerfile")) analysis.type = "docker";
      if (files.includes("next.config.js")) analysis.type = "nextjs";
      if (files.includes("vite.config.js")) analysis.type = "vite";
    }

    return analysis;
  }

  // ─── API DOCUMENTATION ─────────────────────────────────────────────────────

  async generateApiDocs(code, options = {}) {
    const { format = "markdown", style = "openapi" } = options;

    const prompt = `Generate ${format} API documentation for this code:

\`\`\`javascript
${code.substring(0, 5000)}
\`\`\`

Requirements:
- Document all endpoints
- Include request/response examples
- Document parameters and types
- Add error codes
- ${style === "openapi" ? "Use OpenAPI 3.0 format" : "Use markdown format"}

Return the documentation.`;

    const result = await this.ai.run(prompt);
    return result.response;
  }

  // ─── JSDOC GENERATION ──────────────────────────────────────────────────────

  async generateJsDoc(code) {
    const prompt = `Add comprehensive JSDoc comments to this JavaScript code:

\`\`\`javascript
${code.substring(0, 4000)}
\`\`\`

Requirements:
- Add @param tags with types
- Add @returns tags
- Add @throws tags where appropriate
- Add @example for complex functions
- Add @description for classes and modules
- Preserve existing code exactly
- Only add JSDoc comments

Return the code with JSDoc comments added.`;

    const result = await this.ai.run(prompt, { model: "codellama" });
    return result.response;
  }

  // ─── TYPE DEFINITIONS ──────────────────────────────────────────────────────

  async generateTypeDefinitions(code) {
    const prompt = `Generate TypeScript type definitions (.d.ts) for this JavaScript code:

\`\`\`javascript
${code.substring(0, 4000)}
\`\`\`

Requirements:
- Export all public interfaces
- Use generics where appropriate
- Document with JSDoc comments
- Handle optional parameters
- Include default exports

Return only the .d.ts file content.`;

    const result = await this.ai.run(prompt, { model: "codellama" });
    return result.response;
  }

  // ─── CHANGELOG GENERATION ──────────────────────────────────────────────────

  async generateChangelog(commits, version) {
    const prompt = `Generate a CHANGELOG entry for version ${version} from these commits:

Commits:
${commits.map(c => `- ${c.message}`).join("\n")}

Format:
## [${version}] - YYYY-MM-DD

### Added
- New features

### Changed
- Changes to existing features

### Fixed
- Bug fixes

### Removed
- Removed features

Categorize each commit appropriately.`;

    const result = await this.ai.run(prompt);
    return result.response;
  }

  // ─── USAGE EXAMPLES ────────────────────────────────────────────────────────

  async generateExamples(code, count = 3) {
    const prompt = `Generate ${count} usage examples for this code:

\`\`\`javascript
${code.substring(0, 3000)}
\`\`\`

Requirements:
- Practical, real-world examples
- Include imports
- Show different use cases
- Add comments explaining each example
- Handle edge cases in at least one example

Format each example with a title and description.`;

    const result = await this.ai.run(prompt);
    return result.response;
  }

  // ─── INLINE COMMENTS ───────────────────────────────────────────────────────

  async addInlineComments(code, verbosity = "moderate") {
    const prompt = `Add inline comments to explain this code (${verbosity} verbosity):

\`\`\`javascript
${code.substring(0, 4000)}
\`\`\`

Verbosity levels:
- minimal: Only complex logic
- moderate: Key operations and logic
- detailed: Every significant line

Add comments that explain WHY, not just WHAT.
Return the code with comments added.`;

    const result = await this.ai.run(prompt, { model: "codellama" });
    return result.response;
  }

  // ─── ARCHITECTURE DOCS ─────────────────────────────────────────────────────

  async generateArchitectureDocs(files) {
    const prompt = `Generate architecture documentation for this codebase:

Files:
${files.map(f => `- ${f.path}: ${f.description || "No description"}`).join("\n")}

Generate:
1. System Overview
2. Component Diagram (ASCII)
3. Data Flow
4. Key Dependencies
5. Design Decisions

Use markdown format with diagrams where helpful.`;

    const result = await this.ai.run(prompt);
    return result.response;
  }

  // ─── CONTRIBUTING GUIDE ────────────────────────────────────────────────────

  async generateContributingGuide(projectInfo) {
    const prompt = `Generate a CONTRIBUTING.md file for this project:

Project: ${projectInfo.name}
Type: ${projectInfo.type}
Language: ${projectInfo.language || "JavaScript"}

Include:
1. Code of Conduct reference
2. How to report bugs
3. How to suggest features
4. Development setup
5. Pull request process
6. Coding standards
7. Testing requirements
8. Commit message format

Make it welcoming and clear.`;

    const result = await this.ai.run(prompt);
    return result.response;
  }

  // ─── FULL PROJECT DOCS ─────────────────────────────────────────────────────

  async generateFullDocs(projectPath, options = {}) {
    const docs = {};

    // Generate all documentation
    docs.readme = await this.generateReadme(projectPath, options);

    // Read main files for API docs
    const mainFile = path.join(projectPath, "index.js");
    if (fs.existsSync(mainFile)) {
      const code = fs.readFileSync(mainFile, "utf8");
      docs.api = await this.generateApiDocs(code);
      docs.examples = await this.generateExamples(code);
    }

    docs.contributing = await this.generateContributingGuide({
      name: options.name || path.basename(projectPath),
      type: options.type || "node"
    });

    return docs;
  }
}

export default DocGenerator;
