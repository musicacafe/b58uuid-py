# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-12

### Added
- Initial release of b58uuid for Python
- Core functions: `encode()`, `decode()`, `generate()`
- Base58 encoding/decoding with Bitcoin alphabet
- Comprehensive error handling with overflow protection
- Full type hints support
- Zero external dependencies
- 76 comprehensive tests with 100% coverage
- Support for Python 3.8+

### Features
- Always produces exactly 22 characters
- URL-safe output (no special characters)
- Unambiguous alphabet (excludes 0, O, I, l)
- Thread-safe operations
- Cross-language compatible with other b58uuid implementations

[1.0.0]: https://github.com/b58uuid/b58uuid-py/releases/tag/1.0.0
