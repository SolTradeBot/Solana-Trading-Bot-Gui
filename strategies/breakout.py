import random
import time

class BreakoutStrategy:
    """
    Identifies price breakouts by monitoring support and resistance levels.
    """

    def __init__(self, price_fetcher, transaction_executor):
        self.price_fetcher = price_fetcher
        self.transaction_executor = transaction_executor
        self.price_history = []
        self.lookback_period = 20  # Period to calculate support/resistance
        self.breakout_threshold = 0.02  # 2% breakout threshold

    def calculate_support_resistance(self):
        """
        Calculates the support (low) and resistance (high) levels from the price history.
        """
        if len(self.price_history) < self.lookback_period:
            return None, None

        recent_prices = self.price_history[-self.lookback_period:]
        support = min(recent_prices)
        resistance = max(recent_prices)

        return support, resistance

    def analyze_market(self):
        """
        Monitors price movements and executes trades if a breakout is detected.
        """
        current_price = self.price_fetcher.get_Ton_price()
        self.price_history.append(current_price)

        if len(self.price_history) > self.lookback_period:
            self.price_history.pop(0)

        support, resistance = self.calculate_support_resistance()
        if support is None or resistance is None:
            print("Not enough data to calculate support/resistance levels.")
            return

        print(f"Current Price: ${current_price:.2f}, Support: ${support:.2f}, Resistance: ${resistance:.2f}")

        if current_price > resistance * (1 + self.breakout_threshold):
            print("Upside breakout detected! Executing buy order.")
            self.transaction_executor.execute_buy(amount=random.uniform(1, 3))
        elif current_price < support * (1 - self.breakout_threshold):
            print("Downside breakout detected! Executing sell order.")
            self.transaction_executor.execute_sell(amount=random.uniform(1, 3))
        else:
            print("No breakout detected. Holding position.")

if __name__ == "__main__":
    class MockPriceFetcher:
        """
        Simulates a price fetcher for testing purposes.
        """
        def get_Ton_price(self):
            return round(random.uniform(20, 30), 2)

    class MockTransactionExecutor:
        """
        Simulates transaction execution for testing purposes.
        """
        def execute_buy(self, amount):
            print(f"Mock buy executed for {amount:.2f} SOL.")

        def execute_sell(self, amount):
            print(f"Mock sell executed for {amount:.2f} SOL.")

    # Example usage
    fetcher = MockPriceFetcher()
    executor = MockTransactionExecutor()
    strategy = BreakoutStrategy(fetcher, executor)

    for _ in range(10):  # Simulate 10 market checks
        strategy.analyze_market()
        time.sleep(1)
