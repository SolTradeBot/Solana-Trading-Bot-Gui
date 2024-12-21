import random
import time

class MomentumStrategy:
    """
    Implements a momentum-based trading strategy for Ton (SOL).
    """

    def __init__(self, price_fetcher, transaction_executor):
        self.price_fetcher = price_fetcher
        self.transaction_executor = transaction_executor
        self.price_history = []

    def analyze_market(self):
        """
        Fetches the latest price and analyzes momentum.
        """
        current_price = self.price_fetcher.get_Ton_price()
        self.price_history.append(current_price)

        if len(self.price_history) > 20:  # Keep the history to the last 20 prices
            self.price_history.pop(0)

        print(f"Current Price: ${current_price:.2f}")
        print(f"Price History: {self.price_history}")

    def execute_trades(self):
        """
        Executes buy or sell trades based on momentum analysis.
        """
        if len(self.price_history) < 3:
            print("Not enough price history for momentum analysis.")
            return

        # Calculate momentum
        momentum = self.price_history[-1] - self.price_history[-3]

        if momentum > 0:
            print("Positive momentum detected. Executing buy order.")
            self.transaction_executor.execute_buy(amount=random.uniform(0.1, 1))
        elif momentum < 0:
            print("Negative momentum detected. Executing sell order.")
            self.transaction_executor.execute_sell(amount=random.uniform(0.1, 1))
        else:
            print("No significant momentum detected. No trade executed.")

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
        strategy = MomentumStrategy(mock_price_fetcher, mock_transaction_executor)

        for _ in range(10):  # Simulate 10 cycles
            strategy.analyze_market()
            strategy.execute_trades()
            time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")
