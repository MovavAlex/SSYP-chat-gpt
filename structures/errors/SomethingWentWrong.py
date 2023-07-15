import logging


class SomethingWentWrong(Exception):
    def __init__(self, message):
        super().__init__(message)

    def log_error(self):
        logging.error(f'Something went wrong: {self.args}')
