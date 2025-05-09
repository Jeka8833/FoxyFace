import logging
import sys


class LoggerWriter:
    def __init__(self, level):
        # self.level is really like using log.debug(message)
        # at least in my case
        self.level = level

    def write(self, message):
        # if statement reduces the amount of newlines that are
        # printed to the logger
        if message != '\n':
            self.level(message)

    def flush(self):
        # create a flush method so things can be flushed when
        # the system wants to. Not sure if simply 'printing'
        # sys.stderr is the correct way to do it, but it seemed
        # to work properly for me.
        self.level(sys.stderr)


class LoggerManager:
    @staticmethod
    def init(root_level: int = logging.INFO):
        root_logger = logging.getLogger()
        root_logger.setLevel(root_level)

        file_handler = logging.FileHandler("latest.log", mode="w")
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) [%(threadName)s]: %(message)s"))
        file_handler.setLevel(logging.INFO)
        root_logger.addHandler(file_handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter("[%(levelname)s]: %(message)s"))
        console_handler.setLevel(logging.NOTSET)
        root_logger.addHandler(console_handler)

        # Looks ugly in the terminal
        log = logging.getLogger('std')
        sys.stdout = LoggerWriter(log.info)
        sys.stderr = LoggerWriter(log.error)