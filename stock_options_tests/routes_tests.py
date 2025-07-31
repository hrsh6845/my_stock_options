import pytest
from flask import Flask
from unittest.mock import Mock, patch
from stock_options.routes import register_routes


class TestRoutes:
    def setup_method(self):
        self.app = Flask(__name__)
        register_routes(self.app)
        self.client = self.app.test_client()

    def teardown_method(self):
        pass

    @patch('stock_options.routes.MondayCalculator')
    def test_get_monday_options_default(self, mock_calculator):
        mock_instance = Mock()
        mock_instance.get_monday_options.return_value = {'data': 'test'}
        mock_calculator.return_value = mock_instance

        response = self.client.get('/get-monday-options')

        assert response.status_code == 200
        mock_calculator.assert_called_once_with('AAPL')
        mock_instance.get_monday_options.assert_called_once()
        assert response.json == {'data': 'test'}

    @patch('stock_options.routes.MondayCalculator')
    def test_get_monday_options_custom_symbol(self, mock_calculator):
        mock_instance = Mock()
        mock_instance.get_monday_options.return_value = {'data': 'test'}
        mock_calculator.return_value = mock_instance

        response = self.client.get('/get-monday-options?symbol=GOOGL')

        assert response.status_code == 200
        mock_calculator.assert_called_once_with('GOOGL')
        mock_instance.get_monday_options.assert_called_once()
        assert response.json == {'data': 'test'}
