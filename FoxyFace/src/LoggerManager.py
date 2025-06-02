import logging
import sys


class LoggerWriter:
    def __init__(self, level):
        self.level = level

    def write(self, message):
        if message != '\n':
            self.level(message)

    def flush(self):
        self.level(sys.stderr)


class LoggerManager:
    @staticmethod
    def init(root_level: int = logging.INFO):
        root_logger = logging.getLogger()
        root_logger.setLevel(root_level)

        file_handler = logging.FileHandler("latest.log", mode="w", encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(
            u"%(asctime)s [%(levelname)s] %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) [%(threadName)s]: %(message)s"))
        file_handler.setLevel(logging.INFO)
        root_logger.addHandler(file_handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter(u"[%(levelname)s]: %(message)s"))
        console_handler.setLevel(logging.NOTSET)
        root_logger.addHandler(console_handler)

        # Looks ugly in the terminal
        log = logging.getLogger('std')
        sys.stdout = LoggerWriter(log.info)
        sys.stderr = LoggerWriter(log.error)
