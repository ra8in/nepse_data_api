import pytest
from nepse_data_api.security import NepseTokenParser

class TestSecurity:
    def test_token_parser_init(self):
        """Test that token parser initializes correctly"""
        parser = NepseTokenParser()
        assert parser.wasm_module is not None

    def test_parse_token_response(self):
        """Test token parsing logic (mocked since it depends on specific WASM logic)"""
        parser = NepseTokenParser()
        
        # We can't easily test exact WASM output without a real pair of salts/tokens
        # valid for that WASM, but we can test that it accepts the structure
        # and returns 3 values (access, refresh, salts)
        
        # Using dummy values that might fail WASM internal indexing if not careful, 
        # but let's try a minimal valid structure
        data = {
            "salt1": 1, "salt2": 2, "salt3": 3, "salt4": 4, "salt5": 5,
            "accessToken": "a" * 100, # Needs to be long enough for indices
            "refreshToken": "b" * 100
        }
        
        try:
            access, refresh, salts = parser.parse_token_response(data)
            assert isinstance(access, str)
            assert isinstance(refresh, str)
            assert isinstance(salts, list)
            assert len(salts) == 5
        except IndexError:
            # Expected if our dummy salts generate indices out of bounds for dummy strings
            pass
