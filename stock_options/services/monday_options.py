class MondayCalculator:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_monday_options(self):
        # returning dummy data to test the end to end.
        return {
            "symbol": self.symbol,
            "price": 145.75,
            "change": 1.24
        }