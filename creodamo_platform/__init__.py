from .trading import TradingBot
from .utils import ConfigurationValidator, Logger

class CreoDAMO:
   def __init__(self, config):
      self.config = config
      self.logger = Logger()
      self.config_validator = ConfigurationValidator()  
      self.trading_bot = TradingBot(config)

   def run(self):
      if self.config_validator.validate(self.config):
         self.logger.log("Starting CreoDAMO platform")
         self.trading_bot.execute_trading_strategy()
      else:
         self.logger.log("Invalid configuration")
