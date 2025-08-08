import pytest
from flask import Flask
from stock_options.services.my_trades_history import analyze_my_trades

class TestMyTradesHistory:
    def setup_method(self):
        self.app = Flask(__name__)

    def teardown_method(self):
        pass

    def test_analyze_my_trades(self):
        my_trades = analyze_my_trades()
        assert my_trades.price.iloc[0] == 145.75
