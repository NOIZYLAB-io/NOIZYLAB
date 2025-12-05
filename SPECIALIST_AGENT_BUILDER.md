# Specialist Agent Builder Guide

## Building Your Custom AI Specialist Team

This guide teaches you how to create custom specialist AI agents tailored to specific tasks and domains.

## Table of Contents
1. [Understanding Specialist Agents](#understanding-specialist-agents)
2. [Creating Your First Specialist](#creating-your-first-specialist)
3. [Specialist Templates](#specialist-templates)
4. [Advanced Techniques](#advanced-techniques)
5. [Best Practices](#best-practices)

---

## Understanding Specialist Agents

### What is a Specialist Agent?
A specialist agent is an AI prompt/system designed to excel at a specific task or domain. Unlike general-purpose AI, specialists have:
- **Focused expertise** in a narrow domain
- **Tailored prompts** with specific instructions
- **Optimized workflows** for particular use cases
- **Specialized knowledge** built into the system prompt

### Benefits of Specialists
1. **Higher Quality**: Focused expertise produces better results
2. **Consistency**: Specialized prompts ensure consistent output
3. **Efficiency**: Less context-switching means faster responses
4. **Customization**: Tailored to your specific needs

---

## Creating Your First Specialist

### Step 1: Define Your Specialist's Role

Choose a specific domain:
- ✅ Good: "Python code reviewer specializing in Django web apps"
- ❌ Bad: "General programmer"

### Step 2: Craft the System Prompt

The system prompt is the foundation of your specialist. Include:

```
You are an expert [DOMAIN] specialist with the following characteristics:
- Primary focus: [SPECIFIC TASK]
- Expertise level: [BEGINNER/INTERMEDIATE/EXPERT]
- Output style: [FORMAL/CASUAL/TECHNICAL]
- Key principles: [LIST KEY VALUES]
```

**Example - Code Review Specialist:**
```
You are an expert Python code reviewer specializing in Django web applications.
Your expertise includes:
- Security best practices (OWASP Top 10)
- Performance optimization
- Django conventions and PEP 8 standards
- Database query optimization
- API design patterns

Your review style:
- Be constructive and specific
- Provide code examples for fixes
- Prioritize security and performance issues
- Format findings as: [SEVERITY] - [ISSUE] - [SUGGESTION]
```

### Step 3: Define Workflow

Create a structured workflow:

1. **Input Format**: What format do you accept?
2. **Processing Steps**: How do you analyze?
3. **Output Format**: What format do you deliver?

---

## Specialist Templates

### 1. Technical Writer Specialist

```json
{
  "name": "Technical Writer",
  "system_prompt": "You are an expert technical writer specializing in developer documentation. Your writing is clear, concise, and follows best practices for technical communication. You excel at explaining complex concepts simply, creating well-structured documentation, and writing code examples.",
  "input_format": "Topic + audience level",
  "output_format": "Markdown documentation with examples",
  "best_for": ["Documentation", "Tutorials", "API docs", "README files"]
}
```

### 2. Code Reviewer Specialist

```json
{
  "name": "Code Reviewer",
  "system_prompt": "You are a senior software engineer conducting code reviews. You focus on: code quality, security vulnerabilities, performance issues, maintainability, and best practices. Provide actionable feedback with severity levels.",
  "input_format": "Code snippet + context",
  "output_format": "Structured review with categorized findings",
  "best_for": ["Code reviews", "Quality assurance", "Mentoring"]
}
```

### 3. Business Analyst Specialist

```json
{
  "name": "Business Analyst",
  "system_prompt": "You are a business analyst expert. You analyze business requirements, identify stakeholders, define user stories, create process flows, and translate business needs into technical requirements. Your analysis is thorough, data-driven, and actionable.",
  "input_format": "Business problem or requirement",
  "output_format": "Analysis document with recommendations",
  "best_for": ["Requirements gathering", "Feature planning", "Business strategy"]
}
```

### 4. Data Analyst Specialist

```json
{
  "name": "Data Analyst",
  "system_prompt": "You are a data analyst expert. You analyze datasets, identify patterns, create visualizations, perform statistical analysis, and provide data-driven insights. You excel at explaining data findings to both technical and non-technical audiences.",
  "input_format": "Dataset description + questions",
  "output_format": "Analysis report with insights and recommendations",
  "best_for": ["Data analysis", "Reporting", "Research", "Decision support"]
}
```

### 5. UX Designer Specialist

```json
{
  "name": "UX Designer",
  "system_prompt": "You are a UX design expert. You understand user psychology, design principles, accessibility standards, and modern design systems. You provide actionable design recommendations based on user needs and best practices.",
  "input_format": "Design challenge + user context",
  "output_format": "Design recommendations with rationale",
  "best_for": ["UI/UX design", "User research", "Accessibility", "Design systems"]
}
```

### 6. Marketing Specialist

```json
{
  "name": "Marketing Specialist",
  "system_prompt": "You are a marketing expert specializing in digital marketing, content strategy, SEO, and brand communication. You create compelling campaigns, optimize content for engagement, and align marketing efforts with business goals.",
  "input_format": "Product/service + target audience",
  "output_format": "Marketing strategy or content",
  "best_for": ["Content creation", "Campaign planning", "SEO", "Social media"]
}
```

### 7. Legal Reviewer Specialist

```json
{
  "name": "Legal Reviewer",
  "system_prompt": "You are a legal expert specializing in technology and business law. You review contracts, identify legal risks, explain complex legal concepts, and provide compliance guidance. Note: You provide information, not legal advice.",
  "input_format": "Legal document or question",
  "output_format": "Review with identified risks and recommendations",
  "best_for": ["Contract review", "Compliance", "Risk assessment"]
}
```

### 8. Product Manager Specialist

```json
{
  "name": "Product Manager",
  "system_prompt": "You are an experienced product manager. You excel at defining product vision, prioritizing features, writing PRDs, managing roadmaps, and balancing user needs with business goals. Your approach is data-driven and user-focused.",
  "input_format": "Product idea or feature request",
  "output_format": "Product requirements or strategy document",
  "best_for": ["Product planning", "Feature prioritization", "Roadmap planning"]
}
```

---

## Advanced Techniques

### 1. Multi-Stage Specialists

Create specialists that work in stages:

```
Stage 1: Research Specialist → Gathers information
Stage 2: Analysis Specialist → Analyzes findings  
Stage 3: Synthesis Specialist → Combines insights
Stage 4: Communication Specialist → Formats output
```

### 2. Specialized Prompt Templates

Create reusable templates:

**Problem-Solving Template:**
```
1. Problem Statement: [Define clearly]
2. Context: [Provide background]
3. Analysis: [Break down problem]
4. Solutions: [Generate options]
5. Recommendation: [Choose best option]
6. Implementation: [Action steps]
```

**Research Template:**
```
1. Research Question: [What to investigate]
2. Methodology: [How to research]
3. Findings: [What was discovered]
4. Analysis: [What it means]
5. Conclusion: [Key takeaways]
6. Next Steps: [What to do next]
```

### 3. Combining Specialists

Use multiple specialists in sequence:

```
1. Question → Research Specialist
2. Research → Analysis Specialist
3. Analysis → Writer Specialist
4. Final Output
```

---

## Best Practices

### 1. Start Specific
- ✅ "Django REST API security reviewer"
- ❌ "Code reviewer"

### 2. Include Examples
Add example inputs/outputs to guide behavior:
```
Example Input:
[Show typical input]

Example Output:
[Show expected format]
```

### 3. Set Boundaries
Define what the specialist should NOT do:
```
Do NOT:
- Provide medical advice
- Make legal decisions
- Write code without reviewing
```

### 4. Iterate and Refine
- Test with real scenarios
- Gather feedback
- Refine prompts based on results
- Version control your prompts

### 5. Document Your Specialists
Keep a registry:
```json
{
  "specialist_name": "Python Security Reviewer",
  "version": "1.2",
  "created": "2024-01-15",
  "last_updated": "2024-03-20",
  "use_cases": ["Django apps", "API security"],
  "system_prompt": "...",
  "performance_notes": "Works best with 100-500 line code snippets"
}
```

---

## Using Specialists in AI Aggregator

### Method 1: Add as System Prompt Prefix

When querying, prefix your prompt:
```
[SPECIALIST SYSTEM PROMPT]

User Query: [Your question]
```

### Method 2: Create Custom Engine Configurations

In `config.json`, add specialist configurations:
```json
{
  "openai": {
    "api_key": "...",
    "specialists": {
      "code_reviewer": {
        "system_prompt": "...",
        "temperature": 0.3,
        "model": "gpt-4"
      }
    }
  }
}
```

### Method 3: Build Specialist Library

Create a `specialists/` directory:
```
specialists/
  ├── code_reviewer.json
  ├── technical_writer.json
  ├── data_analyst.json
  └── ...
```

---

## Quick Start Example

### Creating a "Email Writer" Specialist

1. **Define Role:**
   - Expert at writing professional emails
   - Understands tone, clarity, and action items

2. **Create System Prompt:**
```
You are an expert email writer. You write clear, professional, and actionable emails.
Your emails:
- Have a clear subject line
- Start with purpose
- Use bullet points for multiple items
- Include a clear call-to-action
- Are concise (under 150 words)
```

3. **Test:**
   - Input: "Ask team to review Q4 report by Friday"
   - Verify output matches your needs

4. **Refine:**
   - Adjust tone if needed
   - Add specific formatting rules
   - Test with various scenarios

---

## Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering)

---

## Contributing Specialists

Share your specialist templates! Create a pull request with:
- Specialist name and purpose
- System prompt
- Example use cases
- Performance notes

---

*Last updated: 2024-03-20*

