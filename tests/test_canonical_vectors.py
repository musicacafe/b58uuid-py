"""
Tests using canonical test vectors from test-vectors.json
"""

import pytest
from b58uuid import encode, decode


class TestCanonicalVectors:
    """Test with canonical test vectors"""
    
    # Canonical test vectors from test-vectors.json
    test_vectors = [
        ("00000000-0000-0000-0000-000000000000", "1111111111111111111111"),  # nil_uuid
        ("ffffffff-ffff-ffff-ffff-ffffffffffff", "YcVfxkQb6JRzqk5kF2tNLv"),  # max_uuid
        ("550e8400-e29b-41d4-a716-446655440000", "BWBeN28Vb7cMEx7Ym8AUzs"),  # standard_uuid
        ("123e4567-e89b-12d3-a456-426614174000", "3FfGK34vwMvVFDedyb2nkf"),  # uuid_v1_example
        ("00000000-0000-0000-0000-000000000001", "1111111111111111111112"),  # uuid_with_leading_zeros
        ("deadbeef-cafe-babe-0123-456789abcdef", "UVqy39vS4tbfPzthw5VEKg"),  # deadbeef_uuid
        ("01020304-0506-0708-090a-0b0c0d0e0f10", "18DfbjXLth7APvt3qQPgtf"),  # sequential_bytes
        ("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", "N5L7eAc4PsHfZViqAMbFEH"),  # all_same_byte
        ("12345678-9abc-def0-1234-56789abcdef0", "3FP9ScppY3pxArsirSpyro"),  # mixed_pattern
    ]
    
    @pytest.mark.parametrize('uuid_str,expected_b58', test_vectors)
    def test_canonical_encode(self, uuid_str, expected_b58):
        """Test encoding with canonical test vectors"""
        result = encode(uuid_str)
        assert result == expected_b58
        assert len(result) == 22
    
    @pytest.mark.parametrize('uuid_str,b58_str', test_vectors)
    def test_canonical_decode(self, uuid_str, b58_str):
        """Test decoding with canonical test vectors"""
        result = decode(b58_str)
        assert result.lower() == uuid_str.lower()
    
    @pytest.mark.parametrize('uuid_str,b58_str', test_vectors)
    def test_canonical_round_trip(self, uuid_str, b58_str):
        """Test round-trip with canonical test vectors"""
        # Encode
        encoded = encode(uuid_str)
        assert encoded == b58_str
        
        # Decode
        decoded = decode(encoded)
        assert decoded.lower() == uuid_str.lower()
        
        # Re-encode
        reencoded = encode(decoded)
        assert reencoded == b58_str


class TestOverflowDetection:
    """Test overflow detection"""
    
    def test_overflow_on_decode(self):
        """Test that decoding a value > 2^128-1 raises overflow error"""
        # "Z" repeated 22 times is much larger than max UUID
        with pytest.raises(ValueError, match="[Oo]verflow"):
            decode("ZZZZZZZZZZZZZZZZZZZZZZ")
    
    def test_max_uuid_does_not_overflow(self):
        """Test that max UUID (all 0xFF) does not overflow"""
        max_uuid = "ffffffff-ffff-ffff-ffff-ffffffffffff"
        encoded = encode(max_uuid)
        decoded = decode(encoded)
        assert decoded.lower() == max_uuid.lower()


class Test22CharacterOutput:
    """Test that all encodings produce exactly 22 characters"""
    
    def test_nil_uuid_22_chars(self):
        """Test that nil UUID produces 22 characters"""
        result = encode("00000000-0000-0000-0000-000000000000")
        assert len(result) == 22
        assert result == "1111111111111111111111"
    
    def test_max_uuid_22_chars(self):
        """Test that max UUID produces 22 characters"""
        result = encode("ffffffff-ffff-ffff-ffff-ffffffffffff")
        assert len(result) == 22
    
    def test_random_uuids_22_chars(self):
        """Test that random UUIDs produce 22 characters"""
        from b58uuid import generate
        
        for _ in range(100):
            b58 = generate()
            assert len(b58) == 22
    
    def test_leading_zero_uuids_22_chars(self):
        """Test that UUIDs with leading zeros produce 22 characters"""
        test_cases = [
            "00000000-0000-0000-0000-000000000001",
            "00000000-0000-0000-0000-00000000000f",
            "00000000-0000-0000-0000-0000000000ff",
            "00000000-0000-0000-0000-000000000fff",
            "01020304-0506-0708-090a-0b0c0d0e0f10",
        ]
        
        for uuid_str in test_cases:
            result = encode(uuid_str)
            assert len(result) == 22, f"UUID {uuid_str} produced {len(result)} chars: {result}"
