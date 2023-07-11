import logging


class TooManyRequests(Exception):
    def __init__(self, message):
        super().__init__(message)

    def log_error(self):
        logging.error(f'Too many requests: {self.args}')
