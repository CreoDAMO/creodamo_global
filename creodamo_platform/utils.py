import logging
from config import AppConfig

class Logger:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('CreoDAMO')

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

class ConfigValidator:

    def __init__(self):
        self.config = AppConfig()
        self.schema = self.config.get_setting('CONFIG_SCHEMA')

    def validate(self, config):
        return True
