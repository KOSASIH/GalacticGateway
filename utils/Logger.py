import logging
import os
import datetime

class Logger:
    def __init__(self, log_level=logging.INFO):
        self.log_level = log_level
        self.logger = logging.getLogger('GalacticGateway')
        self.logger.setLevel(self.log_level)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create a file handler
        self.file_handler = logging.FileHandler('galactic_gateway.log')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

        # Create a console handler
        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def log_exception(self, exception):
        self.logger.exception(exception)

# Example usage:
# logger = Logger(logging.DEBUG)
# logger.info('Galactic Gateway initialized')
