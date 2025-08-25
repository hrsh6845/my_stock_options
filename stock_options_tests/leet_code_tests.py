import pytest
from flask import Flask
from

class TestLeetCode:
    def setup_method(self):
        self.app = Flask(__name__)

    def teardown_method(self):
        pass

    def test_remove_duplicates(self):
        leet_code = LeetCode()
        assert leet_code.remove_duplicates([1, 1, 2]) == [1, 2]