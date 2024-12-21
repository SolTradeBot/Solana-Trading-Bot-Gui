import random
import time

class ScalpingStrategy:
    """
    Implements a scalping strategy for short-term trading of Ton (SOL).
    """

    def __init__(self, price_fetcher, transaction_executor):
        self.price_fetcher = price_fetcher
        self.transaction_executor = transaction_executor
        self.last_price = None

    def analyze_market(self):
        """
        Fetches the current price and decides whether to trade based on small fluctuations.
        """
        current_price = self.price_fetcher.get_Ton_price()
        print(f"Current Price: ${current_price:.2f}")

        if self.last_price is not None:
            price_change = current_price - self.last_price
            percentage_change = (price_change / self.last_price) * 100
            print(f"Price Change: {price_change:.2f} (${percentage_change:.2f}%)")

            if abs(percentage_change) > 0.3:  # Trigger trade for > 0.3% price change
                self._execute_trade(current_price, price_change)
        else:
            print("No previous price to compare. Skipping trade analysis.")

        self.last_price = current_price

    def _execute_trade(self, current_price, price_change):
        """
        Executes a buy or sell trade based on price fluctuation.
        """
        if price_change > 0:
            print("Detected upward movement. Executing sell order.")
            self.transaction_executor.execute_sell(amount=random.uniform(0.1, 0.5))
        else:
            print("Detected downward movement. Executing buy order.")
            self.transaction_executor.execute_buy(amount=random.uniform(0.1, 0.5))

if __name__ == "__main__":
    class MockPriceFetcher:
        """
        A mock price fetcher for testing purposes.
        """
        def get_Ton_price(self):
            return round(random.uniform(20, 30), 2)

    class MockTransactionExecutor:
        """
        A mock transaction executor for testing purposes.
        """
        def execute_buy(self, amount):
            print(f"Mock buy executed for {amount:.2f} SOL.")

        def execute_sell(self, amount):
            print(f"Mock sell executed for {amount:.2f} SOL.")

    # Example usage
    try:
        mock_price_fetcher = MockPriceFetcher()
        mock_transaction_executor = MockTransactionExecutor()
        scalping_strategy = ScalpingStrategy(mock_price_fetcher, mock_transaction_executor)

        for _ in range(10):  # Simulate 10 cycles
            scalping_strategy.analyze_market()
            time.sleep(1)  # Scalping works on shorter intervals
    except Exception as e:
        print(f"Error: {e}")
