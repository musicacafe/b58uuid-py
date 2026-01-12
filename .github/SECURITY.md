# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in b58uuid-py, please report it by emailing:

**security@b58uuid.io**

Please include:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

We will respond within 48 hours and work with you to understand and address the issue.

## Security Considerations

### Overflow Protection

b58uuid-py includes overflow detection to prevent integer overflow attacks during decoding. The library validates that decoded values do not exceed the maximum UUID value (2^128 - 1).

### Input Validation

All inputs are validated before processing:
- UUID strings must be valid UUID format
- Base58 strings must be exactly 22 characters
- Base58 strings must contain only valid Base58 characters

### No External Dependencies

b58uuid-py uses only Python's standard library, reducing the attack surface from third-party dependencies.

## Best Practices

When using b58uuid-py:

1. **Validate inputs**: Always validate UUIDs from untrusted sources
2. **Handle errors**: Catch and handle `ValueError` exceptions appropriately
3. **Use latest version**: Keep the library updated to get security fixes
4. **Review changes**: Check CHANGELOG.md for security-related updates

## Disclosure Policy

- Security issues are fixed as soon as possible
- Fixes are released in patch versions
- Security advisories are published on GitHub
- Credits are given to reporters (unless they prefer to remain anonymous)
