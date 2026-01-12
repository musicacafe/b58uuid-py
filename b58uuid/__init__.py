"""
b58uuid - High-performance Base58-encoded UUID library.
Provides concise, unambiguous, and URL-safe UUIDs.
"""

import uuid as _uuid
from .base58 import encode as base58_encode, decode as base58_decode

__version__ = '1.0.0'
__all__ = ['encode', 'decode', 'generate']


def encode(uuid_str: str) -> str:
    """
    Encodes a standard UUID string to a Base58-encoded string.
    
    Args:
        uuid_str: The UUID string (with or without hyphens)
        
    Returns:
        The Base58-encoded string
        
    Raises:
        ValueError: If the UUID format is invalid
    """
    try:
        # Parse UUID and convert to bytes
        uuid_obj = _uuid.UUID(uuid_str)
        return base58_encode(uuid_obj.bytes)
    except (ValueError, AttributeError) as e:
        raise ValueError(f'Invalid UUID format: {uuid_str}') from e


def decode(b58: str) -> str:
    """
    Decodes a Base58-encoded string back to a standard UUID string.
    
    Args:
        b58: The Base58-encoded string
        
    Returns:
        The UUID string in canonical format
        
    Raises:
        ValueError: If the Base58 string is invalid
    """
    try:
        uuid_bytes = base58_decode(b58)
        return str(_uuid.UUID(bytes=uuid_bytes))
    except ValueError as e:
        # Preserve underlying error information
        error_msg = str(e)
        if 'character' in error_msg or 'Empty' in error_msg or 'overflow' in error_msg.lower() or 'length' in error_msg:
            raise ValueError(error_msg) from e
        else:
            raise ValueError(f'Invalid b58uuid format: {b58}') from e


def generate() -> str:
    """
    Generates a new random UUID and returns its Base58-encoded representation.
    
    Returns:
        The Base58-encoded UUID
    """
    uuid_obj = _uuid.uuid4()
    return base58_encode(uuid_obj.bytes)
