# Security Policy

## 🔒 NOIZYLAB Security

NOIZYLAB takes security seriously. This document outlines our security policies and procedures for reporting vulnerabilities.

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| 3.x.x   | :white_check_mark: |
| 2.x.x   | :x:                |
| < 2.0   | :x:                |

## Reporting a Vulnerability

### 🚨 Please DO NOT create public GitHub issues for security vulnerabilities.

If you discover a security vulnerability, please report it responsibly:

### Option 1: GitHub Security Advisory (Preferred)

1. Go to the [Security Advisories](https://github.com/NOIZYLAB-io/NOIZYLAB/security/advisories/new) page
2. Click "Report a vulnerability"
3. Provide detailed information about the vulnerability

### Option 2: Direct Contact

- **Email**: security@noizylab.io
- **Subject**: `[SECURITY] Brief description`

### What to Include in Your Report

- Type of vulnerability (e.g., XSS, SQL injection, authentication bypass)
- Location of the affected code (file path, line numbers if known)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if available)
- Impact assessment
- Suggested fix (if you have one)

## Response Timeline

| Action                         | Timeline        |
| ------------------------------ | --------------- |
| Initial acknowledgment         | Within 24 hours |
| Preliminary assessment         | Within 72 hours |
| Detailed response/action plan  | Within 7 days   |
| Resolution for critical issues | Within 30 days  |

## Security Best Practices

### For Contributors

1. **Never commit secrets**

   - Use environment variables for API keys
   - Add sensitive files to `.gitignore`
   - Use tools like `git-secrets` to prevent accidental commits

2. **Dependencies**

   - Keep dependencies updated
   - Run `npm audit` / `pip audit` regularly
   - Review dependency changes in PRs

3. **Code Review**
   - All PRs require security-conscious review
   - Use static analysis tools
   - Follow secure coding guidelines

### For Users

1. **Environment Variables**

   ```bash
   # Store secrets in .env (never commit!)
   OPENAI_API_KEY=sk-...
   GEMINI_API_KEY=...
   AZURE_SPEECH_KEY=...
   ```

2. **Access Control**

   - Use strong, unique passwords
   - Enable 2FA on GitHub
   - Limit API key permissions

3. **Data Protection**
   - Don't store sensitive data in logs
   - Encrypt data at rest and in transit
   - Follow data retention policies

## Security Features

### Current Implementations

- ✅ Environment variable management for secrets
- ✅ Input validation and sanitization
- ✅ Rate limiting on API endpoints
- ✅ HTTPS enforcement
- ✅ Dependency vulnerability scanning

### Planned Improvements

- [ ] Automated security scanning in CI/CD
- [ ] SAST (Static Application Security Testing)
- [ ] DAST (Dynamic Application Security Testing)
- [ ] Security headers enforcement
- [ ] Content Security Policy (CSP)

## Dependency Security

We use the following tools to monitor dependencies:

```bash
# JavaScript/Node.js
npm audit
npm audit fix

# Python
pip install pip-audit
pip-audit

# General
snyk test
```

## Disclosure Policy

- We follow [responsible disclosure](https://en.wikipedia.org/wiki/Responsible_disclosure)
- Security researchers who follow this policy will be credited (unless they prefer anonymity)
- We will not take legal action against researchers who:
  - Make a good faith effort to avoid privacy violations
  - Avoid destruction of data
  - Give us reasonable time to fix issues before disclosure

## Hall of Fame

We thank the following security researchers for their contributions:

_(No entries yet - be the first!)_

## Contact

- **Security Team**: security@noizylab.io
- **General Contact**: hello@noizylab.io
- **GitHub**: [@NOIZYLAB-io](https://github.com/NOIZYLAB-io)

---

_Last updated: January 2026_
