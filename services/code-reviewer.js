// ═══════════════════════════════════════════════════════════════════════════════
// CODE REVIEWER - AI-POWERED CODE ANALYSIS & REVIEW
// Comprehensive code review with multiple analysis aspects
// ═══════════════════════════════════════════════════════════════════════════════

export class CodeReviewer {
  constructor(aiRouter) {
    this.ai = aiRouter;
    this.reviewHistory = [];
  }

  // ─── COMPREHENSIVE REVIEW ──────────────────────────────────────────────────

  async review(code, options = {}) {
    const {
      language = "javascript",
      aspects = ["quality", "security", "performance", "style", "bugs"],
      severity = "all", // all, critical, major, minor
      context = null
    } = options;

    const reviews = await Promise.all(
      aspects.map(aspect => this.reviewAspect(code, aspect, language, context))
    );

    // Combine all reviews
    const combined = this.combineReviews(reviews, aspects);

    // Calculate overall score
    const overallScore = Math.round(
      reviews.reduce((sum, r) => sum + (r.score || 0), 0) / reviews.length
    );

    // Filter by severity
    let allIssues = combined.issues;
    if (severity !== "all") {
      const severityOrder = { critical: 0, major: 1, minor: 2 };
      const threshold = severityOrder[severity];
      allIssues = allIssues.filter(i => severityOrder[i.severity] <= threshold);
    }

    const result = {
      id: `review-${Date.now()}`,
      timestamp: new Date().toISOString(),
      language,
      aspects,
      overallScore,
      grade: this.scoreToGrade(overallScore),
      summary: combined.summary,
      issues: allIssues,
      suggestions: combined.suggestions,
      metrics: combined.metrics,
      aspectScores: Object.fromEntries(
        reviews.map((r, i) => [aspects[i], r.score])
      )
    };

    this.reviewHistory.push(result);
    return result;
  }

  async reviewAspect(code, aspect, language, context) {
    const prompts = {
      quality: `Analyze code quality:
- Code organization and structure
- Naming conventions
- Function/method complexity
- Code duplication
- Readability`,

      security: `Security audit:
- Input validation
- SQL injection vulnerabilities
- XSS vulnerabilities
- Authentication issues
- Sensitive data exposure
- Insecure dependencies`,

      performance: `Performance analysis:
- Time complexity
- Memory usage
- Unnecessary computations
- N+1 queries
- Resource leaks
- Optimization opportunities`,

      style: `Style review:
- Consistent formatting
- Best practices for ${language}
- Modern syntax usage
- Documentation completeness
- Error handling patterns`,

      bugs: `Bug detection:
- Logic errors
- Edge cases
- Null/undefined handling
- Type errors
- Race conditions
- Off-by-one errors`
    };

    const prompt = `Review this ${language} code for ${aspect}:

${prompts[aspect]}

CODE:
\`\`\`${language}
${code.substring(0, 4000)}
\`\`\`

${context ? `CONTEXT: ${context}` : ""}

Return JSON:
{
  "score": 0-100,
  "issues": [
    { "severity": "critical|major|minor", "line": number, "message": "", "fix": "" }
  ],
  "suggestions": ["suggestion1", "suggestion2"],
  "summary": "brief summary"
}`;

    const result = await this.ai.run(prompt, { format: "json" });
    return result.response || { score: 50, issues: [], suggestions: [], summary: "Analysis incomplete" };
  }

  combineReviews(reviews, aspects) {
    const allIssues = [];
    const allSuggestions = [];
    const summaries = [];

    reviews.forEach((review, i) => {
      if (review.issues) {
        review.issues.forEach(issue => {
          allIssues.push({ ...issue, aspect: aspects[i] });
        });
      }
      if (review.suggestions) {
        allSuggestions.push(...review.suggestions);
      }
      if (review.summary) {
        summaries.push(`${aspects[i]}: ${review.summary}`);
      }
    });

    // Sort issues by severity
    const severityOrder = { critical: 0, major: 1, minor: 2 };
    allIssues.sort((a, b) => severityOrder[a.severity] - severityOrder[b.severity]);

    return {
      issues: allIssues,
      suggestions: [...new Set(allSuggestions)], // Deduplicate
      summary: summaries.join("\n"),
      metrics: {
        totalIssues: allIssues.length,
        critical: allIssues.filter(i => i.severity === "critical").length,
        major: allIssues.filter(i => i.severity === "major").length,
        minor: allIssues.filter(i => i.severity === "minor").length
      }
    };
  }

  scoreToGrade(score) {
    if (score >= 90) return "A";
    if (score >= 80) return "B";
    if (score >= 70) return "C";
    if (score >= 60) return "D";
    return "F";
  }

  // ─── DIFF REVIEW ───────────────────────────────────────────────────────────

  async reviewDiff(diff, options = {}) {
    const { baseBranch = "main", context = null } = options;

    const prompt = `Review this code diff (changes being merged to ${baseBranch}):

${diff.substring(0, 5000)}

${context ? `PR Context: ${context}` : ""}

Analyze:
1. Code quality of changes
2. Potential bugs introduced
3. Security implications
4. Breaking changes
5. Test coverage needs

Return JSON:
{
  "verdict": "approve|request_changes|comment",
  "confidence": 0-100,
  "summary": "brief summary",
  "concerns": [
    { "severity": "critical|major|minor", "file": "", "line": number, "message": "" }
  ],
  "suggestions": ["suggestion1"],
  "testsNeeded": ["test1"],
  "breakingChanges": true/false
}`;

    const result = await this.ai.run(prompt, { format: "json" });
    return result.response;
  }

  // ─── SPECIFIC CHECKS ───────────────────────────────────────────────────────

  async checkSecurity(code, language = "javascript") {
    return this.reviewAspect(code, "security", language, null);
  }

  async checkPerformance(code, language = "javascript") {
    return this.reviewAspect(code, "performance", language, null);
  }

  async suggestRefactoring(code, language = "javascript") {
    const prompt = `Suggest refactoring improvements for this ${language} code:

\`\`\`${language}
${code.substring(0, 4000)}
\`\`\`

Focus on:
- Extracting functions
- Reducing complexity
- Improving testability
- Better abstractions
- Design patterns

Return JSON:
{
  "refactorings": [
    {
      "type": "extract_function|simplify|abstract|pattern",
      "description": "",
      "before": "code snippet",
      "after": "refactored code",
      "impact": "high|medium|low"
    }
  ],
  "complexityReduction": "percentage estimate"
}`;

    const result = await this.ai.run(prompt, { format: "json" });
    return result.response;
  }

  // ─── FIX GENERATION ────────────────────────────────────────────────────────

  async generateFix(code, issue, language = "javascript") {
    const prompt = `Fix this issue in the ${language} code:

ISSUE: ${issue.message}
${issue.line ? `LINE: ${issue.line}` : ""}
${issue.severity ? `SEVERITY: ${issue.severity}` : ""}

CODE:
\`\`\`${language}
${code.substring(0, 3000)}
\`\`\`

Return JSON:
{
  "fixedCode": "the complete fixed code",
  "explanation": "what was changed and why",
  "linesChanged": [line numbers],
  "testSuggestion": "how to test the fix"
}`;

    const result = await this.ai.run(prompt, { format: "json", model: "codellama" });
    return result.response;
  }

  // ─── COMPARISON ────────────────────────────────────────────────────────────

  async compareImplementations(code1, code2, language = "javascript") {
    const prompt = `Compare these two ${language} implementations:

IMPLEMENTATION 1:
\`\`\`${language}
${code1.substring(0, 2000)}
\`\`\`

IMPLEMENTATION 2:
\`\`\`${language}
${code2.substring(0, 2000)}
\`\`\`

Compare:
- Readability
- Performance
- Maintainability
- Edge case handling
- Best practices

Return JSON:
{
  "winner": 1 or 2,
  "scores": {
    "impl1": { "readability": 0-10, "performance": 0-10, "maintainability": 0-10 },
    "impl2": { "readability": 0-10, "performance": 0-10, "maintainability": 0-10 }
  },
  "analysis": "detailed comparison",
  "recommendation": "which to use and why"
}`;

    const result = await this.ai.run(prompt, { format: "json" });
    return result.response;
  }

  // ─── HISTORY ───────────────────────────────────────────────────────────────

  getHistory(limit = 20) {
    return this.reviewHistory.slice(-limit);
  }

  getStats() {
    if (this.reviewHistory.length === 0) {
      return { reviews: 0 };
    }

    const scores = this.reviewHistory.map(r => r.overallScore);
    const avgScore = scores.reduce((a, b) => a + b, 0) / scores.length;

    const totalIssues = this.reviewHistory.reduce(
      (sum, r) => sum + (r.metrics?.totalIssues || 0),
      0
    );

    return {
      reviews: this.reviewHistory.length,
      averageScore: Math.round(avgScore),
      averageGrade: this.scoreToGrade(avgScore),
      totalIssuesFound: totalIssues,
      criticalIssues: this.reviewHistory.reduce(
        (sum, r) => sum + (r.metrics?.critical || 0),
        0
      )
    };
  }
}

export default CodeReviewer;
