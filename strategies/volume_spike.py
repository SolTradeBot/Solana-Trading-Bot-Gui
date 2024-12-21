import random
import time

class VolumeSpikeStrategy:
    """
    Implements a volume spike strategy to identify large trading volume surges.
    """

    def __init__(self, price_fetcher, transaction_executor, volume_threshold=10000):
        self.price_fetcher = price_fetcher
        self.transaction_executor = transaction_executor
        self.volume_threshold = volume_threshold  # Minimum volume to trigger trades
        self.price_history = []
        self.volume_history = []

    def simulate_market_data(self):
        """
        Simulates market volume data for testing purposes.
        """
        current_price = self.price_fetcher.get_Ton_price()
        current_volume = random.randint(5000, 20000)  # Simulated trading volume
        return current_price, current_volume

    def analyze_market(self):
        """
        Analyzes volume spikes and executes trades if conditions are met.
        """
        current_price, current_volume = self.simulate_market_data()
        self.price_history.append(current_price)
        self.volume_history.append(current_volume)

        print(f"Current Price: ${current_price:.2f}, Current Volume: {current_volume}")

        if current_volume > self.volume_threshold:
            print("High volume spike detected. Executing buy order.")
            self.transaction_executor.execute_buy(amount=random.uniform(1, 3))
        elif current_volume < self.volume_threshold / 2:
            print("Low volume detected. Executing sell order.")
            self.transaction_executor.execute_sell(amount=random.uniform(1, 3))
        else:
            print("Volume within normal range. No action taken.")

        # Limit the history size for performance
        if len(self.price_history) > 100:
            self.price_history.pop(0)
        if len(self.volume_history) > 100:
            self.volume_history.pop(0)

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
    strategy = VolumeSpikeStrategy(fetcher, executor)

    for _ in range(10):  # Simulate 10 market checks
        strategy.analyze_market()
        time.sleep(1)
