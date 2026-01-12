# Contributing to b58uuid-py

Thank you for your interest in contributing to b58uuid-py!

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/b58uuid/b58uuid-py.git
cd b58uuid-py

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

## Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run tests with coverage
python -m pytest tests/ --cov=b58uuid --cov-report=html

# Run specific test file
python -m pytest tests/test_b58uuid.py -v
```

## Code Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints for all functions
- Write docstrings for all public functions
- Keep functions focused and simple

## Making Changes

1. **Fork the repository** on GitHub
2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** with clear, focused commits
4. **Add tests** for any new functionality
5. **Run tests** to ensure everything passes:
   ```bash
   python -m pytest tests/ -v
   ```
6. **Update documentation** if needed (README.md, docstrings)
7. **Push to your fork** and submit a pull request

## Pull Request Guidelines

- **One feature per PR**: Keep pull requests focused on a single feature or fix
- **Write clear descriptions**: Explain what changes you made and why
- **Include tests**: All new code should have corresponding tests
- **Update CHANGELOG.md**: Add your changes under "Unreleased" section
- **Ensure tests pass**: All tests must pass before merging
- **Follow code style**: Maintain consistency with existing code

## Commit Messages

- Use clear, descriptive commit messages
- Start with a verb in present tense (e.g., "Add", "Fix", "Update")
- Keep the first line under 72 characters
- Add details in the body if needed

Examples:
```
Add overflow detection for decode function

Fix edge case in Base58 encoding for zero values

Update README with new API examples
```

## Reporting Issues

When reporting issues, please include:

- **Python version**: Output of `python --version`
- **Operating system**: Windows, macOS, Linux
- **Description**: Clear description of the issue
- **Steps to reproduce**: Minimal code example that reproduces the issue
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened

## Feature Requests

We welcome feature requests! Please:

- Check if the feature already exists or is planned
- Explain the use case and benefits
- Provide examples of how it would be used
- Consider if it fits the library's scope (Base58 UUID encoding/decoding)

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Assume good intentions

## Questions?

If you have questions about contributing, feel free to:

- Open an issue with the "question" label
- Check existing issues and discussions
- Review the README.md for basic usage

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
