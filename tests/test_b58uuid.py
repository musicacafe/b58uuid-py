"""
Tests for b58uuid library.
"""

import pytest
from b58uuid import encode, decode, generate


class TestEncode:
    """Tests for encode function."""
    
    test_vectors = [
        ('550e8400-e29b-41d4-a716-446655440000', 'BWBeN28Vb7cMEx7Ym8AUzs'),
        ('550e8400e29b41d4a716446655440000', 'BWBeN28Vb7cMEx7Ym8AUzs'),
        ('00000000-0000-0000-0000-000000000000', '1111111111111111111111'),
        ('ffffffff-ffff-ffff-ffff-ffffffffffff', 'YcVfxkQb6JRzqk5kF2tNLv'),
    ]
    
    @pytest.mark.parametrize('uuid_str,expected', test_vectors)
    def test_encode(self, uuid_str, expected):
        """Test encoding of various UUIDs."""
        assert encode(uuid_str) == expected
    
    def test_encode_invalid_uuid(self):
        """Test encoding of invalid UUIDs."""
        with pytest.raises(ValueError):
            encode('invalid')
        with pytest.raises(ValueError):
            encode('')


class TestDecode:
    """Tests for decode function."""
    
    test_vectors = [
        ('BWBeN28Vb7cMEx7Ym8AUzs', '550e8400-e29b-41d4-a716-446655440000'),
        ('1111111111111111111111', '00000000-0000-0000-0000-000000000000'),
        ('YcVfxkQb6JRzqk5kF2tNLv', 'ffffffff-ffff-ffff-ffff-ffffffffffff'),
    ]
    
    @pytest.mark.parametrize('b58,expected', test_vectors)
    def test_decode(self, b58, expected):
        """Test decoding of various b58uuids."""
        result = decode(b58)
        assert result.lower() == expected.lower()
    
    def test_decode_invalid_b58(self):
        """Test decoding of invalid b58uuids."""
        with pytest.raises(ValueError):
            decode('000000000000000000000O')  # Contains O
        with pytest.raises(ValueError):
            decode('OOOOOOOOOOOOOOOOOOOOOO')  # Contains O
        with pytest.raises(ValueError):
            decode('')  # Empty


class TestRoundTrip:
    """Tests for round-trip encoding/decoding."""
    
    test_uuids = [
        '550e8400-e29b-41d4-a716-446655440000',
        '00000000-0000-0000-0000-000000000000',
        'ffffffff-ffff-ffff-ffff-ffffffffffff',
        'deadbeef-cafe-babe-0123-456789abcdef',
    ]
    
    @pytest.mark.parametrize('uuid_str', test_uuids)
    def test_round_trip(self, uuid_str):
        """Test that encode/decode round-trip works."""
        encoded = encode(uuid_str)
        decoded = decode(encoded)
        assert decoded.lower() == uuid_str.lower()


class TestGenerate:
    """Tests for generate function."""
    
    def test_generate(self):
        """Test that generate produces valid b58uuids."""
        b58 = generate()
        assert len(b58) == 22
        # Should be decodable
        uuid_str = decode(b58)
        assert len(uuid_str) == 36  # Standard UUID format
    
    def test_generate_unique(self):
        """Test that generate produces unique values."""
        b58_1 = generate()
        b58_2 = generate()
        assert b58_1 != b58_2
