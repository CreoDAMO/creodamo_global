# Import necessary modules
from creodamo_platform import TradingBot, DataManager, WebSocketServer

class CreoDAMO:
    def __init__(self, config_file):
        # Initialize logger
        self.logger = Logger()
        try:
            # Validate and load configuration
            self.config = ConfigValidator(config_file).validate()
            # Create instances of TradingBot, DataManager, and WebSocketServer classes
            self.trading_bot = TradingBot(self.config)
            self.data_manager = DataManager(self.config)
            self.websocket_server = WebSocketServer()
        except Exception as e:
            self.logger.error(f"Initialization error: {e}")
            self.config = None

    def run(self):
        if self.config:
            self.logger.info("Starting CreoDAMO")
            # Execute trading strategies using data manager
            self.trading_bot.execute_strategies(self.data_manager)
            # Start WebSocket server
            self.websocket_server.start()
        else:
            self.logger.error("Invalid configuration - Unable to start")
