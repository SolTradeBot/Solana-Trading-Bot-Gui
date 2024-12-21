import random
import time

class PairTradingStrategy:
    """
    Implements a pair trading strategy based on the price relationship between two assets.
    """

    def __init__(self, price_fetcher, transaction_executor, base_asset="SOL", pair_asset="BTC"):
        self.price_fetcher = price_fetcher
        self.transaction_executor = transaction_executor
        self.base_asset = base_asset
        self.pair_asset = pair_asset
        self.pair_ratio_history = []
        self.lookback_period = 20  # Number of historical ratios to track

    def simulate_pair_price(self):
        """
        Simulates the price of the pair asset for testing purposes.
        """
        base_price = self.price_fetcher.get_Ton_price()
        pair_price = base_price * random.uniform(0.015, 0.025)  # Simulated pair ratio
        return base_price, pair_price

    def analyze_market(self):
        """
        Analyzes the price ratio between two assets and executes trades based on mean reversion.
        """
        base_price, pair_price = self.simulate_pair_price()
        pair_ratio = base_price / pair_price
        self.pair_ratio_history.append(pair_ratio)

        if len(self.pair_ratio_history) > self.lookback_period:
            self.pair_ratio_history.pop(0)

        mean_ratio = sum(self.pair_ratio_history) / len(self.pair_ratio_history)
        deviation = pair_ratio - mean_ratio

        print(f"Base Price ({self.base_asset}): ${base_price:.2f}, Pair Price ({self.pair_asset}): ${pair_price:.2f}")
        print(f"Current Ratio: {pair_ratio:.4f}, Mean Ratio: {mean_ratio:.4f}, Deviation: {deviation:.4f}")

        if deviation > 0.01:  # Ratio significantly above mean
            print(f"Pair ratio high. Executing sell order for {self.base_asset}.")
            self.transaction_executor.execute_sell(amount=random.uniform(0.5, 1.5))
        elif deviation < -0.01:  # Ratio significantly below mean
            print(f"Pair ratio low. Executing buy order for {self.base_asset}.")
            self.transaction_executor.execute_buy(amount=random.uniform(0.5, 1.5))
        else:
            print("Pair ratio within normal range. No trade executed.")

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
            print(f"Mock buy executed for {amount:.2f} {self.base_asset}.")

        def execute_sell(self, amount):
            print(f"Mock sell executed for {amount:.2f} {self.base_asset}.")

    # Example usage
    fetcher = MockPriceFetcher()
    executor = MockTransactionExecutor()
    strategy = PairTradingStrategy(fetcher, executor)

    for _ in range(10):  # Simulate 10 market checks
        strategy.analyze_market()
        time.sleep(1)
