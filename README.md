# B58UUID for Python

[![PyPI version](https://img.shields.io/pypi/v/b58uuid.svg)](https://pypi.org/project/b58uuid/)
[![Python versions](https://img.shields.io/pypi/pyversions/b58uuid.svg)](https://pypi.org/project/b58uuid/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/b58uuid/b58uuid-py/workflows/Tests/badge.svg)](https://github.com/b58uuid/b58uuid-py/actions)

Base58-encoded UUID library for Python with zero dependencies.

## Why This Library?

- **Compact**: 22 characters instead of 36
- **URL-safe**: No special characters that need escaping
- **Unambiguous**: Uses Bitcoin's Base58 alphabet (excludes 0, O, I, l)
- **Fast**: Optimized encoding/decoding algorithms
- **Safe**: Comprehensive error handling with overflow protection
- **Zero dependencies**: Uses only Python standard library
- **Type hints**: Full type annotation support
- **Python 3.8+**: Compatible with Python 3.8 and higher

## Installation

```bash
pip install b58uuid
```

## Usage

```python
import b58uuid

# Generate a new UUID
b58 = b58uuid.generate()
print(b58)  # Output: 3FfGK34vwMvVFDedyb2nkf

# Encode existing UUID
encoded = b58uuid.encode('550e8400-e29b-41d4-a716-446655440000')
print(encoded)  # Output: BWBeN28Vb7cMEx7Ym8AUzs

# Decode back to UUID
uuid_str = b58uuid.decode('BWBeN28Vb7cMEx7Ym8AUzs')
print(uuid_str)  # Output: 550e8400-e29b-41d4-a716-446655440000
```

## API

### Functions

- `generate() -> str` - Generate a new random UUID and return Base58 encoding
- `encode(uuid_str: str) -> str` - Encode UUID string to Base58
- `decode(b58_str: str) -> str` - Decode Base58 string to UUID

### Exceptions

- `ValueError` - Raised for invalid input or overflow

## Features

- Zero dependencies (uses only Python standard library)
- Always produces exactly 22 characters
- Uses Bitcoin Base58 alphabet (no 0, O, I, l)
- Thread-safe operations
- Type hints support
- Full error handling with overflow protection

## Testing

```bash
# Run tests
python -m pytest tests/ -v

# Run tests with coverage
python -m pytest tests/ --cov=b58uuid --cov-report=html
```

## Development

### Requirements

- Python 3.8 or higher
- pytest (for testing)

### Building from Source

```bash
# Clone the repository
git clone https://github.com/b58uuid/b58uuid-py.git
cd b58uuid-py

# Install in development mode
pip install -e ".[dev]"

# Run tests
python -m pytest tests/ -v

# Build package
python -m build
```

For detailed contribution guidelines, see [CONTRIBUTING.md](.github/CONTRIBUTING.md).

## License

MIT License - see LICENSE file for details.
