# Contributing to NOIZYLAB

Thank you for your interest in contributing to NOIZYLAB! We welcome contributions from the community.

## How to Contribute

### Reporting Issues

- Use the GitHub issue tracker to report bugs
- Describe the issue in detail with steps to reproduce
- Include system information (OS version, Python version, etc.)
- Add relevant logs or error messages

### Suggesting Features

- Open an issue with the "enhancement" label
- Describe the feature and its use case
- Explain how it benefits the NOIZYLAB ecosystem

### Code Contributions

1. **Fork the Repository**
   ```bash
   git clone https://github.com/NOIZYLAB-io/NOIZYLAB.git
   cd NOIZYLAB
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow existing code style and conventions
   - Add tests for new functionality
   - Update documentation as needed
   - Keep commits focused and atomic

4. **Test Your Changes**
   ```bash
   # Run any relevant tests
   python -m pytest tests/
   ```

5. **Submit a Pull Request**
   - Push your branch to your fork
   - Create a PR against the `main` branch
   - Provide a clear description of the changes
   - Reference any related issues

## Code Style Guidelines

### Python
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose

### Shell Scripts
- Use `#!/bin/bash` shebang
- Add comments for complex logic
- Use meaningful variable names
- Follow bash best practices

### Documentation
- Use clear, concise language
- Include code examples where helpful
- Keep documentation up-to-date with code changes
- Use proper Markdown formatting

## Project Structure

```
NOIZYLAB/
├── PROJECTS/           # Active audio projects
├── SystemGuardian/     # System monitoring
├── scripts/            # Automation scripts
├── assets/             # Static resources
├── data/               # Databases & configs
├── docs/               # Documentation
└── universal-blocker/  # Network tools
```

## Development Setup

### Prerequisites
- macOS 12+ (Monterey or later)
- Python 3.9+
- Homebrew
- Git

### Installation
```bash
# Install Python dependencies
pip install -r requirements.txt

# Run system checks
./SystemGuardian/guardian_core.sh
```

## Testing

- Write tests for new features
- Ensure existing tests pass
- Test on a clean environment when possible
- Document test procedures for complex features

## Documentation

- Update relevant docs in `/docs`
- Add examples for new features
- Keep the main README.md current
- Update CHANGELOG.md for notable changes

## Code Review Process

1. Automated checks must pass
2. At least one maintainer review required
3. All comments addressed
4. No merge conflicts
5. Documentation updated

## Community

- Be respectful and constructive
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md)
- Help other contributors when possible
- Share knowledge and best practices

## Questions?

If you have questions about contributing:
- Open a discussion on GitHub
- Check existing documentation
- Review closed issues and PRs for examples

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**NOIZYLAB** | Professional Music Production & Audio Engineering Platform
