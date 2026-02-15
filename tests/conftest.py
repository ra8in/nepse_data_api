import pytest
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def mock_token_response():
    return {
        "salt1": 10, "salt2": 12, "salt3": 15, "salt4": 20, "salt5": 25,
        "accessToken": "dummy_access_token_12345_descrambled",
        "refreshToken": "dummy_refresh_token_67890_descrambled",
        "serverTime": 1678900000000
    }

@pytest.fixture
def mock_market_status():
    return {
        "isOpen": "OPEN",
        "asOf": "2026-02-15T12:00:00"
    }
