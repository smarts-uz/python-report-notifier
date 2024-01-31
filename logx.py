import logging
import os
from datetime import datetime


class Logger:
    def __init__(self, module_name, fm, subdirectory=None):
        self.logger = logging.getLogger(module_name)
        formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

        # Creating the log directory based on subdirectory parameter
        log_directory = logger_path(subdirectory)
        self.logger.info(f"Running module {module_name}...")

        # Creating the FileHandler with the log file path
        log_file_path = os.path.join(log_directory, f"{module_name}.log")
        handler2 = logging.FileHandler(log_file_path, mode=fm, encoding='utf-8')
        handler2.setFormatter(formatter)
        self.logger.addHandler(handler2)

    def log(self, message):
        self.logger.setLevel(logging.DEBUG)
        self.logger.info(message)

    def err(self, err):
        self.logger.setLevel(logging.ERROR)
        self.logger.exception(err)


def logger_path(subdirectory = None):
    year, month, day = datetime.now().year, datetime.now().month, datetime.now().day

    # Appending the subdirectory to the logger path if specified
    logger_path = f"C:/Report-Logs/logs/{year}/{month}/{day}/"
    if subdirectory:
        logger_path = os.path.join(logger_path, subdirectory)

    # Creating the directory if it doesn't exist
    if not os.path.exists(logger_path):
        os.makedirs(logger_path)
    return logger_path