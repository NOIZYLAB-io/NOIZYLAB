# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

The NOIZYLAB team takes security issues seriously. We appreciate your efforts to responsibly disclose your findings.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities by email to:
- **Email**: rsplowman@icloud.com
- **Subject**: [SECURITY] Brief description of the issue

### What to Include

Please include the following information in your report:

1. **Type of Issue**
   - Code vulnerability
   - Dependency vulnerability
   - Configuration issue
   - Other (please specify)

2. **Impact**
   - What can be exploited?
   - Who is affected?
   - What is the severity?

3. **Reproduction Steps**
   - Detailed steps to reproduce the issue
   - Any relevant code snippets
   - System configuration details

4. **Proof of Concept**
   - Working exploit (if safe to share)
   - Screenshots or logs
   - Any additional evidence

5. **Suggested Fix** (if available)
   - Proposed solution
   - Relevant patches or code changes

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Varies based on severity
  - Critical: Within 7 days
  - High: Within 30 days
  - Medium: Within 90 days
  - Low: Next scheduled release

### Security Update Process

1. **Acknowledgment**: We confirm receipt of your report
2. **Investigation**: We verify and assess the vulnerability
3. **Development**: We develop and test a fix
4. **Disclosure**: We coordinate disclosure timing with you
5. **Release**: We release the security update
6. **Credit**: We credit you in the security advisory (if desired)

## Security Best Practices

### For Users

1. **Keep Updated**
   - Use the latest version of NOIZYLAB
   - Regularly update dependencies
   - Monitor security advisories

2. **Secure Configuration**
   - Use strong passwords and API keys
   - Don't commit secrets to version control
   - Follow principle of least privilege

3. **System Security**
   - Keep macOS updated
   - Use firewall and security tools
   - Monitor system logs regularly

### For Contributors

1. **Code Security**
   - Validate all inputs
   - Use parameterized queries
   - Avoid hardcoded secrets
   - Handle errors securely

2. **Dependencies**
   - Review dependencies before adding
   - Keep dependencies updated
   - Use dependency scanning tools
   - Remove unused dependencies

3. **Testing**
   - Include security test cases
   - Test edge cases and boundary conditions
   - Perform code reviews
   - Use static analysis tools

## Known Security Considerations

### Network Tools
- Universal Blocker requires elevated permissions
- Review blocklists before deployment
- Monitor network traffic patterns

### System Access
- SystemGuardian runs with limited privileges
- Scripts should be reviewed before execution
- File permissions should be restrictive

### API Integration
- API keys should be stored securely
- Use environment variables for secrets
- Implement rate limiting
- Validate all API responses

## Security Tooling

We use the following security tools:

- **Dependency Scanning**: Regular checks for vulnerable dependencies
- **Code Analysis**: Static analysis for security issues
- **Access Control**: Repository permissions and protected branches
- **Audit Logs**: Tracking of security-relevant changes

## Disclosure Policy

- We coordinate disclosure with security researchers
- We aim for responsible disclosure timelines
- We provide security advisories for significant issues
- We credit researchers in advisories (with permission)

## Security Hall of Fame

We recognize security researchers who help improve NOIZYLAB security:

*No vulnerabilities reported yet*

Thank you for helping keep NOIZYLAB and our users safe!

## Questions?

For general security questions (not vulnerability reports):
- Open a GitHub discussion
- Review security documentation in `/docs`

---

**NOIZYLAB Security Team**
