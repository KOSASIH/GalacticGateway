import sys
import traceback

class ErrorHandling:
    def __init__(self, logger):
        self.logger = logger

    def handle_exception(self, exception):
        self.logger.error('An error occurred: {}'.format(exception))
        self.logger.log_exception(exception)
        self._print_exception_details(exception)

    def _print_exception_details(self, exception):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback, file=sys.stderr)

    def handle_fatal_error(self, exception):
        self.handle_exception(exception)
        sys.exit(1)

# Example usage:
# logger = Logger(logging.INFO)
# error_handler = ErrorHandling(logger)
# try:
#     # Some code that might raise an exception
# except Exception as e:
#     error_handler.handle_exception(e)
