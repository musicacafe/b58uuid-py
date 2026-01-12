"""
Edge case tests for b58uuid Python implementation
"""

import pytest
from b58uuid import encode, decode, generate


class TestEdgeCases:
    """Test edge cases and error handling"""
    
    def test_mixed_case_uuid(self):
        """Test encoding mixed case UUID"""
        mixed_case = '550E8400-E29B-41D4-A716-446655440000'
        result = encode(mixed_case)
        assert result == 'BWBeN28Vb7cMEx7Ym8AUzs'
    
    def test_uppercase_uuid_without_hyphens(self):
        """Test encoding uppercase UUID without hyphens"""
        upper_no_hyphens = '550E8400E29B41D4A716446655440000'
        result = encode(upper_no_hyphens)
        assert result == 'BWBeN28Vb7cMEx7Ym8AUzs'
    
    def test_very_large_uuid_values(self):
        """Test encoding very large UUID values"""
        max_uuid = 'ffffffff-ffff-ffff-ffff-ffffffffffff'
        result = encode(max_uuid)
        assert result == 'YcVfxkQb6JRzqk5kF2tNLv'
    
    def test_very_small_uuid_values(self):
        """Test encoding very small UUID values"""
        min_uuid = '00000000-0000-0000-0000-000000000001'
        result = encode(min_uuid)
        assert result == '1111111111111111111112'
    
    def test_random_uuid_values(self):
        """Test encoding random UUID values"""
        random_uuid = 'deadbeef-cafe-babe-0123-456789abcdef'
        result = encode(random_uuid)
        assert result == 'UVqy39vS4tbfPzthw5VEKg'
        assert decode(result) == 'deadbeef-cafe-babe-0123-456789abcdef'


class TestErrorHandling:
    """Test error handling scenarios"""
    
    def test_invalid_uuid_format(self):
        """Test encoding invalid UUID format"""
        with pytest.raises(ValueError, match="Invalid UUID"):
            encode('invalid-uuid')
    
    def test_empty_string(self):
        """Test encoding empty string"""
        with pytest.raises(ValueError, match="Invalid UUID"):
            encode('')
    
    def test_uuid_with_invalid_characters(self):
        """Test encoding UUID with invalid characters"""
        with pytest.raises(ValueError, match="Invalid UUID"):
            encode('gggggggg-gggg-gggg-gggg-gggggggggggg')
    
    def test_too_short_uuid(self):
        """Test encoding too short UUID"""
        with pytest.raises(ValueError, match="Invalid UUID"):
            encode('550e8400-e29b-41d4-a716')
    
    def test_too_long_uuid(self):
        """Test encoding too long UUID"""
        with pytest.raises(ValueError, match="Invalid UUID"):
            encode('550e8400-e29b-41d4-a716-446655440000-extra')
    
    def test_invalid_base58_characters(self):
        """Test decoding invalid Base58 characters"""
        with pytest.raises(ValueError, match="Invalid Base58"):
            decode('0000000000000000000000')  # Contains 0
    
    def test_base58_with_invalid_characters(self):
        """Test decoding Base58 with invalid characters"""
        with pytest.raises(ValueError, match="Invalid Base58"):
            decode('OOOOOOOOOOOOOOOOOOOOOO')  # Contains O
    
    def test_empty_base58_string(self):
        """Test decoding empty Base58 string"""
        with pytest.raises(ValueError, match="Empty Base58 string"):
            decode('')
    
    def test_base58_with_I(self):
        """Test decoding Base58 with I"""
        with pytest.raises(ValueError, match="Invalid Base58"):
            decode('IIIIIIIIIIIIIIIIIIIIII')
    
    def test_base58_with_l(self):
        """Test decoding Base58 with l"""
        with pytest.raises(ValueError, match="Invalid Base58"):
            decode('llllllllllllllllllllll')


class TestBase58EdgeCases:
    """Test Base58 specific edge cases"""
    
    def test_all_ones_base58_string(self):
        """Test decoding all 1s Base58 string"""
        all_ones = '1111111111111111111111'
        result = decode(all_ones)
        assert result == '00000000-0000-0000-0000-000000000000'
    
    def test_maximum_base58_string(self):
        """Test decoding maximum Base58 string"""
        max_b58 = 'YcVfxkQb6JRzqk5kF2tNLv'
        result = decode(max_b58)
        assert result == 'ffffffff-ffff-ffff-ffff-ffffffffffff'
    
    def test_single_character_base58(self):
        """Test decoding single character Base58"""
        single_char = '1111111111111111111112'
        result = decode(single_char)
        assert result == '00000000-0000-0000-0000-000000000001'
    
    def test_base58_with_leading_ones(self):
        """Test decoding Base58 with leading 1s"""
        leading_ones = '111111111111111111111A'
        result = decode(leading_ones)
        assert result == '00000000-0000-0000-0000-000000000009'


class TestGenerationEdgeCases:
    """Test UUID generation edge cases"""
    
    def test_generate_unique_uuids(self):
        """Test generating unique UUIDs"""
        count = 1000
        uuids = set()
        
        for i in range(count):
            uuid = generate()
            assert len(uuid) == 22
            assert uuid not in uuids
            uuids.add(uuid)
        
        assert len(uuids) == count
    
    def test_generate_valid_base58_strings(self):
        """Test generating valid Base58 strings"""
        for i in range(100):
            b58 = generate()
            # Should not throw
            decode(b58)
    
    def test_generate_strings_with_valid_base58_characters_only(self):
        """Test generating strings with valid Base58 characters only"""
        valid_chars = set('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')
        
        for i in range(50):
            b58 = generate()
            for char in b58:
                assert char in valid_chars


class TestPerformanceEdgeCases:
    """Test performance edge cases"""
    
    def test_rapid_encoding_decoding(self):
        """Test rapid encoding/decoding"""
        iterations = 1000
        uuid = '550e8400-e29b-41d4-a716-446655440000'
        
        start = time.time()
        for i in range(iterations):
            encoded = encode(uuid)
            decoded = decode(encoded)
            assert decoded == uuid
        
        duration = time.time() - start
        assert duration < 1.0  # Should complete in less than 1 second
    
    def test_concurrent_like_operations(self):
        """Test concurrent-like operations"""
        uuids = [
            '550e8400-e29b-41d4-a716-446655440000',
            '12345678-1234-5678-1234-567812345678',
            'ffffffff-ffff-ffff-ffff-ffffffffffff',
            '00000000-0000-0000-0000-000000000000'
        ]
        
        results = []
        for uuid in uuids:
            encoded = encode(uuid)
            decoded = decode(encoded)
            results.append((uuid, decoded))
        
        for uuid, decoded in results:
            assert decoded == uuid


class TestBoundaryConditions:
    """Test boundary conditions"""
    
    def test_uuid_boundary_values(self):
        """Test UUID boundary values"""
        boundaries = [
            '00000000-0000-0000-0000-000000000000',  # Min
            '00000000-0000-0000-0000-000000000001',  # Min + 1
            'ffffffff-ffff-ffff-ffff-ffffffffffff',  # Max
            'ffffffff-ffff-ffff-ffff-fffffffffff0',  # Max - 15
            '80000000-0000-0000-0000-000000000000',  # Midpoint
        ]
        
        for uuid in boundaries:
            encoded = encode(uuid)
            decoded = decode(encoded)
            assert decoded == uuid
    
    def test_base58_boundary_values(self):
        """Test Base58 boundary values"""
        b58_boundaries = [
            '1111111111111111111111',  # Min (all zeros)
            '1111111111111111111112',  # Min + 1
            'YcVfxkQb6JRzqk5kF2tNLv',  # Max (all Fs)
        ]
        
        for b58 in b58_boundaries:
            decoded = decode(b58)
            reencoded = encode(decoded)
            assert reencoded == b58


class TestErrorMessageQuality:
    """Test error message quality"""
    
    def test_helpful_error_messages_for_invalid_uuid(self):
        """Test helpful error messages for invalid UUID"""
        with pytest.raises(ValueError) as exc_info:
            encode('invalid-uuid')
        
        error_message = str(exc_info.value)
        assert 'Invalid UUID' in error_message
        assert 'invalid-uuid' in error_message
    
    def test_helpful_error_messages_for_invalid_base58(self):
        """Test helpful error messages for invalid Base58"""
        with pytest.raises(ValueError) as exc_info:
            decode('0000000000000000000000')
        
        error_message = str(exc_info.value)
        assert 'Invalid Base58' in error_message


# Add timing import
import time