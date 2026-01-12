"""
Base58 encoding and decoding for b58uuid.
Uses the Bitcoin Base58 alphabet.
Always produces exactly 22 characters for 16-byte UUIDs.
"""

ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

# Create reverse lookup table
REVERSE_ALPHABET = {char: i for i, char in enumerate(ALPHABET)}

# Maximum UUID value (2^128 - 1)
MAX_UUID = (1 << 128) - 1


def encode(data: bytes) -> str:
    """
    Encodes a 16-byte UUID to a Base58 string.
    Always returns exactly 22 characters.
    
    Args:
        data: The 16-byte UUID
        
    Returns:
        The Base58-encoded string (exactly 22 characters)
        
    Raises:
        ValueError: If data is not exactly 16 bytes
    """
    if len(data) != 16:
        raise ValueError(f'Input must be exactly 16 bytes, got {len(data)}')
    
    # Convert bytes to integer
    num = int.from_bytes(data, byteorder='big')
    
    # Convert to base58
    result = []
    while num > 0:
        result.append(ALPHABET[num % 58])
        num //= 58
    
    # Reverse the result
    result.reverse()
    
    # Pad with leading '1' to ensure exactly 22 characters
    while len(result) < 22:
        result.insert(0, '1')
    
    return ''.join(result)


def decode(b58: str) -> bytes:
    """
    Decodes a Base58 string to a 16-byte UUID.
    
    Args:
        b58: The Base58-encoded string
        
    Returns:
        The 16-byte UUID
        
    Raises:
        ValueError: If the string contains invalid characters, is empty, or overflows
    """
    if not b58:
        raise ValueError('Empty Base58 string')
    
    # Validate length - should be 22 characters for 16-byte UUID
    if len(b58) != 22:
        raise ValueError(f'Invalid Base58 length: expected 22, got {len(b58)}')
    
    # Convert Base58 to integer with overflow checking
    num = 0
    for i, char in enumerate(b58):
        if char not in REVERSE_ALPHABET:
            raise ValueError(f'Invalid Base58 character at position {i}: {char}')
        
        num = num * 58 + REVERSE_ALPHABET[char]
        
        # Check for overflow
        if num > MAX_UUID:
            raise ValueError('Overflow: decoded value exceeds maximum UUID value (2^128 - 1)')
    
    # Convert integer to bytes (big-endian, 16 bytes)
    return num.to_bytes(16, byteorder='big')

