import statistics
import random
import time

class MeanReversionStrategy:
    """
    Implements a mean reversion strategy by identifying price deviations from the moving average.
    """

    def __init__(self, price_fetcher, transaction_executor, period=20, deviation_threshold=1.5):
        self.price_fetcher = price_fetcher
        self.transaction_executor = transaction_executor
        self.price_history = []
        self.period = period  # Number of periods for moving average
        self.deviation_threshold = deviation_threshold  # Threshold to trigger trades

    def calculate_moving_average(self):
        """
        Calculates the simple moving average (SMA) of the price history.
        """
        if len(self.price_history) < self.period:
            return None
        return statistics.mean(self.price_history[-self.period:])

    def analyze_market(self):
        """
        Monitors the price and executes trades if the current price deviates significantly from the moving average.
        """
        current_price = self.price_fetcher.get_Ton_price()
        self.price_history.append(current_price)

        if len(self.price_history) > self.period:
            self.price_history.pop(0)

        moving_average = self.calculate_moving_average()
        if moving_average is None:
            print("Not enough data to calculate moving average. Waiting for more price data.")
            return

        deviation = current_price - moving_average
        print(f"Current Price: ${current_price:.2f}, Moving Average: ${moving_average:.2f}, Deviation: ${deviation:.2f}")

        if deviation > self.deviation_threshold:
            print("Price above moving average. Executing sell order.")
            self.transaction_executor.execute_sell(amount=random.uniform(0.5, 2))
        elif deviation < -self.deviation_threshold:
            print("Price below moving average. Executing buy order.")
            self.transaction_executor.execute_buy(amount=random.uniform(0.5, 2))
        else:
            print("Price near moving average. No trade executed.")

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
    strategy = MeanReversionStrategy(fetcher, executor)

    for _ in range(10):  # Simulate 10 market checks
        strategy.analyze_market()
        time.sleep(1)
