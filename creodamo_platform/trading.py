`python
# Import necessary modules
from creodamo_platform.strategies import MovingAverageStrategy

class TradingBot:
    def __init__(self, config):
        # Initialize strategy and configuration
        self.strategy = MovingAverageStrategy()
        self.config = config

    def execute_strategies(self, data_manager):
        # Get latest market data
        market_data = data_manager.get_latest_market_data()
        # Execute strategy and get trades
        trades = self.strategy.execute(market_data, self.config)
        # Execute trades using data manager
        data_manager.execute_trades(trades)
