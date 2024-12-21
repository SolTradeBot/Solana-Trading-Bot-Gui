import random
import time

class GridStrategy:
    """
    Implements a grid trading strategy, placing buy and sell orders at predefined price intervals.
    """

    def __init__(self, price_fetcher, transaction_executor, grid_size=0.5):
        self.price_fetcher = price_fetcher
        self.transaction_executor = transaction_executor
        self.grid_size = grid_size  # Price difference to trigger trades
        self.grid_levels = []
        self.initialize_grid()

    def initialize_grid(self):
        """
        Sets up initial grid levels for trading.
        """
        base_price = self.price_fetcher.get_Ton_price()
        self.grid_levels = [
            base_price - self.grid_size * i for i in range(5, 0, -1)
        ] + [
            base_price + self.grid_size * i for i in range(1, 6)
        ]
        print(f"Initialized grid levels: {self.grid_levels}")

    def analyze_market(self):
        """
        Monitors the current price and executes trades if a grid level is crossed.
        """
        current_price = self.price_fetcher.get_Ton_price()
        print(f"Current Price: ${current_price:.2f}")

        for level in self.grid_levels:
            if abs(current_price - level) < self.grid_size / 2:
                self.execute_trade(current_price, level)
                break

    def execute_trade(self, current_price, grid_level):
        """
        Executes a buy or sell trade based on the direction of the price movement.
        """
        if current_price > grid_level:
            print(f"Crossed upward grid level at ${grid_level:.2f}. Executing sell order.")
            self.transaction_executor.execute_sell(amount=random.uniform(0.5, 1.5))
        else:
            print(f"Crossed downward grid level at ${grid_level:.2f}. Executing buy order.")
            self.transaction_executor.execute_buy(amount=random.uniform(0.5, 1.5))

        # Remove the triggered grid level and add a new one to maintain the grid
        self.grid_levels.remove(grid_level)
        new_level = grid_level + self.grid_size if current_price > grid_level else grid_level - self.grid_size
        self.grid_levels.append(new_level)
        self.grid_levels.sort()
        print(f"Updated grid levels: {self.grid_levels}")

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
    strategy = GridStrategy(fetcher, executor)

    for _ in range(10):  # Simulate 10 market checks
        strategy.analyze_market()
        time.sleep(1)
