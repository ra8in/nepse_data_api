import pytest
from unittest.mock import MagicMock, patch
from nepse_data_api.market import Nepse

class TestNepseMarket:
    
    @patch('nepse_data_api.market.requests.Session')
    def test_market_status(self, mock_session):
        """Test fetching market status"""
        # Setup mock
        mock_instance = mock_session.return_value
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "isOpen": "OPEN",
            "asOf": "2026-02-15T12:00:00"
        }
        mock_instance.get.return_value = mock_response

        # Test
        with patch('nepse_data_api.market.Nepse.authenticate'):
            nepse = Nepse(enable_cache=False)
            nepse.access_token = "dummy" # Manually set token to avoid auth call
            status = nepse.get_market_status()
            
            assert status['isOpen'] == "OPEN"
            assert status['asOf'] == "2026-02-15T12:00:00"

    @patch('nepse_data_api.market.requests.Session')
    def test_caching(self, mock_session):
        """Test that caching works"""
        mock_instance = mock_session.return_value
        mock_instance.get.return_value.json.return_value = {"data": "test"}
        mock_instance.get.return_value.status_code = 200
        
        with patch.object(Nepse, 'authenticate'):
            nepse = Nepse(enable_cache=True)
            nepse.access_token = "dummy"
            
            # First call - hits API
            nepse.get_market_summary()
            assert mock_instance.get.call_count == 1
            
            # Second call - should hit cache
            nepse.get_market_summary()
            assert mock_instance.get.call_count == 1
