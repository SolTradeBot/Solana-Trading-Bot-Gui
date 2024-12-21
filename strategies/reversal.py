import random
import time

class ReversalStrategy:
    """
    Implements a reversal strategy using RSI and Bollinger Bands to detect reversals.
    """

    def __init__(self, price_fetcher, transaction_executor):
        self.price_fetcher = price_fetcher
        self.transaction_executor = transaction_executor
        self.price_history = []

    def calculate_rsi(self, prices):
        """
        Calculates the Relative Strength Index (RSI).
        """
        if len(prices) < 14:
            return None  # Not enough data
        gains = [prices[i] - prices[i - 1] for i in range(1, len(prices)) if prices[i] > prices[i - 1]]
        losses = [prices[i - 1] - prices[i] for i in range(1, len(prices)) if prices[i] < prices[i - 1]]

        avg_gain = sum(gains) / 14 if gains else 0
        avg_loss = sum(losses) / 14 if losses else 0

        if avg_loss == 0:
            return 100
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    def calculate_bollinger_bands(self, prices):
        """
        Calculates Bollinger Bands for the given price list.
        """
        if len(prices) < 20:
            return None, None, None  # Not enough data
        sma = sum(prices[-20:]) / 20  # Simple Moving Average
        stddev = (sum([(p - sma) ** 2 for p in prices[-20:]]) / 20) ** 0.5
        return sma, sma + (2 * stddev), sma - (2 * stddev)

    def analyze_market(self):
        """
        Analyzes the market to detect overbought/oversold conditions.
        """
        current_price = self.price_fetcher.get_Ton_price()
        self.price_history.append(current_price)

        if len(self.price_history) > 50:  # Keep only the last 50 prices
            self.price_history.pop(0)

        rsi = self.calculate_rsi(self.price_history)
        sma, upper_band, lower_band = self.calculate_bollinger_bands(self.price_history)

        print(f"Price: ${current_price:.2f}, RSI: {rsi}, SMA: {sma}, Upper Band: {upper_band}, Lower Band: {lower_band}")

        if rsi is not None and rsi < 30 and current_price < lower_band:
            print("Oversold condition detected. Executing buy order.")
            self.transaction_executor.execute_buy(amount=random.uniform(0.5, 1.5))
        elif rsi is not None and rsi > 70 and current_price > upper_band:
            print("Overbought condition detected. Executing sell order.")
            self.transaction_executor.execute_sell(amount=random.uniform(0.5, 1.5))
        else:
            print("No significant reversal detected.")

if __name__ == "__main__":
    class MockPriceFetcher:
        def get_Ton_price(self):
            return round(random.uniform(20, 30), 2)

    class MockTransactionExecutor:
        def execute_buy(self, amount):
            print(f"Mock buy executed for {amount:.2f} SOL.")

        def execute_sell(self, amount):
            print(f"Mock sell executed for {amount:.2f} SOL.")

    # Example usage
    fetcher = MockPriceFetcher()
    executor = MockTransactionExecutor()
    strategy = ReversalStrategy(fetcher, executor)

    for _ in range(10):
        strategy.analyze_market()
        time.sleep(1)
